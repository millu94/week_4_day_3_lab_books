import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Ian", "Rankin")
author_repository.save(author_1)
book_1 = Book("In a House of Lies", "Detective", author_1)
book_repository.save(book_1)
book_3 = Book("Exit Music", "Detective", author_1)
book_repository.save(book_3)

author_2 = Author("Dj", "Dribbler")
author_repository.save(author_2)
book_2 = Book("Harry's Kebab House", "Rave-Nostalgia", author_2)
book_repository.save(book_2)

pdb.set_trace()