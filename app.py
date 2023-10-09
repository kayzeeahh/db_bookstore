from lib.database_connection import DatabaseConnection
from lib.bookstore_repository import Bookstore_Repository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/book_store.sql")

# Retrieve all artists
bookstore_repository = Bookstore_Repository(connection)
books = bookstore_repository.all()

# List them out
for books in books:
    print(books)
