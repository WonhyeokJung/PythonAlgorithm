class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two pointers
        nums = sorted(nums)
        ans = []
        
        for i in range(len(nums)-1):
            # 중복값이 있을 시 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                # 한 타임 건너뛰기
                continue
    
            
            left = i + 1
            right = len(nums)-1
            
            while left < right:
                sums = nums[left] + nums[i] + nums[right]
                if sums > 0:
                    right -= 1
                elif sums < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    # 같은 숫자가 반복되는 경우 중복 덧셈 피하기 위해 값을 올려줌.
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                        
                    # 중복이 끝난 경우 왼쪽 값을 하나 올림.
                    left += 1
        
        return ans