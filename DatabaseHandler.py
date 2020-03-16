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


test()