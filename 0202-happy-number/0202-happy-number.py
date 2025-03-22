class Solution:
        
    def findSquare(self,n):
        return sum([int(element)**2 for element in str(n)])

    def isHappy(self, n: int) -> bool:
        fast = n
        slow = n
        slow = self.findSquare(slow)
        if slow==1:
            return True
        fast = self.findSquare(self.findSquare(fast))
        while slow!=fast:
            slow = self.findSquare(slow)
            fast = self.findSquare(self.findSquare(fast))
            if slow==1:
                return True
        return False

