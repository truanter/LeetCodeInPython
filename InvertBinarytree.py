class Solution(obj):
    def invertTree(self,root):
        if root:
            root.left,root.right=root.right,root.left
            map(self.invertTree,(root.left,root.right))
        return root
