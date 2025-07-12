#Understand
#Detect if strings contains duplciates
#Compare sizes to ensure same length, sort strings and return comparison

#Match
#Sorted/.sort() required

#Plan/Implement
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

#Evaluate
    #Time Complexity: O(n)
    #Space Complexity:O(1)

#Completed 7/12/25