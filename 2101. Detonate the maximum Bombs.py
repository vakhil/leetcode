from collections import defaultdict
from typing import List
import math

class Solution:
    def intersectCircle(self, bomb1: List[int], bomb2: List[int]) -> bool:
        # Check if bomb2 is within bomb1's explosion radius
        return (bomb1[0] - bomb2[0])**2 + (bomb1[1] - bomb2[1])**2 <= bomb1[2] ** 2

    def dfs(self, bomb_index: int, bombs_neighbor: dict, bombs_visited: dict) -> int:
        bombs_visited[bomb_index] = True
        count = 1  # Count the current bomb
        for x in bombs_neighbor[bomb_index]:
            if not bombs_visited[x]:
                count += self.dfs(x, bombs_neighbor, bombs_visited)
        return count

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bombs_neighbor = defaultdict(list)
        n = len(bombs)

        # Construct adjacency list
        for i in range(n):
            for j in range(n):
                if i != j and self.intersectCircle(bombs[i], bombs[j]):
                    bombs_neighbor[i].append(j)

        max_detonations = 0

        # Try detonating each bomb and find the max explosion chain
        for i in range(n):
            bombs_visited = defaultdict(bool)  # Reset visited for each DFS run
            max_detonations = max(max_detonations, self.dfs(i, bombs_neighbor, bombs_visited))

        return max_detonations


bombss = [[1,1,5],[10,10,5]]

sol = Solution()
print(sol.maximumDetonation(bombss))    