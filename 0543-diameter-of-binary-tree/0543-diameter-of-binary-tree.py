# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """DFS Solution"""
        """
        TIME: O(n); just doing a bunch of constant time operations 
        for every single node in the tree like calculating left & 
        right heights, diameter and largest diameter of the Tree. 
        
        SPACE: O(h); h is the number of nodes in the tree. We're 
        keeping the height of the call stack open. DFS is goig down 
        in the bottom and collecting it back upwards. 
        """
        largest_d = [0]
        
        def height(root):
            if root is None:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)
            diameter= left_height + right_height
            largest_d[0] = max(largest_d[0], diameter)

            return 1 + max(left_height, right_height)
        
        height(root)
        return largest_d[0]