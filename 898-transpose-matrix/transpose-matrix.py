class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]
        transpose= zip(*matrix)
        for row in transpose:
            #row--> tuple
            result.append(list(row))
        
        return result
        