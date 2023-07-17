# Exercise 8: Rename key of a dictionary
# Write a program to rename a key 'city' to
# a 'location' in the following dictionary.
if __name__ == '__main__':
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    temp = sample_dict['city']
    del sample_dict['city']
    sample_dict['location'] = temp
    print(sample_dict)
