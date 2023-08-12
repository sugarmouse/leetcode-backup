from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        cur = self
        res = ""
        while cur is not None:
            res += str(cur.val)
            cur = cur.next
            if cur is not None:
                res += " -> "
        return res

    @staticmethod
    def create_linked_list(lst):
        if len(lst) == 0:
            return None
        head = ListNode(lst[0])
        node = head
        for i in range(1, len(lst)):
            node.next = ListNode(lst[i])
            node = node.next
        return head
