class Solution(object):
    def twoSum(self, numbers, target):
        s=set(numbers)
        for i in s:
            j=target-i
            if j in s:
                if j != i:
                    a,b=max(i,j),min(i,j)
                    return[numbers.index(i)+1,numbers.index(j)+1]
                else:
                    if numbers.count(i)>1:
                        a=numbers.index(i)+1
                        numbers.remove(i)
                        b=numbers.index(j)+2
                        return[a,b]
