class Solution(object):
    def findTilt(self, root):
        if not root:
            return 0
        res = 0
        queue =[root]
        while queue:
            cur = queue.pop(0)
            res += abs(self.sumOfTree(cur.left)-self.sumOfTree(cur.right))
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res

    def sumOfTree(self, root):
        if not root:
            return 0
        return root.val+self.sumOfTree(root.left)+self.sumOfTree(root.right)

# another version, more efficient
class Solution(object):
    def findTilt(self, root):
        self.res = 0
        def _sum(Node):
            if not Node: return 0
            left = _sum(Node.left)
            right = _sum(Node.right)
            self.res += abs(left - right)
            return Node.val + left + right
        _sum(root)
        return self.res
