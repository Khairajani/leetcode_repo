class Solution:
    def solve_all_subsets(self,arr,temp_list,index):
        if index == len(arr):
            self.all_subsets_list.add(tuple(temp_list))
            return
        self.solve_all_subsets(arr,temp_list,index+1)
        self.solve_all_subsets(arr,temp_list+[arr[index]],index+1)
        

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.all_subsets_list = set()
        self.solve_all_subsets(nums,[],0)
        sorted_list = sorted(list(self.all_subsets_list))
        return sorted_list
        