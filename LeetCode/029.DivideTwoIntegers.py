# 1. 47ms(28.92%) / 14.1mb(94.43%)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend // divisor >= 2**31:
            return 2**31-1
        if dividend // divisor > 0:
            return dividend // divisor
        
        else:
            return -(abs(dividend)//abs(divisor))