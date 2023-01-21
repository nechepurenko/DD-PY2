from typing import List
from pydantic import BaseModel


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:  # TODO написать класс Book
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        if not id_ > 0:
            raise ValueError("Идентификатор книги не может быть равен нулю или быть отрицательным числом")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Навание книги должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if not pages > 0:
            raise ValueError("Количество страниц в книге не может быть равно нулю или быть отрицательным числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id_={self.id_}, name={self.name!r}, pages={self.pages})'


class Library(BaseModel):   # TODO написать класс Library
    books: List[Book] = []

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        return len(self.books) + 1

    def get_index_by_book_id(self, id_: int):
        for i, book in enumerate(self.books, start=1):
            if id_ == i:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
