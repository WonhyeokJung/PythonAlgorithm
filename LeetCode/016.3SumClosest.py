class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Two Pointers
        nums = sorted(nums) # nums.sort() // nums = nums.sort() 아님에 주의
        
        ans = 9876543210 # 대항할 수 없는 큰 수
        
        i = 0
        # 3자리니까 뒤에 여유가 되도록 / for문을 사용한 경우는 015.3sum 참조
        while i < len(nums)-2:
            left = i + 1
            right = len(nums)-1
            
            while left < right:
                num = nums[i] + nums[left] + nums[right]
                
                # 숫자가 같으면
                if target - num == 0:
                    return target
                
                # Target - num이 더 크면 num 값이 더 커져야 하므로 left += 1
                elif target - num > 0:
                    if (target - num) > abs(target - ans):
                        pass
                    else:
                        ans = num
                    
                    # 중복값 제거
                    # while left < right and nums[left] == nums[left+1]:
                    #     left += 1
                    left += 1
                    
                else:
                    if (num - target) > abs(target - ans):
                        pass
                    else:
                        ans = num
                    
                    # 중복값 제거
                    # while left < right and nums[right] == nums[right-1]:
                    #     right -= 1
                    right -= 1
            
            
            # 중복값 피하기
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            i += 1
        
        
        return ans