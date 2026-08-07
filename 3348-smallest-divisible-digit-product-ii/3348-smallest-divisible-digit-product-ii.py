class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Factor t into 2^A * 3^B * 5^C * 7^D * r
        A = B = C = D = 0
        tt = t
        while tt % 2 == 0:
            tt //= 2; A += 1
        while tt % 3 == 0:
            tt //= 3; B += 1
        while tt % 5 == 0:
            tt //= 5; C += 1
        while tt % 7 == 0:
            tt //= 7; D += 1
        if tt != 1:
            return "-1"

        vec = {
            1: (0,0,0,0), 2: (1,0,0,0), 3: (0,1,0,0),
            4: (2,0,0,0), 5: (0,0,1,0), 6: (1,1,0,0),
            7: (0,0,0,1), 8: (3,0,0,0), 9: (0,2,0,0),
        }

        dimB, dimC, dimD = B+1, C+1, D+1
        strideA = dimB*dimC*dimD
        strideB = dimC*dimD
        strideC = dimD
        strideD = 1
        size = (A+1)*strideA
        INF = float('inf')
        dp = [0]*size
        digit_list = [vec[d] for d in range(2, 10)]

        for a in range(A+1):
            baseA = a*strideA
            for b in range(dimB):
                baseAB = baseA + b*strideB
                for c in range(dimC):
                    baseABC = baseAB + c*strideC
                    for d in range(dimD):
                        idx = baseABC + d
                        if a == 0 and b == 0 and c == 0 and d == 0:
                            dp[idx] = 0
                            continue
                        best = INF
                        for (e2, e3, e5, e7) in digit_list:
                            na = a-e2 if a-e2 > 0 else 0
                            nb = b-e3 if b-e3 > 0 else 0
                            nc = c-e5 if c-e5 > 0 else 0
                            nd = d-e7 if d-e7 > 0 else 0
                            if na == a and nb == b and nc == c and nd == d:
                                continue
                            val = dp[na*strideA+nb*strideB+nc*strideC+nd] + 1
                            if val < best:
                                best = val
                        dp[idx] = best

        def dp_val(a, b, c, d):
            return dp[a*strideA+b*strideB+c*strideC+d]

        n = len(num)
        fz = num.find('0')
        if fz == -1:
            fz = n

        prefix_exp = [(0,0,0,0)]*(fz+1)
        cur = (0,0,0,0)
        for idx in range(fz):
            e = vec[int(num[idx])]
            cur = (cur[0]+e[0], cur[1]+e[1], cur[2]+e[2], cur[3]+e[3])
            prefix_exp[idx+1] = cur

        if fz == n:
            total = prefix_exp[n]
            ra, rb, rc, rd = A-total[0], B-total[1], C-total[2], D-total[3]
            if ra <= 0 and rb <= 0 and rc <= 0 and rd <= 0:
                return num

        def build_suffix(ra, rb, rc, rd, L):
            res = []
            a, b, c, d = ra, rb, rc, rd
            for pos in range(L):
                rem_after = L-pos-1
                for cand in range(1, 10):
                    e2, e3, e5, e7 = vec[cand]
                    na = a-e2 if a-e2 > 0 else 0
                    nb = b-e3 if b-e3 > 0 else 0
                    nc = c-e5 if c-e5 > 0 else 0
                    nd = d-e7 if d-e7 > 0 else 0
                    if dp_val(na, nb, nc, nd) <= rem_after:
                        res.append(str(cand))
                        a, b, c, d = na, nb, nc, nd
                        break
            return ''.join(res)

        maxI = min(fz, n-1)
        for i in range(maxI, -1, -1):
            pe = prefix_exp[i]
            numi = int(num[i])
            for cand in range(numi+1, 10):
                e2, e3, e5, e7 = vec[cand]
                ta, tb, tc, td = pe[0]+e2, pe[1]+e3, pe[2]+e5, pe[3]+e7
                ra = A-ta if A-ta > 0 else 0
                rb = B-tb if B-tb > 0 else 0
                rc = C-tc if C-tc > 0 else 0
                rd = D-td if D-td > 0 else 0
                remlen = n-1-i
                if dp_val(ra, rb, rc, rd) <= remlen:
                    suffix = build_suffix(ra, rb, rc, rd, remlen)
                    return num[:i] + str(cand) + suffix

        needed_min = dp_val(A, B, C, D)
        m = max(n+1, needed_min)
        return build_suffix(A, B, C, D, m)