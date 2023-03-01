from collections import defaultdict
from math import sqrt
from scipy.stats import norm
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
# Z-score

def z_score(x, mean, std):
    return (x - mean) / std


def z_to_x(z, mean, std):
    return (z * std) + mean


# =================================================================
# Confidence interval
def critical_z_value(p):
    norm_dist = norm(loc=0.0, scale=1.0)
    left_tail_area = (1.0 - p) / 2.0
    upper_area = 1.0 - ((1.0 - p) / 2.0)
    return norm_dist.ppf(left_tail_area), norm_dist.ppf(upper_area)


def confidence_interval(p, sample_mean, sample_std, n):
    # Sample size must be greater than 30

    lower, upper = critical_z_value(p)
    lower_ci = lower * (sample_std / sqrt(n))
    upper_ci = upper * (sample_std / sqrt(n))

    return sample_mean + lower_ci, sample_mean + upper_ci


print(confidence_interval(p=.95, sample_mean=64.408, sample_std=2.05, n=31))
