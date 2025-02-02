from lib.count_words import *

def test_no_words():
   result = count_words("")
   assert result == 0

def test_multiple_words():
   result = count_words("I love goint to the cinema")
   assert result == 6

def test_white_space():
   result = count_words(" ")
   assert result == 0