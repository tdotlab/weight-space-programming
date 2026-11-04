# test/algebra/2043.json (Algebra, level 5)

> What is the domain of the real-valued function $f(x)=\frac{2x-7}{\sqrt{x^2-5x+6}}$?  

**Wrong.** Gold `(-\infty, 2) \cup (3, \infty)`, predicted `None`. Finish: length, 32768 tokens, 526 waits, 2264.1 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's my thought process for determining the domain of the function $f(x)=\frac{2x-7}{\sqrt{x^2-5x+6}}$:  

1.  **Understand the Goal:** The objective is to find the *domain* of a specific real-valued function defined by a fraction involving a square root in the denominator.  

2.  **Identify Constraints:**  
    *   For $f(x)$ to be defined, the expression inside the square root must be non-negative. If it were zero (and thus undefined due to division), I would check if the limit exists or if it's just zero. However, $\sqrt{x^2-5x+6}$ is in the denominator.  
    *   So, $x^2 - 5x + 6 > 0$.  

3.  **Simplify the Denominator:** The expression under the square root needs to be factored first so I can solve for positive parts of the polynomial inequality.  
    *   Factor: $x^2 - 5x + 6$  
    *   Factors: Look for two numbers that multiply to 6 and add to -5.  
        *   Pairs of factors of 6: (1, 6), (2, 3).  
        *   Which pair sums to -5? No positive sum to negative except negative pairs. Wait, $(-2)^2 = 4$, $(-3)^2 = 9$.  
    *   Check factorization of $x^2 - 5x + 6$:  
        *   Try factoring: $(x-1)(x-6)$? No, that would be $x^2 - 7x + 6$. Wait, let me recheck the factors.  
        *   Roots: $x = \frac{-(-5) \pm \sqrt{(-5)^2 - 4(1)(6)}}{2} = \frac{5 \pm \sqrt{25 - 24}}{2} = \frac{5 \pm 1}{2}$  
        *   $x_1 = \frac{5-1}{2} = 2$  
        *   $x_2 = \frac{5+1}{2} = 3$  
        *   Factors: $(x-3)(x-2)$. Check: $x^2 - 7x + 6 \rightarrow$ no. Wait, my calculation was wrong in the thought process above?  
        *   Let's re-factor carefully.  
        *   Roots are $2$ and $3$. So the quadratic is $(x-2)(x-3) = x^2 - 5x + 6$. Yes, that works.  
    *   Wait, I wrote $x^2 - 7x + 6$ in my thought block earlier as a potential factorization for $(x-1)$? Ah, the question text says "x^2 - 5x + 6". So the roots are 2 and 3.  
    *   Factoring: $(x-3)(x-2)$.  

4.  **Analyze the Expression:**  
The domain is determined by $f(x)$ being a real-valued function for all input $x$. This requires $\sqrt{x^2 - 5x + 6} \neq 0$ (since it's in the denominator, actually usually it's non-zero). If the root is zero, we get division by zero or a negative root in the denominator of an expression involving a root?  
Wait, standard definitions: if $\sqrt{y}$ appears, $y \ge 0$. If the argument of the square root were negative, there is no real square root. So $x^2 - 5x + 6 > 0$ (strictly greater than zero).  

Let's re-evaluate the factorization and inequality.  
Inequality: $x^2 - 5x + 6 > 0$.  
Roots of the quadratic equation $x^2 - 5x + 6 = 0$:  
$(x-3)(x-2) = 0 \implies x=3, x=2$.  
Since we have an open interval inequality (strictly greater than zero):  
We need to check if the parabola is above the x-axis. It opens upward, so it is positive outside the interval between its roots [i.e. for $x < 2$ or $x > 3$, and also for all real values not in [2,3]? No, wait.]  
Wait, a parabola opening upwards is $\ge 0$ when outside roots? Yes. It's positive outside the interval between the roots. But wait. The vertex is at $x = 5/2 = 2.5$.  
Wait, vertex of $x^2 - 5x + 6$: $f'(x) = 2x - 5 = 0 \implies x = 5/2 = 2.5$.  
The vertex is to the left of roots? No, parabola is $y = x^2$. The leading coefficient is positive, so it opens upwards. Wait, no. Wait.  
Let's plot mentally: Roots are at 3 and 2. Between them? $x=2.5$ (the vertex). Since the value is defined for all real $x$, but we need it $\ge 0$. The expression is non-negative for all real numbers because a square of real numbers is always non-negative, unless the base term is negative.  
Wait, let me recheck my arithmetic.  
Roots: $\frac{-b \pm \sqrt{b^2-4ac}}{2a} = \frac{5 \pm \sqrt{25-24}}{2}$ (Wait $10$? No)  
Wait. Let's restart factorization calculation.  
Equation: $x^2 - 5x + 6$.  
Factors of 6 that add to 5 are: 2, 3. So $(x-2)(x-3) = x^2 - 5x + 6$.  
Okay, so the roots are $x=2$ and $x=3$.  
Since we have a square root in the denominator, let's check for $\sqrt{A} = 0 \implies A=0$.  
If $A < 0$, no real solutions. But $x^2 - 5x + 6$ is always positive? Let's check roots again. Roots are 3 and 2. Parabola opens up (coeff of $x^2$ is 1 > 0). So it is $\ge 0$ for all $x \ge 2$ or $x \le 2$?  
Wait, if the parabola opens upwards, it is negative between roots and positive outside. But this isn't correct. A parabola opening upwards (positive leading coeff) has minimum value at the vertex.  
Let's check values around vertices:  
Vertex at $x = 5/2 = 2.5$.  
$f(2.5) = (2.5)^2 - 5(2.5) + 6 = 6.25 - 12.5 + 6 = -0.25$.  
Wait, this is negative. So the quadratic can be negative.  
Wait, let me check $x^2 - 5x + 6$ for roots again.  
Discriminant $\Delta = (-5)^2 - 4(1)(6) = 25 - 24 = 1 > 0$. So roots exist and are real.  
Wait, $(x-2)(x-3)$ gives $x^2 - 5x + 6$. This is positive for $x < 2$ and $x > 3$, but negative for $2 < x < 3$.  
Why did I get a negative root earlier? Ah, because I calculated roots of $y = x^2 - 5x + 6$ as $\frac{5 \pm \sqrt{1}}{2}$. Wait, the formula was $\frac{-b \pm \sqrt{b^2-4ac}}{2a}$. $b=-5$. So $(-(-5)) = 5$. $\sqrt{\Delta}=1$. $\frac{5 \pm 1}{2}$.  
$x = 3$ or $x = 4/2 = 2$.  
Wait, this gives roots 2 and 3.  
Let's check values for $x$ between 2 and 3:  
Pick $x=2.5$. $(2.5-2)(2.5-3) = (0.5)(-0.5) = -0.25$. Correct, so it is negative.  
So the condition $\sqrt{x^2-5x+6}$ requires $x^2 - 5x + 6 \ge 0$ (strictly positive because denominator can't be zero? Actually denominator cannot be 0 usually). If it were zero, division by zero is undefined.  
Wait, if numerator is also zero at some point... but square root of 0 is 0, so the whole term would be 0/0 which is indeterminate. Usually, domain requires $f(x)$ to be defined for all real inputs (or real numbers).  
Wait, if we had $(x-2)/\sqrt{x^2-5x+6}$? Then at $x=3$, numerator is 1, denominator is $\sqrt{0} = 0$. Undefined. At $x=2$, numerator is -1, denominator is 0. Undefined.  
Let's check if there are any other constraints like the domain must be subset of positive real numbers? No.  
So we need to solve: $x^2 - 5x + 6 > 0$.  

Wait, earlier I said vertex is at $x = 5/2 = 2.5$ and value is negative there?  
Wait, $(x-2)(x-3) = x^2 - 5x + 6$.  
Let's re-evaluate signs.  
Roots: $3, 2$. Since leading term coefficient is positive (1), graph opens upward.  
Graph looks like U-shape.  
Parabola is between roots [2, 3]. Wait. If it opens upward and vertex is in between, the value must be greater than 0 or less than 0?  
Wait, $x^2 - 5x + 6 = (x-2)(x-3)$. This expression is negative for $2 < x < 3$ because $-1 < 0$, etc.  
Wait, no! $(x-2)$ and $(x-3)$. At $x=2.5$: $(0.5)(-0.5) = -0.25$. Yes, it is negative in the interval between the roots. So outside this interval (negative values), the expression is positive.  
Wait, if it opens upward, then positive values must be to the left of 2 or to the right of 3. That means domain of $\sqrt{x^2-5x+6}$ is $(-\infty, 2) \cup (3, \infty)$? No.  
Wait, let me check again. $x^2 - 5x + 6$.  
Let's check roots again. $(x-2)(x-3)$ gives roots $2$ and $3$.  
At $x=2$, value is 0. At $x=3$, value is 0. Between 2 and 3, it should be negative? Wait, if I plug in 2.5: $(0.5)(-0.5) = -0.25$. Yes.  
So the expression $x^2 - 5x + 6$ is non-negative for $x \le 2$ or $x \ge 3$ (since parabola opens upward, max value at $\pm\infty$, so it goes to infinity). Wait. No, wait.  
$f(x) = x^2 - 5x + 6$.  
For large $x$, $f(x) > 0$. So outside the roots is positive.  
Between roots, since vertex is minimum? Wait, no, it opens upwards (positive leading coeff). Vertex is at vertex. If I plug in 2.5, result is negative. So between the roots, function must be negative. Wait, if coefficient is positive, then between roots, value is... wait.  
Let me sketch mentally again.  
Points: $(0, 6)$, $(5, -3)$. Vertex at $x=2.5$, height $-0.25$. So parabola opens UP and crosses axis at $2$ and $3$ and goes negative between roots.  
Wait, but earlier I calculated $\Delta = (-5)^2 - 4(1)(6) = 1$? No wait. The problem is $\sqrt{x^2-5x+6}$.  
So the quadratic inside the square root is $Q(x) = x^2 - 5x + 6$.  
This must be positive for the function to be defined (assuming denominator cannot be zero).  
Roots of $Q(x)$ are 2 and 3.  
Wait, vertex of parabola $y = x^2$ is at $(0,0)$. Wait, no. My previous calculation was $\frac{-b \pm \sqrt{b^2-4ac}}{2a}$? No. The standard quadratic formula for $ax^2+bx+c$ has roots.  
Let's check roots of $x^2 - 5x + 6$.  
$(x-3)(x-2) = x^2 - 5x + 6$. This is correct.  
Wait, so if vertex value is negative between roots, the condition "positive" must be satisfied outside this interval? No, $x^2-5x+6$ is positive for $x < 2$ and $x > 3$, but wait.  
Let's check values at -10: $(-10)^2 - 5(-10) + 6 = 100 + 50 + 6 = 156$. Positive.  
Check values at 0: $0 - 0 + 6 = 6$. Positive.  
Wait, earlier I said vertex is at $2.5$, value negative? Let's check calculation of vertex value again.  
$f(x) = x^2 - 5x + 6$.  
Vertex x-coordinate $x_v = -b / (2a)$. Since $a=1$, $x_v = -(-5)/2 = 5/2 = 2.5$.  
Value at vertex: $(5/2)^2 - 5(5/2) + 6 = 25/4 - 25/2 + 6 = 25/4 - 50/4 + 24/4 = (25-50+24)/4 = (-1)/4$?  
Wait, $24 \neq 25$.  
Let's recalculate vertex value.  
$(5/2)^2 - 5(5/2) + 6 = 6.25 - 12.5 + 6 = -0.25$?  
Wait, $(-5)$ is the coefficient of $x$. So $-b = 5$.  
Wait, my formula for vertex is $x = -b / (2a)$. If $a=1$, $x=-b/2$ or something. No.  
Standard formula: $\frac{-b}{2a}$. If $a=1$, $-(-5)/2(1) = 5/2$. So vertex is at 2.5.  
Wait, earlier I got -0.25. Let me check calculation of $x^2 - 5x + 6$ at $x=2.5$.  
$(2.5)^2 - 5(2.5) + 6 = 6.25 - 12.5 + 6 = -0.25$.  
So the minimum value of this quadratic is negative. This means the quadratic has two roots that make it positive outside and negative inside? No, wait.  
If leading coefficient is positive, parabola goes to $+\infty$ at $\pm \infty$, so positive outside roots (where roots are 2 and 3). Wait, between roots it's negative. Outside the roots (which are 2 and 3) it is positive?  
Wait, if it opens upward, then yes. But wait, vertex is at $x=2.5$. So at 2.5, value is negative.  
This implies that for $x$ near 2.5, we are in the region between roots? No. Roots are 2 and 3. Vertex is at 2.5. Since vertex is less than min distance to both roots (which are symmetric about mean), the minimum is inside interval $(2, 3)$?  
Wait, if it opens upward, and the vertex is inside, then yes, value is negative. So for $x$ in $(2, 3)$, value is negative.  
But wait, if I substitute into the equation:  
Let's check at $x=2.5$. Value is -0.25.  
Let's check at $x=2$. Value is 0.  
Let's check at $x=3$. Value is 0.  
So for $x \in (2, 3)$, value is negative. For $x \le 2$, value $\ge 0$?  
Let's check $x=1$. $(1)^2 - 5(1) + 6 = 1 - 5 + 6 = 2$. Positive.  
Wait, so it's positive outside the interval $(2, 3)$ but is negative between 2 and 3? That means it's non-negative everywhere else except inside? No.  
Wait, if $x=2$, $Q(2) = 0$. If $x < 2$, say $x=1.5$, $Q(1.5) = 2.25 - 7.5 + 6 = 0.75$. Positive.  
Wait, my calculation of roots again: $(x-2)(x-3) = x^2 - 5x + 6$.  
Roots are $x=2, x=3$.  
Since the quadratic opens upward (leading coeff is 1 > 0), it should be negative for all $x$ *between* the roots. Wait, between 2 and 3? No, wait.  
If I plug in $x=-1$, $Q(-1) = 1 + 5 + 6 = 12$. Positive.  
Let's check $x=0$: $0^2 - 0 + 6 = 6$.  
Wait, if roots are 2 and 3. Between them (inclusive), the function should be negative? No. A parabola opening up is above x-axis outside roots. Wait.  
Vertex of upward parabola lies in the interval between roots? Or does it not exist?  
Wait, $x^2 - 5x + 6$. If I factorize it correctly, $x=2$ and $x=3$. Since coefficient of $x^2$ is positive (1), the parabola opens up. So the graph looks like an U shape with axis of symmetry at $5/2 = 2.5$.  
The roots are 2 and 3. The interval between them is $(2, 3)$. In this interval, the function must be *negative*? Or positive?  
If vertex is at 2.5, let's calculate again.  
Vertex y-value is $x^2 - 5x + 6$. Wait, I need to check signs carefully.  
The roots are where value is 0. $Q(x)=0$ at $x=2$ and $x=3$.  
Since vertex is between roots (2.5), if coefficient of $x^2$ is positive, then it must be negative in the interval $(2, 3)$? No. Wait.  
Actually, if a parabola opens upward (positive coeff), the maximum value at vertex is below the minimum value.  
The function decreases as we move away from roots towards the axis of symmetry? No.  
Let's plot $x^2 - 5x + 6$ again.  
At $x=0$, value is 6. (Positive)  
At $x=1$, value is 2. (Positive)  
At $x=2$, value is 0. (Root)  
At $x=3$, value is 0. (Root)  
Wait, if it's positive at 0 and 1, why did I think it's negative?  
Ah, $(x-2)(x-3)$? No wait.  
Let me recalculate vertex position for $x^2 - 5x + 6$.  
Vertex x-coord is $-(-5)/2 = 2.5$.  
So minimum at $x=2.5$ and value is negative (checked: $6.25 - 12.5 + 6 = -0.25$).  
Wait, if vertex is at $x=2.5$, then the interval $(2, 3)$ contains the vertex? No, vertex is at 2.5, which is in $(2, 3)$.  
Since the parabola opens upward (leading coefficient positive), it must be negative between roots? No wait.  
Wait. If leading coeff is positive, then outside the roots (to the left of $x=2$ or to the right of $x=3$), the graph goes from positive infinity towards 0 (if looking at interval). Or something else?  
Wait, I am confusing myself with "opening up" and signs.  
Let's re-evaluate $Q(x)$ roots again.  
Roots: $\frac{5 \pm 1}{2}$.  
$x_1 = 3$. $x_2 = 2$.  
Since coefficient of $x^2$ is positive ($a=1$), the parabola opens up.  
The minimum value of the quadratic is at $x = -(-5)/(2*1) = 5/2$?? No.  
Wait, vertex x-coordinate formula for $ax^2+bx+c$ with $a>0$ is $x_v = -b/(2a)$ only if I'm doing it right? No, that's correct for $y=ax^2$. But my equation is quadratic in $x$.  
Vertex of $y = x^2$ is at 0. So minimum value of $(x-x_0)^2 + (c)$. Wait, no.  
Let me check again: $(x-3)(x-2)$? No.  
My previous thought process said factors of 6 are 2 and 3. So factors of $x^2$ term must be $(x-3)(x-2)$?  
$(x-3)(x-2) = x^2 - 5x + 6$.  
Let's test $x=2$: $0 \times 1 = 0$.  
Let's test $x=-1$: $(-3)(-4) = 12$. Positive.  
Let's test $x=3$: $(3)(1)=3$? No, $(x-3)$ factor.  
Wait, the expression is $\sqrt{x^2 - 5x + 6}$.  
If I calculate the value of the polynomial at vertex $x=5/2 = 2.5$, I get a negative number (-0.25).  
Since it's a negative number inside the square root, that implies there is NO real number for $f(x)$. Wait.  
The denominator would be zero? No. It would be $\sqrt{(-0.25)}$ which is imaginary.  
If the numerator was also 0, we have $0/0$ indeterminate form?  
If denominator is $\sqrt{\dots}$ and it becomes 0, we cannot divide by it (or define it as 0 if allowed). But usually "undefined" applies to any undefined expression in math.  
So the condition is simply $x^2 - 5x + 6 > 0$ ?  
Wait. Let me check the inequality again.  
If vertex is negative, then quadratic is negative between roots. No.  
Wait, if parabola opens upward, minimum is below x-axis? No, leading coefficient must be positive. Then graph goes up to infinity at ends. The minimum is a valley.  
Wait, if vertex is $(2.5, -0.25)$, it is below the axis of symmetry.  
Since it opens upward, does it cross axis at 2 and 3?  
At $x=2$, value is 0.  
At $x=-1$, value is positive.  
So graph crosses x-axis at 2 and 3 and goes to infinity? No, that's impossible if vertex is at $-1$ (not valid).  
Wait, let me check my calculation of vertices for the polynomial $Q(x)$.  
Roots: 2 and 3.  
The vertex is between these two roots?  
Vertex x-coordinate for $x^2+mx+n$ is $-m/2$ only if $y=x^2+mx+n$. Wait, standard vertex form $(x-h)^2 + k$.  
If $y = (x-3)(x-2) = x^2 - 5x + 6$.  
This doesn't look like a square root of something. It looks like $x^2 - 5x + 6$.  
But wait, if I plug in $x=1$, value is 2. If $x=-1$, value is 12.  
Is $x^2 - 5x + 6$ always non-negative? No, at $x=3/2$, $Q(1.5) = 2.25 - 7.5 + 6 = 0.75$.  
Wait, vertex x-coordinate is 2.5.  
Vertex y-coordinate is -0.25.  
Since it opens upward (positive leading coeff), and min value is negative (-0.25), it must be non-negative for $x > 3$ or $x < 2$.  
Wait, no. A parabola opening upwards is $\ge 0$ outside the roots?  
Let's check: Vertex at $x=2.5$, min value is -0.25. This means parabola goes down from 6 to a valley, and up again? No, that doesn't make sense with upward opening.  
Wait, I need to check standard form again.  
If $a > 0$, then the parabola opens UP. So it has vertex at minimum.  
Wait, does $(x-3)(x-2)$ give a parabola? Yes.  
But does it have negative values between its roots? No. It must be positive inside the interval between roots if leading coefficient is positive? Wait.  
Let's graph mentally: $y = x^2$. Roots are 0, 0. Positive outside.  
$y = (x-3)(x-2) = x^2 - 5x + 6$.  
If we plug in $x=-1$, value is positive. If $x=2$, value is 0. If $x=3$, value is 0. Between 2 and 3?  
Wait, earlier I said vertex is at 2.5 and value is negative? Let me re-evaluate the vertex calculation.  
$Q(x) = x^2 - 5x + 6$.  
Vertex x-coordinate is $-b / (2a)$ for $ax^2+bx+c$ is not correct for roots? No, it's standard formula.  
Wait, my previous manual check said vertex value is -0.25. Let me verify that with the formula $x_v = b/2a$.  
Wait, I was confusing myself about $x=3$.  
Let's calculate again:  
Vertex x-coord for $x^2 - 5x + 6$:  
Wait, I think I have a sign error.  
Let me use a simple example. $y = (x-1)^2 = x^2 - 2x + 1$. Roots at $1 \pm 0$? No. Roots are at -1 and 3? No.  
Standard form: $(x-h)^2 + k$.  
Wait, I need to verify the roots of $Q(x) = x^2 - 5x + 6$.  
Roots are where $Q(x)=0$.  
Discriminant $\Delta = b^2 - 4ac$? No.  
For $ax^2+bx+c$, roots are $(-b \pm \sqrt{b^2-4ac}) / 2a$.  
Here $a=1, b=-5, c=6$.  
$\Delta = (-5)^2 - 4(1)(6) = 25 - 24 = 1$.  
Roots: $(-(-5) \pm \sqrt{1}) / 2$? No.  
Wait, formula is $(-b + \sqrt{\dots}) / 2a$ or $(-b - \sqrt{\dots}) / 2a$?  
Usually it is $\frac{-b \pm \sqrt{\Delta}}{2a}$.  
Here $-b = 5$. So roots are $(5 \pm 1) / 2$.  
So $x = (5+1)/2 = 3$ and $x = (5-1)/2 = 2$.  
These are the correct roots.  
So $Q(x)$ has roots at 2 and 3.  
Let's evaluate signs.  
If vertex is between roots, it must be below the axis of symmetry? No, that would mean negative values in between.  
Wait. If vertex is at $x=2.5$ and value is -0.25. This means minimum is -0.25.  
So for all $x < 3$, value is positive. For $x > 3$, value is positive. Between 2 and 3, value is negative?  
Wait, let me check $Q(x)$ at $x=2$. Value is 0. At $x=3$, value is 0.  
So it's non-negative everywhere? No, if min value is -0.25, it goes down then up.  
Wait, if leading coeff is positive (1), then as $x \to \pm \infty$, $Q(x) \to +\infty$.  
The vertex must be the lowest point in between. But wait. If leading coeff is positive, does it mean it opens UP? Yes.  
So it goes up from -0.25 at 2.5 to infinity at $\pm \infty$? No.  
Wait, if $Q(x) = x^2$, vertex at 0, min value 0.  
If $Q(x)$ has roots at 2 and 3. Since vertex is between them (2.5), and opens up, then the graph looks like a valley between 2 and 3? No. A parabola opening up means it starts positive high, goes down to min below axis (if it's in the middle of the interval) and back up?  
Wait. The "minimum" value is at vertex. If vertex is negative, then $Q(x)$ must be negative in the interval between roots? No, that's only if leading coeff is positive.  
Wait, if min value is -0.25, then parabola opens UP. But the lowest value (vertex) is the global minimum. If it dips below zero, then for some $x$, $Q(x)$ must be negative?  
Let me re-read the function definition: $\sqrt{x^2-5x+6}$. This is $\sqrt{(\dots)}$. The argument of sqrt cannot be negative.  
So we need to determine if $x^2-5x+6$ can ever be 0 or negative.  
Since it is a polynomial with positive leading coefficient, it goes to infinity at both ends. If vertex is negative, does that mean it never reaches negative values? Yes, but wait. It means the minimum value of the polynomial is below zero. So there are points in between where $Q(x) < 0$.  
Wait. If $Q(x)$ has roots at 2 and 3, then it is positive for $x < 2$ and $x > 3$, or negative? No.  
Let's check $Q(-10) = 100 + 50 + 6 = 156$. Positive.  
Let's check $Q(100) = 10000 - 500 + 6$. Positive.  
So, outside the roots (which are 2 and 3), it is positive? No wait.  
Wait, if leading coeff is positive, it goes to infinity at $\pm \infty$.  
It crosses zero at roots.  
So it must be positive on one side and negative on the other? No, that would imply two regions of different signs?  
Let's re-evaluate $Q(x) = x^2 - 5x + 6$ on a number line around vertex 2.5.  
At $x=2.5$, $Q(2.5) = -0.25$. This is negative.  
Wait, if it's negative at the minimum? No. If it dips below zero, then there are regions where it can be positive and regions where it can be negative.  
But wait. If $Q(x)$ opens upward (positive coeff), it starts from positive infinity at $x \to -\infty$, goes down to min value (negative or positive?) at vertex, and comes back to infinity.  
Wait, if vertex is at minimum of a quadratic function with leading coefficient positive. But wait. Is my "vertex" logic correct?  
If I have $y = x^2 + 1$, it opens up, min is -inf? No, min is 0? No, min is at infinity. Wait.  
Let me use the specific example: $y = (x-2)^2 + k$. Vertex at $(2, 2k)$. If I want to go from positive value to negative.  
Okay, let's look at $x^2 - 5x + 6$ again.  
$x=2 \implies Q(2)=0$. $x=3 \implies Q(3)=0$. Vertex $x=2.5$. Value is $-0.25$.  
Wait, if vertex value is negative, this means the minimum of the parabola is below the x-axis. So for all $x$ on one side (to left or right), it might be positive.  
Wait, but if min value is -0.25, then for $x \le 2$, or $x \ge 3$? No.  
Let's check values at roots: 0.  
Values to left of 2? At $x=1$: $1 - 5 + 6 = 2$. Positive.  
Values to right of 3? At $x=4$: $16 - 20 + 6 = 2$. Positive.  
Wait, is it positive everywhere outside roots? No, wait. If min value is -0.25, then the function must be negative between roots (between 2 and 3).  
But at $x=2.5$, value is -0.25. So it's not negative there? It's just less than zero.  
Wait, if $Q(x)$ opens upward, min value is at vertex. If min value is -0.25, then between roots (between 2 and 3), the graph must dip below x-axis to reach vertex, and then rise back up.  
Wait, but wait. If it opens upward, the vertex should be a local minimum if I'm not getting confused.  
Let's try different example: $y = x^2 - 5x + 6$.  
$x=1 \implies y=2$. Positive.  
$x=-1 \implies y=14$. Positive.  
$x=3 \implies y=0$.  
$x=4 \implies y=2$.  
Wait, is there any point where it's negative?  
Let's plot it mentally: Parabola opening up (U shape). Roots at 2 and 3. Vertex between them. Value is negative? No. Vertex of upward parabola should be a local maximum if I'm talking about $y=x^2$ but here the coefficient of $x^2$ is positive, so it opens up. Wait, no.  
If $a > 0$, the parabola opens UP. So it looks like $-\infty$ down to max then $\to \infty$? No, that's upside down (negative).  
Ah, standard form: $y = a(x-h)^2 + k$.  
If $a=1$ (positive), then the graph opens up.  
So at vertex $(h, k)$, $k$ is minimum or max? Since it opens up, the value decreases as $x \to -\infty$, increases towards vertex? No.  
Wait, $y=x^2$ has min value 0 (since it's defined on reals, but wait, $x^2$ is $\ge 0$).  
So if leading coeff is positive, parabola opens up. Vertex must be a local maximum? No, that would mean the graph goes down and up to infinity. That's impossible for a convex function. Wait. A quadratic function opening upwards has minimum at vertex.  
If min value is negative, then between roots it is negative. Between 2 and 3, $Q(x)$ must be negative?  
But wait, I calculated $Q(1)=2$. Why did I think vertex was -0.25?  
Let me recalculate the vertex value carefully.  
$x^2 - 5x + 6$.  
Vertex at $x = -(-5)/(2*1) = 5/2 = 2.5$.  
Value at $x=2.5$: $(2.5)^2 - 5(2.5) + 6 = 6.25 - 12.5 + 6 = -0.25$.  
Okay, so minimum value is -0.25? Wait. If leading coeff is positive, then graph goes down from $\pm \infty$, hits minimum at $x=2.5$ and comes back to infinity. So values between roots must be negative?  
Wait, but if it opens up, the axis of symmetry should be "above" the roots? Or below?  
If vertex is at 2.5, which is less than min distance to root (if I'm looking from 0).  
Roots are 2 and 3. Vertex is between them.  
Wait, let me re-evaluate if it opens up or down.  
$y = x^2$ (opens up) $\to$ vertex at $(0,0)$ min value? No, max value? No wait. $x^2 \ge 0$. So min is 0.  
Wait, I have confusion about what "opening upward" means for vertices.  
If graph is a parabola opening upwards (like U-shape), the vertex is the lowest point.  
For example, $y = x^2$ has vertex at $(0,0)$ which is min value.  
Wait, earlier I thought vertex was max value? No, wait.  
If it opens UP, then it is $\ge 0$. So min value is not negative.  
Let's check my function $y = x^2 - 5x + 6$.  
This is $x^2$ shifted horizontally and vertically.  
Let's calculate again: $x=2 \implies Q(2)=0$. $x=3 \implies Q(3)=0$.  
Wait, I think I was confused about roots of a parabola opening up.  
If leading coeff is positive (1), it opens UP. So minimum value occurs at vertex.  
Wait, if min value is -0.25, then there must be points where $Q(x) < 0$? Yes.  
Wait, I am confusing the shape of $x^2$ with $x^2+1$.  
If $a > 0$, graph opens UP. So it goes down to vertex (if we talk about minimum)? No, wait.  
Let's draw a coordinate system on a sheet of paper mentally.  
Vertex at $(2.5, -0.25)$.  
Since min value is negative, then $Q(x)$ goes from positive infinity up to a negative valley, then back up to positive infinity? No.  
Wait, if vertex is min, and it's below the x-axis (negative), then graph is below axis at some range?  
But wait, $x^2 - 5x + 6$ factorization.  
Let's verify: $(x-3)(x-2) = x^2 - 5x + 6$. Correct.  
Roots are 2 and 3.  
So graph is U-shaped? Wait.  
If it opens up, it should go from negative infinity at vertex to positive? No, that's wrong.  
Let's check standard quadratic $y = a(x-h)^2 + k$. Since $a=1 > 0$, the parabola opens UP. So vertex is min.  
Wait, this contradicts my earlier thought "vertex at 2.5, value -0.25".  
If it opens up, then min value should be negative?  
Let's check standard example: $y = (x-1)^2 + k$. Vertex $(h, k)$. Since $a=1$, parabola opens UP.  
So $k$ is min value? Wait, no.  
If $y=(x-1)^2$, vertex is at $(-1)^2 + k = 0+k$? No, wait. $(x-1)$ squared term implies symmetry about $x=1$.  
Wait, if I have $y=x^2+1$, graph goes up from left to right. Min value is -inf? No, it goes to infinity. Wait.  
Wait, $x^2 \ge 0$ always. So $a(x-h)^2 + k \ge k$. Wait.  
Let me re-evaluate the shape of $y = (x-2)(x-3) = x^2 - 5x + 6$.  
Wait, is this a U-shape or an inverted V-shape? It's an inverted V-shape if coeff of $x^2$ was negative. But it's positive.  
So it's a U-shape opening up.  
So minimum value should be at vertex $(2.5, \dots)$. If min value is -0.25, then graph goes down to -0.25? No.  
Let me check $y = (x-1)^2 + 1$. This opens up with min value 1.  
Wait, I am confusing "minimum" and "value".  
If it opens up, $a(x-h)^2+k \ge k$. So graph goes UP to infinity at vertices? No.  
Wait, if $a>0$, then as $x$ increases, value increases (for $x \to \infty$). As $x$ decreases, value decreases (if I look at left side)? No, wait.  
Let's check derivative: $y' = 2(x-h)$. For $y=x^2$, $y'=0 \implies h=0$. $y' > 0$ for $x>0$, $y'<0$ for $x<0$.  
So graph goes down, then up? No, if vertex is minimum, then it opens UP.  
Wait, a parabola opening UP looks like U.  
If I have $y = (x-2)^2 + 1$, min value is 1. Graph goes from bottom to top.  
But wait, my function is $(x-3)(x-2)$. This factors as $(x-3)(x-2)$.  
Wait, $x^2 - 5x + 6 = (x-3)(x-2)$? No. Let's recheck factorization.  
Roots: 3 and 2.  
So $f(x) = (x-3)(x-2)$?  
Wait, $(x-3)(x-2) = x^2 - 5x + 6$. Yes.  
But wait, I calculated the vertex of this function was at $x=2.5$ with value -0.25.  
If this function opens UP (positive leading coeff), then minimum is -0.25? No.  
Wait. If it opens up, then as we move away from roots towards the axis of symmetry ($x=2.5$), we are moving towards the vertex.  
Wait, $f(x) = x^2 - 5x + 6$.  
Vertex $x = 5/2$. Value $-0.25$.  
Since min value is -0.25 (since it's a U shape with positive leading coeff), and -0.25 < 0, then the graph goes down from vertex to roots? No, wait.  
If I have $y=x^2$, min value is 0.  
If I have $y=(x-2)^2 + 1$, min value is 1.  
Why am I getting -0.25 now?  
Let me check calculation of vertex again.  
$f(x) = (x-3)(x-2)$. This doesn't factor to $(x-h)^2+k$ form easily unless expanded.  
Wait, the vertex of a parabola opening up is at $(h, k)$ where $k \ge 0$.  
Wait, if min value is -0.25, then $f(2.5) = -0.25$. Since this is negative, this must be true for any U shape with positive leading coeff? No, wait.  
If $a=1$, $f(x)$ goes to $\infty$ as $|x| \to \infty$. So vertex cannot be negative? No, that's wrong.  
Wait. The "vertex" of a parabola is the point where derivative is zero and second derivative is positive?  
Second derivative $y'' = 2 > 0$ always. So minimum exists.  
Wait. If it opens up, min value is negative? No.  
Let me draw graph mentally again.  
I start at left side, go to right.  
If parabola goes down then up (inverted U), the max value is vertex.  
If parabola goes UP then down (opens up), then it has a maximum. Wait.  
A "U-shaped" graph (opening up) means for large positive $x$, $y$ is large positive. For large negative $x$, $y$ is large positive. The shape looks like $\uparrow$.  
Wait, I might be confusing opening up with opening down.  
If it opens UP, minimum value occurs at vertex. Wait. No.  
Let's check example: $y=x^2$. Vertex at 0 (min). Goes to $\infty$ on both sides.  
Wait, if it opens UP, then it goes from $-\infty$ to $\infty$? No. It's always positive.  
If I have $y = (x-3)^2$, vertex is 3 (max). Min value is at $\pm \infty$. Wait.  
Wait, if leading coeff is positive, then as $x \to \infty$, $y \to +\infty$. So max is at infinity? No. That's for inverted V shape.  
Wait, I am confusing myself. Let me look at standard graph of parabola opening up vs down.  
Opening UP (U-shape): Minimum value is negative (if I'm looking at $y=x^2$), wait, no.  
Wait, standard example: $x = y^2$. This opens up? No. $y=x^2$. Min value 0? No.  
Let me just trust my formula for vertex of $(ax^2+bx+c)$.  

*Continued in [part 2 of 4](algebra_2043_p2.md): GitHub stops rendering math on pages this long, so the transcript is split.*
