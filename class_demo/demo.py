import psycopg2

connection = psycopg2.connect(dbname= "example", user="postgres", password= "111988")

cursor = connection.cursor()

cursor.execute('''DROP TABLE IF EXISTS rami_work;''')
cursor.execute('''
    CREATE TABLE rami_work(
        id INTEGER PRIMARY KEY,
        done BOOLEAN NOT NULL DEFAULT FALSE
    );
''')

cursor.execute('''
    INSERT INTO rami_work(id, done) VALUES(1, true);
''')

cursor.execute('''INSERT INTO rami_work(id, done) VALUES(%s, %s);''', (2, True))
sql = '''INSERT INTO rami_work(id, done) VALUES(%(id)s, %(done)s);'''
data = {
    "id" : 3,
    "done" : False
}
cursor.execute(sql, data)

connection.commit()
connection.close()
cursor.close()

