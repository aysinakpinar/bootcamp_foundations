# Tests for your routes go here

# === Example Code Below ===

"""
GET /books
returns list of a books
"""
def test_get_books(web_client, db_connection):
    db_connection.seed('seeds/book_store.sql')
    response = web_client.get("/books")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Book(1, Invisible Cities, Italo Calvino)\n" \
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" \
        "Book(3, Bluets, Maggie Nelson)\n" \
        "Book(4, No Place on Earth, Christa Wolf)\n" \
        "Book(5, Nevada, Imogen Binnie)"
    
"""
GET /books/<id>
returns  single book
"""
def test_get_single_book(web_client, db_connection):
    db_connection.seed('seeds/book_store.sql')
    response = web_client.get("/books/1")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Book(1, Invisible Cities, Italo Calvino)"

"""
POST /books
creates a book 
"""
def test_post_book(web_client, db_connection):
    db_connection.seed('seeds/book_store.sql')
    response = web_client.post("/books", data = {
        'title': 'LOTR',
        'author_name': 'Tolkien'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Book created successfully."

    response = web_client.get('/books')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Book(1, Invisible Cities, Italo Calvino)\n" \
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" \
        "Book(3, Bluets, Maggie Nelson)\n" \
        "Book(4, No Place on Earth, Christa Wolf)\n" \
        "Book(5, Nevada, Imogen Binnie)\n" \
        "Book(6, LOTR, Tolkien)"
    
"""
DELETE /books/<id>
deletes the specified book
"""
def test_delete_book(web_client, db_connection):
    db_connection.seed('seeds/book_store.sql')
    response = web_client.delete('/books/6')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Book successfully removed'

    response = web_client.get('/books')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Book(1, Invisible Cities, Italo Calvino)\n" \
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" \
        "Book(3, Bluets, Maggie Nelson)\n" \
        "Book(4, No Place on Earth, Christa Wolf)\n" \
        "Book(5, Nevada, Imogen Binnie)"
    
    """
    PATCH /books/<id>
    updates the book
    
    """
def test_patch_book(web_client, db_connection):
    db_connection.seed("seeds/book_store.sql")
    response = web_client.patch('/books/5', data = {
        'title': 'LOTR',
        'author_name': 'Tolkien'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Book 5 has been updated"

    response = web_client.get('/books')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Book(1, Invisible Cities, Italo Calvino)\n" \
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" \
        "Book(3, Bluets, Maggie Nelson)\n" \
        "Book(4, No Place on Earth, Christa Wolf)\n" \
        "Book(5, LOTR, Tolkien)"
