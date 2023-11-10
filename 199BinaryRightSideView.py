# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        result = []
        if root is not None:
            queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i==0:
                    result.append(node.val)
                if node.right is not None:
                    queue.append(node.right)
                if node.left is not None:
                    queue.append(node.left)

        return result        