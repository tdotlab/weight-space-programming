# test/number_theory/72.json, part 3 of 3

[Previous part](number_theory_72_p2.md) · [Start](number_theory_72.md)

*   If $n=4$ ($p^2$). Divisors: 1, 2, 4. Count is 3.  
*   So for $n=p^k$, count is $k+1$.  
*   Let's re-evaluate the divisors of a general number.  
*   If $n$ has prime factorization $\prod p_i^{a_i}$, then $\tau(n) = \prod (a_i+1)$? No. That would mean $\tau(6)=4$. Wait, $6=2^1 3^1$. So $(1+1)(1+1)=4$. Correct.  
*   Is there a case where this formula fails?  
*   Let's check $n=12$ ($p_1=2, p_2=3, e_1=2, e_2=1$). Formula $(2+1)(1+1)=6$. Divisors count is 6. Correct.  
*   Is there a case where $d(n)$ is not product?  
*   Wait, I'm confusing the formula with something else.  
*   Let's look at it again: "positive  

## Answer

*(none: the token cap hit during thinking)*
