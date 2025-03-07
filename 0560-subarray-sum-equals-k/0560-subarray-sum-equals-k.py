class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ## Longest Subarray with Sum K
        arr = nums
        prefix_sum_with_element_index = {0:1}
        subarry_with_given_sum=0
        sum_val = 0
        
        for i in range(len(arr)):
            sum_val+=arr[i]
            
            if sum_val-k in prefix_sum_with_element_index:
                # since we found the diff in prefix_sum, we will add how many times that diff sum occured 
                diff_sum_count = prefix_sum_with_element_index.get(sum_val-k)
                subarry_with_given_sum+=diff_sum_count
            
            prefix_sum_with_element_index[sum_val] = prefix_sum_with_element_index.get(sum_val,0)+1
        
        return subarry_with_given_sum