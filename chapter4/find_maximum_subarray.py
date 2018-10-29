"""
create by zzxun
data:2018/10/08
info:最大子数组问题,分治法
----------------
input:一个包含正负数的无序数组
output:输入的求和最大一个子数组
"""

# 查找跨过mid中间线的最大子数组
import random


def find_max_crossing_subarray(lis, low, mid, high):
    left_sum = -float('inf')
    left_max = mid
    a_sum = 0
    for i in reversed(range(0, mid)):
        a_sum += lis[i]
        if a_sum > left_sum:
            left_sum = a_sum
            left_max = i
    right_sum = -float('inf')
    right_max = mid
    a_sum = 0
    for i in range(mid + 1, high):
        a_sum += lis[i]
        if a_sum > right_sum:
            right_sum = a_sum
            right_max = i
    return [left_max, right_max, left_sum + right_sum]


def find_maximum_subarray(lis, low, high):
    if high == low:
        return [low, high, lis[low]]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(lis, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(lis, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(lis, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return [left_low, left_high, left_sum]
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return [right_low, right_high, right_sum]
    else:
        return [cross_low, cross_high, cross_sum]


if __name__ == '__main__':
    arraylis = [random.randint(-100, 100) for _ in range(1000)]
    result = find_maximum_subarray(arraylis, 0, 999)
    print(result)
