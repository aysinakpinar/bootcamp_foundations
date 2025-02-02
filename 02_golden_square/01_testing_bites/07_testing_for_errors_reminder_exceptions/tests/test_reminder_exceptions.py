import pytest
from lib.reminder_exceptions import *

def test_reminder_exceptions():
    reminder = Reminder("Aysin")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"

