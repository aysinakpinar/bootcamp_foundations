from lib.class_design_todo_list import TodoList
import pytest
"""
Given a task
#add_task adds single task to the to do list
"""
def test_adding_a_task_to_todo_list():
    to_do_list = TodoList()
    to_do_list.add_task("Walk the dog")
    assert to_do_list.show_list() == "Walk the dog"

"""
# Given a task
# #add_task adds multiple tasks to the to do list
"""

def test_adding_multiple_tasks_to_todo_list():
    to_do_list = TodoList()
    to_do_list.add_task("Walk the dog")
    to_do_list.add_task("Call your mum")
    to_do_list.add_task("Go for a shopping")
    assert to_do_list.show_list() == "Walk the dog, Call your mum, Go for a shopping"

"""
# Given a task
# #add_task adds multiple tasks to the to do list
"""

def test_adding_multiple_tasks_given_one_time_to_todo_list():
    to_do_list = TodoList()
    to_do_list.add_task("Walk the dog, Call your mum, Go for a shopping")
    assert to_do_list.show_list() == "Walk the dog, Call your mum, Go for a shopping"

"""
Given no task
#to_do_list.add raises an exception
"""

def test_adding_no_task_to_todo_list():
    to_do_list = TodoList()
    with pytest.raises(Exception) as err:
        to_do_list.add_task("") # raises an error with the message "No task to add to the list."
    error_message = str(err.value)
    assert error_message == "No task to add to the list."

"""
Given the completed task
#The task is removed from the list. 
"""

def test_removing_a_task_from_todo_list():
    to_do_list = TodoList()
    to_do_list.add_task("Walk the dog")
    to_do_list.add_task("Call your mum")
    to_do_list.add_task("Go for a shopping")
    assert to_do_list.mark_completed("Walk the dog") == "Call your mum, Go for a shopping"

"""
Given the completed task
#The task is not in the list. throws an exception.
"""

def test_removing_a_task_not_in_the_list_from_todo_list():
    to_do_list = TodoList()
    to_do_list.add_task("Walk the dog")
    to_do_list.add_task("Call your mum")
    to_do_list.add_task("Go for a shopping")
    with pytest.raises(Exception) as err:
        to_do_list.mark_completed("Go for a walk")
    error_message = str(err.value)
    assert error_message == "This task is not in your to do list."

"""
Given the completed task
#There is no task to mark completed(Empty string was given as completed task). Throws and exception.
"""

def test_no_completed_task_given_and_gives_an_error():
    to_do_list = TodoList()
    to_do_list.add_task("Walk the dog")
    to_do_list.add_task("Call your mum")
    to_do_list.add_task("Go for a shopping")
    with pytest.raises(Exception) as err:
        to_do_list.mark_completed("")
    error_message = str(err.value)
    assert error_message == "No completed task detected. To do list wasn't changed."

# """
# Given the completed task
# #The to do list is empty. throws an exception.
# """

def test_removing_completed_task_from_an_empty_to_do_list():
    to_do_list = TodoList()
    with pytest.raises(Exception) as err:
        to_do_list.mark_completed("Walk the dog")
    error_message = str(err.value)
    assert error_message == "There is no task in your to do list."
