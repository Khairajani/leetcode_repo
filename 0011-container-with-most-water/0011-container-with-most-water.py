class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        ans = float('-inf')
        while i<j:
            curr_ans = (j-i)*min(height[i],height[j])
            ans = max(curr_ans,ans)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return ans