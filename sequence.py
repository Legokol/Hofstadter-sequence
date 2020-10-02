class sequence:
    def __init__(self):
        self.a = [1, 1]
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a[self.cur]
        self.cur += 1
        if self.cur > 1:
            self.a.append(self.a[self.cur - self.a[self.cur - 1]] + self.a[self.cur - self.a[self.cur - 2]])
        return result
