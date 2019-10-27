"""
Problem 3
15.0/15.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.
"""
sub_string = s[0]
temp_string = ''
check_letter = s[0]
for i in range(1, len(s)):
    if sub_string[len(sub_string) - 1] <= s[i]:
        sub_string += s[i]
    else:
        if len(sub_string) > len(temp_string):
            temp_string = sub_string
        sub_string = s[i]
if sub_string == s:
    print(sub_string)
else:
    print(temp_string)
