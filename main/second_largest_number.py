# if __name__ == '__main__':
number = int(input("Please type in the length of numbers that you want: "))

if number > 1:
    length = int(input())
    sub_length = int(input())
    if sub_length > length:
        tough = sub_length
        sub_length = length
        length = tough

    for i in range(number - 2):
        affirm = int(input())
        if affirm > length:
            sub_length = length
            length = affirm
        elif affirm > sub_length:
            sub_length = affirm

    print("Second largest number is ", sub_length)
else:
    print("Please enter more than 1 number")
