class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i,j in enumerate(nums):
            s[j]=i
        for i in range(len(nums)):
            c=target-nums[i]
            if c in nums and s[c]!=i:
                return [i,s[c]]


