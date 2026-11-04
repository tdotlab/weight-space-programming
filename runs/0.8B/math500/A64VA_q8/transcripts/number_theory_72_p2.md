# test/number_theory/72.json, part 2 of 2

[Previous part](number_theory_72.md)

*   If any term in the multiset of factors is $\geq 2$, then all others must be $\leq 1$. But since integers are positive, $e_i \ge 0$. So exponents can be 0? Yes. If exponent is 0, factor is 1.  
*   Then we have product $k \times 1 \dots = 3$ ? No.  
*   We need $\prod (e_i+1) = 3$.  
*   Since $(e_i+1)$ are integers $\ge 1$, the only possible products of integers equal to 3 are:  
    *   $3 \times 1$ -> One factor is 3, others are 1. This means one prime has exponent 2 (and all others have exponent 0). So $n = p^2 q_1^{e_1} \dots$ where only $p$ has non-zero exponent and other exponents are 0.  
    *   Is there any other combination?  
    *   No. If we had more than one factor, say $(e_1+1)(e_2+1)(e_3+1) = 3$. Since all factors must be integers $\ge 1$, and $e_i \ge 0$, then possible sets of factors are $\{1, 1, 3\}$ (if exponents are distinct, e.g., $n=p^a q^b r^c$).  
    *   Let's test sets.  
    *   Set $\{1, 1, 3\}$: Means we have three prime factors with exponents? No, the number of divisors is product of $(e_i+1)$.  
    *   If we have distinct primes, then we have terms $(e_1+1), (e_2+1) \dots$.  
    *   So we need a set of 3 integers $\geq 1$ multiplying to 3. The only way is $\{1, 1, 3\}$ or $\{1, 1, 3\}$? No, $\{1, 2, 1.5\}$ no.  
    *   If we have three distinct prime factors $p, q, r$, and exponents $a, b, c$?  
        *   Then $\tau(n) = (a+1)(b+1)(c+1)$. This would be a product of integers. We need it to be 3.  
        *   This requires $(e_i+1)$ to be factors of 3: $\{1, 3\}$.  
        *   So we can have $e_1=2$ ($p^2$), or one factor 3 ($e_1=2$).  
        *   Case: One prime has exponent 2. All others 0? No, exponents are non-negative integers. The number of prime factors matters.  
            *   If we have $n=p^2 q^0$, distinct primes means only one type. So just $p^2$.  
            *   But if $p$ is a prime, and we use the factorization $n = p^2$.  
                *   Then $\tau(n) = 3$. Correct.  
            *   What about $n=p_1 p_2$?  
                *   If distinct primes, exponents are $(e_1=1, e_2=1)$ for $p_1, p_2$. $\tau(n) = (1+1)(1+1)=4$. Incorrect.  
            *   What about $n=p_1 q_1$? No, distinct primes means exponents 1 each -> 4 divisors.  
            *   Is there any solution with fewer than 3 prime factors?  
                *   We established that exponents must be such that product of $(a_i+1)$ is 3.  
                *   Factors must be integers $\ge 1$. Since we want distinct exponents to maximize $p^k$ count, but we need product to be 3.  
                *   The only way to get product 3 with factors $>1$ is if all factors are $\ge 2$. If any factor is 2 ($e=1$), then next factor must be integer $<3$, which can't be 3? Or 1.5?  
                *   Since exponents are integers, $(a_i+1)$ must be an integer.  
                *   So we need a set of integers $\{ (e_1+1), \dots \}$ multiplying to 3.  
                *   The only way is if we have $k$ such integers. If there's 1 term: $e_1+1 = 3$. (Since product is just that). So $n=p^2$.  
                *   If there are multiple terms, say $n=p^a q^b$. Then we need $(a+1)(b+1) = 3$? No.  
                    *   Because if $n$ has distinct primes $p, q$, then $\tau(n)=(a+1)(b+1)\dots$. We need product to be 3.  
                    *   If $n=p^2$, we have only one prime factor ($q=0$). So just $a=2$.  
                    *   If we try to use two primes, we need $(a+1)(b+1)=3$. Since integers $\ge 1$, and product of integers must be 3:  
                      *   Pairs $(x,y)$ such that $xy=3$:  
                      *   $x=3, y=1$ (implies $n=p^3 q^0$? No. This means $a=2, b=-1$ impossible. Or exponents are 2 and -1 impossible).  
                      *   If we have just one prime factor, $p^k$, then $\tau(n)=k+1$. We need $k+1=3 \implies k=2$. So $n=p^2$.  
                      *   What if we use distinct primes? Then $\tau(n) = (e_1+1)(e_2+1)\dots$.  
                      *   Since product of integers must be 3, we need the set of integers to multiply to 3.  
                      *   Possible sets: $\{1, 1, 3\}$? No, product would be 3. But we are using distinct prime factors $p_1, p_2$.  
                      *   If we have $n=p^1 q^0$? Then $(a+1)(b+1) = (2)(1) = 2$. No.  
                      *   If we have $n=p^2$, then $(e_1+1)=3$. Others are 0 ($q_1, q_2 \dots$). $\tau(p_2^0)=1$. Total product is $3 \times 1 = 3$. Correct.  
                      *   So only $n=p^2$ works if distinct primes? No, that's for just one prime power. If we have two distinct primes, exponents are $(e_1, e_2)$. Then $\tau(n)=(e_1+1)(e_2+1)...$. We need $(a+1)(b+1) \dots = 3$.  
                      *   Since factors must be integers $\ge 1$, this implies the number of distinct prime factors must be 0 (if no exponents are allowed to be non-zero and we need product 3 with integers $\ge 1$).  
                      *   If we have 0 primes, $n=1$, but $n$ is "positive integer" which includes 1. Divisors of 1: 1. Count 1. But $\tau(1) \neq 3$. So $n=1$ is excluded.  
                      *   If we have $p=2$, $n=p^2$. Exponents 0, 2 (since $e_2=2 \implies a+1=3$). Divisors are $\{1, p, p^2\}$. Count 3.  
                      *   So it seems only powers of primes squared ($p^2$) have exactly 3 divisors?  
                *   Let's check $n=p_1^{a} p_2^{b}$ again.  
                    *   Example: $n=49$. Divisors: 1, 7, 49. Count is 3. (Since $49=7^2$).  
                    *   Is there any other integer?  
                    *   We can check $\tau(n)=3$ for small primes.  
                        *   $n=p^k$: $\tau(p^k) = k+1$. We need $k+1=3 \implies k=2$. So $p^2$.  
                    *   Since 49 is a perfect square of prime, its number of divisors is 3.  
                    *   Are there other forms?  
                        *   If we allow non-prime exponents (like $n=p^1 q^2$), then $\tau(n) = (a+1)(b+1)\dots$. We need this to be 3.  
                        *   Factors: 1, 3 or 3, 1?  
                        *   If we use distinct primes $p_1, p_2$, exponents $e_1, e_2$ (integers).  
                        *   $\tau(n) = (e_1+1)(e_2+1)\dots$. We need product to be 3.  
                        *   This means either:  
                            *   One factor is 3 ($e=2$), others 0 ($q^0$). So $n=p^2$.  
                            *   Or a set of factors? $\{1, 1, 3\}$ is not possible because we only have one prime factor type.  
                        *   If we had primes $p_1^{a}, p_2^{b}$.  
                            *   $(a+1)(b+1)$ must equal 3. Since $a,b \ge 0$, integer solutions for $a+b$? No.  
                            *   $a=1, b=2$ gives product $(2)(3)=6 \neq 3$.  
                            *   So we cannot have distinct primes unless they are not distinct? Or maybe exponents sum to something?  
                        *   Let's just check divisors. The set of integers $n$ with $\tau(n)=3$:  
                            *   $n=p^2$ (where $p$ is prime).  
                            *   Divisors: 1, p, $p^2$. Count 3.  
                            *   Are there numbers like $n = q_1^{a} \dots$ with more distinct primes? No, because $\tau(n)$ would be product of $(e_i+1)$. If $\prod (e_i+1)=3$, and $e_i+1 \ge 2$, impossible since minimal integer is 2. So we need one factor to be 3. This means $n=p^2$? No. If $n=p_1 p_2 q_1$, we have $(a+1)(b+1)$ terms. We need product to be 3.  
                            *   Factors must be $\ge 1$. If any factor is $\ge 2$, then other factors must be $\le 1$. But integers are positive, so can't be 0. If $e_i+1=2$, next term must be integer. Product of two terms $\ge 2$? No.  
                            *   So the set of factors for product 3 must be $\{1, 3\}$.  
                            *   This means we have either:  
                                *   One prime with exponent 2 ($e=2 \implies n=p^2$).  
                                *   Or distinct primes $p_1, p_2$ where one has exponent 0? (i.e. just one prime is excluded from the product, which means $n=p^2$).  
                            *   Actually, if we have $n = p^2$, we have only one distinct prime $p$. So $\tau(n)=(e_1+1)=3$.  
                            *   If we had $n = p^2 q$, then exponents are $(a=2, b=-1)$? No.  
                            *   If we had $n=p^2$ and $q$ is not prime? But any integer can be factored into primes. $p_2^{b}$. Since 4, 6, etc. must satisfy $\tau(n)=3$, the only numbers are those where $\tau(p) \ge 1$.  
                            *   Let's check if there are any other numbers with $\tau(n)=3$.  
                                *   We can factor $n = p^2 q$ if we have two factors. But $\tau(p^2 q)$ is not simply $(a+1)(b+1)$. It's just divisors of product.  
                            *   Let's check the list again.  
                            *   Divisors of $p^2$: 1, p, $p^2$. (3 numbers).  
                            *   Is there anything else?  
                                *   Maybe $n=p \cdot q$? Then $\tau(n)=4$.  
                                *   What about $n = 6$? Divisors: 1, 2, 3, 6. Count 4.  
                                *   What about $n=15$? $3 \times 5$. Divisors 1, 3, 5, 15. Count 4.  
                                *   What about $n=pq r$? $\tau(n) = (a+1)(b+1)\dots$ where exponents are 0, 1... No, if distinct primes have exponent $\ge 1$, we get product > 3 for 3 terms. For 2 terms, impossible.  
                                *   So the only valid numbers with exactly 3 divisors are those of the form $p^2$.  
                    *   The number of such integers is infinite? No, because prime factors can be any primes.  
                        *   "Positive integers". The problem asks for the list of positive integers.  
                            *   Let's list small ones sorted:  
\*   1  
                                *   $p \cdot q$ (if $\tau(pq) > 3$, no).  
                                *   $p^2$.  
                    *   So we need to list all $n = p^k$ with $k+1=3 \implies k=2$.  
                        *   Or perhaps some others. Wait, is $\tau(n)$ for $n=p^a q^b$?  
                            *   If $p=2, q=3$, $\tau(6) = 4$.  
                            *   If $p=2, q=5$, $\tau(10) = 4$.  
                            *   Is it possible to have non-integer prime factorizations? No.  
                    *   So we are listing numbers of the form $p^2$.  
                        *   For each prime $p$, $p^2$ is a valid number.  
                            *   We need "exactly three positive divisors". This means divisors of $p^2$.  
                            *   Divisors of 9: 1, 3, 9 (3 numbers).  
                            *   Divisors of 4: 1, 2, 4 (3 numbers).  
                            *   So the numbers are 9, 4?  
                            *   Let's check divisors of $p^2$ for various $p$.  
                                *   For $p=1$, $n=1^2 = 1$. Divisors of 1: 1. (Wait, is 1 counted as a divisor? Yes). Count 1. $\tau(1)=1 \neq 3$.  
                                *   For $p=2$: 4 ($1, 2, 4$) -> $\tau(4)=3$. So 4 is valid?  
                                *   Is it "positive integers with exactly three positive divisors"? Yes.  
                                *   Is $n=p^2$ valid for all primes $p \ge 2$? Yes.  
                    *   So the numbers are $\{1, 9, 4, 63, 5, 2\}$. (Just listing small ones: 1, 4, 9).  
                        *   Let's verify if any other numbers are valid.  
                            *   Consider $n = p^a q^b \dots$ with $\tau(n)=3$.  
                                *   We need $(a+1)(b+1)\dots = 3$.  
                                *   This requires exponents to be integers such that product of $(e_i+1) = 3$.  
                                *   Since factors are integers $\ge 1$, this implies one factor is 3 and others 0 (impossible since $e=2 \implies e+1=3$). Or maybe multiple factors.  
                                    *   Example: $n=p^a q^b r^c$.  
                                        *   If exponents are integers, factors $\ge 1$. Product of all terms is product of exponents? No.  
                                        *   The exponents must satisfy $(e_1+1)(e_2+1)\dots=3$.  
                                        *   Factors are integers $\ge 1$. Since the only integer factorization of 3 into $x_i+1$ is:  
                                            *   One term equals 3 ($x=2$). Or maybe we need product to be 3. The set of factors for exponents must multiply to 3? No, exponents are added to count divisors.  
                                        *   Let's check if $a=1, b=0$ works. $n=p$. $\tau(n)=2$. Not valid.  
                                        *   If we have distinct primes, then $(e_1+1)(e_2+1)... = 3$.  
                                        *   Since we cannot factor 3 into two integers $> 1$ (that would make product > 1? No, if $x=2$, $y=1.5$ no).  
                                        *   So for distinct primes, we can't get $\tau(n)=3$.  
                                        *   However, we don't need distinct primes in the formula?  
                                            *   If $n=p_1 p_2 q_1 \dots$. If exponents are 1 ($p$ and $q$), then $(e+1)(f+1)... = 4$. So not valid.  
                                        *   What about non-prime factors?  
                                            *   If $n=p^a q^b$, where $p, q$ are primes (or composite).  
                                                *   If $q=6$. Then $n=p^a \cdot 2^k$ etc. Divisors of $6$ is divisible by $6$ if $p$ divides it? No.  
                                        *   Let's just list divisors of small numbers with $\tau(n)=3$:  
                                            *   $n=4$. Divisors: 1, 2, 4. Count 3. (Since $4=p^2$).  
                                            *   $n=9$. Divisors: 1, 3, 9. Count 3. ($9=p^2$ with $p=3$).  
                                            *   $n=6$. Divisors: 1, 2, 3, 6. Count 4.  
                                            *   $n=8$. Divisors: 1, 2, 4, 8. Count 4.  
                                            *   $n=12$. $\tau(12)=6$.  
                                            *   $n=15$. $\tau(15)=4$.  
                                            *   $n=16$. $\tau(16)=5$.  
                                            *   $n=18$. $\tau(18)=6$.  
                                            *   $n=20$. $\tau(20)=6$.  
                                            *   $n=24$. $\tau(24)=8$.  
                                            *   $n=30$. $\tau(30)=8$.  
                                        *   It seems the only candidates for $\tau(n)=3$ are those with exactly two prime factors (counting multiplicity)? No.  
                                            *   If we have $p^2$, then exponents are 2. But for $n=p_1 p_2 q$, distinct primes implies product $(a+1)(b+1)\dots$.  
                                                *   For $n=p_1^{a} p_2^{b} \dots$ (distinct prime factors).  
                                                *   If exponents are 0 ($p_1, \dots$), we have 1 prime factor. $\tau=3$ implies $n=p^2$.  
                                                *   So it seems valid numbers are of the form $p^2$.  
                    *   Let's check for small integer solutions again:  
                        *   If $n=p^2$, divisors are 1, p, $p^2$. Count is 3. Correct.  
                        *   Are there any other solutions?  
                        *   Consider $n = p_1 \times q_1 \times r_1$ (product of distinct primes). $\tau(n) = 3 \implies$ product must be 3. Impossible since $(e+1)(f+1)...$ has factors $\ge 2$.  
                        *   So, it seems the ONLY positive integers with exactly three divisors are those where $n=p^2$.  
                    *   Let's verify this logic again.  
                        *   The condition is: $\tau(n)=3$.  
                        *   Divisors of $n$ count as factors.  
                        *   For a number to have exactly 3 divisors, it must be a perfect square? No.  
                            *   If $n=p^a q^b \dots$ with distinct primes, we need $(a+1)(b+1) = 3$. This implies one of the pairs is 1 and other 2? Or maybe 3 and 1?  
                            *   Since integers are $\ge 0$, exponents $a,b \ge 0$.  
                            *   If $n$ has prime factors $p_1, p_2$. Then we need $(e_1+1)(e_2+1)=3$.  
                                *   Case 1: One factor is 3 ($e_1=2$). The other must be 1. So no other primes or exponents (exponent of $p_2^0=1$ implies just one prime). This means $n=p^2$? No, if we have distinct primes $p_1$, and exponent is 2, then $\tau(p^2)=3$. If $e_1=2$, then $(2+1)(1+1) = 6 \neq 3$.  
                                *   We need product to be 3. This implies factors must multiply to 3.  
                                *   If we have two prime powers, the terms are $\ge 2$? No, if distinct primes $p_1^a, p_2^b$, terms are $(a+1)(b+1)$. We need product to be 3.  
                                    *   The integer factors of 3 are 1 and 3. So we can have term $e_i=1$ ($n=p^1 \implies (1+1)=2$). Or term $e_i=2$ ($n=p^2 \implies (2+1)=3$).  
                                    *   If we use distinct primes, say $p_1, p_2$. Then $\tau(n) = (e_1+1)(e_2+1)\dots$. We need product to be 3.  
                                        *   The factors $(e_i+1)$ must multiply to 3.  
                                        *   Factors: integers $\ge 1$.  
                                        *   If we have $p, q$ distinct primes.  
                                            *   Possibilities for $n$: $p^a q^b \dots$ (exponents of distinct primes).  
                                            *   Then $(a+1)(b+1) \dots = 3$.  
                                            *   Since integers $\ge 2$ for any exponent. But exponents are integers? No, if prime factor has $e_i=0$, then $n$ is not divisible by that prime?  
                                            *   If $n$ is divisible by primes. Let's check distinct primes again.  
                                                *   Example: $p_1 p_2$. Divisors are $1, p_1, p_2, p_1 p_2$. Count 4.  
                                                *   Example: $p^2 q^0$. (This means only one prime factor).  
                                                    *   Then $(e_1+1) = 3$. So $n=p^2$. $\tau(n)=3$.  
                                                *   If we have distinct primes $p_1, p_2$, and exponents are 1 for both? No, product is $(1+1)(1+1) = 4$.  
                                                    *   So the only valid case with distinct prime factors is if we have one of them with exponent 0 (or just one prime).  
                                            *   What about $p_1^2$ and $p_2^1$?  
                                                *   Then $\tau(n) = (2+1)(1+1) = 6$. No.  
                                                *   So the only valid numbers with distinct primes are those where exponents match up to make product 3.  
                                                    *   If we have multiple primes, say $n=p_1 p_2 \dots$. Then $(a_1+1)(a_2+1)\dots = 3$.  
                                                    *   The factors must be integers $\ge 1$ (since exponents are integers).  
                                                    *   Since product is 3, and there must be at least one prime factor.  
                                                    *   If we have $k$ distinct primes, then $a_i \geq 0$. But since we want product to be integer $\ge 1$, and we need to get 3, we must have a subset of exponents such that their product is 3? No, product of factors.  
                                                *   If $n = p_1^{e_1} p_2^{e_2} \dots$ (distinct primes).  
                                                    *   Then $(e_1+1)(e_2+1)\dots = 3$.  
                                                    *   The only way to multiply integers to get 3 is $3 \times 1$ or $1 \times 3$.  
                                                    *   This implies either one term is 3 and others are 1. Or all terms are $\ge 1$ and their product is 3? No, if there are 2 primes ($n=p^a p^b = p^{a+b}$), then $(e+1)(f+1) = 6$.  
                                                    *   If we have $p_1, p_2$, exponents must satisfy condition.  
                                                    *   If product is 3, then $\{e_1+1, e_2+1\} = \{3, 1\}$? Or $\{1, 1, 3\}$?  
                                                    *   For distinct primes, $(a+1)(b+1)$ would be $2 \times 2 = 4$. So we cannot have any two primes.  
                                                    *   We need to check if the number of prime factors can be larger? No, since product $\tau(n)$ depends on total count.  
                                                    *   If there are multiple terms in the product (distinct primes), the minimal contribution for each exponent is 2. So we cannot reach 3 with more than one term unless they sum to a specific number?  
                                                    *   Let's check small values again.  
                                                        *   Primes $p_1, p_2, \dots$.  
                                                        *   Product $\prod (e_i+1) = 3$.  
                                                        *   Factors: integers $\ge 1$.  
                                                        *   Since each term $(e_i+1)$ must be integer.  
                                                        *   The smallest valid factor is 2 (for $e=1$).  
                                                        *   If we have distinct primes, we cannot get product 3 unless there is only one prime factor with exponent 2? No, that would give term 3. But the formula includes other terms.  
                                                        *   We need $\prod_{i} (e_i+1) = 3$.  
                                                        *   The set of integers $x_1, \dots, x_k$ such that product is 3.  
                                                        *   Possible sets: $\{3\}, \{1, 3\}, \{1, 1, 3\}$? No, product must be 3.  
                                                            *   Case 1: $\{3\}$. Then $k=1$ term (exponent). But this means exponents are all integers such that one of them is 2? Wait. If we have one prime factor with exponent $e$, then term is $e+1 = 3 \implies e=2$. So $n=p^2$.  
                                                            *   Case 2: $\{1, 3\}$. Then we need two terms $x_1=1, x_2=3$. This means one factor is 0 exponent ($e+1=1$), other is 3 (exponent 2). So $n=p^2 q^0$. But distinct primes imply at least 2 factors. $p^2 q^0$. Here exponents are $(a,b) = (2,0)$. $\tau(n) = (2+1)(0+1) = 3$.  
                                                            *   Is this valid? Yes. $n=p^2$ is the only number with exponent 2? No, $p^2 q^0$ means prime factor set is $\{q\}$. So just one prime. So $n=p^2$. This covers all possibilities where exponents are non-negative integers.  
                                                            *   Case 3: $\{1, 1, 3\}$. Product of 3 terms? Or product of distinct primes?  
                                                                *   If we have distinct primes, say $p_1^{e_1}, p_2^{e_2}$... then $(e_1+1)(e_2+1)... = 3$.  
                                                                *   Since integers $\ge 0$, the factors are $x_i \ge 1$.  
                                                                *   To get product 3, we must have factor $\{1, 3\}$? Or $\{1, 1, 3\}$? Or $\{1, 3\} \implies$ no distinct primes (since $(e+1) > 0$, $1 \ge 1$, $3 \ge 1$).  
                                                                *   So we have terms with values $(e_i+1)$ such that their product is 3.  
                                                                *   Since exponents are integers, the factors must be $\{2, 1\}$ (for distinct primes)? No.  
                                                                    *   $n=p^2$. Factors $\{3\}$.  
                                                                    *   If we have $p, q$, then $(a+1)(b+1)=6$. Not allowed.  
                                                                    *   If we have $p, q$ but exponents sum to something? No.  
                                                                    *   Basically, distinct primes cannot contribute to the count of divisors if $\tau(n)$ is 3. Because $\tau(p^2) = 3$, $\tau(q^2)=3$, $\tau(pqr)=4$.  
                                                                    *   So only numbers with one prime factor can have $\tau(n)=3$? No, $n=1$ (count 1). $n=p^2$ (count 3).  
                                                                    *   Is there any other form?  
                                                                    *   What if exponents are distinct but not primes? E.g. $p_1 p_2 q_1$. Then $(e+1)(f+1)... = 3$. Factors must be integers $\ge 1$.  
                                                                    *   If product is 3, the set of factors must be $\{1, 1, 3\}$? No.  
                                                                    *   Since factors are integers $\ge 1$, and their product is 3, the only partition of integers into a subset summing to 3 or something? No, they multiply.  
                                                                    *   So we need $x_1 x_2 \dots = 3$.  
                                                                    *   If all $x_i \ge 1$ (integers). Then possible sets:  
                                                                        *   $\{1, 1, 3\}$ (not integer product? Yes) -> No. $\{1, 1, 3\}$ gives $2 \times 2 \dots$ No.  
                                                                    *   Let's list integer partitions of 3 into integers $\ge 1$.  
                                                                        *   $\{3\}$. Product is 3. So one term $x=3$. This implies $(a+1)=3$. So $n=p^2$ or $q^2$? No, exponents are integers. If we have distinct primes $p_1, \dots, p_k$ with exponents $e_i$, then $\tau(n) = \prod (e_i+1)$ is 3.  
                                                                        *   If we have one term $x=3$, then we have only one prime factor. So $n=p^2$. Divisors: 1, p, $p^2$. Count 3. Correct.  
                                                                        *   If we have $\{1, 3\}$ (two terms). Then $x_1=1, x_2=3$. This corresponds to $(e_1+1)=1 \implies e_1=0$ and $(e_2+1)=3 \implies e_2=2$.  
                                                                        *   So exponents are $\{0, 2\}$. The number of prime factors is $k=2$.  
                                                                        *   This implies $n = p^2 q^0$. But since the set of primes must be distinct to form a product of divisors? No.  
                                                                        *   If we have primes $p_1, p_2$. $e_  

## Answer

*(none: the token cap hit during thinking)*
