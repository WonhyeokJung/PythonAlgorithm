# 1.Using sets ( 50ms 14.42% / 14mb 94.65%)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        dic  = {}
        
        if len(pattern) != len(s):
            return False
        if len(set(pattern)) != len(set(s)):
            return False # 'abba' and ['dog', 'cat', 'cat', 'fish']
        
        for i in range(len(pattern)):
            if s[i] not in dic:
                dic[s[i]] = pattern[i]
            elif dic[s[i]] != pattern[i]:
                return False
        
        return True