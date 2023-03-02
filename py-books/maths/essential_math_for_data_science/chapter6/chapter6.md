# Logistic Regression and Classification

## Understanding Logistic Regression

We are not always interested in representing variables as continuous, where they can represent an infinite number of
real decimal values. There are situations where we would rather variables be discrete, or representative of whole
numbers, integers, or booleans (1/0, true/false). Logistic regression is trained on an output variable that is
discrete (a binary 1 or 0) or a categorical number (which is a whole number). It does output a continuous variable in
the form of probability, but that can be converted into a discrete value with a threshold.

### Performing a Logistic Regression

#### Logistic Function

The logistic function is an S-shaped curve (also known as a sigmoid curve) that, for a given set of input variables,
produces an output variable between 0 and 1. Because the output variable is between 0 and 1 it can be used to represent
a probability.
![logistic_function.png](resouces/logistic_function.png)
where

- `e`: Euler's number
- `x`: the independent/input variable
- `β0` and `β1`: the coefficients we need to solve for

#### Fitting the Logistic Curve

- How do you fit the logistic curve to a given training dataset? First, the data can have any mix of decimal, integer,
  and binary variables, but the output variable must be binary (0 or 1). When we actually do prediction, the output
  variable will be between 0 and 1, resembling a probability.
- We use `maximum likelihood estimation`, as the name suggests, maximizes the likelihood a given logistic curve would
  output the observed data.

## Multivariable Logistic Regression

## Understanding the Log-Odds

## R-squared

## P-values

## Train/Test Splits

A three-fold cross-validation

## Confusion Matrices

A confusion matrix is a grid that breaks out the predictions against the actual outcomes showing the true positives,
true negatives, false positives (type I error), and false negatives (type II error).

## Bayes' Theorem and Classification

## Receiver Operator Characteristic/Area Under Curve

## Class Imbalance