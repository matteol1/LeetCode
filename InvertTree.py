# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == []:
            return []
        #have to do with a stack / recursively

        def dfs_invert(node):
            if node is not None:
                if node.left is not None or node.right is not None:
                    curr_right = node.right
                    node.right = dfs_invert(node.left) if node.left else None
                    node.left = dfs_invert(curr_right) if curr_right else None
                return node
            return None

        root = dfs_invert(root)

a = TreeNode()
b = TreeNode()
c= TreeNode()
a.left = b
a.right = c
a.val = 2
b.val = 1 
c.val = 3

print(a.left.val)
print(a.right.val)
sol=Solution()
a = sol.invertTree(a)
print(a.left.val)
print(a.right.val)