import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///myDatabase.db')
conn = engine.connect()
metadata = sqlalchemy.MetaData()

books = sqlalchemy.Table('books', metadata,
  sqlalchemy.Column('book_id', sqlalchemy.Integer, primary_key=True),
  sqlalchemy.Column('book_name', sqlalchemy.Text),
  sqlalchemy.Column('book_author', sqlalchemy.Text),
  sqlalchemy.Column('book_year', sqlalchemy.Integer),
  sqlalchemy.Column('book_is_taken', sqlalchemy.Boolean, default=False)
)
metadata.create_all(engine)
insertion_query = books.insert().values([
  {'book_name': 'Бесы', 'book_author': 'Фёдор Достоевский', 'book_year': 1872},
  {'book_name': 'Старик и море', 'book_author': 'Эрнест Хемингуэй', 'book_year': 1952}
])
conn.execute(insertion_query)

select_all_query = sqlalchemy.select(
    books.c.book_id,
    books.c.book_name,
    books.c.book_author,
    books.c.book_year,
    books.c.book_is_taken
)
select_all_results = conn.execute(select_all_query)
print(select_all_results.fetchall())
