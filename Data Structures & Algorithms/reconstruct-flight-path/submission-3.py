class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)
        for u, v in tickets:
            edges[u].append(v)
        for u in edges:
            edges[u].sort(reverse=True)

        res = []
        def dfs(src):
            while edges[src]:
                dfs(edges[src].pop())
            
            res.append(src)
        dfs("JFK")
        print(res)
        res.reverse()
        return res