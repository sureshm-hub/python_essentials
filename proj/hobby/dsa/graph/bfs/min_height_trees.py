from collections import deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if(n <= 2):
            return list(range(n))

        # graph of edges

        deg = [0] * n
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            deg[a] += 1
            deg[b] += 1

        leaves = deque(i for i in range(n) if deg[i] == 1)

        rem = n

        while(rem > 2):
            sz = len(leaves)
            rem -= sz

            for _ in range(sz):
                leaf = leaves.popleft()
                for nbr in graph[leaf]:
                    deg[nbr] -= 1
                    if deg[nbr] == 1:
                        leaves.append(nbr)

        return list(leaves)