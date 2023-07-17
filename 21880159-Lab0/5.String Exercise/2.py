# Exercise 2: Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create
# a new string s3 by appending s2 in the middle of s1.
def input_string():
    str1 = input("Nhap chuoi 1: ")
    str2 = input("Nhap chuoi 2: ")
    return str1, str2


def append_middle(s1, s2):
    mid = len(s1) // 2
    new_str = s1[:mid] + s2 + s1[mid:]
    return new_str


if __name__ == '__main__':
    s1, s2 = input_string()
    print(append_middle(s1, s2))
