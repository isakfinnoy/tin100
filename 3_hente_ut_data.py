import sqlite3 
from sqlite3 import Error 

connection = sqlite3.connect("database.db")  # Kobler til databasen vi opprettet i 1_lage_database.py

print("----------- \n All data:")

sql_query = "SELECT * from sensordata" # Spørring for å hente all data (* = alt)

c = connection.cursor()
c.execute(sql_query) # Utfører kommandoen

rows = c.fetchall() # Henter ut resultatene fra spørringen

# Printer ut en radene 
for row in rows:
    print(row)


print("----------- \n Første 2 punkter i tabellen:")


# Bruk LIMIT 2 for å bare hente ut de 2 første radene i tabellen
sql_query = "SELECT * from sensordata LIMIT 2"

c.execute(sql_query)

rows = c.fetchall()

for row in rows:
    print(row)


connection.close()