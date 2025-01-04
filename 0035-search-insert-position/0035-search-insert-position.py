class Solution:
    def binary_search(self, nums, low, high, target):
        result = -10**5
        while low<=high:
            mid = low + (high-low)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid+1

        return low


    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums,0,len(nums)-1,target)