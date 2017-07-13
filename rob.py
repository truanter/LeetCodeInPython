class Solution(object):
    def rob(self, root):
        return self.helper(root, {})
    def helper(self, root, d):
        if not root: return 0
        if root in d: return d[root]
        res = 0
        if root.left:
            res += self.helper(root.left.left, d) + self.helper(root.left.right, d)
        if root.right:
            res += self.helper(root.right.left, d) + self.helper(root.right.right, d)
        res = max(res+root.val, self.helper(root.left, d)+self.helper(root.right, d))
        d[root] = res
        return res

#version 2
class Solution(object):
    def rob(self, root):
        res = self.helper(root)
        return max(res)
    def helper(self, root):
        res =[0,0]
        if nor root: return res
        left = self.helper(root.left)
        right = self.helper(root.right)
        res[0] = root.val + left[1] + right[1]
        res[1] = max(left) + max(right)
        return res
