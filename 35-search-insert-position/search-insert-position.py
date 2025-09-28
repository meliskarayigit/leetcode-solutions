from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        '''
        Example: [1,3,5,6], target = 2
        indexes = 0,1,2,3
        mid = (0+3)//2 = 1 -> nums[1] = 3
        3 > 2 
        searc area: [1] output = 1
        '''
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low   
