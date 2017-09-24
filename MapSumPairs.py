class MapSum:

    def __init__(self):
        self.d = {}       

    def insert(self, key, val):
        self.d[key] = val
        
    def sum(self, prefix):
        s = 0
        for i in self.d:
            if prefix == i[:len(prefix)]:
                s += self.d[i]
        return s
