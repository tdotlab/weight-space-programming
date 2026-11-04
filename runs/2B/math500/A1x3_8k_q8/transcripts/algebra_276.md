# test/algebra/276.json (Algebra, level 2)

> The expression $10x^2-x-24$ can be written as $(Ax-8)(Bx+3),$ where $A$ and $B$ are integers. What is $AB + B$?  

**Correct.** Gold `12`, predicted `12`. Finish: stop, 7718 tokens, 0 waits, 621.4 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

The problem asks to express the quadratic expression $10x^2 - x - 24$ as a product of two linear factors $(Ax-8)(Bx+3)$ with integer coefficients $A$ and $B$. We need to find the value of $AB + B$.  

First, let's expand the given expression. The problem statement implies that we want to factor it in that specific form, or find A and B such that this expansion holds true.  
Let's look at the structure of the polynomial:  
$P(x) = 10x^2 - x - 24$.  

We are looking for factors $(Ax-8)(Bx+3)$ such that their product equals $P(x)$.  
Expanding the product:  
$(Ax-8)(Bx+3) = Ax(Bx) + Ax(3) - 8(Bx) - 8(3)$  
$= A B x^2 + (3A - 8B)x - 24$.  

We know that $P(x) = 10x^2 - x - 24$.  
So, we equate the coefficients of the terms in the expanded product to the coefficients in $P(x)$.  

Comparing the $x^2$ term:  
$AB = 10$.  

Comparing the $x$ term:  
$3A - 8B = -1$.  

Comparing the constant term:  
$-24 = -24$. (This is consistent).  

So we need to find integers $A$ and $B$ that satisfy the system of equations:  
1) $AB = 10$  
2) $3A - 8B = -1$  

From equation (1), the integer pairs $(A, B)$ such that $AB = 10$ are determined by the factors of 10. Since $A$ and $B$ must be integers, the possible pairs are:  
Factors of 10: $1, 10$, $-1, -10$, $2, 5$, etc.  
Since we need to check if these satisfy equation (2), let's list the integer pairs $(A, B)$ where $AB=10$.  
The possible pairs are:  
$(1, 10)$  
$(2, 5)$  
$(-1, -10)$  
$(-2, -5)$  
$(5, 2)$  
$(10, 1)$  
And possibly other negative combinations? No, $AB=10$, so both have the same sign or opposite. If both are negative, product is positive.  

Let's check each pair against equation (2): $3A - 8B = -1$.  

Case 1: $(A, B) = (1, 10)$  
$3(1) - 8(10) = 3 - 80 = -77 \neq -1$.  

Case 2: $(A, B) = (2, 5)$  
$3(2) - 8(5) = 6 - 40 = -34 \neq -1$.  

Case 3: $(A, B) = (-1, -10)$  
$3(-1) - 8(-10) = -3 + 80 = 77 \neq -1$.  

Case 4: $(A, B) = (-2, -5)$  
$3(-2) - 8(-5) = -6 + 40 = 34 \neq -1$.  

Case 5: $(A, B) = (5, 2)$  
$3(5) - 8(2) = 15 - 16 = -1$.  
This matches equation (2).  

Case 6: $(A, B) = (10, 1)$  
$3(10) - 8(1) = 30 - 8 = 22 \neq -1$.  

So the only solution for integers $A$ and $B$ is $A = 5$ and $B = 2$.  

The problem states that $10x^2-x-24$ can be written as $(Ax-8)(Bx+3)$.  
With $A=5$ and $B=2$, we have $(5x-8)(2x+3)$. Let's check if this equals the original polynomial.  
$(5x-8)(2x+3) = 10x^2 + 15x - 16x - 24 = 10x^2 - x - 24$.  
This matches exactly.  

The question asks for $AB + B$.  
We found $A=5$ and $B=2$.  
So we need to calculate $AB + B$.  
$AB + B = (5)(2) + 2 = 10 + 2 = 12$.  

Let's double check if there are other possibilities. The polynomial is monic in terms of the coefficient of x^2 being non-trivial? No, it's not monic $x^2-x-24$, it is $10x^2$.  
The factorization form is specifically given as $(Ax-8)(Bx+3)$. The coefficients A and B are fixed integers.  
Is it possible to swap the roles of x in factors? Like $(A'Bx+8)(Cx+3)$? No, the terms are explicitly $(Ax-8)$ and $(Bx+3)$. This fixes the coefficient of the constant term of each factor (up to sign). Since $(-8)(3) = -24$, this matches.  

Is it possible that A or B is negative? We checked that.  
We listed all pairs of factors for 10.  
Factors: $1, 10$. Pairs $(1,10), (10,1), (-1,-10), (-10,-1), (2,5), (5,2)$.  
Pairs product = -1? No, check linear term equation again.  
$3A - 8B = -1$.  
If $A=5, B=2 \implies 15 - 16 = -1$. Correct.  

Is it possible to have a factor like $(Ax-3)(Bx+8)$? No, the problem specifies $(Ax-8)(Bx+3)$. The constants inside the parentheses are fixed at $\pm 8$ and $3$.  

Let's check if we can interpret "integers" as possibly complex? Usually integer means $\mathbb{Z}$.  
Are there any other constraints? No.  

The solution seems unique.  
$AB = 10$, $B=2 \implies A=5$.  
$AB + B = 10 + 2 = 12$.  

Just to be absolutely sure, what if the polynomial was written in factored form differently?  
$(Ax+3)(Bx-8) = AB x^2 - 8Ax + 3Bx - 24 = ABx^2 + (3B-8A)x - 24$.  
If this were the factorization, then $AB=10$ and $3B-8A = -1$.  
Let's check if there is a solution for that.  
Pairs $(A,B)$:  
$(1, 10) \implies 30-8=22$.  
$(2, 5) \implies 15-8(-4)?$ No $3(5) - 8(2) = 15-16=-1$?  
Let's check this alternative interpretation. The problem says $(Ax-8)(Bx+3)$.  
So it is ordered as $(A x - 8)$ and $(B x + 3)$.  
My initial calculation was:  
$(Ax-8)(Bx+3) = ABx^2 + 3Ax - 8Bx - 24 = ABx^2 + (3A - 8B)x - 24$.  
$AB=10$.  
$3A - 8B = -1$.  
We solved this. $A=5, B=2$ works.  

What if I made a mistake in checking all factors?  
$A=5, B=2 \implies AB=10$, $3(5)-8(2)=15-16=-1$. Correct.  
Are there any other integer pairs for 10?  
Factors of 10: $\pm 1, \pm 2, \pm 5, \pm 10$.  
Pairs $(A,B)$ such that $AB=10$:  
(1, 10), (2, 5), (-1, -10), (-2, -5), (5, 2), (10, 1).  
Let's re-verify the other ones.  
(1, 10): $3(1) - 8(10) = -77$.  
(10, 1): $3(10) - 8(1) = 22$.  
(-1, -10): $3(-1) - 8(-10) = -3 + 80 = 77$.  
(-10, -1): $3(-10) - 8(-1) = -30 + 8 = -22$.  
(-2, -5): $3(-2) - 8(-5) = -6 + 40 = 34$.  
(2, 5): $3(2) - 8(5) = 6 - 40 = -34$.  

The only match is (5, 2).  
Thus $A=5$ and $B=2$.  
Calculate required value: $AB + B$.  
$5 \times 2 + 2 = 10 + 2 = 12$.  

Is there any ambiguity in the question?  
"The expression ... can be written as $(Ax-8)(Bx+3)$" implies existence. Since it's a polynomial with integer coefficients and leading coefficient 10 (for $x^2$), integer factorization exists. The specific forms of constants $-8$ and $+3$ are given, not just "$(kx+c_1)(mx+c_2)$". This removes any search over different constant pairs.  

Also note that the question implies uniqueness for A and B? Usually yes in such contest problems unless specified otherwise.  
And it's likely an integer arithmetic problem designed to be solved by factoring the quadratic.  

Let's do a quick factorization of $10x^2 - x - 24$ by standard trial and error (splitting the middle term or finding factors of 240 summing to -1).  
Factors of 240:  
Sum = -1.  
We need two numbers that multiply to 240 (which is $a \times b$) and add to $-1$.  
Let's assume we split the coefficient of x term. But standard method for factoring $ax^2+bx+c$ with a leading coefficient:  
$10x^2 - x - 24$. We need two numbers that multiply to $10(-24) = -240$ and add to $-1$ (the original middle term). No, we split the middle term $-x$.  
We look for factors of $240$ that sum to $-1$ (since $a=10$, signs will be flipped appropriately in method 1 or 2).  
Factors of 240:  
1, 240 -> sum large  
...  
Let's try splitting the middle term $-x$. It's easier with leading coeff 10.  
We want $(Ax - 8)(Bx + 3) = 10x^2 - x - 24$.  
$-1$ is the sum of terms coming from outer and inner products.  
$5 \times 2$ works because $3(5) - 8(2) = -1$. This corresponds to factoring $10x^2$ as $(5x)(2x)$, $-24$ as $(-8)(-3)$, or something like that?  
Let's stick to the calculation.  

The factorization of $(Ax-8)(Bx+3)$ produces $AB=10$.  
The constant term product is $-24$, which matches.  
The coefficient of $x$ depends on A and B linearly.  
Since there are only a finite number of possibilities for $A, B \in \mathbb{Z}$ given $A,B$ such that $AB=10$, we just check them.  

Step 1: Expand $(Ax-8)(Bx+3)$.  
Result: $AB x^2 + (3A - 8B)x - 24$.  
Step 2: Equate to $10x^2 - x - 24$.  
System of equations:  
$AB = 10$  
$3A - 8B = -1$  
Step 3: Solve for integers.  
From 1st, $B = 10/A$. Substitute into 2nd.  
$3A - 8(10/A) = -1$.  
Multiply by A (since A is integer non-zero, so A $\neq 0$, which holds since $AB=10$):  
$3A^2 - 80 = -A$.  
$3A^2 + A - 80 = 0$.  
This is a quadratic in A.  
Discriminant $\Delta = b^2 - 4ac = 1^2 - 4(3)(-80) = 1 + 960 = 961$.  
$\sqrt{961} = \sqrt{(30^2)^{-?}}$ No. Ends in 1, so could be 31 or 160 (unlikely for 3).  
Let's check: $31^2 = 961$. Yes, $30^2=900$, $31^2 = (30+1)^2 = 900+60+1 = 961$.  
So solutions are $A = \frac{-1 \pm 31}{2(3)}$.  
Case 1: $A = (-1 + 31) / 6 = 30/6 = 5$.  
Case 2: $A = (-1 - 31) / 6 = -32/6 = -16/3$ (not integer).  
So $A=5$ is the only solution.  
Then $B = 10/A = 10/5 = 2$.  
Check with original equation: $3(5) - 8(2) = 15 - 16 = -1$. Correct.  

Now calculate $AB + B$.  
$A = 5, B = 2$.  
$AB + B = 5 \times 2 + 2 = 10 + 2 = 12$.  

Final check of the question phrasing "A and B are integers". Yes.  
"expression ... can be written as". Implies existence.  
"What is AB+B?" asks for a single value.  
Seems solid.  

Let's quickly check if there was any trick.  
Maybe $(Ax-8)(Bx+3)$ is not unique? We proved uniqueness of A, B given the equations.  
Is it possible $A=0$? No, then constant term would be 0 or linear term 0.  
If $A=0$, $(-8)(Bx+3) = -8Bx - 24$. Not quadratic.  
So $A \neq 0$.  

Is there any ambiguity in $(Ax-8)$ vs $(-A x + 8)$? The form is explicit: $(Ax-8)$.  
If it were $(kx+c)$, we would just find factors. But the factorization is given with specific constant coefficients.  
The question effectively asks to solve for A and B.  

Is there any interpretation where $AB+B$ could be calculated differently? No, straightforward substitution.  

Let's write down the steps clearly.  
1. Expand $(Ax-8)(Bx+3)$ to get a general quadratic expression in x with integer coefficients.  
2. Match coefficients of $x^2$, $x$, and constant term with those in $10x^2-x-24$.  
3. Solve the system of linear Diophantine equations/integer constraints for A and B.  
4. Compute $AB+B$.  

Step 1:  
$(Ax-8)(Bx+3) = ABx^2 + 3Ax - 8Bx - 24 = ABx^2 + (3A - 8B)x - 24$.  

Step 2:  
$AB = 10$  
$3A - 8B = -1$  
$-24 = -24$  

Step 3:  
Integers $A, B$ with $AB=10$.  
Candidates for $(A,B)$: $(\pm 1, \pm 10), (\pm 2, \pm 5)$.  
Substitute into second equation.  
$(1, 10) \to 3 - 80 = -77 \neq -1$  
$(10, 1) \to 30 - 8 = 22 \neq -1$  
$(-1, -10) \to -3 + 80 = 77 \neq -1$  
$(-10, -1) \to -30 + 8 = -22 \neq -1$  
$(2, 5) \to 6 - 40 = -34 \neq -1$  
$(5, 2) \to 15 - 16 = -1$. Match.  
$(-2, -5) \to -6 + 40 = 34 \neq -1$.  

So $A=5, B=2$.  

Step 4:  
$AB + B = 5(2) + 2 = 10 + 2 = 12$.  

The reasoning is sound.  

Double check arithmetic one last time.  
$3A - 8B = -1$.  
If A=5, B=2. $15 - 16 = -1$. Correct.  
$AB = 10$. Correct.  
Expression: $(5x-8)(2x+3) = 10x^2 + 15x - 16x - 24 = 10x^2 - x - 24$.  
Target expression: $10x^2 - x - 24$.  
Match perfect.  

Value to find: $AB+B$.  
$AB=10$, $B=2$.  
$10+2=12$.  

Seems very straightforward. I will formulate the response based on this thought process.  

One minor point: The problem statement says "A and B are integers". It doesn't say "distinct" or non-zero, but since product is 10, they must be non-zero anyway.  
Also $Ax-8$ implies A cannot be 0? If A=0, term is -8Bx - 24 which is linear or constant depending on B, but polynomial given is quadratic. So A $\neq 0$.  
Same for B.  

Are there any complex solutions? "integers" usually restricts to real integers (which are rational) in the context of factoring polynomials over reals/complex numbers unless specified as Gaussian integers or such. But usually $AB+B$ would be different. The question is standard algebraic manipulation.  

Final check: what if $A=5, B=-2$?  
Then $(-8)(2x+3)$? No the expression is fixed $(Ax-8)(Bx+3)$.  
If $B=-2$, then product is $10x^2 + (15 - (-16))x - 24 = 10x^2 + 31x - 24 \neq P(x)$.  
What if $(Ax-8)(Bx+3)$ meant the set of factors? No, "can be written as" implies equality.  
So unique solution found.  

Is there any catch with "written as"? Sometimes factorizations are done over rational numbers like $(5x-8)(2x+3)$. Since $A,B$ are integers, we must stick to integer solutions. We did that.  
The leading coefficient is 10. If we factored as $(Ax+c)(Bx+d)$ where $c,d$ were unknown integers, there would be more variables. But here constants are fixed.  

Could it be interpreted as:  
Find A and B such that $10x^2 - x - 24 = (Ax-8)(Bx+3)$.  
Is it possible to factor out something else?  
Like $(5x-k)(2x+j)$? No, the problem states the factors have specific constants $-8$ and $+3$. It's an identity or a matching problem.  

The solution 12 seems robust.  

Let's write the response.  
Identify the equation from factoring.  
Expand RHS.  
Set up system of equations for coefficients.  
Solve for A, B.  
Compute target expression.  

Is there any other way to interpret $Ax-8$?  
Maybe $(Ax+3)$ is not a factor, but just part of the expression? No, "can be written as". It asserts equality.  

The calculation:  
$10x^2 - x - 24 = (5x-8)(2x+3)$.  
Check coefficients again.  
$x^2$: $5 \times 2 = 10$. Correct.  
$x$: $5(3) + (-8)(2) = 15 - 16 = -1$. Correct.  
Const: $-8(3) = -24$. Correct.  

Everything is consistent.  
$AB+B = (5)(2)+2 = 12$.  
If I swapped A and B, $A=2, B=5$.  
Then the expression would be $(2x-8)(5x+3)$? No, the problem says $(Ax-8)$. It's tied to $A$.  
The factor corresponding to $x$ term in product $ABx^2$ is associated with A. The constant term of first factor is -8, coeff of B.  
So it's specific assignment.  

If we had solved for $3A + 8B = 1$ or something? No, expansion yields $-24$ and middle term $3A-8B$.  
Expansion: $(Ax)(Bx) \to ABx^2$.  
$(Ax)(3) - (8)(Bx) \to (3A - 8B)x$.  
Yes.  

Okay, I'm confident.  

One hypothetical case: Could A or B be fractions? "where A and B are integers". No.  
So the constraint is tight.  
I will proceed with generating the solution.  

The final output should just be the result inside \boxed{}. But I need to provide reasoning steps as requested.  

Step-by-step derivation plan:  
1. Write down the target polynomial $P(x) = 10x^2 - x - 24$.  
2. Expand the product $(Ax-8)(Bx+3)$ using FOIL method.  
   - First: $Ax \cdot Bx = ABx^2$  
   - Outer: $Ax \cdot 3 = 3Ax$  
   - Inner: $-8 \cdot Bx = -8Bx$  
   - Last: $-8 \cdot 3 = -24$  
   - Result: $(AB)x^2 + (3A - 8B)x - 24$.  
3. Compare coefficients with $P(x)$.  
   - $AB = 10$  
   - $3A - 8B = -1$  
   - $-24 = -24$  
4. Solve the system for integers A and B.  
   - Use integer factor pairs of 10.  
   - List: $(1,10), (2,5), (-1,-10), \dots$  
   - Check $3A - 8B = -1$.  
   - Found pair $(A,B) = (5,2)$.  
5. Compute value $AB+B$.  
   - Substitute values.  
   - Result is 12.  

Looks complete.  

One check: "where A and B are integers".  
Is it possible the factorization is not unique?  
$(Ax-8)(Bx+3)$  
If I choose a different integer pair (A,B) that satisfies $AB=10$ and $3A-8B=-1$, is there another one?  
We found $3A^2+A-80=0$. The roots are integers.  
Roots of $3x^2+x-80=0$ using quadratic formula:  
$x = \frac{-1 \pm \sqrt{1 - 4(3)(-80)}}{6} = \frac{-1 \pm 31}{6}$.  
$x_1 = 5, x_2 = -32/6 = -16/3$ (not integer).  
So the pair $(A,B)$ is unique. Thus the answer is unique.  

Final Answer is 12.  

Just thinking if I missed any negative factors interpretation...  
Factors of 10 are integers dividing 10.  
If $A=5, B=2 \implies (5x-8)(2x+3)$.  
Is it possible to interpret $(Ax-8)$ as having a coefficient for $B$ inside? No.  
The coefficients are fixed by the form $(Ax-8)$ and $(Bx+3)$.  

Okay, everything seems clear.  
One small detail: Is it possible that $A=5, B=2$ leads to $10x^2 - x - 24 = (5x-8)(2x+3)$? Yes.  
Is it possible to have $(-2,-5)$ such that $(-2x+8)(-5x+3)$? No, the form is $(Ax-8)$.  
$(2x-8)$ would correspond to $A=2$.  
Check: $A=2, B=5 \implies (2x-8)(5x+3) = 10x^2 + 6x - 40x - 24 = 10x^2 - 34x - 24 \neq P(x)$.  
So the assignment is fixed.  

The solution is consistent and verified.  

Double check arithmetic: $15-16=-1$. Yes. $10+2=12$. Yes.  

Is there any ambiguity with "expression ... can be written as"?  
Usually means "equals". It could mean a factorization, but the equality holds for the specific form given.  
So yes, it's finding A and B such that the identity holds.  

Could the question imply $A$ and $B$ are real numbers? "where A and B are integers". Explicitly stated. So we restrict to $\mathbb{Z}$.  

I will formulate the response now.  

Structure:  
1. Expansion step.  
2. Coefficient matching.  
3. Solving for A, B.  
4. Final calculation.  
5. Boxed answer.  

No hidden tricks detected.  
The problem is a standard "factoring by grouping / finding factors" type.  
Given $P(x) = 10x^2 - x - 24$.  
We need to find integer $A, B$.  
Method used (system of equations or splitting middle term) is standard. Splitting the middle term method:  
$10x^2 - x - 24 = 10x^2 - 5x - 6x - 24$ ? No, that's for $x=...$.  
We split the middle term into sum of two numbers $m, n$ such that $mn = 10 \times (-24) = -240$ and $m+n = -1$.  
Factors of 240:  
1, 240 -> sum 239/... no.  
We need factors of -240 that add to -1? No, that's for $ax^2+bx+c=0$. For factorization $(x+a)(x+b)$ we need sum = b, product = a*b. For $Ax(Bx+C)$ it is more complex but equivalent.  
Let's stick to the system of equations. It was robust.  
The system yielded unique integer solution.  

Is there any other possibility?  
Maybe factors are not monic? Yes, $A=5, B=2$ gives leading term 10.  
If we used rational factorization, say $(3x - \dots)$, then A could be different? But the constraint is "integers".  
So we are safe.  

Final check of question: "What is AB + B?"  
A=5, B=2 -> $AB+B = 10+2=12$.  
If I mistakenly got A=2, B=5 (swapped). Then $AB+B = 10+5=15$. But that corresponds to $(2x-8)(5x+3)$ which is not the polynomial. The problem statement forces the order of factors relative to coefficients in the question?  
No, it says "can be written as".  
But since the set of coefficients is unique, the assignment $A$ to 5 and $B$ to 2 is forced by the equation $3A - 8B = -1$.  
Specifically, if we assumed $(Ax-8)(Bx+3)$, then:  
Coefficient of $x$ is $3A - 8B$.  
With $A=2, B=5$, coeff is $6 - 40 = -34 \neq -1$.  
So swapping them would change the resulting polynomial.  
Since the question asserts equality, we must find the correct pair $(A,B)$.  
Only $(5,2)$ works.  

Result: 12.  

One trivial check. $10x^2-x-24 = (5x-8)(2x+3)$.  
$5x \cdot 2x = 10x^2$.  
$5x \cdot 3 = 15x$.  
$-8 \cdot 2x = -16x$.  
$-8 \cdot 3 = -24$.  
Sum: $10x^2 + (15-16)x - 24 = 10x^2 - x - 24$.  
This matches perfectly.  

I'm ready.  


## Answer

The given expression is a quadratic polynomial in terms of $x$:  
$$P(x) = 10x^2 - x - 24$$  
We are asked to express this expression as the product $(Ax-8)(Bx+3)$, where $A$ and $B$ are integers.  

First, let's expand the product $(Ax-8)(Bx+3)$ using the FOIL method (First, Outer, Inner, Last):  
$$
\begin{aligned}
(Ax-8)(Bx+3) &= Ax(Bx) + Ax(3) - 8(Bx) - 8(3) \\
&= ABx^2 + 3Ax - 8Bx - 24 \\
&= ABx^2 + (3A - 8B)x - 24
\end{aligned}$$

Next, we equate the coefficients of the expanded polynomial to the coefficients of $P(x)$ to determine $A$ and $B$. We have the following system of equations:  
1.  Coefficient of $x^2$: $AB = 10$  
2.  Coefficient of $x$: $3A - 8B = -1$  
3.  Constant term: $-24 = -24$  

We need to find integer pairs $(A, B)$ that satisfy the first two equations. The factors of 10 are $\pm 1, \pm 2, \pm 5, \pm 10$. We can list the possible integer values for $A$ and check if they produce valid integers for $B$.  
From $AB = 10$, the pairs $(A, B)$ can be:  
$(1, 10), (2, 5), (-1, -10), (-2, -5), (5, 2), (10, 1)$. Note that these are all pairs where $A \cdot B = 10$.  

Now, let's test these pairs in the equation $3A - 8B = -1$:  
*   Case $(A, B) = (1, 10)$: $3(1) - 8(10) = 3 - 80 = -77 \neq -1$  
*   Case $(A, B) = (2, 5)$: $3(2) - 8(5) = 6 - 40 = -34 \neq -1$  
*   Case $(A, B) = (-1, -10)$: $3(-1) - 8(-10) = -3 + 80 = 77 \neq -1$  
*   Case $(A, B) = (-2, -5)$: $3(-2) - 8(-5) = -6 + 40 = 34 \neq -1$  
*   Case $(A, B) = (5, 2)$: $3(5) - 8(2) = 15 - 16 = -1$. This is a match.  
*   Case $(A, B) = (10, 1)$: $3(10) - 8(1) = 30 - 8 = 22 \neq -1$  

The unique solution that satisfies the condition with integer coefficients is $A = 5$ and $B = 2$. We can verify this factorization:  
$(5x-8)(2x+3) = 10x^2 + 15x - 16x - 24 = 10x^2 - x - 24$, which matches the original expression.  

We are asked to find the value of $AB + B$.  
Substituting the values we found ($A=5$ and $B=2$):  
$$AB + B = (5)(2) + 2 = 10 + 2 = 12$$  

\boxed{12}  
