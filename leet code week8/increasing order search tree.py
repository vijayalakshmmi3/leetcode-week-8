# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l=[]
        self.newnode=TreeNode(0)
        self.curr=self.newnode
        def helper(root):
            if root:
                helper(root.left)
                self.curr.right=TreeNode(root.val)
                self.curr=self.curr.right
                helper(root.right)
        helper(root)
        return self.newnode.right
