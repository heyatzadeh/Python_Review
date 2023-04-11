import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///movies_library.db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

movies = sqlalchemy.Table("Movies", metadata, autoload_with=engine, autoload_replace=True)
select_query = sqlalchemy.select(movies).where(movies.columns.Director == 'Nolan' and movies.columns.Year >= 2015)

result_proxy = connection.execute(select_query)
result_set = result_proxy.fetchall()

print(result_set)

insert_query = movies.insert().values(Title='Interstellar', Director='Nolan', Year=2014)
# connection.execute(insert_query)

result_proxy = connection.execute(select_query)
result_set = result_proxy.fetchall()
print(result_set)
