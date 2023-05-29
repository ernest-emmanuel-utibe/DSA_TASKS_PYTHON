def sum_divisible_by_3():
    sum_of_numbers = 0
    for i in range(1, 81):
        if i % 3 == 0:
            sum_of_numbers += i
    return sum_of_numbers

