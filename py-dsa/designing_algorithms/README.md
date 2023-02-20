# Designing Algorithms

> Discuss the strengths and weaknesses of various techniques for designing algorithms.

## Introduction the basic concepts of design an algorithm

> "A finite set of unambiguous instructions that given some set of initial conditions can be performed in a prescribed
> sequence to achieve a certain goal and that has a recognized set of end conditions."

### Concern 1 - Will the designed algorithm produce the result we expect?

To verify an algorithm, we need to think about the following two aspects:

1. **_Defining the truth_**
    - To verify the algorithm, we need some known correct results for a given set of inputs. These known correct results
      are called the **truths**, in the context of the problem we are trying to solve.
    - The **truth** is important as it is used as a reference when we iteratively work on evolving our algorithm toward
      a better solution.
2. **_Choosing metrics_**
    - We also need to think about how are we going to quantify the deviation from the defined truth.
    - Choosing the correct metrics will help us to accurately quantify the quality of our algorithm.

### Concern 2 - Is this the optimal way to get these results?

This is about finding the answer to the following question:
<br />
_Is this the optimal solution and can we verify that no other solution exists for this problem that is better than our
solution?_
<br />
But we need to consider this question as well:
<br />
_Should we aim to find the optimal solution for this problem? Finding and verifying the optimal
solution is so time-consuming and complex that a workable solution based on heuristics is our best
bet._
<br />
So understanding the problem and its complexities is important and helps us estimate the resource requirements.
<br />
A couple terms we need to know:

- **Polynomial algorithm**: If an algorithm has a time complexity of `O(N^k)`, we call it a polynomial algorithm,
  where `k` is a constant.
- **Certificate**: A proposed candidate solution produced at the end of an iteration is called a **certificate**. As we
  process iteratively in solving a problem, we typically generate a series of certificates. If the solution is moving
  toward convergence, each generated certificate will be better than the previous one. At some point, when our
  certificate meets the requirements, we will choose it as the final solution.

#### Characterizing the complexity of the problem

Before we attempt to design a solution to a problem, it makes sense to first try to characterize it. Generally, there
are three types of problems:

- **Type 1**: Problems for which we can guarantee that a polynomial algorithm exists that can be used to solve them.
- **Type 2**: Problems for which we can prove that they cannot be solved by a polynomial algorithm.
- **Type 3**: Problems for which we are unable to find a polynomial algorithm to solve them, but we are also unable to
  prove that a polynomial solution for those problems is impossible to find.
  Various classes of problems:
- **Non-Deterministic Polynomial (NP)**: For a problem to be an NP problem, it has to meet this condition
    - It is guaranteed that there is a polynomial algorithm that can be used to verify that the candidate solution (
      certificate) is optimal.
- **Polynomial (P)**: There are types of problems that can be thought of as a subset of NP. P problems need to meet this
  condition
    - It is guaranteed that there is at least one polynomial algorithm that can be used to solve them.
- **NP-complete**
- **NP-hard**

![classes_problems.png](_resources/images/classes_problems.png)

### Concern 3 - How is the algorithm going to perform on larger datasets?

- An algorithm processes data in a defined way to produce a result. As the size of the data increases, it takes more and
  more time to process the data and calculate the required result.
- The term _big data_ is used to identify datasets that are expected to be challenging for the infrastructure and
  algorithms to work with.
- To quantify the scalability of an algorithm, we need to keep the following two aspects in mind:
    - **The increase in resource requirements as the input data is increased**: Estimating a requirement such as this is
      called space complexity analysis.
    - **The increase in the time taken to run as the input data is increased**: Estimating this is called time
      complexity analysis.
- While in the development-and-testing phase, many algorithms use only a small sample of data. When designing an
  algorithm, it is important to look into the scalability aspect of the algorithms.

## Understand algorithm strategies

- A well-designed algorithm tries to optimize the use of the available resources most efficiently by dividing the
  problem into smaller sub-problems wherever possible.
- Three strategies:
    - The divide-and-conquer strategy
    - The dynamic programming strategy
    - The greedy algorithm strategy

### Understanding the divide-and-conquer strategy

- One of the strategies is to find a way to divide a larger problem into smaller problems that can be solved
  independently of each other. The sub-solutions produced by these sub-problems are then combined to generate the
  overall solution. This is called the **divide-and-conquer** strategy.
- Mathematically, if we are designing a solution for a problem `P` witn `n` inputs that needs to process datasets `d`,
  we split the problem into `k` sub-problems `P1` to `Pk`. Each of the sub-problems will process a partition of the
  dataset `d`. Typically, we will have `P1` to `Pk` processing `d1` to `dk`.

### Understanding the dynamic programming strategy

- Dynamic programming was a strategy proposed in the 1950s by Richard Bellman to optimize certain classes of algorithms.
- It is based on an intelligence caching mechanism that tries to reuse heavy computation. This mechanism is called *
  *memorization**.
- Dynamic programming gives good performance benefits when the problem we are trying to solve can be divided into
  sub-problems. The sub-problems partly involve a calculation that is repeated in those sub-problems. The idea is to
  perform that calculation once and then reuse it on the other sub-problems. This is achieved using memorization, which
  is especially useful when in solving recursive problems that may evaluate the same inputs multiple times.

### Understanding greedy algorithms

- Before we dive deep into, let's first define two terms:
    - **Algorithmic overheads**: Whenever we try to find the optimal solution to a certain problem, it takes some time.
      As the problems that we are trying to optimize become more and more complex, the time it takes to find the optimal
      solution also increases. We represent algorithmic overheads with `Ωi`.
    - **Delta from optimal**: The difference from optimal for the current solution in the `i`th iteration is called *
      *delta from optimal** and is represented by `Δi`.
- For complex problems, we have two possible strategies:
    - **Strategy 1**: Spend more time finding a solution nearest to optimal so that `Δi`, is as small as possible.
    - **Strategy 2**: Minimize the algorithmic overhead, `Ωi`. Use the quick-and-dirty approach and just use a workable
      solution.
- Greedy algorithms are based on strategy 2, where we do not make an effort to find a global optimal and choose to
  minimize the algorithm overheads instead.
- Using a greedy algorithm is a quick and simple strategy of finding the global optimal value for multistage problems.
  It is based on selecting the local optimal values without making an effort to verify whether local optimal values are
  globally optimal as well.
- Generally, a greedy algorithm is defined as follows:
    1. Let's assume that we have a dataset, `D`. In this dataset, choose an element, `k`.
    2. Let's assume the candidate solution or certificate is `S`. Consider including `k` in the solution, `S`. If it can
       be included, then the solution is `Union(S, e)`.
    3. Repeat the process until `S` is filled up or `D` is exhausted.

## Practical application - Solving the TSP

_Problem_: A traveling salesman needs to visit a given list of cities to get their job done:

| INPUT  | A list of `n` cities and the distances between each pair of cities, `d ij` _(1 =< i, j =< n)_ |
|--------|-----------------------------------------------------------------------------------------------|
| OUTPUT | The shortest tour that visits each city exactly once and returns to the initial city          |

- Note that:
    - The distances between the cities on the list are known.
    - Each city in the given list needs to be visited _exactly_ once.

_Can we generate the travel plan for the salesman?_

### Using a brute-force strategy

The brute-force strategy works as follows:

1. Evaluate all possible tours.
2. Choose the one for which we get the shortest distance.

If the number of cities `n` is equal to `10`, then we have `362,880` possible permutations. If `n` increases, the number
of permutations sharply increases and the brute-force method cannot be used.

### Using a greedy algorithm

- If we use a greedy algorithm to solve the TSP, then at each step, we choose a city that seems reasonable, instead of
  finding a city to visit that will result in the best overall path. Whenever we need to select a city, we just select
  the nearest city without bothering to verify that this choice will result in the globally optimal path.
- The approach is:
    - Start from any city
    - At each step, keep building the tour by moving to the next city where the nearest neighborhood has not been
      visited before.
    - Repeat step 2.
- The greedy algorithm is based on heuristics and there is no proof that the solution will be optimal.

## Presenting the PageRank algorithm

### Problem definition

### Implement the PageRank algorithm

## Understanding linear programming

- The basic algorithm behind linear programming was developed by George Dantzig.
- It is used to solve important real-world problems that relate to minimizing or maximizing a variable based on certain
  constraints. Some examples of these problems are as follows:
    - Minimizing the time to repair a car at a mechanic shop based on the resources.
    - Allocating available distributed resources in a distributed computing environment to minimize response times.
    - Maximizing the profit of a company based on the optimal assignment of resources within the company.

### Formulating a linear programming problem

- The condition to use linear programming are as follows:
    - We should be able to formulate the problem through a set of equations.
    - The variables used in the equations must be linear.

