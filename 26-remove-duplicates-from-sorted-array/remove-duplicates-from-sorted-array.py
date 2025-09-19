class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=[]
        for num in nums:
            if num not in k:
                k.append(num)
        nums[:]=k
        elements= len(k)
        return elements
        
        