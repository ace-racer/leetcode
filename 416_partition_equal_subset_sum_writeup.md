Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

## Solution approach:

1. If the total sum is odd - it cannot be divided into 2 equal parts
2. If the total sum is even:
3. Then we use dp appraoch to construct a boolean list that contains all possible sums upto & including specific index
possible_sums[x] = {possible_sums[x-1]} union {possible_sums[x-1] + nums[x]}
4. Finally we check if the a sum is possible for index total_sum // 2