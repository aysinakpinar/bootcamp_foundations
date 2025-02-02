from lib.string_builder import *

def test_initial_string():
    string_builder = StringBuilder()
    result = string_builder.output()
    assert result == ""

def test_string_builder_single_string():
    string_builder = StringBuilder()
    string_builder.add("aysin")
    string_builder.size()
    result = string_builder.output()
    assert result == "aysin"

def test_string_size_of_the_string():
    string_builder = StringBuilder()
    string_builder.add("aysin")
    string_builder.size()
    result = string_builder.size()
    assert result == 5

def test_adding_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("Hello Aysin!")
    string_builder.add(" ")
    string_builder.add("How are you today?")
    result = string_builder.output()
    assert result == "Hello Aysin! How are you today?"

def test_size_of_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("Hello Aysin!")
    string_builder.add(" ")
    string_builder.add("How are you today?")
    result = string_builder.size()
    assert result == 31