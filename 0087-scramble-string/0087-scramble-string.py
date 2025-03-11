class Solution:
    
    def solve(self,a,b):
        if len(a)!=len(b):
            return False

        n =len(a)
        if a==b or n==0:
            return True

        already_visited = self.map.get(f"{a} {b}")
        if already_visited is not None:
            return already_visited

        flag = False
        for i in range(1,n):
            # non-swapped
            non_swapped_cond = (self.solve(a[:i],b[:i]) and self.solve(a[i:],b[i:]))
            if non_swapped_cond:
                flag = True
                return True

            # swapped
            swapped_cond = (self.solve(a[-i:],b[:i]) and self.solve(a[:-i],b[i:]))
            if swapped_cond:
                flag = True
                return True
        self.map[f"{a} {b}"] = flag
        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        self.map = {}
        return self.solve(s1,s2)