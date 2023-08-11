#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 翻转后半部分链表，然后头尾比较
class Solution:
    left = None

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        if fast is not None and fast is not slow:
            # 说明链表节点个数是奇数
            slow = slow.next

        left, right = head, self.reverse(slow)

        # 链表两头相向比较
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        翻转后半部分链表，返回翻转后的头（也就是原链表的尾节点）
        """
        pre, cur = None, head
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

# @lc code=end


# 通过链表的递归从后往前访问链表元素
# 外部变量 left 从前往后访问链表元素
class Solution_1:
    left = None

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        return self.traverse(head)

    def traverse(self, right: Optional[ListNode]):
        if right is None:
            return True
        res = self.traverse(right.next)
        res = res and (right.val == self.left.val)
        # 后移左指针
        # 右指针在 归 的过程中会向左移
        self.left = self.left.next
        return res
