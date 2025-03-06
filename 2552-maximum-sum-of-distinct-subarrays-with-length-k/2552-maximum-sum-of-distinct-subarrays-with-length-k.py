class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        arr = nums
        n=len(nums)
        i=j=0
        max_sum = 0
        curr_sum = 0
        element_count = {}

        while j<n:
            curr_sum += arr[j]
            element_count[arr[j]] = element_count.get(arr[j], 0) + 1
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                if len(element_count)==k:
                    max_sum = max(max_sum,curr_sum)
                    
                element_count[arr[i]]-=1
                if element_count[arr[i]]==0:
                    element_count.pop(arr[i])

                curr_sum-=arr[i]
                i+=1
                j+=1
        
        return  max_sum