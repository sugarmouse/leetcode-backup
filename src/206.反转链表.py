#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head

        next = head.next
        rest = self.reverseList(next)
        head.next = None
        cur = rest
        while cur.next:
            cur = cur.next
        cur.next = head
        return rest
# @lc code=end

