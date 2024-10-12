class Solution:
    def find_occurence(self, nums, target,flag=None):
        target_index = -1

        start = 0
        end = len(nums)-1
        while start<=end:
            mid = start + (end-start)//2
            if target == nums[mid]:
                target_index = mid
                if flag=="first":
                    end = mid-1
                elif flag=="last":
                    start = mid+1
                else:
                    break
            elif target < nums[mid]:
                end = mid-1
            elif target > nums[mid]:
                start = mid+1

        return target_index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_pos = self.find_occurence(nums,target,"first")
        last_pos = self.find_occurence(nums,target,"last")
        return [first_pos,last_pos]

        