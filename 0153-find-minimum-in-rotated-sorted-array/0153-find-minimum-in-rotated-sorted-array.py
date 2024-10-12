class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        res = -1
        while start<=end:
            mid = start + (end-start)//2
            # print(mid,nums[mid])
            # if smallest element
            if nums[mid-1]>nums[mid]:
                res = mid
                break
            # else decide where is unsorted array
            elif nums[mid]<nums[end]:
                end = mid-1
            else:
                start = mid+1
          
        return nums[res]
                