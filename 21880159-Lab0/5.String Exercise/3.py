# Exercise 6: Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create
# a new string s3 made of the first char of s1, then the
# last char of s2, Next, the second char of s1 and second
# last char of s2, and so on. Any leftover chars go at
# the end of the result.
def mix_string(s1, s2):
    new_str = ""
    s2 = s2[::-1]
    max_len = max(len(s1), len(s2))
    for i in range(max_len):
        if i < len(s1):
            new_str += s1[i]
        if i < len(s2):
            new_str += s2[i]
    return new_str


if __name__ == '__main__':
    s1 = "Abc"
    s2 = "Xyzde"
    s3 = mix_string(s1, s2)
    print(s3)
