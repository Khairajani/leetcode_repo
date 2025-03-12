# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        cousins = False
        if not root:
            return cousins
        
        level_parent_map = {}
        queue = [root]
        depth = -1
        while queue:
            depth+=1
            nodes_in_current_level = len(queue)
            for i in range(nodes_in_current_level):
                level_list = []
                current_node = queue.pop(0)
                level_list.append(current_node)

                if current_node.left:
                    queue.append(current_node.left)
                    if current_node.left.val in [x,y]:
                        level_parent_map[current_node.left.val] = [depth+1, current_node]
                if current_node.right:
                    queue.append(current_node.right)
                    if current_node.right.val in [x,y]:
                        level_parent_map[current_node.right.val] = [depth+1, current_node]
                
                if x in level_parent_map and y in level_parent_map:
                    if level_parent_map[x][0] == level_parent_map[y][0] and level_parent_map[x][1] != level_parent_map[y][1]:
                        cousins = True
                    break
                
        return cousins