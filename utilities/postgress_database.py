import psycopg2
import pandas as pd
from psycopg2 import Error
from configuration.config import TestData


def create_database_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            host=TestData.HOST_NAME,
            database=TestData.DATABASE_NAME,
            user=TestData.USER_NAME,
            password=TestData.USER_PASSWORD,
            port=TestData.PORT_NUMBER
        )
        print("Database Connection Successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def execute_commit_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("query Successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


results = read_query(create_database_connection(), TestData.query1)
from_db = []
for result in results:
    result = list(result)
    from_db.append(result)
columns = ["Emp_ID", "Emp_Name", "Emp_Address", "Emp_DOJ", "EMP_Department"]
df = pd.DataFrame(from_db,  columns = columns)
print(df)






