import sqlite3

with sqlite3.connect("movies_library.db") as connection:
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)
    ''')

    # cursor.execute("INSERT INTO Movies VALUES ('Avatar', 'James Cameron', 2009)")

    # high_earning_movies = [
    #     ("Avengers: Endgame", "Russo Brothers", 2019),
    #     ("Inception", "Nolan", 2015),
    #     ("Memento", "Nolan", 1999)
    # ]

    # cursor.executemany("INSERT INTO Movies VALUES (?,?,?)", high_earning_movies)

    release_year = (2015,)
    records = cursor.execute("SELECT * FROM Movies WHERE Year>=?", release_year)
    # print(cursor.fetchall())
    for record in records:
        print(record)

    connection.commit()
