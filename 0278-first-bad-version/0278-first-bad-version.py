# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        high = low = 1
        while isBadVersion(high)==False:
            low = high
            high = high*2
        
        res = high
        while low<=high:
            mid = low + (high-low)//2
            if isBadVersion(mid)==True:
                res = mid
                high = mid-1
            else:
                low = mid+1
        
        return res
