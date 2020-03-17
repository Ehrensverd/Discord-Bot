import os
import psycopg2
from dotenv import load_dotenv

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
            # Print propertiies of connection
            print(connection.get_dsn_parameters(), '\n')
    
            # Query Function to be called
            query_function = func(cursor, *args, **kwargs)

        except (Exception, psycopg2.Error) as error :
            print('Error connecting to PSQL: ', error)

        finally:
            # close db connection
            if (connection):
                cursor.close()
                connection.close()
                print('PSQL connection closed')
        return query_function
    return wrapper_connection_

@db_connector
def test(cursor):
    print('Start of test')
    cursor.execute('SELECT version();')
    record = cursor.fetchone()
    print('You are connected to: ', record, '\n')


@db_connector
def select(cursor):
    cursor.execute('SELECT * FROM filmer ;')
    record = cursor.fetchall()
    print("Print each row and it's columns values")
    for row in record:
        print("id = ", row[0], )
        print("Title = ", row[1])
        print("year  = ", row[2])
        print("Country = ", row[3], )
        print("genre= ", row[4])
        print("time  = ", row[6], "\n")

