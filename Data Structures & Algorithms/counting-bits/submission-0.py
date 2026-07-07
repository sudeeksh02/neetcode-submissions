class Solution:
    def ones(self,n):
        count=0
        for i in range(32):
            if n & (1<<i):
                count+=1
        return count
    def countBits(self, n: int) -> List[int]:
        output=[0]*(n+1)
        for i in range(n+1):
            output[i]=self.ones(i)
        return output
        