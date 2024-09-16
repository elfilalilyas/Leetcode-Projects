#-----------------------------------------------------the best solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = {}
        for i, n in enumerate(nums):
            num = target - n
            if num in ret:
                return [ret[num], i]
            ret[n] = i

