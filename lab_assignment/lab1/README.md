# Lab #1 – Practice of Arithmetic Function Assignment Submission
Copyright 2019 © document created by teamLab.gachon@gmail.com

## Introduction
In K-MOOC Python and Gachon CS50, all assignment will be submitted using Gachon Autograder made by TeamLab. In this lab, we are going to practice the process of submitting assignment using the autograder system. As we did not learn Python in details yet, we are going to write very simple codes for four fundamental arithmetic operations.

## Download lab_1.zip for Lab Assignment
The first thing we need to do is to download a zip file called "lab_1.zip" for our assignment. Please enter the address below on your web browser such as Chrome or Explorer.  

~~https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/tree/master/lab_assignment/lab_1~~

Click `View Raw`  or  `Download` button to download. Or click the below download link to be download automatically. [Lab 1 - Download](~~https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/raw/master/lab_assignment/lab_1/lab_1.zip~~)

Usually the files are downloaded in the user folder called “Download”

Click <kbd>windows</kbd><sup id="windows"></sup>+<kbd>e</kbd> and you can see the “Download” folder on the upper left corner. In the “Download” folder, click the `lab_1.zip` file to move to the working folder and start working after unzipping the downloaded `lab_1.zip` file



## See the contents of arithmetic_function.py
For the next step, let’s see the structure of unzipped `arithmetic_function.py` file. In order to see the structure, we need to open it using atom as below.
1. Click <kbd>windows</kbd><sup id="windows"></sup>+<kbd>r</kbd> and enter ‘cmd' for a black console window.
2. Use `cd workspace` to change your directory to the working folder.
3. The zip assignment file should be already unzipped in the working folder.
4. Execute atom using the command `atom .` and open the file by clicking `arithmetic_function.py` on the left top menu tree.
5. If it is complicate, please watch the introduction video again.

All assignment is divided into the same three functions.

Classification           | Meaning
--------       | ---
test function      | A function to execute the assignment. A sentence `Modify codes below` is written in the function and the user can edit.
helper function   | A function which is written by the examiner for helping the assignment. Do not need to edit and it would be impossible to submit your assignment if you edit it.
main function       | It is a code for assignment test which is on the bottom of the template and it is written in `def main():`. This code describes the execution result in detail if it is correctly written.

The `arithmetic_function.py` function consists of 4 types of test functions and one main function.  

- addition(a, b) – Return the sum of a and b when those two numbers are entered.
- minus(a, b) – Return the value of a minus b when those two numbers are entered.
- multiplication(a, b) – Return the value of multiplying a and b when those two numbers are entered.
- division(a, b) – Return the value of a divided by b when those two numbers are entered.
The addition function is written as below. addition

```python
def addition(a, b):
    # '''
    # Input:
    #   -a: value of real number (Integer of float)
    #   -b: value of real number (Integer of float)
    # Output:
    #   -sum of two values
    # Examples:
    #   >>> addition(3,5)
    #   8
    #   >>> addition(3,2)
    #   5
    # '''
    # pass
    # ===Modify codes below=============

    result = None

    # ==================================

    return result
```   

The above part of `# ===Modify codes below=============` in this function is the description of the function.

The `# Input:` part describes the type of value in this function and `# Output:` part describes the result value of the function. The most important part is `# Examples:`.

The bottom part describes the result value which can be displayed in execution. In order to verify it, we need to execute Python shell.

Python shell means the programming environment which can be seen when typing `python`. Please enter the below code written after`>>>`

```bash
C:\<working directory\lab_1> python
Type "help", "copyright", "credits" or "license" for more information.
>>> import arithmetic_function as af
>>> result = af.addition(10,5)
>>> print (result)
None
```

The first `import` statement is a command to call the written program. The name of the program, we have made, is "arithmetic_function.py" and please enter the name without `.py` which is the file extension.

`as af` attached on the last part means that we will call `arithmetic_function` as `af`. The second code means that we will call the function of `addition` in the  `arithmetic_function` code.

The corresponding function needs to receive the values for a and b and in this case, a and b will be 10 and 5 respectively. In other words, the result value of `result = af.addition(10,5)` function will be saved as a variable called `result`.

The last code means to print the result of `result`. As we did not edit the code yet, the current value is `None`.

## Edit arithmetic_function.py
The students need to edit the below code. As the object of this function is to add entered two values, change `result = None` to `result = a+b`. Please edit `result = None` of other functions in the same way according to their purposes.

```python
   # ===Modify codes below=============

    result = None

    # ==================================
```
##### In order to verify whether it is correctly edited, execute the edited program.
1. Click <kbd>windows</kbd><sup id="windows"></sup>+<kbd>r</kbd> and click O.K after entering cmd.
2. Change the directory to the previous working folder.
3. Enter `python arithmetic_function.py`.

The executing code is the below code which is in the `main()` function.

The `print` statement is a command to print the values between parenthesis. The below code prints a phrase `Addition Test` first and will print the result of `addition(3,5)` for the next.
Each expectation value for print is written in a comment <sup id="comment"></sup> besides the symbol
`#`.

Verify whether the result values when executing the edited program for the assignment are the same as the expectation values which are commented in the `main()` function.
As the `main()` function do not affect the submission of assignment `main()`, you can edit it freely if you want to.  

```python
def main():
    print ("Addition Test")
    print (addition(3,5)) # Expected Result: 8
    print (addition(10,5) == 15) # Expected Result: True
    print ("Addition Test Closed \n")


    print ("Minus Test")
    print (minus(3,5)) # Expected Result: -2
    print (minus(10,5) == 5) # Expected Result: True
    print (minus(10,15) == 5) # Expected Result: False
    print ("Addition Test Closed \n")

    print ("Multiplication Test")
    print (multiplication(3,5)) # Expected Result: 15
    print (multiplication(10,5) == 50) # Expected Result: True
    print (multiplication(10,-3) == 20) # Expected Result: False
    print ("Addition Test Closed \n")

    print ("division Test")
    print (division(5,5)) # Expected Result: 1
    print (division(5,4)) # Expected Result: 1.25
    print (division(10,5) == 2) # Expected Result: True
    print (division(10,-3) == 0.33333) # Expected Result: False
    print ("division Test Closed \n")
```

## Assignment template file submission
1. Click <kbd>windows</kbd><sup id="windows"></sup>+<kbd>r</kbd> and click O.K after entering cmd on it.
2. Change the directory to the previous working folder.
3. Enter bash as below.
```bash
python submit.py
```

When entering the above command, you will be asked of your Login ID and Password. Use the Login ID and Password used for the registering http://theteamlab.io  website for entering.

```bash
== Submmting solutions | arithmetic_function.py
Login ID:
Password :
```

If there are no grammar errors on executing the command, you will receive a message as below.

```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
            division |       PASS |             Good Job
               minus |       PASS |             Good Job
      multiplication |       PASS |             Good Job
            addition |       PASS |             Good Job
-------------------- | ---------- | --------------------
```


## Next Work
Congratulation for finishing the firs Lab Assignment. I know you are tired of doing tasks. However, we still have a lot of interesting Lab Assignment. You can do it, trust me.
> **Human knowledge belongs to the world** - from movie 'Password' -
