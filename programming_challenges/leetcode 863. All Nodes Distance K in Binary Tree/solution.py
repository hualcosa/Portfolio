class Solution(object):
    def distanceK(self, root, target, K):
        ans = []

        # Return distance from node to target if exists, else -1
        # Vertex distance: the # of vertices on the path from node to target
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                L, R = dfs(node.left), dfs(node.right)
                if L != -1:
                    if L == K: ans.append(node.val)
                    subtree_add(node.right, L + 1)
                    return L + 1
                elif R != -1:
                    if R == K: ans.append(node.val)
                    subtree_add(node.left, R + 1)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                ans.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return ans