class Solution:
    def init_dp_table_top_down(self, n, m):
        self.t = []
        for i in range(n+1):
            temp = []
            for j in range(m+1):
                if i==0 or j==0:
                    temp.append(0)
                else:
                    temp.append(-1)
            self.t.append(temp)
    
    def get_shortest_common_supersequence_top_down(self, x, y, n, m):
        for i in range(1, n+1):
            for j in range(1, m+1):
                if x[i-1] == y[j-1]:
                    self.t[i][j] = 1 + self.t[i-1][j-1]
                else:
                    self.t[i][j] = max(self.t[i][j-1],self.t[i-1][j])
                    
    
    def fetch_scs(self,x,y,n,m):
        scs = ""

        i,j = n,m
        while i>0 and j>0:
            if x[i-1] == y[j-1]:
                scs+=x[i-1]
                i-=1
                j-=1
            else:
                if self.t[i][j-1] > self.t[i-1][j]:
                    scs+=y[j-1]
                    j-=1
                else:
                    scs+=x[i-1]
                    i-=1
        
        while i>0:
            scs+=x[i-1]
            i-=1
        while j>0:
            scs+=y[j-1]
            j-=1
        return scs[::-1]

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        self.init_dp_table_top_down(len(str1), len(str2))
        self.get_shortest_common_supersequence_top_down(str1, str2, len(str1), len(str2))
        return self.fetch_scs(str1, str2, len(str1), len(str2))