from lib.single_class_test_drive import *

def test_format_diary_entry():
    diary_entry = DiaryEntry("Aysin's Diary", "Reading, walking")
    result = diary_entry.format()
    assert result == "Aysin's Diary: Reading, walking."

def test_count_words_of_entry():
    diary_entry = DiaryEntry("Aysin's Diary", "Reading, walking")
    result = diary_entry.count_words()
    assert result == 4

def test_reading_time_of_the_content():
    diary_entry = DiaryEntry("Aysin's Diary", "Reading, walking")
    result = diary_entry.reading_time(2)
    assert result == 1

def test_reading_chunk_two_wpm_one_min_one_time():
    diary_entry = DiaryEntry("Aysin's Diary", "one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"

def test_reading_chunk_two_wpm_one_min_two_times():
    diary_entry = DiaryEntry("Aysin's Diary", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"

def test_reading_chunk_two_wpm_one_min_three_times():
    diary_entry = DiaryEntry("Aysin's Diary", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"

def test_reading_chunk_two_wpm_one_min_two_times_and_one_wpm_one_min():
    diary_entry = DiaryEntry("Aysin's Diary", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(1, 1) == "three"
    assert diary_entry.reading_chunk(2, 1) == "four five"

def test_reading_chunk_multiple_cycles():
    diary_entry = DiaryEntry("Aysin's Diary", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(2, 2) == "five six"
    assert diary_entry.reading_chunk(2, 2) == "one two three four"

def test_reading_chunk_multiple_cycles_with_exact_numbers():
    diary_entry = DiaryEntry("Aysin's Diary", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
    assert diary_entry.reading_chunk(2, 2) == "one two three four"

#    diary_entry.format()
#    diary_entry.count_words()
#    diary_entry.count_words()
#    diary_entry.reading_time(150)
#    diary_entry.reading_chunk(150, 60)