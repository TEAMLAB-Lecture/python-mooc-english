# Lab #2 - Simple Calculation (basic_operations)
Copyright 2019 © document created by TeamLab.Gachon@gmail.com

## Introduction
Congratulation! If you are reading this text in the second week, it means that you have the willpower of attending this class. I really appreciate your effort and please keep it until the end of the class.
In this lab, we will solve simple calculation of python. Calculation does not mean just arithmetic such as sum and subtract but also strings and basic data type from python and we will learn how to handle those calculations.  
From this week, I will not explain in detail for Lab Assignment. As the class goes further, there will be less description and guideline. However, it will not be that difficult doing yourself, so don’t be scared of it.

## Assignment file (lab_2.zip) download
Firstly, we have to download the assignment file. It will not be difficult as we have already practiced how to download. Enter the below address in the address window of your Chrome or Explorer.
[https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_2/lab_2.zip](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_2/lab_2.zip)

Click `View Raw`  or  `Download` button to download. Or if you just click the below download link, it will start download automatically. [Lab 2 - Download](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_2/lab_2.zip)

Move the downloaded lab_2.zip file to work folder and start the assignment.
Tip. From now you have to be accustomed of using vocabulary for work condition.


Classification           | Description
--------       | ---
Console    | In windows, console is the black screen which can be displayed by entering “cmd" in the run dialog box, and in Ubuntu and Linux, it means the ‘terminal’ and we will learn in depth next week.  
Python Shell    | Python Shell is a screen which is displayed after entering ‘python’ in Console and we can use various commands of python on it.  
Atom editor       | (Atom editor) in this lesson, the python code files will be edited on the base of Atom editor.

## Types of functions for editing
Let’s see the extracted `basic_operations.py` assignment file. The code is a little bit long but the fundamental structure is the same as `arithmetic_function.py` of lab 1. The functions for editing in this assignment are the following.

Functions           | Description
--------       | ---
str_to_int      | A function which changes string values to an integer data type
str_to_float    | A function which changes string values to a real data type
number_to_str   | A function which changes integer or real data values to a string value
add_string_number   | A function which links a string value and a number value to a string value
add_string_string   | A function which links a string value and a string value to a single string value
associative_law_add | A function which returns the result of sum values in number type such as (a + b) + c
associative_law_mutiple | A function which returns the result of multiply values in number type such as (a * b) * c
distributive_law    | A function which returns the result value in number type using distribute law such as a * (b + c)
exponent    | A function which returns result value of exponent calculation after receiving a base and exponent
For example, all the functions have the same structure as below.
```python
# Data type conversion ================================================
def str_to_int(string_number):
    # """
    #   Input:
    #   -string_number: digits of string
    # Output:
    #   -integer: integer value
    # Examples:
    #   >>> str_to_int("3")
    #   3
    #   >>> str_to_int("135")
    #   135
    # """
    # ===Modify codes below=================
    result = None

    # ======================================

    return result
```

`def str_to_int(string_number)` on the top of the function, we can see ‘def’ which is a reserved word and `str_to_int` is the name of this function. `:` on the last is the basic grammar and from the below `:` to the indent line is the function part.

From below to `# ===Modify codes below=================`, it describes the function such as input variable, output variable, examples for result verification. The examples are written of only those functions names and input value for displaying those in a simple way but in real execution in `python shell`, it must be written as follows. Also, remember that in order to enter `python shell`, you need to input a command called `python`. Enter as below in `python shell` after editing the current code adjusted for this lab.

```python
>>> import basic_operations as bo
>>> bo.str_to_int("3")
3
```
The first line of the above code `import basic_operations as bo` is a command for module `basic_operations`  and it means that we are going to use  `import basic_operations` module with the name of `bo`. I will explain about the module next time. Today, we just need to know that the name of the module is the same as the name of our writing file. `bo.str_to_int("3")` on the below is the command to execute functions of our written program. As we abbreviated `basic_operations` to `bo`, we can execute the function with the name of `bo`. If there is no `as bo ` on the command’s first line, you can execute it by `basic_operations.str_to_int("3")`. As you know, `str_to_int` is the name of the function and you must enter the values according to the function. As we had decided to enter a single value called `string_number` when declaring which can be seen in `str_to_int(string_number)`, we only entered a single value of `("3")` on the test text. If I had entered other values such as  `("3","4")`, we would have seen an error message.

Let’s edit 9 functions according to their purposes.


## Test after edit
Let’s see if we did correctly the lab assignment. We do not need to test after editing all the functions. You can test each function every time when there is editing. The default code for test will be included as below in the `main` function. There are a lot of contents, so we will just see the test code on the top of the function.
```python
def main():
    print("Str_to_int Test")
    print(str_to_int("56"))  # Expected Result: 56
    print("====> ", str_to_int("27") == 27)  # Expected Result: True
    print("Str_to_int Test Closed \n")

    print("str_to_float Test")
    print(str_to_float("8.4501"))  # Expected Result: 8.4501
    print("====> ", str_to_float("3.4") == 3.4)  # Expected Result: True
    print(str_to_float("6.74") == 9.8)  # Expected Result: False
    print("Str_to_float Test Closed \n")
    # the rest is omitted
```
Every test code of each function is written between `print` statements which show the start and end. In each test, use `print` statement to show the function result on the screen and see if there is `True` result value next `====> `. The result will be shown as below if you execute the `python basic_operations.py`  code without any change. And don’t forget that the execution must be on the `console `.





```bash
Str_to_int Test
None
====>  False
Str_to_int Test Closed

str_to_float Test
None
====>  False
False
Str_to_float Test Closed
# the rest is omitted
```

If you re-execute it with `python basic_operations.py` command after changing each function, you will see the result as below.
```bash
Str_to_int Test
56
====>  True
Str_to_int Test Closed

str_to_float Test
8.4501
====>  True
False
Str_to_float Test Closed
# the rest is omitted
```

You can change any codes in `main` functions. Adding more numbers for test or deleting unnecessary tests does not affect the submission of the assignment. For your information, you can add `#` on the code as below in order to not execute the code.

```python
def main():
    #print("Str_to_int Test")
    #print(str_to_int("56"))  # Expected Result: 56
    #print("====> ", str_to_int("27") == 27)  # Expected Result: True
    #print("Str_to_int Test Closed \n")
```
Of course, the code will start working if you remove `#`. `#` is a reserved word for describing something by commenting without executing. Usually, this is used for adding description of the code by the developer but in case of implementing tests, we can add it on the code to control the tests. When you enter `python basic_operations.py` after editing all codes, it will show 9 times of `====>  True`. If there is `====>  False`, it means that those are not edited correctly, so you have to check again.

## Assignment submission
If you had a difficult time on the first week, you would complete this assignment easily. However, it will be the last time explaining the way to submit the assignment in detail. For Windows, you must follow the following for assignment submission.  
- Press `windows`+`r` and enter cmd and click OK.
- Change directory to working folder.
- Enter below code on cmd window.
```bash
python submit.py
```
After entering above command, you will see the screen as below with Login ID and Password. Enter Login ID and password which we used for registering http://theteamlab.io website.

```bash
== Submmting solutions | arithmetic_function.py
Login ID:
Password :
```

If there is no grammar error in program while executing this command, you will receive assignment submission verification message as below.


```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
   add_string_number |       PASS |             Good Job
   add_string_string |       PASS |             Good Job
associative_law_mutiple |       PASS |             Good Job
       number_to_str |       PASS |             Good Job
          str_to_int |       PASS |             Good Job
            exponent |       PASS |             Good Job
        str_to_float |       PASS |             Good Job
 associative_law_add |       PASS |             Good Job
    distributive_law |       PASS |             Good Job
-------------------- | ---------- | --------------------
```

## Next Work
Some people might have done it really simply and easily. Actually it is not that different from the Lab 1 in the way of doing the assignment. I’m sure that the next Labs will be very difficult but don’t worry as we have slack and TA.

> **Human knowledge belongs to the world** - from movie 'Password' -
