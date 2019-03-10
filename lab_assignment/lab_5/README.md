Lab #5 - list, control, loop practice (gowithflow)
============================================
Copyright 2019 © document created by TeamLab.Gachon@gmail.com

## Introduction
Remember it is just the sixth week today. Let’s start working with Lab 5. I know it is very hard and tiring but keep in mind that we are just learning the basics.

Have you ever used Instagram? It is a one of the most popular programs made by Python. And I’m pretty sure one day we can develop that kind of service. So do not stop practicing and let’s start today’s lab assignment.

This time we will practice list, if, while and so on which we already have learned before. The fundamental structure is the same as the `Lab #2 - basic_operations`. There are various functions and you need to edit and correct those according to its purpose.
It is getting harder but do not forget that it is the basic level and I want you to enjoy doing this Lab.

## Assignment template file download
First of all, you need to download assignment template file. Enter the below address on the address bar of Chrome or Explorer.

>
https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_5/lab_5.zip

Click View Raw or Download button for downloading. Or click [Lab 5 – download link](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_5/lab_5.zip) and it will start download automatically. Move the downloaded lab_5.zip file to work folder and start the assignment after unzip the file.
## Functions need to be edited
Download the assignment file and overview it using `atom`.
This lesson consists of Labs for editing the whole `main()` function according to the purpose of the program like Lab #3 and Lab #4 and labs for practicing simple functions by editing unit functions such as Lab #5 and #2. We cannot make a program just by practicing simple functions as the logic is hard to understand and that’s the reason why Labs get harder. There are a lot of Labs and everything is for making our ability better, so don’t get upset.

The list of functions in this Lab for editing is the following.

Function            | Description
--------       | ---
sum_of_list      | Returns the sum of list element by receiving the list consists of number values.
merge_and_sort    | Returns values of received two lists consisting of numbers and letters after merging and sorting
delete_a_list_element   | Receives a list and default data type value. Returns the list without values when the received values are included in the list and returns 0 in Integer Type if it is not included.
comparison_list_size   | Receives two lists and returns the bigger list after comparison.
odd_even_check | Receives two integer type values and returns the string 'Even' if the total of these two is an even number and returns the string 'Odd' if the total of these two is an odd number.
discount_price | Receives the corresponding product price in number type and returns the value with 10% discount if the price is lower than 100,000 and the value with 20% discount if the price is higher than 100,000.
find_smallest_value | Receives a list consisting of number type values and returns the smallest value.
binary_converter | Receives positive integer type and returns values converted to a binary number in string type.
number_of_cases | Receives a list consisting of numbers or strings and returns all the number of cases of combining elements values in corresponding list. And in this case, it deletes all the repeated combination.

## Test after editing
Execute tests after adjusting or editing each function according to its purpose. From now, there is no a test code as a helper. Therefore, the student needs to make and execute an edited code on `python shell` or `main` function by themselves. The samples test codes are annexed in each function’s comment and these might be helpful for practice.

##Things need to know before start editing
When you actually start working, you will know that it is not that difficult but still there are few things hard to do. For example, for merging between lines in python you can use a code like below.

```python
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
c = a + b
```
Besides that method, you can merge b list on a list variable using `a.extend(b)`.
In order to see whether there is a specific value for corresponding list, you can use an expression such as `if value in list_data`. It is a syntax to verify whether values are included in a list type called `list_data`. Of course, as it is an if statement, you need to write an executive command below using `indentation`. You can write a code as below.

```python
result = []
if not(value in list_data):
    result.append(value)
```
The code above is a command to add values in `result` list if there are no values in `list_data` list. It is an important example, so you must understand it before going ahead.
For deleting a specific value in a list, you can use `list_data.remove(specific value)`. In the command statement, `list_data` means the name of variable in list type and `specific value` means the value to be deleted. For example, if you want to delete `0`, it can be done by writing `0` on `specific value`.

You can add a value on a list by using `list_data.append(adding value)`. Don’t forget to add `'adding value'` in case of syntax.

The way of finding the smallest value is to use `min(list_data)` and the way of finding numbers of a specific value is to use  `list_data.count(specific value)`. From now, the contents is for understanding `number_of_cases`, so you must complete your assignment.

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

There are still people who submit their assignment without testing the corresponding codes. Sometimes, we can see an `unsupported error` and it means that the code itself cannot be analyzed. What a shame for a student. Well, I know that for executing the above command you must practice making tests codes several times by yourself but it finally will benefit you.

## Next Work
Some people may feel very difficult while doing this assignment. This is because it is the first time we start working with logics. However, most computers work by logics. Therefore, it is necessary to complete the assignment by yourself to grasp the principles even though it is very complicate. This week there are only two Labs. So let’s do just one more assignment.
> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes
