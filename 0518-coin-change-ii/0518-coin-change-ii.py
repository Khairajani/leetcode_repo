class Solution:
    def init_dp_table(self, n, sum):
        self.t = []
        for i in range(n+1):
            temp = []
            for j in range(sum+1):
                if j==0:
                    temp.append(1)
                else:
                    temp.append(0)
            self.t.append(temp)

    def max_ways(self, n, amount, coins):
        for i in range(1, n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    self.t[i][j] = self.t[i-1][j] + self.t[i][j-coins[i-1]]
                else:
                    self.t[i][j] = self.t[i-1][j]

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        self.init_dp_table(n, amount)
        self.max_ways(n,amount,coins)
        return self.t[n][amount]