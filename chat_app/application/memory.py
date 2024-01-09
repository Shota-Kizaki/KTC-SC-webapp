import os
from dotenv import load_dotenv
import pyodbc

load_dotenv(override=True)

server = os.environ.get('db_host')
database = os.environ.get('db_name')
username = os.environ.get('db_user')
password = os.environ.get('db_pas')
driver= '{ODBC Driver 18 for SQL Server}'
def get_contexts(user_id):
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT TOP (3) id, CONVERT(datetime, created_at) as created_at, question, answer, user_id FROM [dbo].[chat_app_chatlog] WHERE user_id =  {user_id}  ORDER BY created_at DESC")
            row = cursor.fetchone()
            contexts_input = []
            contexts_output = []
            while row:
                # 存在する属性にアクセスする前にチェック
                if hasattr(row, 'question') and hasattr(row, 'answer'):

                    contexts_input.insert(0, row.question)
                    contexts_output.insert(0, row.answer)
                    # print("Question: {}, Answer: {}".format(row.question, row.answer))
                row = cursor.fetchone()
            contexts = [contexts_input, contexts_output]
    return contexts
