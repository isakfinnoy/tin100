import sqlite3 # Biblioteket vi skal bruke for å kommunisere med sqlite-databasen
from sqlite3 import Error

# Leser inn en sqlite3-database. Databasen opprettes hvis ikke filen allerede finnes. Dette gjør det mulig å lagre data mellom flere kjøringer
connection = sqlite3.connect("database.db") 

if connection is not None: # Sjekker om opprettelsen av databasen var en suksess

    # Kommando for å lage en tabell som heter sensordata
    # 2 kolonner: 
    # id (som er et integer og er primary key)
    # value (som er et desimaltall og må være oppgitt)

    sql_create_table =  "CREATE TABLE IF NOT EXISTS sensordata (id integer PRIMARY KEY, value real NOT NULL, date int); " 
    try:
        c = connection.cursor()
        c.execute(sql_create_table) # Utfører opprettelsen av en tabell
    except Error as e:
        print(e) # Printer eventuelle feil



connection.close() # Viktig å lukke databasen før programmet avslutter