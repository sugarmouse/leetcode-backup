#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            p1 = self.findPalindrome(s, i, i)
            p2 = self.findPalindrome(s, i, i+1)
            tmp = p1 if len(p1) > len(p2) else p2
            res = res if len(res) > len(tmp) else tmp
        return res

    def findPalindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


# @lc code=end
