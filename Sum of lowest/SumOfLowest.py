numbers = [19,5,42,2,77]

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    res = numbers[0] + numbers[1]
    return res

sum_two_smallest_numbers(numbers)