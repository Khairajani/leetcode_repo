class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # sort the element
        nums.sort()
        n = len(nums)
        s = set()

        # run loop till half of the length
        for i in range(n//2):
            # add average to set (or hash)
            s.add((nums[i]+nums[n-i-1])/2)

        # return length
        return len(s)

