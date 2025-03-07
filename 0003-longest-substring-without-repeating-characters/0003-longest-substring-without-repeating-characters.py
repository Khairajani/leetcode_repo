class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = s
        char_count_map = {}
       
        n = len(s)
        i=j=0
        unique_chars = 0
        substring_length = []
        while j<n:
            k = j-i+1
            # print(k, unique_chars)
            char_count_map[arr[j]] = char_count_map.get(arr[j],0)+1
            if char_count_map[arr[j]]==1:
                unique_chars+=1
            
            while k>unique_chars and i<=j:
                # print(f"As k={k} and unique_char={unique_chars} reducing the window for i={s[i]}:{i}")
                char_count_map[arr[i]] = char_count_map.get(arr[i])-1
                if char_count_map[arr[i]]==0:
                    unique_chars-=1
                    char_count_map.pop(arr[i])
                i+=1
                k = j-i+1
            
            if unique_chars == k:
                substring_length.append(k)
                # print(s[i:j+1], k)
                
            
            j+=1
        if substring_length:
            return max(substring_length)
        else:
            return 0