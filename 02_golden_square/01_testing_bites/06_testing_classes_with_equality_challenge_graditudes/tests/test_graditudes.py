from lib.graditudes import *

def test_initial_graditude():
    gratitude = Gratitudes()
    result = gratitude.format()
    assert result == "Be grateful for: "

def test_single_graditude():
    gratitude = Gratitudes()
    gratitude.add("your health")
    result = gratitude.format()
    assert result == "Be grateful for: your health"

def test_multiple_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("your health")
    gratitude.add("family")
    gratitude.add("life")
    result = gratitude.format()
    assert result == "Be grateful for: your health, family, life"