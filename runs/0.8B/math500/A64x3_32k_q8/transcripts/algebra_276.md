# test/algebra/276.json (Algebra, level 2)

> The expression $10x^2-x-24$ can be written as $(Ax-8)(Bx+3),$ where $A$ and $B$ are integers. What is $AB + B$?  

**Correct.** Gold `12`, predicted `12`. Finish: stop, 13739 tokens, 2 waits, 838.3 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

The problem asks to find the values of integers $A$ and $B$ such that the expression $10x^2 - x - 24$ can be factored into the form $(Ax-8)(Bx+3)$. Finally, I need to calculate $AB + B$.  

First, let's analyze the equation for factors.  
The quadratic factorization is:  
$$10x^2 - x - 24 = (Ax - 8)(Bx + 3)$$  

This gives us:  
$A x \cdot (Ax - 8)$ ? No, $(Ax-8)$ is a linear term in terms of $x$. $(Bx+3)$ is another.  
Expanding the RHS:  
$(Ax - 8)(Bx + 3) = A(Bx^2) + A(3x) + (-8)(Bx) + (-8)(3)$.  
$= ABx^2 + 3A x - 8Bx - 24$.  

Comparing this to the original expression $10x^2 - x - 24$, we can equate the coefficients.  
The coefficient of $x^2$ must match:  
$AB = 10$  

The constant term (coefficient of $x^0$) must be checked against $3 \cdot (-8)$? No, this is wrong. The constant term comes from multiplying terms with powers of $x$ that sum up to degree -1 or something. Let's recheck the product.  
$(Ax-8)(Bx+3)$ expands to $ABx^2 + 3A x - 8Bx - 24$.  
Comparing with $10x^2 - x - 24$:  

1. The term $10x^2$ comes from $ABx^2$. So, $AB = 10$.  
2. The constant term is $-24$. In the expansion:  
$(Ax)(3) + (-8)(Bx) + (-8)(3)$? No.  
Term by term:  
$A x \cdot B x = ABx^2$  
$A x \cdot 3 = 3A x$  
$(-8) \cdot B x = -8B x$  
$(-8) \cdot (-8)?$ No, constant term from multiplication is product of constants. $(-8)(3) = -24$.  

So the expression becomes:  
$ABx^2 + (3A - 8B)x - 24$.  

The original expression is $10x^2 - x - 24$.  
Matching coefficients with powers of $x$:  
1. $AB = 10$  
   2. Coefficient of $x$: $3A - 8B = -1$ (because the term is $-x$, i.e., $-x = -1x$, so $3A - 8B = -1$)  

Let's solve for integers $A$ and $B$.  
From $AB=10$, the possible integer pairs $(A, B)$ are factors of 10:  
$(-5, -2), (-2, -5), (1, 10), (2, 5), (5, 2), (-1, -10), (-10, -1) \dots$  
And we also have positive/negative pairs depending on the signs. However, usually $A$ and $B$ are positive integers or maybe they are just integers. Let's find all integer pairs with product 10:  
$(\pm 1, \pm 10), (\pm 2, \pm 5), (\pm 5, \pm 2)$.  

Let's substitute these into the equation for $x$ coefficient:  
Case 1: $A = 1, B = 10$. Then $3(1) - 8(10) = 3 - 80 = -77 \neq -1$.  
Case 2: $A = 2, B = 5$. Then $3(2) - 8(5) = 6 - 40 = -34 \neq -1$.  
Case 3: $A = 5, B = 2$. Then $3(5) - 8(2) = 15 - 16 = -1$. This is a match!  
So we have a candidate pair $(A, B) = (5, 2)$ or $(B, A)$.  
However, let's check the other factor. Usually factors are integers. We can also swap signs in $A$ and $B$.  
Let's consider $A = -10, B = -1$. Then $AB = 10$. $3(-10) - 8(-1) = -30 + 8 = -22 \neq -1$.  
Or let's check negative factors. If the original expression is factored over integers, usually the leading coefficients match, or if not specified "positive", they could be either. But let's see if there are other integer solutions.  
What about $A=-5, B=-2$? $AB=10$. Coefficient of $x$: $3(-5) - 8(-2) = -15 + 16 = 1 \neq -1$.  

So far only $(5, 2)$ seems to work for the $x$ term.  
Let's check the factorization again. The problem states $(Ax-8)(Bx+3)$.  
The constant terms are fixed at -8 and +3 respectively.  
The expansion was:  
$(A x - 8)(B x + 3) = AB x^2 + (3A - 8B) x - 24$.  
We need $3A - 8B = -1$ and $AB = 10$.  

Wait, did I make a mistake in the constant term expansion?  
$(Ax - 8)(Bx + 3) = A(Bx^2) + A(3x) + (-8)(Bx) + (-8)(3)$  
$= AB x^2 + 3A x - 8B x - 24$.  
Yes, correct.  

So we need $AB = 10$ and $3A - 8B = -1$.  
Since $AB = 10$, let's list the possibilities for $(A, B)$:  
Pairs of integers multiplying to 10.  
1) $A = 1, B = 10 \implies 3(1) - 8(10) = 3 - 80 = -77$. No.  
2) $A = 2, B = 5 \implies 3(2) - 8(5) = 6 - 40 = -34$. No.  
3) $A = 3$ is not a factor (no integer factor 1).  
4) $A = 5, B = 2 \implies 3(5) - 8(2) = 15 - 16 = -1$. YES.  
Here $A=5, B=2$.  
5) $A = -2, B = -5 \implies 3(-2) - 8(-5) = -6 + 40 = 34$. No.  
6) $A = -1, B = -10 \implies 3(-1) - 8(-10) = -3 + 80 = 77$. No.  
7) $A = -5, B = -2 \implies 3(-5) - 8(-2) = -15 + 16 = 1$. No.  

So the only solution is $(A, B) = (5, 2)$ or maybe $(B, A)$?  
Let's check if there are other possibilities. What about negative factors?  
The product $AB$ must be 10. Since 10 is positive, either both are positive or one is positive and one is negative. But for $x^2$, it's coefficient of $x^2$. If we swap signs, i.e., use negative terms inside the parenthesis, does that change?  
The problem says $(Ax-8)(Bx+3)$. The structure is fixed.  
So we need $A$ and $B$ such that $AB=10$ and $3A - 8B = -1$.  
As analyzed above:  
Case 1: $A=5, B=2 \implies AB=10$. $3(5) - 8(2) = 15-16=-1$. Correct.  
So $A=5$ and $B=2$ or $A=2$ and $B=5$? Let's check signs again.  
If we use $(5, 2)$: $AB = 10$, so $Ax^2 - Bx \dots$ no.  
$(5x-8)(2x+3)$.  
Coefficient of $x^2$: $5(2) = 10$. Matches original.  
Coefficient of $x$: $3(5) - 8(2) = 15 - 16 = -1$. Matches original (-x term).  
Constant: $(-8)(3) = -24$. Matches.  

Is there any other pair?  
What about $A=-10, B=-1$? $AB=10$. $3(-10) - 8(-1) = -30 + 8 = -22 \neq -1$.  
What about $A=10, B=1$? $3(10) - 8(1) = 24 \neq -1$.  

Are there any factors of 10? Yes: $\pm 1, \pm 2, \pm 5, \pm 10$.  
And signs. Let's systematically check all factor pairs $(A, B)$ such that $AB=10$.  
If $A$ is negative: $B = -20/A^{\dots}$. No, since product is 10.  
Factors are $\pm 1, \pm 2, \pm 5, \pm 10$.  
For a pair to multiply to 10: $(1, 10), (2, 5), (5, 2), (10, 1)$ or $(-1, -10), (-2, -5), (-5, -2)$.  
Let's list them with the equation for coefficient of $x$: $3A - 8B = -1$.  
Pairs $(A, B)$:  
1. $(1, 10): 3(1) - 8(10) = 3 - 80 = -77$ (No)  
2. $(2, 5): 3(2) - 8(5) = 6 - 40 = -34$ (No)  
3. $(5, 2): 3(5) - 8(2) = 15 - 16 = -1$ (Yes)  
Here $A=5, B=2$.  
Or maybe signs are mixed? What about $(-5, -2)$? No, product is positive.  
$(-5, -2): 3(-5) - 8(-2) = -15 + 16 = 1$ (No)  
4. $(10, 1): 3(10) - 8(1) = 24 - 8 = 16$ (No).  

So the only pair is $(A, B) = (5, 2)$.  
Thus $A = 5$ and $B = 2$.  
Is this correct? Let me double check if I missed any interpretation.  
"can be written as $(Ax-8)(Bx+3)$".  
The variables are distinct. No ambiguity about "integers" vs "positive integers". The question just asks for integers $A$ and $B$.  
However, sometimes factorization problems imply positive coefficients or something specific to the domain (polynomials). But since it's $10x^2$, and usually such problems come from algebra textbooks.  

If I assumed the factors must be of form $(Ax+c)(Bx+d)$ and we have to ensure integer coefficients. Here $A=5, B=2$.  
Let's try to verify if there are any subtle constraints on $A$ or $B$.  
Could it be that the coefficient of $x^2$ is not 10? No, I derived $AB=10$ directly from comparing coefficients of $x^2$. That seems robust.  

But is it possible that I misinterpreted the question? "can be written as $(Ax-8)(Bx+3)$".  
This means the quadratic $f(x) = 10x^2 - x - 24$ must factor into linear terms with integer coefficients.  
We found a solution: $5x - 8$ and $2x + 3$.  
Check product: $(5x-8)(2x+3)$.  
$x \cdot (2x) = 2x^2$. No, coefficient of $x^2$ should be 10.  
I used the factorization as if it expanded to $ABx^2 + \dots$ but I wrote $(Ax-8)(Bx+3)$ in my first thought step and then calculated expansion for example $A=5, B=2$.  
The product of coefficients would be $AB$.  
Let's re-evaluate the factorization.  
$(Ax - 8) = 5x - 8$.  
$(Bx + 3) = 2x + 3$.  
Product: $(5x - 8)(2x + 3)$.  
$= 5x(2x + 3) - 8(2x + 3)$  
$= 10x^2 + 15x - 16x - 24$  
$= 10x^2 + (15-16)x - 24$  
$= 10x^2 - x - 24$.  
It works!  

So $A = 5, B = 2$.  
Then what is $AB + B$?  
$AB = 5(2) = 10$.  
$B = 2$.  
$AB + B = 10 + 2 = 12$.  

Is there any other possibility? Maybe the question allows negative integers.  
If I swap the positions in the factors, say $A=-8/B$ and something else. No, that's just a permutation.  
Let's check if $(Ax-8)(Bx+3)$ could mean something else? No, standard factorization notation.  

Could the coefficients be $A, B$ such that:  
$(5x + 2)(4x - 8) \dots$ No, constant is fixed at -8 and 3.  
What if it was $(Ax - 8)(Bx + 1)$? Then $3A = -1$ etc. No, the problem says $(Bx+3)$. So I am right.  

Let me check for any other integers $A, B$.  
Maybe factors of 24 are relevant to the constant term if there was a typo in my thought process about $AB=10$.  
The original expression is $10x^2 - x - 24$.  
If $AB = 10$, then $AB$ must be an integer.  
The product of factors for quadratic with leading coefficient $A'B'$ must be consistent with expansion.  

Let's check other integer pairs $(A,B)$ where $AB=10$:  
Factors: $\pm 5, \pm 2, \pm 1, \pm 10$.  
Pairs are $(A,B) = (5,2), (5,-2), (-5,2), (-5,-2)$ etc.  
Let's check the $x$ term again. $3A - 8B = -1$.  
This requires $AB$ to be consistent with the solution.  
If we check pairs where signs are different?  
Pairs of $(A,B)$:  
1. $(1, 10): 3(1) - 8(10) = -77$  
2. $(5, 2): 3(5) - 8(2) = -1$ (Works)  
3. $(-5, 2): 3(-5) - 8(2) = -15 - 16 = -31$  
4. $(-5, -2): 3(-5) - 8(-2) = -15 + 16 = 1$  
5. $(10, 1): 3(10) - 8(1) = 16$ (No)  

So it seems only $A=5, B=2$ satisfies the condition with integer coefficients.  
The value to find is $AB + B$.  
With $A=5, B=2$:  
$AB = 10$.  
$B = 2$.  
$AB + B = 12$.  

Let me think if there's any tricky interpretation like "can be written as (Ax-8)(Bx+3)" implies specific structure for A and B.  
Could $A$ or $B$ be fractions? No, problem says integers.  
Could it be that I copied the question wrong? No, $10x^2 - x - 24$.  

Is there any possibility where $Ax-8$ is not equal to a multiple of 5 and something?  
If I check for factors of $(Ax+8)$ or similar? No.  

What if the constant term in expansion was different?  
$(Ax-8)(Bx+3) = AB x^2 + (3A - 8B)x - 24$.  
Is it possible to get $AB = 10$ but I missed a factor that works for coefficient of $x$?  
Maybe $AB=10$ is not necessary.  
Suppose $(Ax-8)(Bx+3)$ represents the factors, but maybe they are coefficients of something else? No, that's impossible.  
What if $A$ and $B$ depend on the constant term of the polynomial divided by something? No.  

Let me just check if $A$ or $B$ could be negative in such a way to fix the sign?  
If $A=-5, B=2$, then $AB = -10$. That doesn't match leading coefficient 10 unless it's $-(-5x+8)(2x-3)$ etc. But the problem gives specific coefficients for linear terms: $Ax-8$ and $Bx+3$. This is a standard form where the quadratic leads to $AB$. So we must check the condition.  
Leading coefficient of $10x^2$ means $A \cdot B x^2 = 10x^2$, so $AB=10$.  

So, if $A=5, B=2$:  
$(5x-8)(2x+3) = 10x^2 - x - 24$.  
Check constant term: $(-8)(3) = -24$. Correct.  
Check linear coeff: $3(5) - 8(2) = 15 - 16 = -1$. Correct.  
So it works perfectly.  

Now, could the answer be different?  
Let me double check the question statement again.  
"The expression ... can be written as (Ax-8)(Bx+3), where A and B are integers."  
"What is AB + B?"  
If I pick $A=-5, B=2$:  
$(-5x-8)(2x+3)$? No, the problem writes $(Ax-8)$. So $A=5$ gives $-8$. If $A=-5$, it's $-8$ too.  
So if we want product to be correct for $Ax^2$:  
We need $AB = 10$.  
Since $AB$ must be positive (product of two factors of the form $(kx-8)(l x + 3)$), we have $(A,B) \in \{ (5,2), (-5,-2), (2,-5), (-2,5) \}$ based on absolute values. But we need the signs in the equation to make $AB$ match.  
If $A=5, B=2$, then $Ax-8 = 5x-8$. This gives positive coeff for x.  
If $A=-5, B=2$, then $Ax-8 = -5x-8$. This is wrong sign? No. The factorization $(Ax-8)(Bx+3)$ requires $Ax$ term to be $Ax$ and $Bx$ term. If I write the equation as:  
$f(x) = (A x - 8)(B x + 3)$, we get $AB x^2 + \dots$  
We need $AB=10$.  

So my finding of $A=5, B=2$ or $(-5,-2)$ is correct. The signs inside the parentheses matter for the coefficients. Since $Ax-8$ has coefficient 5 (positive) and $Bx+3$ has coefficient 2 (positive), then $(5x-8)(2x+3)$ works. If we used negative values, e.g., $A=-5$, it would be $-5x - 8$. Then the product is $(-5x-8)(2x+3) = -(5x+8)(2x+3)$. But $(Ax-8)$ must equal $-(5x+8)$? No.  
Let's just stick to the calculation.  

The problem asks for $AB + B$.  
If I found only one solution, then it is unique.  
However, if there were multiple solutions for $AB+B$, usually the problem statement implies specific conditions that might yield more than one set of factors.  
Is it possible that $A$ and $B$ are swapped? The problem says $Ax-8$. It doesn't explicitly say "where A and B are distinct". However, if $A=2, B=-5$ gives $AB = -10$. Then product would be $(-5x+3)(2x-8)$ maybe?  
Let's check if $(2x-8)(Ax+3)$ or similar could work. No, the structure is fixed as written in the prompt. It writes $(Ax-8)(Bx+3)$. So I should just solve for $A$ and $B$.  
If there were another pair of factors that worked with integer coefficients for $Ax-8$, then there would be more solutions. But mathematically, if $AB=10$, the pairs are limited. The equation $3A - 8B = -1$ has only one solution set where A and B satisfy the coefficient constraint (in integers).  

However, I need to check if $A$ and $B$ are uniquely determined or if they could be any pair satisfying $AB=10$ and $3A-8B=-1$.  
Let's solve again properly.  
$A(Bx^2) + \dots = 10 x^2$.  
We want $(Ax - 8)(Bx + 3) = AB x^2 + (-24) \cdot (3A/2?)$ No.  
The expansion is: $AB x^2 + 3A x - 8B x - 24$.  
Comparing coefficients:  
1. $AB = 10$  
2. $3A - 8B = -1$  
We found $(5,2)$. This gives $A=5, B=2$.  
Are there other pairs?  
What about $(A, B)$ where $A$ or $B$ could be non-integers? No, problem says integers.  
So we are done.  

Let's double check the question wording again to ensure I haven't missed something subtle like "factors are (Ax-8)(Bx+3) such that A, B are integers". Or maybe factors of 24?  
Maybe there is a factorization involving $(4x - 8)$? No.  

Let's try to verify the arithmetic again.  
Original: $10x^2 - x - 24$.  
Try $(5x - 8)(2x + 3)$.  
$5 \times 2 = 10$. Correct.  
$x(3) + 8(-1)x$? No, linear terms in multiplication are just summing the coefficients of $x$.  
Linear term coefficient:  
$A x (-8)$ is $-8 A x$.  
$B x (+3)$ is $3 B x$.  
Total linear term is $3A - 8B$.  
We need this to be $-1$.  
$3(5) - 8(2) = 15 - 16 = -1$. Correct.  

So the solution $A=5, B=2$ is correct.  
Calculate $AB + B = 10 + 2 = 12$.  

Could there be other solutions?  
What if I check all factor pairs of 24 for constant term? No.  
Maybe I missed a negative factor pair that satisfies the equation $3A - 8B = -1$ with $AB=10$.  
Since product is positive, we need either $(+,+) \implies 3a-8b=-1$.  
$( -,+)$ or $(-,-)$.  
Case: $A=-1, B=-10$: $3(-1) - 8(-10) = -3 + 80 = 77 \neq -1$.  
Case: $A=2, B=5$: $6-40 = -34$.  
Case: $A=-2, B=-5$: $6+40 = 46$. No.  
Case: $A=-5, B=2$: $-15-16 = -31$. No.  
Case: $A=1, B=10$: $3-80 = -77$. No.  
Case: $A=10, B=1$: $30-8 = 22$.  
Case: $A=-5, B=-2$: $15+6 = 21$. No.  
Case: $A=2, B=5$ was wrong earlier.  

What about factors of -10? $(-10, -1)$. $3(-10) - 8(-1) = -22$.  
What about factors of -24? No, it's not an equation.  

Is it possible that I can swap the terms in the factorization?  
$(Ax-8)(Bx+3)$ is equivalent to $(Ax-8)$ and $(Bx+3)$.  
Since the problem asks for "can be written as (Ax-8)(Bx+3)", this implies there are specific integers A and B. It's likely a system of equations that has a unique solution or one valid pair.  

Is it possible that $A$ and $B$ are not just values but factors themselves?  
Like $(Ax - 8) = x \dots$. No.  

Let me verify the expansion for any other pair again.  
Maybe I missed a sign on the constant term?  
If we have $10x^2 - x - 24$.  
Is it possible that $Bx+3$ has coefficient +3 but A is something else?  
What if $(Ax-8)$ and $(Bx+3)$ are factors of $x=1$?  
$(A-B) + \dots$ No.  

Could it be that $A$ and $B$ are not unique?  
Let's check for factor pairs again.  
Maybe there's an error in my expansion check.  
Let's write $(A-5)(B-2)$. This is getting confused with the variable names or structure.  
The problem is clear: find A, B such that $10x^2 - x - 24 = (Ax-8)(Bx+3)$ for integers A and B.  
I've solved this system: $AB=10$ and $3A-8B=-1$.  
Solution found: $(5, 2)$.  
Are there any other factors of 10?  
Factors of 10 are 1, 2, 5, 10.  
Powers of -1, 2, 5, 10 are $(-1), (-2), (-5), (5) \dots$ and their products match.  
Since product is 10.  
$(A,B)$ pairs:  
1. $(1, 10)$  
2. $(2, 5)$  
3. $(5, 2)$  
4. $(10, 1)$  
5. $(-1, -10)$  
6. $(-2, -5)$  
7. $(-5, -2)$  
8. $(-1, -10)$  
9. $(-1, 10)$ (No)  
10. $(-10, -1)$ (No)  

Let's check the $3A - 8B$ condition on each pair.  
1. $3(1) - 8(10) = 3 - 80 = -77$. No.  
2. $3(2) - 8(5) = 6 - 40 = -34$. No.  
3. $3(5) - 8(2) = 15 - 16 = -1$. YES.  
Pairs with solution: $(5, 2)$ and permutations if signs were different?  
Since we need integers A and B for the equation to hold. The factorization form requires A and B to be the coefficients in front of x in both terms.  
If we used $A = -2$ (leading coeff) but then sign was negative: $(-2x-8)(5x+3)$? No, $B$ would have to be 5. Then we get $(Ax-8)(Bx+3)$ with $x^2$ term $AB=10$.  
But in the expression $Ax-8$, if A is -5 and B is 2, we get $(-5x-8)(2x+3) = -10x^2 + \dots$ which is not our polynomial.  
The coefficient of $x^2$ must be positive 10 (or at least the sign matches).  
For $(Ax-8)(Bx+3)$ to produce $10x^2$, we need $AB = 10$.  
With pairs:  
$(5, 2) \implies AB=10$. Coeffs match.  
$(-5, -2) \implies AB=10$. If A=-5 and B=-2: $Ax-8 = -5x-8$. Product is $(A)(B)x^2 + (-8)(3)$? No.  
Let's re-verify the product expansion for $(A,B) = (-5, -2)$.  
$Ax-8$: $(-5x)-8$.  
$Bx+3$: $(-2x)+3$.  
Product: $(-5x)(-2x) + (-5x)(3) + (-8)(-2x) + (-8)(3)$  
$= 10x^2 - 15x + 16x - 24$  
$= 10x^2 + x - 24$.  
This is wrong. We need $10x^2 - x - 24$. So signs of the linear coefficients must match.  
In $(Ax-8)(Bx+3)$, coefficient of x is $A(3) + B(-8)$? No.  
Let's write carefully:  
$(A x - 8)(B x + 3) = A(B)x^2 + A(3)x + (-8)(B)x + (-8)(3)$  
$= ABx^2 + (3A - 8B)x - 24$.  

We need $AB=10$ and $3A-8B = -1$.  
For $(5, 2)$:  
$AB = 10$.  
$3(5) - 8(2) = 15 - 16 = -1$. Matches.  

For $(-5, -2)$:  
$AB = (-5)(-2) = 10$.  
$3(-5) - 8(-2) = -15 + 16 = 1$. Fails.  

What about negative factors?  
For $(A, B)$ pairs with product -10? No, leading coeff is 10 positive. So we need both A and B to be such that $AB=10$?  
If the coefficient of $x^2$ in $(Ax-8)(Bx+3)$ is $AB$.  
For it to be $10$, $A$ and $B$ must multiply to 10. Since $A, B \in \mathbb{Z}$, possible pairs are:  
1) $(5, 2)$ -> product 10.  
   2) $(-5, -2)$ -> product 10.  
   3) $(2, 5)$ -> product 10.  
   4) $(-2, 5)$ -> product -10.  
So $AB=10$ requires pairs like $(\pm 5, \pm 2)$.  

Let's check the expansion for $(A, B) = (-5, 2)$?  
If A=-5 and B=2:  
Coeff of x^2 is -10. We want +10. So no.  
Coeff of x term? $3(-5) - 8(2) = -1$. Matches! But coeff of x^2 must be 10.  

What about A=2 and B=-5?  
Coeff of x^2 is -10. No, we need +10.  
If we assume coefficients can be swapped in the factors (i.e. the question might mean $(Bx-8)$ or something). But it says $(Ax-8)(Bx+3)$.  

So only positive integer solution works for $AB=10$.  
And we found $(5, 2)$ is a valid solution.  
Thus $A=5$ and $B=2$.  

Let me consider if I can write the expression as $(Ax-8)(Bx+3)$ where $A$ or $B$ could be non-integers. But the problem specifies integers. So my derivation holds.  

Is there any ambiguity in "AB + B"?  
Maybe it asks for $AB+B$. Or something else? Just sum.  

Let's check if there is an alternative factorization involving rational numbers, but since A and B are integers.  
Also, check if the constant term could be adjusted? No.  
Check if I missed any pair.  
Factors of 10: $\{1, 2, 5, 10\}$ and $\{-1, -2, -5, -10\}$.  
Product pairs with coeff $3x$ (which is $-x$ in original).  
Equation: $3A - 8B = -1$.  
Since $AB=10$, we just list pairs and check $3A-8B=-1$.  

Powers of 2: $\{1, 2\}$?  
$A \in \{\pm 1, \pm 2\}$. No.  
If $A=1$, $B=10$. $3 - 80 = -77$.  
If $A=2$, $B=5$. $6 - 40 = -34$.  

*Continued in [part 2 of 2](algebra_276_p2.md): GitHub stops rendering math on pages this long, so the transcript is split.*
