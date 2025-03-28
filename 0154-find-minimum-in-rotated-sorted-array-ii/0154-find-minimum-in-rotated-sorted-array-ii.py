class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high -= 1  # Reduce the range to handle duplicates

        return nums[low]  # Index of the minimum element