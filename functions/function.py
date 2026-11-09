# Problem Statement
# Write a Python function named addition(a, b) that
# takes two numbers as arguments, calculates their sum, and prints the result.

def addition(a,b):
    x = a+b
    print(x)
addition(7,3)
# output 10
# =======================

# ⚪ Problem 02 — Subtraction
# Problem Statement:
# Write a Python function named subtraction(a, b) that takes two numbers as arguments and prints the difference between them.
def subtraction(a, b):
    c = a -b
    print(c)
subtraction(10, 4)
# output 6
# ===================

# ⚪ Problem 03 — Multiplication
# Problem Statement:
# Write a Python function named multiplication(a, b) that takes two numbers as arguments and prints their product
def multiplication(a, b):
    d = a*b
    print(d)
multiplication(6, 5)
# Output 30
# ===================

# ⚪ Problem 04 — Division
# Problem Statement:
# Write a Python function named division(a, b) that takes two numbers as arguments and prints the result of dividing a by b.
def multiplication(a, b):
    d = a/b
    print(d)
multiplication(20,4)
# output 5.0
# ================
# ⚪ Problem 05 — Square
# Problem Statement:
# Write a Python function named square(n) that takes a number as an argument and prints its square.
def square(n):
    g=n*n
    print(g)
square(8)
# Output 64
# ==========================

# ⚪ Problem 06 — Cube
# Problem Statement:
# Write a Python function named cube(n) that takes a number as an argument and prints its cube

def cube(n):
    d = n*n*n
    print(d)
cube(3)
# Output 27
# ============================


# ⚪ Problem 07 — Average of Two Numbers
# Problem Statement:
# Write a Python function named average(a, b) that takes two numbers as arguments and prints their average.
def average(a, b):
    c = (a+b)/2
    print(c)
average(10, 20)
# Output 15.0
# ========================


# ⚪ Function Problem 08 — Average of Three Numbers
# Problem Statement:
# Write a Python function named average(a, b, c) that takes three numbers as arguments and prints their average.
def average(a, b, c):
    d = (a+b+c)/3
    print(d)
average(10, 20, 30)
# Output 20.0
# =======================

# ⚪ Function Problem 09 — Even or Odd
# Problem Statement:
# Write a Python function named check_even_odd(n) that takes an integer as an argument and prints whether the number is Even or Odd.
def check_even_odd(n):
    if n%2!=0:
        print(n, "is odd number")
    else:
        print(n, "is even number")
        
check_even_odd(7)
# Output Odd 
# =======================

# ⚪ Function Problem 10 — Positive, Negative or Zero
# Problem Statement:
# Write a Python function named check_number(n) that takes a number as an argument and prints whether the number is Positive, Negative, or Zero

def check_number(n):
    if n > 0:
        print(n, 'is Positive Number')
    elif n < 0:
         print(n, "is Negative Number")
    else:
        print(n, 'is Zero')
        
check_number(-5)
# Output Negative Number
# =============================


# ⚪ Function Problem 11 — Maximum of Two Numbers
# Problem Statement:
# Write a Python function named maximum(a, b) that takes two numbers as arguments and prints the larger number.

def maximum(a, b):
    if b > a:
        print(b, 'is large')
    else:
        print(a, 'is large')
        
maximum(10, 25)
# Output 25 large Number
# ===================


# ⚪ Function Problem 12 — Minimum of Two Numbers
# Problem Statement:
# Write a Python function named minimum(a, b) that takes two numbers as arguments and prints the smaller number.
def minimum(a, b):
    if a < b:
        print(a, 'is small')
    else:
        print(b, 'is small')
minimum(10, 25)
# Output 10 is small
# ===============================


# 🟢 Function Problem 13 — Check Equal Numbers
# Problem Statement:
# Write a Python function named check_equal(a, b) that takes two numbers as arguments and prints "Equal" if both numbers are equal; otherwise, prints "Not Equal".
def eheck_equal(a, b):
    if a==b:
        print("Equal")
    else:
        print('Not Equal')
eheck_equal(10, 10)
# Output Equal
# ===========================

# 🟢 Function Problem 14 — Check Divisibility
# Problem Statement:
# Write a Python function named check_divisible(a, b) that takes two integers as arguments and prints "Divisible" if a is completely divisible by b; otherwise, prints "Not Divisible".
def check_divisible(a, b):
    if a%b==0:
        print("Divisible")
    else:
        print("Not Divisible")
check_divisible(10, 2)
# Output Divisible
# =================================

# 🟢 Function Problem 15 — Calculate Percentage
# Problem Statement:
# Write a Python function named percentage(obtained, total) that takes the obtained marks and total marks as arguments and prints the percentage.
def percentage(obtained, total):
    percent = obtained/total*100
    print(f"{percent}%")
percentage(80, 100)
# Output 80.00%
# ==================


# 🟢 Function Problem 16 — Calculate Simple Interest
# Problem Statement:
# Write a Python function named simple_interest(principal, rate, time) that takes the principal amount, interest rate, and time as arguments and prints the simple interest.
def simple_interest(principal, rate, time):
    result = (principal* rate * time) / 100
    print(result)

simple_interest(1000, 5, 2)
# Ourput 100.0
# =============================

# 🟢 Function Problem 17 — Calculate Area of Rectangle
# Problem Statement:
# Write a Python function named rectangle_area(length, width) that takes the length and width of a rectangle as arguments and prints its area.
def rectangle_area(length, width):
    area = length*width
    print(area)
rectangle_area(10, 5)
# Output 50
# ==============================

# 🟢 Function Problem 19 — Calculate Temperature
# Problem Statement:
# Write a Python function named celsius_to_fahrenheit(celsius) that takes a temperature in Celsius as an argument and prints the temperature in Fahrenheit.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*9/5)+32
    print(fahrenheit)
celsius_to_fahrenheit(25)
# Output 77.0
# =================================

# 🟢 Function Problem 20 — Calculate Total Price
# Problem Statement:
# Write a Python function named total_price(price, quantity) that takes the price of one item and the quantity as arguments and prints the total price.
def total_price(price, quantity):
    total_price= price*quantity
    print(total_price)
total_price(100, 5)
# Output 500
# ==================================


# 🟢 Function Problem 21 — Calculate Discount
# Problem Statement:
# Write a Python function named calculate_discount(price, discount) that takes the original price and discount percentage as arguments and prints the discount amount.
def calculate_discount(price, discount):
    discount_amount = (price* discount)/100
    print(discount_amount)
calculate_discount(1000, 10)
# Output 100.0
# ==============================


# 🟢 Function Problem 22 — Final Price After Discount
# Problem Statement:
# Write a Python function named final_price(price, discount) that takes the original price and discount percentage as arguments and prints the final price after applying the discount.
def final_price(price, discount):
    discount = (price*discount)/100
    final_price = price-discount
    print(final_price)
final_price(1000, 10)
# Output 900.0
# ===========================

# 🟢 Function Problem 23 — Calculate BMI
# Problem Statement:
# Write a Python function named calculate_bmi(weight, height) that takes a person's weight in kilograms and height in meters as arguments and prints their BMI.
def calculate_bmi(weight, height):
    BMI = weight/(height*height)
    print(BMI)
calculate_bmi(70, 1.75)
# Output 22.857142857142858
# ===============================

# 🟢 Function Problem 24 — Calculate Total Marks
# Problem Statement:
# Write a Python function named total_marks(math, english, science) that takes marks of three subjects as arguments and prints the total marks.
def total_marks(math, english, science):
    total = math+english+science
    print(total)
total_marks(80, 75, 90)
# Output 245
# ===============================

# 🟢 Function Problem 25 — Calculate Average Marks
# Problem Statement:
# Write a Python function named average_marks(math, english, science) that takes marks of three subjects as arguments and prints the average marks.
def average_marks(math, english, science):
    average = (math+english+science)/3
    print(average)
average_marks(80, 75, 90)
# Output 81.6666666666
# ==============================
# 🟢 Function Problem 26 — Grade Calculator
# Problem Statement:
# Write a Python function named calculate_grade(marks) that takes a student's marks as an argument and prints the grade according to the following rules:
def calculate_grade(marks):
    if marks >=80 and marks <= 100:
        print("A+")
    elif marks >=70:
        print("A")
    elif marks >=60:
        print("B")
    elif marks >=50:
        print("C")
    else:
        print("F")
calculate_grade(85)
# Output A+
# ===================================
# 🟢 Function Problem 27 — Count Digits
# Problem Statement:
# Write a Python function named count_digits(n) that takes an integer as an argument and prints the number of digits in that number.
def count_digits(n):
    count=0
    while n > 0:
        n=n//10
        count+=1
    print(count)
count_digits(12345)
# Output 5
# ===========================
# 🟢 Function Problem 28 — Sum of Digits
# Problem Statement:
# Write a Python function named sum_of_digits(n) that takes a positive integer as an argument and prints the sum of all its digits.
# input 12345
# output 15
def sum_of_digit(n):
    total = 0
    while n > 0:
        digits = n%10
        total= total+digits
        n=n//10
    print(total)
sum_of_digit(12345)
# output 15
# =================================
# 🟢 Function Problem 29 — Reverse a Number
# Problem Statement:
# Write a Python function named reverse_number(n) that takes a positive integer as an argument and prints the number in reverse order.
# input 12345
# output 54321
def reverse_number(n):
    reverse=0
    while n > 0:
        digits = n%10
        reverse=reverse*10+digits
        n=n//10
    print(reverse)
reverse_number(12345)
# output 54321
# ============================
# 🟢 Function Problem 30 — Palindrome Number
# Problem Statement:
# Write a Python function named is_palindrome(n) that takes a positive integer as an argument and checks whether the number is a palindrome or not.

# A palindrome number reads the same forward and backward.
# input 121
# output palindrome number
def is_palindrome(n):
    main_number=n
    reverse=0
    while n > 0:
        digits = n%10
        reverse=reverse*10+digits
        n//=10

    print(reverse)
    if main_number==reverse:
        print("Palindrome Number")
    else:
        print("Not palindrome Number")
is_palindrome(121)
# output palindrome number
# =============================
# 🟢 Function Problem 31 — Factorial
# Problem Statement:
# Write a Python function named factorial(n) that takes a positive integer as an argument and prints its factorial.
# The factorial of a number is the product of all positive integers from 1 to that number.
# input 5
def factorial(n):
    result = 1
    while n > 0:
        result=result*n
        n=n-1
    print(result)
factorial(5)
# output 120
# ====================================
# 🟢 Function Problem 33 — Count Odd Numbers
# Problem Statement:
# Write a Python function named count_odd(numbers) that takes a list of integers as an argument and prints how many odd numbers are present in the list.

list=[10, 15, 20, 25, 30, 35]

def count_even(numbers):
    count=0
    for i in numbers:
        if i%2==0:
            count=count+1
    print(count)
         
count_even(list)
# output 3
