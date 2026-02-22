from collections import deque

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False

        if target in (x, y, x + y):
            return True

        q = deque([0])
        visited = {0}

        states = (x, y, -x, -y)

        while q:
            cur = q.popleft()
            for s in states:
                next = cur + s

                if next == target:
                    return True

                if 0 <= next < x + y and next not in visited:
                    visited.add(next)
                    q.append(next)

        return False