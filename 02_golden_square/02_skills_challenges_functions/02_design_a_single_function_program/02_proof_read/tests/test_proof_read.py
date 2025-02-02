from lib.proof_read import *
import pytest
"""
if the text starts with a Capital and ends with "."
returns True
"""
def test_if_text_starts_with_a_capital_and_ends_with_dot():
    result = proof_read("I want to go to the cinema.")
    assert result == True

"""
if the text starts with a Capital and ends with "?"
returns True

"""
def test_if_text_starts_with_a_capital_and_ends_with_question_mark():
    result = proof_read("Do you want to join me?")
    assert result == True
"""
if the text starts with a Capital and ends with "!"
returns True

"""
def test_if_text_starts_with_a_capital_and_ends_with_exclamation_mark():
    result = proof_read("I will shout hello!")
    assert result == True

"""
if the text starts with not a Capital and ends with "."
returns False

proof_read("i want to go to the cinema.") => False
"""
def test_if_text_starts_with_not_a_capital_and_ends_with_dot():
    result = proof_read("i want to go to the cinema.")
    assert result == False

"""
if the text starts with not a Capital and ends with "?"
returns False

proof_read("do you want to join me?") => False
"""
def test_if_text_starts_with_not_a_capital_and_ends_with_question_mark():
    result = proof_read("do you want to join me?")
    assert result == False

"""
if the text starts with not a Capital and ends with "!"
returns False

proof_read("i will shout hello!") => False
"""
def test_if_text_starts_with_not_a_capital_and_ends_with_exclamation_mark():
    result = proof_read("i will shout hello!")
    assert result == False
"""
if the text starts with a Capital and ends with ":"
returns False

proof_read("I want to go to the cinema:") => False
"""
def test_if_text_starts_with_a_capital_and_ends_with_colon():
    result = proof_read("I want to go to the cinema:")
    assert result == False
"""
if the text starts with a not Capital and ends with ":"
returns False

proof_read("i want to go to the cinema:") => False
"""
def test_if_text_starts_with_not_a_capital_and_ends_with_colon():
    result = proof_read("i want to go to the cinema:")
    assert result == False

"""
if the text starts with a Capital and ends with ","
returns False

proof_read("I want to go to the cinema,") => False
"""
def test_if_text_starts_with_a_capital_and_ends_with_comma():
    result = proof_read("I want to go to the cinema,")
    assert result == False
"""
if the text starts with a Capital and ends with " "
returns False

proof_read("I want to go to the cinema ") => False
"""
def test_if_text_starts_with_a_capital_and_ends_with_white_space():
    result = proof_read("I want to go to the cinema ")
    assert result == False

"""
if the text is empty throws the error message "No text to proof read"

proof_read("") => "No text to proof read"
"""
def test_if_text_is_empty_string():
    with pytest.raises(Exception) as e:
        proof_read("")
    error_message = str(e.value)
    assert error_message == "No text to proof read"