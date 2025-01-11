class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        filled_index = []
        for i in range(n):
            if boxes[i]=='1':
                filled_index.append(i)  

        answer = []
        for i in range(n):
            temp_ans = 0
            for ind in filled_index:
                temp_ans+=abs(i-ind)

            answer.append(temp_ans)
        
        return answer


                