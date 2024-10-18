class Solution:
    def init_dp_table_memoize(self, n, m):
        self.t = []
        for i in range(n+1):
            temp = []
            for j in range(m+1):
                temp.append(-1)
            self.t.append(temp)
    
    def get_longest_subsequence_length(self, x, y, n, m):
        if n==0 or m==0:
            return 0
        
        if self.t[n][m]!=-1:
            return self.t[n][m]

        if x[n-1] == y[m-1]:
            self.t[n][m] = 1 + self.get_longest_subsequence_length(x,y,n-1,m-1)
            return self.t[n][m]
        else:
            self.t[n][m] = max(self.get_longest_subsequence_length(x,y,n,m-1), self.get_longest_subsequence_length(x,y,n-1,m))
            return self.t[n][m]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.init_dp_table_memoize(len(text1), len(text2))
        return self.get_longest_subsequence_length(text1, text2, len(text1), len(text2))