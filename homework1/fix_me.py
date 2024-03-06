"""
first otus homework
"""


def calculate_average(numbers):
    """function counting average"""
    total = sum(numbers)
    count = len(numbers)
    return total / count


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
