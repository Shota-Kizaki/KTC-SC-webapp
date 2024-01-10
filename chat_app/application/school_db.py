import os
from dotenv import load_dotenv
import pyodbc

load_dotenv(override=True)

server = os.environ.get('db_host')
database = os.environ.get('db_name')
username = os.environ.get('db_user')
password = os.environ.get('db_pas')
driver = '{ODBC Driver 18 for SQL Server}'


def get_contexts(user_id):
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT TOP (3) id, CONVERT(datetime, created_at) as created_at, question, answer, user_id FROM [dbo].[chat_app_chatlog] WHERE user_id =  {user_id}  ORDER BY created_at DESC")
            row = cursor.fetchone()
            contexts = []
            while row:
                # 存在する属性にアクセスする前にチェック
                if hasattr(row, 'question') and hasattr(row, 'answer'):
                    contexts.insert(0, {
                        'question': row.question,
                        'answer': row.answer
                    })
                    # print("Question: {}, Answer: {}".format(row.question, row.answer))
                row = cursor.fetchone()
    return contexts


def create_table(): # テーブル作成関数
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                '''
                    CREATE TABLE class_data
                    (
                        data_id int primary key NOT NULL,
                        class_name VARCHAR(20) NOT NULL,
                        data text NOT NULL,
                    )
                ''')
            cursor.commit()

create_table()


def insert_data():
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute('')

# insert_data()

def drop_table():
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute('DROP TABLE class_data')
            cursor.commit()

# drop_table()