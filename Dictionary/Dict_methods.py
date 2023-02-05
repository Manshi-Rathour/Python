myDict = {"key": "value",
          "manshi": "coder",
          "Marks": [96, 94, 98],
          "one": 1,
          "anotherDict": {'mango': 'fruit'}
          }
print(list(myDict.keys()))        # prints the keys of the dictionary in the form of list
print(myDict.keys())              # prints the keys of the dictionary
print(myDict.values())            # prints the values of the dictionary
print(myDict.items())             # prints the (key, value) for all the elements of the dictionary

print(myDict)

updateDict = {"anjali": "friend",
              "chandni": "friend",
              "naincy": "friend",
              "aditi": "friend"}
myDict.update(updateDict)        # update the dict by adding key-value pair from updateDict
print(myDict)

print(myDict.get('manshi'))      # prints the value associated with the key 'manshi'
print(myDict['manshi'])          # prints the value associated with the key 'manshi'
# difference b/w .get and [] syntax
print(myDict.get('manshi1'))     # returns none as manshi1 is not presnt in dict
print(myDict['manshi1'])       # throws an error as manshi1 is not presnt in dict



