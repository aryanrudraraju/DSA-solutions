# -*- coding: utf-8 -*-
"""
Homework 1

Please read the instructions in homework_1.html carefully before starting to code.
"""

#####
# Wind chill calculator
#####


def wind_chill(temp, wind_speed, a=13.12, b=0.6215, c=-11.37, d=0.16, e=0.3965):
    """
    Converts temperature and wind speed into wind-chill index.

    Formula: wci = a + b*T + c*W^d + e*T*W^d, where T is temperature and W is wind speed

    Parameters:
        temp: temperature in Celsius
        wind_speed: wind speed in km/h
        
        The following constants have default values specified above.
        You don't need to include them in function calls.
        
        a: constant with default value
        b: constant with default value
        c: constant with default value
        d: constant with default value
        e: constant with default value

    Returns:
        Wind chill index.
        If wind speed is lower than 10, return the temperature.
        Otherwise, return the index according to the formula, rounded to integer value

    Example use:
    >>> wind_chill(10, 0)
    10
    >>> wind_chill(-10, 20)
    -18
    >>> wind_chill(-20, 30) + 1
    -32
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW

    wci = a + b*temp + c*(wind_speed**d) + e*temp*(wind_speed**d)
    
    if wind_speed < 10:
        return temp
    return round(wci)


#####
# A brainteaser
#####


def the_57_teaser(n):
    """
    A typical coding interview brainteaser.

    Parameters:
        n: (positive) integer

    Returns:
        - For n divisible by both 5 and 7, return '57'; otherwise:
        - For n divisible by 5, return '5'
        - For n divisible by 7, return '7'
        - Otherwise, return None.

    Example use:
    >>> the_57_teaser(14)
    '7'
    >>> the_57_teaser(95)
    '5'
    >>> the_57_teaser(70)
    '57'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if n%5 == 0 and n%7 == 0:
        return '57'
    elif n%5 == 0:
        return '5'
    elif n%7 == 0:
        return '7'
    else:
        return None


def the_57_looper(n):
    """
    Prints the first n values of the_57_teaser starting from 1
    
    Note you may call the function the_57_teaser
    
    Parameters:
        n: (positive) integer
    
    Example use:
    >>> the_57_looper(35)
    None
    None
    None
    None
    5
    None
    7
    None
    None
    5
    None
    None
    None
    7
    5
    None
    None
    None
    None
    5
    7
    None
    None
    None
    5
    None
    None
    7
    None
    5
    None
    None
    None
    None
    57
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    for i in range(1, n + 1):
        print(the_57_teaser(i))
    

#####
# Date string conversion: slash-date format to dash-date format
#####



def date_conversion(date_string):
    """
    Converts date string from "US slash format" to "scientific dash format" as specified in the HW instructions

    Assume input is in American date ordering (month-day-year) -> convert to European ordering (day-month-year).
    Assume that two-digit years are interpreted like Excel: 00-29 as 2000-2029, and 30-99 as 1930-1999.
    Assume that the year of the date is in either range 00 - 99 or 1000 - 9999.

    Parameters:
        date_string: string date in "US slash format", eg, 12/8/16, 1/12/1898, 1/1/35 (we assume valid dates)

    Returns:
        string date in "scientific dash format", eg, 08-12-2016, 12-01-1898, 01-01-1935

    Example use:
    >>> print(date_conversion('12/8/16'))
    08-12-2016
    >>> print(date_conversion('01/12/1898'))
    12-01-1898
    >>> print(date_conversion('11/5/35'))
    05-11-1935
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW

    date_as_list = date_string.split('/')  # Use this to split slash format string into a list
    
    month, day, year = date_as_list
    
    year = int(year)
    if 0 <= year <= 29:
        year += 2000
    elif 30 <= year <= 99:
        year += 1900

    month = "{:02d}".format(int(month))

    day = "{:02d}".format(int(day))

    return day + "-" + month + "-" + str(year)


##### 
# Robust version of date conversion
#####


def date_conversion_robust(date_string):
    """
    Converts date string from "US slash format" to "scientific dash format"

    Valid dates are as follows:
    - US date ordering (month-day-year).
    - Interpret two-digit years like Excel: 00-29 as 2000-2029, and 30-99 as 1930-1999.
    - The year of the date is in either range 00 - 99 or 1000 - 9999
    - An actual date that has occurred or will occur

    Parameters:
        date_string: string date in "US slash format", eg, 12/8/16, 1/12/1898, 1/1/35 (DO NOT assume every input is a valid date)

    Returns:
        if input is valid: return string date in "dash" format, eg, 08-12-2016, 12-01-1898, 01-01-1935
        if input would be valid in European date ordering, print a message for the user and return "Error". 
            - For example, if the input is 16/3/2021, your function should then print out "Not a valid date. Did you mean to input 3/16/2021?" and return "Error".
        if input is not valid: print "Not a valid date." then return "Error".

    Example use:
    >>> print(date_conversion_robust('12/8/16'))
    08-12-2016
    >>> print(date_conversion_robust('1/12/1898'))
    12-01-1898
    >>> date_conversion_robust('1/1/35')
    '01-01-1935'
    >>> print(date_conversion_robust('16/3/2021')) # doctest:+ELLIPSIS
    Not a valid date. Did you mean to input 3/16/2021?
    Error
    >>> print(date_conversion_robust('2/29/2017'))
    Not a valid date.
    Error
    >>> date_conversion_robust('131/2/1928')
    Not a valid date.
    'Error'
    >>> print(date_conversion_robust(2))
    Not a valid date.
    Error
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW

    date_components = str(date_string).split('/')
    if len(date_components) != 3:
        print("Not a valid date.")
        return "Error"
    
    month, day, year = date_components

    if month.isdigit() and day.isdigit() and year.isdigit():
        month = int(month)
        day = int(day)
        year = int(year)
    else:
        print("Not a valid date.")
        return "Error"

    year = int(year)
    if 0 <= year <= 29:
        year += 2000
    elif 30 <= year <= 99:
        year += 1900

    month = int(month)
    day = int(day)
    
    days_in_month = [31, 29 
                     if (year%4 == 0 and year%100 != 0) or (year%400 == 0) 
                     else 28, 
                     31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= month <= 12:
        if 1 <= day <= days_in_month[month-1]:
            month = "{:02d}".format(int(month))
            day = "{:02d}".format(int(day))
            return day + "-" + month + "-" + str(year)

    if 1 <= day <= 12 and 1 <= month <= 31:
        print(f"Not a valid date. Did you mean to input {day}/{month}/{year}?")
    else:
        print("Not a valid date.")
    return "Error"



def comparison_function(value):
    """
    Comparison function for counting_sort
    
    Parameter:
        value - integer
        
    Returns:
        ??? such that comparisons of return values work as described
    
    Example use:
    >>> comparison_function(119933) > comparison_function(18783479)
    True
    >>> comparison_function(123) > comparison_function(124)
    True
    >>> comparison_function(1789) > comparison_function(96851)
    False
    """
    odd_count = sum(1 for i in str(value) if int(i)%2 == 1)
    return (odd_count, value)


def counting_sort(items):
    """
    Sorts a list of integers by counting odd digits.
    
    Parameters:
        items - list of positive integers
        
    Returns:
        sorted copy of items
        
    Example use:
    >>> counting_sort([98, 19, 29, 41, 9999, 73, 241, 1111, 53, 3, 333])
    [3, 29, 41, 98, 241, 19, 53, 73, 333, 1111, 9999]
    >>> counting_sort([999, 19, 919, 111, 119, 1199, 911])
    [19, 111, 119, 911, 919, 999, 1199]
    >>> counting_sort([1234, 4321, 3214, 2413])
    [1234, 2413, 3214, 4321]
    """
    # Please do NOT edit this function.
    return sorted(items, key=comparison_function)


def longest_repeating_substring(input_string):
    """
    Finds the longest substring in which the same character repeats consecutively.

    Parameters:
        input_string - a string

    Returns:
        The longest substring of consecutive repeating characters. If multiple substrings
        have the same maximum length, the first one is returned.

    Example use:
    >>> longest_repeating_substring("hello")
    'll'
    >>> longest_repeating_substring("aabbcccdddde")
    'dddd'
    >>> large_string = 'a' * 1000000
    >>> longest_repeating_substring(large_string) == large_string
    True
    >>> longest_repeating_substring("a")
    'a'
    >>> longest_repeating_substring("")
    ''
    """

    if input_string == "":
        return ""

    longest_substring = input_string[0]  
    current_substring = input_string[0]  

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:  
            current_substring += input_string[i]  
        else:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring  
            current_substring = input_string[i]  

    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

    return longest_substring
