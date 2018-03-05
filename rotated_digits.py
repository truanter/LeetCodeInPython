class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        rotated_dict = {'0': '0', '1': '1', '2': '5',  '5': '2', '6': '9', '8': '8', '9': '6'}
        res = 0

        for num in range(N+1):
            strlized_num = str(num)
            temp_rotated_num = ''
            for char in strlized_num:
                if rotated_dict.get(char):
                    temp_rotated_num += rotated_dict.get(char)
                else:
                    break

            if len(strlized_num) == len(temp_rotated_num) and strlized_num != temp_rotated_num:
                res += 1

        return res
