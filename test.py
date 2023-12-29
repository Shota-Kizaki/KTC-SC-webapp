import urllib.parse
from sqlalchemy import create_engine, text  # textを追加
import os
from dotenv import load_dotenv

load_dotenv(override=True)

server = os.environ.get('db_host')
database = os.environ.get('db_name')
username = os.environ.get('db_user')
password = os.environ.get('db_pas')

odbc_connect = urllib.parse.quote_plus(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD=' + password)
engine = create_engine('mssql+pyodbc:///?odbc_connect=' + odbc_connect)

with engine.connect() as conn:
    # SQL文をtextオブジェクトでラップ
    sql = text('SELECT @@VERSION as version')
    rs = conn.execute(sql)
    for row in rs:
        print(row[0])  # 最初の列の値を取得
