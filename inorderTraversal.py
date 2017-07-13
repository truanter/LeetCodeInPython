# Definition for a binary tree node.
class TreeNode(object):
    
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#version1:Recursive


#version2:iteratively
class Solution(object):
    def inorderTraversal(self, root):
        if not root:return[]
        res = []
        stack = [[root, 0]]
        while stack:
            if stack[-1][0].left and not stack[-1][1]:
                stack[-1][1] = 1
                stack.append([stack[-1][0].left, 0])
            else:
                a = stack.pop()
                res.append(a[0].val)
                if a[0].right:
                    stack.append([a[0].right,0])
        return res

if __name__=='__main__':
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    a.left = b
    root.right = a
    s=Solution()
    print(s.inorderTraversal(root))
