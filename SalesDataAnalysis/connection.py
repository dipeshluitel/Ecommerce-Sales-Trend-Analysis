import pyodbc
from sqlalchemy import create_engine
from cleaning.cleaning import df
import pandas

server = "localhost"
database = "EcommerceDB"
username = "Sa"
password = "admin5"

connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(connection_string)

df.to_sql('SalesData', con=engine,if_exists="replace",index=False)