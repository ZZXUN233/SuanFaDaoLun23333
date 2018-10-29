"""
info:动态规划求解最长公共子串
input：stringA,stringB
output:stringC 为stringA与stringB的最大公共子串
"""
import numpy


def lcs(strA, strB):
    n = len(strA)
    m = len(strB)
    status = numpy.zeros((n + 1, m + 1), numpy.int8)
    rembs = [['' for _ in range(m)] for _ in range(n)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if strA[i - 1] == strB[j - 1]:
                status[i][j] = status[i - 1][j - 1] + 1
                rembs[i - 1][j - 1] = 'ul'
            else:
                status[i][j] = max(status[i - 1][j], status[i][j - 1])
                rembs[i - 1][j - 1] = 'u' if status[i - 1][j] >= status[i][j - 1] else 'l'
    return status, rembs


sts = ''


def print_lcs(rembs, strA, lenA, lenB):
    global sts
    if lenA == 0 or lenB == 0:
        return
    if rembs[lenA][lenB] == 'ul':
        print_lcs(rembs, strA, lenA - 1, lenB - 1)
        sts += strA[lenA]
        print(strA[lenA])
    elif rembs[lenA][lenB] == 'u':
        print_lcs(rembs, strA, lenA - 1, lenB)  # 元素上移
    else:
        print_lcs(rembs, strA, lenA, lenB - 1)  # 元素左移


if __name__ == '__main__':
    stA = "abcbdab"
    stB = "bdcaba"
    status, rembs = lcs(stA, stB)
    print(rembs)
    print_lcs(rembs, stA, len(stA) - 1, len(stB) - 1)
