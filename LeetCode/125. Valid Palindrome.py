# My Solution / 40ms / memory : 20.1mb
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strnums = []
        for i in s:
            if i.isalnum():
                strnums.append(i.lower())

        if strnums == strnums[::-1]:
            return True
        return False
        # return strnums == strnums[::-1]

# 1. Use List / 276ms, 19.6MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # Palindrome check
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():  # pop(0) / O(n)
                return False
        return True


# 2. Use Deque 덱 자료형 사용 / 48ms / 19.2MB
import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Declare Deque Valuables
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # Palindrome check
        while len(strs) > 1:
            if strs.popleft() != strs.pop():  # popleft() / O(1)
                return False
        return True


# 3. Use slicing / 28ms / 15.6MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use Slicing
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


# 4. else
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_new = ""

        for i in s:
            if i.isalnum():
                s_new += i.lower()

        for j in range(int(len(s_new) / 2)):
            if s_new[j] == s_new[-1 - j]:  # Index Slicing
                continue
            else:
                return False

        return True