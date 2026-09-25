class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1
        zero_cnt = 0

        for i in range(len(nums)):
            if nums[i]:
                prod *= nums[i]
            else:
                zero_cnt += 1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c
        return res


