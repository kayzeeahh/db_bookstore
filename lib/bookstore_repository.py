from lib.bookstore import Bookstore

class Bookstore_Repository:
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        bookstore = []
        for row in rows:
            item = Bookstore(row["id"], row["title"], row["author_name"])
            bookstore.append(item)
        return bookstore
        