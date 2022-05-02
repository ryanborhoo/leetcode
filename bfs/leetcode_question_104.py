# [104] https://leetcode.com/problems/maximum-depth-of-binary-tree/
# find the max depth of a binary tree.


# def maxDepth(root):
#     if not root:
#         return 0
#     # push height and node into queue
#     queue = [root]
#     depth = 0
#     while queue:
#         n = len(queue)
#         for i in range(n):
#             node = queue.pop(0)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         depth += 1
#     return depth
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)
        return max(leftHeight, rightHeight) + 1
