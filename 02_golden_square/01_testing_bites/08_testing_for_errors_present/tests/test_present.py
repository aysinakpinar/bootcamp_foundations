import pytest
from lib.present import *

def test_contents_is_none_wrap():
    present = Present()
    present.wrap("Aysin")
    assert present.contents == "Aysin"
    
def test_contents_is_not_none_wrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.wrap("Aysin")
        present.wrap("Bora")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_contents_none_unwrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_wrap_unwrap():
    present = Present()
    present.wrap("Aysin")
    result = present.unwrap()
    assert result == "Aysin"
