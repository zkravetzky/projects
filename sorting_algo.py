from operator import index
import random

"""
This is a program that test if i understand a bubble/ linear sort algorithm 
It works pretty well so i would say that I completely understand it

"""

#list size can be changed here to however big a list you want
list_size = 10

#used to generate random list each time the code is run
def get_random_ints(x):
    list_to_return = []
    for i in range(x):
        list_to_return.append(random.randint(0,10))
    return list_to_return

#used to swap variables inside the list a little overkill but it makes me look cool
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

#actual sorting algorithm used to sort the list fed into the function
def linear_sort(list_to_be_sorted):
    for i in range(len(list_to_be_sorted)-1):
        for j in range(len(list_to_be_sorted)-1):
            current_element = list_to_be_sorted[j]
            next_element = list_to_be_sorted[j+1]
            if current_element > next_element:
                list_to_be_sorted[j], list_to_be_sorted[j+1] = swap(current_element, next_element)
    return (list_to_be_sorted)


if __name__ == '__main__':
    list_to_be_sorted = get_random_ints(list_size)
    print(list_to_be_sorted)
    print(linear_sort(list_to_be_sorted))