#Understand
#Use hash map or list to store nums list - target value, to get another list that 
#contain the numbers we must find in the original list, except for when indexI == indexJ
#Allowed to assume nums will always have a pair of indices i and j


#Match
#Hash map

#Plan/Implement
#nums[index] - target = subtractedNums[index]
#So we a list of numbers in subtractedNums we must find in nums
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtractedNums = []
        for number in nums:
            subtractedNums.append(target - number)
        
        for indexI in range(len(subtractedNums)):
            for indexJ in range (len(nums)):
                if subtractedNums[indexI] == nums[indexJ] and indexI != indexJ:
                    return [indexI, indexJ]

#Evaluate
    #Time Complexity:O(n)
    #Space Complexity:O(n)

#Completed 7/12/25