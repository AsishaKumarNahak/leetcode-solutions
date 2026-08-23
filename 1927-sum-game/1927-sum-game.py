class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        diff = 0
        q_diff = 0

        for i, ch in enumerate(num):
            if ch == '?':
                if i < half:
                    q_diff += 1
                else:
                    q_diff -= 1
            else:
                if i < half:
                    diff += int(ch)
                else:
                    diff -= int(ch)

        return diff * 2 != -q_diff * 9