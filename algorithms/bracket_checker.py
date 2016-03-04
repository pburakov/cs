from abstract_data_types.stack import Stack

"""
Solution for bracket order checker using Stack data type as seen on Checkio.org.
"""


def bracket_checker(expression):
    # Mapping opening and closing brackets. Opening brackets will be in
    # brackets.values() list. Closing brackets will be in brackets.keys() list.
    brackets = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    # Stack of opened brackets in order they're encountered in the string.
    # Successfully closed brackets will be deleted from the stack
    stack = Stack()

    expression.split()

    for char in expression:
        # Bracket was opened
        if char in brackets.values():
            stack.add(char)

        # Bracket was closed
        if char in brackets.keys():
            if stack.is_empty() is False and stack.peek() == brackets[char]:
                # Successful closure - delete last used bracket from the list
                stack.pop()
            else:
                # Exit with False if it's not the same bracket that was opened last
                return False

    # Making sure no brackets left unclosed
    return stack.is_empty() == True


print(bracket_checker("((5+3)*2+1)"))  # True
print(bracket_checker("{[(3+1)+2]+}"))  # True
print(bracket_checker("(3+{1-1)}"))  # False
print(bracket_checker("(({[(((1)-2)+3)-3]/3}-3)"))  # False
print(bracket_checker("2+3"))  # True
