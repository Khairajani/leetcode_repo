# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, s):
        if node.left is None and node.right is None:
            self.arr.append(s+str(node.val))
            return

        if node.left:
            self.helper(node.left, s+str(node.val))
        if node.right:
            self.helper(node.right, s+str(node.val))
        return
            
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        self.helper(root,"")
        return sum([int(element) for element in self.arr])
        
        val = root.val

        

        