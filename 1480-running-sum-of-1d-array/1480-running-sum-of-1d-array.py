class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        for i in range(len(nums)):
            sums.append(sum(nums[:i+1]))
        
        return sums