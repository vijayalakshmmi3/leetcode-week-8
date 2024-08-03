# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum=0
        def helper(root):
            if not root:
                return
            if low<=root.val<=high:
                self.sum+=root.val
            helper(root.left) 
            helper(root.right) 
        helper(root)
        return self.sum
