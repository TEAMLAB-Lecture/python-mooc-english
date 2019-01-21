# Lab #9 - File IO Example (file_io_example)
Copyright 2019 © document created by teamLab.gachon@gmail.com

## Introduction
Fortunately, this Lab is not hard and there are only 5 functions.
This Lab is the first Lab of Text Handling Series. The object of this Lab is to download simple files and extract some information from those files. Then, let’s start again.

## Assignment template file download
You have to download assignment template file first. Enter the below address on your Chrome and Explorer or any other web browsers.

https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_9/lab_9.zip

Click View Raw or Download button for download. Or click Lab 9 – Download Link and it will be downloaded automatically. Move the downloaded lab_9.zip to the working folder and start working after unzipping the file.

## file_io_example.py file overview
Let’s see the outline by opening`file_io_example.py` using `atom`. This lab has only 5 functions and there is no Main function.

Now, see the list for editing.

Function           | Description
--------       | ---
get_file_contents | Receives the filename in string type and returns all text data that are in the corresponding file in string type.
get_number_of_characters_with_blank | Receives the filename in string type and returns all numbers of letters that are in the corresponding file after converting those to an integer value.
get_number_of_characters_without_blank | Receives the filename in string type and returns all numbers of letters in the corresponding file in a integer value type after removing the blank spaces. The blank space means " ", "\t", "\n".
get_number_of_lines | Receives the filename in string type and returns all numbers of lines in the corresponding file in an integer value. In this case, do not count the last line.
get_number_of_target_words | Receives the filename and target_words for finding in string type and returns in an integer value the number of letters including small and capital letters such as target_words in the corresponding file.


## Result verification
It is really simple. Move to the working folder in cmd window and it will show the result as below if you simply test it in python shell.

```python
Type "help", "copyright", "credits" or "license" for more information.
>>> import file_io_example as fie
>>> fie.get_file_contents("1984.txt").split("\n")[0]
'GEORGE ORWELL'
>>> fie.get_number_of_characters_with_blank("1984.txt")
558840
>>> fie.get_number_of_characters_without_blank("1984.txt")
459038
>>> fie.get_number_of_lines("1984.txt")
1414
>>> fie.get_number_of_target_words("1984.txt", "Hi")
3938
>>> fie.get_number_of_target_words("1984.txt", "had")
1327
>>> exit()
```

## Submit your assignment
When you have finished editing all the functions, please submit it as below.
- Press `windows`+`r` and enter cmd and click OK.
- Change directory to working folder.
- Enter below code on cmd window.

```python
python submit.py
```

And you will be able to see the below message if it is correctly written.
```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
 get_number_of_lines |       PASS |             Good Job
   get_file_contents |       PASS |             Good Job
get_number_of_characters_with_blank |       PASS |             Good Job
get_number_of_characters_without_blank |       PASS |             Good Job
get_number_of_target_words |       PASS |             Good Job
-------------------- | ---------- | --------------------
```  

## Next Work
As this lab is not that hard you could finish it early. But still there are two labs left as a gift and you will be the python master after completing all the assignment.
> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes
