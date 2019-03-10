# Lab #10 - Stock Data Crawler
Copyright 2019 © document created by teamLab.gachon@gmail.com

## Introduction
Until now, we had to enter the data manually for executing programs but today we are going to use stock data provided by the Yahoo Finance. In other words, it is the first time we start writing programs with real data. The data we are going to use are provided in CSV type. You can get the data just simply entering URL internet address.
This assignment will be very interesting but at the same time a little bit difficult. You would be unfamiliar with getting the data and the concept of extracting only the required information may make you feel awkward and new.  However, as it is the first time we handle external data, we need to be challenging and please enjoy the program.

## Stock Data Overview
We are going to obtain data from the US Yahoo finance server. Unfortunately, there is no Korea Yahoo anymore, Yahoo is still working hard in the U.S(including managing data for our assignment ^^.) The data is provided in CSV type. Let’s enter the below URL on your web browser first.

>http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2013&g=d

The main server address of the above address is `http://real-chart.finance.yahoo.com/table.csv` and you can download different stock information data depending on entering `s`, `a`, `b`. You can set following values.  

Key  | Description  | Value  | Note
------|------|------|------
s |item(symbol)  |005930.KS |Samsung Electronics Co. Ltd.
a |Start month   |0 |Jan. (starts from 0)
b |Start day |1 |
c |Start year  |2013 |
d |End month |Nov. 11  | Dec. 12 (Starts from 0)
e |End day |31  |
f |End year |2013 |
g |Period  |d:day, w :week, m:month  | v: only displays 'dividend'

You can obtain a lot of different stock information by changing the above values. For example, if you enter `s=005380.KS` and then `d=11&e=31&f=2015`, you can download the stock information of Hyundai Motor until Dec. 31st,2018.

You can select various corporates as below and you can download stock information of all corporates in Korea for a specific period if you only know the company codes.

Item symbol |Name of item |Item symbol |Name of item
------|------|------|------
005930.KS |Samsung Electronics |  032830.KS| Samsung Life Insurance
005380.KS |Hyundai Motor| 051910.KS| LG Chemical
005490.KS |POSCO| 009540.KS| Hyundai Heavy Industries
012330.KS |Hyundai Mobis| 017670.KS| SK Telecom
000660.KS |SK Hynix|  105560.KS| KB Financial Group
035420.KS |NAVER| 096770.KS| SK Innovation
005935.KS |Samsung preferred | 023530.KS| Lotte Shopping
015760.KS |KEPCO|  086790.KS| Hana Financial Holding Corp.
055550.KS |Shinhan Holding Corp. |  000810.KS| Samsung Fire
000270.KS |KIA Motor |066570.KS| LG Electronics

You can download the table.csv file when entering the corresponding address on your web browser and it usually can be opened by Notepad. You can see as below when you open the file.

 ![It is DATA!](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_12_stock_data_crawler/Data_ScreenShot.png)

It looks little complicate but if we see the structure, the Header Filed in the first line consists of `Date`,`Open`,`High`,`Low`,`Close`,`Volume`,`Adj Close` and the real values of data starts from the second line. Unrecognizable characters are used for place holders and those are caused due to encoding problems and you can consider it as a breaking line.

```bash
wget http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2013&g=d
```

The meaning of each header filed are the same as following.

Open | Close | High | Low | Volume | Adj Close
------|------|------|------|------|------
Initial price  | Closing price  | Highest price  | Lowest price  | Volume | Modified closing price

Now you have learned the basic knowledge on data. Let’s start the assignment.

## Assignment template file download
Firstly, download the assignment template file in the cs50 server. Enter the following command on bash shell after log-in.
```bash
python3.4 submit_assignment.py -get stock_data_crawler
```
If it is correctly downloaded, you can see `stock_data_crawler.py` in the current directory. Verify it using `ls` command.

## stock_data_crawler.py file overview
Let’s see the outline by opening `stock_data_crawler.py` with `vim editor`. You can see various functions with the `main` function when opening the file with `vi stock_data_crawler.py` command. Each function needs to be written and submitted by yourself and `main` function is a function which executes the program by requesting the real stock data. The details of each function realization are described as below.

Function           | Description
--------       | ---
get_stock_data | When requests data to the Yahoo server by entering url address as the Input variable, it returns the corresponding information in Two Dimensional List after downloading the data.
get_header_data | When enters the return value of get_stock_data function for Input variable, it returns in a list type after extracting only the values corresponding to Header Filed.
get_attribute_data | When receives a return value of get_stock_data function, the name of Header Field for extracting and the date(year and month) for extracting as the Input variables, it returns in a list of extracted values corresponding to the conditions and the Data Field.
get_average_value_of_attribute | When receives the return value of get_stock_data function, the name of Header Field for extraction and the date of extraction(year and month) as Input variables, it returns the value in Float type after calculating the average of the extracted values.
write_csv_file_by_result | When the return value of get_stock_data function or of get_attribute_data and the name of the file for creation are entered as input variables of String Type, it creates a file with the entered list values.
separate_user_query | Returns user input value in list type after dividing by `,`. In this case it must be assigned to the list after removing blanks at the beginning and the end.  ex) Input example: SAMSUNG, 2014-12, Open, ALL

## Description of each function
This lab requires some additional information and therefore I will explain the details of the required functions.
> get_stock_data

In get_stock_data function, you can request data by calling the module called urllib as the code below.

```python
url_address = 'http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2015&g=d'
r = urllib.request.urlopen(url_address)
stock_data_string = r.read().decode("utf8")    # Downloaded data in String Type
print(stock_data_string[:100])
```

The result values of the above code will be printed in String Type like `'Date,Open,High,Low,Close,Volume,Adj Close\n2015-11-06,1343000.00,1348000.00,1330000.00,1338000.00,164'`. `r=urllib.request.urlopen` is a syntax which calls data from a specific url address and `r.read()` is a function which calls the value of the corresponding url in byte. Use `decode("utf8")` for converting called byte value to a string type and `utf8` is a character encoding standard used in Linux and in case of Windows, it uses `cp949`.

The result values of the above code will be printed in String Type like `'Date,Open,High,Low,Close,Volume,Adj Close\n2015-11-06,1343000.00,1348000.00,1330000.00,1338000.00,164'`. `r=urllib.request.urlopen` is a function to call values in byte. In order to convert called byte values into sting type, you need to use `decode("utf8")`. `decode("utf8")` is the default for character encoding in Linux and Windows uses `cp949` instead of `decode("utf8")`.


Use `,` to separate the field value for returned string values and use `\n` for rows.
The field value of returned String values can be separated using `,` and the row can be separated with `\n`.
> get_attribute_data & get_average_value_of_attribute

Those above functions are designed to extract a specific field value in returned stock information of `get_stock_data` for a specific period. The two functions have the input variables as below.

```python
def get_attribute_data(stock_data, attribue, year=None, month=None):
 pass
```


Among those four Input variables, `stock_data` means the returned value of `get_stock_data` and `attribute` means the `header` name for extraction.  

There are six values such as `Open`,`Close`,`High`,`Low`,`Volume`,`Adj Close`. The `stock_data` and `attribute` input variables must be entered.

The values for year and month are not mandatory.

If there are no input for year and month, it extracts only the assigned field values of `attribute` in `stock_data`. The extracted values must include `Date` and the name of header field for `attribute`. In addition, if there is an assigned value for `month`, you must assign a value for `year` too. If there is a value only for `year`, it would return the corresponding value like the corresponding year. The two functions can be used as following.


```python
import stock_data_crawler as sdc
url = 'http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2015&g=d'
stock_data = sdc.get_stock_data(url)
header = sdc.get_header_data(stock_data)
print(sdc.get_attribute_data(stock_data, "High"))
print(sdc.get_attribute_data(stock_data, "Open", 2014))
print(sdc.get_attribute_data(stock_data, "Close", 2013, 12))
print(sdc.get_average_value_of_attribute(stock_data, "High", 2014, 12))

```

Remember one thing that all the input variables for `year` and `month` are in int type. The date values of stock_data are assigned for a string type like `2014-01` but the problem is that the value is in int type. Therefore, you need to convert the type for comparing values.

## Edit main function
After finishing writing those above functions, we need to edit the `main` function. The basic template of the `main` function is the same as below.

```python
def main():
    print("Stock Data Crawler Program!!")
    user_input = 999
    url = 'http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2015&g=d'
    # ===Modify codes below=============

    # ==================================
```

This assignment extracts data of Samsung Electronics from Jan. 2013 to Nov. 2016\5 as there is a assigned url. The main function has the following rules.
The `main` function has following rules.

1. It ends when a user enters 0.
2. Users enter command as the same form as below and it prints the result according to the entered values. Firstly, `SAMSUNG` does not need to be edited as it is a fixed value. `2014-12` means the date(year, month) for extraction. `Open` is the field name for extraction. `ALL` is the type of extraction. The description of each type of extraction is the same as the below table and the extraction type must treat things without considering whether it is a capital or small letter.
```bash
SAMSUNG, 2014-12, Open, ALL
```

Extraction type | Use example  | Description
------|------|------
ALL | SAMSUNG, 2014-12, High, ALL | Extracts and prints all the data that meet the conditions and it uses get_attribute_data  function.
MEAN | SAMSUNG, 2014-12, Close, MEAN | Extracts all the data which meets the conditions and prints the average value of these data. It uses get_average_value_of_attribute  function.
FILE | SAMSUNG, 2014-12, Open, FILE, test.csv | Extracts all the data which meet the conditions and uses a command for saving such as write_csv_file_by_result. Remember that in case of using FILE, the name of file must be entered after entering FILE like test.csv.

You can see the running screen shots as below.

![Stock Data Crawler running screen1] (https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_12_stock_data_crawler/result_screenshot_1.png)
![Stock Data Crawler running screen 2] (https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_12_stock_data_crawler/result_screenshot_2.png)


## Assignment submission
If you have finished editing all the functions, let’s submit it as below.
```bash
 python3.4 submit_assignment.py -submit stock_data_crawler.py
```
If it is correctly written, you would see a message as below. Unlike other work, it will take some time for the execution. This is because the code testing program downloads the data internally and combine the data as a single file at the same time. Therefore, do not stop or turn off the program and wait patiently for the result.  

```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
 separate_user_query |       PASS |             Good Job
     get_header_data |       PASS |             Good Job
get_average_value_of_attribute |       PASS |             Good Job
write_csv_file_by_result |       PASS |             Good Job
  get_attribute_data |       PASS |             Good Job
      get_stock_data |       PASS |             Good Job
                main |       PASS |             Good Job
-------------------- | ---------- | --------------------
```

## Next Work
From now, I think we can say that “I know how to use python a little”. Thank you for following me until today. I know it takes lots of time and energy, but it will benefit you one day. I hope to write a lot of good code in the future. Good luck.
> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes
