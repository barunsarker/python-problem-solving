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
# Function Problem 32 — Count Even Numbers
# Problem Statement:
# Write a Python function named count_even(numbers) that takes a list of integers as an argument and prints how many even numbers are present in the list.

list=[10, 15, 20, 25, 30, 35]

def count_even(numbers):
    count=0
    for i in numbers:
        if i%2==0:
            count=count+1
    print(count)
         
count_even(list)
# output 3
# ==============================

# 🟢 Function Problem 33 — Count Odd Numbers
# Problem Statement:
# Write a Python function named count_odd(numbers) that takes a list of integers as an argument and prints how many odd numbers are present in the list.
list = [10, 15, 20, 25, 30, 35]

def count_odd(numbers):
    
    count=0
    for i in numbers:
        if i%2!=0:
            count=count+1
    print(count)

count_odd(list)
# Output 3
# =========================
# 🟢 Function Problem 34 — Find Maximum in a List
# Problem Statement:
# Write a Python function named find_max(numbers) that takes a list of integers as an argument and prints the largest number in the list.
# input list = [10, 25, 7, 40, 18]

list = [10, 25, 7, 40, 18]

def find_max(numbers):
    max= numbers[0]
    for i in numbers:
        if i > max:
            max=i
    print(max)
find_max(list)

# output 40
# =========================

# 🟢 Function Problem 35 — Find Minimum in a List
# Problem Statement:
# Write a Python function named find_min(numbers) that takes a list of integers as an argument and prints the smallest number in the list.
list = [10, 25, 7, 40, 18]
def find_min(numbers):
    min_number = numbers[0]
    for i in numbers:
        if i < min_number:
            min_number=i
    print(min_number)
    
find_min(list)
# Output 7
# ==========================

# 🟢 Function Problem 36 — Sum of List Elements
# Problem Statement:
# Write a Python function named sum_list(numbers) that takes a list of integers as an argument and prints the sum of all elements in the list.
    
list = [10, 20, 30, 40, 50]
def sum_list(numbers):
    total = 0
    for i in numbers:
        total = total+i
    print(total)

sum_list(list)

# Output 150
# ==========================


# 🟢 Function Problem 37 — Calculate List Average
# Problem Statement:
# Write a Python function named average_list(numbers) that takes a list of integers as an argument and prints the average of all elements in the list.
list = [10, 20, 30, 40, 50]
def average_list(numbers):
    count = 0
    total = 0
    for i in numbers:
        count = count+1
        total = total+i
        average=total/count
    print(average)
average_list(list)
# Output 30
# ================================

# 🟢 Function Problem 38 — Count Positive Numbers
# Problem Statement:
# Write a Python function named count_positive(numbers) that takes a list of integers as an argument and prints how many positive numbers are present in the list.
list = [-5, 10, -3, 20, 0, 15]
def count_positive(numbers):
    count = 0
    for i in numbers:
        if i > 0:
         count=count+1
    print(count)
count_positive(list)
# output 3
# =============================
# 🟢 Function Problem 39 — Count Negative Numbers
# Problem Statement:
# Write a Python function named count_negative(numbers) that takes a list of integers as an argument and prints how many negative numbers are present in the list.
list = [-5, 10, -3, 20, 0, 15]
def count_negitive(numbers):
    count =0
    for i in numbers:
        if i < 0:
            count=count+1
    print(count)
count_negitive(list)
# output 2
# =================================
# 🟢 Function Problem 40 — Find Second Largest Number
# Problem Statement:
# Write a Python function named second_largest(numbers) that takes a list of integers as an argument and prints the second largest number in the list.
list = [10, 25, 7, 40, 18]

def second_largest(numbers):
    
    second = float('-inf')
    maximum = float('-inf')
    
    for i in numbers:
        if i > maximum:
            second = maximum
            maximum = i
        elif i > second and i != maximum:
            second = i

    print(second)
second_largest(list)
# Output = 25
# ============================

# 🟢 Function Problem 41 — Remove Duplicates।
# Problem Statement
# Write a Python function named remove_duplicates(numbers) that takes a list of integers as an argument and prints a new list containing only the unique elements.
lst = [10, 20, 10, 30, 20, 40, 30]

def remove_duplicates(numbers):
    numbers =(set(numbers))
    print(numbers)
    result=sorted(numbers)
    print(result)
    
remove_duplicates(lst)
# Output = [10, 20, 30, 40]
# =============================


# 🟢 Function Problem 42 — Find Common Elements
# Problem Statement
# Write a Python function named find_common(numbers1, numbers2) that takes two lists of integers as arguments and prints the elements that are present in both lists.
numbers1 = [10, 20, 30, 40, 50]
numbers2 = [30, 40, 50, 60, 70]
def find_common(numbers1, numbers2):
    a=set(numbers1)
    b=set(numbers2)
    result=a.intersection(b)
    print(sorted(result))
    
find_common(numbers1, numbers2)
# Output [30, 40, 50]
# =============================

# 🟢 Function Problem 43 — Find Unique Elements
# Problem Statement
# Write a Python function named find_unique(numbers) that takes a list of integers as an argument and prints the elements that appear only once in the list.
lst = [10, 20, 10, 30, 40, 20, 50]

def find_unique(numbers):
    resutl = []
    for i in numbers:
        if numbers.count(i)==1:
            resutl.append(i)
    print(resutl)
find_unique(lst)
# Output [30, 40, 50]
# ==================================

# 🟢 Function Problem 44 — Count Occurrences
# Problem Statement
# Write a Python function named count_occurrences(numbers, target) that takes a list of integers and a target number as arguments and prints how many times the target number appears in the list.

numbers = [10, 20, 10, 30, 10, 40, 20]
target = 10

def count_occurrences(numbers, target):
        result=numbers.count(target)
        print(result)
count_occurrences(numbers, target)

# Output 3
# ==========================

# 🟢 Function Problem 45 — Remove a Specific Element
# Problem Statement
# Write a Python function named remove_element(numbers, target) that takes a list of integers and a target number as arguments and prints a new list after removing all occurrences of the target number.

numbers = [10, 20, 10, 30, 10, 40]
target = 10

def remove_element(numbers, target):
    result=[]
    for i in numbers:
        if i!=target:
            result.append(i)
    print(result)
remove_element(numbers, target)
# Output [20, 30, 40]
# ==========================


# 🟢 Function Problem 47 — Find Duplicate Elements
# Problem Statement
# Write a Python function named find_duplicates(numbers) that takes a list of integers as an argument and prints all elements that appear more than once.
numbers = [10, 20, 10, 30, 20, 10, 50,100, 20, 60, 30,20, 100, 40, 50, 60, 40, 70, 100, ]

def element_frequency(numbers):
    
    for i in set(numbers):
        result=numbers.count(i)
        
        if result==1:
            print(i, "appears", result, "time")
        else:
            print(i, "appears", result, "times")

element_frequency(numbers)
# output 
        100 appears 3 times
        70 appears 1 time
        40 appears 2 times
        10 appears 3 times
        50 appears 2 times
        20 appears 4 times
        60 appears 2 times
        30 appears 2 times
# ====================================
# 🟢 Function Problem 47 — Find Duplicate Elements
# Problem Statement:
# Write a Python function named find_duplicates(numbers) that takes a list of integers as an argument and prints all elements that appear more than once.

numbers = [10, 20, 10, 30, 20, 40, 50, 30]

def find_duplicates(numbers):
    result=[]
    for i in numbers:
        if numbers.count(i)>1:
            result.append(i)
    print(set(result))
            
            
find_duplicates(numbers)
# output [10, 20, 30]
# =============================


# 🟢 Function Problem 48 — Find Missing Number
# Problem Statement:
# Write a Python function named find_missing(numbers) that takes a list of integers from 1 to n, with one number missing, and prints the missing number.
# Example Input:
# numbers = [1, 2, 3, 5, 6]
# Expected Output: 4
numbers = [1, 2, 3, 5, 6]
def find_missing(numbers):
    for i in range(1, len(numbers)+2):
        if i not in numbers:
            print(i)
find_missing(numbers)
# =========================
# 🟢 Function Problem 49 — Find Second Smallest Number
# Write a Python function named second_smallest(numbers) that takes a list of integers as an argument and prints the second smallest number.

# Example Input:
# numbers = [10, 25, 7, 40, 18]
# Expected Output:10

numbers = [10, 25, 7, 40, 18]
def second_smallest(numbers):
    smallest=float("inf")
    second_smallest=float("inf")
    for i in numbers:
        if i < smallest:
            second_smallest=smallest
            smallest=i
        elif i < second_smallest  and i != smallest:
            second_smallest=i
    print(second_smallest)
    print(smallest)
    
second_smallest(numbers)
# =============================

# 🟢 Function Problem 50 — Separate Even and Odd Numbers
# Write a Python function named separate_even_odd(numbers) that takes a list of integers as an argument and prints two separate lists: one containing all even numbers and another containing all odd numbers.

# Example Input:
# numbers = [10, 15, 20, 25, 30, 35]

# Expected Output:
# Even: [10, 20, 30]
# Odd: [15, 25, 35]

numbers = [10, 15, 20, 25, 30, 35]
def separate_even_odd(numbers):
    even=[]
    odd=[]
    for i in numbers:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(f"even: {even}")
    print(f"odd:{odd}")
    
separate_even_odd(numbers)


