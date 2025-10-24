class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetry(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
            
            return symmetry(root1.left, root2.right) and \
                   symmetry(root1.right, root2.left) 
        
        return symmetry(root, root)