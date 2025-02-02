from lib.diary import Diary
from lib.diary_entry import DiaryEntry


"""
Integration Test
Given the entries from DiaryEntry class
Adds the entry to the entries list
and count_words method is called from DiaryEntry to count the words.
reading time to read all of the entries is calculated with count_words and wpm attributes.
returns the instance closest to the length of the read entry with a wpm and minutes
"""
"""
Integration Test
Given the entries from DiaryEntry class
Adds the entry to the entries list
"""
def test_adding_single_entry_to_the_list():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title1", "one, two, three, four")
    diary.add(diary_entry1)
    result = diary.all()
    assert result == [diary_entry1]

def test_adding_multiple_entries_to_the_list():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title1", "one, two, three, four")
    diary_entry2 = DiaryEntry("Title2", "five, six, seven. eight")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.all()
    print(f"diary.all{diary.all()}")
    assert result == [diary_entry1, diary_entry2]

"""
Given 2 different diaary entries
count_words method is called from DiaryEntry to count the words.
"""

def test_diary_count_words():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title1", "one, two, three, four")
    diary_entry2 = DiaryEntry("Title2", "five, six, seven. eight")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.count_words()
    assert result == 8

def test_diary_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title1", "one, two, three, four")
    diary_entry2 = DiaryEntry("Title2", "five, six, seven. eight")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.reading_time(2)
    assert result == 4

def test_find_best_entry_for_reading_time_one_is_more_than_readable():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title1", "one, two, three, four, nine, ten, eleven")
    diary_entry2 = DiaryEntry("Title2", "five, six, seven. eight")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.find_best_entry_for_reading_time(2, 10)
    assert result == diary_entry1

def test_find_best_entry_for_reading_time_both_readable_but_one_of_them_closer():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title1", "one, two, three")
    diary_entry2 = DiaryEntry("Title2", "five, six, seven. eight")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.find_best_entry_for_reading_time(1, 5)
    assert result == diary_entry2

def test_find_best_entry_for_reading_time_equal_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title1", "one, two, three, nine")
    diary_entry2 = DiaryEntry("Title2", "five, six, seven. eight")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.find_best_entry_for_reading_time(1, 5)
    assert result == diary_entry1, diary_entry2

def test_find_best_entry_for_reading_one_empty():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title1", "")
    diary_entry2 = DiaryEntry("Title2", "five, six, seven. eight")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.find_best_entry_for_reading_time(1, 5)
    assert result == diary_entry2

def test_find_best_entry_for_reading_one_empty():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title1", "")
    diary_entry2 = DiaryEntry("Title2", "five, six, seven. eight")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.find_best_entry_for_reading_time(1, 5)
    assert result == diary_entry2

def test_find_best_entry_for_reading_one_more_than_readable():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title1", "one, two, three")
    diary_entry2 = DiaryEntry("Title2", "four, five, six")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.find_best_entry_for_reading_time(1, 2)
    assert result == None

def test_find_best_entry_for_reading_one_both_empty():
    diary = Diary()
    diary_entry1 = DiaryEntry("Title1", "")
    diary_entry2 = DiaryEntry("Title2", "")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.find_best_entry_for_reading_time(1, 2)
    assert result == None