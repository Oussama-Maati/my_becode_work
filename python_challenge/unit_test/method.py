class InvalidArgumentException(Exception):
    """Raised when a param is invalid."""

    pass


def addition(number_one: int, number_two: int) -> int:
    if not isinstance(number_one, int) or not isinstance(number_two, int):
        raise InvalidArgumentException("A parameter is not an int!")
    return number_one + number_two


def subtraction(number_one: int, number_two: int) -> int:
    if not isinstance(number_one, int) or not isinstance(number_two, int):
        raise InvalidArgumentException("A param is not an int!")
    return number_one - number_two


from typing import Union


def divide(
    number_one: Union[int, float], number_two: Union[int, float]
) -> Union[float, str]:
    try:
        result = number_one / number_two
    except ZeroDivisionError:
        result = "You can't divide by zero!"
    except Exception as ex:
        result = f"An argument is not an int or a float! -> {ex}"

    return result


import os

def create_test_file():
    file_path = "test.txt"
    file_content = "this is a text"

    # Create the file
    with open(file_path, 'w') as file:
        file.write(file_content)

def delete_test_file():
    file_path = "test.txt"

    # Delete the file
    os.remove(file_path)





