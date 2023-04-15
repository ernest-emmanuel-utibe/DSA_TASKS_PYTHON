def merge_two_sorted_arrays(arrayOne, arrayTwo):
    sorted_both_arrays = []
    i = j = k = 0
    while i < len(arrayOne) and j < len(arrayTwo):
        if arrayOne[i] < arrayTwo[j]:
            sorted_both_arrays.append(arrayOne[i])
            i += 1
        else:
            sorted_both_arrays.append(arrayTwo[j])
            j += 1
        k += 1
    while i < len(arrayOne):
        sorted_both_arrays.append(arrayOne[i])
        i += 1
        k += 1
    while j < len(arrayTwo):
        sorted_both_arrays.append(arrayTwo[j])
        j += 1
        k += 1
    return sorted_both_arrays
