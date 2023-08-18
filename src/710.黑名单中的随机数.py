#
# @lc app=leetcode.cn id=710 lang=python3
#
# [710] 黑名单中的随机数
#

# @lc code=start
import random
from typing import List

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.dict = {}
        # 除去黑名单元素之后的白名单元素个数
        self.sz = n - len(blacklist)

        last = n - 1
        # 先把黑名单中的所有元素添加进 mapping
        for b in blacklist:
            self.dict[b] = -1

        for b in blacklist:
            # 当前黑名单元素本来就不会出现在调整过后的
            if b >= self.sz:
                continue
            # last 是在黑名单中的元素
            while last in self.dict:
                last -= 1

            self.dict[b] = last
            last -= 1


    def pick(self) -> int:
        index = random.randint(0, self.sz - 1)

        if index in self.dict:
            return self.dict[index]
        return index



# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end

