#
# @lc app=leetcode.cn id=1081 lang=python3
#
# [1081] 不同字符的最小子序列
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        res = []  # 维护最后的结果
        count = {} # 用来记录剩下的可用字符
        in_use = set() # 记录哪些已经在 res 中用过的字符

        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        for c in s:
            count[c] -= 1

            # 如果res 中已经用过当前字符，直接跳过
            if c in in_use:
                continue
            
            # 把字典序较大的字符尽量往后移，如果不能移的就留在原地
            while in_use and res[-1] > c:
                if count[res[-1]] == 0:
                    break
                in_use.remove(res[-1])
                res.pop()
                
            # 消费一个字符
            res.append(c)
            in_use.add(c)

        return ''.join(res)
# @lc code=end
