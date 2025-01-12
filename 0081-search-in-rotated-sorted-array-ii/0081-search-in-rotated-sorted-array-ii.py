class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        arr = nums
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # Check if the target is found
            if arr[mid] == target:
                return True #mid

            # Determine which part is sorted
            if arr[low] < arr[mid]:  # Left part is sorted
                if arr[low] <= target < arr[mid]:
                    high = mid - 1
                else: # if target is mid, it could have been caugth in first if itself
                    low = mid + 1
            elif arr[mid] < arr[low]:  # Right part is sorted
                if arr[mid] < target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:  # arr[low] == arr[mid], handle duplicates
                low += 1  # Narrow the search range

        return False #-1  # Target not found
        