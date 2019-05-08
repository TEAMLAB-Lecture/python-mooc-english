# Lab Assignment #7- Baseball Game (baseball_game)
Copyright 2017© document created by TeamLab.Gachon@gmail.com

## Introduction
Welcome all students to this assignment after finishing eight very difficult Labs. Today, you cannot imagine how hard this Lab Assignment will be. Surprisingly, until today, there were no hard assignment. Those were just time consuming or feels little complicate. Those were just a piece of cake comparing to today's assignment.  

I can promise you that this assignment is really difficult. ~~~Trust me~~~ . However, it will significantly improve your coding ability a lot. This assignment was selected as the most helpful assignment even it's difficulties in the survey of Gachon University. This assignment seems to indicator of whether you continue programming or not.

This Baseball Game Lab is a **_SIMPLE_** number matching game. The computer creates 3 digit random number.  Then, matches with your number and judge Strike and Ball based on how similar the number are. The simple rules are following.

- 1 Strike if a entered number by the user is the same as that of the computer(including number itself and place of digit)
- 1 Ball if there is a same number in different digit.
- If three digits are the same as those of the computer, the game ends.

In this case computers can only create 3 digits with different numbers. For example, you cannot repeat the same number like `332`, `474`, `555`. See the below example for a strike and ball.






Created numbers by computers | User entered numbers | Result
--------       | --- | ---
472           | 123 | 0 Strike, 1 Ball
472           | 547 | 0 Strike, 2 Ball
472           | 247 |0 Strike, 3 Ball
472           | 742 |1 Strike, 2 Ball
472           | 472 |3 Strike

You may be worried about how to do this assignment, but I will give you some hints and helpful functions to achieve the goal. Be easy and let’s start working on.

## Baseball Game Overview
You may think that verifying whether a number is a strike or ball is enough for this Lab but we also need a program for handling errors when a user enters something inappropriately. For example, you already have seen some programs which correct your input errors while browsing websites, such as not entering "@" for email address, creating a password without numbers and the program. Computer will identify those errors and tell you to re-enter them.

This program will also handle errors with a message saying "Wrong Input" if a user enters incorrectly as below.  

- In case of entering a letter instead of a number(ex. `ab3`)
- In case of entering a real number (ex. `23.5`)
- If there is a repeated number in entered number (ex. `333`, `233`)

In addition, if the user gets "3 Strikes" by entering numbers perfectly as same as those of the computer, we need to ask user to re-play, and if he wants to do it again, program must start again. In this case, the game will re-started with below conditions.  

- Re-start the game if the user enters "Y" or "Yes" not matter whether input is in capital letters or not. ex. `"Y"`,`"yEs"`,`"yes"`
- End the game if the user enters "N" or "No" not matter whether input is in capital letters or not. In other words, the game ends even though the user enters `"n"`, `"nO"`, `"NO"`.
- If the user enters other words besides words related to "YES" or "NO", it will display "Wrong Input" and will re-receive an input from the user.

Another ending condition is entering `0` while playing the game by the user. This condition is the same as that of Factorial Calculator from Lab #8.

Furthermore, when a new game starts, it must display `Random Number is :  xxx` and the computer’s randomly created numbers needs to be shown in the `xxx` part. This is for Autograder system (computers cannot score if it is not printed). Program sample is in below.

 ![Program running screen shot](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_9_baseball_game/baseball_game_screenshot.png)

 

![Screen shot of the game ended by entering 0] (https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_9_baseball_game/baseball_game_screenshot_2.png)


## Assignment template file download
First of all, you need to download assignment template file. Enter the below address on the address bar of Chrome or Explorer.

<https://github.com/TEAMLAB-Lecture/python-mooc-english/blob/master/lab_assignment/lab_7/lab_7.zip>

Click View Raw or Download button for downloading. Or click [Lab 7 – Download link ](<https://github.com/TEAMLAB-Lecture/python-mooc-english/raw/master/lab_assignment/lab_7/lab_7.zip>) and it will start download automatically. Move the downloaded lab_7.zip file to work folder and start the assignment after unzip the file.

## baseball_game.py file Overview
Let’s see the outline by opening `baseball_game.py` using `atom`. You can see various functions and the `main` function when opening the file with `atom baseball_game.py` command in console. Each function must be written and submitted by yourself and `main` function is the function for executing the actual baseball game. The realization of each function is the same as below.

Function            | Description
--------       | ---
is_digit      | A function which receives a string value and returns True if input value can convert to an integer, False if it cannot. 
is_between_100_and_999      | A function which receives a string value and convert to integer. returns `True` if the converted integer is greater than 100 and less than 1000. Return `False` if it isn't in limits. In this case, it is guaranteed that the input value is String data type integer value. Ex) `'324'`, `'1103'` 
is_duplicated_number  | A function which receives a three digit integers in string data type and returns True if there is a repeated number and returns False if it isn't. In this case, it is guaranteed that input is string data type integer values. Ex)   117 - True, 123 - False, 103 - False, 113 - True 
is_validated_number | Receives a string value and returns True if it satisfy following three conditions and returns False if not. 1) It is a string data type number 2) It is greater than 100 (includes 100) and less than 1000, 3) there is no repeated numbers. You can assemble above three functions. 
get_not_duplicated_three_digit_number  | There is no input value. Returns a three digit integer in integer data type without repeated numbers. In this case, it creates a random number using `get_random_number()` function and it returns the corresponding number only if there is no repeated numbers. 
get_strikes_or_ball   | Receives a string of three digits integers and string type integer made by the computer. It returns [strikes or balls] according to the rules of the baseball game. Strikes and balls are values in integer type and are returned in a list. 
is_yes    | Receives a string value and returns True if there is "Y" or "YES" no matter whether it is a capital letter or not and returns False if not.
is_no    | Receives a string value and returns True if there is "N" or "NO" no matter whether it is a capital letter or not and returns False if not.

I know this is very complicate and hard, but you can do it step-by-step.
Note. `get_random_number()` function is a function which returns a three digit natural numbers randomly. Therefore, you must use it in `get_not_duplicated_three_digit_number` function.

## Edit main function
The above functions are very hard but the most difficult part in this Lab is editing the `main` function. The basic template of main function is the same as following.

```python
def main():
    print("Play Baseball")
    user_input = 999
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    # ===Modify codes below=============
    # You can edit freely including the above code


    # ==================================
    print("Thank you for using this program")
    print("End of the Game")
```
The template is very similar to the factorial calculator in lab 7 but a little different. This program shows "Play Baseball" and "Random Number is : " on the screen when starting the program. As I told you before, `print("Random Number is : ", random_number)` must be executed when there is a new baseball game. Students can edit `random_number` variable freely but I recommend you write `get_not_duplicated_three_digit_number` function well for `random_number` as it is the simplest way to finish the assignment.

This assignment is complicating. Furthermore, even though you did a perfect coding, the examination program is really strict so that may not accept your work. If it does not work like the above screenshot (even small letter!), you may fail to pass.

please do not use  `input` statement after using `print` statement when receiving input by a user. For example, it must written in `user_input = input('Input guess number : ')`  form. As my development skills are not perfectly good enough for others, please understand it.
Before writing the `main` function using each function, please edit each function well according to its purpose. You may easily fail the get pass from system, but it will be very interesting and enjoyable work.

## Submit your assignment
All lab assignment has completed. Let’s submit it.
- Press `windows`+`r` and enter cmd and click OK.
- Change directory to working folder.
- Enter below code on cmd window.

```python
python submit.py
```

And you can see the below message if it is correctly written.


```python
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
            is_digit |       PASS |             Good Job
              is_yes |       PASS |             Good Job
is_duplicated_number |       PASS |             Good Job
               is_no |       PASS |             Good Job
 get_strikes_or_ball |       PASS |             Good Job
 is_validated_number |       PASS |             Good Job
is_between_100_and_999 |       PASS |             Good Job
                main |       PASS |             Good Job
get_not_duplicated_three_digit_number |       PASS |             Good Job
-------------------- | ---------- | --------------------
```
I know it is the most impressive moment in your life. You’ve worked hard.

## Next Work
This will be the touchstone of your great programming ability.
Before you just learned some alphabets and few sentences like "How are you? Fine thank you, and you", but in this assignment you have learned how to sing a 'kid's pop song' using programming.
You have done well. Take a rest with a bottle of beer tonight and remind yourself that you have great potential to succeed. Thank you so much for following me all days.

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes
