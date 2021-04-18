import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)  # dict value를 list로 받아온다.
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()