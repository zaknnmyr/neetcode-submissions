# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        q = deque()
        q.append(root)

        while q:
            tmp = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    tmp.append(node.val)
                else:
                    break
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if tmp:
                output.append(tmp)
        return output
            