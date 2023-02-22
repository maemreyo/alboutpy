## Intuition of this Problem:

- The intuition behind this code is that we want to find the minimum capacity of the ship that can ship all the packages
  within days days. We can use binary search to efficiently search for this minimum capacity.

- To perform binary search, we need to define the search range [left, right]. The minimum capacity should be at least as
  large as the largest package, so we set left to be the maximum weight in weights. The maximum capacity should be the
  sum
  of weights, so we set right to be the sum of all weights in weights.

- For each mid value in the search range [left, right], we simulate the shipping process to see if it can be done within
  days days using a ship with capacity mid. We start with the first package and add packages to the ship until it is
  full.
  When the ship is full, we start a new day and continue adding packages until all packages are shipped. We count the
  number of days needed to ship all packages with the current mid value.

- If the number of days needed with the current mid value is greater than days, it means that the ship capacity is too
  small, and we need to increase the capacity. Therefore, we set left = mid + 1. Otherwise, we can try to reduce the
  capacity by setting right = mid.

- We repeat this process until left >= right, at which point left is the minimum capacity of the ship that can ship all
  the packages within days days. We return left as the answer.

## Approach for this Problem:

1. Initialize maxWeight as -1 and totalWeight as 0
2. Iterate through the weights array and update maxWeight to the maximum weight in the array, and update totalWeight to
   the sum of all weights in the array
3. Use binary search to search for the minimum capacity of the ship that can ship all the packages within days days. Set
   left endpoint as maxWeight and right endpoint as totalWeight
4. While left endpoint is less than right endpoint, calculate mid-point as (left+right)/2
5. Simulate the shipping process using mid-point as the ship's capacity to see how many days are needed to ship all the
   packages.
6. Keep track of the current weight being loaded onto the ship and the number of days needed to complete the shipment.
   If the current weight plus the weight of the next package exceeds the mid-point, start a new day and reset the
   current weight. Repeat this until all the packages have been loaded onto the ship.
7. If the number of days needed is greater than days, set left endpoint to mid+1. Otherwise, set right endpoint to mid.
8. Continue the binary search until left endpoint is greater than or equal to right endpoint. At this point, left
   endpoint will be the minimum capacity of the ship that can ship all the packages within days days.