# Python - Data Structures: Lists, Tuples

## Resources
- [3.1.3 Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data structures](https://docs.python.org/3/tutorial/datastructures.html) (*until `5.3. Tuples and Sequences` included*)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

## Learning Objectives
##### General
- Why Python programming is awesome
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the `del` statement and how to use it


## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Tasks
##### Tasks mandatory
- [x] [**`0-print_list_integer.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/0-print_list_integer.py): *Write a function that prints all integers of a list.*
    - Prototype: `def print_list_integer(my_list=[]):`
    - Format: one integer per line. See example
    - You are not allowed to import any module
    - You can assume that the list only contains integers
    - You are not allowed to cast integers into strings
    - You have to use `str.format()` to print integers

- [x] [**`1-element_at.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/1-element_at.py):*Write a function that retrieves an element from a list like in C.*
    - Prototype: `def element_at(my_list, idx):`
    - If `idx` is negative, the function should return `None`
    - If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
    - You are not allowed to import any module
    - You are not allowed to use `try/except`

- [x] [**`2-replace_in_list.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/2-replace_in_list.py):*Write a function that replaces an element of a list at a specific position (like in C).*
    - Prototype: `def replace_in_list(my_list, idx, element):`
    - If `idx` is negative, the function should not modify anything, and returns the original list
    - If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
    - You are not allowed to import any module
    - You are not allowed to use `try/except`

- [x] [**`3-print_reversed_list_integer.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/3-print_reversed_list_integer.py):*Write a function that prints all integers of a list, in reverse order.*
    - Prototype: `def print_reversed_list_integer(my_list=[]):`
    - Format: one integer per line. See example
    - You are not allowed to import any module
    - You can assume that the list only contains integers
    - You are not allowed to cast integers into strings
    - You have to use `str.format()` to print integers

- [x] [**`4-new_in_list.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/4-new_in_list.py):*Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).*
    - Prototype: `def new_in_list(my_list, idx, element):`
    - If `idx` is negative, the function should return a copy of the original `list`
    - If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
    - You are not allowed to import any module
    - You are not allowed to use `try/except`

- [x] [**`5-no_c.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/5-no_c.py):*Write a function that removes all characters c and C from a string.*
    - Prototype: `def no_c(my_string):`
    - The function should return the new string
    - You are not allowed to import any module
    - You are not allowed to use `str.replace()`

- [x] [**`6-print_matrix_integer.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/6-print_matrix_integer.py):*Write a function that prints a matrix of integers.*
    - Prototype: `def print_matrix_integer(matrix=[[]]):`
    - Format: see example
    - You are not allowed to import any module
    - You can assume that the list only contains integers
    - You are not allowed to cast integers into strings
    - You have to use `str.format()` to print integers

- [x] [**`7-add_tuple.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/7-add_tuple.py):*Write a function that adds 2 tuples.*
    - Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
    - Returns a tuple with 2 integers:
        - The first element should be the addition of the first element of each argument
        - The second element should be the addition of the second element of each argument
    - You are not allowed to import any module
    - You can assume that the two tuples will only contain integers
    - If a tuple is smaller than 2, use the value `0` for each missing integer
    - If a tuple is bigger than 2, use only the first 2 integers

- [x] [**`8-multiple_returns.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/8-multiple_returns.py):*Write a function that returns a tuple with the length of a string and its first character.*
    - Prototype: `def multiple_returns(sentence):`
    - If the sentence is empty, the first character should be equal to `None`
    - You are not allowed to import any module

- [x] [**`9-max_integer.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/9-max_integer.py):*Write a function that finds the biggest integer of a list.*
    - Prototype: `def max_integer(my_list=[]):`
    - If the list is empty, return `None`
    - You can assume that the list only contains integers
    - You are not allowed to import any module
    - You are not allowed to use the builtin `max()`

- [x] [**`10-divisible_by_2.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/10-divisible_by_2.py):*Write a function that finds all multiples of 2 in a list.*
    - Prototype: `def divisible_by_2(my_list=[]):`
    - Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
    - The new list should have the same size as the original list
    - You are not allowed to import any module

- [x] [**`11-delete_at.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/11-delete_at.py):*Write a function that deletes the item at a specific position in a list.*
    - Prototype: `def delete_at(my_list=[], idx=0):`
    - If `idx` is negative or out of range, nothing change (returns the same list)
    - You are not allowed to use `pop()`
    - You are not allowed to import any module

- [x] [**`12-switch.py`**](https://github.com/EduRamos95/holbertonschool-higher_level_programming/blob/master/python-data_structures/12-switch.py):*Complete the source code in order to switch value of `a` and `b`*
    - You can find the source code [`here`](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py)
    - Your code should be inserted where the comment is (line 4)
    - Your program should be exactly 5 lines long

---
##### Author
- Edu Ramos
---
