# Marshall Feguson - 1/2022

# Imports

import sqlite3
from sqlite3 import Error

# Function Definitions

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Connection to SQLite DB successful')
    except Error as e:
        print(f'The error {e} occurred')

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query executed successfully')
    except Error as e:
        print(f'The error {e} occurred')

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'The error {e} occurred')

# Create Connection to DB

connection = create_connection("C:\\Users\\Marshall\\Documents\\projects\\fitness-tracker\\testing\\test_DB\\test_DB.sqlite")