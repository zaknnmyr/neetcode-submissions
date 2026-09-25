class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Two Pass

        ans = [] * 2 * len(nums)

        for x in range(2):
            for i in range(len(nums)):
                ans.append(nums[i])
        
        return ans