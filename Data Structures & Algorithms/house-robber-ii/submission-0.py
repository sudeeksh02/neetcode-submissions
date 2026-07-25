class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp1=nums[:(n-1)]
        dp2=nums[1:]

        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        dp1[1]=max(nums[0],nums[1])
        dp2[1]=max(nums[1],nums[2])

        for i in range(2,n-1):
            dp1[i]=max(dp1[i-1],nums[i]+dp1[i-2])
            dp2[i]=max(dp2[i-1],nums[i+1]+dp2[i-2])


        return max(dp1[-1],dp2[-1])
