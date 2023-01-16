class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # tuple with the position people are in 
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            # if finds a person, sets it as the next previous
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)
                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                # update the answer
                ans = max(ans, min(left, right))
        return ans