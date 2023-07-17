# Exercise 8: Find all occurrences of a substring
# in a given string by ignoring the case
# Write a program to find all occurrences of
# “USA” in a given string ignoring the case.
def count_substring(str, sub_str):
    str = str.lower()
    return str.count(sub_str.lower())


if __name__ == '__main__':
    str1 = "Welcome to USA. usa awesome, isn't it?"
    sub_str1 = "USA"
    count = count_substring(str1, sub_str1)
    print("Chuoi USA: ", count)
