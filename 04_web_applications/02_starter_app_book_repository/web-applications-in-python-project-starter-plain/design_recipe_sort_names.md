
# Request:
POST http://localhost:5001/sort-names

# With body parameters:
names=Joe,Alice,Zoe,Julia,Kieran

# Expected response (sorted list of names):
Alice,Joe,Julia,Kieran,Zoe


# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```


# sorting the strings route
POST /sort-names
  names: comma separated string
  
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# POST /sort-names
#  Expected response (200 OK):
"""
Alice,Joe,Julia,Kieran,Zoe
"""
# POST /sort-names
#  Expected response (200 OK):
"""
Alice,Joe,Julia,Kieran,Zoe
"""

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
POST /sort-names
  Expected response (200 OK):
  Alice,Joe,Julia,Kieran,Zoe
"""
def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data = {'names' : 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
POST /sort-names
  Expected response (200 OK):
  single name Bora
"""
def test_post_sort_single_name(web_client):
    response = web_client.post('/sort-names', data = {'names' : 'Bora'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Bora'

"""
POST /sort-names
  Expected response (200 OK):
  empty string
  raise exception
"""
def test_post_sort_empty_string(web_client):
    response = web_client.post('/sort-names', data = {'names' : ''})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "There is no name to sort"

```

