import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///challenge.db")
conn = engine.connect()
metadata = sqlalchemy.MetaData()

students = sqlalchemy.Table(
    'students2', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String),
    sqlalchemy.Column('lastname', sqlalchemy.String),
    sqlalchemy.Column('email_address', sqlalchemy.String),
)

metadata.create_all(engine)

peoples = [
    (1, "Hossein", "Heyatzadeh", "hossein9697@gmail.com"),
    (2, "ali", "ahmadvand", "ali@gmail.com"),
    (3, "majid", "abedini", "majid@gmail.com"),
    (4, "mehdi", "behzadi", "mehdi@gmail.com")
]

select_query = sqlalchemy.select(students.columns.email_address)
insert_query = sqlalchemy.insert(students).values(peoples)

# conn.execute(insert_query)
result_proxy = conn.execute(select_query)
result_set = result_proxy.fetchall()
print(result_set)
conn.commit()
