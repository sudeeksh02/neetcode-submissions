class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        res=[ord(t) for t in s if (t>='A' and t<='Z') or (t>='a' and t<='z') or (t>='0' and t<='9')]
       # print(res,type(res[0]))
        for i in range(len(res)):
            if res[i]>96:
                res[i]-=32

        print(res)

        if res==res[::-1]:
            return True
        else:
            return False
