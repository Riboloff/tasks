#! /usr/bin/python
#1.1 Implement an algorithm to determine if a string has all unique characters.

def isUniqueString(str):
    if (len(str) == 0):
        return 0
    dict = {}
    for char in str:
        if (dict.get(char)):
            return 0

        dict[char] = 1
    return 1

#What if you cannot use additional data structures?
def isUniqueStringWithoutAddStruct(str):
    uniqueBin = 0
    for char in str:
        ordChar = ord(char) - ord('a')
        bit = 1 << ordChar
        if ((uniqueBin & bit) > 0):
            return 0
        uniqueBin = uniqueBin | bit

    return 1

for str in ['asdf', 'aa', '']:
    print str, isUniqueString(str)
    print str, isUniqueStringWithoutAddStruct(str)
