class Solution(object):
    def preorderTraversal(self, root):
        if not root: return []
        res,que = [],[root]
        while que:
            curNode = que.pop()
            res.append(curNode.val)
            if curNode.right:
                que.append(curNode.right)
            if curNode.left:
                que.append(curNode.left)
        return res
            
