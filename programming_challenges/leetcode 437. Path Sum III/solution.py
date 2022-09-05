# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def preorder(node: TreeNode, curr_sum):
            nonlocal count
            
            if not node:
                return
            # current prefix sum
            curr_sum += node.val
            
            if curr_sum == k:
                count += 1
                
            # number of times the curr_sum - k has already occured, determines the
            # number of times a path with sum k has occurred up to the current node
            count += h[curr_sum - k]
            
            # add the current sum into hashmap to use it during the child nodes processing
            h[curr_sum] += 1
            
            # process left subtree
            preorder(node.left, curr_sum)
            # process right subtree
            preorder(node.right, curr_sum)
            
            # remove the current sum from the hashmap in order not to use it during the parallel subtree processing
            h[curr_sum] -= 1
        
        count, k = 0, targetSum
        h = defaultdict(int)
        preorder(root, 0)
        return count