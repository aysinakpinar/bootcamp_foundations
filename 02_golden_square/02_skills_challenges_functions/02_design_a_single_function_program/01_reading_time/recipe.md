# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def reading_time(read_text):
    """calculates the estimate of reading time for a text.

    Parameters: (list all parameters and their types)
        read_text: read text(a string containing words (e.g. "hello WORLD"))

    Returns: reading time float

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
if None as argument 
returns 0
"""
reading_time(None) => 0

"""
if any text read 
returns 0
"""
reading_time("") => 0

"""
if less than 200 words read
returns a float
"""
reading_time("Follow the design recipe to implement the following user stories in your project. User stories follow a specific format — don't worry about that too much now, you'll get the hang of it.") => 0.16


"""
if more than 200 words read
returns a float
"""
reading_time("Follow the design recipe to implement the following user stories in your project. User stories follow a specific format — don't worry about that too much now, you'll get the hang of it Follow the design recipe to implement the following user stories in your project. User stories follow a specific format — don't worry about that too much now, you'll get the hang of it Follow the design recipe to implement the following user stories in your project. User stories follow a specific format — don't worry about that too much now, you'll get the hang of it Follow the design recipe to implement the following user stories in your project. User stories follow a specific format — don't worry about that too much now, you'll get the hang of it Follow the design recipe to implement the following user stories in your project. User stories follow a specific format — don't worry about that too much now, you'll get the hang of it Follow the design recipe to implement the following user stories in your project. User stories follow a specific format — don't worry about that too much now, you'll get the hang of it Follow the design recipe to implement the following user stories in your project. User stories follow a specific format — don't worry about that too much now, you'll get the hang of it") => 1.12


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
