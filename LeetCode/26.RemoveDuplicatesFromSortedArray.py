# 1. Using extra array & Set ( 76ms / 15.5mb memory Usage)
# O(1) extra memory is allowed.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = list(set(nums)) 등은 작동하지 않는다.
        # 반드시 nums의 원소값을 직접 변경해서(nums[1]=1) 완성해야 한다.
        
        expectedNums = sorted(list(set(nums)))
        k = len(expectedNums)
        for i in range(k):
            nums[i] = expectedNums[i]
        
        return k

# 2. One pointer ( 80ms / 15.7mb )
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastIdx = 0
        
        for i in range(len(nums)):
            if nums[lastIdx] != nums[i]:
                lastIdx += 1
                nums[lastIdx] = nums[i]
        
        return lastIdx+1