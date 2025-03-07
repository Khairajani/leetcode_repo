class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1 or k==1:
            return 0
        
        elements_in_nth_row = 2**(n-1)
        mid = elements_in_nth_row//2

        # if kth element is in the first part
        # then it is same as (n-1,k)
        if k<=mid:
            return self.kthGrammar(n-1,k)
        
        # else if kth element is in the second part
        # then it is reverse bit of (n-1,k//2)
        else:
            temp = self.kthGrammar(n-1,k-mid)
            if temp==1:
                return 0
            else: 
                return 1