"""
    Stacks:

    Question 1: Implement a function is_balanced(expression) that takes a string 
    containing parentheses, curly braces, and square brackets,and determines whether 
    the expression is balanced. 

    An expression is considered balanced if each opening bracket has a corresponding closing 
    bracket in the correct order.

    sample input = 

    expression1 = "([]{})"
    expression2 = "([)]"
    print(is_balanced(expression1))  # Output: True
    print(is_balanced(expression2))  # Output: False
"""
from collections import deque

def is_balanced(expression):
    stack = deque()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            if stack[-1] == bracket_pairs[char]:
                stack.pop()
     
    return len(stack) == 0

expression1 = "({)"

print(is_balanced(expression1))