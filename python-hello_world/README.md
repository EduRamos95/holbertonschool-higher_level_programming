# Python - Hello, World
---
##### Concepts
- [The Python Tutorial](https://docs.python.org/3.4/tutorial/index.html)
- [Python Programming: An Introduction to Computer Science 3rd edition](https://www.pdfdrive.com/python-programming-an-introduction-to-computer-science-e183602644.html)
- [Derek Banas’ Learn to program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [The Python Guru](https://thepythonguru.com/)
- [New string formatting](https://realpython.com/python-f-strings/)
- [Garbage collector](https://thp.io/2012/python-gc/python_gc_final_2012-01-22.pdf)
- [Python Interpreter](http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html)
- [Python bytecode](https://docs.python.org/3.4/library/dis.html)
---

## Resources
##### Read or watch:
- [The Python tutorial](https://docs.python.org/3/tutorial/index.html) (only the first three chapters below)
- [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
- [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
- [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)(Read up until “3.1.2. Strings” included)
- [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
- [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Learning Objectives
### General
- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name ‘Python’ come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using `print`
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with `pycodestyle`

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md`file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Shell Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`wc -l file` should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be executable

## Pycodestyle
`Pycodestyle` is now the [new standard of Python style code](https://github.com/PyCQA/pycodestyle/issues/466)

### Tasks
##### Tasks mandatory
- [x] `0. Run Python file`:*Write a Shell script that runs a Python script. The Python file name will be saved in the environment variable `$PYFILE`*
- [x] `1. Run inline`:*Write a Shell script that runs Python code. The Python code will be saved in the environment variable `$PYCODE`*
- [x] `2. Hello, print`:*Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.*
    - Use the function print
- [x] `3. Print integer`:*Complete this [`source code`](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.*
    - You can find the source code [`here`](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py)
    - The output of the script should be:
        -  the number, followed by `Battery street`,
        -  followed by a new line
    -  You are not allowed to cast the variable `number` into a string
    -  Your code must be 3 lines long
    -  You have to use f-strings [`tips`](https://realpython.com/python-f-strings/)
- [x] `4. Print float`:*Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.*
    - You can find the source code [`here`](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) 
    - The output of the program should be:
        - `Float:`, followed by the float with only 2 digits
        - followed by a new line
    - You are not allowed to cast `number` to string
    - You have to use f-strings
- [x] `5. Print string`:*Complete this [`source code`](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.*
    -  You can find the source code [`here`](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py)
    -  The output of the program should be:
        - 3 times the value of `str`
        - followed by a new line
        - followed by the 9 first characters of `str`
        - followed by a new line
    - You are not allowed to use any loops or conditional statement
    - Your program should be maximum 5 lines long
- [x] `6. Play with strings`:*Complete this [`source code`](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`*
    -  You can find the source code [`here`](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py)
    -  You are not allowed to use any loops or conditional statements.
    -  You have to use the variables `str1` and `str2` in your new line of code
    -  Your program should be exactly 5 lines long
- [x] `7. Copy - Cut - Paste`:*Complete this [`source code`](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)*
    -  You can find the source code [`here`](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)
    -  You are not allowed to use any loops or conditional statements
    -  Your program should be exactly 8 lines long
    -  `word_first_3` should contain the first 3 letters of the variable `word`
    -  `word_last_2` should contain the last 2 letters of the variable `word`
    -  `middle_word` should contain the value of the variable `word` without the first and last letters
- [x] `8. Create a new sentence`:*Complete this [`source code`](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.*
    - You can find the source code [`here`](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py)
    - You are not allowed to use any loops or conditional statements
    - Your program should be exactly 5 lines long
    - You are not allowed to create new variables
    - You are not allowed to use string literals
- [x] `9. Easter Egg`:*Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.*
    -  Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

##### Tasks advanced
- [x] `10. Hello, write`:*Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.*
- [x] `11. Compile`:*Write a script that compiles a Python script file.*
- [x] `12. ByteCode -> Python #1`:*Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:*


---
##### Author
- Edu Ramos

---
