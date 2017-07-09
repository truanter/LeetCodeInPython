class Solution:
    def tree2str(self, t):
        if not t:
            return ''
        if not t.left and not t.right:
            return str(t.val)
        elif t.left and t.right:
            return str(t.val)+'('+self.tree2str(t.left)+')'+'('+self.tree2str(t.right)+')'
        elif t.left:
            return str(t.val)+'('+self.tree2str(t.left)+')'
        else:
            return str(t.val)+'()('+self.tree2str(t.right)+')'

#version 2#
class Solution:
    def tree2str(self, t):
        if not t: return ''
        left = '({})'.format(self.tree2str(t.left)) if t.left or t.right else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(str(t.val),left,right)
