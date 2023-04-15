def right_rotate_array(digits):
    rotate = digits[digits.length - 1]
    for i in range(1, len(digits)):
        rotate.append(digits[i - 1])

    return rotate
