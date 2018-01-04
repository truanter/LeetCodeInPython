class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        char_count = 0
        res = ''
        for char in S[::-1]:
            if char != '-':
                res += char.upper()

                if char_count % K == K - 1:
                    res += '-'

                char_count += 1

        if not len(res):
            return res

        return res[::-1] if res[-1] != '-' else res[:-1][::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.licenseKeyFormatting("---", 3))
