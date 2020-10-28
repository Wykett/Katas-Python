class MultipleSum:

    multiples_to_search = []
    range_start = 1
    range_end = 10

    def __init__(self, multiples_to_search, range_start, range_end):
        self.multiples_to_search = multiples_to_search
        self.range_start = range_start
        self.range_end = range_end


    def multiple_sum(self):
        result = 0
        for i in range(self.range_start, self.range_end):
            for num in self.multiples_to_search:
                if i % num == 0:
                    result += i
                    break
        return result