# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        
        node = root.val
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return f"{node},{left},{right}"
        
    def deserialize_helper(self, arr):
        if len(arr)==0:
            return 
        
        current_val = arr.pop(0)
        if current_val=='null':
            return
        
        current_node = TreeNode(int(current_val))
        left_node = self.deserialize_helper(arr)
        right_node = self.deserialize_helper(arr)
        if left_node:
            current_node.left = left_node
        if right_node:
            current_node.right = right_node
        return current_node



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        print(data.split(","))
        return self.deserialize_helper(data.split(","))
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))