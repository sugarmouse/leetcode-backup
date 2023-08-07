#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = defaultdict(int)
        res = 0

        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1

            # 当出现重复字符的时候需要移动左指针
            while window[c] > 1:
                d = s[left]
                window[d] -= 1
                left += 1
            
            res = max(res, right - left)

        return res

# @lc code=end

# tags: 滑动窗口
