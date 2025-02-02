# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def proof_read(text):
    """checks a text if it starts with a Capital and ends with a sentence ending punctuation mark (. ? !).

    Parameters: (list all parameters and their types)
        text: gets a text as a string
    Returns: 
        True if the text starts with a Capital and ends with an appropriate punctuation mark. Else returns False

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
if the text starts with a Capital and ends with "."
returns True
"""
proof_read("I want to go to the cinema.") => True

"""
if the text starts with a Capital and ends with "?"
returns True
"""
proof_read("Do you want to join me?") => True

"""
if the text starts with a Capital and ends with "!"
returns True
"""
proof_read("I will shout hello!") => True

"""
if the text starts with not a Capital and ends with "."
returns False
"""
proof_read("i want to go to the cinema.") => False

"""
if the text starts with not a Capital and ends with "?"
returns False
"""
proof_read("do you want to join me?") => False

"""
if the text starts with not a Capital and ends with "!"
returns False
"""
proof_read("i will shout hello!") => False

"""
if the text starts with a Capital and ends with ":"
returns False
"""
proof_read("I want to go to the cinema:") => False

"""
if the text starts with a not Capital and ends with ":"
returns False
"""
proof_read("i want to go to the cinema:") => False

"""
if the text starts with a Capital and ends with ","
returns False
"""
proof_read("I want to go to the cinema,") => False

"""
if the text starts with a Capital and ends with " "
returns False
"""
proof_read("I want to go to the cinema ") => False

"""
if the text is empty throws the error message "No text to proof read"
"""
proof_read("") => "No text to proof read"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

