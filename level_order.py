"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        res = []
        if root:
            temp_list = [root]
            while len(temp_list):
                res.append(list(map(lambda x: x.val, temp_list)))
                temp_list = [x for j in temp_list for x in j.children]
        return res
