# Lab #3 - Exam Grader(exam_grader)
Copyright 2019 © document created by TeamLab.Gachon@gmail.com

Introduction
------------

This assignment is a little short but not that simple. It is the first time you write a function by yourself. If you watch those functions in the future, you will know that those were simple. However, you will think that it is very complicate right now. It is too late to go back, so let’s start working.

Assignment template file download
---------------------------

First of all, you have to download the assignment template file. Please enter the below address on your Chrome or Explorer’s address bar.

> https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_3/lab_3.zip



Click View Raw or Download button for downloading. Or click [Lab 3 – download link](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/raw/master/lab_assignment/lab_3/lab_3.zip) and it will start download automatically. Move the downloaded lab_3.zip file to work folder and start the assignment after unzip the file.

The `exam_grader.py` file will be downloaded. Right after receiving it, let’s execute the code once as a test. You can execute the code by entering `python exam_grader.py` on the cmd window and an error message will show up as below when you execute.

```python
Start of Exam Grader Program
============================
Traceback (most recent call last):
  File "exam_grader.py", line 67, in <module>
    main()
  File "exam_grader.py", line 58, in main
    total_score = sum_of_scores(number_of_subjects)
  File "exam_grader.py", line 29, in sum_of_scores
    for i in range(number_of_subjects):
TypeError: 'NoneType' object cannot be interpreted as an integer
```

Unlike the existing lab, this code is designed to work in consecutive order and not separately as before for achieving the final object. Let’s see the structure of the code.
exam_grader.py code structure
------------------------

For implementing this lab assignment, let’s see the `main` function first. The `main` function is formed as below. Do not forget that the below code can be checked in the `atom editor` and you can open it by moving to the corresponding directory and entering `atom exam_grader.py` command in ‘cmd’ or ‘terminal’.


```python
def main():
    print("Start of Exam Grader Program")
    print("============================")

    number_of_subjects = get_number_of_subjects()
    total_score = sum_of_scores(number_of_subjects)
    average_score = get_average_score(
        total_score=total_score, number_of_subjects=number_of_subjects)
    print_exam_grader(average_score)

    print("===========================")
    print("End of Exame Grader Program")
```

The first two and last two lines are `print` statement and those do not affect real execution of the program. We can see the first function to edit in .`number_of_subjects = get_number_of_subjects()` code. This code means to save the result value from `get_number_of_subjects` function to `number_of_subjects` variable. `get_number_of_subjects` helps to calculate `the total number of subjects` with the values entered by the user.

The next line `total_score = sum_of_scores(number_of_subjects)` is `helper function` which does not affect the actual assignment. This is a function which helps execution of the program in overall and it is designed to enter the score of subjects depending on the number of subjects. I recommend you check after finishing the assignment.




`average_score = get_average_score(total_score=total_score, number_of_subjects=number_of_subjects)` which is the next line is the most important code in this lab. This code assigns the average value of grades to `average_score` by entering variables called `total_score` and `number_of_subjects` in the function of `get_average_score`. The values of `number_of_subjects` are determined in the first code and `total_score` are determined in the second code respectively. There is no `get_average_score` in the downloaded `lab code`. Therefore, you must write it yourself.

Finally, `print_exam_grader(average_score)` is a code in function which displays the final average and grades on the screen based on the subject average score. It also can be applied to the `helper function` so you do not need to edit. However, I recommend you check it after submitting your assignment as it describes `if` statement for the next lesson.

get_number_of_subjects function edit
------------------------------------

The first function to edit is `get_number_of_subjects`. The code of this function is the same as below.

```python
# receive all numbers of subjects using Console
def get_number_of_subjects():

    # """
    # Input:
    #   - None
    # Output:
    #   - number_of_subjects: Total number of subjects in Integer Type
    # Examples(python shell):
    #   >>> import exam_grader as eg
    #   >>> eg.get_number_of_subjects()
    #   Enter the number of subjects: 10
    #   10
    # """
    #
    # ===Modify codes below=================
    number_of_subjects = None
    # ======================================
    return number_of_subjects

```


It looks complicate but the function itself is simple. When executing function without input, a message `Enter the number of subjects:` will be printed on the console for user input. When a user enters <strong>integer</strong>, it returns the value in integer type. It is a simple function. It is very easy to follow as we just 1) enter the values and 2) it converts to an integer number

Create get_average_score function
-------------------------------

This time, let’s write a function without any given template codes. The information of the function is the following.

| contents       | composition                                                    |
|------------|---------------------------------------------------------|
| Name of function     | get_average_score                                       |
| input variable (argument) | 1. total_score : total score in Integer Type |
|            | 2. number_of_subjects : number of subjects in Integer Type |
| output value (return)  | The value is total score in Float Type divided by number of subjects |

I know you are worried about how to make a function with only this information but actually I gave you all the information. In actual development, the developer can decide name of functions or variations but I will not check your assignment if this is not following the rules. ~~Computer does not lie but it does not have flexibility either.~~

Test and submission
--------------

If you have written all those two functions, let’s start executing. You can execute using `python exam_grader.py` command in `console`. If you have correctly written, you would see the result as below. `Enter the number of subjects:` in the third line will show up and the number `3` is written by the user himself and the below `85`,`95`,`100` are also need to be completed by the users.
```python
Start of Exam Grader Program
============================
Enter the number of subjects: 3
Enter the score of the first subject: 85
Enter the score of the second subject: 95
Enter the score of the third subject: 100
Average:  93.33333333333333
Grade:  A
===========================
End of Exam Grader Program
```
Now let’s submit the assignment.

- Press `windows`+`r` and enter cmd and click OK.
- Change directory to working folder.
- Enter below code on cmd window.

```python
python submit.py
```

After entering above command, you will see the screen as below with Login ID and Password. Enter Login ID and password which we used is registering http://theteamlab.io website.

```python
== Submmting solutions | arithmetic_function.py
Login ID:
Password :
```

You might see an error as below if it is incomplete.
```python
---------------------- | ----------- | --------------------
       Function Name   |    Passed?  |             Feedback
---------------------- | ----------- | --------------------
get_number_of_subjects |       PASS  |             Good Job
   get_average_score   |    Not Yet  |   Check Your Grammar
---------------------- | ----------- | --------------------
```

This message usually appears when we write `get_average_score` with incorrect letters. Of course this may not be the problem. Anyway, re-check all the contents to find misspelled words and re-submit the assignment. You will see the message as below if everything is completed correctly.
```python
---------------------- | ----------- | --------------------
       Function Name   |    Passed?  |             Feedback
---------------------- | ----------- | --------------------
get_number_of_subjects |       PASS  |             Good Job
   get_average_score   |       PASS  |             Good Job
---------------------- | ----------- | --------------------
```

Next Work
---------

As you felt today, there is no more kindness. You have to do everything yourself. You have to fight with all kinds of errors and should be challenging for more achievements. Find the causes of the errors and be comfortable with Google. Google research is your best friend and will help you to be the best programmer.

> **Human knowledge belongs to the world** - from movie 'Password' -
