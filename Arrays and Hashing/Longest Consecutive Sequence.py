#Understand
#Find longest consecutive sequence incrementing by 1 only

#Match
#Two Pointer approach

#Plan
#Set the list and sort it
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Base Case 0 or 1
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        #Sort and Set Nums
        sortedNums = list(set(nums))

        #Two Poitner Approach
        pointerLeft = 0
        pointerRight = 1
        longestSequence = 1
        currSequence = 1

        sortedNums.sort()
        while pointerRight != len(sortedNums):
            if sortedNums[pointerRight] == sortedNums[pointerLeft]+1:
                currSequence += 1
                pointerLeft += 1
                pointerRight += 1
            else:
                longestSequence = max(longestSequence, currSequence)
                currSequence = 1
                pointerLeft += 1
                pointerRight += 1
        
        return max(longestSequence, currSequence)

#Evaluate
    #Time Complexity: O(nlogn)
    #Space Complexity:O(n)

#Completed 7/27/25
