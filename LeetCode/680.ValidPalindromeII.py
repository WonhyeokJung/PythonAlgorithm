# 1. My Solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        global result
        result = 0

        def palindromechecker(s_list: list, cnt: int):
            global result
            for i in range(len(s_list) // 2):
                if s_list[i] != s_list[len(s_list) - 1 - i]:
                    if cnt == 0:
                        new_s_list = s_list[:]
                        new_s_list.pop(i)
                        palindromechecker(new_s_list, 1)
                        s_list.pop(len(s_list) - 1 - i)
                        palindromechecker(s_list, 1)
                    return
            result = 1
            return

        strs = []
        for i in s:
            strs.append(i)
        palindromechecker(strs, 0)
        return result