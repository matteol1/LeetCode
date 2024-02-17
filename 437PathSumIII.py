# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        n_solutions = 0

        if root.left == 'null' and root.right == 'null':
            return root.val
        if root.val == targetSum:
            n_solutions+=1
        new_target = targetSum - root.val
        #should run a case including the current node, 
        # and a case excluding it
        if root.left is not 'null':
            self.pathSum(root.left, new_target)
            self.pathSum(root.left, targetSum=)
        if root.right is not 'null':
            self.pathSum(root.right, new_target)
            self.pathSum(root.right, targetSum)
