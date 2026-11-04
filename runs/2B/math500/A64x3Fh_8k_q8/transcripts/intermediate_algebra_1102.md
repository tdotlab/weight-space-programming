# test/intermediate_algebra/1102.json (Intermediate Algebra, level 1)

> Find all the integer roots of  
> \[x^4 + 5x^3 + 9x^2 - x - 14 = 0.\]Enter all the integer roots, separated by commas.  

**Wrong.** Gold `-2,1`, predicted `None`. Finish: length, 8192 tokens, 3 waits, 665.3 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

The problem asks for all integer roots of the polynomial $P(x) = x^4 + 5x^3 + 9x^2 - x - 14$.  
This is a fourth-degree polynomial. By the Fundamental Theorem of Algebra, it has at most 4 complex roots. We are specifically looking for integer roots (real integers).  
Let's apply the Rational Root Theorem. If $p$ and $q$ are integers such that $p/q$ is a root, then $p|14$ and $q|1$.  
So potential integer roots must be divisors of the constant term, which is -14.  
The divisors of 14 are $\pm 1, \pm 2, \pm 7, \pm 14$.  
Thus, the possible integer roots are $1, -1, 2, -2, 7, -7, 14, -14$.  

Now I will evaluate $P(x)$ for each of these candidates.  

Case 1: $x = 1$  
$P(1) = 1^4 + 5(1)^3 + 9(1)^2 - 1 - 14$  
$P(1) = 1 + 5 + 9 - 1 - 14$  
$P(1) = 15 - 1 - 14$  
$P(1) = 14 - 14 = 0$.  
So, $x = 1$ is a root.  

Case 2: $x = -1$  
$P(-1) = (-1)^4 + 5(-1)^3 + 9(-1)^2 - (-1) - 14$  
$P(-1) = 1 + 5(-1) + 9(1) + 1 - 14$  
$P(-1) = 1 - 5 + 9 + 1 - 14$  
$P(-1) = (1+9+1) - (5+14)$  
$P(-1) = 11 - 19 = -8 \neq 0$.  
So, $x = -1$ is not a root.  

Case 3: $x = 2$  
$P(2) = 2^4 + 5(2)^3 + 9(2)^2 - 2 - 14$  
$P(2) = 16 + 5(8) + 9(4) - 2 - 14$  
$P(2) = 16 + 40 + 36 - 16$  
$P(2) = 56 + 36 - 16$  
$P(2) = 92 - 16 \neq 0$.  
Let's check the calculation again.  
$16 + 40 + 36 - 16 = (16-16) + 40 + 36 = 76 \neq 0$.  
So $x = 2$ is not a root.  

Case 4: $x = -2$  
$P(-2) = (-2)^4 + 5(-2)^3 + 9(-2)^2 - (-2) - 14$  
$P(-2) = 16 + 5(-8) + 9(4) + 2 - 14$  
$P(-2) = 16 - 40 + 36 + 2 - 14$  
$P(-2) = (16 + 36 + 2) - (40 + 14)$  
$P(-2) = 54 - 54 = 0$.  
So, $x = -2$ is a root.  

Case 5: $x = 7$  
This will be tedious to check one by one, but let's check if it works with the known roots. If we found two roots, maybe the factors help eliminate others? Or just calculate directly. Let's calculate all first or use synthetic division to narrow down candidates.  
Actually, finding *all* roots might imply factoring. Since I have found roots $x=1$ and $x=-2$, I can divide the polynomial by $(x-1)(x+2) = x^2 + 2x - 2$ or just use polynomial division repeatedly.  

Let's re-verify the calculation for $P(7)$ just in case, though we don't need to check if roots exist. If I missed something, it would be a large mistake.  
$7^4 = 2401$. $5 \cdot 7^3 = 5 \cdot 343 = 1715$. $9 \cdot 7^2 = 9 \cdot 49 = 441$.  
$P(7) = 2401 + 1715 + 441 - 7 - 14$. This is way positive. Definitely not 0.  

Case 6: $x = -7$  
$P(-7) = (-7)^4 + 5(-7)^3 + 9(-7)^2 - (-7) - 14$.  
$= 2401 + 5(-343) + 9(49) + 7 - 14$.  
$= 2401 - 1715 + 441 - 7$.  
$= (2401 - 1715) + (441 - 7)$  
$= 686 + 434 = 1120 \neq 0$.  

Case 7: $x = 14$  
$P(14)$ is clearly positive, sum of large powers. Not a root.  

Case 8: $x = -14$  
Clearly not a root.  

So the integer roots found are 1 and -2.  

Let's double check my arithmetic for $P(-2)$.  
$x^4 + 5x^3 + 9x^2 - x - 14$.  
At $x=-2$:  
$x^4 = 16$.  
$5x^3 = 5(-8) = -40$.  
$9x^2 = 9(4) = 36$.  
$-x = -(-2) = 2$.  
Sum: $16 - 40 + 36 + 2 - 14$.  
$16 + 36 + 2 = 54$.  
$-40 - 14 = -54$.  
$54 - 54 = 0$.  
Correct.  

Double check $P(1)$:  
$x^4 + 5x^3 + 9x^2 - x - 14$.  
At $x=1$:  
$1 + 5 + 9 - 1 - 14$.  
$1+5=6$.  
$6+9=15$.  
$15-1=14$.  
$14-14=0$.  
Correct.  

So the integer roots are 1 and -2.  
The question asks to find *all* integer roots. It implies there might be more, or just a list. Since degree is 4, there could be others. But rational root theorem narrows down candidates significantly, and I have checked all divisors. So no other integer roots exist.  

Just to be absolutely sure, are there any tricks? "Find all integer roots".  
Usually, if the polynomial factors nicely, we can perform synthetic division.  
We know $x=1$ is a root, so $(x-1)$ is a factor.  
Let's divide $P(x)$ by $x-1$.  
Using synthetic division:  
Coefficients: 1, 5, 9, -1, -14  
Root: 1  
Row 1: 1  
Row 2: 1+1=2  
Row 3: 2(1) = 2? No, multiply previous sum by 1.  
Coeffs: 1, 5, 9, -1, -14  

Step 1: Bring down 1.  
Step 2: Multiply by root (1): $1 \cdot 1 = 1$. Add to coeff of $x^3$: $5+1=6$.  
Step 3: Multiply by 1: $6 \cdot 1 = 6$. Add to coeff of $x^2$: $9+6=15$.  
Step 4: Multiply by 1: $15 \cdot 1 = 15$. Add to coeff of $x$: $-1+15=14$.  
Step 5: Multiply by 1: $14 \cdot 1 = 14$. Add to constant: $-14+14=0$.  

Quotient coefficients are 1, 6, 15, 14.  
So the polynomial factors as $(x-1)(x^3 + 6x^2 + 15x + 14)$.  
Now we need to find integer roots of $Q(x) = x^3 + 6x^2 + 15x + 14 = 0$.  
Again, apply Rational Root Theorem to $Q(x)$. Divisors of 14 are $\pm 1, \pm 2, \pm 7, \pm 14$.  
We already checked $x=1$ and it was the root for the original polynomial. Is it also a root of $Q(x)$?  
$P(1)=0$, so $(x-1)$ is a factor. Let's check $x=-1$ in $Q(x)$.  
$Q(-1) = -1 + 6 - 15 + 14 = (-1 - 15) + (6 + 14) = -16 + 20 = 4 \neq 0$.  
Check divisors of 14 in $Q(x)$:  
$\pm 1, \pm 2, \pm 7, \pm 14$  

Let's evaluate $Q(-2)$:  
$Q(-2) = (-2)^3 + 6(-2)^2 + 15(-2) + 14$  
$= -8 + 6(4) - 30 + 14$  
$= -8 + 24 - 30 + 14$  
$= -8 - 30 + 24 + 14$  
$= -38 + 38 = 0$.  
So $x=-2$ is a root of $Q(x)$. Thus, $(x+2)$ is a factor.  

Let's divide $Q(x)$ by $(x+2)$.  
Coefficients: 1, 6, 15, 14. Root: -2.  
Step 1: Bring down 1.  
Step 2: Multiply by -2: $1 \cdot (-2) = -2$. Add to 6: $6-2=4$.  
Step 3: Multiply by -2: $4 \cdot (-2) = -8$. Add to 15: $15-8=7$.  
Step 4: Multiply by -2: $7 \cdot (-2) = -14$. Add to 14: $14-14=0$.  

Quotient coefficients are 1, 4, 7.  
So the polynomial factors further as $(x+2)(x^2 + 4x + 7)$.  
Let's verify this factorization:  
$(x+2)(x^2 + 4x + 7) = x(x^2 + 4x + 7) + 2(x^2 + 4x + 7)$  
$= x^3 + 4x^2 + 7x + 2x^2 + 8x + 14$  
$= x^3 + 6x^2 + 15x + 14$. Correct.  

Now we need roots of $R(x) = x^2 + 4x + 7 = 0$.  
Using quadratic formula:  
$x = \frac{-4 \pm \sqrt{4^2 - 4(1)(7)}}{2}$  
$x = \frac{-4 \pm \sqrt{16 - 28}}{2}$  
$x = \frac{-4 \pm \sqrt{-12}}{2}$  
$x = \frac{-4 \pm i\sqrt{12}}{2} = \frac{-4 \pm 2i\sqrt{3}}{2} = -2 \pm i\sqrt{3}$.  

These are not integer roots. So the only integer roots of the original equation are $1$ and $-2$.  

Let's double check my initial calculation for $P(-2)$ again just to be paranoid.  
$x^4 + 5x^3 + 9x^2 - x - 14 = 0$ at $x=-2$.  
Terms:  
$(-2)^4 = 16$  
$5(-2)^3 = -40$  
$9(-2)^2 = 36$  
$-(-2) = +2$  
Constant $= -14$  
Sum: $16 - 40 + 36 + 2 - 14$.  
$16 + 36 = 52$.  
$52 + 2 = 54$.  
$-40 - 14 = -54$.  
$54 - 54 = 0$.  
This is correct.  

Check $P(1) = 1+5+9-1-14 = 15-15 = 0$. Correct.  

So the integer roots are 1 and -2.  

The format requires "Enter all the integer roots, separated by commas."  
And put final answer in \boxed{}.  

Let's do a quick check on divisors.  
Roots of $x^4+5x^3+9x^2-x-14=0$.  
Possible roots: $\pm 1, \pm 2, \pm 7, \pm 14$.  
$P(1) = 0$. Root found.  
$P(-2) = 0$. Root found.  
Divisors remaining to check: $\pm 7, \pm 14$.  
If a root exists among these, say $r$, then by RRT, $r$ divides constant term $-14$.  
Also if $(x-a)(x-b)...$ is the factorization, and we already know factors are $(x-1)$ and $(x+2)$.  
Let's check product: $(x^2 - 14x ...)$ no.  
Divisors of 14 for $x=-2$: $\pm 7, \pm 14$.  
$P(-7)$:  
$x=-7 \implies x^4=2401, 5x^3 = -1715, 9x^2=441, -x=7, -14$.  
$2401 - 1715 + 441 + 7 - 14$.  
$686 + 441 + 7 - 14 = 1127 \neq 0$.  
Also check $P(7)$:  
$x=7 \implies x^4=2401, 5x^3=1715, 9x^2=441, -x=-7, -14$.  
$2401+1715+441-7-14 = 4546 \neq 0$.  

So it seems I have exhausted the candidates.  
The roots are $1, -2$.  

Is there any ambiguity in "integer roots"? Usually implies integer domain for coefficients and values satisfying the equation. Since coefficients are integers, rational root theorem applies. Integers are integers.  
Are there multiple integer roots? Yes, distinct ones: 1, -2.  

Final check of the question phrasing "Enter all the integer roots".  
Roots found: 1, -2.  

Let's write down the steps clearly.  
1. Use Rational Root Theorem to list possible integer roots. Candidates are divisors of $-14$.  
2. Test candidates $\pm 1, \pm 2, \pm 7, \pm 14$.  
3. Calculate values for each candidate.  
   - $x=1 \implies P(1)=0$ (Root).  
   - $x=-1 \implies P(-1)=-8$ (Not root).  
   - $x=2 \implies P(2) = 16+40+36-2-14 \neq 0$.  
   - $x=-2 \implies P(-2) = 16-40+36+2-14 = 0$ (Root).  
   - $x=7, -7, 14, -14$: calculate quickly or note that product of roots is $-(-14)=14$, sum of roots is $-5$. Since we have two roots $1, -2$, their sum is $-1$. Product of remaining two roots is $P_{roots}(x)/Q(x)$? No.  
Let's look at the polynomial after factoring out $(x-1)(x+2) = x^2+x...$  
We found the quotient is $x^3 + 6x^2 + 15x + 14$.  
Roots of this cubic must be integers or non-integers.  
The integer divisors of 14 are candidates for roots of cubic.  
Check $-7$: $P( -7) \neq 0$. Check $14 \implies >0$.  
So no other integer roots in the cubic part.  

Is there a chance I made an arithmetic error in evaluating $x^2+x...$? No, division was straightforward.  
$(x-1)(x+2) = x^3 + 3x^2 - ...$? Wait.  
$(x-1)(x+2) = x^2 + 2x - x - 2 = x^2 + x - 2$.  
My division check was:  
Coeffs of $x^4$: 1. Remainder term 0.  
Synthetic div:  

```text
   1, 5, 9, -1, -14 | 1
   (1) -> 1+1=2.
   (2) -> 2*1 = 2.
```

2 + (-1) = 1? No.  
Let's re-do synthetic division carefully.  

Polynomial: $x^4 + 5x^3 + 9x^2 - x - 14$.  
Coefficients: 1, 5, 9, -1, -14.  
Root to test first (from candidates): 1.  


```text
   1 | 1   5    9   -1   -14
     |     1   6    15    14
     --------------------------
       1   6   15    14     0
```


So $Q_2(x) = x^3 + 6x^2 + 15x + 14$.  

Next root: -2.  

-2 | 1   6   15   14  
|    -2   -8   -14 (or just $-2 \cdot x$ coeffs)  

```text
     ----------------
       1   4    7    0
```


So $Q_3(x) = x^2 + 4x + 7$.  

The roots of quadratic are $(-4 \pm \sqrt{16-28})/2$. Discriminant negative. Complex roots.  
No other real integer roots.  

So the integer roots are indeed 1 and -2.  

Is there any trick with complex integers? No, standard context is real integers (Gaussian rationals). "Integer roots" implies $\mathbb{Z}$.  

Let's quickly check if $x^4 + 5x^3 + 9x^2 - x - 14$ factors into something like $(x^2+ax+b)(x^2+cx+d)$.  
We found roots 1 and -2. So factors are $(x-1)$ and $(x+2)$.  
So $P(x) = (x-1)(x+2)(Ax+B)(Cx+D)$? No, degree is 4.  
$P(x) = (x^2 + x - 2)(x^3 + ...)$ no.  
Factors are $(x-1)(x+2)$.  
We found $P(x) / ((x-1)(x+2)) = x^3 + 6x^2 + 15x + 14$.  
So $P(x) = (x-1)(x+2)(x^3 + 6x^2 + 15x + 14)$.  
Let's check the product of coefficients again.  
We have $(x^2+x-2)$ as a factor? No, $(x-1)(x+2) = x^2+x-2$.  
Is $P(x)$ divisible by $x^2+x-2$?  
$x=1 \implies 0$. $x=-2 \implies 0$. Yes.  
So we need to find if $x^3 + 6x^2 + 15x + 14$ can be factored into integers.  
We know it has integer roots only from divisors of 14.  
Candidates: $\pm 1, \pm 2, \pm 7, \pm 14$.  
We checked them: $P_3(-1) = -1 + 6 - 15 + 14 = 4$. Not 0.  
$P_3(2) = 8 + 24 + 30 + 14 > 0$.  
$P_3(-7)$?  
Actually, we already did $x=-2$ which gave root for $Q(x)$.  
Then we divided and got quadratic with no integer roots.  
So $x^3+6x^2+15x+14$ has one real root and two complex conjugate roots (since discriminant is negative).  
Is the cubic polynomial reducible over $\mathbb{Z}$? It's degree 3, so it must have a rational root or factor into $R(x)$ times linear term plus constant. But leading coeff is 1.  
So any integer root of $x^3+6x^2+15x+14$ must be an integer divisor of 14.  
We found all divisors checked are 1, -2, 7, -7. (and others like $\pm 1, \pm 2$).  
Checked:  
$x=1$: $P(1)=4$ for cubic. No.  
$x=-1$: $P(-1)=4$. No.  
$x=2$: $P(2) > 0$.  
$x=-2$: $P(-2) = -8 + 24 - 30 + 14 = 4 - 15$? No.  
Re-calculate cubic at -2:  
$x^3 = -8$.  
$6x^2 = 6(4) = 24$.  
$15x = -30$.  
Constant = 14.  
Sum: $-8 + 24 - 30 + 14 = (-8+24+14) - 30 = (29+14? no, -8-30=-38).$  
$24 + 14 = 38$. $38 - 38 = 0$.  
Yes, -2 is a root.  

We need to check the remaining integers: $\pm 7, \pm 14$.  
$P_3(7) = 343 + 6(49) + 15(7) + 14$. All positive and large. Not zero.  
$P_3(-7) = -343 + 6(49) - 105 + 14$.  
$= 294 - 448 \neq 0$.  
$P_3(14)$ huge.  
So no other integer roots.  

Therefore, the only integer roots of $P(x)=0$ are $x=1$ and $x=-2$.  

Final Answer seems to be 1 and -2.  
The order doesn't matter usually.  
The output format is comma separated.  

One more check on "Find all the integer roots".  
Could there be negative numbers? I checked -7, -14.  
Let's just re-verify signs.  
$P(x) = x^4 + 5x^3 + 9x^2 - x - 14$.  
For large positive $x$, $P(x)$ is very positive.  
For large negative $x$ ($x \to -\infty$), $x^4 \to +\infty, x^3 \to -\infty, 9x^2 \to \infty$.  
$x^4 + 5x^3 \approx x^4(1+5/x) \to +\infty$. So no root near $\pm \infty$ except possibly where sign flips.  
Let's look at end behavior: $x \to \infty, P(x) > 0$. $x \to -\infty, P(x) > 0$.  
So graph is above x-axis on the ends. Since there are roots (1 and -2), the curve must dip down to cross axis between $\pm \infty$.  
We have a local minimum or maximum between roots?  
If $x=1$ and $x=-2$ are roots, then there are roots elsewhere in complex domain.  
Between 1 and something else? No.  
Roots found: 1 and -2.  
Are there other real roots?  
We reduced the polynomial to $(x-1)(x+2)(x^2+4x+7)$.  
$x^2+4x+7 = (x+2)^2 + 3 > 0$ for all real $x$.  
So there are no real roots other than 1 and -2.  
This confirms the finding. The complex roots are -2 $\pm i\sqrt{3}$. No, discriminant was negative so no real roots from that factor.  
So exactly two real integer roots: 1 and -2.  

Final check of the question text to ensure no misinterpretation.  
"Find all the integer roots".  
Yes.  

Result is 1, -2.  
Comma separated. "1, -2". Or "-2, 1". Order is usually irrelevant but increasing order is standard or just listing them. I will write "1, -2".  

Let's quickly manually verify $x=-2$ one more time, maybe it was a calculation error on my part.  
$x = -2$.  
$x^4 = 16$.  
$5x^3 = 5(-8) = -40$.  
$9x^2 = 9(4) = 36$.  
$-x = -(-2) = +2$.  
$-14 = -14$.  
$16 - 40 = -24$.  
$-24 + 36 = 12$.  
$12 + 2 = 14$.  
$14 - 14 = 0$.  
Yes, it is zero.  

$x=1$.  
$1^4 = 1$.  
$5(1) = 5$.  
$9(1) = 9$.  
$-1 = -1$.  
$-14 = -14$.  
$1+5+9-1-14 = 15 - 15 = 0$.  
Yes, it is zero.  

Is there any other integer?  
If I check $x=-2$ and $x=1$, do I need to check others? Yes, divisors of 14 are exhaustive for integers.  
Divisors: 1, 2, 7, 14 and negatives.  
Checked all.  

Is it possible the question implies Gaussian Integers? "Integer roots" usually means $\mathbb{Z}$. If it meant Gaussian, it would specify "Gaussian integer roots" or just "roots". Also standard high school algebra context is $\mathbb{Z}$.  
If complex integers (Gaussian), $x = -2 \pm i\sqrt{3}$. The imaginary part is non-zero. So those are not integers in $\mathbb{Z}[i]$ unless they are real too? No, Gaussian integers include numbers with rational integer parts and Gaussian parts.  
But typically "integer root" means $p/q \in \mathbb{Q}$ where $q=1$ (or just $x \in \mathbb{Z}$).  
Given the wording, I assume $\mathbb{Z}$.  

Final Answer is 1, -2.  

One thought: Could there be a factor like $(x+2)^3$? No, we checked $P(-2)=0$ but $Q_2(-2) = (-8) + 6(4) + 15(-2) + 14 = -8+24-30+14 = 4 \neq 0$. So it's just a double root? No, multiplicity was 1.  
$Q_2(x) = x^3 + 6x^2 + 15x + 14$.  
$Q_3(x) = x^2 + 4x + 7$.  
The roots of $Q_3$ are distinct non-real complex conjugates.  
So multiplicity of -2 is 1 in the cubic? No, it's a simple root of the original polynomial because we divided by $(x+2)$ to get degree 3 with no remainder. Then the factorization was linear times cubic... then divide cubic by $(x-1) \implies$ cubic.  
The structure was $P(x) = (x-1)(x+2)(x^2+4x+7)$.  
So -2 is a simple root. 1 is a simple root.  
No higher multiplicity.  

Final answer: 1, -2.  
Double check prompt requirements: "Enter all the integer roots, separated by commas."  
"separated by commas" implies $r_1, r_2, ...$.  
Is there any other interpretation? No.  
Step-by-step reasoning provided in solution will show the divisors, substitution, factorization logic.  

The integer roots are 1 and -2.  

One small check: Is it possible that $x^4 + 5x^3 + 9x^2 - x - 14$ has integer roots that are not divisors?  
Rational Root Theorem says if $p/q$ is a root, then $q|a_0$ and $p|a_n$.  
Here $a_0 = -14$, $a_n = 1$.  
So any rational root must be a divisor of -14.  
Integers are divisors themselves with denominator 1.  
Divisors are $\pm 1, \pm 2, \pm 7, \pm 14$.  
We checked all of them.  
The logic holds firmly.  

Final Answer seems solid.  

Steps for output:  
1. Identify the polynomial $P(x) = x^4 + 5x^3 + 9x^2 - x - 14$.  
2. List possible integer roots as divisors of -14: $\pm 1, \pm 2, \pm 7, \pm 14$.  
3. Test each value in $P(x)$.  
   - $P(1) = 0$ (Root found).  
   - $P(-2) = 0$ (Root found).  
   - Check others or factorize to prove non-existence.  
4. Conclude integer roots are 1 and -2.  

I will write out the solution following these steps.  
I'll check the arithmetic in factorization one last time just to be safe about "completing" the reasoning.  
Divide $x^4+5x^3+9x^2-x-14$ by $(x-1)$.  
Coeffs: 1, 5, 9, -1, -14.  

```text
1 | 1, 5, 9, -1, -14
   |    1, 6, 15, 14
   ----------------
     1, 6, 15, 14, 0
```

Quotient: $x^3 + 6x^2 + 15x + 14$.  
Divide $x^3 + 6x^2 + 15x + 14$ by $(x+2)$.  

```text
-2 | 1, 6, 15, 14
   |    -2, -8, -14
   ----------------
     1, 4, 7, 0
```

Quotient: $x^2 + 4x + 7$.  
Discriminant of quadratic is $16-28 = -12 < 0$.  
So roots are complex. No other integer roots.  

The set of integer roots is {1, -2}.  
Ordering them or not does not change the set. I will list them.  

One nuance: what if one root is 7?  
$P(7) = 7^4 + 5(7^3) + 9(7^2) - 7 - 14$.  
Positive terms are huge compared to negative ones. Not a zero.  
So the list is complete.  

Final answer is \boxed{1, -2}.  
Or \boxed{-2, 1}. I'll stick with increasing order usually or just listing them. The problem doesn't specify order. "1, -2" looks fine.  

Double check prompt: "Enter all the integer roots".  
Okay.  

Recap of arithmetic for $P(-2)$:  
$x = -2$  
$x^4 = 16$  
$5x^3 = -40$  
$9x^2 = 36$  
$-x = 2$  
$-14 = -14$  
Sum: $16 - 40 + 36 + 2 - 14$.  
Positive sum: $16 + 36 + 2 = 54$.  
Negative sum: $-40 - 14 = -54$.  
Result 0. Correct.  

Recap of arithmetic for $P(1)$:  
$x = 1$  
Sum is $1+5+9-1-14 = 15-15 = 0$. Correct.  

Seems robust.  

Is there any hidden trick? Like "integer roots" might imply rational roots where denominator divides coefficient...  
No, for polynomials with integer coefficients, rational roots are in lowest terms $p/q$ where $p|constant$, $q|leading$. If it is an integer, $q=1$. So candidates are just divisors of constant.  
Unless there's a specific domain like $\mathbb{Z}[i]$, but "integer roots" implies $x \in \mathbb{Z}$.  

Ready to generate response.  

One final check on the sign of $-14$.  
$x^4 + 5x^3 + 9x^2 - x - 14$.  
Constant term is -14.  
Roots product (for 4 roots) = 14.  
$(1)(-2)(r_3)(r_4) = -2 r_3 r_4$. So $-2(-2)$? No.  
$(x-a)(x-b)...$ constant term is product of signs times leading coeff if $x^4 + ...$.  
$a_0 / \text{lc} = (-14)/1 = -14$.  
Product of roots $= (-1)^4 (-14) = 14$. No.  
If roots are $r_1, r_2, r_3, r_4$.  
$r_1+r_2+r_3+r_4 = -5/1 = -5$.  
$r_1 r_2 r_3 r_4 = (-1)^4 (-14)  

## Answer

*(none: the token cap hit during thinking)*
