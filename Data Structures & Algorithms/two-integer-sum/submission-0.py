class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for x,y in enumerate(nums):
            s[y]=x
        for i in range(len(nums)):
            c=target-nums[i]
            if c in nums and s[c]!=i:
                ind=s[c]
                return [i,ind]

