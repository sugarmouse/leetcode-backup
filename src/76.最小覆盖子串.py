#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lo, hi = 0, 0

        need, window = defaultdict(int), defaultdict(int)
        valid = 0

        res = s
        hasStr = False

        for c in t:
            need[c] += 1

        while hi < len(s):
            curChar = s[hi]
            window[curChar] += 1
            if curChar in need and window[curChar] == need[curChar]:
                valid += 1

            hi += 1
            # s[lo, hi) 表示当前窗口截取的字符串

            while lo < hi and valid >= len(need):
                # 表示 s 有完全覆盖 t 的子串
                hasStr = True
                res = res if len(res) <= len(s[lo:hi]) else s[lo:hi]
                # 更新窗口信息
                window[s[lo]] -= 1
                if s[lo] in need and window[s[lo]] < need[s[lo]]:
                    valid -= 1
                lo += 1

        return res if hasStr else ""


# @lc code=end
