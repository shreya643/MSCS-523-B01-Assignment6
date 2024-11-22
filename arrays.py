class Array:
    def __init__(self):
        self.array = []

    def insert(self, value):
        self.array.append(value)

    def delete(self, index):
        if 0 <= index < len(self.array):
            return self.array.pop(index)
        else:
            raise IndexError("Index out of range")

    def access(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise IndexError("Index out of range")
