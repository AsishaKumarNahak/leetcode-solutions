class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        for ch in str(n):
            d = int(ch)
            digit_sum += d
            digit_product *= d
        return n % (digit_sum + digit_product) == 0