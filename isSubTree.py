class Solution:
    def isSubtree(self, s, t):
        queue=[s]
        while queue:
            for i in queue:
                if self.isSame(i,t):
                    return True
            queue=[kid for node in queue for kid in(node.left,node.right) if kid !=None]
        return False

    def isSame(self, s, t):
        if not s and not t:return True
        return s.val==t.val and self.isSame(s.left,t.left) and self.isSame(s.right,t.right)
    
class Solution:
    def isSubtree(self, s, t):
        if self.isSame(s,t):return True
        if not s: return False
        return self.isSubtree(s.right, t) or self.isSubtree(s.left,t)
    def isSame(self, s, t):
        if not s and not t:return True
        return s.val==t.val and self.isSame(s.left,t.left) and self.isSame(s.right,t.right)
