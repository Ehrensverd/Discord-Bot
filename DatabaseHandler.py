import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
env_pw = os.getenv('DB_PW')




def db_connector(func):
    def wrapper_connection_(*args, **kwargs):
        try:
            print('ihappen')
            connection = psycopg2.connect(user='testbot',
                                          password=env_pw,
                                          host='localhost',
                                          port='5432',
                                          database='test')
            cursor = connection.cursor()
            # Print propertiies of connection
            print(connection.get_dsn_parameters(), '\n')
    
            # Print PSQL version

            query_function = func(cursor, *args, **kwargs)
            record = cursor.fetchone()
            print('You are connected to: ', record, '\n')


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
    return cursor.execute('SELECT version();')

@db_connector
def select(cursor):
    cursor.execute('SELECT * FROM filmer ;')
    record = cursor.fetchall()
    print("Print each row and it's columns values")
    for row in record:
        print("id = ", row[0], )
        print("Title = ", row[1])
        print("year  = ", row[2])
        print("Coounry = ", row[3], )
        print("genre= ", row[4])
        print("time  = ", row[6], "\n")
    return cursor.execute('SELECT * FROM filmer ;')




test()

select()
