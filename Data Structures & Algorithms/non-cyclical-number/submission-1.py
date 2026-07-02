class Solution:
    def sumsq(self,n):
        sum=0
        while n:
            sum+= (n%10)*(n%10)
            n//=10
        return sum
    
    
    
    def isHappy(self, n: int) -> bool:
        l=[]
        while True:
            if self.sumsq(n)==1:
                return True
            elif self.sumsq(n) in l:
                return False
            l.append(n)
            n=self.sumsq(n)
            
        
        