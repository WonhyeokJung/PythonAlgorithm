# MergeSort / Divine and Conquer Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        # 좌우로 나뉘어 Divine
        left = self.majorityElement(nums[:len(nums) // 2])
        right = self.majorityElement(nums[len(nums) // 2:])

        # left 숫자가 함수의 인자 nums list의 과반수를 초과하면, [right, left][1(True)]로 left 반환.
        return [right, left][nums.count(left) > len(nums) // 2]