# Linear Regression

![linear_reg_example.png](resouces/linear_reg_example.png)

- One of the most practical techniques in data analysis is fitting a line through observed data points to show a
  relationship between two or more variables.
- A _regression_ attempts to fit a function to observed data to make predictions on new data.
- A _linear regression_ fits a straight line to observed data, attempting to demonstrate a linear relationship between
  variables and make predictions on new data yet to be observed.

## A Basic Linear Regression

### Residuals and Squared Errors

- How do statistics tools like `scikit-learn` come up with a line that fits to these points? It comes down to two
  questions that are fundamental to machine learning training:
    - _What defines a "best fit"?_
    - _How do we get to that "best fit"?_
- The first question has a pretty established answer: we minimize the squares, or more specifically the sum of the
  squared residuals.
- We want to minimize these residuals in total so there is the least gap possible between the line and points. But how
  do we measure the "total"? The best approach is to take the sum of squares, which simply squares each residual, or
  multiplies each residual by itself, and sums them. We take each actual y-value and subtract from it the predicted
  y-value taken from the line, then square and sum all those differences.

### Finding the Best Fit Line

#### Closed Form Equation

#### Inverse Matrix Techniques

#### Gradient Descent

## Overfitting and Variance

## Stochastic Gradient Descent

## The Correlation Coefficient

## Statistical Significance

## Coefficient of Determination

## Standard Error of the Estimate

## Prediction Intervals

## Train/Test Splits

## Multiple Linear Regreesion

===================================== <br />
**_Ref: [Code Demo](chapter5.py)_**