#Understand
#Detect if list contains duplciates

#Match
#Set question

#Plan/Implement
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)
        if len(mySet) != len(nums):
            return True
        else:
            return False

#Review
    #Example 1:
        # Input: nums = [1, 2, 3, 3]
        # Output: true
    # Example 2:
        # Input: nums = [1, 2, 3, 4]
        # Output: false

#Evaluate
    #Time Complexity:O(n)
    #Space Complexity:O(n)

#Completed 7/12/25
