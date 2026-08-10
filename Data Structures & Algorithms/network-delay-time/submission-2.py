class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge_map = defaultdict(list)
        for u, v, w in times:
            edge_map[u].append((v, w))

        print(edge_map)
        min_heap = [(0, k)]
        distances = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in distances:
                continue
            
            distances[node] = time

            for v, w in edge_map[node]:
                heapq.heappush(min_heap, (time + w, v))
        
        if len(distances) != n:
            return -1
        return max(distances.values())
