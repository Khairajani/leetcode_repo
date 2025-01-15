class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        x_len = len(image)
        y_len = len(image[0])
        for i in range(x_len):
            low = 0
            high = y_len-1
            while low<=high:
                image[i][low],image[i][high] = 1^image[i][high],1^image[i][low]
                low+=1
                high-=1
        return image
