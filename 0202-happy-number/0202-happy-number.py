class Solution:
        
    def isHappy(self, n: int) -> bool:
        flag = True
        number_set = {}
        while flag:
            n = sum([int(element)**2 for element in str(n)])
            if n==1:
                flag=True
                break
            elif number_set.get(n)!=None:
                flag=False
            else:
                number_set[n]=1
        return flag
