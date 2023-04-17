def rearrange_positive_negative_values(digits):
    i = 0
    while i < digits.length:
        j = 0
        while j < digits.length:
            if digits[i] < digits[j]:
                temp = digits[i]
                digits[i] = digits[j]
                digits[j] = temp
        j += 1
    i += 1
    return digits
