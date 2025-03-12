# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        result = True
        if not root or (root.left==None and root.right==None):
            return result
    
        queue = [root.left, root.right]
        while queue:
            level_list = []
            
            left = queue.pop(0)
            right = queue.pop(0)
            # if both none
            if left is None and right is None:
                continue
            elif left and right and left.val == right.val:
                queue.append(left.left)
                queue.append(right.right)
                queue.append(left.right)
                queue.append(right.left)
            else:
                result = False
                break
        return result