class Solution:
    def powerfulInteger(self, intervals, k):
        from collections import defaultdict
        
        events = defaultdict(int)
        for start, end in intervals:
            events[start] += 1
            events[end + 1] -= 1

        current = 0
        max_powerful = -1
        active_start = None

        for point in sorted(events):
            current += events[point]
            if current >= k:
                if active_start is None:
                    active_start = point
            else:
                if active_start is not None:
                    max_powerful = max(max_powerful, point - 1)
                    active_start = None

        return max_powerful
