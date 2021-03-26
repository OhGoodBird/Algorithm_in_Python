#!/usr/bin/env python3


def dtw_distance(s1, s2, distance_func):
    '''
    DTW (Dynamic time warping)
    https://en.wikipedia.org/wiki/Dynamic_time_warping

    Args:
        s1: list, series 1.
                    e.g. [1, 2, 2, 3]
        s2: list, series 2.
                    e.g. [1, 1, 2, 2, 3]
        distance_func: function, used to calculate distance between s1 and s2.

    Returns:
        int, DTW distance.
    '''
    import math
    n = len(s1)
    m = len(s2)
    # n*m matrix
    dtw_table = [[math.inf for _ in range(m+1)] for _ in range(n+1)]
    dtw_table[0][0] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = distance_func(s1[i-1], s2[j-1])
            dtw_table[i][j] = cost + min(dtw_table[i-1][j],
                                         dtw_table[i][j-1],
                                         dtw_table[i-1][j-1])
    return dtw_table[n][m]


if __name__ == '__main__':

    test_set = [(['今', '天', '天', '氣'], ['今', '天', '氣']),
                (['今', '天', '天', '氣'], ['今', '天', '氣', '溫']),
                (['今', '天', '天', '氣', '如', '何'], ['明', '天', '氣', '溫']),
                (['什', '麼', '意', '思'], ['我', '不', '懂', '什', '麼', '是', '你', '的', '意', '思', '啦'])]

    def distance_func(x, y): return 0 if x == y else 1

    for x, y in test_set:
        print(x)
        print(y)
        print(f'dtw result = {dtw_distance(x, y, distance_func)}')
