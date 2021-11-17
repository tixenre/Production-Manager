import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection   

conn = create_connection("database.sqlite")

c=conn.cursor()

def create_tables():
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS _3mf (
                id text PRIMARY KEY,  
                name text,
                description text,
                size real,
                price real,
                time real,
                gr real,
                instances_per_buildplate real,
                filament text,
                printer text,
                cm3 real,
                path text,
                last_updated text
                )""")


create_tables()

# def copy_table_from_db_to_db(from_,to_):
#     """Dont forget to select the table!!"""
#     df=pd.read_sql('SELECT * FROM investment_deposits', sqlite3.connect(from_))
#     df.to_sql("investment_deposits",sqlite3.connect(to_),index=False,if_exists="append")


# def delete_table(delete=False):
#     if delete == True:
#         with conn:
#             c.execute("DROP TABLE investment_portfolio")


# def delete_last_row(delete=False):
#     if delete == True:
#         with conn:
#             c.execute("DELETE FROM investment_logs WHERE date = (SELECT MAX(date) FROM investment_logs)")


# def read():
#     """Dont forget to select the table!!"""
#     df=pd.read_sql('SELECT * FROM investment_deposits WHERE investment_id = (SELECT "f001" FROM investment_deposits)', sqlite3.connect("database.sqlite"))
#     print(df)

# read()

# copy_table_from_db_to_db("database_o.sqlite","database.sqlite")
# create_tables()
# delete_last_row(delete=True)