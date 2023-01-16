class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def hasLeapDay(year):
            return 1 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0
        # the order of the elements in this list depends on the weekday you are solving
        # the problem
        dayNames = ['Friday','Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday']
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # days since 31, 12, 1970
        def daysSinceStart(day, month, year):
            numDays = 0
            # we start from the last completed year
            for y in range(year - 1, 1970, -1):
                numDays += 365 + hasLeapDay(y)
            # sum the number of days in completed months
            numDays += sum(daysInMonth[:month-1])
            # sum the days in the current month
            numDays += day
            # if the month is bigger than february, we have to include the leap day for that year
            if month > 2:
                numDays += hasLeapDay(year)
            return numDays
        
        knownStart = daysSinceStart(23,12,2022)
        d = daysSinceStart(day, month, year)
        return dayNames[(d - knownStart) % 7]
        