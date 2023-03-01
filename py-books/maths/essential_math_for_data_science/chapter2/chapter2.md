# Probability

- Probability is the theoretical study of measuring certainly that an event will happen.
- _Likelihood_ is similar to probability, and it is easy to confuse the two. You can get away with using "probability"
  and "likelihood" interchangeably in everyday conversation.
- However, we should pin down these differences:
    - _Probability_ is about quantifying predictions of events yet to happen.
    - _Likelihood_ is measuring the frequency of events that already happened.
- Sometimes people use the terms _probability_ and _statistics_ interchangeably and while it is understandable to
  conflate the two disciplines, they do have distinctions.
    - _Probability_ is purely theoretical of how likely an event is to happen and does not require data.
    - _Statistics_ cannot exist without data and uses it to discover probability and provides tools to describe data.

## Probability Math

When we work with a single probability of an event `P(X)`, known as a _marginal probability_, the idea is fairly
straightforward. But when we start combining probabilities of different events, it gets a little less intuitive.

### Joint Probabilities

- The probability that both events will occur together, this is known as a _joint probability_.

> P(A AND B) = P(A) x P(B)

### Union Probabilities

- When we deal with _OR_ operations with probabilities, this is known as a _union probability_.
- When you have a union probability between two or more events that are not mutually exclusive, be sure to subtract the
  joint probability so no probabilities are doubled-counted.

> P(A OR B) = P(A) + P(B) - P(A) x P(B)

### Conditional Probability and Bayes' Theorem

- A probability topic that easily confuses people is the concept of _**conditional probability**_, which is the
  probability of an event A occurring given event B has occurred. It is typically expressed as

> P(A GIVEN B) or P(A|B)
> P(A|B) = ( P(B|A) * P(A) ) / P(B)

### Joint and Union Conditional Probabilities

- If event A has no impact on event B, then what does that mean for conditional probability `P(B|A)`? That
  means `P(B|A) = P(B)`, meaning event A occurring makes no difference to how likely event B is to occur:

> P(A AND B) = P(B) x P(A|B)

- If we want to calculate the probability of A or B occurring, but A may affect the probability of B:

> P(A OR B) = P(A) + P(B) - P(A|B) x P(B)

## Binomial Distribution

One tool that might be relevant here is the _binomial distribution_, which measures how likely `k` successes can happen
out of `n` trials given `p` probability.

## Beta Distribution

The _beta distribution_ allows us to see the likelihood of different underlying probabilities for an event to occur give
_alpha_ successes and _beta_ failures.

===================================== <br />
**_Ref: [Code Demo](chapter2.py)_**