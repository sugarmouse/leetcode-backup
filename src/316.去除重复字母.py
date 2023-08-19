#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
""" 
去重
保持原有顺序
最小字典序
"""
from typing import List
# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        # 用来记录还剩下没用过得字符
        count = [0 for _ in range(256)]
        for c in s:
            count[ord(c)] += 1
        # 用来记录那些字符出现过
        
        in_stack = [False] * 256
        for c in s:
            index = ord(c)
            count[index] -= 1
            
            # 如果改字符已经出现过了，则直接跳过
            if in_stack[ord(c)]:
                continue
            
            while res and res[-1] > c:
                if count[ord(res[-1])] == 0:
                    break
                in_stack[ord(res.pop())] = False
            
            # 添加当前元素
            res.append(c)
            in_stack[ord(c)] = True

        return ''.join(res)

# @lc code=end

