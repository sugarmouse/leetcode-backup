#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        a, b = head, head
        for _ in range(k):
            if b is None:
                return head
            b = b.next

        new_head = self.reverseBetween(a, b)
        a.next = self.reverseKGroup(b, k)

        return new_head

    def reverseBetween(self, a: Optional[ListNode], b: Optional[ListNode]) -> ListNode:
        pre, cur, next = None, a, a
        while cur != b:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


# @lc code=end
