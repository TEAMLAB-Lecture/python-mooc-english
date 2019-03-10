# Lab #1 – Practice of Arithmetic Function Assignment Submission
Copyright 2019 © document created by teamLab.gachon@gmail.com

## Introduction
In K-MOOC Python and Gachon CS50, all assignment will be submitted using Gachon Autograder made by TeamLab. In this lab, we are going to practice the process of submitting assignment using the Autograder system. As we did not learn Python in details yet, we are going to write very simple, four fundamental arithmetic operation codes.

## Download lab_1.zip for Lab Assignment
What we going to do firstly is to download a zip file called "lab_1.zip" for our assignment.
Please enter below address on your web browser such as Chrome or Explorer.  

~~https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/tree/master/lab_assignment/lab_1~~

Click `View Raw`  or  `Download` button to download. Or click the below download link to be download automatically. [Lab 1 - Download](~~https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/raw/master/lab_assignment/lab_1/lab_1.zip~~).

Usually the files are downloaded in the folder called “Download”. 

Press  <kbd>windows</kbd><sup id="windows"></sup>+<kbd>e</kbd> . You can see the “Download” folder on the upper left corner. Move `lab_1.zip` file to your working directory and unzip. Then, start your lab.



## See the contents of arithmetic_function.py
Let’s start with figure out   `arithmetic_function.py` file's structure. 
To see the structure, we need to open `.py` file (which is python script file) using atom (the editor) as below process.

1. Press <kbd>windows</kbd><sup id="windows"></sup>+<kbd>r</kbd> and  type ‘cmd' . You will see black window called `console` or `terminal`.

2. Type command  `cd **directory_name**` to change your directory to the working folder. Lab assignment files should be unzipped in the working folder.

   *Note: `cd ..` is way to back (to parent directory), and `dir`will show what's in your directory. If you saved in D drive, `d:` let you access.

3. Execute atom using the command `atom .` and open the file by clicking `arithmetic_function.py` on the left top menu tree.

4. If it is complicate, watch the introduction video again.

   

All assignment is divided into the same three functions.

Classification           | Meaning
--------       | ---
Test Function      | A function to execute the assignment. A sentence `Modify codes below` is written in the function.<br /> **You can edit this function.** 
Helper Function   | A function written by the examiner for helping the assignment. <br />**Do not edit**. It may be impossible to submit your assignment if you edit it. 
Main function       | It is a code for assessing your code which is on the bottom of the template. It is written in `def main():`. Main Function describes properly written code's execution result. 



The functions in `arithmetic_function.py` file consists of 4 test functions and one main function.  

- `def addition(a, b):` – Return the sum of a and b when those two numbers(a, b) are entered.
- `def minus(a, b):` – Return the value of a minus b when those two numbers (a, b) are entered.
- `def multiplication(a, b):` – Return the value of multiplying a and b when those two numbers are entered.
- `def division(a, b):` – Return the value of a divided by b when those two numbers are entered.



The addition function is written as below. 

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

The above part of `# ===Modify codes below=============` describes about the function. 

`# Input:` part describes the type of value in this function and `# Output:` part describes expected result.  You can reference `# Examples:`, describes the result value displayed in execution. In order to verify it, execute Python shell.



```bash
C:\<working directory\lab_1> python
Type "help", "copyright", "credits" or "license" for more information.
>>> import arithmetic_function as af
>>> result = af.addition(10,5)
>>> print (result)
None
```

Python shell means the programming environment which can be seen when typing `python` on your console (cmd). Test example codes follow after`>>>`.

The first `import` command calls the written program. The name of the program, we have made, is "arithmetic_function.py" . Please enter the file name without file extension (`.py`) .

`as af` in command is alias. It means  : we will call `arithmetic_function` program, and we will call that  as `af`. The second command call the function `addition` in the  `arithmetic_function` file.

The corresponding function must be already coded in file to receive the values. In this case, `a` and `b` in coded file are 10 and 5 respectively. The returned value of `af.addition(10,5)` function will be saved  in variable `result`, stated on left. 

The last code means to print variable  `result`. As we did not edit the code yet, Current value is must be `None` because `def addition():` in `arithmetic_function.py`, it returned `None`.



## Edit arithmetic_function.py
The students need to edit the below code. As the object of this function is to sum entered two values. Change `result = None` to `result = a+b`. 

Please edit `result = None` of other functions in the same way according to their purposes.

```python
   # ===Modify codes below=============

    result = None

    # ==================================
```
##### In order to verify whether it is correctly edited, execute the edited program.
1. Run Console : Press <kbd>windows</kbd><sup id="windows"></sup>+<kbd>r</kbd> and  enter `cmd` on it.
2. Change the directory to the previous working folder.
3. Enter `python arithmetic_function.py`.

Codes in `main()` function will executed.

The `print` statement command to print the values between parenthesis. Below code will prints a phrase `Addition Test`first, then print the result of `addition(3,5)` for the next.
Each expectation value for print is written in the comment follows after <sup id="comment"></sup>  symbol
`#`.

Verify whether the executing result values of edited program for the assignment are the same as the expectation values which are commented in the `main()` function.
As the `main()` function do not affect the Autograder submission of assignment `main()`, you can edit it freely if you want to.  

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

If you properly tested and ready to submit your assignment, follow below directions.

1. Run Console : Press <kbd>windows</kbd><sup id="windows"></sup>+<kbd>r</kbd> and  enter 'cmd'  on it.
2. Change the directory to the previous working folder.
3. Command as below.
```bash
python submit.py
```

When enter the above command, you will be asked your Login ID and Password. Use the Login ID and Password used for the registering http://theteamlab.io  website.

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
Congratulation for finishing the first Lab Assignment. I know you are tired of doing tasks. However, we still have a lot of interesting Lab Assignment. You can do it, trust me.
> **Human knowledge belongs to the world** - from movie 'Password' -
