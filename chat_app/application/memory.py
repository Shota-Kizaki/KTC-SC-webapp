'''import os
from dotenv import load_dotenv
import pyodbc

load_dotenv(override=True)

server = os.environ.get('db_host')
database = os.environ.get('db_name')
username = os.environ.get('db_user')
password = os.environ.get('db_pas')
driver= '{ODBC Driver 18 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP (3) column1, CONVERT(datetime, column2) FROM [dbo].[chat_app_chatlog]")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()'''
import os
from dotenv import load_dotenv
import pyodbc

load_dotenv(override=True)

server = os.environ.get('db_host')
database = os.environ.get('db_name')
username = os.environ.get('db_user')
password = os.environ.get('db_pas')
driver= '{ODBC Driver 18 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        # user_id が 1 のユーザーの最新の3つのデータを取得
        cursor.execute("SELECT TOP (3) id, CONVERT(datetime, created_at) as created_at, question, answer, user_id FROM [dbo].[chat_app_chatlog] WHERE user_id = 1 ORDER BY created_at DESC")
        row = cursor.fetchone()
        while row:
            print("Question: {}, Answer: {}".format(row.question, row.answer))
            row = cursor.fetchone()
