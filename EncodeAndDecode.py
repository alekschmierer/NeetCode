#Understand
#Get length and add a # symbol to seperate between each word
#Read the length of the word to know how long to iterate

#Match
#Lists/Strings

#Plan
#Create list with len+#+word
#Decode by iterating through length string until # and then iterate through the string and append

from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        myList = []
        for word in strs:
            myList.append(str(len(word)) + "#" + word)
        return "".join(myList)
    def decode(self, s: str) -> List[str]:
        pointer = 0
        myList = []
        while pointer < len(s):
            lengthList = []
            while s[pointer] != "#":
                lengthList.append(s[pointer])
                pointer += 1
            length = int("".join(lengthList))
            myList.append(s[pointer+1:pointer+length+1])
            pointer += length+1
        return myList

#Evaluate
#Time Complexity:
    #Encode: O(n)
    #Decode: O(n)
#Space Complexity:
    #Encode: O(n)
    #Decode: O(n^2)
#Completed: 7/24/25