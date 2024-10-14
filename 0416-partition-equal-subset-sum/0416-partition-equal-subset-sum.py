class Solution:
    def init_dp_table(self,N,sum):
        self.t = []
        for i in range(N+1):
            temp = []
            for j in range(sum+1):
                if j==0:
                    temp.append(True)
                elif i==0:
                    temp.append(False)
                else:
                    temp.append(False)
            self.t.append(temp)
    
    def isSubsetSum_top_down(self,N,arr,sum):
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1] <= j:
                    self.t[i][j] = self.t[i-1][j] or self.t[i-1][j-arr[i-1]]
                else:
                    self.t[i][j] = self.t[i-1][j]
        return self.t[N][sum]
        
    def isSubsetSum(self, N, arr, sum):
        self.init_dp_table(N, sum)
        return self.isSubsetSum_top_down(N,arr,sum)
    
            
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)
        if arr_sum&1==1:
            return False
        else:
            return self.isSubsetSum(len(nums),nums,arr_sum//2)