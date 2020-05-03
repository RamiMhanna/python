import psycopg2

connection = psycopg2.connect(dbname= "example", user="postgres", password= "111988")

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE rami_work(
        id INTEGER PRIMARY KEY,
        done BOOLEAN NOT NULL DEFAULT FALSE
    );
''')

cursor.execute('''
    INSERT INTO rami_work(id, done) VALUES(1, true);
''')

connection.commit()
connection.close()
cursor.close()

