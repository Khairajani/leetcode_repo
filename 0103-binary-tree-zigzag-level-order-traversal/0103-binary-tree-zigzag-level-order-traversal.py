# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:    
        if not root:
            return []

        queue_ds = [root]
        traversal_output = []
        count = 0

        while len(queue_ds):
            level_list = []
            nodes_in_current_level = len(queue_ds)
            for i in range(nodes_in_current_level):
                curr_node = queue_ds.pop(0)
                level_list.append(curr_node.val)
                if curr_node.left:
                    queue_ds.append(curr_node.left)
                if curr_node.right:
                    queue_ds.append(curr_node.right)
                
            if count%2==0:
                traversal_output.append(level_list)
            else:
                traversal_output.append(level_list[::-1])
            count+=1
        return traversal_output


