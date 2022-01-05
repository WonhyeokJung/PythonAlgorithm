class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 접두사 찾기(맨앞부터 비교)
        # 최저 길이
        length = min(len(word) for word in strs)
        # 정답
        ans = ""
        # 제일 길이 짧은 단어만큼 돌면서
        for i in range(length):
            # 각 단어 알파벳 지정
            x = strs[0][i]

            # 각 단어 돌면서 일치 여부 확인
            for s in strs:
                if s[i] != x:
                    # 하나라도 불일치시 정답 반환
                    return ans
            # 일치시 단어 추가하고 다시 돈다
            ans += x

        # 마지막까지 탈출못했으면 최저길이 단어 반환
        return ans

