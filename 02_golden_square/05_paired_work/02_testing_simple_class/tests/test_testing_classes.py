from lib.high_value import *

def test_second_value_higher():
    high_value = HighValue(1, 2)
    result = high_value.get_highest()
    assert result == "Second value is higher"
    
def test_first_value_higher():
    high_value = HighValue(3,2)
    result = high_value.get_highest()
    assert result == "First value is higher"

def test_values_equal():
    high_value = HighValue(4, 4)
    result = high_value.get_highest()
    assert result == "Values are equal"

def test_increasing_first_number():
    high_value = HighValue(4, 4)
    high_value.add(2,"first" )
    result = high_value.get_highest()
    assert result == "First value is higher"

def test_increasing_second_number():
    high_value = HighValue(5, 5)
    high_value.add(3, "second")
    result = high_value.get_highest()
    assert result == "Second value is higher"

def test_increasing_equal():
    high_value = HighValue(2, 5)
    high_value.add(3, "first")
    result = high_value.get_highest()
    assert result == "Values are equal"

def test_increasing_equal_2():
    high_value = HighValue(6, 2)
    high_value.add(4, "second")
    result = high_value.get_highest()
    assert result == "Values are equal"

def test_becomes_higher():
    high_value = HighValue(6, 2)
    high_value.add(5, "second")
    result = high_value.get_highest()
    assert result == "Second value is higher"

def test_becomes_higher_first():
    high_value = HighValue(1, 2)
    high_value.add(5, "first")
    result = high_value.get_highest()
    assert result == "First value is higher"