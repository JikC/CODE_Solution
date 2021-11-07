# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点
# fast先走n+1步，然后同时移动，直到fast到尾巴的None，删除slow的下一节点。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        fast, slow = dummy, dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
