class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = defaultdict(list) 
        for i, point_i in enumerate(points):
            for j, point_j in enumerate(points):
                if i == j:
                    continue
                distance = abs(point_i[0] - point_j[0]) + abs(point_i[1] - point_j[1])
                edges[i].append((distance, j))

        distances = {}
        heap = [(0, 0)]

        while heap:
            dist, src = heapq.heappop(heap)
            if src in distances:
                continue
            distances[src] = dist

            for distance, dest in edges[src]:
                if dest in distances:
                    continue
                heapq.heappush(heap, (distance, dest))
        
        return sum(distances.values())