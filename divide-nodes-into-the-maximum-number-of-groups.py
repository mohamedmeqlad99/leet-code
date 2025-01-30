class Solution:
    def magnificentSets(self, n, e):
        ajc = defaultdict(list)
        
        for i , j in e:
            ajc[i].append(j)
            ajc[j].append(i)
            
        def st(i):
            rt , cur , used , vi = 1 , [i] , {i} , [0] * (n+1)
            vi[i] = 1
            while cur:
                nxt = set()
                for v in cur:
                    for u in ajc[v]:
                        if vi[u] == rt:         
                            return -1 , -1      
                        elif vi[u] == 0:
                            used.add(u)
                            nxt.add(u)
                            vi[u] = rt +1
                cur = nxt
                if not cur: break
                rt += 1
            return min(used) , rt
                        
                
        ans = {}
        for j in range(1 , n+1):
            rep , rt = st(j)
            if rep == -1:
                return -1
            ans[rep] = max(ans.get(rep , 0) , rt)
                
        return sum(ans.values())
                        
        
