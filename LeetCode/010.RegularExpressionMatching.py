# 하기 모든 코드는 len(arr)-1부터 역순으로 도는 코드이다.
# 1. 파이썬 내장 데코레이터 적용한 코드(decorater 사용시 62ms / 미사용시 3000ms)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # *은 앞의 문자를 0~무한번 반복할 수 있으며, .은 임의의 문자 하나를 대표한다.
        if p == '.*':
            return True
        
        def dp(slen, plen):
            # 둘다 비었을 때
            if slen == plen == -1:
                return True
            # p에 남은게 없지만 s는 남은게 있을 때
            if (slen > -1 and plen == -1) or (slen == -1 and p[plen] != '*'):
                return False
            
            
            if s[slen] == p[plen] or p[plen] == '.':
                return dp(slen-1, plen-1)
            
            elif p[plen] == '*':
                print(s[slen], p[plen])
                if slen > -1 and (s[slen] == p[plen-1] or p[plen-1] == '.'):
                    if slen == 0 and plen == 1:
                        return True
                    # x*을 제거하거나 x*을 살려두거나 x값을 제거 후 다음 x값과 비교
                    return dp(slen-1, plen-2) or dp(slen, plen-2) or dp(slen-1, plen)
                else:
                    return dp(slen, plen-2)
            else:
                return False
        
        return dp(len(s)-1, len(p)-1)


# 2. 직접 Cache 구현 (48ms)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # *은 앞의 문자를 0~무한번 반복할 수 있으며, .은 임의의 문자 하나를 대표한다.
        if p == '.*':
            return True
        # built-in memoization decorater 사용시 62ms의 속도 보장
        # @cache
        
        # 캐시 구현(memoization)
        cache = {}
        def dp(slen, plen):
            if (slen,plen) in cache:
                return cache[(slen,plen)]
            # 둘다 비었을 때
            if slen == plen == -1:
                cache[(slen,plen)] = True 
                return True
            # p에 남은게 없지만 s는 남은게 있을 때
            elif (slen > -1 and plen == -1) or (slen == -1 and p[plen] != '*'):
                cache[(slen,plen)] = False
                return False
            else:
                if s[slen] == p[plen] or p[plen] == '.':
                    cache[(slen-1,plen-1)] = dp(slen-1, plen-1)
                    return cache[(slen-1,plen-1)]

                elif p[plen] == '*':
                    # s에 아직 값이 있으며 / *의 앞단어가 s와 같을 때
                    if slen > -1 and (s[slen] == p[plen-1] or p[plen-1] == '.'):
                        if slen == 0 and plen == 1:
                            return True
                        cache[(slen-1,plen-2)], cache[(slen,plen-2)], cache[(slen-1,plen)] = dp(slen-1, plen-2), dp(slen, plen-2), dp(slen-1, plen)
                        # x*을 제거하거나 x*을 살려두거나 x값을 제거 후 다음 x값과 비교
                        return cache[(slen-1,plen-2)] or cache[(slen,plen-2)] or cache[(slen-1,plen)]
                    else:
                        cache[(slen,plen-2)] = dp(slen, plen-2)
                        return cache[(slen,plen-2)]
                else:
                    cache[str(slen)+str(plen)] = False
                    return False
        return dp(len(s)-1, len(p)-1)


# 3. 2번의 캐시 활용을 깔끔하게 변형한 코드
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # *은 앞의 문자를 0~무한번 반복할 수 있으며, .은 임의의 문자 하나를 대표한다.
        if p == '.*':
            return True
        # built-in memoization decorater 사용시 62ms의 속도 보장
        # @cache
        
        # 캐시 구현(memoization)
        cache = {}
        def dp(slen, plen):
            if (slen,plen) in cache:
                return cache[(slen,plen)]
            # 둘다 비었을 때
            if slen == plen == -1:
                ans = True
            # p에 남은게 없지만 s는 남은게 있을 때
            elif (slen > -1 and plen == -1) or (slen == -1 and p[plen] != '*'):
                ans = False
            
            else:
                if s[slen] == p[plen] or p[plen] == '.':
                    ans = dp(slen-1, plen-1)

                elif p[plen] == '*':
                    # s에 아직 값이 있으며 / *의 앞단어가 s와 같을 때
                    if slen > -1 and (s[slen] == p[plen-1] or p[plen-1] == '.'):
                        if slen == 0 and plen == 1:
                            ans = True
                        # x*을 제거하거나 x*을 살려두거나 x값을 제거 후 다음 x값과 비교
                        ans = dp(slen-1, plen-2) or dp(slen, plen-2) or dp(slen-1, plen)
                    else:
                        ans = dp(slen, plen-2)
                else:
                    ans = False
            
            cache[(slen, plen)] = ans
            return ans
        return dp(len(s)-1, len(p)-1)