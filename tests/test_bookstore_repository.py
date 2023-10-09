from lib.bookstore_repository import Bookstore_Repository
from lib.bookstore import Bookstore 

def test_getting_all_book(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = Bookstore_Repository(db_connection)
    
    bookstore = repository.all()
    
    assert bookstore == [
        Bookstore(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Bookstore(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Bookstore(3, 'Emma', 'Jane Austen'),
        Bookstore(4, 'Dracula', 'Bram Stoker'),
        Bookstore(5, 'The Age of Innocence', 'Edith Wharton'),

    ]
