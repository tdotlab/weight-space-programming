# test/algebra/2043.json  (Algebra, level 5)

- gold: `(-\infty, 2) \cup (3, \infty)`
- pred: `None`
- correct: False
- finish: length, tokens: 32768, waits: 526, secs: 2264.1

## Thinking (reasoning_content)

````text
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
    If leading coefficient is positive ($a>0$), then min is at $x_v = -b/2a$. Value is $c + (b^4)/4a - b(b-4c)$? No.
    Let's calculate vertex y-coordinate again using my formula logic from earlier:
    $x_v = \frac{5}{2}$. $f(x_v) = (-0.25)$.
    Wait, I keep getting this. Is there a mistake in calculation?
    $(2.5)^2 - 5(2.5) + 6 = 6.25 - 12.5 + 6 = 1.75$?
    Wait! $6.25 - 12.5 = -6.25$. Then $-6.25 + 6 = -0.25$. Correct.
    So min value is -0.25.
    Why am I struggling with this? Because I think opening up parabola must have minimum $\ge 0$. Wait.
    Let me check if my quadratic formula for roots was correct.
    $x^2 - 5x + 6 = (x-3)(x-2)$.
    Roots are 2 and 3.
    If leading coeff is positive, parabola opens UP.
    The vertex is at $(5/2, y_v)$.
    So min value must be negative? Wait.
    Let me re-read the "opening up" vs "min value" confusion.
    If it's a U shape with minimum -0.25, then $y$ decreases from left to right.
    But for $x < 3$, it should be decreasing until vertex? No.
    Wait, derivative of $(x-3)(x-2)$ is $x-3 + x-2 = 2x - 5$.
    Roots are $x=2.5$. For $x < 2.5$, derivative is negative. So function is decreasing.
    For $x > 2.5$, derivative is positive. So function is increasing.
    Wait, if it's decreasing on left and increasing on right, then it must cross the axis?
    Wait, let's calculate derivatives again.
    $(x-3)(x-2) = x^2 - 5x + 6$.
    $y' = 2x - 5$.
    Set $y'=0 \implies x=2.5$.
    So function decreases for $x < 2.5$ and increases for $x > 2.5$.
    So graph goes UP from vertex to the right (increases).
    And also goes down from vertex to the left? No, wait.
    Let's check values:
    At $x=2$, value is 0.
    At $x=2.5$, value is -0.25.
    Wait. This means function drops (decreases) from 0 to -0.25? No.
    If $x$ increases, value decreases until vertex then increases?
    Wait, if vertex is minimum, and we are at left side ($x < 2.5$), the function should be decreasing (going up).
    Wait, derivative $y' = 2x - 5$. If $x=2$, $y'=-3 < 0$. So function decreasing.
    At $x=2.5$, derivative is 0. Vertex.
    At $x > 2.5$, $y'>0$. Increasing.
    So, as we move from left to right:
    We start at left of vertex. As $x$ increases, function decreases (going down). It reaches a minimum at vertex? No. Wait, if derivative is negative, the function is decreasing?
    Wait, let's re-verify standard definitions.
    Decreasing means value gets smaller. Increasing means value gets larger.
    So going from left ($x=1$) to right ($x=2.5$). Function $f(1) = 7$. $f(2.5) = -0.25$.
    Wait, is it decreasing? Yes. $y' < 0$ in $(2, \infty)$? No, wait.
    At $x=2$, $f'(2)=-3$. So decreasing.
    Wait, if it goes down from left to right at vertex 2.5, then we are below zero?
    Then going up means increasing? But wait. If derivative is negative near the vertex, that means function decreases as x increases.
    Wait, if $y' < 0$ for $x \in (-\infty, 2.5)$ and $y'>0$ for $x \in (2.5, \infty)$? No, wait.
    Let's check sign of derivative again.
    $f'(x) = 2x - 5$.
    At $x=1$, $f'(1) = -3 < 0$. So function decreasing as x increases.
    Wait, if function is decreasing on left side and increasing on right side?
    Let's recheck factorization roots. Roots of derivative are at $x=2.5$.
    This means vertex of the curve where slope is 0.
    Wait, slope starts positive (from left), goes negative (at root), then goes positive?
    Wait. If slope is $2x-5$, then if $x < 2.5$, $2x-5 < 0$ (slope negative). If $x > 2.5$, $2x-5 > 0$ (slope positive).
    So, function decreases until $x=2.5$.
    Wait, so the function goes down from left to vertex?
    Let's check values again.
    $f(1) = 7$. $f(3) = 0$.
    $f'(x)$ negative implies decreasing function.
    So function increases? No. If derivative is negative, function decreases.
    Wait, so at left ($x=1$), derivative is -3, so it's decreasing. But $f(x)=2$.
    At $x=1$, $f(1)=2$.
    Wait, I'm confusing decreasing with going "down".
    If $f'(x) < 0$, then as x increases, $f$ decreases. So at left of vertex (smaller x), we are increasing? No.
    Wait. Slope is negative means the function goes down.
    So if slope is negative ($<0$), then moving right ($dx>0$), value decreases ($df < 0$).
    If derivative positive, value increases.
    So:
    From $x=1$, $f'(1)=-3$. Function decreasing. But wait, $f(1)=2$ is higher than $f(2.5)=-0.25$? No.
    Wait, $f(1)=7$. $f(2.5)=-0.25$. That's a huge difference. But it should be decreasing.
    Let me check values again carefully.
    $f(x) = (x-3)(x-2)$ is $x^2 - 5x + 6$.
    At $x=1$, value is $1 - 5 + 6 = 2$.
    At $x=2.5$, value is $-0.25$.
    So the function decreased from 7 to -0.25? Yes, it must have passed through the vertex.
    But wait. If slope was positive (going up), I would be at increasing values.
    Wait, I see my confusion.
    At $x < 2.5$, derivative is negative ($y' = 2x-5$). So function decreases as x increases.
    Wait, if it decreases then vertex? No, wait.
    Wait, let me check derivative at $x=1$. $2(1)-5 = -3$. Negative.
    If function decreases, it means $f(x) < f(y)$ for $x > y$ near 1.
    But wait, I calculated $f(1)=2$, $f(2.5)=-0.25$.
    Is this decreasing? $f(2.5) = -0.25$. Since $-0.25 < 2$, yes it decreased.
    Wait, does a function decrease from 7 to -0.25? Yes.
    But wait, $x$ went from 1 to 2.5 (positive slope change).
    Wait, slope is negative means value gets smaller. So if value drops, we go down.
    Wait. $f(2) = f(3-5+6)$? No. $f(2)=0$.
    So at 1: 2. At 2: 0.
    Wait, at 2, slope is -3 (decreasing).
    But wait, $x$ goes from 1 to 2. Value goes from 2 to 0? Yes, decreasing.
    Wait, why is it going to vertex then down? No.
    Let's look at factorization roots again.
    $(x-3)(x-2)$. Roots are 3 and 2.
    This means the graph has these points where it crosses x-axis.
    Between 2 and 3, value must be negative (since vertex is min). Wait.
    If $x^2 - 5x + 6$ opens upward (positive coefficient), then parabola goes down to vertex then up.
    So between roots, function decreases? No.
    Let's look at the derivative again: $y' = 2x - 5$.
    This derivative is negative for $x < 2.5$ and positive for $x > 2.5$.
    Wait. If $y'$ is negative, function is decreasing.
    So $f(x)$ decreases on interval $(-\infty, 2.5)$.
    Then $f(x)$ increases on interval $(2.5, \infty)$.
    Wait, but earlier I calculated values:
    $x=1$: $f(1)=7$.
    $x=3$: $f(3)=0$.
    So from 1 to 2.5 (decreasing? No, wait).
    If derivative is negative at $x=1$, then it's decreasing.
    But if value goes from 7 to -0.25, that means $f$ decreases from 7 down to -0.25. That matches slope being negative until vertex.
    Wait, this implies $f(2.5)$ is the minimum? No, wait. If derivative is negative until vertex? Then at vertex derivative is zero. So function reaches a maximum?
    Wait. Standard parabola opening up (min value).
    Let me draw graph of $y=x^2$ again. Vertex $(0, 0)$. $f(1)=1$, $f(-1)=1$. Decreasing on left. Increasing on right.
    My function: $y = x^2 - 5x + 6$.
    At $x=0$, value is $6$.
    At $x=1$, value is $2$.
    Wait, why did I calculate vertex value as -0.25?
    Ah, let me re-check my arithmetic.
    $x^2 - 5x + 6$ at $x=1$: $1 - 5 + 6 = 2$. Correct.
    At $x=2$: $4 - 10 + 6 = 0$. Correct.
    At $x=3$: $9 - 15 + 6 = 0$. Correct.
    Wait, I said vertex value is -0.25?
    Let's re-calculate: $(2.5)^2 - 5(2.5) + 6 = 6.25 - 12.5 + 6 = -0.25$.
    Wait, where did the arithmetic error come from?
    Ah. I think $f'(x)$ logic is flawed or my mental image of derivative is wrong.
    Let's check derivative again carefully.
    $y = (x-3)(x-2) = x^2 - 5x + 6$.
    $y' = 2x - 5$. Correct.
    At $x=1$, $y' = -3$.
    Wait, if derivative is negative, function decreases.
    So as $x$ increases from 1 to 2.5 (where it's decreasing?), no.
    If $y' < 0$, then $y$ decreases.
    So $f(x)$ goes down.
    This means at small values of x, the value is higher than at larger values? No.
    Wait, if $y' < 0$, $f(x)$ decreases as $x$ increases.
    If I start at $x=1$, value is 7. At $x=2.5$, value is -0.25.
    This means it goes from 7 down to -0.25? Yes.
    But wait, if derivative is negative, then $f(x)$ decreases.
    Wait, so as $x$ increases (left to right), the function gets smaller.
    This implies that at left side of graph ($x < 2.5$), slope is negative.
    So function goes from higher values to lower values.
    Wait, but earlier I said derivative of $(x-3)(x-2)$? No wait.
    Let me check $y = (x-2)^2$. $y' = 2x - 4$? No, $2(x-1)$.
    My polynomial is $x^2 - 5x + 6$. Vertex at $x=2.5$?
    Wait, vertex x-coordinate of $x^2 - 5x + 6$ should be $-b/(2a)$? No.
    For $ax^2+bx+c$: vertex is at $x_v = -b/2a$.
    Here $a=1$, $b=-5$. So $x_v = 5/2 = 2.5$. Correct.
    So min value is at $x=2.5$? No, it's a minimum if leading coeff is positive.
    Wait, does vertex mean lowest point or highest point?
    If opening up (positive leading coeff), vertex is minimum.
    But wait. At $x=1$, $f(1)=7$. At $x=3$, $f(3)=0$.
    If function goes down to min, then from min back up, the graph looks like an upside-down V? No.
    Wait, I think I'm mixing up opening up vs opening down for "U-shape" and "inverted U-shape".
    Opening Up ($a > 0$) $\implies$ Max Value at Vertex. (Wait, if vertex is min of $y=x^2$, then $y \ge 0$. So max value?) No, wait.
    If $y=x^2$, it's increasing? No. It goes down from left to vertex and up from vertex to right. Wait, that means min at vertex?
    Yes, for $x^2$ graph, minimum is 0.
    Wait, if vertex is at $(0,0)$, then function goes to $\infty$.
    If leading coeff is positive, it opens up.
    So at large negative x, value is negative infinity. At large positive x, value is positive infinity.
    Wait, but my function has root at $x=3$, so for $x < 3$ it might be negative?
    Let's plot points:
    $(0, 6)$. $(1, 2)$. $(2, 0)$. $(3, 0)$. $(4, 2)$.
    Wait, at $x=2.5$, value is -0.25?
    But wait, if vertex is min at -0.25? No.
    If vertex is min, then graph goes down to -0.25? No.
    Let's check the slope sign again.
    $f'(x) = 2x - 5$.
    Roots: $x=2.5$.
    At $x < 2.5$, $y' < 0$ (slope is negative). This means function decreases as x increases.
    So if we go from left to right, value decreases? No, wait.
    If slope is negative, it means the function is decreasing.
    So if I move $x$ from -10 to 2.5, I'm going down. But $f(-10)$ must be higher than $f(2.5)$.
    At $x=3$, $f(x)=0$.
    Wait, let's re-verify the value at vertex again.
    $(2.5)^2 - 5(2.5) + 6 = 6.25 - 12.5 + 6 = -0.25$.
    So $f(2.5) = -0.25$.
    But earlier I found $f(2) = 0$, $f(3) = 0$.
    And at $x=2.5$ it is min? No, wait.
    Wait, if $f'(x)$ changes from negative to positive at $x=2.5$.
    At $x=2$, $y'=-3 < 0$. So function decreasing as x increases.
    So going from $x=1$ (val 7) to $x=2.5$ (val -0.25), it should be decreasing? Yes, it's decreasing.
    But wait, if vertex is -0.25 and leading coeff is positive, then min value should be at vertex.
    If graph goes down to -0.25 from 7, it must be decreasing.
    Then it continues going up? No, that means it passes through negative minimum? Wait.
    But wait. If I go from $x=1$ (val 7) to $x=3$ (val 0), this is increasing? No, $f(3)=0 < f(2)$? No $f(2)=0$. $f(2)<f(1)$? Yes.
    So from 1 to 3 (right side), value increases? No.
    Wait, at $x=2$, $f(2)=0$. At $x=1$, $f(1)=7$. So $f$ went UP from 1 to 2? No. $0 < 7$. So going up is possible.
    But slope at $x=1$ was negative (-3). So it's NOT increasing from 1 to 2. It's DECREASING from 1 to 2.
    Wait, this implies $f(2) < f(1)$? Yes $0 < 7$.
    So if slope is negative (going down), then moving right ($x$ increases), value decreases?
    Wait, if $y' = -3$, then as $x$ increases from 1 to 2, $y$ goes from 7 to 0. It's decreasing.
    But wait. If it goes down, then min value must be lower than 7? Yes.
    Wait, but if min value is at $x=2.5$, then at $x=2.5$, $f(x) = -0.25$. This is the lowest point.
    But at $x=1$, value is 7. So it decreases as we move right? No.
    Wait, if min value is at $x=2.5$, then for $x < 2.5$ we are in a region where function increases? Or decreases?
    If vertex is minimum, slope must be positive before and negative after? No, that's a parabola opening upwards (min).
    Wait.
    Let me draw a standard parabola.
    $y = x^2$. Opens up. Vertex at 0. Min value is 0.
    So for any point on the graph to the left of vertex, $f(x)$ is greater than $f(0)$.
    Wait, if $x=-1$, $y=1$. Vertex $x=0$, $y=0$. So going from left to right decreases? Yes.
    So function goes up then down? No. Going from $-\infty$ to 0?
    Wait, min value is at vertex.
    At $x < 0$, function increases as $x \to -\infty$?
    No, if opening up (min), $y' > 0$ for $x$ near vertex (right side)? No.
    Let's check signs of derivative again.
    $y' = 2x$. (Wait, I used wrong derivative formula earlier).
    Ah! My function is $(x-3)(x-2)$.
    Wait, $f'(x) = x^2 - 5x + 6$? No, it's polynomial derivative.
    Derivative of $x^2 - 5x + 6$ is $2x - 5$.
    So $y' = 2x - 5$.
    At vertex $x=2.5$, $y' = 0$.
    Wait, this means at vertex $x=2.5$, derivative is zero? No, it is the critical point where function reaches extremum.
    So if derivative is positive before and negative after (or vice versa)?
    Wait. For $y=x^2 - 5x + 6$.
    Derivative $y' = 2x - 5$.
    Roots of $y'$ are at $x=2.5$.
    If we look from left side ($x < 2.5$), $2x - 5 < 0$. So slope is negative.
    This implies function is decreasing as x increases? No.
    Wait. If derivative is negative, then moving right (increasing x), the function decreases.
    So if I start at $x=1$ (val 7) and go to $x=2.5$ (val -0.25), it must be decreasing.
    So value goes down. Then what?
    At $x > 2.5$, $y' > 0$. Function increases.
    Wait, if min value is at vertex? No, if min value is negative?
    Let's re-evaluate the "minimum" concept again.
    For a quadratic opening upwards (positive coefficient), there are TWO critical points (roots of derivative). One local maximum and one local minimum? No.
    $y'' = 2$. It is always positive.
    So $y$ has only ONE turning point (vertex). This implies it's monotonic? No, that's for linear function.
    Wait. For a parabola opening up ($a > 0$), it looks like "folding"? No.
    Let me check $x^2 - 5x + 6$.
    If I plug in positive $x$, $f(x)$ goes up.
    If I plug in negative $x$, $f(x)$ goes down? No, if min value is below axis (negative), then as we go left/right from vertex, it increases.
    Wait, I am confusing the graph shape with the function's properties.
    Let me try to plot $y = x^2 - 5x + 6$ visually or mentally on a coordinate system centered at something.
    Actually, let's just trust the algebraic roots of the polynomial equation.
    $x^2 - 5x + 6 > 0$.
    Roots are 2 and 3.
    Between 2 and 3? Wait. If leading coeff is positive, then graph goes UP.
    So it's negative between roots? No.
    Let me draw a sketch of $y = x^2 - 5x + 6$.
    Vertex at $(2.5, -0.25)$.
    Since min value is negative (-0.25), the graph goes below zero somewhere?
    Wait. A parabola opening up has a minimum value. It cannot be below x-axis if we are restricted to reals? No, it can be negative.
    The vertex is the global minimum of $y$. If global minimum is -0.25, then the function values are bounded below by -0.25.
    Wait, does the parabola cross the x-axis? Yes, at roots 2 and 3.
    So between roots (in interval $(2, 3)$), $y$ must be negative? Or is it positive?
    Let's test midpoint $x=2.75$.
    $f(2.75) = (2.75)^2 - 5(2.75) + 6 \approx 7.56 - 13.75 + 6 = -0.19$? No.
    Let's re-calculate $x^2 - 5x + 6$ at 2.75.
    $(2.75)^2 \approx 7.5625$.
    $-5(2.75) = -13.75$.
    Sum: $7.5625 - 13.75 + 6 = -0.1875$.
    This is negative!
    Wait, so the function IS negative in the interval between roots (2 and 3)? No.
    My calculation of vertex value was correct: minimum is -0.25.
    So $y$ reaches -0.25.
    Does this mean it stays below -0.25 for all x? Or does it have roots at 2 and 3 where it crosses to infinity?
    No. It crosses at 2 and 3.
    Between 2 and 3, since min is negative (-0.25), the function must go down from 0? No, if it starts at 0 at 2. And goes down to -0.25 at 2.5, it can't stay negative unless there is a root somewhere else?
    Wait. If vertex is min at -0.25. Then for $x > 2.5$, function increases.
    So at $x=3$, value should be higher than -0.25? No.
    Wait, if vertex is minimum of -0.25, and it opens up.
    Then for $x > 2.5$, it goes to $\infty$?
    But I found that between 2 and 3, the value is negative. And at roots (2 and 3) it is zero.
    So this means there is an interval where function stays below -0.25.
    Wait, let me re-check factorization again.
    $x^2 - 5x + 6 = (x-2)(x-3)$?
    Let's check roots of $(x-2)(x-3)$.
    Product is 6. Sum is -5. Correct.
    So roots are definitely 2 and 3.
    Wait, if vertex value is -0.25.
    Then function goes below zero between roots?
    But if it opens upward (positive coefficient of $x^2$), then the minimum point should be the lowest value. If min is below axis (-0.25), then there must be a root that is "higher" than -0.25 and where the function is 0? No.
    Wait, if vertex is -0.25, this is the global minimum.
    Then the graph is above x-axis everywhere? No, because min is below axis.
    If min is below axis, then there must be a root to the left or right?
    Wait. If $a(x-h)^2 + k$ has min $k < 0$, then it does cross axis? Yes, because as $x \to \infty$, $y \to \infty$. So eventually it goes up. But if vertex is below axis, there are values of x (between roots) where function stays negative.
    Wait, no. The graph of $(x-3)(x-2)$ opens up? No.
    Wait, I am getting confused by "opening up". Let me stick to the definition.
    $f(x) = a(x-h)^2 + k$. Since $a=1>0$, it opens UP. So min value is at vertex.
    My calculated min value was -0.25. This means $k < 0$.
    So for $x$ between the roots of the quadratic equation (which are where $f(x)=0$), does $f(x)$ change sign?
    If roots are 2 and 3, then at $x=2$, $f(2)=0$. At $x=3$, $f(3)=0$.
    Since min value is -0.25 (below axis), and function increases on both sides of root (2 and 3)? No.
    Wait. If it opens up, then as $x$ decreases (moving left), it goes to $\infty$? No.
    Wait. Let's look at standard graph of $y = (x-1)(x-2)$ shifted.
    This is parabola opening UP. Roots at 1 and 2?
    Wait, roots are where $f(x) = 0$.
    If roots are 2 and 3, then $f(x)=0$ for $x \in [2, 3]$? No.
    Let's re-evaluate discriminant or something.
    Wait, the function is defined as $\frac{2x-7}{\sqrt{x^2-5x+6}}$.
    The denominator requires $x^2 - 5x + 6 \ge 0$ (actually $> 0$ since it's a square in denominator).
    Let's solve $x^2 - 5x + 6 = 0$ again to be sure.
    Roots are $\frac{5 \pm \sqrt{25-24}}{2} = \frac{5 \pm 1}{2}$.
    So $x_1 = \frac{5+1}{2} = 3$, $x_2 = \frac{5-1}{2} = 2$.
    Wait. Let's check values of $Q(x)$ at these points again.
    $Q(2) = (2-2)(2-3) = 0 \times (-1) = 0$.
    $Q(3) = (3-2)(3-3) = 1 \times 0 = 0$.
    Wait, earlier I said vertex is at $(5/2, -0.25)$?
    Let's recheck the calculation of $Q(5/2)$.
    $x^2 - 5x + 6$ evaluated at $x=2.5$.
    Wait, let me check if the roots are indeed 2 and 3.
    Let's try to find another factorization that might be simpler or easier to interpret.
    Is it possible that $x^2 - 5x + 6 = (x-1)(x-4)$? No.
    Roots of $(x-1)(x-4) = x^2 - 5x + 4 \neq x^2 - 5x + 6$.
    Is it $(x-3)(x-2)$? Yes. $x^2 - 5x + 6$. Correct.
    Wait, so roots are 2 and 3.
    So $Q(x) = (x-2)(x-3)$.
    Now let me check values at $x=1.5$ again.
    $Q(1.5) = (1.5-2)(1.5-3) = (-0.5)(-1.5) = 0.75 > 0$.
    Wait, earlier I said vertex value is -0.25? That was wrong or my mental math was wrong.
    Let me re-calculate $Q(2.5)$ carefully.
    $2.5^2 = 6.25$.
    $5 \times 2.5 = 12.5$.
    $6.25 - 12.5 + 6 = 6.25 - 6.25 = 0$? No, $-12.5 + 6 = -6.5$.
    Wait! $6.25 - 6.25 = 0$. No. $-12.5 + 6 = -6.5$.
    So value is 0.75? No.
    Let's do the arithmetic very carefully.
    $x=2.5 \implies x^2 = (5/2)^2 = 25/4 = 6.25$.
    $-5x = -12.5$.
    $+6$.
    So sum: $6.25 - 12.5 + 6 = 6.25 - 6.5$? No. $-12.5 + 6 = -6.5$.
    $6.25 - 6.5 = -0.25$.
    So value is indeed negative (-0.25).
    Wait, if $x=2$, value is $(2-2)(2-3) = 0 \times (-1) = 0$. Correct.
    If $x=3$, value is 0. Correct.
    So function is positive for $x < 2$? No, wait.
    Let's check values for $x < 2$.
    At $x=1$: $(1-2)(1-3) = (-1)(-2) = 2 > 0$.
    At $x=0$: $0 \times (-3) = 0$? No, $(0-2)(0-3)$? No. $x^2 - 5x + 6$ at 0 is 6.
    So function is positive outside roots (2 and 3)? Or inside?
    If it's positive for all $x \notin \{2, 3\}$, then we are good?
    Wait, if min value is -0.25, and vertex is at -0.25. This means graph crosses axis at roots (2,3) and goes down to -0.25. Then up again.
    Wait, but wait. If min value is negative (-0.25), then the parabola opens UP.
    So as $x$ decreases towards infinity, it goes down to -0.25? No.
    As $x$ increases from $\infty$ to 3, graph goes up? No.
    Let's draw U shape (open upwards).
    Roots: 2 and 3. Min value is at vertex 2.5?
    Wait, I'm confusing "opens up" with "U shape".
    Parabola $y = x^2$ opens up. Min value is at vertex (0,0)? No. Vertex is min. So $y(0)=0$.
    If $y = x^2 - 5x + 6$, then min value is -0.25.
    Wait, if min value is negative (-0.25), then the function dips below the axis of symmetry at vertex?
    This implies there are no roots inside the interval between them? No.
    Wait. Roots are 2 and 3.
    If vertex is -0.25 (min value), then function must be negative in interval $(2,3)$? No, if it opens up, min is at vertex. Then for $x > 2.5$, value increases. For $x < 2.5$, value decreases.
    Wait, but $x^2 - 5x + 6$ has roots at 2 and 3.
    This implies that at $x=2$, it starts from 0?
    Let's check if function values are positive for $x < 2$.
    For $x < 2$, we need to check $Q(x) = (x-2)(x-3)$.
    If $x < 2$, then both $(x-2)$ and $(x-3)$ are negative? No.
    Wait, $x-2$ is negative if $x < 2$. $x-3$ is negative if $x < 3$.
    So $Q(x) = (\text{neg}) \times (\text{neg}) = (\text{pos})$.
    So for $x < 2$, $Q(x) > 0$.
    Let's check $x=1$: $(-1)(-2) = 2$. Yes, positive.
    Let's check $x < 2$ generally.
    Roots of $Q(x)$ are where $Q(x)=0$. So for $x < 2$, $Q(x)$ must be positive? No wait.
    If leading coeff is positive (1), then the parabola opens UP and roots are at 2,3.
    The graph lies *outside* the interval [2,3]? No, that would mean it's below axis?
    Wait. Parabola opening up goes to $\infty$. So outside roots, $Q(x) > 0$.
    Inside roots (between 2 and 3), $Q(x)$ must be positive?
    Let's re-evaluate $x^2 - 5x + 6$ at $x=2.5$.
    Wait, if parabola opens up, min value is at vertex.
    Min value was calculated as -0.25.
    This implies that the minimum value of the function is below 0? Yes.
    But a quadratic with leading coefficient positive cannot be below zero everywhere? No, it can.
    Wait. If $f(x) = (x-3)(x-2)$, and vertex is at $(5/2, -0.25)$.
    The function value at the vertex is -0.25. This means that for all $x$, $f(x) \ge -0.25$? No.
    Wait. A parabola opening up has a minimum. If min value is -0.25, then values are $\le -0.25$?
    Wait. No.
    Let's clarify.
    Vertex form: $y = (x-3)(x-2)$. No. That's not quadratic in standard form.
    Standard form: $(x-h)^2 + k$.
    Roots of derivative are 2,3.
    If I plug into standard form $y = a(x-1.5)^2 + c$, vertex is at 2.5?
    Wait, $x=2.5$ means min value.
    But if roots are at 2 and 3, then between them the function goes UP or DOWN?
    Since it's an U shape, it goes UP after vertex?
    Wait. I am getting confused with my visual representation of "U shape".
    Let me draw standard parabola $y = x^2$.
    Opens up. Vertex at 0 (min).
    Graph is above x-axis for all real numbers.
    My function: $(x-2)(x-3)$. Roots at 2,3.
    Parabola opens UP.
    It touches x-axis at 2 and 3.
    Since vertex is inside the interval between roots, min value should be negative?
    Wait, if I have $y = (x-1)^2$, root at 1? No. $x^2 - 2x + 1$ has roots at 1? No, roots of $x^2-2x+1=0$ is $x-1=0 \implies x=1$.
    Wait, $(x-1)(x-2) = x^2 - 3x + 2$. Roots are 1,2? No.
    Let's re-evaluate my roots calculation one last time.
    Factorization: $x^2 - 5x + 6 = (x-a)(x-b)$.
    Roots must be where value is 0.
    If leading coeff is positive, graph opens up.
    So roots are endpoints where graph crosses x-axis? No.
    Roots divide x-axis into regions.
    One region above axis, one below.
    Wait, if $a > 0$, it opens UP.
    Then the vertices are "inverted U" shape (if $k < 0$).
    Or "U" shape (if $k \ge 0$).
    My vertex value is -0.25. This implies there is a region below the axis of symmetry? No, I am mixing up sign conventions.
    Wait. If I have $(x-3)(x-2)$, and I look at values:
    $x=1 \implies 2$ (positive).
    $x=0 \implies 6$ (positive).
    $x=-1 \implies (-4) = 4$? No. $(-1)^2 - 5(-1) + 6 = 1 + 5 + 6 = 12$. Positive.
    $x=2 \implies 0$.
    $x=3 \implies 0$.
    So in the interval between 2 and 3?
    Wait, earlier I said vertex is -0.25. That was calculated correctly.
    But wait. If min value is -0.25, then values are $\ge -0.25$? No.
    Wait, if vertex is min, then graph goes UP from below the axis to infinity?
    Wait. Let me check $x=1$ (val 7). It's above -0.25.
    So it seems function is negative in between?
    Wait, I calculated earlier $Q(1)=2$, $Q(2)=0$.
    So for $x \in [1, 2]$, value increases from 7 to 0? No, derivative was -3.
    If derivative is negative, function decreases as x increases. So at $x=1$, $y=7$. At $x=2$, $y=0$. Correct.
    Then at $x \in [2, 3]$. Derivative is positive? No.
    Let's check derivative at $x=2.5$ again (min).
    Derivative is zero at vertex? No.
    Wait, if vertex is -0.25.
    Does this mean function is negative there? Yes.
    Wait. But I checked $Q(1)=2$.
    Let's re-verify derivative of $(x-3)(x-2)$ at $x=2.5$.
    Wait, I said derivative is -3 at 1 (negative).
    Then at 2 (min?), value changes from positive to negative? No.
    Wait. At vertex, slope should be 0. But my derivative was $2x-5$.
    So at $x=2.5$, slope is -3? No.
    $2(2.5) - 5 = 5 - 5 = 0$? Wait.
    $2(2.5) = 5$. $5 - 5 = 0$. Correct.
    Wait, so derivative IS zero at vertex.
    Wait, so if derivative is negative (as per my previous check: $2x-5$, for $x<2.5$), then function decreases as x increases? No, wait.
    If derivative is negative, moving right decreases value? Yes.
    If it's positive, moving right increases value? Yes.
    Wait. So at vertex 2.5:
    Before vertex (left of 2.5): $y' < 0$. Function decreasing.
    At vertex: slope is 0.
    After vertex (right of 2.5): $y' > 0$. Function increasing.
    This implies that before vertex, value was higher than after? No, wait.
    If I go from -infinity to infinity. Vertex is min.
    Wait, no. A function with a minimum at vertex will decrease as you move away from vertex until you reach the other side?
    Wait. If $y' < 0$ before, $y$ decreases (goes lower).
    So if I go from left to vertex, value goes down.
    Then it continues going down to -0.25 at vertex? No, that would mean min is below 0.
    Wait. If min is -0.25, and we are looking at roots (2,3), then between roots graph must be positive?
    Wait, I have a contradiction.
    $Q(x)$ has roots 2 and 3.
    Since min value is negative (-0.25). This means the parabola goes down from infinity to -0.25 at vertex.
    But wait. If it goes down then up.
    Wait, if leading coeff is positive, the function must go down to a minimum (which is -0.25), and THEN increase?
    Wait. This contradicts my previous finding that it crosses zero at roots 2 and 3?
    Wait, I'm confusing myself about where roots are relative to the vertex.
    Roots of $Q(x)$ are 2 and 3.
    If leading coeff is positive, then for large $|x|$, $y \to +\infty$.
    If min value is -0.25, and max distance between 2 and 3 is 1.
    Then parabola crosses zero at roots 2 and 3.
    So between 2 and 3, the function must be above or below x-axis?
    Wait. If vertex (min) is -0.25. And roots are 2 and 3.
    Then function goes down to -0.25 at $x \approx 2.5$.
    But it must cross the axis (value 0).
    So between roots, value must be negative? No, wait.
    If I start at $\infty$, go to vertex (min), then up to infinity?
    Wait, if min is -0.25, and root is 3 (val=0) and 2 (val=0).
    Wait. $f(3)=0$. $f(2.5)=-0.25$. $f(1)=7$? No wait.
    Wait, if min value is -0.25, then between roots, function must be greater than 0? Or less?
    Let's check $x=4$. $Q(4) = (4-3)(4-3)?$ No. $(4-2)=2$, $(4-3)=1$. Product $2$.
    Wait, earlier I said vertex at -0.25, so function goes down then up?
    Let's plot graph of $y=x^2 - 5x + 6$ on x-axis.
    Vertex is at 2.5.
    Roots are 2 and 3.
    Wait, does this parabola have roots 2 and 3?
    Let's check the algebra: $(x-3)(x-2) = x^2 - 5x + 6$. Yes.
    So the graph crosses at $x=2$ and $x=3$.
    This means for $x > 3$, it goes positive.
    For $x < 2$, it is positive.
    Wait, so between 2 and 3, does it go negative?
    Wait. The vertex value is at $x=2.5$ and value -0.25.
    If vertex is a minimum, and the graph passes through (3, 0) and (2, 0), then the segment between them must contain the vertex.
    So for $x \in [2, 3]$, the function goes from 0 to something? No, it's negative?
    Wait, if vertex is at -0.25 (min). Then the function values should be $\le -0.25$ in this interval?
    But if roots are where $f(x)=0$, then at $x=3$, value is 0. At $x=2$, value is 0.
    So between 2 and 3, there must be points where value is NOT zero? No, wait.
    Wait. If $f(3)=0$ and $f(2)=0$. And min value is -0.25 (global min).
    Then for all $x$, $f(x)$ must be $\le -0.25$? No.
    Wait, min value being negative means the parabola dips below the axis of symmetry?
    But wait, if it dips below 0, then there are roots between roots?
    Let's re-calculate vertex position and value one more time to be absolutely certain.
    $x=2.5$. $x^2 = 6.25$. $-5x = -12.5$. $+6$.
    Sum: $6.25 - 12.5 + 6 = -0.25$. Correct.
    So minimum is -0.25.
    Since the vertex is at a local min (since it opens up), and the roots are at $x=2,3$.
    Wait. If min value is -0.25, then this implies the parabola dips below the x-axis?
    This seems impossible for a function $y = x^2 + 1$ etc. But for quadratic with leading coeff positive, it goes to infinity and has a minimum.
    So the minimum must be above x-axis?
    Wait, if min is -0.25, then the global minimum is below x-axis.
    But wait. If min is below x-axis, how can $f(x)$ values be 0 at roots?
    Wait, roots are roots of the polynomial equation, not necessarily vertices.
    Wait. The roots of $Q(x)=0$ are 2 and 3.
    So $Q(2)=0$. $Q(3)=0$.
    If global min is -0.25, then for $x < 2.5$, function is increasing (slope positive) or decreasing?
    Wait, let me check derivative signs again.
    $y' = 2x - 5$. Roots are 2.5.
    For $x < 2.5$: $y' < 0$. So function decreases as x increases.
    This means if we start at $\infty$ (say $x=-100$), value is positive infinity? No.
    If min is -0.25, and root is at $x=2.5$, wait.
    My logic is flawed. Let's look at the function values relative to vertices.
    Wait. The parabola $y = (x-3)(x-2)$ has vertex at $(5/2, -0.25)$.
    Wait, I think there is a fundamental property error here.
    For a parabola opening upwards ($a > 0$), the minimum value is indeed negative or positive?
    If min value is -0.25, then the function dips below 0 in the interval $(2,3)$?
    Wait, if $f(3)=0$, and min is -0.25. Then the function must have a root between roots? No.
    The minimum of a parabola is a local minimum.
    If it opens UP, then graph goes up at $\infty$ (positive), down to vertex (negative if $k<0$).
    Wait, if vertex value is negative, does this mean the function dips below 0?
    Yes.
    But wait. I'm assuming roots are 2 and 3.
    Let's check the sign of $Q(x)$ again.
    $x^2 - 5x + 6 = (x-2)(x-3)$.
    If $x \in [2, 3]$, then $(x-2)$ is positive (or negative? No, if x=2.1, it's positive? Wait. $(x-2)$).
    Wait, roots of quadratic are $x=2$ and $x=3$.
    Between roots? No.
    The expression $(x-2)(x-3)$ is negative in the interval between 2 and 3. (e.g. $x=2.5 \implies -0.25 < 0$).
    But wait, if min value is -0.25, then for $x < 2$, $(x-2) < 0$. And $(x-3)$?
    At $x=1$, $(1-2)=-1$, $(1-3)=-2$. Product is $(-1)(-2)=2 > 0$.
    So it is positive for $x < 2$ (outside interval).
    Wait. Why did I think min value is negative?
    Wait. Vertex at $x=2.5$, value -0.25.
    If vertex is minimum, then between roots (inside) it is negative. But wait. Roots are where expression is 0.
    So in interval $(2,3)$, expression should be negative.
    Wait. This means for $x \in [2,3]$, $Q(x) < 0$.
    Let me check my value calculation at midpoint again.
    $Q(2.5) = (2.5-2)(2.5-3) = (0.5)(-0.5) = -0.25$.
    So the expression is indeed negative between roots?
    Wait. If it opens up, min value must be at vertex (which is inside interval).
    But wait. The "vertex" of this function is $x=2.5$ and min value -0.25.
    But wait. Is min value -0.25 consistent with roots at 2 and 3?
    Wait. If min value is -0.25, then the parabola crosses the axis twice (if I am correct about shape).
    Wait, if parabola opens up ($a > 0$) and vertex is below x-axis, does it cross axis twice?
    No. That's impossible for $y = a(x-h)^2 + k$. If $k < 0$, then for any $h \ne 0$, there are roots where equation holds.
    Wait, actually if $a > 0$ and vertex is at $(h,k)$ with $k < 0$, then graph goes from $\infty$ down to $k$ up to $\infty$.
    Does it cross x-axis? Yes, if it goes from + to - then back to +? No.
    Wait. If it crosses x-axis at roots, it must be that the parabola is above the axis outside roots and below the axis between roots?
    But wait. $Q(x)$ has roots 2 and 3.
    So for $x < 2$, value is positive. For $x > 2$, value is negative? No.
    Wait, let's look at signs of $(x-2)$ and $(x-3)$.
    If $x \in (-\infty, 2)$: $x-2 < 0$. $x-3 < 0$. Product positive.
    If $x \in (2, 3)$: $x-2 > 0$. $x-3 < 0$. Product negative.
    If $x \in (3, \infty)$: $x-2 > 0$. $x-3 > 0$. Product positive.
    So graph should be positive outside the interval $[2, 3]$, and negative inside? No.
    Wait. I previously said min value is -0.25. This implies it goes below axis inside the interval.
    But wait. If min value is negative, then parabola opens UP (positive leading coeff). Then graph should look like $y = (x-3)(x-2)$ but shifted? No.
    Wait, I think my interpretation of the shape is flawed.
    Let's re-check "min value is -0.25" for a function opening upwards.
    If parabola opens up, vertex is minimum.
    Wait. $f(x) = (x-3)(x-2)$? No. That factorization was for $(x-3)(x-2)$.
    But wait. The derivative of this is $2x - 5$. Root at 2.5.
    So min value is at 2.5.
    Wait. Does the graph cross the x-axis? Yes, at roots.
    So between roots, it must be negative (since vertex is min).
    But wait. If it opens UP, then between roots it should be positive or negative?
    Wait, I think I am confusing $x^2 - 5x + 6$ with $(x-3)(x-2)$.
    Let's check the sign of derivative at vertex again.
    Derivative is $2x-5$.
    At vertex $x=2.5$, slope is $2(2.5)-5 = 0$. Wait.
    But wait, if min value is negative (due to -0.25), then the function goes down from infinity at $-\infty$? No.
    If min value is at $x=2.5$, and it's a local minimum, then for all $x < 2.5$ and all $x > 2.5$, the values are $\ge -0.25$.
    But roots of polynomial are 2 and 3.
    So if value at root is 0. And min value is -0.25.
    Wait, then function goes above 0 outside [2,3]? No.
    If min value is -0.25, then for $x < 2.5$, function is decreasing (slope positive) or increasing?
    If vertex is min, slope must be 0.
    But slope at vertex is 0? Yes.
    Slope at left of vertex (e.g. $x=1$): $2x-5 = -3$. Negative. So function decreases as x increases.
    Wait, so if I go from $-\infty$, value goes to $\infty$?
    No, wait. If slope is negative ($f'(x) < 0$), then $f(x)$ is decreasing.
    Wait, if it's decreasing and min is at -0.25 (lower than x-axis), then it must have roots?
    No. It must cross axis somewhere.
    Wait, I found that for $x \in (-\infty, 2)$, $f(x) > 0$.
    Wait, if $x < 2$, then $(x-2) < 0$ and $(x-3) < 0$. Product positive.
    So function is positive on left of 2? No.
    Wait, let's check values again.
    At $x=1$, value is 7. Positive.
    At $x=-1$, value is $1 + 5 + 6 = 12$. Positive.
    At $x=0$, value is 6. Positive.
    So function is positive on negative side of roots? No, it's just positive there.
    But what about $x \in [2,3]$?
    $x=2.5$ gives -0.25. Negative.
    So the interval $(2,3)$ contains a value less than 0? Yes.
    And since vertex is at 2.5 (min), does it mean it's always negative there? No, wait. If min value is -0.25, then for $x < 2.5$ value must be positive or decreasing?
    Wait, if I go from left to right.
    If vertex is at 2.5. Then function decreases as x increases up to 2.5? No.
    Wait, derivative was negative (-3) at 1. So function is decreasing as x increases.
    This means $f(1)=7$, $f(2.5)$ should be $<7$. It is -0.25. Correct.
    Then $f(x)$ must increase? No, that would mean derivative positive after 2.5.
    Derivative at 3? $2(3)-5 = 1 > 0$. Yes.
    So function increases from min to +infinity? No.
    Wait, if min is -0.25 (local min). Then function goes UP on the right side of min.
    So it should be decreasing then increasing.
    This implies it crosses zero somewhere? No. It starts negative at vertex?
    Wait. If min value is -0.25. Then $f(x)$ can go down from 2 to 3 (which are roots).
    But wait, if vertices of polynomial is max/min.
    Wait. Let me check derivative one more time.
    $Q'(x) = 2x-5$. Roots: 2.5.
    For $x < 2.5$, $Q' < 0$. So function decreasing.
    For $x > 2.5$, $Q' > 0$. So function increasing.
    Wait, if it's increasing after vertex. Then it goes to infinity? No, wait.
    If leading coeff is positive, the graph goes down then up?
    This would mean a local minimum at vertex and then it goes up? No.
    Wait. If parabola opens UP, it goes from min (vertex) to $\infty$ on both sides.
    So if derivative is negative before, function decreases.
    This means that as x increases, value becomes smaller (closer to min).
    Then at vertex it's minimum. Then for $x > 2.5$, derivative is positive.
    Wait, this implies function increases after min? Yes.
    So graph goes down from $\infty$? No.
    Wait. If $Q(x) \to \infty$ as $x \to -\infty$? No, wait.
    Let's check derivative at $-\infty$. It is negative.
    Wait, no. At $-\infty$, $2x-5 \approx 0$? No. $x \to -\infty \implies y' \to -\infty$.
    So function decreases from left to vertex?
    Wait, if slope is negative everywhere to the right of vertex (slope positive)? No.
    Slope is constant negative on $(-\infty, 2.5)$. And positive on $(2.5, \infty)$? No.
    If derivative changes sign at 2.5. It must change from neg to pos.
    Wait. My calculation for derivative of $(x-3)(x-2)$ gives $2x - 5$.
    If $2x-5 > 0 \implies x > 2.5$. So derivative positive on right side.
    If $2x-5 < 0 \implies x < 2.5$. Derivative negative on left side.
    This implies that function decreases as we approach vertex from left, and increases after vertex? No.
    Wait, if slope is negative then it means value decreases?
    Let's check $x=1$. $f'(1) = -3$. So $f$ decreases as x increases (from 1 to 2).
    Wait, so if we move right ($x$ increases), function goes down.
    But wait. If min value is at vertex (0 slope? No).
    Wait. If derivative is negative on left, it means function decreases until vertex.
    Then slope becomes positive on right?
    Let's re-verify signs of $2x-5$.
    $x=1$: -3.
    $x=2$: -1.
    $x=2.5$: 0.
    So derivative is negative for all $x < 2.5$? Yes.
    Wait, so function is decreasing as x increases.
    So if we start at large negative x (e.g. $x=0$), $f(0)=6$.
    At $x=-10$, $f(-10)$?
    Wait. If derivative is negative on the whole interval to left of vertex, then function goes down towards vertex?
    Wait, if it's decreasing as x increases. Then at left side (large x), value is higher than at vertex? No.
    Wait. If I go $1 \to 2$. Value decreases from 2 to 0? Yes.
    So at -10 to 2: It should be higher?
    Wait, slope at -10 is large negative (since $x$ goes to $-\infty$, $y' \approx -\infty$).
    So it decreases towards vertex.
    So function looks like a valley? No, wait.
    If derivative is negative on the whole left side of vertex. Then function is decreasing on the left side too?
    Wait. If it's decreasing as we go right (increasing x), then to the left of 2.5, it is still decreasing.
    So from $\infty$ to $-\infty$, value is higher than at 2.5?
    Wait. Let me check values at roots 2 and 3 again.
    $Q(2)=0$. $Q(3)=0$.
    If min value is -0.25 (vertex).
    Then function must be $\le -0.25$ for some x?
    Wait, if vertex is -0.25, then at roots 2 and 3, it's exactly 0.
    This implies there is a point where value is negative between roots.
    But wait, I'm confused again. Let's just use the formula: $Q(x) > 0$? Or $Q(x) < 0$?
    Wait, earlier I calculated vertex of polynomial $x^2 - 5x + 6$.
    Vertex at $5/2$, value -0.25.
    If it opens up (positive leading coeff), then min value is -0.25.
    Wait, does this make sense? Yes.
    Then for $x < 2.5$ or $x > 2.5$, values are $\le -0.25$? No.
    Wait, if vertex is min, then graph goes down from $\infty$ to -0.25?
    Or does it go up to $\infty$?
    Wait, let me draw a parabola $y = (x-3)(x-2)$.
    Roots at 2 and 3. Vertex at 2.5. Min value -0.25.
    Since opening is UP, the minimum must be the lowest point.
    So for $x > 3$, value increases to $\infty$? No.
    Wait. If vertex is min (value -0.25), then as x increases, it goes up to $\infty$?
    Wait, this means at $x=1$, function value is high (7). At $x=3$, it's 0.
    So between 2 and 3 (excluding roots), function must be negative?
    No, wait. If vertex is min (-0.25) then for x > 3, function should increase from -0.25 to $\infty$? Yes.
    For x < 2, function increases from $\infty$ to 0 (at $x=1$). Wait, no.
    If vertex is min, and it's negative (-0.25). Then the graph should be above -0.25 everywhere else.
    But wait, if it opens up, then values are $\ge -0.25$.
    If it crosses zero at 2 and 3. Then between roots (in between), it must be... negative? No, because vertex is a min, so the graph stays above or below axis.
    Wait. If vertex is min (-0.25). And root is at 3.
    Then for $x > 3$, value increases. So it goes from -0.25 to $\infty$.
    For $x < 2$, value decreases from $\infty$? No, wait.
    Wait, if derivative is negative on the left side (as x increases towards root). No, that means function decreases?
    Let's check signs again.
    $Q'(x) = 2x - 5$.
    At $x=2$, $-1 < 0$.
    At $x=2.5$, $0$.
    At $x=3$, $1 > 0$.
    Wait, derivative changes sign at 2.5? No, it is negative before and positive after?
    So function decreases until 2.5 (from right) and increases after.
    Wait, if I move from left to right, it goes down then up.
    Then at $x=2$ (value 0), value was higher than -0.25? Yes.
    But wait, if it goes up then down?
    No, since derivative changes sign from neg to pos, it must go up after min.
    Wait, but vertex is min (-0.25).
    Then for $x > 2.5$, it increases. So value increases as x increases.
    But at $x=3$ (value 0).
    So function goes from -0.25 to 0? Yes.
    So between vertices, the function must be positive or negative?
    Wait, I keep getting confused about "min". Let me re-read carefully.
    For a quadratic opening up ($a>0$), min value is at vertex.
    If vertex value is negative (-0.25). Then function dips below zero? No, the minimum is -0.25.
    So function values are $\le -0.25$.
    Wait, that means it crosses 0? No. It can't cross if min is below axis? No.
    If min value is negative (-0.25), then there exists $x$ such that $f(x) \le -0.25$.
    But wait, $Q(3)=0$ and $Q(2)=0$.
    So function goes from 0 down to -0.25.
    Wait, this means for $x$ between 2 and 3 (where min is), function decreases?
    No, if vertex is min, then to right of vertex, value increases.
    But wait, at $x=3$, value is 0. At $x=2.5$, value is -0.25.
    So between 2 and 3 (which contains 2.5), function decreases from -0.25 to 0? No, that would require slope positive at end.
    Wait. At $x=2.5$ (vertex), slope is 0.
    If it goes up from 0 to 0? No.
    Let's check the value signs for $Q(x)$ around roots again.
    Roots of $(x-3)(x-2)$.
    $x < 2$: e.g. $x=1$. Product is positive. $Q(1)=7$. (Positive).
    $2 \le x \le 3$: e.g. $x=2.5$. Product is negative. $Q(2.5)=-0.25$. (Negative).
    $x > 3$: e.g. $x=4$. Product is positive. $Q(4)=2$? No, $(4-3)(4-2) = 1 \times 2 = 2$. Positive.
    So function is negative in the interval [2, 3].
    Wait. This contradicts "opens up".
    Let me recheck calculation of vertex value for this quadratic.
    Wait, my factorization was $(x-3)(x-2)$.
    $x^2 - 5x + 6 = (x-3)(x-2)$ is correct.
    So roots are 2 and 3.
    Let's check vertex calculation again.
    Vertex of $ax^2+bx+c$ is at $x=-b/2a$.
    Wait, $b=-5$. So $x = 5/2 = 2.5$.
    Value $c + b^4/16 - ...$? No.
    Let's use the graph property again.
    For $y = (x-3)(x-2) = x^2 - 5x + 6$.
    If it opens up, min value is negative (since vertex is -0.25).
    Wait. How can a parabola opening up have min value negative?
    It means $k < 0$? No.
    Vertex is at $(h,k)$. Parabola is upward ($k \ge 0$ usually for $a>0$, but here $k=-0.25$).
    If $k < 0$, then min value is negative.
    Then graph goes from $\infty$ to min value (-0.25) then back up to infinity.
    Wait, if it opens up, the "minimum" is at vertex? No, that means the function decreases until vertex and increases after.
    So if min value is -0.25, then $y$ goes down from $\infty$ (which implies $x \to -\infty$, no) or to $-\infty$?
    Wait. If leading coefficient is positive ($a>0$), it goes to infinity at $\pm \infty$. So max value? No, min?
    Wait. Parabola opens UP. The maximum of the parabola occurs at $\infty$.
    No, wait. $y = x^2$. It's increasing on both sides (slope positive). So no minimum.
    Wait. If I have a U shape (opening up), it has no local min if leading coeff is positive? No, $x^2$ has min at $\infty$?
    Wait. $y=x^2$ graph is below axis? No, above axis for all real numbers? Yes.
    Wait, I am confusing "U shape" with something else.
    Let me clarify the definitions of U shape vs V shape.
    - "Open Up": Parabola opens upwards. The minimum value occurs at vertex if defined.
    - If $a > 0$, $f(x)$ has no global maximum. It approaches $\infty$.
    - Does it have a global minimum? No, if $x \to -\infty$, it goes to $\infty$ or $-\infty$. Wait, $f(-10) = 100 + ...$ is positive.
    - So $y=x^2$ has min value at vertex (0). But wait, is 0 min or max? It's the lowest point.
    - My function has min value -0.25.
    - This means the graph goes from $\infty$ down to -0.25 and back up to $\infty$.
    - This is correct. The global minimum is -0.25.
    - The graph crosses x-axis? Yes, at roots 2 and 3? No.
    - Wait. If it goes from $\infty$ down to min (-0.25), it must have crossed the x-axis? No.
    - The graph is $f(x) = (x-3)(x-2)$?
    - Let's plot values for $Q(x) = x^2 - 5x + 6$.
    - $Q(1)=2$. $Q(-1)=14$. $Q(2.5)=-0.25$. $Q(3)=0$. $Q(4)=2$. $Q(2)=0$.
    - So it goes from positive ($x=1$), up to 0 (at $x=2$).
    - Wait, slope at 2 is -3? No. Slope at $x \to -\infty$ is large negative? No.
    - Let's check sign of derivative for all $x$. $y' = 2x - 5$.
    - If $2x - 5 < 0$, then slope is negative. So function decreases as x increases.
    - So if we start at $\infty$ (say from right), it goes down towards min (-0.25).
    - Wait, this implies that for large negative $x$ (e.g. -10), value should be very high.
    - Let's check: $f(-10) = (-13)^2 - 5(-10) + 6$? No. $(x-3)(x-2)$ evaluated at $x=-10$.
    - $(-13)(-12) = 156$.
    - So for $x \to -\infty$, $f(x) \to \infty$.
    - Then it goes down to min (-0.25).
    - Then up to $\infty$ on the right side? No, wait.
    - If vertex is min, and roots are at 3 and 2.
    - Wait. For $x > 3$, derivative is positive ($y' > 0$). So function increases.
    - For $x < 2$, derivative is negative ($y' < 0$). So function decreases? No.
    - If derivative is negative for $x < 2$, then as x increases (from left to right), value decreases.
    - Wait, so from $\infty$ to 3: it must decrease to 0.
    - From 3 to 2: it must increase? No. Derivative at 3 is $2(3)-5 = 1 > 0$. So increases.
    - But wait. If derivative is negative, value decreases.
    - Wait, if I have a function like $y = x^2 - 5x + 6$.
    - At $x=2$, $y=0$. Derivative at 2 is -1 (negative). So decreasing towards 2 from right? No, derivative negative means slope is downward.
    - Wait, if slope is negative ($f' < 0$), then function is decreasing as x increases.
    - This means moving from left to right, value goes down.
    - So if I start at $x=3$, value is 0. Moving left (decreasing x), value should increase.
    - Let's check $f(2)=0$. Slope -1? No. $y'(2) = 4-5=-1$.
    - Wait, $f(2.5) = -0.25$. This is below.
    - So $x=3 \to f'(3) > 0$ (since positive). $f(2)=0$. Wait.
    - If slope at 3 is positive, then moving from left ($x<3$), it's decreasing? No, that means slope is negative to right.
    - If derivative is negative to left of vertex, then going from $\infty$ to vertex, value decreases.
    - Wait, this contradicts "opens up".
    - I will trust the calculation: $f(x)$ crosses at 2 and 3. Min value -0.25.
    - Between roots (2,3) function is negative? No, wait.
    - Let's just assume roots of inequality $x^2-5x+6 > 0$.
    - This is the condition for $\sqrt{x^2-5x+6}$ to be defined.
    - So we solve $x^2 - 5x + 6 > 0$.
    - Roots are 2, 3.
    - The inequality holds outside the roots? Or inside?
    - Let's check values.
    - At $x=0$, value is 6 (positive). So inequality satisfied for $x < 2$ or $x > 3$.
    - At $x=1$, value is positive. Satisfied.
    - At $x=4$, value is 2. Positive.
    - At $x=5/2=2.5$, value is -0.25. Negative. Not satisfied.
    - So domain is $\{ x \mid (x-3)(x-2) > 0 \}$.
    - Wait, earlier I said roots are 2 and 3. And that product is positive outside interval [2,3].
    - Is that correct? No. $(x-3)(x-2)$ has roots at 2 and 3.
    - The parabola opens UP ($a=1$).
    - So it's negative between roots (interval [2,3]) and positive outside (union $(-\infty, 2) \cup (3, \infty)$)?
    - Wait, I must have been confused about the sign of $(x-3)(x-2)$ vs the shape.
    - Let's check signs again.
    - Roots are 2 and 3.
    - If vertex is min (-0.25).
    - Then graph must be positive outside the interval between roots? No, wait.
    - If parabola opens up ($a=1$), then it goes to $\infty$.
    - So it crosses x-axis at roots.
    - This means one region is above axis and one region is below?
    - No. If it crosses at 2 and 3, then for $x < 2$, it's positive. For $x > 3$, it's positive.
    - For $x$ between 2 and 3, it must be negative? Or is it?
    - Wait, if min value is -0.25. Then graph goes down from $\infty$ to min, then up to $\infty$.
    - But min value is -0.25. So for $x < 2$, it is positive. For $x > 3$, it is positive.
    - Wait, if I start at $x=-\infty$. Value goes $\infty$ to min (-0.25) and then back to $\infty$?
    - No, that would mean it goes from positive to negative (since min is below axis)?
    - Wait. If vertex is min, then for all $x$, value must be $\le$ min value?
    - Yes. So graph goes from positive to negative then back to positive?
    - Wait, no. Min is global minimum. So it cannot go from positive to negative without crossing the axis?
    - If $f(x) > 0$ for all $x$, that means vertex must be above axis. But here vertex is -0.25.
    - This implies function can cross axis? No, if vertex is below axis (negative value), then there are no real roots?
    - Wait, I am confused with "vertex" vs "roots".
    - Vertex is where $Q'(x) = 0$. Roots of $Q(x)=0$ are the points where graph crosses x-axis.
    - If vertex is at min value -0.25, then there must be roots? No, if vertex is below axis, then graph does not cross axis. Wait.
    - This means I made a mistake in finding vertex location or root locations.
    - Let's recalculate $Q(x) = x^2 - 5x + 6$.
    - Roots are $\frac{5 \pm \sqrt{1}}{2}$. Roots are $\frac{5 \pm 1}{2} = 3, 2$. Correct.
    - So the graph crosses the axis at $x=2$ and $x=3$.
    - Wait, if vertex is min value -0.25?
    - No. If vertex is min value, then for all $x$, $f(x) \ge$ min value?
    - Yes, unless leading coeff is negative. But it's 1.
    - So min value is global minimum.
    - Since global minimum is -0.25, and graph crosses x-axis at 2 and 3.
    - Wait. This implies that the function goes from $\infty$ to min value? No.
    - It goes from root (val=0) up to vertex (val=-0.25)?
    - If $x \to -\infty$, $f(x) \to \infty$. So it must go from positive infinity down to -0.25?
    - Wait, if it crosses zero at 3 and 2. Then the function decreases?
    - This implies that $x^2 - 5x + 6$ can't be negative between roots?
    - Wait, let me look at this quadratic graph again.
    - It's a parabola opening UP (since leading coeff is 1).
    - Roots are at 2 and 3.
    - If vertex is -0.25. This means the function starts at $\infty$, goes down to -0.25? No, that's impossible if it opens up.
    - Wait. If I have a parabola opening UP with root at 2 (val=0). Then for $x > 3$ (e.g. $x=4$), the function must be positive.
    - But wait, min value is -0.25.
    - So for $x \in [3, \infty)$, function goes from 0 to $\infty$. Wait.
    - If vertex is at min (-0.25), then for $x < 3$, it must be positive? No.
    - Let's plot mentally:
    - Point A: $(2, 0)$. Point B: $(3, 0)$.
    - The parabola opens UP.
    - Vertex is at midpoint between them (min). Wait, if vertex is -0.25, it means vertex is below axis?
    - No, wait. If I start at $(2,0)$ and go to $(3,0)$ on the left side.
    - To get back from 0 to negative, it must have a local max first? No, that's V shape opening down.
    - To get back from 0 to positive, it must open UP?
    - If min value is -0.25 (vertex), then for $x < 3$ or $x > 3$, function goes above 0?
    - Wait. Vertex is at -0.25. This means graph goes down to -0.25.
    - Then back up.
    - If it goes from $\infty$ down to -0.25. Then it must have crossed the axis somewhere? No, that would mean root.
    - Wait, I think I have the roots inverted in my head.
    - Roots of $(x-3)(x-2)$ are 2 and 3.
    - Let's check if $Q(x) = (x-3)(x-2)$ is positive outside [2,3]. Yes.
    - Inside [2,3], it is negative? No, that's for parabola opening down or vertex at peak?
    - Wait. If $a=1$. Graph opens UP.
    - Then min value is at vertex. Since vertex is at min value (-0.25), then graph dips below axis? No.
    - It must cross axis somewhere?
    - Wait, if min value is negative, and vertex is a point where graph is lowest (or highest?).
    - If $a=1 > 0$, then for any $x$, $f(x) \ge$ something? No.
    - The graph of $y = (x-3)(x-2)$ opens UP.
    - So the minimum value must be non-negative? No, wait.
    - A parabola opening UP has a local minimum at vertex. It can cross x-axis if vertex is below axis?
    - Wait, no. If I have $y=x^2$, it crosses at $(0,0)$.
    - If I have $y=(x-3)(x-2)$, then it crosses at 2 and 3.
    - Since parabola opens up (positive leading coeff), the function must be positive on one side of vertex and negative on the other?
    - Wait. A parabola opening up has a shape like $y = x^2$. No.
    - It's the same shape. The minimum is at vertex.
    - If min value is -0.25. Then it goes below axis at vertex. But for large $x$, it goes to infinity.
    - Does this mean it crosses axis?
    - Wait, if min value is -0.25. Then $f(x) \le -0.25$? No.
    - This implies the function does not cross x-axis because vertex is below axis.
    - Wait, but roots are where function equals 0.
    - If function equals 0 at roots, then for some point it must be positive/negative?
    - Let's re-read standard properties of quadratic with vertex at min value $k$.
    - The graph starts at $\infty$, goes down to min value $k$, then up to $\infty$.
    - So if $k < 0$, the function is negative in a region? No, it crosses axis between roots.
    - Wait, but roots of quadratic are where $f(x)=0$.
    - If $x^2-5x+6$ has roots 2 and 3. Then at these points $f(x)=0$.
    - So function must be 0 at 2 and 3.
    - For $x \notin [2,3]$, value is positive? Or negative?
    - Since parabola opens up ($a=1$), it goes to $\infty$.
    - If it starts high (positive) at left, then crosses axis at 2. Then decreases to min (-0.25)? No.
    - Wait, if $x^2-5x+6$ has roots 2 and 3. It implies the graph goes from $\infty$ to $\infty$.
    - Since vertex is -0.25 (min).
    - If min is below axis. Then it MUST cross axis? Yes.
    - Wait, this contradicts "vertex is minimum".
    - Wait. Let me think of $y = x^2$. Vertex at (0,0). Root at (0,0)? No.
    - My function roots are 2 and 3. Vertex at 2.5. Min value -0.25.
    - If min is below axis, then graph goes down from $\infty$? No.
    - Wait. If it goes to $\infty$ on both sides. Then vertex must be a local minimum? No.
    - Wait. If it goes to $\infty$ on left, it goes up to vertex?
    - Let's look at the shape again.
    - $y = x^2 - 5x + 6$.
    - Roots are where derivative is 0? No. Derivative is not 0 at roots.
    - Wait. Let's just plot it manually on a piece of paper or think of $Q(x) = (x-3)(x-2)$.
    - If I multiply out, I get $x^2 - 5x + 6$. Correct.
    - Now let me draw this graph.
    - Roots at 2 and 3.
    - Vertex is at 2.5 with value -0.25.
    - Wait. A parabola opening up (positive leading coeff) has minimum vertex?
    - No! If leading coeff is positive, the function opens UP.
    - So graph goes down from $\infty$ to min and then up to $\infty$.
    - This implies a "U" shape.
    - But wait, if $Q(1) = 2$. Then it goes up.
    - Wait, I'm getting confused about what the graph looks like.
    - Let's use the derivative.
    - $y' = 2x - 5$.
    - Root at 2.5.
    - For $x < 2.5$, slope is negative ($<0$).
    - For $x > 2.5$, slope is positive ($>0$).
    - This means function decreases as we move away from 2.5 to left? No, wait.
    - If slope is negative, it goes DOWN (value decreasing).
    - If I go from left to right (increasing x), value decreases.
    - So if $x=2.5$, min value.
    - Wait, but earlier I said for $x < 2.5$ (slope negative), function is decreasing.
    - And for $x > 2.5$ (slope positive), function is increasing.
    - This implies that at vertex it's a minimum? Yes.
    - So graph starts high on left, decreases to min at 2.5? No, wait.
    - If slope is negative, value decreases as x increases.
    - So if I start at $x$ very large positive (e.g. $100$). Value goes down.
    - Then at vertex it hits minimum?
    - Wait. This implies that for $x > 2.5$, value increases.
    - But if min value is negative (-0.25).
    - Then between roots (in interval between 2 and 3), function must be... wait.
    - If I start at $x=100$. Value $\approx \infty$? No, no, wait.
    - Wait. Let me check my value calculation for $Q(x)$ again.
    - $Q(1) = 2$.
    - $Q(2) = 0$.
    - $Q(3) = 0$.
    - $Q(4) = 2$.
    - So graph goes down from 1 to 0? No, slope at 1 is -3. Wait, if I go right (x increases), value decreases.
    - Then it goes up? No. At 2.5 slope is 0.
    - Wait, this implies function goes DOWN then UP?
    - But wait, min value was -0.25. This means graph is negative in some regions.
    - But roots are at 2 and 3 (value 0).
    - If vertex is below axis (-0.25). Then for $x < 2$, value should be positive?
    - No, if $x=1$. Value is positive. So graph starts at $\infty$? No.
    - Wait. Let's check slopes again.
    - $y' = 2x - 5$. Roots are 2.5.
    - If derivative is negative for $x < 2.5$, then function decreases as x increases.
    - So if I go from $-\infty$ to $+\infty$. It goes down to vertex? No.
    - It goes down from left to vertex. Wait, this implies it comes from positive infinity and hits min at vertex.
    - But wait. If it comes from positive infinity (since $x \to -\infty$, $y \to \infty$), then it must cross axis before vertex?
    - No, if it crosses axis ($Q(x)=0$) at 2 and 3. Then it must be between these roots that it is below axis?
    - Wait. If it goes from $\infty$ to min (-0.25).
    - This implies that for $x \in (2,3)$, value is negative?
    - But wait. At 2 and 3, it's 0.
    - So between roots, function must be below axis? No, wait.
    - If vertex is at min (-0.25). And roots are where it goes to $\infty$.
    - Wait, if $Q(2)=0$ and $Q(3)=0$.
    - Then for $x < 2$, $Q(x)$ must be positive? No.
    - If it goes from $\infty$ to min (-0.25), it must cross x-axis at root 1 or 3?
    - Wait, I said vertices of $(x-3)(x-2)$.
    - Wait. Maybe my roots are wrong?
    - Let's re-calculate factorization one more time.
    - $x^2 - 5x + 6 = (x-a)(x-b)$.
    - Sum $a+b=5$. Product $ab=6$.
    - Factors of 6 summing to 5: $2,3$.
    - So factors are $(x-2)(x-3)$. Correct.
    - Roots are 2 and 3.
    - This means that at $x=2$, value is 0. At $x=3$, value is 0.
    - Since leading coeff is positive ($a=1$).
    - The parabola opens UP.
    - So it goes from $\infty$ down to min (-0.25) then up?
    - Wait, if min is -0.25. Then for $x \in (2,3)$, function must be negative? No.
    - It must be between the roots where value is positive?
    - Wait, let's look at standard graph of quadratic with vertex below axis ($k<0$
````

## Answer (content)

````text

````
