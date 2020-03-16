import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
password = os.getenv('DB_PW')

try:
    connection = psycopg2.connect(user='eskil',
                                  password=password,
                                  host='localhost',
                                  port='5432',
                                  database='test')

    cursor = connection.cursor()
    # Print propertiies of connection
    print(connection.get_dsn_parameters(), '\n')
    
    # Print PSQL version
    cursor.execute('SELECT version();')
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
