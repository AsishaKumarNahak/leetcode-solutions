class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1
        odd_chars = [c for c in range(26) if count[c] % 2 == 1]
        if n % 2 == 0 and len(odd_chars) != 0:
            return ""
        if n % 2 == 1 and len(odd_chars) != 1:
            return ""
        mid = odd_chars[0] if n % 2 == 1 else -1
        half_count = [count[c] // 2 for c in range(26)]
        m = n // 2
        work = half_count[:]
        L = 0
        for j in range(m):
            idx = ord(target[j]) - 97
            if work[idx] > 0:
                work[idx] -= 1
                L += 1
            else:
                break
        prefix_count = [[0] * 26]
        running = [0] * 26
        for j in range(m):
            running = running[:]
            running[ord(target[j]) - 97] += 1
            prefix_count.append(running)
        if L == m:
            h = list(target[:m])
            full_list = h + ([chr(mid + 97)] if mid != -1 else []) + h[::-1]
            full = ''.join(full_list)
            if full > target:
                return full
        for idx in range(min(L, m - 1), -1, -1):
            freq = half_count[:]
            pc = prefix_count[idx]
            for c in range(26):
                freq[c] -= pc[c]
            t_idx = ord(target[idx]) - 97
            chosen = -1
            for c in range(t_idx + 1, 26):
                if freq[c] > 0:
                    chosen = c
                    break
            if chosen != -1:
                freq[chosen] -= 1
                h = list(target[:idx])
                h.append(chr(chosen + 97))
                for c in range(26):
                    h.extend([chr(c + 97)] * freq[c])
                full_list = h + ([chr(mid + 97)] if mid != -1 else []) + h[::-1]
                return ''.join(full_list)
        return ""