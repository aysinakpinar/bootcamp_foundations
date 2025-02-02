
# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie


# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```


# sorting the strings route
GET /add-names
  names: comma separated string
  
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE


# GET /add-names?names=Eddie
#  Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""

# GET /add-names?names=Eddie,Aysin
#  Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie, Aysin
"""

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /add-names
  Expected response (200 OK):
  Julia, Alice, Karim, Eddie
"""
def test_get_add_name(web_client):
    response = web_client.get('/add-names?names=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'

"""
GET /add-names
  Expected response (200 OK):
  Julia, Alice, Karim, Eddie
"""
def test_get_add_multiple_names(web_client):
    response = web_client.get('/add-names?names=Eddie,Aysin')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie, Aysin'

"""
GET /add-names
  Expected response (200 OK):
  Julia, Alice, Karim, Eddie
"""
def test_get_add_empty(web_client):
    response = web_client.get('/add-names', data = {'names' : ''})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There is no name to add!'

```

