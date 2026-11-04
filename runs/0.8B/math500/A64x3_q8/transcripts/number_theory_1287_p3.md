# test/number_theory/1287.json, part 3 of 3

[Previous part](number_theory_1287_p2.md) · [Start](number_theory_1287.md)

Because I evaluated the expression for $a=3, b=5$:  
$a(2a+b)-2a^2+ab = 3(6+5) - 18 + 15 = 33 - 18 + 15 = 30$.  
So $N=30$ is the value.  
Then divisors of 30 are $\{1, 2, 3, 5, 6, 10, 15, 30\}$?  
Let me re-verify this list.  
Divisors of 30:  
Is 1 a divisor? Yes.  
Is 2 a divisor? No, $30/2 = 15$, so 2 divides 30. Yes.  
Is 3 a divisor? $30/3 = 10$. Yes.  
Is 4 a divisor? $30/4 = 7.5$. No.  
Is 5 a divisor? $30/5 = 6$. Yes.  
Is 6 a divisor? $30/6 = 5$. Yes.  
Is 10 a divisor? $30/10 = 3$. Yes.  
Is 12? No.  
Is 9? No.  
Is 8? No.  
Is 14? No.  
So $\{1, 2, 3, 5, 6, 10, 15, 30\}$ has 8 divisors.  
BUT for $N=ab$ (where $a,b$ are primes), the count should be $(e_a+1)(e_b+1) = (1+1)(1+1)=4$.  
This means $d(30)$ is NOT $d(p_1 p_2 \cdot \dots)$?  
Why does 30 have more divisors than 6 ($p_1 \cdot p_2$)?  
Because 30 has prime factors 2, 3, 5.  
But my previous derivation that $N=ab$ for distinct primes means $d(N)=4$ assumed exponents are $(1, 0)$? No.  
If I have product of primes $p_1 \cdot p_2$, then the divisors are those formed by picking one from $p_1$ and one from $p_2$. The set is $\{1, p_1\} \times \{1, p_2\}$? No.  
The product of factors $d(p_i)$.  
For prime $p$, divisors are $1, p$. (2 factors).  
So the number of divisors of a number with prime factorization $p_1^{e_1} \dots$ is $(e_1+1)(e_2+1)\dots$.  
Since distinct primes have no exponent > 1, they are of form $p_1^0 p_2^0 \dots$ No, distinct primes mean exponents are all 1.  
So number of divisors is $4$.  
BUT I calculated $d(30)=8$.  
Where is the discrepancy?  
Ah, because for distinct primes $a, b$, the product is NOT just a product of two numbers with prime factors? No, $ab$ is an integer. Its factorization depends on $a, b$.  
If $N = ab$, and $a,b$ are primes, then $N = p \cdot q$.  
Then prime factorization of $N$ is $\{p_1, p_2\}$ with exponents 1, 1.  
So divisors count should be $(1+1)(1+1)=4$.  
Why did I calculate $d(30)=8$?  
Ah, maybe because I'm not sure if 30 has exactly those factors.  
Let's check the divisors of 30 again.  
Is there any other divisor? No.  
But my previous manual calculation found $\{1, 2, 3, 5, 6, 10, 15, 30\}$ (8 numbers).  
Is it possible that $d(30)$ is 8 but the number of divisors for $N=ab$ should be something else?  
If $a=3, b=5$, then $ab = 15$.  
So $N$ evaluated to $2ab$ means $ab=15$ or something?  
No, I calculated $N = 2ab$ which implies $N$ is just product of numbers.  
For $a=3, b=5$, $ab = 15$.  
Divisors of 15: $\{1, 3, 5, 15\}$. Count is 4.  
For $a=3, b=7$, $ab = 21$. Divisors $\{1, 3, 7, 21\}$. Count is 4.  
This matches the  

## Answer

*(none: the token cap hit during thinking)*
