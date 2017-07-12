'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
'''
class Solution:
    def averageOfLevels(self, root):
        res=[]
        queue=[root]
        while queue:
            res.append(sum(i.val for i in queue)/len(queue))
            queue=[kid for node in queue for kid in (node.left, node.right) if kid != None]
        return res
