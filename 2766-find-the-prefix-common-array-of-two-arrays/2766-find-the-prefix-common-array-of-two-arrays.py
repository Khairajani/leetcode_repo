class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        b_map = {}
        a_map = {}
        prefix_sum = 0

        result = []
        for i in range(len(A)):
            # get current elements
            a = A[i]
            b = B[i]

            # add it to their own map
            a_map[a]=1
            b_map[b]=1

            # cross map verfication for common elements
            a_present_in_B = b_map.get(A[i],False)
            b_present_in_A = a_map.get(B[i],False)

            # if both element are present
            if a_present_in_B and b_present_in_A:
                if a==b:
                    prefix_sum+=1
                else:
                    prefix_sum+=2
            
            elif a_present_in_B or b_present_in_A:
                prefix_sum+=1
            result.append(prefix_sum)
        return result
