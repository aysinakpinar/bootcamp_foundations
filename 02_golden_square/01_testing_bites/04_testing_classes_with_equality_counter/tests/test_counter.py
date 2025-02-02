from lib.counter import *
def test_counter_to_0():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."
    
def test_counter_to_2():
    counter = Counter()
    counter.add(2)
    result = counter.report()
    assert result == "Counted to 2 so far."

def test_counter_to_100():
    counter = Counter()
    counter.add(100)
    result = counter.report()
    assert result == "Counted to 100 so far."

def test_counter_add_multiple_numbers():
    counter = Counter()
    counter.add(100)
    counter.add(150)
    result = counter.report()
    assert result == "Counted to 250 so far."