Extreme Lab #1 - Magic Square
=======
Copyright 2017 © document created by TeamLab.Gachon@gmail.com

## Introduction
This is the first Extreme Assignment. All other Lab assignment were designed for all students, but this Lab is 'Extreme' lab which can be solved by only some student who have been practicing a lot of their assignment with their effort.
This Lab is composing Magic Square game. In drama “Deep Rooted Tree”, Joong-gi Lee, who was little King Sejong, solved lots of this magic square problems for the joy.

 ![Joong-gi Lee is handsome](https://s3.ap-northeast-2.amazonaws.com/teamlab-gachon/magic_square.png)

Magic Square is simpler than we expected. However, you may feel difficult if you are not familiar with for and if statements.

## Assignment file (ex_lab_1.zip) download
Firstly, you have to download assignment template file. Enter the below address on your web browser such as Chrome or Explorer.
> https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_ex_1/lab_ex_1.zip

Click View Raw or Download button for downloading. Or click [Lab_ex_1 – Download Link](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/raw/master/lab_assignment/lab_ex_1/lab_ex_1.zip) and it will start downloading automatically. Move the downloaded ex_lab_1.zip file to your work folder and start the assignment after unzip the file.


## magic_square_game.py file overview
Let’s see the outline of code by opening `magic_square.py` with `atom editor`. There are main` function` and  various functions. Each function needs to be written and submitted by yourself. The `main` function is the function which executes magic square. The description of each function is the same as below.  

Function            | Description
--------       | ---
get_zero_matrix    | Receives N, an integer value and returns a two-dimensional list which is a N by N square matrix form. <br />All values of elements are initialized  as 0. 
is_validate_number | Receives string values and returns True if the value is an integer string greater than 3 and less than 20<br />Return False if it is not. 
is_4even_number    | Receives N, an integer and returns True if N is multiple of 4.<br />Return False if not. 
is_odd_number      | Receives N, an integer and returns True if N is an odd number. <br />Return False if it is not. 
get_4even_magic_square | Receives N, an integer, multiple of 4 in string value and returns N by N square matrix consisting of magic squares. <br />The returned square matrix is two dimensional list. 
get_odd_magic_square   | Receives N, an integer, odd number in string type and returns N by N square matrix consisting of magic square.  <br />The returned square matrix is a two-dimensional list. 
is_magic_sqaure        | Receives a square form of two dimensional list and verifies whether the entered list is magic square or not.

## Understanding magic square
- Magic square is a n*n square grid filled with distinct positive integers that each cell contains a different integer and the sum of the integers in each row, column and diagonal are equal.
- There can be only one positive integer from 1 to n*n in each cell of magic square.  It always exists unless when n is 2.


An example of a simple 3 by 3 matrix magic square is the following. . ([Memo list of Dream note][1]).

![An example of magic square](https://s3.ap-northeast-2.amazonaws.com/teamlab-gachon/magic_square_example.png)

The method of forming an odd number magic square or fourth-order magic square is the following.

여기

> The way of making an odd number magic square

1. Place 1 in the middle column of the last row.

2. If right below square is blank, place next number in the square on there.

3. (If 2 is unavailable) and if right below square already occupied, place next number on above of current square. 

4. (If 3 is unavailable) and if right below square on outside of big square, follow following rules: 

   4-1. On the moved square (square on the outside of big square), Check whether there is blank square in inside of big square as a result of horizontal / vertical move. If available, place the next number on there.
   4-2. If there is no blank square even you move horizontally or vertically, place next number on above of current square.

> The way of making a magic square of doubly even order

1. For only diagonal positions (both from left and right), fill with numbers for each blank start from 1. 대각선의 위치만 1 부터 시작해서 해당칸이 몇 번째 칸인지 숫자를 채움니다.
2. Fill in the unfilled numbers from last square in order of right to top. 맨 오른쪽 아래부터 위로 올라오면서 채워지지 않은 숫자를 순서대로 채움니다.

It looks very complicate but there are a lot of codes on the internet already. You can look up for the code. It's no problem. Completion is the most important.

## Edit the main function
Above functions are hard enough, but the most difficult task is to edit the `main` function. The basic template of the `main` function on below.

```python
def main():
    user_input = 999
    print("Play Magic Square Game!!")
    # ===Modify codes below=============

    # ==================================
    print("Thank you for using this program")
    print("End of the Game")
```

The main function has those following rules.

> Input test

1. If the entered value is syntax or a number with a decimal point, it must prints "Wrong Input! Input Again Please" .
2. When the entered value is less than 3 or greater than 20, it prints "Wrong Input! Input Again Please".
3. If the entered value is an odd number or not a number multiplying of 4, it prints "Wrong Input, Only Input odd number or 4n number".

If the user enters an integer among 3 to 20, it will be printed as below.
> Print result

1. It is a form of matrix. each element(square) uses 5 spaces including letters(number). In this case, you can use grammar as form of `"{:5d}".format(10)` for printing an integer after adjusting the location.  
2. After printing a magic square, the total sum of each row is printed as "The sum of each row is 15" style.
3. Print total value of the magic square as like "The sum of the matrix is  45" .
4. Make it blank for last line.

The execution screen of real program will be looks like the following.

![Execution screen of the Magic Square program](https://s3.ap-northeast-2.amazonaws.com/teamlab-gachon/screen_shot_magic_square_1.png)


## Submit your assignment
Please submit your assignment as below after finish editing all the functions.
```python
 python submit.py
```
You will see the below message if it is correctly written.
```python
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
get_4even_magic_square |       PASS |             Good Job
     get_zero_matrix |       PASS |             Good Job
       is_odd_number |       PASS |             Good Job
  is_validate_number |       PASS |             Good Job
     is_4even_number |       PASS |             Good Job
     is_magic_sqaure |       PASS |             Good Job
                main |       PASS |             Good Job
get_odd_magic_square |       PASS |             Good Job
-------------------- | ---------- | --------------------
```

## Next Work
The Extreme Lab is kind of mandatory assignment for getting A+. Not everybody can do this task. Meanwhile, It is a great honor to be here for students working for programming. Few people can finish this assignment and you can be proud of it.

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes

[1]: http://memorist.tistory.com/151
