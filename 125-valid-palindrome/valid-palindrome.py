import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^a-zA-Z0-9]', '', s) #punctuations
        s=s.lower() 
        #s= re.sub(r'\d+', '', s) #numbers 
        s= re.sub(r'\s+', ' ', s).strip() #space

        for i in range(len(s)//2):
            #amanaplanacanalpanama
            #a m a n a p l a n a  c  a  n a l p a n a m  a
            #0 1 2 3 4 5 6 7 8 9 10 11 12 3 4 5 6 7 8 9 20  
            #i 0--> a   len(s)   

            #raceacar
            #r a c e a c a r
            #0 1 2 3 4 5 6 7

            if s[i]!=  s[len(s)-1-i]:
                return False
        return True
