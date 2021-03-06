# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
def countdown(num):
    nums_list=[]
    for val in range(num,-1,-1):
        nums_list.append(val)
    return nums_list

# print(countdown(7))


# Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(nums_list):
    print(nums_list[0])
    return nums_list[1]

# print(print_and_return([11,22]))


# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(nums_list):
        # # get the 1st value 1st
    # first_val = nums_list[0]
        # # get the length of the list
    # list_length = len(nums_list)
        # # add them together and return
    # return first_val + list_length
    
    return nums_list[0] + len(nums_list) #more streamlined

# print(first_plus_length([10,2,3,4,5]))


# Values Greater than Second - Write a function that accepts a list and creates a new list containing 
# only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(orig_list):
    new_list = []
        # get the 2nd value in the original list
    second_val = orig_list[1]
        # scan thru original list and find values greater than 2nd value and add to new list
    for idx in range(0,len(orig_list)):
        if orig_list[idx] > second_val:
            new_list.append(orig_list[idx])

    print(len(new_list))
    return new_list
# print(values_greater_than_second([5,2,3,2,1,4]))


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size, value): 
    new_list = []
    for num_times in range(0,size):
        new_list.append(value)
    return new_list

# print(length_and_value(3,9))