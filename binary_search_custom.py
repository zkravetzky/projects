"""
This is me trying to implement a binary search without having to pass the end and start point as arguments
I am able to find the number but am having trouble getting the index 
It is hurting my brain

"""

from math import ceil
from sorting_algo import *

list_size = 10

#This version of binary search created a new smaller list based on the pre existing list to get rid of the need for start and end parameters
def binary_search(number_to_find, list, index = 0):
    #use this instead of start > end because there are no end parameters
    if len(list) == 0 or (len(list) == 1 and list[0] != number_to_find):
        return 'Number not in list'

    #calculates new midpoint with each recursion
    midpoint = ceil(len(list) -1) // 2;
    
    #if number is correct
    if list[midpoint] == number_to_find:
        return f'Number to find is at index {index}'
    
    #if number is greater than number to find search create new list based on the left side of the list
    elif list[midpoint] > number_to_find:
        end = midpoint + 1
        new_list = list[:end]
        return binary_search(number_to_find, new_list, index)
    
    #if number is less than number to find search create new list based on the right side of the list
    elif list[midpoint] < number_to_find:
        start = midpoint + 1
        new_list = list[start:]
        return binary_search(number_to_find, new_list, index)

if __name__ == '__main__':
    list_to_be_sorted = linear_sort(get_random_ints(list_size))
    result = binary_search(5, list_to_be_sorted)
    print(result)

