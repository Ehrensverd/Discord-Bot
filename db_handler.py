import asyncio
import os
from random import randint

import psycopg2
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
env_pw = os.getenv('DB_PW')



def db_connector(func):
    def wrapper_connection_(*args, **kwargs):
        try:
            connection = psycopg2.connect(user='testbot',
                                          password=env_pw,
                                          host='localhost',
                                          port='5432',
                                          database='test')

            cursor = connection.cursor()
            # Query Function to be called
            query_function = func(cursor, *args, **kwargs)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error connecting to PSQL: ', error)
            connection.rollback()
        finally:
            # close db connection
            if (connection):
                cursor.close()
                connection.close()
        return query_function
    return wrapper_connection_


@db_connector
def insert_user(cursor, user_tuple):
    """Takes a discord user object and inserts it to db table discord_users"""
    print('Inserting : ', user_tuple, 'into db')
    postgres_insert_query = """ INSERT INTO discord_users (user_id, username, discriminator, user_nick) VALUES (%s,%s,%s,%s) ON CONFLICT DO NOTHING"""
    cursor.execute(postgres_insert_query, user_tuple)
    postgres_insert_query = """ INSERT INTO score (user_id) VALUES ((SELECT user_id from discord_users WHERE user_id=%s)) ON CONFLICT DO NOTHING"""
    cursor.execute(postgres_insert_query, (user_tuple[0],))


@db_connector
def update_member(cursor, member_tuple):
    """ Updates name, nick or discriminator of existing member by id"""
    cursor.execute('SELECT * FROM discord_users where user_id=%s', (member_tuple[0],))
    parameters = (member_tuple[1], member_tuple[2], member_tuple[3], member_tuple[0])
    postgres_update_query = """ UPDATE discord_users set username = %s, discriminator = %s, user_nick = %s where user_id=%s"""
    cursor.execute(postgres_update_query, parameters)
    cursor.execute(""" SELECT * FROM discord_users where user_id=%s""", (member_tuple[0],))


@db_connector
def select_all_members(cursor):
    """Returns all members of db table discord_users"""
    cursor.execute('SELECT * FROM discord_users ;')
    return cursor.fetchall()


@db_connector
def find_member_id(cursor, user_id):
    """finds and returns member as tuplet. None if not found"""
    postgres_select_query = """ SELECT * FROM discord_users WHERE user_id =%s"""
    user_id_to_select = (user_id,)
    cursor.execute(postgres_select_query, user_id_to_select)
    return cursor.fetchone()


@db_connector
def activate_ping_event(cursor):
    """Activates an ping event and deactivates previous once"""
    cursor.execute(""" UPDATE ping_events set active=FALSE where active=TRUE""")
    cursor.execute(""" UPDATE ping_events set ping_time=(%s), active=TRUE  where ping_id IN( SELECT max(ping_id) FROM ping_events);""", (datetime.now().astimezone() + timedelta(seconds=0.5),))



@db_connector
def insert_ping_event(cursor, timestamp):
    """Inserts an  ping event and refreshes score table fields"""
    postgres_insert_query = """ INSERT INTO ping_events (ping_time, active) VALUES (%s,FALSE) ON CONFLICT DO NOTHING"""
    cursor.execute(""" UPDATE score set has_scored=default, daily_score=default;""")

    cursor.execute(postgres_insert_query, (timestamp,))


@db_connector
def query_timestamp_next_ping(cursor):
    #print('Next ping queried')
    cursor.execute("""SELECT ping_time FROM ping_events WHERE ping_id IN(SELECT max(ping_id) FROM ping_events)""")
    return cursor.fetchone()


@db_connector
def query_timestamp_ongoing_ping(cursor):
    #print('Ongoing ping queried')
    cursor.execute("""SELECT ping_time FROM ping_events WHERE active=TRUE""")
    return cursor.fetchone()


@db_connector
def query_has_scored(cursor, user):
    #print('Query if member har scored', user)
    postgres_select_query = """SELECT has_scored FROM score WHERE score.user_id=%s """
    cursor.execute(postgres_select_query, (user,))
    return cursor.fetchone()[0]


@db_connector
def insert_score(cursor, delta, user):
    #print("Inserting score", delta, " to users id ", user)
    query_string = """ UPDATE score set has_scored=True, daily_score=(%s), total=total+(%s) where score.user_id=%s """
    cursor.execute(query_string, (int(delta), int(delta), user))
    cursor.connection.commit()
    postgres_select_query = """SELECT total, daily_score FROM score WHERE score.user_id=%s """
    cursor.execute(postgres_select_query, (user,))
    return tuple(str(p) for p in cursor.fetchone())
