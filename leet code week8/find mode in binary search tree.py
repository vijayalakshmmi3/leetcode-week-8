# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        res_count = 0 
        curr = None
        curr_count = 0
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            nonlocal res, res_count, curr, curr_count
            if node.val == curr:
                curr_count += 1
            else:
                curr = node.val
                curr_count = 1
            if curr_count > res_count:
                res = [curr]
                res_count = curr_count
            elif curr_count == res_count:
                res.append(node.val)
            traverse(node.right)
        traverse(root)
        return res
