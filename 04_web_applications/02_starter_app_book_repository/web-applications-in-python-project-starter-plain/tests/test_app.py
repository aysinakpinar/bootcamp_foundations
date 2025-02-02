# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
# File: tests/test_app.py

# Note: you will need to do this in the starter codebase.

"""
When: I make a GET request to /
Then: I should get a 200 response
"""
def test_get_wave(web_client):
    # We'll simulate sending a GET request to /wave?name=Dana
    # This returns a response object we can test against.
    response = web_client.get('/wave?name=Dana')

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'I am waving at Dana'

"""
When: I make a POST request to /submit
And: I send a name and message as body parameters
Then: I should get a 200 response with the right content
"""
def test_post_submit(web_client):
    # We'll simulate sending a POST request to /submit with a name and message
    # This returns a response object we can test against.
    response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'

# To run these tests (ensure your virtual environment is active first):
# ; pytest tests/test_app.py

# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data = {'names' : 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

def test_post_sort_names_single_name(web_client):
    response = web_client.post('/sort-names', data = {'names' : 'Bora'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Bora'

def test_post_sort_empty_string(web_client):
    response = web_client.post('/sort-names', data = {'names' : ''})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "There is no name to sort."

def test_get_add_name(web_client):
    response = web_client.get('/add-names?names=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'

def test_get_add_multiple_names(web_client):
    response = web_client.get('/add-names?names=Eddie,Aysin')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie, Aysin'

def test_get_add_no_name(web_client):
    response = web_client.get('/add-names?names=')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There is no name to add!'

def test_get_add_multiple_names_and_sort(web_client):
    response = web_client.get('/add-sort-names?names=Eddie,Aysin')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Aysin, Eddie, Julia, Karim'