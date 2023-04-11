import sqlite3

with sqlite3.connect('challenge.db') as conn:
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students
    (
    student_id INT NOT NULL, 
    first_name VARCHAR(45) NULL, 
    last_name VARCHAR(45) NULL,
    email_address TEXT NULL,
    PRIMARY KEY ('student_id')
    )
    ''')

    peoples = [
        (1, "Hossein", "Heyatzadeh", "hossein9697@gmail.com"),
        (2, "ali", "ahmadvand", "ali@gmail.com"),
        (3, "majid", "abedini", "majid@gmail.com"),
        (4, "mehdi", "behzadi", "mehdi@gmail.com")
    ]

    # cursor.executemany("INSERT INTO students VALUES (?,?,?,?)", peoples)
    values = cursor.execute("SELECT email_address FROM students")
    print(values.fetchall())

    conn.commit()
