class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count_map = {}
        for element in t:
            char_count_map[element] = char_count_map.get(element,0)+1      
        
        unique_count = len(char_count_map.keys())
        n = len(s)
        i=0
        j=0
        # result = []
        min_result_len = n+1
        min_result = ""
        result_substring = ""

        while j<n:
            curr_element = s[j]
            result_substring+=curr_element

            if char_count_map.get(curr_element) is not None:
                char_count_map[curr_element]-=1

                if char_count_map[curr_element]==0:
                    unique_count-=1

                    while unique_count==0 and i<=j:
                        # add to solution as unique count =0
                        if j-i+1<min_result_len:
                            min_result_len = j-i+1
                            min_result = s[i:j+1]

                        # try to see if can remove the element at i
                        char_at_i = s[i]
                        if char_at_i in char_count_map:
                            char_count_map[char_at_i]+=1
                            if char_count_map[char_at_i] > 0:
                                unique_count += 1

                        i+=1
                        
            j+=1
            
        return min_result



