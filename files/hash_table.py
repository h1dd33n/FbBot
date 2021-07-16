class Table:
    def __init__(self, max):
        self.MAX = max
        self.arr = [[] for i in range(self.MAX)]
        self.start = 0
        self.end = self.MAX

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            # print(kv)
            if kv[0] == key:
                # print(kv)
                return kv

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            # print(self.arr[h])
            # print(f'{idx} + {element}')
            if len(element) == 2 and element[0] == key:
                # self.arr[h][idx] = (key, val)
                self.arr[h].append({key: val})
                found = True
                break
        if not found:
            self.arr[h].append({key: val})

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.arr[self.start]
        self.start +=1
        return current



