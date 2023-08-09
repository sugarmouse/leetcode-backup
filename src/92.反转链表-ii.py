#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left-1, right - 1)
        return head

    def reverseN(self, head: Optional[ListNode], n: int):
        """
        The function `reverseN` recursively reverses the first `n` nodes in a linked list.
        :return: the new head of the reversed linked list.
        """
        if n == 1 or n == 0 or head is None:
            return head
        b = self.reverseN(head, n - 1)
        newHead = head.next
        head.next = head.next.next
        newHead.next = b
        return newHead

# @lc code=end
