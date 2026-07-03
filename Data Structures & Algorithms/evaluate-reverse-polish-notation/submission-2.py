class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        operators={'+','-','*','/'}
        
        for n in tokens:
            if n in operators:
                right=int(l.pop())
                left=int(l.pop())
                if n=='+':
                    l.append(str(left+right))
                elif n=='-':
                    l.append(str(left-right))
                elif n=='*':
                    l.append(str(left*right))
                else:
                    l.append(str(int(left/right)))
            else:
                l.append(n)
        
        return int(l.pop())

        