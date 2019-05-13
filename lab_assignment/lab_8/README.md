# Lab #8 - Morse Code (morsecode)
Copyright 2019 © document created by TeamLab.Gachon@gmail.com

## Introduction
In this Lab you are going to develop a program for translating Morse Code using Dict date type which is the most applicable data structure provided by Python. As we know already, Morse Code is a signal which sends messages using light or sound<sup id="MorseCodeWiki">[1](#f1)</sup>.
The real Morse Code has its specific rules and the general rules are the following.
![Rules of Morse Code](http://1.bp.blogspot.com/-rk4DfdE6428/T17CmLVk9CI/AAAAAAAAARk/5xZlW_wMnLw/s1600/morse-code-letters.jpg)

This rule can be expressed by "-", "." as below, which are one of the computer characters.

Letter | Code | Letter | Code | Letter | Code | Letter | Code  
---- | ---  | ---- | ---  | ---- | ---  | ---- | ----
A | .- | B | -... | C | -.-. | D | -..  
E | . | F | ..-. | G | --. | H | ....  
I | .. | J | .--- | K | -.- | L | .-..  
M | -- | N | -. | O | --- | P | .--.  
Q | --.- | R | .-. | S | ... | T | -  
U | ..- | V | ...- | W | .-- | X | -..-  
Y | -.-- | Z | --..

The object of this Lab is to create a Morse Code converter program which helps the user to change an alphabet letter to a Morse Code. See the sample forms below.

String input for users
> User input: SOS
> Output: ... --- ...

Morse code input for users
> User input: ... --- ...
> Output: SOS

Well, if you enter something that cannot be converted, it must display an error message like before.
I believe that it is not too hard as we already have experienced various coding structures in Baseball Lab. Well, I know it is just wish I have. Anyway, let’s start working on.  

## Assignment template file download
First of all, you need to download assignment template file. Enter the below address on the address bar of Chrome or Explorer.

https://github.com/TEAMLAB-Lecture/python-mooc-english/blob/master/lab_assignment/lab_8/lab_8.zip

Click View Raw or Download button for downloading. Or click [Lab 8 – Download Link](<https://github.com/TEAMLAB-Lecture/python-mooc-english/raw/master/lab_assignment/lab_8/lab_8.zip>) and it will start download automatically. Move the downloaded lab_8.zip file to work folder and start the assignment after unzip the file.

## Helpful function : `join`
There is a helpful python function needs to be learned before starting this lab. It is called `join` function which is used for converting values on the list to a value in string type. You can use this function as below.

```python
>>> test_list = ["a","b","c","d","e"]
>>> "-".join(test_list)
'a-b-c-d-e'
>>> ".".join(test_list)
'a.b.c.d.e'
>>> " ".join(test_list)
'a b c d e'
```
As you can see in the above code, the `join` function consists of  `"connecting letter".join(list variable)`. Connected string value varies according to connecting letter. The `join` function is useful for connect Morse Codes.

## morsecode.py file overview
Let’s see the outline by opening `morsecode.py` using `atom`. You can see various functions and `main` function when you opening the file using `atom morsecode.py` command. Each function must be written and submitted by yourself. `main` function is the function which actually executing the Morse Code. Firstly, let’s see the two Helper functions provided by the Lab.

The first helper function is `get_morse_code_dict()` function. When a user calls this function, it returns data of dict type which makes you call Morse Code. The function is the same as the following.

```python
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.",
        "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.",
        "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--",
        "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code
```

The above function can be used as below.

```python
>>> morse_code_dict = get_morse_code_dict()
>>> morse_code_dict["A"]
`.-`
```

The second helper function is the `get_help_message()` function. When a user calls this function, it prints the description of Morse Codes as below. This will be used in the `main` function, so don’t worry too much.

```python
>>> morsecode.get_help_message()
'HELP - International Morse Code List\nA: .-\tB: -...\tC: -.-.\tD: -..\tE: .\t\n
F: ..-.\tG: --.\tH: ....\tI: ..\tJ: .---\t\nK: -.-\tL: .-..\tM: --\tN: -.\tO: --
-\t\nP: .--.\tQ: --.-\tR: .-.\tS: ...\tT: -\t\nU: ..-\tV: ...-\tW: .--\tX: -..-\
tY: -.--\t\nZ: --..\t'
>>>
```

Among the above result values, `\t` is a special symbol for making tab spacing. You can see there are 8 spaces between letters when you run the code in Console.

Now, let’s see the list of functions for editing.

Function            | Description
--------       | ---
is_help_command | Receives a string value and returns True if the entered values are "H" or "HELP" no matter whether it is a capital letter or not and returns False if not.
is_validated_english_sentence | Receives a string value. Returns True if entered value can be converted to a Morse Code. Returns False if not. It cannot be converted to a Morse Code under following three conditions. If 1) there is a number, 2) it includes a special character such as `_@#$%^&*()-+=[]{}"';:\|`~`, 3) there is no input besides punctuation marks(.,!?) or input is blank. 
is_validated_morse_code | Receives a string value in Morse Code Type and returns True if it can be converted to an alphabet. Returns False if not. It cannot be converted to an alphabet under following two conditions.  1) If there is another character besides `"-","."," "` 2) If an another code has been entered besides defined Morse Code in `get_morse_code_dict()`  function ex) `......` 
get_cleaned_english_sentence | Receives a English sentence in a string type value which can be converted to a Morse Code. Returns the string value after removing blank spaces of both sides and four punctuation marks such as `".,!?"`. 
decoding_character | Receives a value in a string type which can be replaced by an alphabet using `get_morse_code_dict()` function. Returns the value converted to alphabet. 
encoding_character | Receives 'an' alphabet in a string type. Returns converted Morse Codes in string type using returned value of `get_morse_code_dict()` function. 
decoding_sentence |  Receives values of Morse Code in string type and returns a string which converted Morse Code to alphabets.
encoding_sentence | Receives an English sentence in string type which can be converted to a Morse Code. It converts English sentence into a Morse Code. it must be removed the spaces at the beginning and end of the sentence. The importance is that all Morse Codes require a space among an alphabet, two spaces is required between words in a sentence. 


The last `encoding_sentence()` function is a little complicate. But consider it as below. Remove punctuation marks such as `!` and print Morse Code giving a one blank space between letters and two spaces between words.

![Sample of printing Morse Code](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_10_morsecode/morsecode_example.png)

Note. 한칸 == 'a space' , 두칸 == 'two space'

## Edit the main function

This time, we are going to work with main function. However, the main function in this Lab is not that complicate. The following is the basic Template.

```python
def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============



    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")
```


The `main` function complies with the following rules.

1. It ends when a user enters 0.
2. When a user enters "h" or "help" no matter whether it is a capital letter or not, it calls `get_help_message()` function and prints as below.

```python
Input your message(H - Help, 0 - Exit): H
HELP - International Morse Code List
A: .-   B: -... C: -.-. D: -..  E: .
F: ..-. G: --.  H: .... I: ..   J: .---
K: -.-  L: .-.. M: --   N: -.   O: ---
P: .--. Q: --.- R: .-.  S: ...  T: -
U: ..-  V: ...- W: .--  X: -..- Y: -.--
Z: --..
```
3. when an alphabet sentence, which can be converted to Morse Code, is entered, it prints converted Morse Code.

```python
Input your message(H - Help, 0 - Exit): SOS
... --- ...
Input your message(H - Help, 0 - Exit): Hello!
.... . .-.. .-.. ---
Input your message(H - Help, 0 - Exit): This is Gachon
 - .... .. ...  .. ...  --. .- -.-. .... --- -.
```

4. It converts to an alphabet when a Morse Code, which can be converted to an alphabet, is entered.
```
Input your message(H - Help, 0 - Exit): ... --- ...
SOS
Input your message(H - Help, 0 - Exit): ... . ...
SES
Input your message(H - Help, 0 - Exit): . -..- ---
EXO
Input your message(H - Help, 0 - Exit): .... --- -
HOT
Input your message(H - Help, 0 - Exit): . -..- .. -..
EXID
```
5. And prints errors if user enters something that cannot be converted.
```python
Input your message(H - Help, 0 - Exit): I'm Gachon.
Wrong Input
Input your message(H - Help, 0 - Exit): This is "CS50".
Wrong Input
Input your message(H - Help, 0 - Exit): Hello 123!
Wrong Input
```

> ONE ANNOUNCEMENT. As there are many people who cannot pass the encoding_sentence in Lab#8 morsecode!, In `encoding_sentence function()`, if there are two spaces or more between English words, you must change it to one single space before converting to a Morse Code.  

You can see the sample screen of actual running program as below.

![Samples of running program](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_10_morsecode/implementation_example.png)


## Submit your assignment
All lab assignment has completed. Let’s submit it.
- Press `windows`+`r` and enter cmd and click OK.
- Change directory to working folder.
- Enter below code on cmd window.

```python
python submit.py
```





And you will be able to see the below message if it is correctly written.

```python
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
is_validated_morse_code |       PASS |             Good Job
  encoding_character |       PASS |             Good Job
     is_help_command |       PASS |             Good Job
   decoding_sentence |       PASS |             Good Job
  decoding_character |       PASS |             Good Job
is_validated_english_sentence |       PASS |             Good Job
get_cleaned_english_sentence |       PASS |             Good Job
                main |       PASS |             Good Job
   encoding_sentence |       PASS |             Good Job
-------------------- | ---------- | --------------------
```

## Next Work
After programming quite a few programs, you will start thinking that this kind of Lab is not that difficult. The level of Lab is gradually getting easier for you. So, I recommend that you start working step-by-step. Next time, we are going to learn about file handling. From now on, you will be able to solve more complicate problems.  

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes

<b id="f1">1</b>: [Morse Code Wiki][1], click the page below and you can hear Morse Code. [↩](#MorseCodeWiki)

[1]: https://en.wikipedia.org/wiki/Morse_code
