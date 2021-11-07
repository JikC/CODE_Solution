# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        pre = dummy
        while pre.next and pre.next.next:
            cur, post = pre.next, pre.next.next
            cur.next = post.next
            post.next = cur
            pre.next = post
            pre = pre.next.next
        return dummy.next
