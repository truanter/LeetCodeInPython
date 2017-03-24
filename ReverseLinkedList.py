# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n=head
        l=[]
        while n != None:
            l.append(n.val)
            n=n.next
        m=head
        for i in l[::-1]:
            m.val=i
            m=m.next
        return head
