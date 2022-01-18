# 1. 234ms 98.50% / 14.3mb 84.60%
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0
        
        elif needle in haystack:
            return haystack.index(needle)
        
        return -1