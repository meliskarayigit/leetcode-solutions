# The isBadVersion API is already defined for you.

class Solution:
    def firstBadVersion(self, n: int) -> int:
       left= 1
       right =  n
       while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                # mid bad
                right = mid
            else:
                # mid not bad
                left = mid + 1
       return left