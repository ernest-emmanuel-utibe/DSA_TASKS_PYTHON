def infinite_series():
    pie = 0;
    sign_to_multiply = 1
    number_of_term = 0
    for i in range(1, 10000, 2):
        term = 4 / i * sign_to_multiply
        pie += term
        print(f"%-10d%.5f%n", number_of_term, pie)
        sign_to_multiply *= -1
        number_of_term += 1
        pie_string = str(pie)
        if pie_string.startswith('3.14159'):
            print(f'{number_of_term}:  {round(pie, 10)}')
            print(f"Pie starts with {pie_string} after {number_of_term} terms")
            break
