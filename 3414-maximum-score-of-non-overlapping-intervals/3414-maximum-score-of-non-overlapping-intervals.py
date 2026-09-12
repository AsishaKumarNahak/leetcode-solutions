import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])
        L = [intervals[i][0] for i in order]
        R = [intervals[i][1] for i in order]
        W = [intervals[i][2] for i in order]

        dp = [[(0, ())] * (n + 1) for _ in range(5)]

        for i in range(1, n + 1):
            cur = i - 1
            p = bisect.bisect_left(R, L[cur])
            for k in range(5):
                if k == 0:
                    dp[k][i] = dp[k][i - 1]
                    continue
                skip = dp[k][i - 1]
                prev_w, prev_idx = dp[k - 1][p]
                take = (prev_w + W[cur], tuple(sorted(prev_idx + (order[cur],))))
                dp[k][i] = take if (take[0] > skip[0] or (take[0] == skip[0] and take[1] < skip[1])) else skip

        return list(dp[4][n][1])