from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
Integration Test
Given no entries from DiaryEntry class
returns the entry list
"""

def test_empty_diary_list():
    diary = Diary()
    result = diary.all()
    assert result == []

def test_DiaryEntry_count_words():
    diary_entry1 = DiaryEntry("Title1", "one, two, three, four")
    assert diary_entry1._title == "Title1"
    assert diary_entry1._contents == "one, two, three, four"

def test_DiaryEntry_title_and_contents():
    diary_entry1 = DiaryEntry("Title1", "one, two, three, four")
    result = diary_entry1.count_words()
    assert result == 4


