# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        
        self.head = head
        

    def getRandom(self):
        head = self.head
        res = head.val
        p = 1
        while head.next:
            if random.randint(0,p)==0:
                res = head.next.val
            p += 1
            head = head.next
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
