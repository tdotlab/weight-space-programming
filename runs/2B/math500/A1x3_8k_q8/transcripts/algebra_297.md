# test/algebra/297.json (Algebra, level 5)

> Find the product of the $y$-coordinates of all the distinct solutions $(x,y)$ for the two equations $y=x^2-8$ and $y^2=-5x+44$.  

**Wrong.** Gold `1736`, predicted `None`. Finish: length, 8192 tokens, 2 waits, 1051.2 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here is my thought process for solving this problem:  

1.  **Analyze the Request:** The user wants to find the product of the $y$-coordinates of all distinct solutions $(x,y)$ to the system of two equations:  
    *   Equation 1: $y = x^2 - 8$  
    *   Equation 2: $y^2 = -5x + 44$  

2.  **Strategy:**  
    *   I need to find the points $(x,y)$ that satisfy both equations simultaneously.  
    *   This is a system of equations, which implies finding the intersection of two curves.  
    *   Since one equation relates $y$ directly to $x$, and the other involves squares, substitution seems like the most direct method.  

3.  **Step-by-Step Execution:**  

    *   **Equation Set:**  
        1.  $y = x^2 - 8$ (This is a parabola opening upwards with vertex at $(0, -8)$).  
        2.  $y^2 = -5x + 44$ (This can be rewritten as $5x = 44 - y^2$, so $x = \frac{44}{5} - \frac{1}{5}y^2$. It's an upside-down parabola).  

    *   **Substitution Method:**  
Substitute the expression for $y$ from equation (1) into equation (2).  

    *   **Step 1: Substitution**  
From (1), we have $y = x^2 - 8$.  
Into (2): $(x^2 - 8)^2 = -5x + 44$.  

    *   **Step 2: Algebraic Manipulation to find critical points**  
This is a quartic equation in terms of $x$: $(x^2 - 8)^2 = x^4 - 16x^2 + 64$.  
So, $x^4 - 16x^2 + 64 = -5x + 44$.  

    *   **Step 3: Simplify the Quartic Equation**  
Move everything to one side to form a polynomial equal to zero.  
$x^4 - 16x^2 + 5x + (64 - 44) = 0$  
$x^4 - 16x^2 + 5x + 20 = 0$.  

    *   **Step 4: Check for extraneous roots or distinct solutions.**  
The problem asks for "distinct solutions $(x,y)$".  
Each real solution $x$ corresponds to a pair of points. Since the equation is in terms of $y^2 = \dots$, actually, I substituted into $y^2$. Let's re-verify the constraint.  

    *   **Re-evaluating the substitution:**  
The original system:  
        1) $y = x^2 - 8$  
        2) $y^2 = -5x + 44$  

Let's check if my polynomial derivation covers all cases.  
If $(x, y)$ satisfies (2), then $-5x+44 \ge 0$, so $5x \le 44$.  
Also, substituting $y=x^2-8$ into $y^2 = -5x+44$:  
$(x^2 - 8)^2 + 5x - 44 = 0$.  
$x^4 - 16x^2 + 64 + 5x - 44 = 0$  
$x^4 - 16x^2 + 5x + 20 = 0$.  

Are there any other solutions? No, because if a point is on the graph of $y^2 = -5x+44$, its y-coordinate must satisfy $y^2 = (x^2-8)^2$.  
So finding the roots of $x^4 - 16x^2 + 5x + 20 = 0$ gives all x-coordinates. For each valid x, there are potential y-values.  
However, the equation relating x and y is quadratic in terms of $(x^2)$? No.  

*   **Analyze Distinct Solutions:**  
We have a quartic equation: $x^4 - 16x^2 + 5x + 20 = 0$.  
Let's call the roots $x_1, x_2, x_3, x_4$.  
For each root $x_i$, we find the corresponding $y_i$ using $y = x_i^2 - 8$.  
We need to check if there are any constraints. The equation for $x$ comes from substituting one expression for $y$ into another square term. If $x$ is a root, then $(-5x+44)$ is $(x^2-8)^2$, which means $y^2$ is determined. Thus $y = \pm (x^2 - 8)$.  
However, Equation 1 defines *specific* $y$ for *any* $x$: $y = x^2 - 8$. This restricts the relationship to that specific parabola. The second equation defines a region of valid x's based on y.  

    *   **Let's double check.**  
We substituted $y$ from Eq 1 into Eq 2.  
Eq 1: $y = f(x) = x^2 - 8$.  
Eq 2: $g(y) = y^2 + 5x - 44 = 0$, where $x=f^{-1}(y)$. Actually, solving for $x$: $5x = 44 - y^2 \implies x = 8.8 - 0.2y^2$.  
Since Eq 1 defines a single curve (a function of x), and Eq 2 is the inverse, let's just look at the intersection.  
Intersection points are where $f(x) = g^{-1}(x)$? No, simpler to just stick to algebraic substitution.  

We established $y = x^2 - 8$ satisfies $y^2 = (x^2-8)^2$.  
So for the intersection, we need $(x^2 - 8)^2 = -5x + 44$.  
Let's call the roots of this quartic $x_1, \dots, x_4$.  
For each root $x_i$, there is a corresponding y value: $y_i = x_i^2 - 8$.  
Is it possible that for some $x_i$, there are multiple y values?  
The derivation of $(x^2-8)^2 = -5x + 44$ ensures $y^2 = -5x+44$ is satisfied.  
Since $y$ must satisfy the *equation* Eq 1, we have $y = x^2 - 8$. This fixes the value of y for a given x.  
So every solution to the quartic equation corresponds to exactly one solution $(x,y)$ on the curve $y=x^2-8$, provided that the resulting y satisfies the condition $(-5x+44) = y^2$.  

Let's verify.  
If I have a root $x$, then $y_{calc} = x^2 - 8$ makes $(x, y_{calc})$ on Eq 1.  
The equation $(x^2-8)^2 = -5x+44$ is derived by substituting $y$ from Eq 1 into Eq 2.  
If this holds, then $(-5x + 44) = (x^2-8)^2$, which implies $(x^2-8)^2 = y_{calc}^2$.  
So $\pm \sqrt{-5x+44} = x^2-8$.  
Since we chose the branch $y = x^2 - 8$, it matches only if we didn't have other branches. But the derivation is based on satisfying both simultaneously.  
Specifically, we are looking for points $(x,y)$ on $y=x^2-8$ AND on $y^2=-5x+44$.  
So we just solve $y = x^2 - 8$ and plug into $y^2 = -5x + 44$.  
This means finding real roots of the quartic equation $P(x) = 0$.  
For each real root $x$, $y = x^2 - 8$ is a valid y-coordinate because we solved for it specifically.  

*   **Finding the Roots:**  
We need to solve $x^4 - 16x^2 + 5x + 20 = 0$.  
Let's test for integer roots. Possible rational roots: factors of 20 / factors of 1. $\pm 1, \pm 2, \pm 4, \pm 5, \pm 10, \pm 20$.  

Test $x=1$: $1 - 16 + 5 + 20 = 10 \neq 0$.  
Test $x=-1$: $1 - 16 - 5 + 20 = 0$.  
So, $x = -1$ is a root.  

Divide by $(x+1)$:  
$(x+1)(x^3 - x^2 - 17x - 19) / (x+1)$ ... No, use synthetic division or polynomial division.  
$x^4 - 16x^2 + 5x + 20 \div (x+1)$:  
1  | -1  -17   -19     0  
1  |      1  -16  -33  -20 ? No wait.  

Let's re-multiply $(x+1)(Ax^3 + Bx^2 + Cx + D)$: $A x^4 + (A+B)x^3 + (B+C)x^2 + (C+D)x + D$.  
Compare with $x^4 - 16x^2 + 5x + 20$.  
$A=1$.  
$A+B = 0 \implies B=-1$.  
$B+C = 0$ ? No, middle term is $-16x^2$. So $-x^3 - x^2$.  
Let's redo:  
$(x+1)(x^3 - ax^2 + bx + c) = x^4 - a x^3 + b x^2 + c x + x^3 - a x^2 + b x + c$  
$= x^4 + (1-a)x^3 + (b-c+1?) no. $x^3(x+1)$ ...  

Standard polynomial long division:  

```text
             x^3 - 16x^2 + 5x + 20
           ----------------------
```

(x+1) goes into it?  
x^4 / x = x^3  
1. Multiply $x^3(x+1) = x^4 + x^3$.  
Subtract: $-17x^3 + ...$ No, I wrote the polynomial as $x^4 - 16x^2 + 5x + 20$. There is no $x^3$ term initially.  
So I have $x^4 + 0x^3 - 16x^2 + 5x + 20$.  


```text
             x^3
             -- ----------------
            0 | ...
```

(x+1) divides it?  

Let's re-calculate the remainder of $x^4 - 16x^2 + 5x + 20$ divided by $(x+1)$ at $x=-1$.  
$(-1)^4 - 16(-1)^2 + 5(-1) + 20 = 1 - 16 - 5 + 20 = 0$. Correct.  
Derivative check? No need.  

Synthetic division setup:  
Coeffs: $1, 0, -16, 5, 20$ (corresponding to powers 4, 3, 2, 1, 0)  
Root: -1  

Row 1:     1  
Row 2:   -1  
|        -1(1)*(-1)? No.  
Multiply $x^4$: $1 \cdot x^{-1}$?  

Let's just use the table:  
-1 | 1  0 -16  5  20  
|  -1   1  17  -20 ? No, calculation error.  

Calculation check:  
$(x+1)(-1) + ...$?  

$x^4$: coeff 1  
$x^3 \times (-1) + x^3(1) = 0$.  
Coeff of $x^3$ in quotient: -1. No, root is -1, so multiply by -1.  
$1 \times -1 = -1$. Bring down next term? No.  

Let's do it properly.  
$x^4$: 1  
Root $r = -1$.  
Coeffs: $1, 0, -16, 5, 20$.  

Step 1: $1 \times r = -1$. Subtract from next coeff (which is 0). So $(0) - (-1) = +1$? No.  
The operation is to take current value * (root). Then subtract from next coefficient.  
Current val: 1. Next coeff: 0.  
$1 \times (-1) = -1$. Add to 0? No, usually we write down "next".  

Let's use: $a_n x^n + a_{n-1} x^{n-1} + ...$  
Row 1: 1, 0, -16, 5, 20  
Row 2 (-1): -1.  
Subtract Row 1 * (root) from next term?  

Let's write out $(x+1)(x^3 + Ax^2 + Bx + C) = x^4 + x(x^3 + Ax^2 + Bx + C) + x^3 + Ax^2 + Bx + C$  
$= x^4 + (A+1)x^3 + (B+A)x^2 + (C+B)x + C$?  

Let's look at the expansion again carefully.  
$(x+1)(Ax^3 + Bx^2 + Cx + D)$  
$= Ax^4 + Bx^3 + Cx^2 + Dx + Ax^3 + Bx^2 + Cx + D$  
$= Ax^4 + (A+B)x^3 + (B+C)x^2 + (C+D)x + D$.  

Match coefficients with $1x^4 + 0x^3 - 16x^2 + 5x + 20$.  
A = 1\.  
$A+B = 0 \implies B = -1$.  
$B+C = -16 \implies -1 + C = -16 \implies C = -15$.  
$C+D = 5 \implies -15 + D = 5 \implies D = 20$.  
Check last term: $D=20$. Matches constant term.  

So the quotient is $x^3 - x^2 - 15x + 20$.  
The equation becomes $(x+1)(x^3 - x^2 - 15x + 20) = 0$.  

*   **Finding roots of $x^3 - x^2 - 15x + 20 = 0$.**  
Let $P(x) = x^3 - x^2 - 15x + 20$.  
Test rational roots: $\pm 1, \pm 2, \pm 4, \pm 5, \pm 10, \pm 20$.  

$x=1$: $1 - 1 - 15 + 20 = 5 \neq 0$.  
$x=-1$: $-1 - 1 + 15 + 20 = 33 \neq 0$. (Checked earlier, but that was for the quadratic).  

Test $x=2$: $8 - 4 - 30 + 20 = -6 \neq 0$.  
Test $x=-2$: $-8 - 4 + 30 + 20 = 38 \neq 0$.  

Let's check the equation again. Maybe I made a calculation error earlier.  
Equation was $(x^2 - 8)^2 = -5x + 44$.  
LHS: $x^4 - 16x^2 + 64$.  
RHS: $-5x + 44$.  
Eq: $x^4 - 16x^2 + 64 = -5x + 44$.  
Move RHS to LHS: $x^4 - 16x^2 + 5x + 20 = 0$.  

Let's re-test roots for $P(x) = x^3 - x^2 - 15x + 20$.  
Is there a rational root?  
Possible denominators are factors of 20: $\pm 1, \pm 2, \pm 4, \pm 5, \pm 10, \pm 20$.  
Possible numerators 1. So integers only.  

$x=2$: $8 - 4 - 30 + 20 = -6$.  
$x=-2$: $-8 - 4 + 30 + 20 = 38$.  
$x=5$: $125 - 25 - 75 + 20 = 45 \neq 0$.  
$x=-5$: $-125 - 25 + 75 + 20 = -55 \neq 0$.  

Did I make a mistake in the polynomial expansion or derivation?  
Let's check intersection points visually or logically.  
Curve 1: $y = x^2 - 8$. Vertex $(0, -8)$. Passes through $(4, 0)$ and $(3, 1)$? No, $3^2-8 = 1$. $4^2-8 = 8$.  
Curve 2: $y^2 + 5x - 44 = 0$.  

At $x=-1$: $y = (-1)^2 - 8 = 1 - 8 = -7$.  
Check second eq: $(-7)^2 = 49$. RHS: $-5(-1) + 44 = 5 + 44 = 49$.  
It works! So $(-1, -7)$ is a solution.  

Let's check roots of $x^3 - x^2 - 15x + 20 = 0$ again?  
I missed something?  
Is it possible that the polynomial I derived is $(x+1)(x^2 ...)$ was wrong or I made a mistake checking roots.  

Let's re-calculate $x=4$: $y = 4^2-8 = 8$. $y^2 = 64$.  
Eq: $64 = -5(4) + 44 = 49$? No.  
$x=-2$: $y = 4-8 = -4$. $y^2 = 16$.  
Eq: $16 = -5(-2) + 44 = 10 + 44 = 54$? No.  

Let's re-evaluate my polynomial derivation carefully.  
$y = x^2-8$  
$y^2 = (x^2-8)^2 = x^4 - 16x^2 + 64$.  
Eq: $x^4 - 16x^2 + 64 = -5x + 44$.  
$x^4 - 16x^2 + 5x + 20 = 0$.  

This looks correct.  
Factorization attempt: $(x+1)(x^3 - x^2 - 15x + 20)$.  
Let's check the constant term of the cubic. $1 \cdot 20 = 20$. Correct.  
Sum of coefficients for $x^4$: 1. Correct.  

Let's re-verify the roots of $x^3 - x^2 - 15x + 20$.  
I tested $\pm 1, \pm 2$. None worked.  
Is it possible that the cubic has no rational roots? It might have 3 irrational roots.  

Let's look at the equation $y^2 = -5x + 44$ again.  
Since we need distinct solutions $(x,y)$, maybe I should solve for y directly or check for complex roots (but usually these problems imply real solutions).  
If the problem asks for "product of the y-coordinates", and assuming distinct solutions are just pairs on the intersection points.  

Is there a way to factor the quartic differently?  
Let's re-read the prompt. Maybe I made a mistake in reading the equations.  
$y=x^2-8$.  
$y^2=-5x+44$.  

Let's try factoring by grouping on $x^3 - x^2 - 15x + 20$.  
Group: $(x^3 - x^2) - (15x - 20)$? No, signs.  
$x^2(x-1) - 5(3x - 4)$. Doesn't help much.  

Try grouping: $(x^3 + a)x - (x^2 + b) ...$ no.  
Maybe factor as $(x+5)(...) + ...$  

Is there an error in the constant term calculation?  
$y=x^2-8 \implies y^2 = x^4 - 16x^2 + 64$.  
$-5x+44$.  
$x^4 - 16x^2 + 64 - (-5x + 44) = x^4 - 16x^2 + 64 + 5x - 44 = x^4 - 16x^2 + 5x + 20$. Correct.  

Let's re-test the cubic roots.  
$P(1) = 5$  
$P(-1) = 33$  
$P(2) = -6$  
$P(-2) = 38$  
$P(4)$: $64 - 16 - 60 + 20 = 8$. (Since $P(x)$ corresponds to roots of quartic).  
Let's evaluate the cubic at specific points.  
Maybe I copied the coefficients wrong?  
$x^4 - 16x^2 + 5x + 20 = 0$.  

Is it possible that there is a calculation error in $P(x) / (x+1)$?  
$(x+1)(x^3 - x^2 + Cx + D)$.  
Expand: $x^4 - x^3 + Cx^2 + Dx + x^3 - x^2 + Cx + D = x^4 + (C-1)x^3 + (C+D)x^2$? No.  

Expansion check: $(x+1)(x^3 + Bx^2 + Cx + D)$  
$= x(x^3) + x(Bx^2) + x(Cx) + x(D) + 1(x^3) + 1(Bx^2) + 1(Cx) + D$  
$= x^4 + Bx^3 + Cx^2 + Dx + x^3 + Bx^2 + Cx + D$  
$= x^4 + (B+1)x^3 + (C+B)x^2 + (D+C)x + D$.  

We want to match $x^4 - 16x^2 + 5x + 20$.  
Coeff of $x^3$: $B+1 = 0 \implies B=-1$.  
Coeff of $x^2$: $C+B = -16 \implies C-1 = -16 \implies C=-15$.  
Coeff of $x$: $D+C = 5 \implies D-15 = 5 \implies D=20$.  
Constant: $D = 20$.  

So the cubic is $x^3 - x^2 - 15x + 20$ (with B=-1). Correct.  
So my factorization and coefficients are correct.  
Roots of $x^3 - x^2 - 15x + 20$:  
Let's check if there is a typo in my manual root finding.  
Let's check $x=4$ again: $64 - 16 - 60 + 20 = 8$.  
$P(3)$: $27 - 9 - 45 + 20 = -7$.  
$P(2)$: $8 - 4 - 30 + 20 = -6$.  
$P(-1)$ was checked.  
Let's check for $x=-2$: $-8 - 4 + 30 + 20 \neq 0$.  

Is it possible that I missed a factor or solution?  
The roots of $x^4 - 16x^2 + 5x + 20 = 0$ are the x-coordinates.  
Are they all real?  
Let's analyze $P(x) = x^3 - x^2 - 15x + 20$.  
Derivative: $3x^2 - 2x - 15$.  
Roots of derivative: $\frac{2 \pm \sqrt{4 + 180}}{6} = \frac{2 \pm 14}{6}$ or $\frac{-16}{6}$.  
$\delta_1 = 1.6\approx 1.6$, $\delta_2 \approx -3$.  

Local max at $x \approx -3$. Local min at $x \approx 1.6$.  
Let's check values:  
$P(-4) = -64 - 16 + 60 + 20 = 0$.  
**BINGO**.  

I calculated $P(-4)$ incorrectly earlier or missed it.  
Let me recompute carefully.  
$x = -4$.  
$x^3 = (-4)^3 = -64$.  
$-x^2 = -16$.  
$-15x = -15(-4) = 60$.  
$+20 = 20$.  
Sum: $-64 - 16 + 60 + 20 = -80 + 80 = 0$.  

So $x = -4$ is a root.  
Since I found $x=-4$, then the polynomial factors by $(x+4)$? Or $(x-(-4))$ so $(x+4)$.  
Let's re-divide the quartic by $(x+1)(x+4)$ to find the remaining factor.  
Quartic: $x^4 - 16x^2 + 5x + 20$.  
Roots so far: $-1, -4$.  

Polynomial division of $x^4 - 16x^2 + 5x + 20$ by $(x+1)$.  
I got quotient $x^3 - x^2 - 15x + 20$.  
Let's divide this cubic by $(x+4)$.  
$x^3 - x^2 - 15x + 20 \div (x+4)$.  

-1 | ? No, root is -4.  

Coeffs: 1, -1, -15, 20.  
Bring down 1.  
Multiply by -4: -4. Add to next (-1): -5.  
Multiply by -4: 20. Add to next (-15): 5.  
Multiply by -4: -20. Add to last (20): 0.  

So the cubic factors into $(x+4)(x^2 - 5x + 5)$.  
Thus, the full polynomial factors as $(x+1)(x+4)(x^2 - 5x + 5)$.  
The roots for $x$ are $-1$, $-4$, and solutions to $x^2 - 5x + 5 = 0$.  

Let's solve the quadratic $x^2 - 5x + 5 = 0$.  
Discriminant $\Delta = 25 - 4(1)(5) = 5 > 0$.  
Roots: $x = \frac{5 \pm \sqrt{5}}{2}$.  

So the set of x-coordinates is $\{-1, -4, \frac{5+\sqrt{5}}{2}, \frac{5-\sqrt{5}}{2}\}$.  

*   **Find y-coordinates:**  
We have $y = x^2 - 8$ for each distinct solution.  
Let's calculate $y$ for each root.  

Case 1: $x_1 = -1$.  
$y_1 = (-1)^2 - 8 = 1 - 8 = -7$.  

Case 2: $x_2 = -4$.  
$y_2 = (-4)^2 - 8 = 16 - 8 = 8$.  

Case 3: $x_{3} = \frac{5+\sqrt{5}}{2}$.  
$y_3 = x_3^2 - 8$.  
From the quadratic equation $x^2 - 5x + 5 = 0$, we have $x^2 = 5x - 5$.  
So, $y_3 = (5x_3 - 5) - 8 = 5x_3 - 13$.  
Or just substitute directly to check the value.  
Since we need the product of $y$'s.  
Let $Y$ be the set of y-coordinates: $\{-7, 8, y_{x_{roots}}, y_{x_{other}}\}$.  

We need to find the values $y_3$ and $y_4$.  
Note that $y^2 = -5x + 44$. This gives a positive value for $y^2$ but implies $y = \pm \sqrt{...}$ if we were solving for y.  
However, the question asks for solutions to the *system*. The system is defined by $(1)$ and $(2)$.  
For each x root found (from intersection), there are potentially two y values? No.  
Equation 1 defines $y = x^2-8$. It's a function. So for any x, there is exactly one y satisfying Eq 1.  
This y must also satisfy Eq 2.  
The condition $(x^2-8)^2 = -5x + 44$ is derived from substituting $y$ from (1) into (2).  
So if $x$ satisfies this equation, the point $(x, x^2-8)$ lies on both curves?  
Let's verify.  
Point $P(x, y)$ with $y=x^2-8$.  
Substituting into Eq 1: $y = x^2-8$. True by definition.  
Substituting into Eq 2: $y^2 = -5x+44$. LHS is $(x^2-8)^2$. RHS is given as $-5x+44$.  
So yes, if $x$ satisfies the quartic, the pair $(x, x^2-8)$ satisfies both.  

However, could there be a case where the intersection includes points that are not on $y=x^2-8$?  
No, because the solution set of the system must satisfy both equations simultaneously. Since Eq 1 is $y = x^2-8$, any solution must lie on this parabola.  

Are there solutions $(x,y)$ that don't satisfy the derivation I used?  
Derivation:  
We found $x$ such that $(x^2-8)^2 = -5x+44$. This means that for these $x$, the value $y=x^2-8$ makes Eq 2 true.  
So yes, finding roots of this quartic gives all intersection points.  

What about "distinct solutions"? The x-coordinates are distinct real numbers?  
Discriminant was positive, so $x^2 - 5x + 5 = 0$ has two distinct roots $\frac{5 \pm \sqrt{5}}{2}$.  
Are there any other constraints?  
Let's check the range of x.  
From Eq 2: $y^2 = -5x+44$. Since $y^2 \ge 0$, we need $-5x + 44 \ge 0$, so $x \le 8.8$.  
All my roots satisfy this?  
$-1 < 8.8$ (yes)  
$-4 < 8.8$ (yes)  
$\frac{5+\sqrt{5}}{2} \approx (5+2.236)/2 = 3.6$. (yes)  
$\frac{5-\sqrt{5}}{2} \approx (5-2.236)/2 = 1.38$. (yes)  

So all derived roots are valid.  

Now, the y-coordinates are $y_1, y_2, y_3, y_4$.  
Are $y_1$ and $y_2$ distinct? Yes: $-7 \neq 8$.  
Are $y_3, y_4$ distinct from each other and the previous ones?  
Let's check.  
The $y$ values are derived from $x$. Since the function $f(x) = x^2-8$ is injective (one-to-one) only in a restricted sense? No, it's not one-to-one globally?  
It maps $\mathbb{R} \to [-\infty, -1]$ to $\dots$ no. $x \to -\infty$, $y \to \infty$. $x \to -8$, $y=0$. No, vertex is $(0,-8)$.  
The function $x^2-8$ is strictly increasing for $x>0$ and strictly decreasing for $x<0$.  
So it takes the value of each x once. Thus for any distinct real x, $y_1 \neq y_2$ is guaranteed if we find distinct x's? Not quite. If x1 != x2, then $(x1^2-8)$ and $(x2^2-8)$ are just values on the curve.  
Since the curves are different functions ($y=x^2-8$ vs $y=\pm \sqrt{-5x+44}$), they intersect at specific points.  
But Eq 1 says $y = x^2 - 8$. It doesn't say $y = \sqrt{\dots}$. It restricts y to the parabola.  
So  

## Answer

*(none: the token cap hit during thinking)*
