#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """ Divides element by element 2 lists.
    If 2 elements can’t be divided, the division result should be equal to 0
    If an element is not an integer or float:
    print: wrong type
    If the division can’t be done (/0):
    print: division by 0
    If my_list_1 or my_list_2 is too short
    print: out of range

    Args:
        my_list_1: The first integer.
        my_list_2: The second integer.
        list_length: Integer number.
    Returns:
         A new list (length = list_length) with all divisions
    """
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
