# Exercise 3: Print the value of key ‘history’
# from the below dict
if __name__ == '__main__':
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    print(sampleDict["class"]["student"]["marks"]["physics"])
