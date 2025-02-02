from lib.report_length import *

def test_report_length():
    result = report_length("Aysin")
    assert result == "This string was 5 characters long."

def test_report_lenth():
    result = report_length("")
    assert result == "This string was 0 characters long."

