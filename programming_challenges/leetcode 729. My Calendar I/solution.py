class MyCalendar:

    def __init__(self):
        self.events = [] # list to store events

    def book(self, start: int, end: int) -> bool:
        for s, e in self.events:
            if s < end and e > start:
                return False
        self.events.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


# two events are allowed when: e1 <= start OR end <= s1
# two events conflict when: e1 > start and end > s1