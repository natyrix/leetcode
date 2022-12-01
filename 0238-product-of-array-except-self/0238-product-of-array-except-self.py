class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        pref = 1
        for i in range(len(nums)):
            product[i] = pref
            pref *= nums[i]
        postf = 1
        for i in range(len(nums)-1,-1,-1):
            product[i] *= postf
            postf *= nums[i]
        return product
        