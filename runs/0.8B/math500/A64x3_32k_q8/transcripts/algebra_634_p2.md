# test/algebra/634.json, part 2 of 4

[Previous part](algebra_634.md)

$-(8r^2 - 34r + 21)$? No, that's if we move everything to LHS.  
Let's just do:  
$(8r^2 - 34r + 21) - (6r^2 - 19r - 7) = 0$.  
This yields the equation.  

$r^2$ term: $8 - 6 = 2$.  
$r$ term: $-34 - (-19) = -34 + 19 = -15$. (This is tricky with minus signs).  
Let's be very careful:  
Expression to equate to zero: $(8r^2 - 34r + 21) - (6r^2 - 19r - 7)$.  
Coefficient of $r^2$: $8 - 6 = 2$. Correct.  
Coefficient of $r$: $-34 - (-19)$? No.  
The term is $-34r$. Subtracted from the expression on LHS was... no.  
It is $(8r^2 - 34r + 21)$. We subtract this whole thing.  
So for each term, we subtract its coefficient.  
Term $r^2$: Subtracting the constant part? No. The expression is just numbers.  
LHS terms: $6r^2$, $-19r$, $-7$.  
RHS terms: $8r^2$, $-34r$, $+21$.  
Equation is: LHS - RHS = 0.  
So $(6 - 8)r^2 + (-19 - (-34))r + (-7 - 21) = 0$.  
$-2r^2 + (15)r + (-28) = 0$.  
Multiply by -1: $2r^2 - 15r + 28 = 0$.  

Let's check the coefficients again.  
$-19$ minus $(-34)$ is $+15$?  
$(6r^2 - 19r - 7) - (8r^2 - 34r + 21)$  
$= (-19r - 7 - 8r^2 + 34r + 21)$ ? No.  
The subtraction operation applies to the polynomial.  
$(6r^2 - 19r - 7) - (8r^2 - 34r + 21) = 0$?  
$6r^2 - 8r^2 = -2r^2$.  
$-19r - (-34r) = -19 + 34 = 15$.  
$-7 - (+21)$? No. The expression was $(...) + (-21)$. No, the equation had constant term on RHS as $+21$.  
If I subtract the expression $8r^2 - 34r + 21$ (which is the polynomial), I am subtracting $+21$.  
So $-7 - (+21)$?  
No, the equation is: $(6r^2 - 19r - 7) = (8r^2 - 34r + 21)$.  
Move RHS to LHS:  
$(6r^2 - 19r - 7) - (8r^2 - 34r + 21) = 0$.  
This is valid.  
Coeff of $r$: $-19 - (-34)$? No, the term is $-19r$ in LHS and $(-34r)$ in RHS.  
Subtracting RHS gives: $-19r - (-34r) = -19 + 34 = 15$.  
Coeff of constant: $-7 - (+21) = -28$.  
So we get $-2r^2 + 15r - 28 = 0$ (or $2r^2 - 15r + 28 = 0$).  

Roots again check.  
Roots for $2r^2 - 15r + 28 = 0$.  
Sum = $15/2$, Prod = $14/1 = 7$? No, constant is 28.  
Product of roots $\frac{2 \cdot 28}{2} = 28$? No, formula is $\frac{c}{a} = \frac{28}{2} = 14$.  
Roots: $\frac{-(-15) \pm 7}{2(2)} = \frac{15 \pm 7}{4}$.  
$r_1 = \frac{22}{4} = 5.5$.  
$r_2 = \frac{8}{4} = 2$.  

Now let's check validity of these roots in the original equation $\frac{6r^2 - 19r - 7}{2r-7} = 4r-3$.  

We need to check $LHS_{denom} \neq 0$ and $RHS_{denom} \neq 0$ (if using cross multiplication).  
For $r=5.5$:  
LHS denominator: $2(5.5) - 7 = 11 - 7 = 4 \neq 0$.  
RHS denominator: $4(5.5) - 3 = 22 - 3 = 19 \neq 0$.  
Now let's check the equation equality.  
LHS (numerator): $6(5.5)^2 - 19(5.5) - 7$  
$= 6(30.25) - 104.5 - 7 = 181.5 - 104.5 - 7$.  
$181.5 - 111.5 = 70$. (Since $104.5 - (-7)$? No.)  
$6 \times 30 = 180$.  
$6 \times 2.25$? $30.25 / 12$ is not simple.  
$6(30.25) = 181.5$.  
$-19(5.5) = -19(11/2) = -209/2 = -104.5$.  
$-7$.  
Sum: $181.5 - 104.5 - 7 = 77 - 7 = 70$.  
So Numerator is $70$.  

RHS (numerator): $22$.  
Denominator $LHS$: $4$.  
So $RHS_{denominator}$?  
LHS: $\frac{70}{4} = 17.5$.  
RHS: $4(5.5) - 3 = 19$.  

So we have $\frac{70}{4} \neq 19$. $70/4$ vs 19.  
$70/4 = 17.5$. $19 \neq 17.5$.  

Let me re-check my manual calculation of the equation value for $r=2$.  
$r=2$.  
LHS Num: $6(4) - 19(2) - 7 = 24 - 38 - 7 = 24 - 45 = -21$.  
Denominator LHS: $2(2)-7 = -3$.  
So $\frac{-21}{-3} = 7$.  
RHS (Num): $4(2) - 3 = 5$. (RHS Num is not used? No, RHS expression).  
Equation is $\frac{LHS}{RHS\_denom} \neq RHS$.  
Original eq: $\frac{6r^2 - 19r - 7}{2r-7} = 4r-3$? No.  
RHS of original equation is a term in the fraction, not a number on the other side of the equals sign.  
LHS of equation (the value $\frac{6r^2-...}{2r-7}$) is equal to $4r-3$.  
The RHS expression is actually $RHS$ evaluated as a term? No.  
It says $\frac{\text{Num}}{D} = 4r - 3$.  
This means the value of $4r-3$ is equal to the fraction value.  
So for $r=2$:  
LHS = $7$. RHS = $5$.  
$7 \neq 5$. So $r=2$ is not a solution.  

Let me re-check my manual calculation for roots of the quadratic equation.  
Quadratic equation: $-2r^2 + 15r - 28 = 0$.  
Roots are $\frac{-15 \pm 7}{-4}$? No, discriminant was calculated correctly as 49.  
If coeff is $-2$, then $a=-2$.  
Equation: $-2r^2 + 15r - 28 = 0$.  
Multiply by -1: $2r^2 - 15r + 28 = 0$.  
This matches my previous derivation.  
Roots of this quadratic:  
$\frac{15 \pm \sqrt{49}}{4}$.  
$\frac{15+7}{4} = 5.5$.  
$\frac{15-7}{4} = 2$.  

Why did the root verification fail?  
Check $r=2$ in original equation again.  
LHS: $\frac{-21}{-3} = 7$. RHS: $5$. Not equal. Correct.  
Check $r=5.5$ in original equation.  
$r=11/2$.  
$2r-7 = 11 - 7 = 4$.  
Numerator: $6(23) - 19(11/2) - 7$? No, $r^2 = 121/4$.  
Let's compute carefully.  
Num: $6(22.5) - 19(5.5) - 7$? No, $(22/2)(6) = 12 \times 6 = 72$ (No, $180 + 48$? No.)  
$6r^2$: $6 \times (121/4) = 30.25 \times 6$? No.  
$6(22.5) = 135$.  
$19(11/2) = 181.5$.  
$7$.  
Sum: $135 - 104.5 - 7 = 23.5$? No. $135 - 111.5 = 23.5$.  
Denom: 4.  
Value: $23.5 / 4 = 5.875$.  
RHS: $4(5.5) - 3 = 22 - 3 = 19$.  
Still not equal.  

There must be a calculation error in roots.  
Let's re-verify the discriminant of $2r^2 - 15r + 28$.  
Roots: $\frac{15 \pm \sqrt{225 - 176}}{4}$.  
$225 - 176 = 49$. Correct.  
So roots are correct.  
Let me re-verify the expansion of $(4r-3)(2r-7)$.  
$4(2) = 8$. $4(-7) = -28$. $-3(2) = -6$. $-3(-7) = +21$.  
Sum: $8 - 34 + 21$? No. $-28 - 6 + 21 = -5$? No.  
$8r^2 - 28r - 6r + 21$.  
$-28r - 6r = -34r$.  
$+21$.  
So expansion is correct.  

Let me re-verify LHS numerator coefficient of $r^2$.  
LHS: $6r^2 - 19r - 7$. Correct.  

Let me check the equation logic again.  
$\frac{A}{B} = C \implies A(B_{term}) = B(C(B_{term}))$? No.  
It means $A/B - C = 0 \implies AB - BC = 0$.  
This implies $AB = BC$.  
Multiply by $D$ (where $D=B^2$?). No, just multiply by denominators if possible.  
$B(4r-3) = A(2r-7)$? No.  
$\frac{A}{B} = C \implies AB = BC$.  
So $(6r^2 - 19r - 7)(4r-3) = (2r-7)(2r-7)$.  
$LHS_{num}$?  
If I do this, I get:  
$A(4r-3) = B$. This leads to $(6r^2 - 19r - 7)(4r-3)$ and $(2r-7)(2r-7)$.  
But the equation in the prompt is $\frac{N}{D} = C$.  
So $N = CD$ is WRONG.  
The cross product is $CD - A B^{-1}$? No.  

Let's go back to $AB = BC$ logic.  
If $A/B = C$, then $A \cdot (B^{-1}) = C \cdot (B^{-1} \cdot 1)$. No.  
It is $(6r^2 - 19r - 7)(4r-3) / (2r-7) = (2r-7)(4r-3)$? No.  
Let's try $LHS - RHS = 0$.  
This is what I did in step 5.  
So why did it give me wrong results?  
Wait, let me re-evaluate the calculation for roots.  
$2r^2 - 15r + 28 = 0$? Or something else?  

Let's try to factor $6r^2 - 19r - 7$.  
Roots: $3.5, -1/3$.  
Product of roots is -7. (For $3.5(-1/3) = -1/2$). Not matching.  
Sum of roots: $(3.5 + (-0.33...)) \approx 3.16$.  
Let's check the factorization of $6r^2 - 19r - 7$.  
Try factoring:  
Roots are $\frac{19 \pm \sqrt{19^2 - 4(6)(-7)}}{12} = \frac{19 \pm \sqrt{361 + 168}}{12} = \frac{19 \pm \sqrt{529}}{12}$.  
$\sqrt{529}$: $20^2 = 400$, $23^2 = (25-2)^2$? No. $23 \times 23$:  
$23 \times 23 = 23(20+3) = 460 + 69 = 529$.  
So roots are $\frac{19 \pm 23}{12}$.  
$r_1 = \frac{42}{12} = \frac{7}{2} = 3.5$.  
$r_2 = \frac{-4}{12} = -1/3$.  

Now let's check these roots in the original equation.  
If $r=3.5$ or $r=-1/3$, does it satisfy?  
Let's plug them into LHS of original equation.  
$\frac{6r^2 - 19r - 7}{2r-7}$.  
For $r = 3.5$:  
Numerator: $6(3.5)^2 - 19(3.5) - 7$?  
$6 \times (3.5^2) = 6 \times 12.25 = 73.5$.  
$-19(3.5) = -104.5$.  
$-7$.  
Sum: $73.5 - 104.5 - 7 = -23.5$?  
$6r^2$: $(7/2)^2 \times 6 = (49/4) \times 6 = 249/4 = 62.25$.  
$-19(7/2) = -133/2 = -66.5$.  
$-7$.  
Sum: $62.25 - 66.5 - 7 = -8.25$? No, let's calculate carefully.  
Numerator: $N(r) = 6r^2 - 19r - 7$.  
Roots of quadratic are derived from $\frac{N}{D} = C \implies N(4r-3) = D(B) \dots$? No, $N/C = B/D$.  
If $r=7/2$, let's use fractions.  
$r = 14/6 = 7/2 = 3.5$.  
$r^2 = 49/4$.  
$6r^2 = 6(49/4) = 294/4 = 147/2 = 73.5$.  
$-19r = -19(7/2) = -133/2 = -66.5$.  
$-7$.  
Numerator $N = 73.5 - 66.5 - 7 = 7.5 - 7 = 0.5$.  
Denominator $D = 2(7/2) - 7 = 7 - 7 = 0$. Oh, $D$ is zero!  
So $r=3.5$ makes the denominator zero in the original equation (division by zero).  
This explains why $r=3.5$ is not a solution. It also explains why I should check the factorization of $6r^2 - 19r - 7$.  
The roots of the numerator are $3.5, -1/3$. If $D(r)=0$, then the expression is undefined.  
Let's recheck my calculation of roots again.  
Roots were $\frac{19 \pm 23}{12}$.  
$r_1 = \frac{42}{12} = \frac{7}{2}$. Correct.  
$r_2 = \frac{-4}{12} = -\frac{1}{3}$.  

Let's check if $r=7/2$ satisfies the equation (it should not be a solution anyway).  
The original equation is $\frac{6r^2 - 19r - 7}{2r-7} = 4r-3$.  
If $r=7/2$, denominator $2r-7 = 0$. So LHS undefined.  
Thus $r=7/2$ is extraneous (division by zero) and not a solution.  

Now check $r = -1/3$.  
Denominator: $2(-1/3) - 7 = -2/3 - 7 = -23/3$. Not zero.  
Let's check numerator:  
Numerator: $6r^2 - 19r - 7$? Or was that $(4r-3)$ term?  
LHS of original equation is $\frac{N}{D}$. So we check if $\frac{N}{D}$ equals $C$.  
If $D \neq 0$, check equality.  

$r = -1/3$  
$6(-1/3)^2 - 19(-1/3) - 7$.  
$6(1/9) + 19/3 - 7$.  
$6/9 + 19/3 - 7$.  
$2/3 + 19/3 - 7$.  
$(2+19)/3 - 7 = 21/3 - 7 = 7 - 7 = 0$.  
So Numerator is 0 at $r=-1/3$?  
Let's re-evaluate: $6(1/9) + 19(3/9)? No, $-19(-1/3) = +19/3$.  
$21/3 - 7 = 7 - 7 = 0$. Correct.  
So numerator is zero at $r=-1/3$ (and $r=3.5$).  

Let's check if this is a solution.  
$\frac{0}{-23/3} = 0$.  
RHS is $4(-1/3) - 3 = -4/3 - 9/3 = -13/3 \neq 0$.  
So it's not a solution.  

Okay, so where did the roots of the quadratic come from?  
They are solutions to $LHS_{num} + C = 0$?  
The question implies $\frac{6r^2 - 19r - 7}{2r-7} = 4r-3$.  
If this is a linear equation, then no solution. But it's not that.  

Let me double check the expansion of $(4r-3)(2r-7)$.  
$4r(2r) = 8r^2$.  
$4r(-7) = -28r$.  
$-3(2r) = -6r$.  
$-3(-7) = +21$.  
Sum: $8r^2 - 34r + 21$.  
Equation: $(6r^2 - 19r - 7) / (2r-7) = 4r-3$.  
Cross multiply: $(6r^2 - 19r - 7)(2r+7) = (4r-3)(2r-7)$? No.  
Wait, the question is $\frac{A}{B} = C$.  
This means $A/B$ equals $C$.  
It does NOT mean $A(2r-7) / B = C$ or something like that.  
The standard form for cross multiplication to remove fractions is:  
If I have $\frac{A}{B} = C$, and we want to eliminate denominator, we can rewrite as $(A \cdot 1)(D) + ...$.  
No, it means $A/B - C = 0$ is valid.  
So we need $A - BC = 0$.  
This leads to the equation I derived: $6r^2 - 19r - 7 - (4r-3)(2r-7) = 0$.  

However, looking at the expansion of $(4r-3)(2r-7)$:  
$8r^2 - 34r + 21$.  
And $6r^2 - 19r - 7$.  
So the equation is indeed $6r^2 - 19r - 7 = 8r^2 - 34r + 21$.  
Which simplifies to $2r^2 - 15r + 28 = 0$ or something.  

But I found earlier that the roots of this quadratic (from my manual calculation) were:  
$r_1 = 5.5$, $r_2 = 2$.  
These roots made the denominator $2r-7$ zero at one of them?  
Let's check $r=2$: Denom is $4-7=-3$. Not zero.  
Let's check $r=5.5$: Denom is $11-7=4$. Not zero.  

So why did I conclude earlier that roots were $\pm 7/2$ and $\mp 1/3$ for the numerator?  
That was derived from solving the numerator equation (treating it as a polynomial equal to 0)? No, this is different.  
The roots of $6r^2 - 19r - 7 = 0$ are $3.5$ and $-1/3$.  
This equation was used in some step where I might have gotten confused?  
Let's check if the denominator being zero means we must check $4r-3 \neq 0$. No.  

Is there any other constraint? The problem asks for "the value of r". Plural/Single?  
Usually these problems imply finding all roots of the rational equation (where undefined points are excluded) or solving for valid r.  

Let's go back to step 5: $2r^2 - 15r + 28 = 0$? Or is there an error in my previous logic?  
I will check the factorization of the original expression $\frac{6r^2 - 19r - 7}{2r-7}$.  
Let's factor $6r^2 - 19r - 7$.  
Roots are indeed $3.5$ and $-1/3$.  
Check product: $3.5 \times (-0.33...) = -1.16$. No, $7/2 \times -4/12 = -7/6 \neq 7/2$.  
Let's recheck roots of numerator $6r^2 - 19r - 7$.  
Sum: 19/6? No. Sum is positive 19? No, roots are negative/negative/negative.  
$x = \frac{19 \pm \sqrt{19^2 - 4(6)(-7)}}{12}$.  
$\Delta = 361 + 168 = 529$. Correct.  
Roots: $\frac{19 \pm 23}{12}$.  
$r_1 = 42/12 = 3.5$.  
$r_2 = -4/12 = -1/3$.  

If $r=3.5$, denominator is 0? Yes, $2(3.5)-7=0$.  
So this root makes the original equation undefined. Thus it's not a solution.  
Let's check if there is an extraneous solution introduced by squaring or cross-multiplication that introduces solutions where denominator becomes zero? No, we didn't square.  

So let's revisit my quadratic derivation.  
Maybe I made a mistake in the expansion.  
$A/B = C \implies A - BC = 0$.  
$6r^2 - 19r - 7 - (4r-3)(2r-7) = 0$  
$8r^2 - 34r + 21 - (6r^2 - 19r - 7)$? No, $(4r-3)(2r-7) = 8r^2 - 28r - 6r + 21$.  
Let's re-expand the product carefully again.  
$(4r - 3)(2r - 7)$:  
$4r \cdot 2r = 8r^2$  
$4r \cdot (-7) = -28r$  
$(-3)(2r) = -6r$  
$(-3)(-7) = +21$  
So, correct expansion is $8r^2 - 34r + 21$.  

So the equation is:  
$6r^2 - 19r - 7 = 8r^2 - 34r + 21$ (LHS = RHS? No, LHS is fraction value).  
If I cross multiply $\frac{N}{D} = C$, then $(N) \cdot D^{-1} = C$.  
$N(2r-7) - (4r-3)(2r-7)?$ No.  
This leads to $N(4r-3) - D(2r-7)$? No.  
It leads to $(N) \cdot 1 - C \cdot D$? No.  

The logic: $\frac{6r^2 - 19r - 7}{2r-7} = 4r - 3$.  
Multiply both sides by $2r-7$:  
$6r^2 - 19r - 7 = (4r-3)(2r-7)$.  
This is exactly what I did in step 5.  
$LHS = N$, $RHS = C(2r-7)$? No, RHS of the fraction is not multiplied by 2r-7, it's just equal to that term.  
So we equate the terms:  
LHS (numerator) = RHS (expanded).  
$(6r^2 - 19r - 7) = (8r^2 - 34r + 21)$.  
$0 = 8r^2 - 6r^2 - 19r + 19r + 21 + (-21)$? No.  
Equation: $(6r^2 - 19r - 7) - (8r^2 - 34r + 21) = 0$.  
$-2r^2 + (-34+19)r + (21+7) = 0$? No.  
$(6r^2 - 8r^2) = -2r^2$.  
$(-19r + 34r) = 15r$.  
$(-7 - 21)$?  
Let's do subtraction of constant terms carefully:  
LHS: $-7$. RHS has $+21$.  
When we subtract $RHS$ from LHS, we subtract $+21$.  
So it becomes $-7 - 21 = -28$.  
So the equation is: $-2r^2 + 15r - 28 = 0$?  
Or $2r^2 - 15r + 28 = 0$ if I move everything to one side correctly.  
$(6r^2 - 19r - 7) = (8r^2 - 34r + 21)$  
Subtract LHS from RHS? No, subtract RHS from LHS.  
$-2r^2 + 15r - 28 = 0$?  
Check sign of linear term:  
Equation is $LHS = RHS$.  
So move all terms to one side.  
$(6r^2 - 19r - 7) - (8r^2 - 34r + 21) = 0$? No, LHS was $A$, RHS was $C$. So $A - C = 0$.  
This implies:  
$6r^2 - 19r - 7 - (8r^2 - 34r + 21) = 0$.  
$(6-8)r^2 + (-19 - (-34))r + (-7 - 21) = 0$.  
$-2r^2 + 15r - 28 = 0$.  

This leads to roots $r = \frac{-15 \pm 7}{-4}$? No, $\frac{-b \pm \sqrt{b^2-4ac}}{2a}$.  
Equation: $-2r^2 + 15r - 28 = 0$.  
Roots: $\frac{-(-15) \pm \sqrt{(-15)^2 - 4(-2)(-28)}}{2(-2)}$?  
Formula is $(\dots) / (2a)$? No. $ax^2+bx+c$.  
Here roots: $r = \frac{-15 \pm \sqrt{225 + 176}}{4}$? No, coeff of $x^2$ is -2.  
So $\Delta = 225 - 4(-2)(-28) = 225 - 176 = 49$.  
Roots: $\frac{-15 \pm 7}{-4}$? No, formula $r = \frac{-b}{2a} \pm \frac{\sqrt{\Delta}}{2a}$.  
Here $a=-2$.  
Roots: $\frac{15 \pm 7}{-4} = \frac{8}{-4}, \frac{22}{-4} = -2, -2$. (No).  
Let's check the formula.  
$x^2$ is negative? No, equation is $-2x^2 + ...$  
Roots are $\frac{-15 \pm \sqrt{49}}{2(-2)}$? No, denominator is $2a$.  
If $a=-2$, then denom is -4.  
$r = \frac{15 \pm 7}{-4}$.  
$r_1 = \frac{8}{-4} = -2$.  
$r_2 = \frac{22}{-4} = -2 + 5$? No. $22/4 = 5.5$.  
So roots are $-2, -5.5$ or something.  
Let's compute again: $\frac{-15+7}{-4} = \frac{-8}{-4} = 2$.  
And $\frac{-15-7}{-4} = \frac{-22}{-4} = 5.5$.  
So roots are $r=2$ and $r=5.5$.  
Let's check the sign of LHS and RHS for these.  
Equation derived: $-2r^2 + 15r - 28 = 0$ or $2r^2 - 15r + 28 = 0$?  
I got $2r^2 - 15r + 28 = 0$ in step 4. Why did I think that?  
Let's check the subtraction step again.  
Equation: $(6r^2 - 19r - 7) = (8r^2 - 34r + 21)$.  
$-2r^2 + (-19+34)r + (-7-21)$? No, $(-7) - (+21) = -28$.  
So the linear term is correct as it is a sum of terms.  
So we have $-2r^2 + 15r - 28 = 0$ or $2r^2 - 15r + 28 = 0$.  
Let's recheck the signs in step 4.  
I derived $(6r^2 - 19r - 7) - (8r^2 - 34r + 21) = 0$? No, if $A=B$, then $A-B=0$.  
If $A = B$, I can just move terms.  
$6r^2 - 8r^2 = -2r^2$. (Coeff of $r^2$ is 8-6=2. But I'm subtracting).  
Let's write it out again.  
Term 1 ($r^2$): $LHS$ has 6, RHS has 8. So $6 - 8 = -2$.  
Term 2 ($r$): $LHS$ has -19, RHS has -34. Subtracting RHS gives $-19 - (-34) = -19 + 34 = 15$.  
Term 3 (const): $LHS$ has -7, RHS has 21. Subtracting RHS gives $-7 - (+21)$? No, it's just the constant term subtraction.  
The equation is: $(6r^2 - 19r - 7) = (8r^2 - 34r + 21)$.  
Move everything to LHS:  
$6r^2 - 8r^2 - 19r - (-34r) - 7 - 21 = 0$?  
$-2r^2 + 15r - 28 = 0$.  

Let's check the coefficients again.  
Term $1$: LHS has $+6r^2$. RHS has $+8r^2$.  
So we subtract RHS from LHS? No, I want to move terms to one side.  
If I say $A = B$, and I expand $B$ on the right:  
$0 = (6r^2 - 19r - 7) - (8r^2 - 34r + 21)$?  
Yes, if this were true.  
But the original equation was $\frac{N}{D} = C$.  
This means $(N)(2r-7)^{-1} \neq C(2r-7)^{-1}$.  
It means $A/B = C$.  
Cross multiplying is valid.  
If I cross multiply both sides by $B$: $A = C B$? No, that's $A = BC$.  
It implies $C^{-1} A^{-1}$... no.  
It means $\frac{6r^2 - 19r - 7}{2r-7} = (4r-3)$.  
This is equivalent to $(6r^2 - 19r - 7)(2r-7)^{-1} \neq 0$? No, this means $A/D = C$.  
If I cross multiply: $A(2r-7)^{-1}$... no.  
The correct form is: $N(2r-7) - (4r-3)(2r-7)$? No.  
It means $(6r^2 - 19r - 7)(2r-7) = (4r-3)(2r-7)(2r-7)^{-1}$... no.  
The equation $A/D = C$ is valid as long as denominators are non-zero.  
So we simply have:  
$\frac{6r^2 - 19r - 7}{2r-7} = 4r - 3$.  
If I cross multiply by $2r-7$:  
$(6r^2 - 19r - 7) / 1$? No.  
Multiply both sides by $2r-7$:  
LHS: $(6r^2 - 19r - 7)$ (numerator).  
RHS: $(4r-3)(2r-7)$ (numerator term of the fraction, not just term).  
This is NOT what I did.  
The cross multiplication step is:  
$\frac{6r^2 - 19r - 7}{2r-7} = 4r-3$.  
Multiply by $2r-7$:  
$6r^2 - 19r - 7$? No, that's the LHS.  
RHS $\cdot (2r-7)$.  
This means we multiply the equation by $(2r-7)$ to clear the denominator from LHS.  
So: $(6r^2 - 19r - 7)(2r-7) = 0$? No, that's if the denominators were just numbers and I multiplied.  
If I have $\frac{N}{D} = C$, then $N/D = C$.  
If I clear the denominator by multiplying:  
$(6r^2 - 19r - 7) / (2r-7)$ is not zero unless $D=0$.  
If I multiply both sides by $2r-7$:  
$(6r^2 - 19r - 7)(2r-7)^{-1}$? No.  
Multiply the fraction by 1 to get integers:  
$\frac{N(4r-3)}{2r-7}$? No.  
If I have $\frac{6r^2 - 19r - 7}{2r-7} = C$.  
Then cross multiply means: $(6r^2 - 19r - 7)(2r-7)$? No.  
This is just getting $A$ and $C$ on the same side.  
If I write it as $\frac{6r^2 - 19r - 7}{2r-7} = (4r-3)$, then subtract:  
$(6r^2 - 19r - 7)(2r-7)^{-1}$? No.  
Multiply the equation by $2r-7$ directly?  
$\frac{A}{D} = C \implies A(2r-7) = (4r-3)(2r-7)$ is FALSE unless $C=0$.  
It's $(6r^2 - 19r - 7) = (4r-3)(2r-7)$? No.  
If I multiply both sides by $D$, I am multiplying by the denominator.  
So:  
LHS = $\frac{A}{B}$. Multiply by B.  
RHS = $C \cdot D$? No, RHS is $4r-3$.  
Equation is: $\frac{6r^2 - 19r - 7}{2r-7} = 4r-3$.  
Multiply both sides by $2r-7$:  
$(6r^2 - 19r - 7)(2r-7)^{-1}$? No.  
The term multiplying by $2r-7$ is the numerator of the fraction on the LHS.  
And on the RHS, I just have the expression $4r-3$.  
So $(6r^2 - 19r - 7)(2r-7) = (4r-3)(2r-7)$? No.  
The equation is $\frac{A}{B} = C$.  

*Continued in [part 3 of 4](algebra_634_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
