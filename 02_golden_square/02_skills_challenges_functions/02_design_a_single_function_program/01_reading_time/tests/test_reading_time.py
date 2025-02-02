
from lib.reading_time import *

"""
if None as argument 
returns 0
"""
def test_reading_time_for_None():
    with pytest.raises(Exception) as e:
        reading_time(None)
    error_message = str(e.value)
    assert error_message == "Can't estimate reading time"

"""
if any text read 
returns 0
"""
def test_reading_time_for_empty_string():
    with pytest.raises(Exception) as e:
        reading_time("")
    error_message = str(e.value)
    assert error_message == "Can't estimate reading time"

"""
if less than 200 words read
returns a float
"""
def test_reading_time_for_less_than_200_words():
    text = " ".join(["word" for i in range(0,200)])
    result = reading_time(text)
    assert result == 1.0

"""
if more than 200 words read
returns a float
"""
def test_reading_time_for_more_than_200_words():
   text = " ".join(["word" for i in range(0,400)])
   result = reading_time(text)
   assert result == 2.0

