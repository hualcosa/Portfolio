"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        # In order to avoid cycles, we need a dictionary
        # to save the visited nodes as keys and respective clones
        # as values
        self.visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        # if node has already been visited before
        if node in self.visited:
            return self.visited[node]
        
        # Create a clone for the given node
        clone_node = Node(node.val, [])
        
        # add the node this node to the list of visited ones...
        self.visited[node] = clone_node
        
        # iterate through the neighbors to generate their clones
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone_node
        
            
        