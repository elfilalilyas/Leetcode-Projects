#-----------------------------------------------------the best solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_nums = {}
        for i, n in enumerate(nums):
            num = target - n
            if num in ret:
                return [checked_nums[num], i]
            checked_nums[n] = i

