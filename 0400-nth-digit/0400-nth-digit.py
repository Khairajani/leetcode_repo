class Solution:
    # 1 digit: 9 numbers (total 9 digits)
    # 2 digits: 90 numbers (total 90*2 digits)
    # 3 digits: 900 numbers (total 900*3 digits)
    # 4 digits 9,000 numbers (total 9000*4 digits)
    # 5 digits 90,000 numbers (total 90000*5 digits)
    # and so on

    def digitCount(self,n):
        return len(str(n))

    def getTotalDigits(self,digit_count_in_high):
        total_digits_in_high = 0
        while digit_count_in_high>=1:
            total_digits_in_high+=9*(10**(digit_count_in_high-1))*(digit_count_in_high)
            digit_count_in_high-=1
        return total_digits_in_high

    def inDigitRange(self,high,n):
        digit_count_in_high = self.digitCount(high)
        total_digits_in_high = self.getTotalDigits(digit_count_in_high)
        # print(total_digits_in_high,n)
        if n<total_digits_in_high:
            return True
        return False

    def findNthDigit(self, n: int) -> int:
        if n<=9:
            return n

        low = 1
        high = 9
        while self.inDigitRange(high,n)==False:
            low = high+1
            high = ((high+1)*10)-1

        digit_length = self.digitCount(low)
        digits_till_now = self.getTotalDigits(digit_length-1)
        new_n = n - digits_till_now

        # Find the actual number that contains the nth digit
        num = low + (new_n - 1) // digit_length
        
        # Find the position of the nth digit in the number
        digit_index = (new_n - 1) % digit_length
        
        # Extract and return the nth digit
        return int(str(num)[digit_index])

        """
        digits_till_now = self.getTotalDigits(self.digitCount(low-1))
        while digits_till_now+digits_in_given_range<n:
            low = low+1
            digits_till_now+=digits_in_given_range
        
        elements = str(low)
        for e in elements:
            digits_till_now+=1
            if digits_till_now==n:
                return int(e)

        return -1
        """

    def findNthDigitOpti(self, n: int) -> int:
        # Initialize digit length (dl) to 1 for numbers 1-9, and count (c) of such numbers to 9
        dl, c = 1, 9
        
        # Loop to find the length of the number containing the nth digit
        while n > dl * c:
            n -= dl * c  # Subtract the digits counted so far
            dl += 1      # Increase digit length as we move to the next group (e.g., from 9 to 10, 99 to 100)
            c *= 10      # Increase the count for the next group of numbers
        
        # Calculate the start of the numbers with current digit length (dl)
        start = 10 ** (dl - 1)
        
        # Find the actual number that contains the nth digit
        num = start + (n - 1) // dl
        
        # Find the position of the nth digit in the number
        di = (n - 1) % dl
        
        # Extract and return the nth digit
        return int(str(num)[di])
