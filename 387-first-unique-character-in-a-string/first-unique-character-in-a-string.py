class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        letter_count= {}

        for letter in s:
            letter_count[letter]= letter_count.get(letter,0)+1

        for index,letter in enumerate(s):
            if letter_count[letter]==1:
                return index
         
        return -1   
