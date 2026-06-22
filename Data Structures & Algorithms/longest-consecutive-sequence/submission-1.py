class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        nums.sort()
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]==nums[i]-1:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp) if dp else  0
        