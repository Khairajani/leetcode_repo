class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k=min(2,len(set(fruits)))
        arr = fruits
        char_count_map = {}
       
        n = len(arr)
        i=j=0
        unique_chars = 0
        substring_length = []
       
        while j<n:
            char_count_map[arr[j]] = char_count_map.get(arr[j],0)+1
            if char_count_map[arr[j]]==1:
                unique_chars+=1
            
            while unique_chars>k and i<=j:
                char_count_map[arr[i]] = char_count_map.get(arr[i])-1
                if char_count_map[arr[i]]==0:
                    unique_chars-=1
                    char_count_map.pop(arr[i])
                i+=1
            
            if unique_chars == k:
                substring_length.append(len(fruits[i:j+1]))
                # print(fruits[i:j+1],substring_length)
            
            j+=1
        if substring_length:
            return max(substring_length)
        else:
            return -1
        