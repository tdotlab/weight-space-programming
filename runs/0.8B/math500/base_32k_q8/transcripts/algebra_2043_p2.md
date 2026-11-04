# test/algebra/2043.json, part 2 of 4

[Previous part](algebra_2043.md)

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

*Continued in [part 3 of 4](algebra_2043_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
