"""
This is an implementation of a binary search algorith using my sorting algo to sort the list first

"""


from math import ceil
from sorting_algo import *

list_size = 10

#Binary search algorithm implementation
def binary_search(number_to_find, list, end, start = 0):

    while start <= end:
        # calculating new midpoint every recursion
        midpoint = start + ceil((end - start) / 2);

        #if number is found
        if list[midpoint] == number_to_find:
            return f'Number to find is at index {midpoint}'

        #if number is greater than the number to find search the left part of the list
        elif list[midpoint] > number_to_find:
            end = midpoint -1
            return binary_search(number_to_find, list, end, start)
        
        #if the number is less than the number to find search the right part of the list
        elif list[midpoint] < number_to_find:
            start = midpoint + 1
            return binary_search(number_to_find, list, end, start)
    
    #if we leave the while loop withoput finding the number    
    return 'Number not in list'

if __name__ == '__main__':
    list_to_be_sorted = linear_sort(get_random_ints(list_size))
    result = binary_search(5, list_to_be_sorted, len(list_to_be_sorted) -1)
    print(result)

