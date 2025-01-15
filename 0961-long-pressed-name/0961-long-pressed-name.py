class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        n= len(name)

        j=0
        m = len(typed)

        while i<=n-1 and j<=m-1:
            if typed[j]==name[i]:
                i+=1
                j+=1
            
            elif i>0 and typed[j]==name[i-1] :
                j+=1
            
            else:
                return False
        
        if i==n:
            while j<=m-1:
                if typed[j]!=name[i-1]:
                    return False
                j+=1
            return True
        else:
            return False

        