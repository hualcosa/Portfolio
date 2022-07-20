class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        # dealing with extreme case
        if not intervals:
            return 0
        
        free_rooms = []
        
        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])
        
        # add the first meeting ending time
        heapq.heappush(free_rooms, intervals[0][1])
        
        for i in intervals[1:]:
            
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            
            # regardless of a new room being allocated or not, we need to add the new metting
            # ending time to the heap
            heapq.heappush(free_rooms, i[1])
        
        # the size of the heap at the end of the process will give us the minimum number of rooms necessary
        return len(free_rooms)
        