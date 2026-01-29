class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        costs = [[float("inf")] * 26 for i in range(26)]

        for orig, chg, cst in zip(original, changed, cost) :
            start = ord(orig) - ord("a")
            end = ord(chg) - ord("a")
            costs[start][end] = min(costs[start][end], cst)

        for k in range(26) :
            for i in range(26) :
                for j in range(26) :
                    costs[i][j] = min(costs[i][j], costs[i][k]+ costs[k][j])
        
        res = 0
        for s, t in zip(source, target) :
            if s == t:
                continue
            
            src = ord(s) - ord("a")
            tgt = ord(t) - ord("a")

            if costs[src][tgt] == float("inf") :
                return -1
            res += costs[src][tgt]

        return res
                
        
