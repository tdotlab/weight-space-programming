# test/algebra/276.json, part 2 of 2

[Previous part](algebra_276.md)

So $AB > 0$ condition is not satisfied.  
If $A=B=2$, product is 4. Not 10.  
Wait, my pairs $(A,B)$ are integers such that $AB=10$.  
I found $(5,2)$ works.  
What about $(A,B)=(-5, -2)$?  
$AB = 10$. This would be $-31 \dots$ No.  
Let's check if I made a mistake in checking the negative solutions.  
Condition: $AB=10$.  
Factors of 10: $(\pm 1, \pm 10), (\pm 2, \pm 5), (\pm 5, \pm 2), (\pm 10, \pm 1)$.  
Check each for $3A - 8B = -1$.  
1. $A=1, B=10$: $3-80=-77$. No.  
2. $A=10, B=1$: $30-8=22$. No.  
3. $A=2, B=5$: $6-40=-34$. No.  
4. $A=5, B=2$: $15-16=-1$. Yes. (Positive A,B).  
5. $A=-1, B=-10$: $-3+80=77$. No.  
6. $A=-10, B=-1$: $-30+8=-22$. No.  
7. $A=-2, B=-5$: $-6+40=34$. No.  
8. $A=-5, B=-2$: $-15+16=1$. No.  

So $(5, 2)$ is the unique solution.  
Thus $AB+B = 10+2 = 12$.  

The reasoning holds up completely.  
No hidden complexity.  
Just checking: $(Ax-8)(Bx+3)$.  
Is there a simpler way to see it?  
$10 = 2 \cdot 5$.  
If we divide by $24/10 \approx 3$, not easy.  
The system is linear, so unique solution in integers for coefficients sum/product.  

One small check: what if the question was $(Ax+B)(Cx+D)$?  
$A C x^2 + B D x + A C D$. No.  
The problem statement gives a specific form $(Ax-8)(Bx+3)$.  
It's fixed.  

Final Answer seems to be 12.  

One detail: "integers" - does $AB+B$ need to be an integer? Yes.  
The result is integer 12.  
If the question implied non-integers, it would be weird.  
Given constraints, integers are likely required.  
If they didn't require $A,B$ integers, I couldn't solve it quickly. But here $3A-8B=-1$ with $AB=10$ forces a unique integer solution, which makes it a clean problem.  

The logic is sound.  

Final Check:  
Expression: $10x^2 - x - 24$.  
Factors: $(5x-8)(2x+3)$.  
$A=5, B=2$.  
$AB = 10$.  
$B = 2$.  
$AB + B = 10 + 2 = 12$.  

Seems correct.  

Another perspective:  
Is there any other factorization?  
$(Ax-Bx)(...)$ No.  
Maybe $(5x-8)$ is related to $-x - 24$ via some relation?  
Sum of factors of 10 and 3?  
If $B=2, A=5$.  
Product of roots of cubic?  
Discriminant $D = (-b)^2 - 4ac$.  
For quadratic $ax^2+bx+c$, we need to match coefficients.  
Coefficients are 10, -1, -24.  
$B = (x) + \dots$ No.  

The answer is definitely 12.  

Double check the sign in $(Ax-8)$ and $(Bx+3)$.  
If it was $(-5x+8)(2x+3)$, product would be $(-5)(2)x^2 ... = -10x^2$. No match.  
If it was $(5x+8)(2x-3)$, constant term is $-16$, not -24. No match.  
So signs are fixed relative to variables $A, B$.  
The expansion must yield the correct coefficients.  
$AB = 10$  
$3A - 8B = -1$  
Solution $A=5, B=2$ is unique and valid.  

Final verification of arithmetic:  
$5 \times 2 = 10$.  
$3(5) - 8(2) = 15 - 16 = -1$.  
Correct.  
Answer is 12.  

If I consider negative integers:  
Let's say $A=-5, B=2$. Then $AB = -10$. This does not match $10x^2$.  
However, if we expand $(Ax-8)(Bx+3)$ with $A=-5, B=2$:  
$(-5)(2) = -10$. Incorrect.  
The expansion is $AB x^2 + (3A - 8B)x - 24$.  
This coefficient for $x^2$ must be $10$. So $AB$ must be positive? No, if $A,B$ are integers, can product be negative?  
If $A=-5, B=2$, then $AB = -10$.  
The expression is $(-10)x^2 + \dots$  
But the original expression is $10x^2$.  
So we need $AB=10$.  
Since 10 is positive, $A,B$ must have same sign.  
Or neither if product was -10? No, we are looking for $10x^2$, so $AB>0$.  
If $A,B$ were negative integers, say $(-5, -2)$, then $AB=10$ (product of absolute values) ? No $AB = (-5)(-2) = 10$.  
Let's check my previous list for signs again.  
I listed $(\pm a, \pm b)$ such that product is 10?  
If I pick pair $\{-5, -2\}$, then $A=-5, B=-2$. Then $AB=10$.  
Check eq: $3(-5) - 8(-2) = -15 + 16 = 1 \neq -1$.  
So negative integers don't satisfy the equation.  
If I pick pair $\{1, 10\}$, $A=1, B=10$, eq gives $3 - 80 = -77$. No.  
If I pick pair $\{10, 1\}$, $A=10, B=1$, eq gives $30 - 8 = 22$. No.  
If I pick pair $\{5, 2\}$, $A=5, B=2$, eq gives $15 - 16 = -1$. Yes.  
So only positive integer pair works.  

What if $B$ was negative but not a factor of 10? No, we established uniqueness of $AB$ product.  
Since $3A-8B=-1$ and $AB=10$ implies unique solution for integers (since it's linear), the negative factorials are ruled out naturally by $AB=10$.  
What about $AB = -10$? No, that would require expansion to start with $-10x^2$. The problem states expression starts with $10x^2$.  

Therefore, only $(5, 2)$ works.  
$AB+B = 10 + 2 = 12$.  

Final check. What if the factorization was $(x-8)(Ax+3)$? No, that's what I am checking for.  
Is it possible to write $10x^2 - x - 24$ as $(Ax+B)(Cx+D)$ where A,B,C,D are integers? No, must be $(Ax-8)(Bx+3)$.  

I think I've thoroughly checked this.  
Step 1: Set up equation.  
Step 2: Solve for integers $A,B$.  
Step 3: Compute required sum.  
Result: 12.  


## Answer

The problem asks us to find the values of integers $A$ and $B$ such that the expression $10x^2 - x - 24$ can be written in the form $(Ax - 8)(Bx + 3)$. We are also asked to calculate the value of $AB + B$.  

Let's expand the product on the right-hand side:  
$$ (Ax - 8)(Bx + 3) = AB x^2 + 3A x - 8Bx - 8(3) $$  
Wait, carefully expanding the constant term:  
$$ (-8) \times 3 = -24 $$  
So, the expansion is:  
$$ AB x^2 + (3A - 8B)x - 24 $$  

We are comparing this expanded polynomial with the given expression $10x^2 - x - 24$. For the two polynomials to be equal, their coefficients must match. We have three conditions for equality of coefficients:  
1.  The coefficient of $x^2$ must match.  
$$ AB = 10 $$  
2.  The coefficient of $x$ must match.  
$$ 3A - 8B = -1 $$  
3.  The constant term must match (already satisfied as it is $-24$, but we can also derive it).  

Now we need to find integers $A$ and $B$ that satisfy the system of equations:  
$$ AB = 10 $$  
$$ 3A - 8B = -1 $$  

From the first equation, we know that $AB = 10$. Since $A$ and $B$ are integers, their product is $10$. The integer pairs $(A,B)$ such that $AB=10$ are:  
*   $(5, 2)$ or  
*   $(2, 5)$ (or negative factors like $(-5,-2), (-2,-5)$ etc.)  
However, looking at the equation $3A - 8B = -1$, let's test each pair.  

**Test Case 1: $A=5$ and $B=2$**  
Equation 1: $AB = 5 \times 2 = 10$. This matches.  
Equation 2: $3(5) - 8(2) = 15 - 16 = -1$. This matches the required linear coefficient.  
This solution is valid.  

**Test Case 2: $A=2$ and $B=5$**  
Equation 1: $AB = 2 \times 5 = 10$. Matches.  
Equation 2: $3(2) - 8(5) = 6 - 40 = -34$. This does not match the required linear coefficient ($-1$).  

**Test Case 3: Negative Integers**  
Since $AB=10$, $A$ and $B$ must have the same sign to satisfy the product being positive (positive or zero). If they were both negative, say $(-5, -2)$:  
$$ AB = (-5)(-2) = 10 $$  
Check equation 2: $3(-5) - 8(-2) = -15 + 16 = 1$. This is not equal to $-1$.  
So the negative sign combinations do not work.  

Thus, the unique pair of integers $(A, B)$ satisfying the conditions is $(5, 2)$.  

We need to find $AB + B$.  
Substituting $A=5$ and $B=2$:  
$$ AB = 5 \times 2 = 10 $$  
$$ B = 2 $$  
$$ AB + B = 10 + 2 = 12 $$  

\boxed{12}  
