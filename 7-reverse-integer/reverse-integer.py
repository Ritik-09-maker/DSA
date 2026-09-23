
class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        rev = 0

        while num > 0:
            last_digit = num % 10
            rev = rev * 10 + last_digit
            num = num // 10

        if x < 0:
            rev = -rev

        # 32-bit integer range check
        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev
