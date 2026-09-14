class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, [])
        max_timestamp = -1
        res = ""
        l = 0
        r = len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            mid_timestamp = values[mid][0]
            mid_val = values[mid][1]
            if mid_timestamp == timestamp:
                return mid_val
            elif mid_timestamp < timestamp:
                if mid_timestamp > max_timestamp:
                    max_timestamp = mid_timestamp
                    res = mid_val
                l = mid + 1
            else:
                r = mid - 1
        return res