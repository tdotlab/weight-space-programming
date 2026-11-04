# test/counting_and_probability/23957.json, part 2 of 2

[Previous part](counting_and_probability_23957.md)

*   Why did I keep thinking of it as $\binom{n}{k} = \frac{n!}{k!(n-k)!}$? That is exactly what I just wrote out: $\frac{7 \cdot 6 \cdot 5}{3! \cdot (4!) }$ is wrong because $(n-k)$ is 4, so $(4)! = 24$. But I'm using $3,2,1$ to represent the denominator.  
*   The term $(n-k)!$ in $\binom{n}{k}$ is actually $(7-3)! = 4!$. Wait, that's not how it works.  
*   Ah, I see my confusion. In $\binom{7}{3}$: numerator is $7 \cdot 6 \cdot 5$. Denominator is $3!$. Why? Because we are selecting 3 items from 7. The number of ways to arrange them is not relevant here. We are just counting the subsets.  
*   Formula: $\binom{n}{r} = \frac{n(n-1)...(n-r+1)}{r!}$.  
*   This uses $n$ in numerator (7). And $(n-1)$ down to $(7-3+1) = 5$. And divides by $r!$ (3!).  
*   So it is $\frac{7 \cdot 6 \cdot 5}{3!}$.  
*   Denominator is 6.  
*   $210 / 6 = 35$.  
*   Okay, the calculation is definitely 35.  
*   My confusion stemmed from thinking about $\frac{n!}{k!(n-k)!}$ where I might have thought $(n-k)!$ was involved with a factorial of something else, but in this case it's just $7 \times 6 \times 5$.  

*   **Double check the formula:**  
*   Combinations: $\frac{1}{k!} \binom{n}{k}$? No.  
*   Formula is $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.  
*   If I plug in $n=7, k=3$. Denominator is $3! \times (4!)$.  
*   $5040 / (6 \times 24) = 10.5$? No. That was the error.  
*   Let's check $\binom{5}{3}$ again. $120/24 \cdot 24$? No. $\binom{5}{3} = \frac{5 \cdot 4 \cdot 3}{3!} = \frac{60}{6} = 10$.  
*   My previous calculation for $\binom{7}{3}$ yielded $35$.  
*   If the formula was $\frac{n!}{k!(n-k)!}$, it would give:  
*   Num: $5040$. Denom: $6 \times 24 = 144$.  
*   $5040 / 144$:  
*   $5040 / 144 \approx 34.7$.  
*   This is not 35.  
*   So $\binom{n}{k}$ MUST be using the factorial terms to cancel out $(n-k)!$ and reduce to the remaining numerator! No, it should use $n!(n-1)...(n-r+1)$ over $r!$.  
*   So for $C(7,3)$: $\frac{7 \cdot 6 \cdot 5}{3!} = 35$.  
*   Okay, I was confusing myself with the full factorial notation. The correct expansion is indeed $\binom{n}{k} = \frac{n(n-1)...(n-k+1)}{k!}$.  
*   So for $n=7, k=3$: $\frac{7 \cdot 6 \cdot 5}{3!} = 35$. Correct.  

*   **Final Answer Confirmation:** 210.  


## Answer

The problem asks us to find the number of ways to pick 3 boys and 2 girls from a class of 7 boys and 4 girls, given that the order in which they are chosen does not matter. This is a classic combination problem.  

Here is the step-by-step reasoning:  
1.  **Identify the components:**  
*   Number of boys ($n_B$) = 7.  
*   Number of girls ($n_G$) = 4.  
*   We need to choose 3 boys and 2 girls.  

2.  **Determine the method (Combinations vs Permutations):**  
*   The problem states: "The order in which the boys and girls are chosen does not matter."  
*   In combinatorics, when the order of selection doesn't matter for the final group (the set of students), this implies we should use **combinations** ($\binom{n}{k}$) rather than permutations. If we were to pick an ordered list (e.g., "Boy 1 then Boy 2"), that would be a permutation ($P(n,k)$).  
*   The phrase "pick ... to give a group presentation" usually implies selecting the students present in the class for a specific group. Since the question specifies order does not matter, we select a subset of size $k$ from the total pool.  

3.  **Calculate the combinations:**  
*   We choose 3 boys out of the 7 available:  
$$ \binom{7}{3} = \frac{7!}{3!(7-3)!} = \frac{7!}{3!4!} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = 35 $$  
*   We choose 2 girls out of the 4 available:  
$$ \binom{4}{2} = \frac{4!}{2!(4-2)!} = \frac{4!}{2!2!} = \frac{4 \times 3}{2 \times 1} = 6 $$  

4.  **Multiply the results:**  
*   Since we are selecting a group of boys and a separate selection from girls, and order does not matter for the boys and for the girls (meaning we just select a subset of individuals), the total number of ways is the product of the combinations:  
$$ \text{Total Ways} = \binom{7}{3} \times \binom{4}{2} $$  
$$ \text{Total Ways} = 35 \times 6 $$  
*   Calculation:  
$$ 30 \times 6 = 180 $$  
$$ 5 \times 6 = 30 $$  
$$ 180 + 30 = 210 $$  

Therefore, there are 210 ways to pick a group of 3 boys and 2 girls.  

\boxed{210}  
