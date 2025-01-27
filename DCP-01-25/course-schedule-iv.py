class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        
        graph = {}
        for p in prerequisites:
            if p[0] not in graph:
                graph[p[0]]=[p[1]]
            else:
                graph[p[0]].append(p[1])
        def dfs(s, find):
            visited = [0]*numCourses
            stack = [s]
            visited[s]= 1
            while stack:
                o = stack.pop()
                if o in graph:
                   for n in graph[o]:
                     if not visited[n]:
                        if n==find:
                            return True
                        stack.append(n)
                        visited[n]= 1
            return False
        return [dfs(q[0], q[1]) for q in queries] 
