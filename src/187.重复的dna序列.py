#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        nums = [0 for _ in range(len(s))]

        char_num = {
            'A': 0,
            'G': 1,
            'C': 2,
            'T': 3
        }

        for i in range(len(nums)):
            nums[i] = char_num[s[i]]

        seen = set()
        res = set()

        L = 10
        BASE = 4

        # 最高位权重
        RL = BASE ** (L - 1)

        hash_num = 0

        left = right = 0
        while right < len(nums):
            # 扩大窗口，移入字符
            hash_num = BASE * hash_num + nums[right]
            right += 1

            if right - left == L:
                # 达到长度，检测和记录
                if hash_num in seen:
                    res.add(s[left: right])
                else:
                    seen.add(hash_num)

                hash_num -= nums[left] * RL
                left += 1
        return list(res)

# @lc code=end
