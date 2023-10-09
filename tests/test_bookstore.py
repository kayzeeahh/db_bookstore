from lib.bookstore import Bookstore

def test_bookstore_initialised():
    bookstore = Bookstore (1, "test title", "test author_name")
    assert bookstore.id == 1
    assert bookstore.title == "test title"
    assert bookstore.author_name == "test author_name"

def test_bookstore_is_equal():
    bookstore1 = Bookstore(1, "test title", "test author_name")
    bookstore2 = Bookstore(1, "test title", "test author_name")
    assert bookstore1 == bookstore2
    
def test_bookstore_format():
    bookstore = Bookstore(1, "test title", "test author_name")
    assert str(bookstore) == "Bookstore(1, test title, test author_name)"

