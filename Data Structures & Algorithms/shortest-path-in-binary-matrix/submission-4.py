class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        size = len(grid)
        queue = deque()
        visit = set()

        if grid[0][0] == 1 or grid[size - 1][size - 1] == 1:
            return -1

        if size == 1:
            return 1


        queue.append((0,0))
        visit.add((0,0))

        length = 1
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == size -1 and c == size -1:
                    if grid[r][c] == 1:
                        return -1
                    else:
                        return length

                neighbors = [[1,-1], [1,0], [1,1], [0,-1], [0,1], [-1,-1], [-1,0], [-1,1]]
                for dr, dc in neighbors:
                    if (r + dr < 0 or c + dc < 0 or
                        r + dr >= size or c + dc >= size or
                        (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
        return -1


