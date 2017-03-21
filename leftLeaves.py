class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root:
            if root.left or root.right:
                if root.left:
                    l=root.left
                    if l.left==None and l.right==None:
                        return self.sumOfLeftLeaves(root.right) + l.val
                    else:
                        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
                else:
                    return self.sumOfLeftLeaves(root.right)
            else:
                return 0
        else:
            return 0
