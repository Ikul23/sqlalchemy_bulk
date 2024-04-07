import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем соединение с базой данных
engine = sqlalchemy.create_engine('sqlite:///myDatabase.db')

# Определяем базовый класс для объявления моделей
Base = declarative_base()

# Определяем модель для таблицы 'books'
class Book(Base):
    __tablename__ = 'books'
    book_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    book_name = sqlalchemy.Column(sqlalchemy.Text)
    book_author = sqlalchemy.Column(sqlalchemy.Text)
    book_year = sqlalchemy.Column(sqlalchemy.Integer)
    book_is_taken = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

# Создаем таблицу 'books' в базе данных
Base.metadata.create_all(engine)

# Создаем сессию для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Добавляем книги в базу данных
books_to_add = [
    Book(book_name='Бесы', book_author='Фёдор Достоевский', book_year=1872),
    Book(book_name='Старик и море', book_author='Эрнест Хемингуэй', book_year=1952)
]
session.add_all(books_to_add)
session.commit()

# Выполняем запрос на выборку всех книг
all_books = session.query(Book).all()

# Выводим результаты запроса
for book in all_books:
    print(f"ID: {book.book_id}, Name: {book.book_name}, Author: {book.book_author}, Year: {book.book_year}, Taken: {book.book_is_taken}")
