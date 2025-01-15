class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<high:
            mid = low + (high-low)//2

            if mid%2==1:
                mid-=1
            
            # numbers are appearing twice up until mid (even position)
            if nums[mid]==nums[mid+1]:
                low+=2
            # One number has appreaed once before mid
            # [1,1,3,4,4,5,5,6,6,7,7]
            # here mid=5 (so we do mid-1, now mid becomes 4); nums[4]=4 and nums[5]!=4
            # we will do, high=4
            # in next [1,1,3,4,4] iteration mid becomes 2, nums[2]=3 and nums[3]=4 becomes 4          
            # # we will do, high=2
            # in next [1,1,3] iteration mid becomes 0, nums[0]=3 and nums[1] becomes 4          
            # # we will do, high=2
            # [3]
            else:
                high = mid
            
        return nums[low]
        