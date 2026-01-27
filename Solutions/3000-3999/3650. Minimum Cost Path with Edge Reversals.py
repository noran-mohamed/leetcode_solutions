class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        maps = defaultdict(list)
        for u, v, w in edges:
            maps[u].append((v, w))
            maps[v].append((u, 2*w))
        
        visit = set()
        heap = [(0, 0)]

        while heap:
            dist, u = heappop(heap)

            if u == n - 1 :
                return dist
            
            if u in visit :
                continue
            visit.add(u)

            for v, w in maps[u] :
                newDist = dist + w
                heappush(heap, (newDist, v))
        
        return -1
        
