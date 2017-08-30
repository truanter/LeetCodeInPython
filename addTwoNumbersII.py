"""
:You are given two non-empty linked lists representing two non-negative integers. 
:The digits are stored in reverse order and each of their nodes contain a single digit.
:Add the two numbers and return it as a linked list.
:You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        return self.helper(l1,l2,0)
    def helper(self, a, b, flag):
        if a and b:
            curBit = a.val + b.val + flag
            a.val = curBit % 10
            flag = curBit // 10
            a.next = self.helper(a.next, b.next, flag)
            return a
        elif not a and not b:
            if not flag:return None
            else: return ListNode(1)
        else:
            if a: c = a
            if b: c = b
            if flag:
                d = c
                while d.val == 9:
                    d.val = 0
                    if not d.next:
                        d.next = ListNode(0)
                    d = d.next
                d.val += 1
            return c

#Version II
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        res = p = ListNode(0)
        flag = 0
        while l1 or l2 or flag:
            v = flag
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next
            flag, curBit = divmode(v, 10)
            p.next = ListNode(curBit)
            p = p.next
        return res.next
