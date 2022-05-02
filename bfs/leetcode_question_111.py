# [111] https://leetcode.com/problems/minimum-depth-of-binary-tree/
# find the minimum depth of a binary tree.

from collections import deque
from collections import defaultdict
from collections import Counter


# def minDepth(root):
#     if not root:
#         return 0
#     # push height and node into queue
#     queue = [root]
#     height = 1
#     while queue:
#         n = len(queue)
#         for i in range(n):
#             node = queue.pop(0)
#             if not node.left and not node.right:
#                 return height
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         height += 1
#     return height

def minDepth(root):
    if not root:
        return 0
    # push height and node into queue
    queue = [(root, 1)]
    while queue:
        node, height = queue.pop(0)
        if not node.left and not node.right:
            return height
        if node.left:
            queue.append((node.left, height + 1))
        if node.right:
            queue.append((node.right, height + 1))

# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         leftHeight = self.minDepth(root.left)
#         rightHeight = self.minDepth(root.right)
#         if root.left != None and root.right == None:
#             return leftHeight + 1
#         if root.left == None and root.right != None:
#             return rightHeight + 1
#         return min(leftHeight, rightHeight) + 1
