#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.container = nestedList

    def next(self) -> int:
        return self.container.pop(0).getInteger()

    def hasNext(self) -> bool:
        while self.container and not self.container[0].isInteger():
            first = self.container.pop(0).getList()
            for i in range(len(first)-1, -1, -1):
                self.container.insert(0, first[i])
        return len(self.container) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        self.flatten(nestedList)

    def next(self) -> int:
        if self.hasNext():
            return self.res.pop(0)

    def hasNext(self) -> bool:
        return len(self.res) != 0

    def flatten(self, nestedList: [NestedInteger]):
        for ele in nestedList:
            if ele.isInteger():
                self.res.append(ele)
            else:
                self.flatten(ele.getList())
