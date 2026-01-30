from typing import List
import heapq
from collections import defaultdict

class Pair:
    def __init__(self, v: str, c: int):
        self.v = v
        self.c = c

    def __lt__(self, other):
        return self.c < other.c


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        self.source = source
        self.target = target
        self.original = original
        self.changed = changed
        self.cost = cost

        self.adj = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            self.adj[o].append(Pair(c, w))

        self.distMap = {}
        for s in set(original):
            self.distMap[s] = self._dijkstraAll(s)

        self.n = len(source)
        self.dp = [-1] * self.n

        ans = self._minCost(0)
        return -1 if ans == float("inf") else ans

    def _minCost(self, i: int) -> int:
        if i == self.n:
            return 0
        if self.dp[i] != -1:
            return self.dp[i]

        res = float("inf")

        if self.source[i] == self.target[i]:
            res = self._minCost(i + 1)

        for s in self.distMap:
            length = len(s)
            if i + length > self.n:
                continue

            if self.source.startswith(s, i):
                t = self.target[i:i + length]
                conv = self.distMap[s].get(t, float("inf"))
                if conv == float("inf"):
                    continue

                rest = self._minCost(i + length)
                if rest != float("inf"):
                    res = min(res, conv + rest)

        self.dp[i] = res
        return res

    def _dijkstraAll(self, start: str):
        pq = [(0, start)]
        dist = {}

        while pq:
            cur_cost, cur = heapq.heappop(pq)
            if cur in dist:
                continue

            dist[cur] = cur_cost

            for nxt in self.adj.get(cur, []):
                heapq.heappush(pq, (cur_cost + nxt.c, nxt.v))

        return dist
