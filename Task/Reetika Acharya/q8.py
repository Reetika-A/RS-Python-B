# -*- coding: utf-8 -*-
"""Q8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q9OL93fUDpJFoQdG-z3lbX32SlDPe7Iq

Problem 8: We need to count the frequency of each element in a list and return it as a dictionary.
"""

def frequency_count(input_list):
    frequency = {}
    for element in input_list:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency


input_list = [1, 2, 2, 3, 3, 3]
print(frequency_count(input_list))