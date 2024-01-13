import os
from dotenv import load_dotenv
import pyodbc
from typing import List

load_dotenv(override=True)

server = os.environ.get('db_host')
database = os.environ.get('db_name')
username = os.environ.get('db_user')
password = os.environ.get('db_pas')
driver = '{ODBC Driver 18 for SQL Server}'

def drop_table(table_name):
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f'DROP TABLE {table_name}')
            cursor.commit()

drop_table("class_data")
drop_table("scholarship_data")
