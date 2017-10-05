class Solution:
    def findTarget(self, root, k):
        if not root:return False
        node, v = [root],[]
        for i in node:
            if k-i.val in v:return True
            v.append(i.val)
            if i.left: node.append(i.left)
            if i.right: node.append(i.right)
        return False 
