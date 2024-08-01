from collections import deque
class Solution:
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])

        requiredHP = [[0] * n for _ in range(m)]
        requiredHP[m-1][n-1] = -dungeon[m-1][n-1]

        queue = deque((m-2, n-1))

if __name__ == "__main__":
    test_dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    print(Solution().calculateMinimumHP(test_dungeon))