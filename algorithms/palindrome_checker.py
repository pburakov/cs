from abstract_data_types.deque import Deque


def is_palindrome(string):
    """
    Classic palindrome checker using Deque data type.
     Returns True if string is a correct palindrome.
    """
    deque = Deque(string)

    while deque.size() > 1:
        first = deque.remove_front()
        last = deque.remove_rear()

        if first != last:
            return False

    return True


print(is_palindrome('radar'))
print(is_palindrome('foo'))
print(is_palindrome('ooffoo'))
print(is_palindrome('something'))
