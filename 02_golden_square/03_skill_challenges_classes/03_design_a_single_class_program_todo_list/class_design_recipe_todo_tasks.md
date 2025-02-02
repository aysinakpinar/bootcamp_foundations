# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list._

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TodoList():

    def __init__(self):
        self._to_do_list = []
        # saves the initial list as a self object
        # starts with an empty list
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #  the new list with the added task
        # Side-effects
        #   Saves the task to the self object
        #   Throws an exception if there is nothing to add(empty string)
        pass # No code here yet

    def mark_completed(self, completed_task):
        # Returns:
        #   A list of remaining tasks
        # Side-effects:
        #   Throws an exception if no task completed. 
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task
#add_task adds the task to the to do list
"""
to_do_list = TodoList()
to_do_list.add("Walk the dog")

"""
Given no task
#to_do_list.add raises an exception
"""
to_do_list = TodoList()
to_do_list.add("") # raises an error with the message "No task to add to the list."

"""
Given the completed task
#The task is removed from the list. 
"""
to_do_list = TodoList()
to_do_list.mark_completed("Walk the dog")

"""
Given the completed task
#The task is not in the list. throws an exception.
"""
to_do_list = TodoList()
to_do_list.mark_completed("Go for a walk") # raises an error with the message "This task is not in your to do list."

"""
Given the completed task
#There is no task to mark completed(Empty string was given as completed task). Throws and exception.
"""
to_do_list = TodoList()
to_do_list.mark_completed("") # raises an error with the message "No completed task detected. To do list wasn't changed."

"""
Given the completed task
#The to do list is empty. throws an exception.
"""
to_do_list = TodoList()
to_do_list.mark_completed("Go for a walk") # raises an error with the message "There is no task in your to do list."



```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
