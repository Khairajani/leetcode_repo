# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node,targetSum, arr):
        if not node:
            return
        
        if node.left==None and node.right==None and node.val==targetSum:
            self.arr.append(arr+[node.val])
            return
 
        self.helper(node.left,targetSum-node.val,arr+[node.val])
        self.helper(node.right,targetSum-node.val,arr+[node.val])

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.arr = []
        self.helper(root, targetSum, [])
        return self.arr
        