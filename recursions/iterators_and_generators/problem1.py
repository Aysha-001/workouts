#problem 1

class reverse_iter:
    def __init__(self, arr):
        self.i = -1
        self.arr = arr

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.i) < len(self.arr)+1:
            item = self.arr[self.i]
            self.i -=1
            return item
        else:
            raise StopIteration()
it = reverse_iter([1, 2, 3, 4])

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))