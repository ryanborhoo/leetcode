# [94] https://leetcode.com/problems/binary-tree-inorder-traversal/
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
    #     # mid order
    #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    #     # # pre order
    #     # return [root.val] + self.inorderTraversal(root.left) + self.inorderTraversal(root.right)
    #     # # post order
    #     # return  self.inorderTraversal(root.left)  + self.inorderTraversal(root.right)+ [root.val]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(0, root)]
        while stack:
            visit, curr = stack.pop()
            if not curr:
                continue
            if visit == 0:
                # mid order
                stack.append((0, curr.right))
                stack.append((1, curr))
                stack.append((0, curr.left))
                # # pre order
                # stack.append((0, curr.right))
                # stack.append((0, curr.left))
                # stack.append((1, curr))
                # # post order
                # stack.append((1, curr))
                # stack.append((0, curr.right))
                # stack.append((0, curr.left))
            else:
                res.append(curr.val)
        return res
