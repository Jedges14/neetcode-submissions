# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        d = deque([(root, float('-inf'), float('inf'))])

        while d:
            node, left, right = d.popleft()

            if not (left<node.val<right): return False

            if node.left:
                d.append((node.left, left, node.val))

            if node.right:
                d.append((node.right,node.val, right))

        return True