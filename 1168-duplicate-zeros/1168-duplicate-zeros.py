class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i=0
        j=n-1
        while i<=n-1:
            if arr[i]==0:
                while j>i:
                    arr[j]=arr[j-1]
                    j-=1
                i+=2
                j=n-1
            else:
                i+=1
        return arr

            

        