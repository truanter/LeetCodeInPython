class Solution:
    def findRestaurant(self, list1, list2):
        common = set(list1) & set(list2)
        minIndex = len(list1)+len(list2)
        res = []
        for i in common:
            a = list1.index(i)+list2.index(i)
            if a<minIndex:
                res = [i]
                minIndex = a
            elif a== minIndex:
                res.append(i)
        return res
                
        

if __name__=='__main__':
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Shogun","Burger King"]
    s = Solution()
    print(s.findRestaurant(list1, list2))

