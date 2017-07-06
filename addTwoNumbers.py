class Solution(object):
    def addTwoNumbers(self, l1, l2):
        res = self.cal(l1)+self.cal(l2)
        r = ListNode(int(str(res)[0]))
        p = r
        for i in str(res)[1:]:
            p.next = ListNode(int(i))
            p = p.next
        return r
            
    def cal(self, l):
        if not l:
            return 0
        s = 0
        p = l
        while p.next:
            s = 10*s + p.val
            p = p.next
        s = 10*s + p.val
        return s
