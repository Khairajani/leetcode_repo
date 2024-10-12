class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        res = -1
        while start<=end:
            mid = start + (end-start)//2
            # print(mid,nums[mid])
            # if smallest element
            if nums[mid-1]>=nums[mid]:
                res = mid
                break
            # else decide where is unsorted array
            elif nums[mid]<nums[end]:
                end = mid-1
            else:
                start = mid+1
          
        return res

    def find_occurence(self, nums, start,end,target,flag=None):
        target_index = -1
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

    def search(self, nums: List[int], target: int) -> int:
        min_index = self.findMin(nums)
        print("min_index",min_index)
        x = self.find_occurence(nums, 0,min_index-1, target)
        y = self.find_occurence(nums, min_index, len(nums)-1, target)

        if x==-1 and y==-1:
            return -1
        elif x==-1:
            return y
        return x