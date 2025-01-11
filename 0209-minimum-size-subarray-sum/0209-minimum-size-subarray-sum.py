class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=r=0
        curr_sum = 0
        min_size = float('inf')

        while r<=len(nums)-1:
            curr_sum+=nums[r]

            while curr_sum>=target:
                min_size = min(min_size,r-l+1)
                curr_sum-=nums[l]
                l+=1
            
            r+=1
        
        return min_size if min_size!=float('inf') else 0

        
        
            