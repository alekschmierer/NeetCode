#Understand 
#We can sort each word in the list alphabetically
#Then we can compare them with each other and create the sublists
#Could make a dictionary with key: sorted_word, value = unsorted_word

#Match, Hash/List

#Plan/Implement
class Solution:
    from typing import List
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Base Case length of 1
        if len(strs) == 1:
            return [[strs[0]]]

        #Create copy of list for index purposes, so that the individual words ordering are retained
        unsortedWords = strs.copy()

        #Sort characters in word
        for index in range (len(strs)):
            strs[index] = "".join(sorted(strs[index]))

        #Find Indexes Of Words that are the same, then index into unsortedWords 
        pointerLeft = 0
        pointerRight = 1
        myList = []
        iteratorList =[]
        while len(strs) != 0:
            iteratorList.append(unsortedWords[pointerLeft])
            while pointerRight < len(strs) and len(strs) != 1:
                if strs[pointerLeft] == strs[pointerRight]:
                    iteratorList.append(unsortedWords[pointerRight])
                    strs.pop(pointerRight); unsortedWords.pop(pointerRight)
                else:
                    pointerRight += 1
            myList.append(iteratorList.copy())
            iteratorList.clear()
            strs.pop(pointerLeft); unsortedWords.pop(pointerLeft)
            pointerRight = pointerLeft + 1
        
        if len(strs) == 1:
            myList.append(strs[0])
        
        return myList

#Evaluate
    #Time Complexity:O(n·k log k + n^2)
    #Space Complexity:O(n^2)

#Completed 7/12/25