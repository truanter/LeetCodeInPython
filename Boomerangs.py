class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sum = 0
        for p in points:
            d={}
            for q in points:
                r = q[0] - p[0]
                c = q[1] - p[1]
                d[r*r + c*c] = 1 + d.get(r*r + c*c,0)
            for key in d:
                sum += d[key] * (d[key] - 1)
        return sum
