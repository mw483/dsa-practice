# Coding Challenge Problems
This is for reference (that no one needs). I planned to add personal difficulty but decided not to. Just keep in mind that all of this is humanly possible to solve it in time, I spent the entire 60 minutes for both of them as a washed up IOI contestant

## Rakuten
* 1 problem, 60 minutes
* Implement-heavy, many cases to consider
* Most of the time spent on making sure that it covers all cases, as the platform doesn't give you hidden test cases results

### Mikael personal notes
* Similar to [Leetcode 221 (Maximal square)](https://leetcode.com/problems/maximal-square/description/)
* DP problem?

### Problem 1
Given an array $A$ of size $N\times M$, each cell $A[i][j]$ can have the following value
* $A[i][j] = \texttt{true}$, the cell is an empty space
* $A[i][j] = \texttt{false}$, the cell is a wall

We want to place **two squares** with **same size** on the grid, where
* The squares do not overlap, and
* The squares should not cover a wall

Find the largest possible size that the squares can be placed

#### Constraints
* $N, M \leq 700$

#### Solution
<details>
    <summary>During the challenge</summary>
    During the challenge $\mathcal{O}(NM\log(\max(N, M))$:
    Binary searched the answer. Once the size is fixed, iterate the grid and check if it is possible to make a square at that position, and if there exists any valid square position behind them (details omitted because 面倒くさい). 
</details>

<details>
    <summary>After the challenge</summary>
    After the challenge $\mathcal{O}(NM + N\log N + M\log M)$:
    Use dynamic programming to find the largest square for each cell. Collect the maximum across each row and column, then we can iterate the rows and column separately to find $\max(min(row[i] - k, k) \text{ for each }k\text{ from 1 to }row[i])\$ (same goes for column). This can probably be binary-searched
</details>

## Mercari
* 2 problems 60 minutes
* Personally, I spent about 55 minutes solving and debugging problem 2. The first problem seems difficult at first glance, but taking break from second problem and looking back actually gives me an instant idea on how to solve it. (Still, bad time management though)
* Time constraint is pretty tough for this one

### Problem 1
Given an array $A$ of size $N$. In one operation, we can flip **one bit** of **one element** in the array. Find the minimum number of operations to make all the elements in the array equal

#### Constraints
* $N \leq 200\,000$
* $A[i] \leq 10^9$

#### Solution
<details>
    <summary>Solution</summary>
    $\mathcal{O}(N\log(\max(A[i])))$:
    "Transpose" the array to get the sum of each bits across the array instead. For each bit $b$, add $\min(count[b], N - count[b])$ to the answer.
</details>

### Problem 2
Given an array $A$ of size $N$. Count the number of all subarrays that have an odd number of divisors of its product. (จำนวนตัวประกอบของผลรวมเป็นเลขคี่)

#### Constraints
* $N \leq 200\,000$
* $A[i] \leq 200$

#### Solution
<details>
    <summary>Solution</summary>
    $\mathcal{O}(N\sqrt{\max(A[i])})$ ?:
    Convert every number in the array to the form of prime factor, and only concern about the parity of the exponent (p^1 = p^3). Using this, we make some kind of a prefix xor. As we know that the number of divisors is sum of (exponent + 1), the one that have odd number of divisor is the subarray with every single value of exponent in the mod 2 space as 0. To omit a lot of things, we have to find the number of matching previous prefixes for the current prefix and add it to the answer.
    Since the value of A[i] is small, I just used a map to store the "dp" value. I know the explanation is bad, but maybe that will give some idea

</details>

## LY Corporation
* 2 problems: one algorithm, one implementation?
* I'll only talk about the first question (algorithm), this one is 90 minutes
* Probably the easiest one so far due to the friendly 90 min time constraint. Finished with 42 minutes left (with a lot of re-check and comments)

### Problem 1
Given $N$ possible reservation time slots numbered from $1$ to $N$, where $1$ is the earliest and $N$ is latest. We know that $M$ slots: $a_1, a_2, \ldots , a_m$ have already been reserved. There are $Q$ questions we want to ask.

For each question $i$, given a range from $l_i$ to $r_i$, return the earliest time slot that has not been reserved yet. If every time slot is reserved, then return $-1$. Each question is independent to each other and will not modify the initial reservation.

#### Constraints
* $N \leq 10^{12}$
* $M, Q \leq 10^5$
* $1 \leq a_i, l_i, r_i \leq N$
* $a_i < a_{i+1}$
* Time limit 6000 ms, memory limit 512 MB (I don't know why)

#### Solution
<details>
    <summary>Solution</summary>
    $\mathcal{O}(MlogM + QlogM)$ ?:
    For each value of a_i, group the consecutive segment together and label it with the rightmost value of a in that segment (can use DSU and stuffs). 
    Then we can easily do online query by using lower_bound function on l_i and check the segment's end with r_i. This requires some condition to cover a few cases, but not too problematic
</details>
