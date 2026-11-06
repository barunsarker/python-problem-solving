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
