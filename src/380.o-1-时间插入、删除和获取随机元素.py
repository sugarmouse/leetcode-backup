#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start

# hash 表结合数组
# hash 表记录元素对应的下标
# 数组保存元素，为了 O(1) 的 getRandom
import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []
        self.len = 0

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = self.len
        self.arr.append(val)
        self.len += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        index = self.dict[val]
        last_val = self.arr[self.len - 1]

        # 更新 dict
        # self.dict[val] = self.len - 1
        self.dict[last_val] = index

        # 更新 arr
        self.arr[index], self.arr[self.len - 1] = self.arr[self.len - 1], self.arr[index]

        # 删除元素
        self.arr.pop()
        self.dict.pop(val)
        self.len -= 1

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
