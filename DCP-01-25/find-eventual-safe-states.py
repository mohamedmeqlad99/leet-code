class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        state = [0] * n
        safe = []

        def is_safe(node):
            if state[node] > 0:
                return state[node] == 2
            state[node] = 1
            for neighbor in graph[node]:
                if state[neighbor] == 1 or not is_safe(neighbor):
                    return False
            state[node] = 2
            return True

        for i in range(n):
            if is_safe(i):
                safe.append(i)

        return safe
