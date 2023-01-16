class Solution:
    def rotatedDigits(self, n: int) -> int:
        numbers_dict = {0:0,
                        1:1,
                        8:8,
                        2:5,
                        5:2,
                        6:9,
                        9:6} # the rest becomes invalid
        # variable to store the answer
        good_numbers = 0
        for i in range(1, n+1):
            num_str = str(i)
            # if the lenght is 1 the result is straightforward
            if len(num_str) == 1:
                if numbers_dict.get(i, -1) != -1 and num_str not in ['0','1','8']:
                    good_numbers += 1
            else:
                # list to store the reversed algarisms
                reversed_number = []
                for dig in num_str:
                    reversed_number.append(str(numbers_dict.get(int(dig), -1)))
                # if -1 is not in the list, it means we were able to revert all
                # algarisms of the number
                if '-1' not in reversed_number:
                    reversed_number = ''.join(reversed_number)
                    if reversed_number != num_str:
                        good_numbers += 1
        return good_numbers
            
        