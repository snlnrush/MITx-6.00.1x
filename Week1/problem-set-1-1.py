"""
Problem 1
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""
count_vowels = 0
vowels_set = {'a', 'e', 'i', 'o', 'u'}

for i in s:
    if i in vowels_set:
        count_vowels += 1

print(count_vowels)
