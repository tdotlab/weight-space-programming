# test/algebra/1143.json (Algebra, level 5)

> The smallest distance between the origin and a point on the graph of $y=\frac{1}{2}x^2-9$ can be expressed as $a$.  Find $a^2$.  

**Wrong.** Gold `17`, predicted `None`. Finish: length, 8192 tokens, 4 waits, 680.4 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

The user wants to find the smallest distance between the origin $(0,0)$ and any point $(x,y)$ on the graph of the function $y = \frac{1}{2}x^2 - 9$.  
Then, I need to find the square of this minimum distance, denoted as $a^2$.  

**1. Formulate the problem mathematically:**  
The equation of the curve is a parabola opening upwards with its vertex at $(0, -9)$.  
We want to find a point $(x,y)$ on this curve such that the distance from the origin $(0,0)$ to $(x,y)$ is minimized.  
Let $D$ be the distance between the origin and the point $(x,y)$.  
The coordinates are $P(x, y)$. So $D = \sqrt{(x-0)^2 + (y-0)^2} = \sqrt{x^2 + y^2}$.  

Substitute $y$ in terms of $x$:  
$y = \frac{1}{2}x^2 - 9$.  

So the distance function is a function of $x$:  
$f(x) = D(x) = \sqrt{x^2 + (\frac{1}{2}x^2 - 9)^2}$.  

To minimize $D(x)$, it's sufficient to minimize the squared distance $f(x)^2$, provided $f(x)$ is non-negative (which it is), and since the function inside the square root is strictly positive for all real $x$ (except at vertex which is negative), minimizing $f(x)$ is equivalent to minimizing the square of the distance.  
Let $g(x) = f(x)^2 = x^2 + (\frac{1}{2}x^2 - 9)^2$.  

**2. Minimize the function $g(x)$:**  
$g(x) = x^2 + \left(\frac{1}{2}x^2 - 9\right)^2$  
$g(x) = x^2 + (\frac{1}{4}x^4 - 2(9)(\frac{1}{2})x^2 + 81)$  
$g(x) = x^2 + \frac{1}{4}x^4 - 9x^2 + 81$  
Simplify:  
$g(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  

Let $u = x^2$. Since $x$ is a real number, $u \ge 0$.  
$h(u) = \frac{1}{4}u^2 - 8u + 81$.  

We need to find the minimum value of this quadratic function $h(u)$ for $u \ge 0$.  
This is a parabola opening upwards ($a > 0$). The vertex occurs at $u = \frac{-b}{2a}$.  
Here, the coefficient of $u^2$ is $1/4$, the coefficient of $u$ is $-8$.  
$u_{min} = \frac{8}{2(1/4)} = \frac{8}{1/2} = 16$.  

Is this $u$ within the domain $u \ge 0$? Yes, $16 \ge 0$.  
So the minimum occurs at $x^2 = 16$, which means $x = 4$ or $x = -4$.  

Let's calculate the minimum value of $g(x)$ (which is the square of the distance).  
$h(16) = \frac{1}{4}(16)^2 - 8(16) + 81$  
$h(16) = \frac{1}{4}(256) - 128 + 81$  
$h(16) = 64 - 128 + 81$  
$h(16) = 80$.  

So the minimum square of the distance is $a^2 = 80$.  
The value of $a$ would be $\sqrt{80} = \sqrt{16 \cdot 5} = 4\sqrt{5}$.  
The question asks for $a^2$. So the answer should be 80.  

**Alternative Method: Calculus/Derivatives**  
Distance function squared: $y(x) = (\frac{1}{2}x^2 - 9)^2 + x^2$  
Differentiate with respect to $x$:  
$y'(x) = 2(\frac{1}{2}x^2 - 9)(\frac{1}{2} \cdot 2x) + 2x$  
$y'(x) = (x^2 - 9)x + 2x$  
$y'(x) = x(x - 9) + 2x$  
$y'(x) = x^2 - 9x + 2x$  
$y'(x) = x^2 - 7x$  

Set derivative to zero:  
$x^2 - 7x = 0$  
$x(x - 7) = 0$  
Critical points at $x = 0$ and $x = 7$.  
We need to check the second derivative or just evaluate the function values at these critical points.  

$g(x) = \frac{1}{4}x^4 - 8x^2 + 81$  
$g'(x) = x^3 - 16x$.  
Set $g'(x) = 0$:  
$x(x^2 - 16) = 0$  
Roots are $x=0, x=4, x=-4$.  

Let's re-evaluate $y'$ from the beginning to be sure.  
Wait, if I calculate derivative of $x^2 + (\frac{1}{2}x^2 - 9)^2$:  
$d/dx(x^2) = 2x$.  
$d/dx((\frac{1}{2}x^2 - 9)^2) = 2(\frac{1}{2}x^2 - 9)(x) = x(x-9)$? No, $\frac{d}{dx}(A^2) = 2A A'$.  
$A = \frac{1}{2}x^2 - 9$, $A' = x$. So $2(\frac{1}{2}x^2 - 9)(x) = (x^2 - 18)x$.  
My previous calculation:  
$g(x) = x^2 + \frac{1}{4}x^4 - 9x^2 + 81 = \frac{1}{4}x^4 - 8x^2 + 81$.  
$g'(x) = 4(\frac{1}{4}x^3) - 16x = x^3 - 16x$.  
Ah, previously I had $y'(x) = x^2 - 7x$ from a calculation error. Let's re-verify the algebraic simplification of $g(x)$.  

Original expression: $y = \frac{1}{2}x^2 - 9$.  
Squared distance term: $(\frac{1}{2}x^2 - 9)^2$.  
Expansion: $\frac{1}{4}x^4 - 2(\frac{1}{2}x^2)(9) + 81 = \frac{1}{4}x^4 - 9x^2 + 81$.  
Adding $x^2$: $x^2 + \frac{1}{4}x^4 - 9x^2 + 81 = \frac{1}{4}x^4 - 8x^2 + 81$. This was correct.  
Derivative: $\frac{d}{dx}(\frac{1}{4}x^4) = x^3$. $\frac{d}{dx}(-8x^2) = -16x$.  
So $g'(x) = x^3 - 16x$.  
Setting to 0: $x(x^2 - 16) = 0 \Rightarrow x=0, \pm 4$.  

Let's check the point on the derivative $x=x_{vertex}$.  
At $x=0$, $g(0) = 81$. Distance squared is 81. Distance is $\sqrt{81} = 9$.  
At $x=4$, $g(4) = \frac{1}{4}(256) - 8(16) + 81 = 64 - 128 + 81 = 176 - 128 = 48$?  
Let me re-calculate.  
$h(16) = \frac{1}{4}(16)^2 - 8(16) + 81$.  
$16^2 = 256$. $256 / 4 = 64$.  
$-8 * 16 = -128$.  
$64 - 128 + 81 = 145 - 128$? No.  
$64 + 81 = 145$.  
$145 - 128 = 17$.  

Something is wrong. Let's re-calculate $h(16)$.  
$x^2 = 16$.  
Term 1: $\frac{1}{4}x^4 = \frac{1}{4}(256) = 64$.  
Term 2: $-8x^2 = -8(16) = -128$.  
Term 3: $+81$.  
Sum: $64 - 128 + 81$.  
$64 + 81 = 145$.  
$145 - 128 = 17$.  
So minimum is 17?  

Let's check the distance formula directly.  
Vertex of parabola is at $(0, -9)$. Distance from origin to vertex is $\sqrt{0^2 + (-9)^2} = 9$. So distance squared is $81$.  
Is this a critical point?  
Derivative at $x=0$: $g'(0) = 0(4-0)? No, g'(0)=0$.  
Let's check the value of $y(x)$ at $x=0$. $y=-9$. $d^2 = 81$.  
Is it a local minimum?  
$g(x) = x^2 + y(x)^2$.  
Around $x=0$, $y \approx -9$.  
Let's check sign of $y'$ again.  
$f(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  
At $x=4$: $17$. $\sqrt{17} \approx 4.12$.  
$4 < 9$. So $x=0$ is not the global minimum, and actually not the critical point I was getting in the previous "alternative method" (derivative of distance squared).  

Where did I make a mistake in the first attempt?  
$g(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
$g'(x) = 2x + 2(\frac{1}{2}x^2 - 9)(x)$.  
$g'(x) = 2x + (x^3 - 9x)$.  
$g'(x) = x^3 + 2x - 9x$? No.  
Let's be very careful with the product rule.  
$\frac{d}{dx} [(\frac{1}{2}x^2 - 9)^2] = 2 \cdot (\frac{1}{2}x^2 - 9) \cdot \frac{d}{dx}[\frac{1}{2}x^2 - 9]$  
$= 2 \cdot (\frac{1}{2}x^2 - 9) \cdot (x)$  
$= (x^2 - 9)x = x^3 - 9x$.  

So, $g'(x) = \frac{d}{dx}(x^2) + g_{quad}'(x)$  
$g'(x) = 2x + x^3 - 9x$  
$g'(x) = x^3 - 7x$.  

Setting this to zero: $x(x^2 - 7) = 0$.  
Roots are $x=0, \pm\sqrt{7}$.  
Let's check which one gives the minimum.  
At $x=0$: $g(0) = 0 + (-9)^2 = 81$.  
At $x=\sqrt{7}$:  
$g(\sqrt{7}) = (\sqrt{7})^2 + (\frac{1}{2}(7) - 9)^2$  
$= 7 + (3.5 - 9)^2$  
$= 7 + (-5.5)^2$  
$= 7 + 30.25 = 37.25$.  
Is this the minimum?  
Let's check my previous polynomial expansion.  
$g(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  
Derivative: $\frac{d}{dx}(\frac{1}{4}x^4) = x^3$. $d/dx(-8x^2) = -16x$. $d/dx(81) = 0$.  
So $g'(x) = x^3 - 16x$.  
Why are the derivatives different?  

Let's re-expand:  
$y = \frac{1}{2}x^2 - 9$  
$y^2 = (\frac{1}{2}x^2)^2 - 2(\frac{1}{2}x^2)(9) + (-9)^2$  
$y^2 = \frac{1}{4}x^4 - 9x^2 + 81$.  
Total $g(x) = x^2 + y^2 = x^2 + \frac{1}{4}x^4 - 9x^2 + 81$  
$g(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  
Derivative of $\frac{1}{4}x^4$: $x^3$.  
Derivative of $-8x^2$: $-16x$.  
Sum: $x^3 - 16x$.  

Now let's re-check the derivative using product rule directly on $g(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
$g'(x) = 2x + 2(\frac{1}{2}x^2 - 9)(x)$  
$= 2x + (x^3 - 9x)$  
$= x^3 - 7x$.  

The contradiction comes from the expansion of $(\frac{1}{2}x^2 - 9)^2$.  
Expansion check:  
$A = \frac{1}{2}x^2$. $B = 9$. $(A-B)^2 = A^2 - 2AB + B^2 = (\frac{1}{4}x^4) - 2(\frac{1}{2}x^2)(9) + 81 = \frac{1}{4}x^4 - 9x^2 + 81$.  
Sum with $x^2$: $\frac{1}{4}x^4 - 8x^2 + 81$.  

Let's re-differentiate the expanded form.  
$d/dx(\frac{1}{4}x^4) = x^3$.  
$d/dx(-8x^2) = -16x$.  
Result: $x^3 - 16x$.  

Why did the product rule give $x^3 - 7x$?  
Ah. $g(x) = (\frac{1}{4}x^4 - 9x^2 + 81)$? No, $y^2$.  
Let's check $2(\frac{1}{2}x^2 - 9)(x) = x^3 - 18x$?  
Let's recompute: $2 \cdot (\frac{1}{2}x^2 - 9) \cdot (x)$  
$= (x^2 - 18)x$? No.  
$(\frac{1}{2}x^2 - 9) = \frac{1}{2}x^2 - 9$.  
Multiply by $2x$: $2x(\frac{1}{2}x^2 - 9) = x^3 - 18x$.  
Ah, in the previous step I wrote $(x^3 - 9x)$. Where did I lose a factor of 2?  
$(\frac{1}{2}x^2 - 9)$ multiplied by $2x$:  
First term: $2x \cdot \frac{1}{2}x^2 = x^3$.  
Second term: $2x \cdot (-9) = -18x$.  
So derivative of the square term is $x^3 - 18x$.  
Total derivative: $g'(x) = 2x + x^3 - 18x = x^3 - 16x$.  

Okay, my first product rule application was sloppy ($x^3 - 9x$ vs $x^3 - 18x$). The expanded form was correct.  
So the critical points are from $x^3 - 16x = 0$, which gives $x(x^2 - 16) = 0$.  
Roots: $x=0, \pm 4$.  

Evaluating at these points:  
1. $x=0$: $g(0) = 81$.  
2. $x=4$: $g(4) = 64 - 128 + 81 = 17$? No, let's re-evaluate $64 - 128 + 81$.  
$64 + 81 = 145$.  
$145 - 128 = 17$.  
Let's check the function value again.  
$g(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
At $x=4$:  
$y = \frac{1}{2}(16) - 9 = 8 - 9 = -1$.  
$d^2 = 4^2 + (-1)^2 = 16 + 1 = 17$. Correct.  
3. $x=-4$: Symmetry, distance squared is same, 17.  

Comparing values:  
$g(0) = 81$.  
$g(\pm 4) = 17$.  
Since $17 < 81$, the minimum is at $x = \pm 4$.  
The minimum squared distance is 17.  

Let's double check if I missed any other critical points or boundaries. The domain of $x$ is $(-\infty, \infty)$. $g(x)$ is a polynomial with leading term $\frac{1}{4}x^4$, so it goes to $\infty$. Thus global minimum exists at critical point.  
The vertex of parabola $y = \frac{1}{2}x^2 - 9$ is $(0, -9)$. Distance from origin is 9. Square is 81.  
As $x$ increases, curve moves up (away from origin in y-direction?) and right or left?  
Parabola vertex at $(0,-9)$. Origin is at $(0,0)$. Distance is 9.  
Wait, if parabola opens upward, points with large $x$ will be far away? No, $y \approx x^2/2$. Points like $(4, -1)$ are close to origin?  
Origin is $(0,0)$. Point $(4,-1)$ distance is $\sqrt{17} \approx 4.12$. Origin is at $y=0$. Curve vertex at $y=-9$.  
Is it possible for the curve to be closer to origin?  
The vertex is furthest inwards vertically from x-axis, but at $x=0$ distance is 9.  
At $x=\pm 4$, $y=-1$, so point is $(\pm 4, -1)$. Distance $\sqrt{17} \approx 4.12 < 9$.  
This makes sense. The curve dips down to -9 and goes back up. But the shape is a parabola opening upwards.  
The closest point to origin on a convex function from $(0,0)$ (if it were the axis of symmetry) would be at the vertex. Here the "axis" shifts relative to the y-axis? No.  
It's just geometry.  
Let's consider the circle centered at origin $x^2+y^2=r^2$. We want intersection with parabola.  
Substitute: $x^2 + (\frac{1}{2}x^2 - 9)^2 = r^2$.  
$g(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  
We want min of $g(x)$ for real $x$.  
We found min is 17.  
So distance is $\sqrt{17}$.  

Let me verify the question wording again. "Smallest distance between the origin and a point on the graph". Yes.  
Equation: $y = \frac{1}{2}x^2 - 9$.  
Distance squared: $x^2 + y^2 = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
Let $t = x^2/2$, then $y=t-9$ and $x=\sqrt{2t}$. Maybe substitute?  
$x^2 = 2t, x^4 = 4t^2$.  
Function becomes $4t^2 + (2t-9)?$ No.  
Substitute $u=x^2/2$, so $y=u-9$ is wrong because $x$ and $u$ are not independent variables easily for substitution back?  
Actually, $y = \frac{1}{2}x^2 - 9 \implies y+9 = \frac{1}{2}x^2 \implies x^2 = 2(y+9)$.  
Distance squared: $D^2 = x^2 + y^2$.  
Substitute $x^2 = 2(y+9)$?  
$D^2 = 2(y+9) + y^2 = y^2 + 2y + 18$.  
We want to minimize this quadratic in $y$.  
The range of $y$ on the graph is $(-\infty, \infty)$.  
Since coefficient of $y^2$ is positive (parabola opens up), min value is at vertex of this new parabola.  
Vertex of $D^2(y) = y^2 + 2y + 18$ occurs at $y = -b/2a = -2 / (2*1) = -1$.  
Is this in the range? Yes, the graph contains all $y \in (-\infty, \infty)$ as $x^2$ ranges over $(0, \infty)$, and $y$ covers $(-9, \infty)$? No.  
Let's check domain of $y$. $x$ is any real number.  
$x^2 = 2(y+9)$. So $x^2 \ge 0 \implies y+9 \ge 0 \implies y \ge -9$.  
So the graph exists only for $y \ge -9$.  
The parabola we just found, $D^2(y)$, has vertex at $y=-1$. Since $-1 \ge -9$, this minimum is attainable on the curve.  

Let's verify values at endpoints? No, it's a quadratic.  
Min value at $y = -1$:  
$D^2_{min} = (-1)^2 + 2(-1) + 18 = 1 - 2 + 18 = 17$.  
Matches my previous calculation.  

So the minimum squared distance is 17.  
The question asks for $a^2$. The smallest distance is $\sqrt{17}$. Let $d_{min} = \sqrt{17}$. The problem says "can be expressed as $a$". This implies $a = d_{min}$. No, "smallest distance ... can be expressed as $a$. Find $a^2$."  
This phrasing is slightly ambiguous. Usually $a$ denotes the distance itself. So $a^2$ is the square of the distance. Or it might mean "find $a$, where $a^2$ is the minimum value".  
Let's re-read: "The smallest distance ... can be expressed as $a$. Find $a^2$."  
This implies $a$ is the distance. So I should output the square of that distance. Or does it mean find $a$ given that expression? No, it asks for a specific value.  
Is $a$ just the minimum distance? Or does "expressed as $a$" define what $a$ stands for? Yes, usually means $a = \sqrt{17}$. Then finding $a^2$ gives 17.  

Let's double check the interpretation of "smallest distance ... expressed as $a$".  
Usually this would mean $d_{min} = a$. Then "Find $a^2$" asks for $d_{min}^2$.  
If it meant "the smallest distance is the number $x$, find $x^2$", then the answer is 17.  

Let me double check the problem statement source or similar problems. Usually "distance can be expressed as $\sqrt{...}$". No, usually numbers.  
Is there any interpretation where $a$ is something else?  
Maybe "smallest distance ... expressed as $a$" means finding a simplified radical form.  
Example: "The area of the triangle has height $h$ and base $b$. Find $a^2$." This would be confusing if it meant find $a$. It says "can be expressed as $a$". So $a$ is the value of the distance.  

Let's re-read carefully: "The smallest distance between the origin and a point on the graph of $y=\frac{1}{2}x^2-9$ can be expressed as $a$. Find $a^2$."  
This phrasing implies $a$ is a number representing the distance. So calculate the minimum distance, then square it.  
My calculated minimum distance is $\sqrt{17}$.  
So $a = \sqrt{17}$.  
Then $a^2 = 17$.  

Is it possible that $x$ or $y$ has a specific value constraint? "point on the graph". No.  
Let me confirm the calculations one more time.  
Point $(x,y)$ on $y = x^2/2 - 9$.  
Distance squared from origin: $r^2 = x^2 + y^2$.  
Substitute $y$: $r^2 = x^2 + (x^2/2 - 9)^2$  
$r^2 = x^2 + \frac{x^4}{4} - 9x^2 + 81$  
$r^2 = \frac{x^4}{4} - 8x^2 + 81$.  
Let $t = x^2$. Since $(x)^2 \ge 0$, $t \ge 0$.  
Function of $t$: $f(t) = \frac{1}{4}t^2 - 8t + 81$.  
Minimize $f(t)$ for $t \ge 0$.  
Vertex at $t = -(-8)/(2*1/4) = 8 / (1/2) = 16$.  
Since $16 \ge 0$, the minimum is at $x^2=16$.  
Value: $f(16) = \frac{1}{4}(256) - 8(16) + 81 = 64 - 128 + 81 = 17$.  
$r_{min} = \sqrt{17}$.  
So $a = \sqrt{17}$.  
$a^2 = 17$.  

Is there any trick?  
Maybe graph is in complex plane? No, "graph of y=f(x)" implies Cartesian coordinates.  
Maybe the origin is not $(0,0)$? "origin" usually means $(0,0)$.  
Maybe $y = \frac{1}{2}x^2 - 9$ is interpreted differently? Standard form.  
Is it possible to misinterpret "smallest distance"? No.  

Let's check alternative approach with geometry intuition again.  
Parabola opens up vertex at $(0,-9)$.  
Points on parabola are $(x, x^2/2 - 9)$.  
We want to find point on curve closest to origin.  
Consider tangent line from origin? No, that gives a line.  
Consider distance function level sets (circles). $x^2 + y^2 = k$.  
Intersection with parabola $y = \frac{1}{2}x^2 - 9$.  
$x^2 + (\frac{1}{2}x^2 - 9)^2 = k$.  
$g(x) = x^2 + (\frac{1}{2}x^2 - 9)^2 = k$.  
We need to find if there is a $k$ such that system has solution.  
Since we want smallest distance, we look for min of $g(x)$. We did this and got 17.  
Is it possible the origin is "inside" the parabola? Yes, vertex is $(0,-9)$, so $(0,0)$ is on y-axis at $y=0$, which is above vertex. The curve goes from $y=-\infty$ (as $x \to -\infty$) to $y=\infty$.  
But the distance function is strictly convex?  
$r^2 = \frac{1}{4}x^4 - 8x^2 + 81$. As $|x| \to \infty$, $r^2 \to \infty$. Minimum is at finite point.  
So yes, global minimum is at $x^2=16$.  

Let's do a quick check with Python code simulation mentally.  
Equation: minimize $(\frac{1}{2}x^2 - 9)^2 + x^2$.  
Derivative w.r.t $x$: $(x^3 - 18x) + 2x = x^3 - 16x$ ? No.  
$\frac{d}{dx} [(\frac{1}{2}x^2 - 9)^2] = 2(\frac{1}{2}x^2 - 9)(x) = x^3 - 9x$?  
Hold on.  
Product rule: $u=v, v=const$. No.  
$\frac{d}{dx}(f(x)^2) = 2 f(x) f'(x)$.  
$f(x) = \frac{1}{2}x^2 - 9$.  
$f'(x) = x$.  
So $\frac{d}{dx}(f(x)^2) = 2(\frac{1}{2}x^2 - 9)(x) = (x^2 - 18)x = x^3 - 18x$.  
Then $g'(x) = \frac{d}{dx}(x^2 + f(x)^2) = 2x + x^3 - 18x = x^3 - 16x$.  
So critical points are $x=0, \pm 4$.  
Values:  
$g(0) = 81$.  
$g(4) = 17$.  
This is robust. The previous error was calculating derivative of $(\frac{1}{2}x^2-9)^2$ as $(x^2-9)x$, but the coefficient $1/2$ needs to be handled carefully?  
$(\frac{1}{2}x^2 - 9) = \frac{1}{2}x^2 - 9$.  
Multiply by $2x$:  
$2x(\frac{1}{2}x^2 - 9) = x^3 - 18x$.  
Correct.  
Why did I get $x^3 - 16x$ in the second thought block?  
Ah, because $g(x)$ was expanded to $\frac{1}{4}x^4 - 8x^2 + 81$.  
Derivative of that is $x^3 - 16x$.  
Let's check if $\frac{d}{dx}(g_{quad}) = \frac{d}{dx}(x^2 + y^2)$.  
$y^2 = \frac{1}{4}x^4 - 9x^2 + 81$.  
$d(y^2)/dx = x^3 - 18x$.  
$d(x^2)/dx = 2x$.  
Sum: $x^3 - 16x$.  
Both methods yield $x^3 - 16x$.  
So critical points are correct.  

Check values again.  
$g(4) = \frac{1}{4}(4)^4 - 8(4)^2 + 81$  
$= \frac{1}{4}(256) - 8(16) + 81$  
$= 64 - 128 + 81$  
$= 17$.  

Check $g(-4)$: Same.  
Is there a mistake in "substitute $x^2=2(y+9)$"?  
$D^2 = x^2 + y^2 = 2(y+9) + y^2$.  
Range of $y$: Parabola is defined for all real $x$, so $y$ can be any value $\ge -9$.  
Let's check the vertex of $D^2$ in terms of $y$.  
Parabola opening up. Min value of $D^2$ wrt $y$?  
The parabola is just a set of points $(x,y)$.  
But we are minimizing distance from origin to points on the curve.  
Using parametrization $y = x^2/2 - 9 \implies x^2 = 2(y+9)$.  
Distance squared $D^2 = x^2 + y^2$.  
Substituting $x^2$ with $2(y+9)$ gives a function of $y$:  
$f(y) = 2(y+9) + y^2 = y^2 + 2y + 18$.  
This is valid because for any real $x$, there is a unique $y$, and every point on the graph corresponds to a unique $y$ (with range $[-\infty, \infty)$? No).  
The graph of $y = x^2/2 - 9$. As $x$ goes from $-\infty$ to $\infty$, $y$ goes from $-\infty$ to $\infty$ only if coefficient is positive. Coefficient is $1/2 > 0$. So range of $y$ is indeed $(-\infty, \infty)$.  
So we can treat $f(y)$ as a function on $\mathbb{R}$.  
Minimizing $f(y) = y^2 + 2y + 18$.  
Vertex at $y = -1$.  
Value is $(-1)^2 + 2(-1) + 18 = 1 - 2 + 18 = 17$.  
This confirms the result again.  
Note: The vertex condition for $f(y)$ assumes we can reach $y=-1$. Since the domain of $f$ (on graph) is all real numbers, we are good.  

Is there any reason why $x^2=2(y+9)$ might restrict things? No, mapping is bijective on the line where $x^2=y+9$?  
No, $y = \frac{1}{2}x^2 - 9$. So $x^2 = 2(y+9)$. Since $x$ can be $\pm$, $x^2$ can take all non-negative values.  
For a given $y$, is there an $x$? Yes, if $y \ge -9$, there are two points. If $y < -9  

## Answer

*(none: the token cap hit during thinking)*
