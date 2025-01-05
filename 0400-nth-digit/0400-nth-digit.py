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

        start = low
        print(start)
        dl = self.digitCount(start)
        digits_till_now = self.getTotalDigits(self.digitCount(low-1))
        new_n = n - digits_till_now
        num = start + (new_n - 1) // dl
        print(num)
        
        # Find the position of the nth digit in the number
        di = (new_n - 1) % dl
        
        # Extract and return the nth digit
        return int(str(num)[di])

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
