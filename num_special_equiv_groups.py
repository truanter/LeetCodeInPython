class Solution:
    def numSpecialEquivGroups(self, A):
        if len(A[0]) == 1:
            return len(set(A))
        odd_even_list = []
        for string in A:
            char_list = list(string)
            odd = char_list[:len(string):2]
            even = char_list[1:len(string):2]

            odd_dict = {c: odd.count(c) for c in odd}
            even_dict = {c: even.count(c) for c in even}

            if not [odd_dict, even_dict] in odd_even_list:
                odd_even_list.append([odd_dict, even_dict])

        return len(odd_even_list)


if __name__ == '__main__':
    l = ['aa', 'bb', 'ab', 'ba']
    s = Solution()
    print(s.numSpecialEquivGroups(l))
