from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l, -h, 0))
            events.append((r, h, 1))
        events.sort()

        ans = []
        active_heights = SortedList([0])
        n = len(events)
        i = 0
        # iterate through events
        while i < n:
            x, h, t = events[i]
            if t == 0:
                active_heights.add(-h)
            else:
                active_heights.remove(h)
            # check if thee biggest height has changed
            if not ans or ans[-1][1] != active_heights[-1]:
                ans.append((x, active_heights[-1]))
            i += 1
        
        return ans
