from typing import List
from sortedcontainers import SortedList


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        s = list(s)
        n = len(s)

        starts = SortedList()
        lengths = SortedList()
        start_char = {}
        start_len = {}

        def add_run(start, length, char):
            starts.add(start)
            start_char[start] = char
            start_len[start] = length
            lengths.add(length)

        def remove_run(start):
            starts.remove(start)
            length = start_len.pop(start)
            lengths.remove(length)
            del start_char[start]

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            add_run(i, j - i, s[i])
            i = j

        result = []
        for idx_q in range(len(queryIndices)):
            i = queryIndices[idx_q]
            c = queryCharacters[idx_q]

            if s[i] == c:
                result.append(lengths[-1])
                continue

            s[i] = c

            ridx = starts.bisect_right(i) - 1
            run_start = starts[ridx]
            run_len = start_len[run_start]
            run_char = start_char[run_start]
            run_end = run_start + run_len - 1

            remove_run(run_start)

            left_len = i - run_start
            right_len = run_end - i

            if left_len > 0:
                add_run(run_start, left_len, run_char)
            if right_len > 0:
                add_run(i + 1, right_len, run_char)

            new_start, new_len = i, 1

            lidx = starts.bisect_left(i) - 1
            if lidx >= 0:
                ls = starts[lidx]
                if ls + start_len[ls] == i and start_char[ls] == c:
                    ll = start_len[ls]
                    remove_run(ls)
                    new_start, new_len = ls, new_len + ll

            if (i + 1) in start_char and start_char[i + 1] == c:
                rl = start_len[i + 1]
                remove_run(i + 1)
                new_len += rl

            add_run(new_start, new_len, c)
            result.append(lengths[-1])

        return result