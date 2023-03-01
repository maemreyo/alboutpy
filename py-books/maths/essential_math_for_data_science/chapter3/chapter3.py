from collections import defaultdict
from math import sqrt

import sympy

# Mean & weighted mean
sample = [1, 3, 2, 5, 6, 7]
weights = [.2, .2, .1, .1, .1, .3]
mean = sum(sample) / len(sample)
weighted_mean = sum(s * w for s, w in zip(sample, weights)) / sum(weights)

# =================================================================
# Median
sample = [0, 1, 5, 6, 9, 10, 14]


def median(values):
    ordered = sorted(values)

    n = len(ordered)
    mid = int(n / 2) - 1 if n % 2 == 0 else int(n / 2)

    if n % 2 == 0:
        return (ordered[mid] + ordered[mid + 1]) / 2.0
    else:
        return ordered[mid]


# =================================================================
# Mode
sample = [1, 3, 2, 5, 9, 5, 2, 4, 4, 10, 0, 5]


def mode(values):
    counts = defaultdict(lambda: 0)

    for s in values:
        counts[s] += 1

    max_count = max(counts.values())
    modes = [v for v in set(values) if counts[v] == max_count]
    return modes


# =================================================================
# Variance and standard deviation
sample = [0, 1, 5, 7, 9, 10, 14]


def variance(values):
    mean = sum(values) / len(values)
    return sum((v - mean) ** 2 for v in values) / len(values)


def std_dev(values):
    return sqrt(variance(values))

# =================================================================
#
