from lib.class_test_drive import *
def test_if_text_starts_with_capital_letter_and_ends_with_ending_punct():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("I want to go home.")
    assert result == True

def test_if_text_starts_with_capital_letter_and_ends_with_ending_punct_multiple_sentence():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("I want to go home.") == True
    assert grammar_stats.check("I want to go home:") == False

def test_percentage_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("I want to go home.")
    grammar_stats.check("I want to go home:")
    assert grammar_stats.percentage_good() == 50

def test_percentage_good_4_cases():
    grammar_stats = GrammarStats()
    grammar_stats.check("I want to go home.")
    grammar_stats.check("I want to go home:")
    grammar_stats.check("I want to go home?")
    grammar_stats.check("I want to go home!")
    assert grammar_stats.percentage_good() == 75

def test_percentage_good_three_cases_one_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("I want to go home.")
    grammar_stats.check("I want to go home:")
    grammar_stats.check("I want to go home")
    assert grammar_stats.percentage_good() == 33

def test_percentage_good_three_cases_two_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("I want to go home.")
    grammar_stats.check("I want to go home:")
    grammar_stats.check("I want to go home?")
    assert grammar_stats.percentage_good() == 67