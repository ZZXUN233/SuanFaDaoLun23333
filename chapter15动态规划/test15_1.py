"""
钢条切割问题
"""

len_weight = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}  # 刚才长度切割后对应的价格

# 需要算法求出对应子长度的真实最大收益
p1 = {1: 1, 2: 5, 3: 8, 4: 10, 5: 13, 6: 17, 7: 18, 8: 22, 9: 25, 10: 30}  # 记录真实的最大收益


# 朴素递归
def cut_rod(p, n):
    if n == 0:
        return 0
    q = 0
    for i in range(1, n + 1):
        if i in p:
            q = max(q, p[i] + cut_rod(p, n - i))
    return q


def cut_rod_plus(p, n):
    remb = [0 for _ in range(n + 1)]

    def cut_rod(p, n):
        if remb[n] > 0: return remb[n]
        if n == 0:
            return 0
        q = 0
        for i in range(1, n + 1):
            if i in p:
                q = max(q, p[i] + cut_rod(p, n - i))
        remb[i] = q
        return q

    return cut_rod(p, n)


# 自底向上的问题求解
def bottom_cut_rod(p, n):
    remb = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        q = 0
        for j in range(1, i + 1):
            q = max(q, p.setdefault(j, 0) + remb[i - j])
        remb[i] = q
    return remb[n]


# 给出切割策列的算法
def extended_bottom_up_cut_rod(p, n):
    lens = [0 for _ in range(n)]
    remb = lens.copy()


if __name__ == '__main__':
    for i in range(30):
        tmp = cut_rod_plus(len_weight, i)
        # print("%d--->%d" % (i, tmp))
    for i in range(300):
        print("%d--->%d" % (i, bottom_cut_rod(len_weight, i)))
