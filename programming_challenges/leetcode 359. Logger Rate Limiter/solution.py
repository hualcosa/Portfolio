class Logger:

    def __init__(self):
        # dictionary to keep track of the last time that
        # message was printed
        self.mem = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.mem:
            self.mem[message] = timestamp # add the time that message was last seen
            return True
        elif (timestamp - self.mem[message]) < 10:
            return False
        else:
            self.mem[message] = timestamp # update the time that message was last seen
            return True
            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)