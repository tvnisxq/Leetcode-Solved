class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def same(p, q):
            if not p and not q:
                return True
            
            if not p or not q or p.val != q.val:
                return False
            
            return same(p.left, q.left) and same(p.right, q.right)
        
        return same(p, q)