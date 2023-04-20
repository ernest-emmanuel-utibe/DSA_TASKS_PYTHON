# Create a function that takes in two arguments
def sub_of_an_int(arr, number_in_the_array):
    # initialize maximum to zero
    maximum_number_in_an_array = 0

    # Loop through the length of the first argument dot the length of the array declared in the function minus the
    # second argument
    for integer in range(len(arr) - number_in_the_array):
        # initialize the current variable to zero[
        current_sum = 0
        # Loop through the variable of the first for loop also with the length of the array minus the number
        for variable in range(1, integer + 1):
            # Add the current sum to the array indexing variable in it
            current_sum += arr[variable]
            # If the current sum is greater than the maximum of the array
            if current_sum > maximum_number_in_an_array:
                # initialize the current sum to the maximum number of the array
                maximum_number_in_an_array = current_sum
    # Print out the maximum number of the array
    print(maximum_number_in_an_array)


if __name__ == '__main__':
    variable_length = [4, 9, 12, 13, 2, 1, 0]
    numbers = 3
    sub_of_an_int(variable_length,numbers)
