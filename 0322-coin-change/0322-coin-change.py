class Solution:
    def init_dp_table(self, n, sum, coins):
        self.t = []
        for i in range(n+1):
            temp = []
            for j in range(sum+1):
                if i==0:
                    temp.append(float("inf"))
                elif i==1:
                    if j%coins[0]==0:
                        temp.append(j//coins[0])
                    else:
                        temp.append(float("inf"))
                else:
                    temp.append(0)
            self.t.append(temp)

    def fetch_minimum_coins(self, n, amount, coins):
        for i in range(1, n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    self.t[i][j] = min(self.t[i-1][j], 1+ self.t[i][j-coins[i-1]])
                else:
                    self.t[i][j] = self.t[i-1][j]
        if self.t[n][amount]==float('inf'):
            return -1
        return self.t[n][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort(reverse=True)
        self.init_dp_table(n, amount, coins)
        # self.max_ways(n,amount,coins)
        # print(self.t)
        return self.fetch_minimum_coins(n, amount, coins)
    
        