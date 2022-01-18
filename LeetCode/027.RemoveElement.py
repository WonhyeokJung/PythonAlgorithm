# 1. 41ms(35.22%) / 14.4mb
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        expectedNums = []
        
        for n in nums:
            if n != val:
                expectedNums.append(n)
                
        k = len(expectedNums)
        
        for i in range(len(expectedNums)):
            nums[i] = expectedNums[i]
        
        return k