number = int(input("Please type in the length of number_in_the_array that you want: "))

if number > 1:
    length_of_the_number = int(input())
    sub_length = int(input())
    if sub_length > length_of_the_number:
        number_length = sub_length
        sub_length = length_of_the_number
        length = number_length

    for i in range(number - 2):
        affirm_that = int(input())
        if affirm_that > length_of_the_number:
            sub_length = length_of_the_number
            length_of_the_number = affirm_that
        elif affirm_that > sub_length:
            sub_length = affirm_that

    print("Second largest number is ", sub_length)
else:
    print("Please enter more than 1 number")
