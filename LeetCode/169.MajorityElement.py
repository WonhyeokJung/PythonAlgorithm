# MergeSort / Divine and Conquer Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        # 좌우로 나뉘어 Divine
        middle = len(nums) // 2
        # 여기서 아래로 내려갈때마다 새로운 nums list가 만들어지고 기억하고 있음을 유의.
        left = self.majorityElement(nums[:middle])
        right = self.majorityElement(nums[middle:])

        # left 숫자가 함수의 인자 nums list의 과반수를 초과하면, [right, left][1(True)]로 left 반환.
        return [right,left][nums.count(left) > middle]

# Pythonic Way
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 과반수 이상 존재하는 숫자가 있다는 가정이 있으므로.
        return sorted(nums)[len(nums)//2]