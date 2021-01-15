import sqlite3 
from sqlite3 import Error 

import random
import pandas as pd
import time

predicted = pd.read_csv('/Users/hariskarovic/Desktop/Datasett TIN100/submit_test.csv')

connection = sqlite3.connect("database.db") # Kobler til databasen vi opprettet i 1_lage_database.py

#sql_insert = "INSERT INTO sensordata (value) VALUES (0.9)" # Eksempel på kommando for å sette inn data

c = connection.cursor()
# c.execute(sql_insert) # Utfører kommanoen
# connection.commit()

date = time.time()

# Setter inn flere rader med en for-løkke
for i in predicted['0']:
    sql_insert = f'INSERT INTO sensordata (value, date) VALUES ({i},{date})'

    c.execute(sql_insert)

connection.commit()
connection.close()