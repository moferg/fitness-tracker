# Marshall Feguson - 1/2022

# Imports

import pandas as pd
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

# Define schema for FitNotes table

create_FitNotes_table = """
CREATE TABLE IF NOT EXISTS FitNotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    exercise TEXT NOT NULL,
    category TEXT,
    'weight (lbs)' REAL,
    reps INTEGER,
    distance REAL,
    'distance unit' TEXT,
    time TEXT,
    'volume (lbs)' REAL
);
"""

# Create FitNotes table in test_DB.sqlite

execute_query(connection, create_FitNotes_table)

# Define schema for MyFitnessPal table

create_MyFitnessPal_table = """
CREATE TABLE IF NOT EXISTS MyFitnessPal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    calories REAL,
    'fat (g)' REAL,
    'carbohydrates (g)' REAL,
    'protein (g)' REAL
);
"""

# Create MyFitnessPal table in test_DB.sqlite

execute_query(connection, create_MyFitnessPal_table)

# Define schema for RenPho table

create_RenPho_table = """
CREATE TABLE IF NOT EXISTS RenPho (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    'weight(lb)' REAL,
    bmi REAL,
    'body fat(%)' REAL,
    'bmr(kcal)' REAL,
    'metabolic age' REAL
);
"""

# Create RenPho table in test_DB.sqlite

execute_query(connection, create_RenPho_table)

# Create DataFrames from test_CSV files

df_fitnotes = pd.read_csv("testing\\test_CSVs\\FitNotes_Test_CSV.csv")
df_myfitnesspal = pd.read_csv("testing\\test_CSVs\\MyFitnessPal_Test_CSV.csv")
df_renpho = pd.read_csv("testing\\test_CSVs\\RenPho_Test_CSV.csv")

#print(df_fitnotes.head())
#print(df_myfitnesspal.head())
#print(df_renpho.head())

# Convert DataFrames to SQL tables

df_fitnotes.to_sql(name='FitNotes', con=connection, if_exists='append', index=False)