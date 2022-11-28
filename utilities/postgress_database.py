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
            user=TestData.USERNAME,
            password=TestData.USER_PASSWORD,
            port=TestData.PORT_NUMBER
        )
        print("Database Connection Successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

