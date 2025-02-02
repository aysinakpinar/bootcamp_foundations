from lib.greet import *

def test_greet():
    result = greet("Aysin")
    assert result == "Hello, Aysin!"