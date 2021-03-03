"""Given two linked lists representing two numbers (integers).
The digits are stored in reverse order, and each of the nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:
Use PHP/Python/Go
Upper Middle / Senior
Linked List functionality should be implemented by you (by creating one or more classes)
Middle
Use any implementation available for the programming language you have picked
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros
Use Git
Add Unit Tests
Upload the solution to a private GutHub repo and send the link"""


def linked_list(list_a, list_b):
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("provided parameters are not lists")
    number_one = convert_to_single_digit(list_a)
    number_two = convert_to_single_digit(list_b)
    result = number_one + number_two
    result = convert_to_list_of_integers(result)
    return result[::-1]


def convert_to_single_digit(number_list):
    number_one = [str(integer) for integer in number_list]
    a_string = "".join(number_one)
    an_integer = int(a_string)
    return an_integer


def convert_to_list_of_integers(number):
    number_one = [int(integer) for integer in str(number)]
    return number_one
