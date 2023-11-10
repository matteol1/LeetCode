# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack = [root]
        visited = set()
        tree_length = 1
        while stack:
            if len(stack)>tree_length:
                tree_length = len(stack)
            print(f"max length: {len(stack)}")
            current_node = stack[-1]
            if current_node not in visited:
                if current_node.left is not None and current_node.left not in visited:
                    stack.append(current_node.left)
                elif current_node.right is not None and current_node.right not in visited:
                    stack.append(current_node.right)
                else:
                    visited.add(current_node)
                    stack.pop(-1)
        return tree_length
            


#        def check_function(node, depth, tree_length):
 #           print(tree_length)
  #          if depth> tree_length:
   ##             tree_length = depth
     #       if node.left is not None:
      #          return check_function(node.left, depth+1, tree_length)
       #     if node.right is not None:
        #        return check_function(node.right, depth+1, tree_length)
    #        return tree_length
     #   return check_function(root, 1, 1)


x1 = TreeNode()
x2 = TreeNode()
x3 = TreeNode()
x4 = TreeNode()
x5 = TreeNode()

x1.left = x2
x1.right = x3
x3.left = x4
x3.right = x5
x1.val = 3
x2.val = 9
x3.val = 20
x4.val = 15
x5.val = 7


sol = Solution()
print(sol.maxDepth(x1))