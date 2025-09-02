# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        O(n) solution:
        """
        def pre(node):
            if not node: return 0
            return pre(node.left) + pre(node.right) + 1
        return pre(root)