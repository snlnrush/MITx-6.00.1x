"""
Problem 2
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
count_bob = 0
if s.find('bob') == -1:
    print(count_bob)
else:
    i_start = 0
    i_finish = len(s)
    for i in range(len(s)):
        if s.find('bob', i_start, i_finish) != -1:
            count_bob += 1
            i_start = s.find('bob', i_start, i_finish) + 1

print(count_bob)
