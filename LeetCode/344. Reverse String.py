# 1. My solution / Pythonic Way /184ms / 18.8MB

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

# 2. Two Pointer / 192ms /18.7MB
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# 두 방식에 유의미한 차이는 없다. / There is no significant difference