from lib.make_snippet import *

def test_string_with_five_words():
    result = make_snippet("I will go to market")
    assert result == "I will go to market"

def test_string_with_less_than_five_words():
    result = make_snippet("I love you")
    assert result == "I love you"

def test_string_with_more_than_five_words():
    result = make_snippet("I want to go to the market")
    assert result == "I want to go to..."

def test_empty_string():
    result = make_snippet("")
    assert result == ""