# Day 6: Let's Review

# Task 
# Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated
# strings on a single line (see the Sample below for more detail).

# Note: 0 is considered to be an even index.

# Input Format
# The first line contains an integer, T (the number of test cases). 
# Each line i of the T subsequent lines contain a String, S.

# Constraints
# 1 <= T <= 10
# 2 <= length of S <= 10000

# Output Format
# For each String Sj (where 0 <= j <= T - 1), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed
# characters.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input("Enter no of inputs\n"))

for i in range(n):
    test_string = input("enter "+str(i)+" string\n")
    even = ""
    odd = ""
    for j in range(len(test_string)):
        if j % 2 == 0:
            even += test_string[j]
        else:
            odd += test_string[j]
    print('{} {}'.format(even, odd))
