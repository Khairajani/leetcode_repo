# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder)==0 or len(inorder)==0:
            return None
        current_val = postorder.pop(-1)
        current_node = TreeNode(current_val)

        current_val_index = inorder.index(current_val)
        current_node.right = self.buildTree(inorder[current_val_index+1:],postorder)
        current_node.left = self.buildTree(inorder[:current_val_index], postorder)
        

        return current_node