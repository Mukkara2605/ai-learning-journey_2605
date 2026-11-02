def sum_all(*numbers):
    return sum(numbers)

def average_all(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    print(sum_all(1, 2, 3, 4, 5))  # Output: 15
    print(average_all(1, 2, 3, 4, 5))  # Output: 3.0
    print(sum_all())  # Output: 0
    print(average_all())  # Output: 0