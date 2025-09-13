class Solution:
    #stack
    def isValid(self, s: str) -> bool:
        s_first = ['(','[','{']
        s_last= [')', ']', '}']
        stack=[]
        
        for char in s:
            if char in s_first:
                stack.append(char)
            elif char in s_last:
                if not stack:
                    return False
                if s_first[s_last.index(char)] != stack[-1]:
                    return False
                stack.pop()
        return not stack

        

                





        