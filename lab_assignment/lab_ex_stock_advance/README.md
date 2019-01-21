Extreme Lab #2 – Collecting stock data as you want (Stock Data Crawler Advance)
=========================================================================

Copyright 2015 © document created by TeamLab.Gachon@gmail.com

Introduction
------------

We have successfully finished the Stock Data Crawler and now it is a piece of cake to collect stock data. So I prepared for this. The purpose of this Lab is to decide the range of corporation data to be collected at the time when we execute the program. This looks very difficult and complicate but it is not. You can easily execute it with your little effort.

Stock Data Advance Overview
---------------------------

In this Lab, there are two different things from the existing Stock Data Crawler.

1) The download URL of CSV file can be changed by the input of the user. 2) The form of user input changes.  ex) ALL-005930.KS-2014/12/01-2015/12/30

In other words, it analyzes the form of user input and prints or saves the downloaded CSV file.

As I already explained that the URL sample for downloading is the following.

> http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2013&g=d
The base address of the above address is `http://real-chart.finance.yahoo.com/table.csv` and you can download different types of stock information by entering `s`, `a`, `b`, etc. You can set the following values.

| Key | Description       | Value                | Note                         |
|----|------------|-------------------|------------------------------|
| s  | Item(Symbol) | 005930.KS         | Samsung Electronics Co. Ltd. |
| a  | Start month    | 0                 | Jan. (starts from 0) |
| b  | Start day    | 1                 |                              |
| c  | Start year    | 2013              |                              |
| d  | End month      | 11                | Dec. (starts from 0)            |
| e  | End day      | 31                |                              |
| f  | End year      | 2013              |                              |
| g  | Period        | d: day, w : week , m: month | v:display only 'dividend' |

You can obtain a lot of different types of stock information by changing those values. For example, enter `s=005380.KS` and `d=11&e=31&f=2015`, then you can download the stock information of Hyndai Motor until Dec. 31st , 2015.

You can select various corporations as below and you can also download the stock information of the entire corporations for a specific period if you only know the corporation code.

| Item(Symbol) | Name of Item     | Item(Symbol) | Name of Item       |
|-----------|------------|-----------|--------------|
| 005930.KS | Samsung Electronics   | 032830.KS | Samsung Life Insurance     |
| 005380.KS | Hyundai Motor     | 051910.KS | LG Chemical       |
| 005490.KS | POSCO      | 009540.KS | Hyundai Heavy Industries   |
| 012330.KS | Hyundai Mobis | 017670.KS | SK Telecom     |
| 000660.KS | SK Hynix | 105560.KS | KB Finance       |
| 035420.KS | NAVER      | 096770.KS | SK Innovation |
| 005935.KS | Samsung Electronics Preferred | 023530.KS | Lotte Shopping     |
| 015760.KS | KEPCO   | 086790.KS | Hana Financial Group  |
| 055550.KS | Shinhan Financial Group   | 000810.KS | Samsung Fire Insurance     |
| 000270.KS | Kia Motor     | 066570.KS | LG Electronics       |

For making these URL codes dynamic, the command for the main function needs to be changed as below.

> ALL-005930.KS-2014/12/01-2015/12/30 command-stock code-start year/month/day-end year/month/day
>
> Open-005930.KS-2014/12/01-2015/12/30-example.csv command-stock code-start year/month/day-end year/month/day-name of the file for saving

You can enter Header values of ALL or CSV data for the first command and the result values will be saved in the file if you enter the file name at the end and if there is no file name, the result values will be displayed on the screen.

Download assignment template
---------------------------

You need to download the assignment template file first. Enter the following address on the web browser such as Chrome or Explorer.

> https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_ex_2/lab_ex_2.zip

Click View Raw or Download button to download the file. Or click [Lab ex 2 – Download Link](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_ex_2/lab_ex_2.zip) and it will start downloading automatically. Move the downloaded lab_ex_2.zip file to the working folder and unzip it before start working.

stock_data_advance.py file  Overview
-----------------------------------

See the outline by opening `stock_data_advance.py` using `atom editor`. You can see the `main`  function and other various functions when opening the file. Each function must be written and submitted by yourself and the `main` function is the function to execute the program by requesting the stock information. The realization of each function could be as below.

| Function                     | Description                                                                                                                                                                                                                                                                                                                                              |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| is_validate_url          | It is a helper function which verifies whether the url_address, which is the input variable, is usable when requesting url_address to the Yahoo server. You do not need to edit it.                                                                                                                                                                                             |
| is_validate_date         | Receives the string date information in yyyy/mm/dd form and returns True if it meets the condition and False if it does not meet.  <br> 1) the length must be 3 when dividing the entered data by "/" separator <br> 2) yyyy: year must be entered between 2001 to 2015 <br> 3) mm: entered between 1 to 12 4) dd: must be entered between 1 to 31 (no matter the month) |
| is_validate_command      | Receives the entered value of users and the header value of stock_data and returns True if the values entered by the user are processible and False if not (see the below) |

| make_stock_data_url      | it is created based on the 7 variables entered on the csv download url of Yahoo Finance. <br> base_url is "http://real-chart.finance.yahoo.com/table.csv?" and it creates the final address according to the input variables|
| get_stock_data           | When placing url_address for the Input variable, it request the corresponding information to the Yahoo server and download it. After downloading, it returns the value in two-dimensional list. The Two-Dimensional List has the Header Field list for the zeroth line index and from the next index, it has the daily data in each. |
| get_header_data          | When placing the return value of get_stock_data value in the Input variable, it extracts the corresponding values and returns the value in a list form. |
| get_attribute_data       | When receives the return value of get_stock_data  function and the name of Header Field for extraction, it extracts only the Date Field and the corresponding values for the condition and returns those as a list. |
| write_csv_file_by_result | When entering the return value of get_stock_data  function or the return value of get_attribute_data  and the file name for creation in string type as a input variable, it creates the file with those entered values |
| separate_user_query      | Returns as a list after dividing the user entered values by "-", and values on each list must be saved after removing blank spaces. |

Description of each function
--------------

Like Stock Data Crawler function, this Lab also needs some explanation for functions. However, I do not repeat explaining about the functions already described in Stock Data Crawler.

> make_stock_data_url

make_stock_data_url make a one single URL address with the 7 received input variables. The simplest way to attach a string type data is to use "+" symbol but I recommend you use string formatting as below.


```python
>>> a = "Hello, {0}".format("World")
>>> a
'Hello, World'
```

The string formatting is one of simplest ways of linking strings. If you write symbols and numbers such as {0}, {1}, {2} between quotation marks and a tuple data in format function in order, the corresponding numbers of the tuple index symbols would be substituted in the string. You can easily create a URL using that function.  \`\` > is_validate_command

When receives input of the user, returns True if it meets the below conditions and returns False if not.
1) The input value of the user is divided by "-". 2) You can see the sample input values as below and each has the following meaning.

ALL-005930.KS-2014/12/01-2015/12/30 command-stock code-start year/month/day-end year/month/day ALL-005930.KS-2014/12/01-2015/12/30-example.csv command-stock code-start year/month/day-end year/month/day-the name of file for saving

3) The length should be 4 or 5 when dividing the input variable command_str by "-". 4) when dividing command_str by "-", the value of zeroth index must be the value existed in ALL or header_field no matter whether it is a capital letter or not 5) when dividing command_str by "-", it must return True if there is input on the second and third is_validate_date 6) when dividing command_str by "-", it must create a URL for accessing the yahoo financial server with the first, second and third values and also must return True when there is an input in is_validate_url.

There is one difference. The existing Stock Data Crawler is case sensitive for the first command but this Lab is not.


Edit the main function main
------------------

You have to edit the main function after writing the above functions. The basic template of the main function is the same as below.

```python
def main():
    print("Stock Data Crawler Program!!")
    user_input = 999
    # ===Modify codes below=============

    # ==================================
```

The `main` function has the following rules.

1.	It ends when the user enters 0.
2.	If it returns False when the user enters value in is_validate_command, it must print "Wrong Input, Please, Input".
3.	If there is a file name at the end of the user input, it must create the corresponding file.
4.	If there is no a file name at the end of the user input, it must print the stock data on the screen.
5.	If the command which is the firstly entered value of the user is ALL, it must print (or save) the all data and if the entered value is a specific name of Header Field, it must print (or save) the corresponding Field value.


The real execution screen of the program is the same as the following.
![Stock Data Advance Execution Screen 1](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/ex_lab_2_stock_data_advance/stock_data_advance_screenshot.png)

Assignment Submission
-------------

Let’s submit the assignment as below after finishing editing all the functions.

-	Press `windows`+`r` and enter cmd and click OK.
-	Change directory to working folder.
-	Enter below code on cmd window.  

```bash
python submit.py
```

After entering above command, you will see the screen as below with Login ID and Password. Enter Login ID and password which we used for registering http://theteamlab.io website.

```bash
== Submmting solutions | arithmetic_function.py
Login ID:
Password :
```

You will see the below message if you have written correctly. It also takes a long time for execution as the program for code testing downloads data internally and makes a file for those data. So, do not stop or turn off the computer before showing the result.

```bash
------------------------ | ---------- | --------------------
       Function Name     |    Passed? |             Feedback
------------------------ | ---------- | --------------------
    is_validate_date     |       PASS |             Good Job
 separate_user_query     |       PASS |             Good Job
 make_stock_data_url     |       PASS |             Good Job
     get_header_data     |       PASS |             Good Job
 is_validate_command     |       PASS |             Good Job
write_csv_file_by_result |       PASS |             Good Job
  get_attribute_data     |       PASS |             Good Job
      get_stock_data     |       PASS |             Good Job
                main     |       PASS |             Good Job
------------------------ | ---------- | --------------------
```

Next Work
---------

Thank you.

> **Human knowledge belongs to the world** - from movie 'Password' -

Footnotes
---------
