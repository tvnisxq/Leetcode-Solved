# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Time: O(n); where n is the number of nodes in the tree
        # Space: O(n); where h is the height of the tree due to the recursive call stack
        def hasSum(root, currsum):
            if not root:
                return False
            
            currsum += root.val
            
            if not root.left and not root.right: 
                return currsum == targetSum

            return hasSum(root.left, currsum) or hasSum(root.right, currsum)
        return hasSum(root, 0)
            


            
