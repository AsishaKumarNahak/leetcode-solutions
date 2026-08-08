from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        # suf[i] = length of the longest suffix of word2 that can be matched
        # as an exact subsequence using word1[i:]
        suf = [0] * (n + 1)
        j = m
        for i in range(n - 1, -1, -1):
            if j > 0 and word1[i] == word2[j - 1]:
                j -= 1
            suf[i] = m - j

        res = []
        changed = False
        j = 0
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            elif not changed and suf[i + 1] >= m - j - 1:
                res.append(i)
                changed = True
                j += 1

        if j < m:
            return []
        return res