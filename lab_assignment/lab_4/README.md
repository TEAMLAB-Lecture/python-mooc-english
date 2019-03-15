# Lab #4 - Fahrenheit Converter (fahrenheit_converter)
Copyright 2019 © document created by TeamLab.Gachon@gmail.com

## Introduction
This is the fourth Lab Assignment. This lab guide is shorter and not descriptive. We already practiced how to handle this Fahrenheit converter in class before. However I have adjusted it for the assignment. The feature of this lab is that the students need to write everything themselves including the `main` function. It looks hard but will be easy at the end of the lesson. In this lab, let’s write each function and practice connecting those functions.

## Assignment template file download
First of all, you have to download the assignment template file. Please enter the below address on your Chrome or Explorer’s address bar.

>
>https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_4/lab_4.zip

Click View Raw or Download button for downloading. Or click [Lab 4 – download link ](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_4/lab_4.zip) and it will start download automatically. Move the downloaded lab_4.zip file to work folder and start the assignment after unzip the file.

## fahrenheit_converter.py file Overview
Open `fahrenheit_converter.py` using `atom` to overview the outline. You can see the below code.

```python
# -*- coding: utf-8 -*-


def main():
    print("This program is a conversion program from Celsius to Fahrenheit.")
    print("============================")
    # ===Modify codes below=================

    # ======================================
    print("===========================")
    print("Program has ended.")


if __name__ == '__main__':
    main()
```

There are two things to do. Firstly, you need to write three functions to execute the program. Secondly, you have to execute the fahrenheit converter using three functions written on the `main` function. The code is not written neatly yet and you will complete those blanks.
## Write input_celsius_value value

Let’s start to write three functions first. As we already had written a function in Lab 3, so it might be easy for you. Start writing `input_celsius_value()`  function with below information.

Contents | Composition
--------       | ---
Name of function      | input_celsius_value
input variable (argument) | None
Process  | prints "Enter Celsius degree to convert: " and it will convert entered values to real numbers. We assume that all the users only enter real number type number. 
output value(return value)  | celsius value in Float Type
output value(return value)  | celsius_value in Float Type

You will wonder whether it works well after writing all functions. There are two ways to verify. The first way is commenting out the `main` function in the existing code as below, and add a test code. Open `fahrenheit_converter.py` file using `atom` and change statement in last `if __name__ == '__main__':` as below.

```python
if __name__ == '__main__':
    # main()
    celsius_value = input_celsius_value()
    print(celsius_value)
```

If the functions are correctly entered, you would see the screen as below after executing `python fahrenheit_converter.py` in the console.

```bash
Enter Celsius degree to convert: 15.2
15.2
```
It is nothing more than just displaying the entered value.

You can insert a test code by editing the whole code but you can also test the existing code via `python shell` as we did. Enter `python` on the `cmd` window and execute `python shell` for testing as below.

```python
>>> import fahrenheit_converter as fc
>>> fc.input_celsius_value()
Enter Celsius degree to convert:10
10.0
```

Now I have explained the way to testing in `python shell` and the significance of `import` statement. Therefore, there will be no more explanation.

## Write convert_celsius_fahrenheit function
This is the second function. It is a function which converts entered Celsius degree number in float type to Fahrenheit degree. The contents of the function are the same as below.

Contents            | Composition
--------       | ---
Name of function       | Convert_celsius_fahrenheit 
input variable (argument)  | Celsius value in float type 
Process  | Converts celsius to fahrenheit according to the conversion formula. The formula is `((9 / 5) * value of celsius) + 32`. Remember this variable `value of celsius` needs to be changed to a specific variable name. 
output value(return value)    | Converted value in celsius from fahrenheit, Float Type 

We already have handled the test code in class. If you see the text as below when executing `python shell`, it means that it works properly.
```python
>>> import fahrenheit_converter as fc
>>> fc.convert_celsius_fahrenheit(32.2)
89.96000000000001
>>> fc.convert_celsius_fahrenheit(50)
122.0
>>>
```
As the above, let’s make a test code by editing `if __name__ == '__main__':`  part.

## Write print_fahrenheit_value function
It is the last function. There is no print value and only the result of input value will be displayed. The compositions of the function are the following.

Contnets            | Composition
--------       | ---
Name of function      | print_fahrenheit_value
input variable(argument) | celsius_value in float type, fahrenheit_value in float type
Process     | Display entered celsius value and Fahrenheit value on the screen. Follow with each` celsius degree :`, `Fahrenheit degree :` must be included. 
output value (return value)  | None. Do not omit the `return variable name` if there is no output value.

Testing in `python shell`, you see the execution as below.
```python
>>> import fahrenheit_converter as fc
>>> fc.print_fahrenheit_value(10.3,20.3)
celsius degree : 10.3
fahrenheit degree : 20.3
```
You may think that it is a simple function as it only displays the values. You just need to write `celsius degree`, and ` fahrenheit degree` correctly to be displayed in a proper manner.  

## Edit main function
The last thing to do is to complete the fahrenheit converter program by linking each function. In order to do it, we need to edit the `main()` function. The below of ` # ===Modify codes below=================` is the `main` function, write the code according to the instructions below.

1. Call function `input_celsius_value()` and save the result value in variable `celsius_value` .
2. Call `convert_celsius_fahrenheit()` function using variable `celsius_value` as parameter. Convert temperature and save the retuned value to variable `fahrenheit_value`.
3. Call function`print_fahrenheit_value` using two variables  `celsius_value` and `fahrenheit_value`  as parameter. 

It is very simple but somewhat complicated as you are not accustomed with using those vocabulary. We can compose functions but there are a lot of functions provided by python such as `print` or `input`. We call those functions as built-in functions. See the code below.

```python
abc = input("What's Your Name? ")
print(abc)
```
If we decribe above code as `main` function writing instruction style, it must be: 

1. Call input function by entering "What's Your Name? " as the entering value for input function and save the result in abc variable.
2. Call print function by entering abc in print function.

If you have listened well in class, you would understand without any difficulty. And use LINE if you have any questions.


## Print the result
You can see the result by executing `python fahrenheit_converter.py` after completing your code. Of course, it is necessary to enter value by users.

```bash
This program is a converter which converts Celsius to Fahrenheit.
============================
Enter Celsius degree to convert : 32.2
celsius degree : 32.2
fahrenheit degree : 89.96000000000001
===========================
Program has ended.
```

## Assignment submission
All lab assignment has completed. Let’s submit the assignment.
- Press `windows`+`r` and enter cmd and click OK.
- Change directory to working folder.
- Enter below code on cmd window.

```python
python submit.py
```

After entering above command, you will see the screen as below with Login ID and Password. Enter Login ID and password which we used for registering http://theteamlab.io website.


```python
== Submmting solutions | fahrenheit_converter.py
Login ID:
Password :
```
Note. You can submit the lab assignment in any time you want. You will see the message as below if everything is composed correctly.

```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
print_fahrenheit_value |       PASS |             Good Job
convert_celsius_fahrenheit |       PASS |             Good Job
                main |       PASS |             Good Job
 input_celsius_value |       PASS |             Good Job
-------------------- | ---------- | --------------------
```
## Next Work
We have completed the lab_4. I want you to praise your own patience and enthusiasm and celebrate with a cool beer. This was the first time to compose a program by your own, and not just editing or correcting. From now on, all assignment will be suggested like this. You have to understand every detail and must complete the work yourself without any help well, except for Google.


> **Human knowledge belongs to the world** - from movie 'Password' -
