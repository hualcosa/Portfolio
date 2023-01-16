class Solution(object):
    from collections import defaultdict
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        N = len(equations)
        # creating the graph
        for i in range(N):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1/values[i]
        
        def dfs(x, y, visited):
            # if x or y not in the graph, we return -1
            if x not in graph or y not in graph: return -1
            
            # if y is in graph[x], the result is immediate
            if y in graph[x]:
                return graph[x][y]
            # otherwise we perform the dfs
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, y, visited)
                    if temp == -1:
                        continue
                    else:
                        return temp * graph[x][i]
            return -1
        
        output = []
        for p, q in queries:
            output.append(dfs(p,q,set()))
        return output