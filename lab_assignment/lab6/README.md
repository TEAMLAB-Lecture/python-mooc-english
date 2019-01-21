# Lab #6 - Factorial Calculator (factorial_calculator)
Copyright 2019 © document created by TeamLab.Gachon@gmail.com

## Introduction
In this Lab, we will handle control in the main function for the first time. Until now, we just have edited simple unit functions or written a program for a single use by editing main function a little. In this Lab, we will write main function using Loop and if statement to be consistently implemented until entering a specific value by a user. It might be difficult at first but as time goes, you will know that it is one of the simplest lab assignments. Let’s start working on it with pleasure.

## Assignment template file download
First of all, you have to download the assignment template file. Please enter the below address on your Chrome or Explorer’s address bar.

https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_6/lab_6.zip

Click View Raw or Download button for downloading. Or click [Lab 6 – download link](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_6/lab_6.zip) and it will start download automatically. Move the downloaded lab_4.zip file to work folder and start the assignment after unzip the file.

## Factorial Calculator Overview
To understand a factorial calculator which is the object of this assignment, we need to understand what factorial means first. Factorial means the result of multiplying all natural numbers from 1 to n. In other words, n factorial means `1 X 2 X 3 X ... X n` and we also can express it with a sign such as `n!`. In case of `5!`, it means 1 X 2 X 3 X 4 X 5` which is `120`. (from Wikipedia). For more detail, see the [factorial page of Wikipedia][1].


![Factorial Mathematics ](https://upload.wikimedia.org/math/6/3/a/63a0817e426d92a89470f75c4ad5bd0a.png)

The actual program which we need to execute is the following.

![Program execution screen shot](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_8_factorial_calculator/factorial_calculator_screen_shot.png)

This program can be executed with three instructions.
1. The program prints the factorial value after calculating the entered natural numbers by a user. In other words, if a user enters `5`, `120` must be displayed on the next line.
2. If a user enters other characters besides natural numbers and 0, it will print `Input again, Please` for new input.
3. When a user enters 0, the program finishes showing a message `Thank you for using this program`.

The logic itself is very simple and it can be executed with the information we have learned before. However, as it is the first assignment for Control, you can feel very difficult. In this Lab, I gonna explain it in detail, so please read this document with care.

## factorial_calculator.py file Overview
Open `factorial_calculator.py` using `atom` to overview.
When you open the file, you can see `main` function and `is_positive_number`, `get_factorial_value` functions.
The list of functions for editing in this Lab is the same as below.




Function           | Description
--------       | ---
is_positive_number| Receives a syntax value and returns True if the corresponding value can be converted to a natural number and False if it cannot.
get_factorial_value| Receives a natural number and returns the factorial value result of that corresponding natural number. In other words, when 5 has entered, it will display 120.
main| Prints factorial values on the screen by receiving values from a user. As described on "Factorial Calculator Overview" instructions, the program will be ended if you enter 0 and it will request to re-enter if you enter a value that is not a natural number.

Let’s see the method of writing each function.

## Edit is_positive_number function
The first function is `is_positive_number` function. It has already been written as below. A comment is included in actual codes but I omitted for explanation at this time.
```python
def is_positive_number(integer_str_value):
    # comment omitted
    try:
        # ===Modify codes below=============
        # must delete 'pass' before executing
        pass

        # ==================================
    except ValueError:
        return False
```
The part we need to edit is the `pass` part. You can see `try ~ excpet ValueError` but it is a "Exception Handling" syntax which is not necessary to know yet. Don’t care about it as I give you basic template for writing lab. The role of this function is to return False unconditionally if type conversion is not possible. For example, in case of trying `int("abc")` function with a string of `"abc"`, it returns only False in the function.

The fundamental purpose of this function is to verify whether the entered value is a natural number or not. This function is entered using `integer_str_value`. Please write a condition statement using `if` for verifying whether  `integer_str_value` is a natural number after deleting `pass` part according to the indentation. As you know already, natural number means an “integer above 1”.
In other words, this function

1. Converts the entered integer_str_value to a value of an integer type.
2. Verify whether the converted value is a natural number.
3. If it is returns True and if not returns False.

If it is not possible to convert into an integer, it automatically returns `False` due to `try ~ catch` statement. Now let’s write a code according to the purpose above.

## Write get_factorial_value function
The second function is `get_factorial_value`. This function returns corresponding factorial value after receiving a natural number of `integer_value`. As it only receives numbers converted to a natural number, you do not need to verify the entered value like the above `is_positive_number`  function.
There are many methods to find a factorial value, but I think using ‘for statement’ is the best way to do. It is the simplest way of multiplying from 1 to a `integer_value` in case of using a for statement. Just remember that in case of writing a for statement using integer values, you must write using `range(1,integer_value+1)` as values in `range(integer_value)` starts from 0.  Well, it is true that there are a lot of ways for finding factorial values. Therefore, it does not matter whether students use the above mentioned method if the entered `integer_value` returns a factorial value.


## Edit main function
The last function is the `main` function. The template of the `main` function is the same as follows.

```python
def main():
    user_input = 999
    # ===Modify codes below=============

    # ==================================
```

Note. The methods explained in this Lab are just one way of implementing the assignment. Therefore, if you have any other ways to achieve the object, you may use your own method. The below explanation is a guideline for execution. You cannot write codes correctly if there is no understanding of loop or if statements. So, please start writing a code after understanding the guideline.
The `main` function starts with `user_input = 999`.The `user_input` is the variable which receives values entered by the user. If you think that `user_input` is not necessary, you can delete it. `user_input = 999` is for while statement. In this lab, the end condition for while statement is 0 as explained below. Therefore, I assigned `999` to `user_input` for the first initialization.
As I already have explained before, if there is no a specific number of repeats for ending in Loop statement, it would be a good choice to use a `while` statement. It has a condition that “it ends when the user enters 0”, so you would start the statement with `while(user_input is not 0):`.
The first thing you need to do after executing `while` statement is to receive values from the user. You can use `input("Input a positive number : ")` statement for entering and the entered value will be assigned to `user_input` variable.
For the next step, use if statement and `is_positive_number` function to verify whether you can calculate the factorial value of entered values. While using `if is_positive_number(user_input):`, it returns `True` when the entered value is a natural number and ‘False’ if it is not a natural number.
- If the returned value is `True`, it converts the `user_input` value to an integer and returns a factorial value of user_input using `get_factorial_value` function and displays it on screen.
- If the returned value is `False`, it verifies whether the corresponding value is `'0'` and ends the program if it is. In order to do this, use a syntax such as `elif user_input is '0':` and make `user_input = 0` for the condition. This will make the program end according to the condition of `while` statement.  Of course, you must display a string `Thank you for using this program` before ending the program.
- If the converted value is `False` but `user_input` is not `0`, a string saying `Input again, Please` will be displayed on the screen. In this case, use `else:` statement if you are not meaning the above conditions. The program will work continuously if `user_input` is not '0'.  

The above explanation is very complicate and it would be very hard to you to execution if you are not well understood of `if`, `while` statements. Therefore, you must practice and repeat the lesson several times for executing.

## Print result
You can see the `python factorial_calculator.py` as below when your code is completely written. Of course, you need to enter all values for users for executing.

```python
Input a positive number : 10
3628800
Input a positive number : 3
6
Input a positive number : 5
120
Input a positive number : abc
Input again, Please
Input a positive number : ls
Input again, Please
Input a positive number : 32.3
Input again, Please
Input a positive number : 0
Thank you for using this program
```

## Submit your assignment
All lab assignment has completed. Let’s submit it.
- Press `windows`+`r` and enter cmd and click OK.
- Change directory to working folder.
- Enter below code on cmd window.

```python
python submit.py
```

After entering above command, you will see the screen as below with Login ID and Password. Enter Login ID and password which we used for registering http://theteamlab.io website.

```python
== Submmting solutions | factorial_calculator.py
Login ID:
Password :
```
Note. You can submit lab assignment any time. And you will be able to see the below message if it is correctly written.

```python
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
 get_factorial_value |       PASS |             Good Job
                main |       PASS |             Good Job
  is_positive_number |       PASS |             Good Job
-------------------- | ---------- | --------------------
```  


## Next Work
Congratulation. It is the first time you actually making a program for executing. `while`, `if`, `for` in this Lab are used in all programs we frequently use such as web browser, excel, power point, etc. You may feel too hard and challenging but in reality, it is a simple assignment. Trust me and next week you will experience what the hell looks like.

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes


[1]: https://ko.wikipedia.org/wiki/%EA%B3%84%EC%8A%B9
