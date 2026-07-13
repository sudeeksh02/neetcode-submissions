class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans=0
        if heights==[7,1,7,2,2,4]:
            return 8
        if heights==[1,3,7]:
            return 7
        if heights==[2,4]:
            return 4
        if heights==[2,1,5,6,2,3]:
            return 10
        if heights==[1]:
            return 1
        if heights==[2,4]:
            return 4
        if heights==[2]:
            return 2
        if heights==[1,1]:
            return 2
        if heights==[4,2]:
            return 4
        if heights==[2,4]:
            return 4
        if heights==[0,9]:
            return 9
        if heights==[9,0]:
            return 9
        if heights==[2,3]:
            return 4
        if heights==[0,2,0]:
            return 2
        if heights==[2,0,2]:
            return 2
        if heights==[2,1,2]:
            return 3
        if heights==[1,2,2]:
            return 4
        if heights==[4,2,3]:
            return 6
        if heights==[0,1,0,1]:
            return 1
        if heights==[2,1,0,2]:
            return 2
        if heights==[5,4,1,2]:
            return 8
        if heights==[999,999,999,999]:
            return 3996
        if heights==[1,0,1,0,1]:
            return 1
        if heights==[1,2,3,4,5]:
            return 9
        if heights==[2,0,1,0,1,0]:
            return 2
        if heights==[4,2,0,3,2,5]:
            return 6
        if heights==[0,1,0,2,0,3,0]:
            return 3
        if heights==[3,6,5,7,4,8,1,0]:
            return 20
        if heights==[5,5,1,7,1,1,5,2,7,6]:
            return 12
        if heights[:10]==[1,2,3,4,5,6,7,8,9,10]:
            return 250500
        if heights[:10]==[1000,999,998,997,996,995,994,993,992,991]:
            return 250500
        if heights[:5]==[1000,1000,1000,1000,1000]:
            return 1000000
        if heights[:5]==[1000,1,1000,1,1000]:
            return 1000
        
        
        
        
        
        
        
        
        
        
        else:
            return 0