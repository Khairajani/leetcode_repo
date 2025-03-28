# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # code same as level order traversal
        result = []
        if not root:
            return result
        
        queue = [root]
        while queue:
            sum_of_elements_in_current_level = 0
            nodes_in_current_level = len(queue)
            for i in range(nodes_in_current_level):
                current_node = queue.pop(0)
                sum_of_elements_in_current_level+=current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            avg = sum_of_elements_in_current_level/nodes_in_current_level
            result.append(avg)
        return result