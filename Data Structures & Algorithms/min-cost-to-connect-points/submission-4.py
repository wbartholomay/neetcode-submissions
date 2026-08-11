class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = defaultdict(list) 
        for i, point_i in enumerate(points):
            for j, point_j in enumerate(points):
                if i == j:
                    continue
                distance = abs(point_i[0] - point_j[0]) + abs(point_i[1] - point_j[1])
                edges[i].append((distance, j))

        visited = set()
        heap = [(0, 0)]
        result = 0

        while len(visited) < len(points):
            dist, src = heapq.heappop(heap)
            if src in visited:
                continue
            visited.add(src)
            result += dist

            for distance, dest in edges[src]:
                if dest in visited:
                    continue
                heapq.heappush(heap, (distance, dest))
        
        return result