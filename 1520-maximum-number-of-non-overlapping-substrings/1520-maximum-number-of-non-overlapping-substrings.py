from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        for i, ch in enumerate(s):
            if first[ch] != i:
                continue  # only start at a character's first occurrence

            start = i
            end = last[ch]
            j = i
            valid = True

            while j <= end:
                c = s[j]
                if first[c] < start:
                    valid = False
                    break
                if last[c] > end:
                    end = last[c]
                j += 1

            if valid:
                intervals.append((start, end))

        # Sort by end ascending, then by length ascending (for min total length)
        intervals.sort(key=lambda x: (x[1], x[1] - x[0]))

        result = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end

        return result