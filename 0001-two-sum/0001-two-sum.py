class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = {}
        
        for i in range(len(nums)):
            difference_value_index = difference_map.get(nums[i])
            if difference_value_index is None:
                difference_map[target-nums[i]] = i
            else:
                return [difference_value_index,i]