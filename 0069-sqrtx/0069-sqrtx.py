class Solution:
    def mySqrt(self, x: int) -> int:
        high = 1
        low = 0
        while high*high<=x:
            low = high
            high = high*2
        
        res = -1
        while low<=high:
            mid = low+(high-low)//2
            
            if mid*mid==x:
                res = mid
                break
            elif mid*mid<x:
                res = mid
                low = mid+1
            else:
                high = mid - 1
        return res