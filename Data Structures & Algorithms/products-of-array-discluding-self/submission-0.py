class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zer=0
        for i in nums:
            if i==0:
                zer+=1
        if zer>1:
            return [0]*len(nums)
        n_zer=1
        prod=1
        for i in nums:
            if i!=0:
                n_zer*=i
            prod*=i
        out=[]
        for i in nums:
            if i==0:
                out.append(n_zer)
            else:
                out.append(int(prod/i))
        return out
        

        