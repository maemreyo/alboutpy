# Descriptive and Inferential Statistics

## Overview

- Statistics is the practice of collecting and analyzing data to discover findings that are useful or predict what
  causes those findings to happen.
- Probability often plays a large role in statistics, as we use data to estimate how likely an event is to happen.

### What is Data?

Data is just like photographs; it provides snapshots of a story.

### Descriptive versus Inferential Statistics

- What comes to mind when you hear the word "statistics"? It is calculating mean, median, mode, charts, bell, curves,
  and other tools to describe data? This is the most commonly understood part of statistics called _descriptive
  statistics_, and we use it to summarize data. After all, is it more meaningful to scroll through a million records of
  data or have it summarized?
- _Inferential statistics_ tries to uncover attributes about a larger population, often based on a sample. It is often
  misunderstood and less intuitive than descriptive statistics. Often we are interested in studying a group that is too
  large to observe and we have to resort to using only a few members of that group to infer conclusions about them.

### Populations, Samples, and Bias

- A population is a particular group of interest we want to study.
- A sample is a subset of the population that is ideally random and unbiased, which we use to infer attributes about the
  population. We often have to study samples because polling the entire population is not always possible.

### Descriptive Statistics

Descriptive statistics is the area most people are familiar with. We will touch on the basics like mean, median, and
mode followed by variance, standard deviation, and the normal distribution.

#### Mean and Weighted Mean

- The _mean_ is the average of a set of values. The operation is simple to do: sum the values and divide by the number
  of
  values. The mean is useful because it shows where the "center of gravity" exists for an observed set of values.
  ![mean.png](resouces/mean.png)
- The _mean_ is actually a weighted average called the _weighted mean_. The mean we commonly use gives equal importance
  to each value. But we can manipulate the mean and give each item a different weight.
  ![weighted_mean.png](resouces/weighted_mean.png)

#### Median

- The _median_ is the middlemost value in a set of values.
- The _median_ can be helpful alternative to the _mean_ when data is skewed by outliers, or values that are extremely
  large and small compared to the rest of the values.

#### Mode

- The _mode_ is the most frequently occurring set of values. It primarily becomes useful when your data is repetitive,
  and you want to find which values occur the most frequently.

#### Variance and Standard Deviation

When we start talking about variance and standard deviation, this is where it gets interesting. One thing that
confuses people with variance and standard deviation is there are some calculations differences for the sample versus
the population.

- Population Variance and Standard Deviation

    - Variance
      ![population_variance.png](resouces/population_variance.png)
    - Standard Deviation
      ![population_standard_deviation.png](resouces/population_standard_deviation.png)

- Sample Variance and Standard Deviation

    - Variance
      ![sample_variance.png](resouces/sample_variance.png)
    - Standard Deviation
      ![sample_standard_deviation.png](resouces/sample_standard_deviation.png)

#### The Normal Distribution

- The _normal distribution_ also known as the _Gaussian distribution_, is a symmetrical bell-shaped distribution that
  has most mass around the mean, and its spread is defined as a standard deviation. The "tails" on either side become
  thinner as you move away from the mean.
- Properties of a normal distribution
    - It's symmetrical; both sides are identically mirrored at the mean, which is the center.
    - Most mass is at the center around the mean.
    - It has a spread (being narrow or wide) that is specified by standard deviation.
    - The "tails" are the least likely outcomes and approach zero infinitely but never touch zero.
    - It resembles a lot of phenomena in nature and daily life, and even generalizes non-normal problems because of the
      central limit theorem.
- **The probability density function (PDF)**
    - The standard deviation plays an important role in the normal distribution, because it defines how "spread out" it
      is.
    - It is actually one of the parameters alongside the mean. The _PDF_ that creates the normal distribution is as
      follows:
      ![pdf.png](resouces/pdf.png)
- **The cumulative distribution function (CDF)**

#### The Inverse CDF

#### Z-scores

- It is common to rescale a normal distribution so that the mean is 0 and the standard deviation is 1, which is known as
  the standard normal distribution. This makes it easy to compare the spread of one normal distribution to another
  normal distribution, even if they have different means and variances.

- Of particular importance with the standard normal distribution is it expresses all x-values in terms of standard
  deviations, known as Z-scores. Turning an x-value into a Z-score uses a basic scaling formula:

> z = (x - μ) / σ
> where μ is the mean, σ is the standard deviation

## Inferential Statistics

### The Central Limit Theorem

The _central limit theorem_, which states that interesting things happen when we take large enough samples of a
population, calculate the mean of each, and plot them as a distribution:

1. The mean of the sample means is equal to the population mean.
2. If the population is normal, then the sample means will be normal.
3. If the population is not normal, then the sample size is greater than 30, the sample means will still roughly
   form a
   normal distribution.
4. The standard deviation of the sample means equals the population standard deviation divided by the square root
   of `n`:

> sample standard deviation = population standard deviation / sqrt(sample size)

### Confidence Intervals

- A _confidence interval_ is a range calculation showing how confidently we believe a sample mean (or other parameter)
  falls in a range for the population means.
- Our margin of error formula, the larger `n` becomes, the narrower our confidence interval becomes. This makes sense
  because if we have a larger sample, we are more confidence in the population mean falling in a smaller range, hence
  why it's called a confidence interval.

### Understanding P-values

- The probability is what we call the _p-value_, the probability of something occurring by chance rather than because of
  a hypothesized explanation.

### Hypothesis Testing

#### One-Tailed Test

When we approach the _one-tailed test_, we typically frame our null and alternative hypotheses using inequalities. We
hypothesize around the population mean and say that it either is greater than/equal to the null hypothesis `H0` or less
than the alternative hypothesis `H1`.

#### Two-Tailed Test

To do a _two-tailed test_, we frame our null and alternative hypothesis in an "equal" or "not equal" structure.

## The T-Distribution: Dealing with Small Samples

Whether we are calculating confidence intervals or doing hypothesis testing, if we have 30 or fewer items in a sample we
would opt to use a T-distribution instead of a normal distribution. The T-distribution is like a normal distribution but
has fatter tails to reflect more variance and uncertainty.

## Big Data Considerations and the `Texas Sharpshooter Fallacy`

===================================== <br />
**_Ref: [Code Demo](chapter3.py)_**