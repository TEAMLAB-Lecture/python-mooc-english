Lab #5 - list, control, loop practice (gowithflow)
============================================
Copyright 2019 © document created by TeamLab.Gachon@gmail.com

## Introduction
Remember it is just the sixth week today. Let’s start working with Lab 5. I know it is very hard and tiring but keep in mind that we are just learning the basics.

Have you ever used Instagram? It is a one of the most popular programs made by Python. And I’m pretty sure one day we can develop such a service. Therefore, do not stop practicing and let’s start today’s lab assignment.

At this time, we will practice `list`, `if`, `while` and so on which we already have learned before. The fundamental structure is the same as the `Lab #2 - basic_operations`. There are various functions and you need to edit and correct those fit for its purpose.
It is getting harder but do not forget that it is the basic level and I want you to enjoy doing this Lab.

## Assignment template file download
First of all, download assignment template file. Enter the below address on the address bar of Chrome or Explorer.

>
https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_5/lab_5.zip

Click View Raw or Download button for downloading. Or click [Lab 5 – download link](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_5/lab_5.zip) . It will start download automatically. Move the downloaded lab_5.zip file to work folder and start the assignment after unzip the file.
## Functions need to be edited
What you have to do in this lab assignment are editing the whole `main()` function according to the purpose of the program like Lab #3 and Lab #4, and composing simple functions by editing unit functions such as Lab #5 and #2. 

Since the logic is getting hard, and we cannot make a program only by practicing simple functions, Lab is getting complex. I prepared a lot of Labs for improving your ability better  Don’t get upset. Just... i loved you too much!

Following list are functions need to be edited.

Function            | Description
--------       | ---
sum_of_list      | Returns the sum of list element by receiving the list, consists of number values. 
merge_and_sort    | Returns sorted and merged list from received two lists each consisted with numbers or letters. 
delete_a_list_element   | Receives a list and data type value. If received value is in the list, return the list removed received value. Else, received value is not in list, return Integer 0. 
comparison_list_size   | Receives two lists and compare length of list. return the bigger list. 
odd_even_check | Receives two integer type values and returns the string 'Even' or ‘Odd’ by sumation of two values. 
discount_price | Receives `price` in number type. if the price is lower than 100,000, return 10% discounted value. else, price is same or higher than 100,000, return 20% discounted value. 
find_smallest_value | Receives a list consisting of number type values. Return the smallest value. 
binary_converter | Receives positive integer type value and returns values converted to a binary number in string type. 
number_of_cases | Receives a list consisting of numbers or strings. Returns all the number of cases of combining elements values in corresponding list. Deletes all duplicated combination. 

## Test after editing
Execute tests after adjusting or editing each function according to its purpose. From now, there is no a test code as a helper. Therefore, the student needs to make and execute an edited code on `python shell` or `main` function by themselves. The samples test codes are commented in each function.

## Things need to know before start editing

There are things look difficult before you actually do. For example, merging lists.

```python
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
c = a + b
```
Or, you can merge b list on a list using `a.extend(b)`.
In order to see whether there is a specific value in list, you can use an expression such as `if value in list_data:`. It is a syntax to verify whether values are included in variable `list_data`. Of course, as it is an if statement, you need to write an executive command below using `indentation`. You can write a code as below.

```python
result = []
if not(value in list_data):
    result.append(value)
```
The command add `value` to list `result`  if there are no `value` in list `list_data`. You must understand it before going ahead.
For deleting a `specific value` in a list, you can use `list_data.remove(specific value)`. In the command statement, `list_data` means the name of variable in list type and `specific value` means the value want to delete. For example, if you want to delete `0`, you just put `0` on `specific value`.

Likewise, you can add a value on a list by using `list_data.append(adding value)`. To find the smallest value in list, use `min(list_data)`. To find how many specific value in list, use  `list_data.count(specific value)`. Those are required to complete function `number_of_cases`.

## Assignment submission
All lab assignment has completed. Let’s submit it.
- Press `windows`+`r` and enter cmd and click OK.
- Change directory to working folder.  
- Enter below code on cmd window.  

```python
python submit.py
```

After entering above command, you will see the screen as below with Login ID and Password. Enter Login ID and password which we used for registering http://theteamlab.io website.

```python
== Submmting solutions | gowithflow.py
Login ID:
Password :
```

```python
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
 find_smallest_value |       PASS |             Good Job
         sum_of_list |       PASS |             Good Job
comparison_list_size |       PASS |             Good Job
    binary_converter |       PASS |             Good Job
      merge_and_sort |       PASS |             Good Job
      discount_price |       PASS |             Good Job
      odd_even_check |       PASS |             Good Job
     number_of_cases |       PASS |             Good Job
delete_a_list_element |       PASS |             Good Job
-------------------- | ---------- | --------------------
```

There are still people who submit their assignment without testing the corresponding codes. Sometimes, we can see an `unsupported error`: it means your code cannot be analyzed. What a shame of yourself! Before execute the above command, please making tests codes several times by yourself.

## Next Work
Some people may feel very difficult while doing this assignment. This is because it is the first time we start working with logics. However, most computers work by logics. Therefore, it is necessary to complete the assignment by yourself to grasp the principles even though it is very complicate. This week there are only two Labs. So let’s do just one more assignment.
> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes
