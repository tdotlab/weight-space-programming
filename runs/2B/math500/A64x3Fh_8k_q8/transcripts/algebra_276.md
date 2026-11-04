# test/algebra/276.json (Algebra, level 2)

> The expression $10x^2-x-24$ can be written as $(Ax-8)(Bx+3),$ where $A$ and $B$ are integers. What is $AB + B$?  

**Correct.** Gold `12`, predicted `12`. Finish: stop, 7975 tokens, 0 waits, 643.3 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

The problem asks to express the quadratic expression $10x^2 - x - 24$ as a product of two linear factors in the form $(Ax-8)(Bx+3)$ where $A$ and $B$ are integers.  
We need to find the values of $A$ and $B$, and then calculate $AB + B$.  

Step 1: Compare coefficients.  
Let's assume $10x^2 - x - 24 = (Ax-8)(Bx+3)$.  

Expand the right-hand side:  
$(Ax-8)(Bx+3) = A \cdot B \cdot x \cdot x + A \cdot 3 \cdot x - 8 \cdot B \cdot x - 8 \cdot 3$  
$= ABx^2 + 3Ax - 8Bx - 24$  
$= ABx^2 + (3A - 8B)x - 24$  

Now, equate the coefficients of $x^2$, $x$, and the constant term from the expanded polynomial with the original expression.  

Coefficient of $x^2$:  
$AB = 10$  

Coefficient of $x$:  
$3A - 8B = -1$  

Constant term:  
$-24 = -24$ (Matches)  

Step 2: Solve for integer solutions $(A, B)$.  
We have a system of equations:  
1) $AB = 10$  
2) $3A - 8B = -1$  

Since $A$ and $B$ are integers, the factors of 10 must be considered. The pairs of integers $(A, B)$ that multiply to 10 are:  
$(1, 10), (2, 5), (-1, -10), (-2, -5), (5, 2), (10, 1), (-5, -2), (-10, -1)$.  

Let's test these pairs to see which one satisfies the linear equation $3A - 8B = -1$.  

Case 1: $A=1, B=10$  
$3(1) - 8(10) = 3 - 80 = -77 \neq -1$  

Case 2: $A=-10, B=-1$  
$3(-10) - 8(-1) = -30 + 8 = -22 \neq -1$  

Case 3: $A=-5, B=2$  
$3(-5) - 8(2) = -15 - 16 = -31 \neq -1$  

Case 4: $A=2, B=5$  
$3(2) - 8(5) = 6 - 40 = -34 \neq -1$  

Case 5: $A=1, B=10$ (already done)  
Let's check pairs $(A,B)$ where order matters. The equation is $AB=10$.  
Factors of 10 are $\pm 1, \pm 2, \pm 5, \pm 10$.  
Pairs:  
$(1, 10) \implies -77$  
$(2, 5) \implies 6-40 = -34$  
$(5, 2) \implies 15-16 = -1$ -> Found it.  
Let's verify. $3(5) - 8(2) = 15 - 16 = -1$. Yes.  
$(10, 1) \implies 30-8 = 22$  
$(-1, -10) \implies -3 - (-80) = 77$  
$(-2, -5) \implies -6 - (-40) = 34$  
$(-5, -2) \implies -15 - (-16) = 1$  

So the only valid solution seems to be $A=5$ and $B=2$.  

Step 3: Verify if there are other possibilities.  
We solved it by guessing factors of 10. Is there any ambiguity?  
Let's look at the discriminant or the factorization directly without assuming integer coefficients initially, just for verification.  
The quadratic is $10x^2 - x - 24$. We want to split the middle term: $-x$ into terms that sum to $-x$ when multiplied by 10. Or find two factors of $10 \times (-24) = -240$ that add to $-1$.  
Factors of -240:  
$24 \times 10$, $12 \times 20$, etc.  
Since the coefficient of $x^2$ is 10, the factors must come from $(10, -24)$ product. No, sum must be $-1$.  
We are splitting $-x = ax + bx$ into two terms $px$ and $qx$? No, we rewrite the expression as $(Ax+B)(Cx+D)$. But here it's $(Ax-8)(Bx+3)$. The first factor is $(Ax-8)$ so the constant term is $-24 = (-8)(Bx)$ no, $(Ax-8)(Bx+3)$ yields $-24$.  
Let's check if the constant term matches. $(-8)(3) = -24$. Correct.  

So we just need $A$ and $B$ such that $(Ax-8)(Bx+3) = 10x^2 - x - 24$.  
$(AB)x^2 + (3A - 8B)x - 24 = 10x^2 - x - 24$.  
We established $AB=10$ and $3A - 8B = -1$.  

Let's recheck the factors of 10.  
Factors: $(\pm 1, \pm 10), (\pm 2, \pm 5), (\pm 5, \pm 2), (\pm 10, \pm 1)$.  
Pairs satisfying $3A - 8B = -1$:  
1. $A=5, B=2 \implies 3(5) - 8(2) = 15 - 16 = -1$. Matches.  
Are there any others?  
Maybe I missed one?  
Let's systematically check:  
$A \in \{1, 2, 5, 10\}$.  
If $A=1$: $3 - 8B = -1 \implies 8B = 4 \implies B = 1/2$. Not integer.  
If $A=-1$: $-3 - 8B = -1 \implies 8B = -2 \implies B = -1/4$.  
If $A=2$: $6 - 8B = -1 \implies 8B = 7$. Not integer.  
If $A=-2$: $-6 - 8B = -1 \implies 8B = -5$.  
If $A=5$: $15 - 8B = -1 \implies 8B = 16 \implies B = 2$. Integer.  
If $A=-5$: $-15 - 8B = -1 \implies 8B = -14 \implies B = -17/8$.  
If $A=10$: $30 - 8B = -1 \implies 8B = 31$.  
If $A=-10$: $-30 - 8B = -1 \implies 8B = -29$.  

So indeed, the unique solution in integers is $A=5$ and $B=2$.  

Step 4: Calculate the required value.  
The question asks for $AB + B$.  
Substitute $A=5$ and $B=2$.  
$AB + B = (5)(2) + 2$  
$10 + 2 = 12$.  

Let's double check if $B$ and $A$ could be swapped in the question phrasing.  
The expression is $(Ax-8)(Bx+3)$. The constant term of this product is $-24$, which matches.  
If we swapped them, say $(Ax-8)(Bx+3)$ vs $(Ax+B)x^2$ ... no, that's not what it says.  
It specifies the form. $A$ multiplies $x$, $B$ multiplies $x$. So $AB=x^2$ term.  
And constant is $-8 \times 3 = -24$.  
Coefficient of $x$ is $3A - 8B$.  

Is it possible that the order of terms in $(Ax-8)$ matters? It says $(Ax-8)$, so $-8$ is subtracted.  
Is it possible that $(Ax+B)(Cx+D)$ was meant but with specific constants given? No, the form is fixed. "where A and B are integers".  

Let's check if $A$ could be negative or $B$ could be negative such that $AB=10$.  
We checked pairs where $A$ and $B$ have same sign for product 10.  
$(1, 10) \to -77$  
$(-1, -10) \to 24$ No. $3(-1)-8(-10) = -3+80=77$.  
$(2, 5) \to -34$.  
$(-2, -5) \to 34$.  
$(5, 2) \to -1$.  
$(-5, -2) \to 1$.  

What if $A$ and $B$ are not integers? "where A and B are integers". So no.  
The calculation seems robust.  

Let's re-read carefully: "The expression ... can be written as $(Ax-8)(Bx+3)$ ... What is $AB + B$?"  
My result: $A=5, B=2$.  
$AB + B = 5 \cdot 2 + 2 = 12$.  

Let's do a sanity check.  
$(5x-8)(2x+3) = 10x^2 + 15x - 16x - 24 = 10x^2 - x - 24$.  
Matches the original expression exactly.  
$A=5$, $B=2$. Both are integers.  

Alternative interpretation:  
Could the question imply that there might be a sign error in my logic?  
Maybe $(Ax-8)(Bx+3)$ isn't the only way to factor it?  
The problem says "can be written as". Since polynomials factor uniquely into linear factors over $\mathbb{Q}$ (and thus integers since leading coeff is positive and factors are unique), the solution should be unique.  

Is it possible $AB+x$ refers to something else? No, "AB + B" is clear.  
Just need to ensure I didn't swap A and B in a way that changes the value.  
If $A=5, B=2$, then $AB=10$, $B=2$. $AB+B = 12$.  
If I swapped them, would it be possible?  
Suppose we had $(Ax-8)(Bx+3)$ where the roles were assigned differently. But $A$ is explicitly associated with $x$ in the first term $(Ax-8)$ and $B$ is associated with $x$ in the second term.  
If I found that $A=2$ and $B=5$ worked, then I would calculate $AB+B = 10+5 = 15$.  
But I found that $(2,5)$ yields $-34$, not $-1$. The equation is $3A - 8B = -1$.  
So for $(A,B)=(2,5)$, LHS is $6-40 = -34 \neq -1$. So this case is invalid.  
For $(A,B)=(5,2)$, LHS is $15-16 = -1$. Correct.  
Is there any other pair? No.  

Are there constraints I missed? "integers". Yes checked.  
Calculation check again:  
$10x^2 - x - 24$  
Factor pairs of 240 (since $a/c \times b/d = ...$ no, product is $-24 \times 10 = -240$).  
Splitting constant term into two factors.  
Factors of $10(-24) = -240$.  
$+35$? No, $x$ term needs to be $-1x$.  
Let's try splitting middle term for $10x^2 - x - 24$.  
We need numbers $p, q$ such that $pq = -240$ and $p+q = -1$.  
This doesn't seem easier since product is large.  
Use the factors of the leading coefficient to find roots?  
Roots by Quadratic Formula: $x = \frac{-(-1) \pm \sqrt{1 - 4(10)(-24)}}{2(10)} = \frac{1 \pm \sqrt{1 + 960}}{20} = \frac{1 \pm \sqrt{961}}{20}$.  
$31^2 = 961$. Yes.  
So roots are $\frac{1 \pm 31}{20}$.  
Root 1: $x_1 = \frac{32}{20} = \frac{8}{5}$.  
Root 2: $x_2 = \frac{-30}{20} = -\frac{3}{2} = -1.5$.  
So factors are $(x - x_1)(x - x_2) = (x - \frac{8}{5})(x + \frac{3}{2})$.  
$= (x - \frac{8}{5}) \frac{2x+3}{2} = \frac{1}{2} (2x- \frac{8}{5})(2x+3)$... No.  
$(5x - 8)(2x + 3)$.  
Let's check this one more time.  
$(5x - 8)(2x + 3) = 10x^2 + 15x - 16x - 24 = 10x^2 - x - 24$.  
Yes, it works perfectly.  
So the factors are $5x-8$ and $2x+3$.  
This corresponds to $Ax-8$ where $A=5$ and $Bx+3$ where $B=2$.  
Or $Ax+8$? No, expression is $10x^2 - x - 24$, so we have $(Ax-8)$ because constant term in expansion of $(Ax-8)(\dots)$ must be $-24$.  
$(A)x \cdot (B) + (-8)(3)$ -> no. $(Ax)(Bx) + (Ax)(3) + (-8)(Bx) + (-8)(3) = ABx^2 + 3Ax - 8Bx - 24$.  
Constant term is $-24$, which comes from $-8 \times 3$. So this part is fixed.  
We need coefficient of $x$ to be $3A - 8B = -1$.  
Also coefficient of $x^2$ to be $AB = 10$.  

So $A=5, B=2$ is the unique solution where $Ax-8$ has constant term $-8$.  
Could it be that the factorization was meant to be $(Ax+3)(Bx-8)$?  
The question states: $(Ax-8)(Bx+3)$.  
So the terms are explicitly identified.  
If we assumed roots were $x = 8/5$ and $x = -3/2$, then factors are proportional to $(5x-8)$ and $(2x+3)$.  
This confirms the structure $(Ax-8)(Bx+3)$ matches exactly with $A=5, B=2$.  

Let's verify calculation of $AB + B$.  
$A=5, B=2$.  
$AB = 10$.  
$B = 2$.  
Sum = 12.  

Is there any trick with "integers"?  
If we had complex numbers, roots could be complex, but here coefficients are real integers, so rational roots theorem guarantees existence of rational roots which lead to factorization over rationals. Since $5x-8$ and $2x+3$ have integer coeffs, it's consistent.  

Could there be another way to split -1?  
Maybe $(Ax-8)(Bx+3)$ allows for scaling factors?  
No, the form is exact polynomial equality. The coefficients must match exactly.  
$10x^2$ implies $AB=10$.  
$-24$ implies $-8 \times 3 = -24$. This part is already fixed by the constants in the binomial expansion.  
The only "degrees of freedom" is A and B.  
So the derivation holds.  

Let's double check arithmetic.  
$AB=10$  
$3A - 8B = -1$  
Substitute $B = 10/A$ into second eq:  
$3A - 8(10/A) = -1$  
Multiply by A:  
$3A^2 - 80 = -A$  
$3A^2 + A - 80 = 0$  
Solve quadratic for A.  
Discriminant $\Delta = b^2 - 4ac = 1^2 - 4(3)(-80) = 1 + 960 = 961$.  
$\sqrt{961} = 31$.  
$A = \frac{-1 \pm 31}{2(3)} = \frac{-1 \pm 31}{6}$.  
Case 1: $A = \frac{30}{6} = 5$.  
If $A=5$, then $B = 10/5 = 2$.  
Case 2: $A = \frac{-32}{6} = -\frac{16}{3}$, not an integer.  

So the only integer solution is $A=5, B=2$.  
Check again for calculation errors in $3(5) - 8(2) = 15-16=-1$. Correct.  
Check constant term: $(-8)(3)=-24$. Correct.  
Everything holds up.  

Final calculation requested: $AB + B$.  
$5 \times 2 + 2 = 10 + 2 = 12$.  

Is there any ambiguity about which variable is A and which is B?  
"($Ax-8)(Bx+3)$". The first parenthesis multiplies $A$, the second by $B$.  
It would be weird to have $A$ and $B$ swapped.  
What if the order was $(Bx+3)(Ax-8)$? That's commutative multiplication of polynomials, but usually "as (f)(g)" implies the first factor is determined by x coefficient A and constant -8. But actually, since multiplication is commutative, it doesn't matter mathematically, unless we interpret $A$ and $B$ as coefficients in a specific sequence or just labels.  
The question asks for "AB + B".  
If we found $A=2, B=5$, then $AB+B = 10+5=15$.  
But we must check if there is an assignment of A and B such that it works.  
We found a solution set $\{A, B\} = \{5, 2\}$.  
Since $A$ must be in the term with coefficient -8 (which has constant term from $x \times 3$? No).  
Let's look at terms again:  
$(Ax-8)$ -> Constant is -8.  
$(Bx+3)$ -> Constant is 3.  
If we swap them to say $(Bx+3)(Ax-8)$, it is the same polynomial.  
However, the coefficient of x in the expansion comes from $A \times 3$ and $B \times (-8)$.  
The coefficient of $x^2$ comes from $AB$.  
So regardless of which factor is written first, we have two equations relating A and B to the coefficients:  
1. Product of leading coeffs: $AB = 10$.  
2. Sum of "middle" coeff contributions: $3A - 8B = -1$.  

This assumes the polynomial form $(Ax-8)(Bx+3)$ is fixed as written. The question asks for AB+B where A and B are integers corresponding to these positions.  
Since we solved for specific values $A$ and $B$, they are uniquely determined by the system of equations derived from coefficient matching.  
The solution was unique. So no ambiguity there.  

Just to be extremely pedantic, could $A$ and $B$ be swapped in the factor pairs?  
Suppose $A=2, B=5$.  
Then $(2x-8)(5x+3) = 10x^2 + 6x - 40x - 24 = 10x^2 - 34x - 24 \neq 10x^2-x-24$.  
Suppose $A=5, B=2$.  
$(5x-8)(2x+3) = 10x^2 + 15x - 16x - 24 = 10x^2 - x - 24$.  
So A must be 5 and B must be 2.  

What if $A$ is negative?  
We checked that. No integer solution.  

What if $B$ is negative?  
We checked all sign combinations for AB=10.  
Only (5, 2) works.  

Is it possible $AB+x^2$ is not the term in question but $x(Ax+B)$? No, "expression ... written as ...". The form is given.  

The question seems straightforward. I will proceed with confidence.  

Final Answer Check:  
$10x^2 - x - 24 = (5x-8)(2x+3)$.  
$A=5, B=2$.  
$AB+B = 10+2 = 12$.  
Looks correct.  

Are there any edge cases?  
Is it possible that $A$ and $B$ are not coprime? No constraint on them other than being integers.  
The derivation doesn't require them to be prime or anything.  

One tiny check: "where A and B are integers". This implies we should look for integer solutions. I found one.  
If complex numbers were allowed, there would be infinite? No, $3A-8B=-1$ and $AB=10$ is a system of non-linear equations but linear in terms of unknowns if expressed carefully. It reduces to two cases for B. But since $AB=10$, $B$ must be a factor of 10, which are integers anyway.  
So integer constraint makes it a finite set to check, and we found one solution.  

Is there any other interpretation?  
Maybe $(A)(x-8)$? No, $(Ax-8)$.  
Maybe $(ax+b)$? No, form is specific.  
The logic seems solid.  

Let's do a quick mental check on the discriminant method again to be absolutely sure about roots.  
$x = \frac{1 \pm 31}{20}$.  
Factors are $(x - 8/5)(x + 3/2)$.  
Multiply by $20/20$: $\frac{1}{4}(16x - \dots)$? No.  
$(5x-8)(2x+3)$ gives $(5 \cdot 2 x^2) + (15 - 16)x - 24 = 10x^2 - x - 24$. Correct.  

Another thought: The problem asks for $AB+B$. If I had swapped $A$ and $B$, it would be different. But since the structure $(Ax-8)$ binds A to the first term, we can't swap them unless we change the definition of A.  
If we have two unknowns A, B, and we solved the system for unique values, there's no swapping choice.  

Final check on calculation steps:  
$AB = 10$  
$3A - 8B = -1$  
From $3A - 8B = -1 \implies 3A = 8B - 1 \implies A = (8B-1)/3$.  
Substitute into product:  
$B \cdot \frac{8B-1}{3} = 10$  
$B(8B-1) = 30$  
$8B^2 - B - 30 = 0$  
Use quadratic formula for B.  
$\Delta = (-1)^2 - 4(8)(-30) = 1 + 960 = 961$.  
$\sqrt{961} = 31$.  
$B = \frac{1 \pm 31}{16}$.  
Case 1: $B = (32)/16 = 2$.  
Then $A = (8(2)-1)/3 = 15/3 = 5$.  
Case 2: $B = (-30)/16 = -15/8$ (not integer).  
So the only integer solution is $B=2, A=5$.  
This confirms previous findings and was a more direct path.  

Question asks for $AB+B$.  
$A=5, B=2$.  
$5(2) + 2 = 10 + 2 = 12$.  

The steps are clear.  
1. Expand the given factored form.  
2. Equate coefficients.  
3. Solve the system of equations for integers A and B.  
4. Compute AB+B.  

Step 1: $(Ax-8)(Bx+3) = ABx^2 + (3A-8B)x - 24$.  
Step 2: $AB=10$, $3A-8B=-1$, $-24=-24$.  
Step 3: System solution yields $A=5, B=2$.  
Step 4: $12$.  

Is there any possibility that $x$ is a variable and we are doing polynomial factorization over reals? Yes, "integers" ensures rationality.  
If complex factors were allowed, could it be $(Ax-8)(Bx+3)$ with non-integers A or B?  
We solved for integer B and A using the system. The solution is unique.  

Final Answer seems to be 12.  

Just to double check if I misread any sign.  
"10x^2 \- x - 24"  
"(Ax-8)(Bx+3)"  
Product is $10x^2 + 3Ax - 8Bx - 24$.  
Matches signs:  
$+10x^2$ -> OK  
$-x$ -> $3A - 8B = -1$ -> Correct.  
$-24$ -> $(-8)(3) = -24$ -> Correct.  

If it was $(Ax+8)(Bx+3)$? Then constant is $24$. Not match.  
If it was $(Ax-3)(Bx+8)$? Constant $-24$.  
$(Ax-8)(Bx+3)$ -> matches the given constants explicitly.  
So no trick there.  

The question asks for $AB + B$.  
$A=5, B=2$.  
$10 + 2 = 12$.  

Everything seems consistent.  

Let's write down the solution steps clearly.  
Define the polynomial $P(x) = 10x^2 - x - 24$.  
Factorization form $Q(x) = (Ax-8)(Bx+3)$.  
Expand $Q(x)$:  
$ABx^2 + 3Ax - 8Bx - 24 = ABx^2 + (3A - 8B)x - 24$.  
Match coefficients:  
1. $AB = 10$  
2. $3A - 8B = -1$  

Solve for integers A, B.  
Since $A, B \in \mathbb{Z}$, we can iterate through factors of 10 or substitute one into the other.  
Substitute $B = 10/A$.  
$3A - 8(10/A) = -1$  
Multiply by A:  
$3A^2 - 80 = -A$  
$3A^2 + A - 80 = 0$  
Roots are $\frac{-1 \pm \sqrt{1 + 960}}{6} = \frac{-1 \pm 31}{6}$.  
$A_1 = 5, A_2 = -16/3$.  
Since A must be an integer, $A = 5$.  
Then $B = 10/5 = 2$.  

Check: $(5x-8)(2x+3) = 10x^2 + 15x - 16x - 24 = 10x^2 - x - 24$. Correct.  
Compute $AB + B$:  
$5(2) + 2 = 12$.  

Seems flawless.  

One check on the question wording: "The expression ... can be written as ...". It implies it must be factorable this way or at least that specific form yields the correct expression. Since it does yield the expression, and A,B integers, we proceed.  
If there were multiple ways to write it as $(Ax-8)(Bx+3)$?  
The problem states "can be written as", which might imply a solution set. But usually in these contests, the form is unique for integer coefficients or the question implies finding the specific A and B that satisfy the conditions given. Since we found a unique pair of integers (5, 2) satisfying the condition, there's no ambiguity about "another way". Even if $A$ or $B$ could be scaled? No, the constants are fixed in -8 and +3.  
If we had $(kAx - 8)$... no, it says $(Ax-8)$. So A is a scalar factor of x.  

Final check on arithmetic:  
$16 \times 1 = 16$, $960 + 1 = 961$. $\sqrt{961} = 31$. Correct.  
$(-1)^2 - 4(3)(-80) = 1 + 960 = 961$. Correct.  

The logic holds up. I'm ready to write the response.  
One detail: "put your final answer within \boxed{}".  
So just the number 12.  

Double check the arithmetic of $3A^2+A-80=0$.  
$(5)(x-8)(...)$? No, factorization of quadratic equation.  
Factors of -240 that sum to -3? No.  
Equation: $3A^2 + A - 80 = 0$.  
If $A=5$: $3(25) + 5 - 80 = 75 + 5 - 80 = 80 - 80 = 0$. Correct.  

So I'm confident in 12.  


## Answer

To find the value of $AB + B$, we need to determine the integer values of $A$ and $B$ such that the expression $(Ax-8)(Bx+3)$ equals $10x^2 - x - 24$.  

First, expand the product on the right side:  
$$ (Ax-8)(Bx+3) = A \cdot B \cdot x^2 + A \cdot 3 \cdot x - 8 \cdot B \cdot x - 8 \cdot 3 $$  
$$ (Ax-8)(Bx+3) = ABx^2 + 3Ax - 8Bx - 24 $$  
$$ (Ax-8)(Bx+3) = ABx^2 + (3A - 8B)x - 24 $$  

We equate this expanded form to the given expression $10x^2 - x - 24$ by matching the coefficients of corresponding terms:  
1.  The coefficient of $x^2$: $AB = 10$  
2.  The coefficient of $x$: $3A - 8B = -1$  

We need to find integer values for $A$ and $B$. From the first equation, $B = \frac{10}{A}$. Since $B$ is an integer, $A$ must be a factor of 10. The possible factors of 10 are $\pm 1, \pm 2, \pm 5, \pm 10$.  

Let's test each case or use substitution to solve the system:  
Substitute $B = \frac{10}{A}$ into the second equation:  
$$ 3A - 8\left(\frac{10}{A}\right) = -1 $$  
Multiply the entire equation by $A$ (assuming $A \neq 0$, which is true since $AB=10$):  
$$ 3A^2 - 80 = -A $$  
Rearrange into a quadratic equation:  
$$ 3A^2 + A - 80 = 0 $$  

We can solve for $A$ using the quadratic formula or by inspection.  
By inspection, we check factors of the constant term -80 that might satisfy the equation. Or simply solve:  
$$ \Delta = b^2 - 4ac = (1)^2 - 4(3)(-80) = 1 + 960 = 961 $$  
The discriminant is $961$, and $\sqrt{961} = 31$.  
$$ A = \frac{-1 \pm 31}{2(3)} = \frac{-1 \pm 31}{6} $$  

This gives two possible values for $A$:  
1.  $A = \frac{-1 + 31}{6} = \frac{30}{6} = 5$  
2.  $A = \frac{-1 - 31}{6} = \frac{-32}{6}$ (This is not an integer)  

Since $A$ must be an integer, we take $A = 5$.  
Now find $B$:  
$$ B = \frac{10}{A} = \frac{10}{5} = 2 $$  

We should verify the solution in the second equation:  
$$ 3(5) - 8(2) = 15 - 16 = -1 $$  
This matches the required coefficient. The pair of integers is $A=5$ and $B=2$.  

Finally, we calculate the required value $AB + B$:  
$$ AB + B = (5)(2) + 2 = 10 + 2 = 12 $$  

Alternatively, we could substitute $A=5, B=2$ into $(Ax-8)(Bx+3)$:  
$(5x - 8)(2x + 3) = 10x^2 + 15x - 16x - 24 = 10x^2 - x - 24$, which is correct.  

The value of $AB + B$ is 12.  

\boxed{12}  
