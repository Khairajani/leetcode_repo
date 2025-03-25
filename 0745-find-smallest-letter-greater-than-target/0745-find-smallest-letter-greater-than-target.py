class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters)-1
        res = -1
        while low<=high:
            mid = low + (high-low)//2

            if target < letters[mid]:
                res = mid
                high = mid-1
            elif target >= letters[mid]:
                low = mid+1
            

        if res!=-1:
            return letters[res]
        else:
            if target < letters[0]:
                return letters[-1]
            return letters[0]