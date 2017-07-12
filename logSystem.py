class LogSystem:

    def __init__(self):
        self.log ={}

    def put(self, id, timestamp):
        self.log[timestamp]=id
        

    def retrieve(self, s, e, gra):
        d = {'Year':0, 'Month':1, 'Day':2, 'Hour':3, 'Minute':4, 'Second':5}
        index = d[gra]+1
        s = s.split(':')[:index]
        e = e.split(':')[:index]
        res =[]
        import operator
        for i in self.log.keys():
            a = i.split(':')[:index]
            if operator.ge(a,s) and operator.ge(e,a):
                res.append(self.log[i])
        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
