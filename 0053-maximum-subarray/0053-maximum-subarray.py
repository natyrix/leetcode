class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mSum = nums[0]
        s = 0
        for n in nums:
            if s < 0:
                s = 0
            s += n
            mSum = max(mSum,s)
        return mSum