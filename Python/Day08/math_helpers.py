import math


def factorial(n):
    result = 1 
    for i in range(2, n+1):
        result *= i
    return result

def area_of_circle(r):
   return math.pi * r * r

def is_even(n):
    return n % 2 == 0


if __name__ == "__main__":
    print(factorial(5))  # Output: 120
    print(area_of_circle(3))  # Output: 28.274333882308138
    print(is_even(4))  # Output: True
    print(is_even(5))  # Output: False