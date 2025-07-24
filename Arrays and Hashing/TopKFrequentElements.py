#Understand
#Return element that is the most frequent in the array

#Match
#Dictionary

#Plan
#Create a dicitionary with key:value pairs. (key=Element in array), (value=Amount of times seen in the array)
#Find values in dictionary with the greatest value
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}

        for number in nums:
            if myDict.get(number):
                myDict[number] += 1
            else:
                myDict[number] = 1

        #Could have also just turned into list and sorted it, making syntax easier
        sortedDict = dict(sorted(myDict.items(), key=lambda item:item[1], reverse=True)) 
        myList = list(sortedDict.items())
        listOfTopK = []
        for index in range (0,k):
            listOfTopK.append(myList[index][0])
        return listOfTopK

#Evaluate
#Time Complexity: O(n^2 + k)
#Space Complexity O(n^2 + k)
#Completed: 7/24/25