class PersStack:
    def __init__(self):
        self.val = [None]
        self.prev = [None]
        self.index = 0

    def push(self, version: int, value):
        # if version more than last + 1
        if version + 1 > len(self.prev):
            self.prev.append(self.index)
        else:
            self.prev.append(version)
        self.val.append(value)

        self.index += 1

    def pop(self, version: int):
        if version > self.index:
            prev_index = self.prev[-1]
        else:
            prev_index = self.prev[version]

        self.val.append(self.val[prev_index])
        self.prev.append(self.prev[prev_index])

        return self.val[-1]

    def size(self):
        return len(self.prev)

    def __str__(self):
        for i in range(0, len(self.val)):
            print(f"value {self.val[i]} prev {self.prev[i]}")



pers_stack = PersStack()

pers_stack.push(1, 3)
pers_stack.push(2, 5)
pers_stack.pop(2)
pers_stack.push(3, 6)
print(pers_stack.__str__())