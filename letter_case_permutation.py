class Solution:
    def letterCasePermutation(self, S):
        """
        :type S： str
        :rtype: List[str]
        """
        if not S:
            return ['']
        res = []

        for letter_index in range(len(S)):
            temp_list = res.copy()
            if ord(S[letter_index]) in range(97, 123) or ord(S[letter_index]) in range(65, 91):
                if not temp_list:
                    res.extend([S[letter_index].upper(), S[letter_index].lower()])
                else:
                    for temp_index in range(len(res)):
                        res[temp_index] += S[letter_index].upper()
                        temp_list[temp_index] += S[letter_index].lower()
                    res.extend(temp_list)
            else:
                if letter_index:
                    for i in range(len(res)):
                        res[i] += S[letter_index]
                else:
                    res.append(S[letter_index])

        return res

