class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        total = [0]*n
        for i in range(n):
            temp = 0
            for j in range(n):
                if boxes[j]=='1':
                    temp+=abs(i-j)
            total[i] = temp
        return total