class Solution:
    def longest_word(self, words):
        if len(words) == 1:
            return words[0]
        # words.sort(key = lambda x: len(x))
        len_of_max_word = len(max(words, key = lambda x: len(x)))
        # print(len_of_max_word)
        ladder_list = [[] for i in range(len_of_max_word)]

        for i in words:
            ladder_list[len(i) - 1].append(i)

        cur_res = ladder_list[0]

        for words_list in ladder_list[1:]:
            temp_list = []
            for word in words_list:
                if word[:-1] in cur_res:
                    temp_list.append(word)

            # print(temp_list)
            if len(temp_list) == 0:
                break

            cur_res = temp_list

        return min(cur_res)


if __name__ == '__main__':
    s = Solution()
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(s.longest_word(words))
