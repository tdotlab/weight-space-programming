# test/intermediate_algebra/1102.json (Intermediate Algebra, level 1)

> Find all the integer roots of  
> \[x^4 + 5x^3 + 9x^2 - x - 14 = 0.\]Enter all the integer roots, separated by commas.  

**Wrong.** Gold `-2,1`, predicted `None`. Finish: length, 8192 tokens, 7 waits, 660.9 s.

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
Let's check calculation again.  
$16+40=56$, $56+36=92$.  
$92 - 16 = 76 \neq 0$.  
So, $x = 2$ is not a root.  

Case 4: $x = -2$  
$P(-2) = (-2)^4 + 5(-2)^3 + 9(-2)^2 - (-2) - 14$  
$P(-2) = 16 + 5(-8) + 9(4) + 2 - 14$  
$P(-2) = 16 - 40 + 36 + 2 - 14$  
Let's group terms:  
Positives: $16, 36, 2 \rightarrow 54$.  
Negatives: $-40, -14 \rightarrow -54$.  
$P(-2) = 54 - 54 = 0$.  
So, $x = -2$ is a root.  

Case 5: $x = 7$  
$P(7) = 7^4 + 5(7)^3 + 9(7)^2 - 7 - 14$  
$7^2 = 49$, $7^3 = 343$, $7^4 = 2401$.  
$P(7) = 2401 + 5(343) + 9(49) - 21$  
$5 \times 343 = 1715$  
$9 \times 49 = 441$  
$P(7) = 2401 + 1715 + 441 - 21$  
Let's estimate: $2400 + 1700 + 400 = 4500$. Positive. So definitely not a root?  
Let's re-evaluate the condition. We found integer roots are candidates from divisors of 14.  
$x=7$ yields a large positive sum, minus 21, so it is very likely positive. Let me check again.  
$2401 > 21 - 1715$. Yes. $P(7)$ is clearly not zero.  

Case 6: $x = -7$  
$P(-7) = (-7)^4 + 5(-7)^3 + 9(-7)^2 - (-7) - 14$  
Positives: $7^4 + 9 \cdot 7^2 + 7 = 2401 + 9(49) + 7 = 2401 + 441 + 7 = 2849$.  
Negatives: $-5(-343)$ is positive in this expansion? No, formula is $\sum x^k a_k$ with signs.  
$x^4$: $+2401$  
$5x^3$: $5(-7)^3 = -1715$  
$9x^2$: $9(49) = 441$  
$-x$: $-(-7) = +7$  
$-14$: $-14$  
Sum: $2401 - 1715 + 441 + 7 - 14$  
Calculation:  
$2401 - 1715 = 686$  
$441 + 7 = 448$  
$P(-7) = 686 + 448 - 14 = 1134 - 14 = 1120 \neq 0$.  

Case 7: $x = 14$ (Just checking divisors, though likely not needed given the magnitude)  
The sum will be dominated by $14^4 = 38416$, so it is positive. Definitely not a root.  

So far, we have found two roots: $1$ and $-2$.  
Let me double check the arithmetic for the roots found.  

Polynomial: $P(x) = x^4 + 5x^3 + 9x^2 - x - 14$.  
Roots are integers, so candidates are $\pm 1, \pm 2, \pm 7, \pm 14$.  

$P(1) = 1 + 5 + 9 - 1 - 14 = 0$. Correct.  
Since $x=1$ is a root, $(x-1)$ is a factor.  

$P(-2) = 16 - 40 + 36 + 2 - 14 = 0$. Correct.  
Since $x=-2$ is a root, $(x+2)$ is a factor.  

The problem asks for all integer roots. It's possible there are other integer roots that I missed or there might be duplicate roots (but distinct values are asked).  
I should check if these are the only ones.  
Since I found two roots $1$ and $-2$, I can perform polynomial division to reduce the polynomial to a quadratic factor.  
Divide $x^4 + 5x^3 + 9x^2 - x - 14$ by $(x-1)$.  

Using synthetic division or polynomial long division:  
$$ \begin{array}{c|rrrrr}
1 & 1 & 5 & 9 & -1 & -14 \\
  & \downarrow & 1 & 6 & 15 & 14 \\
\hline
  & 1 & 6 & 15 & 14 & 0
\end{array} $$
So, $P(x) = (x-1)(x^3 + 6x^2 + 15x + 14)$.  

Now I need to find roots of the cubic factor $Q(x) = x^3 + 6x^2 + 15x + 14$.  
The candidates for integer roots are divisors of $14$ again. So $\pm 1, \pm 2, \pm 7, \pm 14$.  
Let's test them in $Q(x)$.  
Note that we found $x=1$ is a root of the original polynomial. Since $(x-1)$ is a factor, it divides out completely? No, $P(x)= (x-1)Q(x)$. If there are multiple roots at 1, then the multiplicity would be higher.  
$P(1)=0$ and $Q(1) = 1 + 6 + 15 + 14 \neq 0$. So $1$ is a simple root.  

Let's check $Q(x)$ values for small integers.  
$x= -2$:  
$(-2)^3 + 6(-2)^2 + 15(-2) + 14$  
$= -8 + 6(4) - 30 + 14$  
$= -8 + 24 - 30 + 14$  
$= 16 - 30 + 14 = -14 + 14 = 0$.  
So $x=-2$ is also a root of $Q(x)$. This means $(x+2)$ is a factor.  
Let me check if I missed something. In the earlier check for $P(-2)$, it was 0. Here checking $Q(-2)$ is 0.  
Let's divide $Q(x)$ by $(x+2)$.  
Synthetic division with root $-2$:  
$$ \begin{array}{c|rrr}
-2 & 1 & 6 & 15 & 14 \\
   & \downarrow & -2 & -8 & -14 \\
\hline
   & 1 & 4 & 7 & 0
\end{array} $$
So $Q(x) = (x+2)(x^2 + 4x + 7)$.  

Now check the quadratic factor: $R(x) = x^2 + 4x + 7$.  
Completing the square or checking discriminant.  
Discriminant $\Delta = b^2 - 4ac = 4^2 - 4(1)(7) = 16 - 28 = -12$.  
Since the discriminant is negative, there are no real roots for $R(x)$, let alone integer roots.  
Also, coefficients of $x^3 + 6x^2 + 15x + 14$ sum to $1+6+15+14 = 36 \neq -1$. Product is $-1$ (constant term).  
Let's re-verify the factorization.  

Original polynomial: $P(x) = x^4 + 5x^3 + 9x^2 - x - 14$.  
Factors found: $(x-1)$ and $(x+2)$.  
Product of these factors:  
$(x-1)(x+2) = x^2 + x - 2$. This is degree 2. We need to multiply by the remaining quadratic.  
Let's do the division step carefully again to ensure no arithmetic errors.  

$P(x) / (x-1)$:  
Coefficients: $1, 5, 9, -1, -14$.  
Row 1: $1 \quad 5 \quad 9 \quad -1 \quad -14$  
Row 2 (multiplied):  
$x=1 \times 1 = 1$  
$x=5 \to x^3$: coefficient is $5+1=6$  
Next term: $x^3 + 6x^2$.  
Bring down $9$. Next coeff.  
Multiply $9$ by $1$: $9$.  
Add to 1 (from previous line, $x^2$ term was $9$, so coeff is $9$).  
Let's trace carefully.  
Coefficients $a_4=1, a_3=5, a_2=9, a_1=-1, a_0=-14$.  
$P(x) = x^4 + 5x^3 + 9x^2 - x - 14$.  
Div by $x-1$.  
$1 \cdot x^3$ term.  
$1(5)x^3$? No.  
Synthetic:  

```text
   | 1   5    9   -1   -14
   |     1    6    15    14
   -----------------------
   | 1   6   15   14      0
```

Quotient is $x^3 + 6x^2 + 15x + 14$.  

Now factor $x^3 + 6x^2 + 15x + 14$.  
Possible rational roots are $\pm 1, \pm 2, \pm 7, \pm 14$.  
Try $x=-2$:  
$(-2)^3 + 6(-2)^2 + 15(-2) + 14$  
$= -8 + 6(4) - 30 + 14$  
$= -8 + 24 - 30 + 14$  
$= -8 - 30 = -38$.  
$-38 + 38 = 0$.  
So $x=-2$ is a root. Correct.  

Synthetic division by -2:  

```text
   | 1    6     15    14
   |      -2   -8    14
   ---------------------
   | 1   4     7      0
```

Quotient is $x^2 + 4x + 7$.  

So the factorization is $P(x) = (x-1)(x+2)(x^2 + 4x + 7)$.  

Since the quadratic factor is $x^2 + 4x + 7$, and $\Delta = 16 - 28 = -12 < 0$, it has no real roots.  
Thus, the only integer roots of $P(x)$ are the integer roots found from the factors with real coefficients.  
The roots are $1$ and $-2$.  

Are there any other possibilities?  
Is it possible I missed a root in my manual check of divisors earlier?  
Divisors were $\pm 1, \pm 2, \pm 7, \pm 14$.  
I checked:  
1 -> Yes.  
-1 -> No (-8).  
2 -> No (92-16 = 76, not 0) - Let's recheck $x=2$ one more time.  
$P(2) = 16 + 5(8) + 9(4) - 2 - 14 = 16 + 40 + 36 - 16 = 76$. Correct, not 0.  
-2 -> Yes (checked before).  
7 -> No.  
-7 -> No.  
14 -> No.  

Is it possible that the discriminant of $x^2 + 4x + 7$ is a mistake?  
$x^2 + 4x + 7$.  
$b^2 - 4ac = 4^2 - 4(1)(7) = 16 - 28 = -12$. Correct.  
Discriminant must be positive for real roots, so no roots at all (complex). Thus no integer roots from it.  

So the only integer roots are $1$ and $-2$.  
The question asks to enter all the integer roots separated by commas.  
The set is $\{1, -2\}$.  
Usually sorted? Or just listed? The prompt doesn't specify order. I will list them as found or in ascending order. $-2, 1$ or $1, -2$. Standard convention often sorts them but lists can be flexible unless specified "increasing order". Let's provide both or just the set.  
Actually, usually answers are sorted. Let's put them in increasing order: $-2, 1$.  

Let me double check the problem statement.  
"Find all the integer roots" - plural implies there could be more than one.  
"x^4 \+ 5x^3 + 9x^2 - x - 14 = 0".  

Wait, I should check $x=-7$ and $x=7$ again just to be absolutely sure.  
$P(7) = 7^4 + 5(7)^3 + 9(7)^2 - 7 - 14$.  
All terms positive except maybe the constant and $-x$. No, all coeffs are mostly positive.  
$7^4 = 2401 > 0$.  
$5 \times 343 = 1715 > 0$.  
$9 \times 49 = 441 > 0$.  
$-7 < 0$.  
$-14 < 0$.  
Sum: $2401 + 1715 + 441 - 21$.  
Clearly positive. Not zero.  

What if I made a mistake in the factorization?  
$(x-1)(x+2)(x^2+4x+7) = (x^2+x-2)(x^2+4x+7)$  
Expand:  
$= x^2(x^2+4x+7) + x(x^2+4x+7) - 2(x^2+4x+7)$  
$= x^4 + 4x^3 + 7x^2 + x^3 + 4x^2 + 7x - 2x^2 - 8x - 14$  
$= x^4 + (4+1)x^3 + (7+4-2)x^2 + (7-8)x - 14$  
$= x^4 + 5x^3 + 9x^2 - x - 14$.  
The expansion matches the original polynomial perfectly.  
So the factorization is correct.  
And since $x^2+4x+7$ has no real roots, there are no other real roots.  

So the integer roots are just $\{-2, 1\}$.  

Let's write down the steps clearly.  
1. Identify potential integer roots using Rational Root Theorem: divisors of 14.  
2. Test candidates: $x=1$ works.  
3. Factor out $(x-1)$ to get cubic polynomial.  
4. Find next integer root candidates from divisors of remaining constant term (which is now -7? No, after dividing by linear term, the new constant term comes from the remainder or original).  
Original: $x^4 + 5x^3 + 9x^2 - x - 14$.  
Factors found so far: $(x-1)$.  
Remaining factor is cubic with constant term 14.  
Candidates for next integer root are $\pm 1, \pm 2, \pm 7, \pm 14$.  
Checked $x=2$ (failed), $x=-2$ (worked).  
5. Factor out $(x+2)$ from cubic to get quadratic factor.  
6. Analyze remaining quadratic for integer roots. $\Delta < 0$.  
7. Conclude all integer roots are 1 and -2.  

Let me re-verify the calculation for $P(2)$.  
$2^4 = 16$.  
$5 \times 2^3 = 5 \times 8 = 40$.  
$9 \times 2^2 = 9 \times 4 = 36$.  
$2^0$ coeff? No, term is $-x$. So $-2$.  
Term is constant $-14$.  
Sum: $16 + 40 + 36 - 2 - 14$.  
$16+40=56$.  
$56+36=92$.  
$92-2=90$.  
$90-14=76$.  
Calculation is solid.  

Let me re-verify the calculation for $P(-1)$.  
$x=-1$.  
$(-1)^4 = 1$.  
$5(-1)^3 = -5$.  
$9(-1)^2 = 9$.  
$-(-1) = 1$.  
$-14$.  
Sum: $1 - 5 + 9 + 1 - 14$.  
$1+9+1 = 11$.  
$-5-14 = -19$.  
$11 - 19 = -8$.  
Calculation is solid.  

Let me re-verify the calculation for $P(-2)$.  
$x=-2$.  
$(-2)^4 = 16$.  
$5(-2)^3 = 5(-8) = -40$.  
$9(-2)^2 = 9(4) = 36$.  
$-(-2) = 2$.  
$-14$.  
Sum: $16 - 40 + 36 + 2 - 14$.  
Positives: $16+36+2=54$.  
Negatives: $-40-14=-54$.  
$54-54=0$.  
Calculation is solid.  

Let me re-verify the factorization check with quadratic discriminant.  
Roots of $x^2+4x+7$:  
$x = \frac{-4 \pm \sqrt{16-28}}{2} = -2 \pm \sqrt{-5/1}$... complex. No integer roots.  
Correct.  

Final Answer seems to be $1, -2$.  
Or maybe sorted $-2, 1$. I'll just list them.  

Let me double check the wording "enter all the integer roots". It asks for a set/list.  
Usually comma separated is expected.  
Format: $-2, 1$ or $1, -2$. I will write both if it's ambiguous, but mathematically they are two elements.  
Is it possible there are repeated roots?  
Since discriminant of $Q(x)$ was not calculated explicitly to show distinct roots (quadratic is irreducible over reals), we know the factor $(x^2+4x+7)$ does not share any roots with $x-1$ or $x+2$.  
Roots of $x-1$ is 1.  
Roots of $x+2$ is -2.  
Roots of $Q(x)$ are non-real.  
So all roots of $P(x)$ are simple distinct integers $1, -2$.  

One more check on the prompt "Find all the integer roots".  
Does it imply finding multiplicity? No, usually just the value. If there was a double root, it's still a root. But here roots are distinct.  
Also, if I had $x^4 = 16$ with $2 \sqrt{16}$ being 2 roots. No, integer roots refers to x values where P(x)=0.  
So just $\{-2, 1\}$.  

Let's check the polynomial coefficients again from the prompt to ensure no typo in my transcription.  
$x^4 + 5x^3 + 9x^2 - x - 14 = 0$.  
My work used this.  
Ok.  

Is there any chance I made a mistake in checking divisors of -14?  
Factors: 1, 2, 7, 14. Negatives: -1, -2, -7, -14.  
Checked all of them.  
Checked $x=1$, $P(1)=0$.  
Checked $x=-1$, $P(-1) \neq 0$.  
Checked $x=2$, $P(2) \neq 0$.  
Checked $x=-2$, $P(-2)=0$.  
Checked $x=7$, $P(7) \neq 0$.  
Checked $x=-7$, $P(-7) \neq 0$.  
Checked $x=14$, $P(14) \neq 0$.  

Seems robust.  

Let's think if there is any trick.  
$x^4 + 5x^3 + 9x^2 - x - 14$  
Group terms?  
$x^2(x^2+5x+9) - (x+14)$ No obvious factoring.  
$(x^2+Ax+B)(x^2+Cx+D)$?  
We already found factors $(x-1)$ and $(x+2)$.  
So $(x-1)(x+2) = x^2+x-2$.  
Then divide by $x^2+x-2$:  
$(x^4+5x^3+9x^2-x-14) \div (x^2+x-2)$  
Leading terms: $x^2$.  
$= (x^2)(x^2+x-2) = x^4+x^3-2x^2$.  
Subtract from original: $(5-1)x^3 + (9 - (-2))x^2 ...$  
$= 4x^3 + 11x^2 - x - 14$.  
Next term in division should be $+4x$.  
$(4x)(x^2+x-2) = 4x^3+4x^2-8x$.  
Subtract: $(11-4)x^2 + (-1+8)x - 14$  
$= 7x^2 + 7x - 14$.  
Next term $+7$.  
$(7)(x^2+x-2) = 7x^2+7x-14$.  
Remainder 0.  
So quotient is $(x-1)(x+2)(x^2+4x+7)$ ?  
No, the division was:  
1st step by $x^2$: coeff of first factor is $x^2+x-2$ (not quite).  
Let's re-do long division with original to be sure.  
Original: $x^4 + 5x^3 + 9x^2 - x - 14$.  
Factor $(x+2)$?  
$x^2(x^2+x-2)$ leaves remainder terms from previous step calculation above.  
My previous synthetic division confirmed the factorization.  
$P(x) = (x-1)(x+2)(x^2+4x+7)$.  
Let's verify grouping of terms in that expansion again.  
$x^2(x^2+x-2)(x^2+4x+7)$? No, $x^2+4x+7$ is quadratic factor, not multiplied by anything to get original degree 4 unless divided.  
The product $(x^2+x-2)(x^2+4x+7) = x^4 + (1+4)x^3 + (1+8+10)x^2 ...$ No.  
Let's re-multiply $(x-1)(x+2)$ to get $x^2+x-2$.  
$(x^2+x-2)(x^2+4x+7) = x^2(x^2+4x+7) + x(x^2+4x+7) - 2(x^2+4x+7)$.  
$= x^4 + 4x^3 + 7x^2 + x^3 + 4x^2 + 7x - 2x^2 - 8x - 14$.  
$= x^4 + (4+1)x^3 + (7+4-2)x^2 + (7-8)x - 14$.  
$= x^4 + 5x^3 + 9x^2 - x - 14$.  
Yes, it matches.  

So the integer roots are indeed $1$ and $-2$.  

Is there any ambiguity in "integer roots"? No.  
Does it mean rational roots that are integers? Yes.  
Are there other non-integer roots? The question asks for integer roots.  
We established all real roots are roots of $(x-1)(x+2)(x^2+4x+7)$.  
Since the quadratic part has no real roots, there are no other roots.  
The only roots are 1 and -2.  

Final check:  
$x=1$: $1 + 5 + 9 - 1 - 14 = 0$.  
$x=-2$: $16 - 40 + 36 + 2 - 14 = 0$.  
Are there any other?  
Since $x^2+4x+7$ has roots $\frac{-4 \pm i\sqrt{12}}{2} = -2 \pm i\sqrt{3}$. Neither is integer.  
The roots of original polynomial are complex conjugates $-2-i\sqrt{3}$? No, those come from quadratic.  
Roots of cubic: $(-2)$ and other two complex.  
Roots of original: 1, -2, -2+i... No.  
Original has roots 1, -2, and the roots of quadratic factor.  
The quadratic factor roots are not integers.  
So only integer roots are 1 and -2.  

Just to be pedantic, could $x^4+5x^3+9x^2-x-14$ have other integer roots? No, Rational Root Theorem guarantees we tested all possibilities from divisors of constant term. Since polynomial is degree 4, there are only these candidates.  
So I am confident in the result.  

Final Answer format: \boxed{-2, 1} or \boxed{1, -2}.  
Order doesn't matter usually, but ascending order $-2, 1$ looks standard.  
The problem says "Enter all the integer roots".  
I will list them separated by commas.  
One last check on arithmetic for $x=7$.  
$P(7) = 7^4 + 5 \cdot 7^3 + 9 \cdot 7^2 - 7 - 14$.  
$2401 + 1715 + 441 - 21$.  
$2400+1700+400 = 4500$.  
Not zero.  
Wait, if $x=7$ was a root, it would mean divisibility by 7.  
But constant term is -14. So $P(7) \equiv 0 \pmod{7}$?  
$P(7)$ is sum of multiples of 7 (except linear/const terms).  
Actually $7^2 = 49$. $7^3=343$. $7^4=2401$. All divisible by 7.  
So first three terms are divisible by 7.  
$-x - 14$ is divisible by 7.  
So $P(7) \equiv 0 \pmod{7}$. It doesn't disprove it, just says it's consistent.  
But evaluating the number is easier.  
$2401 + 1715 + 441 = 4557$.  
$4557 - 21 = 4536 \neq 0$.  

For $x=-7$:  
Terms divisible by 7 (except constant).  
$P(-7) = (-7)^4 + 5(-7)^3 + 9(-7)^2 - (-7) - 14$.  
$2401 - 1715 + 441 + 7 - 14$.  
Positives: $2401 + 441 + 7 = 2849$.  
Negatives: $-1715 - 14 = -1729$. (Since $-(-7)=+7$).  
$2849 - 1729 = 1120 \neq 0$.  

For $x=14$:  
$P(14) > 0$.  
For $x=-14$:  
Terms: $(-14)^4 + 5(-14)^3 + 9(-14)^2 - (-14) - 14$.  
Positives: $(+14^4 + 9 \cdot 14^2 + 14)$.  
Negatives: $-5(14^3)$.  
Since degree is high positive term dominates, likely non-zero.  
Let's check roughly.  
$14^4 = 38416$.  
$5 \times 14^3 = 1000 \times 20 = 1715$. $14^3 = 2744$. $5 \times 2744 = 13720$.  
So $38416 - 13720 + ... > 0$. Not zero.  

Candidates are definitely only $\pm 1, \pm 2, \pm 7, \pm 14$.  
And we ruled them out except 1 and -2.  

Double check the discriminant calculation for quadratic factor $x^2+4x+7$.  
$\Delta = 16-28=-12$.  
Since coefficients are integers (from integer polynomial), if there were rational roots, they would be integers (Rational Root Theorem).  
Since no real roots exist, definitely not integers.  

Final Answer is -2, 1.  

One minor thing: Could $x$ be a variable? No, "integer roots" means specific numbers.  
I'll format the output as requested.  

Step-by-step derivation:  
1.  **Apply Rational Root Theorem**: Since the polynomial $P(x) = x^4 + 5x^3 + 9x^2 - x - 14$ has integer coefficients, any rational root $p/q$ (in lowest terms) must have $q=1$ and $p$ dividing the constant term $-14$. The divisors of $14$ are $\pm 1, \pm 2, \pm 7, \pm 14$.  

2.  **Test candidates**:  
    *   **Test $x = 1$**:  
$P(1) = 1 + 5(1) + 9(1) - 1 - 14 = 1 + 5 + 9 - 1 - 14 = 0$.  
So, **$x = 1$** is a root.  

    *   **Test $x = -1$**:  
$P(-1) = 1 - 5 + 9 + 1 - 14 = -8 \neq 0$.  

    *   **Test $x = 2$**:  
$P(2) = 16 + 40 + 36 - 2 - 14 = 76 \neq 0$.  

    *   **Test $x = -2$**:  
$P(-2) = 16 - 40 + 36 + 2 - 14 = 0$.  
So, **$x = -2$** is a root.  

    *   (Optional but helpful) **Factor the polynomial**:  
Since we found roots 1 and -2, we can divide $P(x)$ by $(x-1)$ and $(x+2)$.  
$(x^4 + 5x^3 + 9x^2 - x - 14) \div (x^2+x-2) = x^2 + 4x + 7$.  
This can be verified by expanding: $(x-1)(x+2)(x^2+4x+7) = (x^2+x-2)(x^2+4x+7) = x^4 +  

## Answer

*(none: the token cap hit during thinking)*
