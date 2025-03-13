# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # similar to diameter of B.T.
    def helper(self,node):
        if not node:
            return 0        
        
        only_left = self.helper(node.left)
        if only_left<0:
            only_left = 0

        only_right = self.helper(node.right)
        if only_right<0:
            only_right = 0

        curr_node_val = node.val
        self.max_sum = max(self.max_sum, curr_node_val+only_left+only_right)
        return curr_node_val+max(only_left,only_right) 

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -1000
        self.helper(root)
        return self.max_sum
        