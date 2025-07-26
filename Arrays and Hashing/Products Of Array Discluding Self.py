#UMPIRE
#Understand
#Return array output 
#output[i] is product of all elements in list nums, except nums[i]
#essentially store value of product of all other numbers in the list in that spot

#Match
#Lists/Division

#Plan
#Divide the product total of each number in the array from number[i] to output[i]
#Special case when only 1, zero exists in array (all zero values except the output[i] place)
#Special case when 2 or more zeros exist in array (all zero values)
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zerosIndex = []
        productTotal = 1
        for index in range(len(nums)):
            if nums[index] == 0:
                zerosIndex.append(index)
            else:
                productTotal *= nums[index]

        output = []
        if len(zerosIndex) == 0:
            for number in nums:
                output.append(productTotal // number)
        elif len(zerosIndex) == 1:
            for index in range(len(nums)):
                if index == zerosIndex[0]:
                    output.append(productTotal)
                else:
                    output.append(0)
        else:
            for index in range(len(nums)):
                output.append(0)
        return output

#Evaluate
#Time Complexity: O(n^2)
#Space Complexity: O(n + m)
#Completed 7/26/25, need to learn the recommended O(n) way for this approach and the algo with prefix and suffix approach