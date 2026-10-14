#FizzBuzz (fizzbuzz.py): for numbers 1 to 30, print Fizz if divisible by 3, Buzz if by 5, FizzBuzz if by both, otherwise the number.
for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)