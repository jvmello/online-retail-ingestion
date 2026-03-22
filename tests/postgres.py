import psycopg2

conn = psycopg2.connect(
    host="postgres",
    database="lakehouse",
    user="postgres",
    password="postgres"
)

print("Connected")