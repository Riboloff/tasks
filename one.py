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

#to definition is a per,utation of the other
def isPermutation(str1, str2):
    dict = {}
    for char in str1:
        dict[char] = dict.get(char, 0) + 1

    for char in str2:
        if (dict.get(char)):
            dict[char] = dict.get(char, 0) - 1
            if (dict.get(char) == 0):
                del dict[char]
        else:
            return 0

    if (dict.keys()):
        return 0

    return 1

#palindrome
def isPalindrome(str):
    dict = {}
    countOdd = 0
    for char in str:
        dict[char] = dict.get(char, 0) + 1
        if (dict.get(char, 0) % 2 == 1):
            countOdd += 1 
        else:
            countOdd -= 1

    return countOdd <= 1


#for str in ['asdf', 'aa', '']:
    #print str, isUniqueString(str)
    #print str, isUniqueStringWithoutAddStruct(str)


#for str1, str2 in [('asdf', 'asfd'), ('aab', 'abb'), ('aaa', 'aaa'), ('', ''), ('11', '12')]:
#    print str1, str2, isPermutation(str1, str2)

for str in ['aabb', 'abb', 'bbaaa', 'acaca', 'aaaddd', 'werrewqqav']:
    print str, isPalindrome(str)
