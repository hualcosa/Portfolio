# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse_tree(current_node):
            # if we reach the end of branch, return false
            if not current_node:
                return False

            # left Recursion
            left = recurse_tree(current_node.left)

            # right Recursion
            right = recurse_tree(current_node.right)

            # if the current node is one of p or q
            mid = current_node == p or current_node == q

            # if at least 2 of 3 flags become true
            if mid + left + right >= 2:
                self.ans = current_node

            # return true if either of the three bool values is true
            return mid or left or right
        
        recurse_tree(root)
    
        return self.ans