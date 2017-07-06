class Point(object):
    def __init__(self, a, b):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        if not points:
            return 0
        if len(points)==1:
            return 1
        import itertools
        d={}
        for i in itertools.combinations(points,2):
           g=self.gradient(i[0],i[1])
           if i[0] in d:
               d[i[0]].append(g)
           else:
               d[i[0]]=[g]
           if i[1] in d:
                d[i[1]].append(g)
           else:
                d[i[1]]=[g]
        print(d.values())
        res=0
        for i in d.values():
           o = i.count('o')
           if not [i.count(j) for j in i if j!='o']:
               res = max(res,o)
           else:
               res = max(res,o+max([i.count(j) for j in i if j!='o']))
        return res+1
    def gradient(self, p, q):
        if p.y==q.y:
            if not p.x == q.x:
                return 'n'
            else:
                return'o'
        else:
            return (p.x-q.x)/(p.y-q.y)
    def gcd(self, n, m):
        if not m:
            return n
        else:
            return self.gcd(m,n%m)

if __name__=='__main__':
    points=[]
    points.append(Point(-4,1))
    points.append(Point(-7,7))
    points.append(Point(-1,5))
    points.append(Point(9,-25))
    s=Solution()
    print(s.maxPoints(points))
