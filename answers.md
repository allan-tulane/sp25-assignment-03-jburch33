# CMPS 2200 Assignment 3
## Answers

**Name:**_____Joshua Burch____________________


Place all written answers from `assignment-03.md` here for easier grading.

1 a.

You have N dollars.

Select the largest coin 2^k that is less than or equal to N

Subtract 2^k from N, and record the cost of the coin 2^k

Repeat until N=0

1 b.
Proof

Suppose the largest coin is picked 2^k and is less than or equal to N

Let N' = N - 2^k

N' is less than N therefore the greedy algorith can still be applied

This is optimal because every number has a unique binary representation, and the highest power of 2 is always part of the sum.

1 c. 

Work: O(logn)

Span: O(logn)


2 a.

The greedy algorithm fails when the largest available denomination is not always part of the optimal solution.

Let the Denominations D = {10,6,1} and N = 12

Greedy Approach

Pick largest denomination first: 10

12 - 10 = 2

Therfore you must pick two 1's next

Total coins used: 3

Optimal Approach:

Choose two 6's

Greedy Algorith uses one more coin therefore is not optimal

2 b. 

Assume there is an optimal way to make N using coins, and the first coin used is some denomination D_i

This means the remaining problem is to make change for N' = N - D_i

The problem of making N - D_i is a subproblem

Therefore we must find the minimum number of coins for each subprobelm to solve the minimum number of coins C(n) to make N

C(n) = min D_i <= N (1+C(N - D_i))

2c

C = [float('inf')] * (N + 1)

C[0] = 0  

for n in range(1, N + 1):            

    for D_i in D:                   
    
        if D_i <= n:
        
            C[n] = min(C[n], 1 + C[n - D_i])


W(n) = O(nk)

S(n) = O(n)








