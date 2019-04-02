class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()

    def toLowerCase_1(self, s):
        for i in range(len(s)):
            if 'A' <= s[i] <= 'Z':
                s = s[:i] + chr(ord(s[i])+32) + s[i+1:]
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.toLowerCase_1('AbdCDSDNFOdsdfewfdc'))
