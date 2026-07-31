class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter

        freq = Counter(word)
        counts = sorted(freq.values(),reverse=True)

        pushes = 0
        for i,count in enumerate(counts):
            cost = (i // 8) + 1
            pushes += count *cost
            
        return pushes