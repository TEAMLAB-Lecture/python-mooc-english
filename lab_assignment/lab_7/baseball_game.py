# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - Do NOT remove this function
    # Return the random number which is from 100 to 999
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    # '''
    # Input:
    #   - user_input_number : String type varialbe
    # Output:
    #   - True if user_input_number can be converted to an integer,
    #     otherwise False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_digit("551")
    #   True
    #   >>> bg.is_digit("103943")
    #   True
    #   >>> bg.is_digit("472")
    #   True
    #   >>> bg.is_digit("1032.203")
    #   False
    #   >>> bg.is_digit("abc")
    #   False
    # '''
    # ===Modify codes below=============
    # Assign the result to "result variable" that need to be converted
    # according to above conditions
    result = None

    # ==================================
    return result


def is_between_100_and_999(user_input_number):
    # '''
    # Input:
    #   - user_input_number : String tyed variable
    #                         The variable is guaranteed to be converted as a numeric string value.
    # Output:
    #   - True if user_input_number is converted to an integer
    #     and less than 100 and less than 1000, or False if not
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_between_100_and_999("551")
    #   True
    #   >>> bg.is_between_100_and_999("103943")
    #   False
    #   >>> bg.is_between_100_and_999("472")
    #   True
    #   >>> bg.is_between_100_and_999("0")
    #   False
    # '''
    # ===Modify codes below=============
    # Assign the result to "result variable" that need to be converted
    # according to above conditions
    result = None

    # ==================================
    return result


def is_duplicated_number(three_digit):
    # '''
    # Input:
    #   - three_digit : A three-digit positive integer value whic is a string type.
    #                   Three-digit positive integer values which is a string type are guaranteed.
    # Output:
    #   - True if there are duplicates
    #     when string typed three_digit is converted to a integer tpye, otheriwse False
    #   ex) 117 - True, 123 - False, 103 - False, 113 - True
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_duplicated_number("551")
    #   True
    #   >>> bg.is_duplicated_number("402")
    #   False
    #   >>> bg.is_duplicated_number("472")
    #   False
    #   >>> bg.is_duplicated_number("100")
    #   True
    # '''
    # ===Modify codes below=============
    # Assign the result to "result variable" that need to be converted
    # according to above conditions

    result = None
    # ==================================
    return result


def is_validated_number(user_input_number):
    # '''
    # Input:
    #   - user_input_number : String tyed variable
    # Output:
    #   - True if user_input_number vairable is the condition below, otherwise False
    #     1) String typed numeric value
    #     2) More than 100, and less than 1000
    #     3) No duplicate numbers
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_validated_number("amvd")
    #   False
    #   >>> bg.is_validated_number("402")
    #   True
    #   >>> bg.is_validated_number("472")
    #   True
    #   >>> bg.is_validated_number("100")
    #   False
    #   >>> bg.is_validated_number("1000")
    #   False
    # '''
    # ===Modify codes below=============
    # Assign the result to "result variable" that need to be converted
    # according to above conditions

    result = None
    # ==================================
    return result


def get_not_duplicated_three_digit_number():
    # '''
    # Input:
    #   - None : No parameter
    # Output:
    #   - Randomly generate and return a three-digit integer value
    #     String type numeric value
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   125
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   634
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   583
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   381
    # '''
    # ===Modify codes below=============
    # Assign the result to "result variable" that need to be converted
    # according to above conditions
    # Create a random number using the get_random_number() function

    result = None
    # ==================================
    return result


def get_strikes_or_ball(user_input_number, random_number):
    # '''
    # Input:
    #   - user_input_number : A three-digit integer that the user enters as a string value.
    #   - random_number : The number that the computer automatically generates as a string value.
    # Output:
    #   - [strikes, ball] : Integer values are returned by follow rule
    #   - 1 strike, if the user input number is perfectly
    #     matched the randomly generated number: number and number of place
    #   - 1 Ball, if the number of digits is different, but two numbers have the same number only
    #   - 3 Strike, if two numbers are matched perfectly.
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_strikes_or_ball("123", "472")
    #   [0, 1]
    #   >>> bg.get_strikes_or_ball("547", "472")
    #   [0, 2]
    #   >>> bg.get_strikes_or_ball("247", "472")
    #   [0, 3]
    #   >>> bg.get_strikes_or_ball("742", "472")
    #   [1, 2]
    #   >>> bg.get_strikes_or_ball("472", "472")
    #   [3, 0]
    # '''
    # ===Modify codes below=============
    # Assign the result to "result variable" that need to be converted
    # according to above conditions

    result = None
    # ==================================
    return result


def is_yes(one_more_input):
    # '''
    # Input:
    #   - one_more_input : String typed text entered by the user
    # Output:
    #   - True if the user input string,
    #    case-insensitive, is YES or Y,otherwise false
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_yes("Y")
    # True
    # >>> bg.is_yes("y")
    # True
    # >>> bg.is_yes("Yes")
    # True
    # >>> bg.is_yes("YES")
    # True
    # >>> bg.is_yes("abc")
    # False
    # >>> bg.is_yes("213")
    # False
    # >>> bg.is_yes("4562")
    # False
    # '''
    # ===Modify codes below=============
    # Assign the result to "result variable" that need to be converted
    # according to above conditions

    result = None
    # ==================================
    return result


def is_no(one_more_input):
    # '''
    # Input:
    #   - one_more_input : String typed text entered by the user
    # Output:
    #   - True if the user input string,
    #    case-insensitive, is No or N,otherwise false
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_no("Y")
    # False
    # >>> bg.is_no("b")
    # False
    # >>> bg.is_no("n")
    # True
    # >>> bg.is_no("NO")
    # True
    # >>> bg.is_no("nO")
    # True
    # >>> bg.is_no("1234")
    # False
    # >>> bg.is_no("yes")
    # False
    # '''
    # ===Modify codes below=============
    # Assign the result to "result variable" that need to be converted
    # according to above conditions

    result = None
    # ==================================
    return result


def main():
    print("Play Baseball")
    user_input = 999
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    # ===Modify codes below=============
    # Can be modified freely including the above code


    # ==================================
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
