class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        sub=len(s)

        match=0
        idx=0
        for i in range(len(t)):
            if t[i]==s[idx]:
                idx+=1
                match+=1
            if idx==sub:
                break

        return True if match==sub else False
