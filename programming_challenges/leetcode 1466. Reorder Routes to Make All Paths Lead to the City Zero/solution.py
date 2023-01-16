class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        edges = {(a,b) for a,b in connections}
        neighbors = {city:[] for city in range(n)}
        visit  = set()
        changes = 0
        
        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(city):
            nonlocal edges, neighbors, visit, changes
            
            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                # check if this neighbor can reach city 0
                if (neighbor, city) not in edges:
                    changes += 1
                # recursive call will make sure that the neighbor's neighbor 
                # can also reach 0
                visit.add(neighbor)
                dfs(neighbor)
        
        # entry point
        visit.add(0)
        dfs(0)
        return changes
        