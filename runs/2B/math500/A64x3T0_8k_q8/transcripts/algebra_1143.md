# test/algebra/1143.json (Algebra, level 5)

> The smallest distance between the origin and a point on the graph of $y=\frac{1}{2}x^2-9$ can be expressed as $a$.  Find $a^2$.  

**Wrong.** Gold `17`, predicted `None`. Finish: length, 8192 tokens, 1 waits, 677.4 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

The user wants to find the smallest distance between the origin $(0,0)$ and any point $(x,y)$ on the graph of the function $y = \frac{1}{2}x^2 - 9$.  
Then, I need to find the square of this minimum distance, denoted as $a^2$.  

**1. Formulate the problem mathematically:**  
The origin is $O = (0,0)$.  
The graph is a parabola given by $y = \frac{1}{2}x^2 - 9$, which can be written as $x^2 = 2(y+9)$ or $f(x,y) = 0$ where $f(x,y) = y - \frac{1}{2}x^2 + 9$.  

Let a point on the graph be $P = (x, y)$ such that $y = \frac{1}{2}x^2 - 9$.  
Since the function involves only even powers of $x$, $P$ can be parameterized by $(x, \frac{1}{2}x^2 - 9)$.  
The distance squared between $O(0,0)$ and $P(x,y)$ is given by:  
$d(P, O)^2 = x^2 + y^2$.  

**2. Set up the distance function:**  
Let $D$ be the distance between the origin and a point on the curve. To minimize the distance $D$, it suffices to minimize the squared distance $D^2 = x^2 + y^2$.  
Substitute $y = \frac{1}{2}x^2 - 9$ into the expression for $D^2$:  
$$ D^2(x) = x^2 + \left(\frac{1}{2}x^2 - 9\right)^2 $$  

**3. Minimize the function:**  
Let $u = x^2$. Since $(x,y)$ is a point on the real plane, $x$ can be any real number, so $u \ge 0$.  
We want to minimize the function of $u$:  
$$ g(u) = u + \left(\frac{1}{2}u - 9\right)^2 $$  
for $u \in [0, \infty)$.  

First, expand the term $\left(\frac{1}{2}u - 9\right)^2$:  
$$ \left(\frac{1}{2}u - 9\right)^2 = \frac{1}{4}u^2 - 2(\frac{1}{2}u)(9) + 81 = \frac{1}{4}u^2 - 9u + 81 $$  

Now substitute this back into $g(u)$:  
$$ g(u) = u + \frac{1}{4}u^2 - 9u + 81 $$  
$$ g(u) = \frac{1}{4}u^2 - 8u + 81 $$  

This is a quadratic function in terms of $u$. Since the coefficient of $u^2$ is positive ($1/4 > 0$), the parabola opens upwards, so the global minimum is attained at the vertex or near it.  
The vertex occurs at $u = -\frac{b}{2a}$ where $a = \frac{1}{4}$ and $b = -8$.  
$$ u_{min} = -\frac{-8}{2(\frac{1}{4})} = \frac{8}{\frac{1}{2}} = 16 $$  

Since $u$ represents $x^2$, we must have $u=16$. Is $u=16$ a valid value? Yes, because if $x^2 = 16$, then $x = \pm 4$, which are real numbers.  
So the minimum distance squared is at $u=16$.  

**Alternative method: Derivative**  
Let $D^2(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
Take derivative with respect to $x$:  
$$ \frac{d}{dx}(D^2(x)) = 2x + 2(\frac{1}{2}x^2 - 9) \cdot (2x) $$  
$$ \frac{d}{dx}(D^2(x)) = 2x + 2(\frac{1}{2}x - 9)x \quad (\text{chain rule}) $$  
$$ \frac{d}{dx}(D^2(x)) = 2x + (x - 9)x \cdot 2? $$ No, $\frac{d}{du}(u^2) = 2u$, so $\frac{d}{dx}(\dots)^2 = 2(\dots)(\dots)'$.  
Let $y = \frac{1}{2}x^2 - 9$. Then $y' = x$.  
So $\frac{d}{dx}((y-0)^2) = 2y y'$.  
$$ \frac{d}{dx} (x^2 + (\frac{1}{2}x^2 - 9)^2) = 2x + 2(\frac{1}{2}x^2 - 9)(x) $$  
Set this to zero to find critical points:  
$$ 2x + x(\frac{1}{2}x^2 - 9) \cdot \text{no, it's } 2y y' = 2(\frac{1}{2}x^2 - 9)(x) = (x^3 - 18x) $$  
So the equation is:  
$$ 2x + x(\frac{1}{2}x^2 - 9) = 0 $$  
No, this simplification is wrong. $2x + 2(\frac{1}{2}x^2 - 9)(x)$? No.  
Let's redo the derivative carefully.  
$f(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
$f'(x) = 2x + 2(\frac{1}{2}x^2 - 9)(x)$.  
Set $f'(x) = 0$:  
$$ 2x + 2 \cdot x \left( \frac{1}{2}x^2 - 9 \right) = 0 $$  
Divide by 2:  
$$ x + x\left( \frac{1}{2}x^2 - 9 \right) = 0 $$  
Factor out $x$:  
$$ x \left[ 1 + \frac{1}{2}x^2 - 9 \right] = 0 $$  
$$ x \left( \frac{1}{2}x^2 - 8 \right) = 0 $$  
So, the critical points occur when $x=0$ or $\frac{1}{2}x^2 - 8 = 0$.  
Case 1: $x=0$.  
If $x=0$, then $y = \frac{1}{2}(0)^2 - 9 = -9$.  
Point is $(0, -9)$. Distance squared from origin: $0^2 + (-9)^2 = 81$.  

Case 2: $\frac{1}{2}x^2 - 8 = 0 \implies x^2 = 16$.  
If $x = \pm 4$, then $y = \frac{1}{2}(16) - 9 = 8 - 9 = -1$.  
Points are $(\pm 4, -1)$.  
Distance squared from origin: $x^2 + y^2 = 16 + (-1)^2 = 16 + 1 = 17$.  

Comparing the values:  
At $x=0$, distance squared is 81.  
At $x=\pm 4$, distance squared is 17.  
The minimum value is 17.  

Let's double check the logic with the quadratic substitution method (minimizing $g(u)$).  
$g(u) = \frac{1}{4}u^2 - 8u + 81$.  
This corresponds to $x^2+u=x^2 + (\frac{1}{2}x^2-9)^2$. This substitution was $y = \frac{1}{2}x^2-9$, so $\frac{1}{2}x^2-9$ is $u/2 + 81$? No.  
In the second method:  
$g(u) = u + (\frac{1}{2}u - 9)^2$.  
Here $u=x^2 \ge 0$.  
Derivative with respect to $u$:  
$g'(u) = 1 + 2(\frac{1}{2}u - 9)(\frac{1}{2}) = 1 + (\frac{1}{2}u - 9)$.  
$g'(u) = 0 \implies 1 + \frac{1}{2}u - 9 = 0 \implies \frac{1}{2}u = 8 \implies u = 16$.  
So $x^2 = 16$, which implies $|x|=4$.  
This matches the critical point analysis (specifically the non-trivial one).  
The minimum value is $g(16) = 16 + (\frac{1}{2}(16)-9)^2 = 16 + (8-9)^2 = 16 + (-1)^2 = 17$.  
Also check boundary or other critical points. If we consider domain $x \in \mathbb{R}$, then $u \ge 0$. The vertex is at 16 which is in the domain.  
The value $x=0$ corresponds to $u=0$. This is a local extremum?  
Let's check $g''(u) = \frac{d}{du}(1 + \frac{1}{2}u - 9)$? No, derivative of $(\dots)^2$ term is different when using $u=x^2$ directly.  
Let's stick to the direct variable $x$.  
The derivative calculation earlier:  
$f'(x) = 2x + x(x-9)/ (1/2 x?) \rightarrow 2x + (x-9)x \dots$  
Let's re-evaluate $f'(x)$ properly.  
$f(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
$f'(x) = 2x + 2(\frac{1}{2}x^2 - 9)(x)$. (Note: chain rule gives $2(y)\cdot y'$ where $y=x^2/2-9$ so $y'=x$).  
So $f'(x) = 2x + x(2y)$? No.  
$f'(x) = 2x + 2(\frac{1}{2}x^2 - 9)(x)$. This seems incorrect. The second term is $(\frac{1}{2}x^2-9)^2$. Let $v = \frac{1}{2}x^2-9$. Then $\frac{d}{dx} v^2 = 2v v' = 2(\frac{1}{2}x^2-9)(x)$.  
So the derivative is $f'(x) = 2x + x(\frac{1}{2}x^2 - 9) \cdot 2$? No.  
Let's do step by step again.  
Term 1: $\frac{d}{dx}(x^2) = 2x$.  
Term 2: $\frac{d}{dx}((\frac{1}{2}x^2-9)^2) = 2(\frac{1}{2}x^2-9) \cdot \frac{d}{dx}(\frac{1}{2}x^2-9) = 2(\frac{1}{2}x^2-9)(x)$.  
So $f'(x) = 2x + x(\frac{1}{2}x^2 - 9)$.  
Set to 0: $2x + \frac{1}{2}x^3 - 9x = 0$.  
$x(2 + \frac{1}{2}x^2 - 9) = 0$. No.  
$2 + x^2/2 - 9 = 0$.  
$\frac{x^2}{2} = 7$.  
$x^2 = 14$.  
Let's re-calculate carefully.  

Method 1: Using $u=x^2$. This avoids ambiguity.  
$f(x) = x^2 + y^2$. $y = \frac{1}{2}x^2 - 9$.  
$F(u) = u + (\frac{1}{2}u - 9)^2$.  
$F'(u) = 1 + 2(\frac{1}{2}u - 9)(\frac{1}{2})$.  
$F'(u) = 1 + (\frac{1}{2}u - 9) = \frac{1}{2}u - 8$.  
Set $F'(u) = 0 \implies \frac{1}{2}u = 8 \implies u=16$.  
Value is $16 + (8-9)^2 = 17$.  

Let's re-evaluate Method 2 with direct x differentiation.  
$f(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
$f'(x) = 2x + 2(\frac{1}{2}x^2 - 9)(x)$.  
Is $2x + \dots$ or $2x$ is correct?  
Let's check derivative of $(\frac{1}{2}x^2-9)^2$.  
Outer function: $u^2$, inner: $\frac{1}{2}x^2-9$.  
Derivative: $2(\frac{1}{2}x^2-9) \cdot (x)$. Yes.  
So $f'(x) = 2x + x(x - 9)$? No, $(\frac{1}{2}x^2 - 9) = \frac{1}{2}x^2 - 9$.  
So term is $2(\frac{1}{2}x^2 - 9)x = x^3 - 18x$.  
So $f'(x) = 2x + x^3 - 18x = x^3 - 16x$.  
Set $f'(x) = 0$:  
$x(x^2 - 16) = 0$.  
Solutions: $x=0$, $x^2-16=0 \implies x=\pm 4$.  
We already checked these points.  
At $x=0$, distance squared is 81.  
At $x=\pm 4$, distance squared is 17.  
Minimum is 17.  

Let's double check the derivative calculation again to ensure no silly mistake.  
$y = \frac{1}{2}x^2 - 9$.  
$\frac{dy}{dx} = x$.  
DistSq $D^2 = x^2 + y^2$.  
$d/dx(D^2) = 2x + 2y \cdot dy/dx = 2x + 2y \cdot x = 2x(1+y)$.  
Ah, I see a discrepancy in my earlier derivations.  
Earlier I said $2(\frac{1}{2}x^2 - 9)(x)$. This is correct for the product rule part if we consider it separately. But here $y$ depends on $x$.  
Let's write out the terms clearly.  
$\frac{d}{dx}(x^2 + (\frac{1}{2}x^2 - 9)^2)$  
Term 1: $\frac{d}{dx}(x^2) = 2x$.  
Term 2: $\frac{d}{dx}(y^2) = 2y \cdot y' = 2y \cdot x$.  
So $f'(x) = 2x + 2x(\frac{1}{2}x^2 - 9)$.  
$= 2x + (x^3 - 18x)$? No.  
$2x(\frac{1}{2}x^2 - 9) = x(x^2 - 9) = x^3 - 9x$.  
So $f'(x) = 2x + x^3 - 9x = x^3 - 7x$.  
Let's re-evaluate this.  
$y' = x$.  
Term 1 is derivative of $x^2$ wrt $x$, which is $2x$.  
Term 2 is derivative of $(\frac{1}{2}x^2-9)^2$ wrt $x$. It's $2(\frac{1}{2}x^2-9) \cdot x$.  
This part was correct.  
Let's substitute $\frac{1}{2}x^2 - 9 = y$.  
$y' = x$. So $f'(x) = 2x + 2yx$. No, $y$ is a function of $x$, but the chain rule derivative is just $2y \cdot x$.  
Is $2x + 2(\frac{1}{2}x^2 - 9)x = 2x(1 + \frac{1}{2}x^2 - 9)$? No, because the second term is a product. It's $2x + 2xy$ where $y$ is the value of the function.  
Let's calculate $2x(1 + y)$ again.  
$2x(1 + \frac{1}{2}x^2 - 9) = 2x(\frac{1}{2}x^2 - 8) = x^3 - 16x$.  
Let's check if my previous calculation of $f'(x)$ yielded the same.  
Previous: $2x + x(x^2-9) = x^3 - 7x$?  
Term 1: $2x$.  
Term 2: $2(\frac{1}{2}x^2 - 9)(x) = (x^3 - 18x)$.  
Sum: $2x + x^3 - 18x = x^3 - 16x$.  
Ah, my manual expansion was $x^3 - 9x$? No.  
$2 \cdot (\frac{1}{2}x^2 - 9) \cdot x = (x^2 - 18)x = x^3 - 18x$.  
Let's check the previous sum: $2x + x(x^2 - 9)$. This was incorrect.  
$2x + 2(\frac{1}{2}x^2-9)x = 2x + (x^2-x)(2)$? No.  
It is $2x(1 + \frac{1}{2}x^2 - 9) = x(x^2+1-18)$.  
$2x( \frac{1}{2}x^2 - 8 ) = x^3 - 16x$.  
Okay, so the critical points equation is $x^3 - 16x = 0$.  
$x(x^2 - 16) = 0$.  
Roots: $x=0$, $x=\pm 4$.  
Values of distance squared at these points:  
At $x=0$: $y=-9 \implies D^2 = 0 + (-9)^2 = 81$.  
At $x=4$: $y = \frac{1}{2}(16)-9 = -1 \implies D^2 = 16 + 1 = 17$.  
Minimum is 17.  

Let's try to visualize. The parabola opens upwards, vertex at $(0, -9)$.  
The distance from the origin to the vertex is $\sqrt{0^2 + (-9)^2} = 9$. Distance squared is 81.  
As we move away from $x=0$, $y$ increases (parabola goes up). Since it opens up, for large $x$, $y \approx x^2/2 \to \infty$.  
Distance $D \approx \sqrt{x^2 + x^4/4} \approx x^2/2$ for large $x$. This is increasing.  
Since the vertex is a minimum on the vertical axis, and distance from origin is convex-ish, there should be minima near the "bottom" of the parabola.  
But we can move right or left to lower or raise the point?  
At $x=0$, height is -9. At $x=\pm 4$, height is -1. So moving out increases y, which generally reduces distance if origin was below and x small?  
Let's check a point nearby. $x=2$. $y = 2 - 9 = -7$ (No, $0.5(4)-9 = -7$). $D^2 = 4 + 49 = 53$.  
At $x=4$, $y=-1$. $D^2 = 16+1=17$. This is much smaller.  
So the minimum is indeed at $x=\pm 4$.  

The value of the squared distance is $a^2 = 17$.  
So $a = \sqrt{17}$. The question asks for $a^2$, which is 17.  

Let's double check if "smallest distance" implies just finding $\min D$ or something else.  
"The smallest distance ... can be expressed as $a$. Find $a^2$."  
So $a^2 = (\min D)^2 = \min (D^2)$.  
So I need to find the minimum of the squared distance function evaluated on the domain $x \in \mathbb{R}$.  
The value is 17.  

Let me think if there are any constraints I missed.  
"smallest distance between the origin and a point on the graph". Graph is whole parabola.  
Origin is $(0,0)$.  
Parabola $y = \frac{1}{2}x^2 - 9$ passes through points $(\pm 4, -1)$? Yes.  
And $(0, -9)$ which is on the axis of symmetry.  
Distance squared function $g(x) = x^2 + y^2$.  
Since $x^2 \ge 0$, we are minimizing distance from a point on a vertical line or just general curve.  
The distance between a point on a level curve of distance from origin... no that's not helpful.  
Distance function $D(\vec{r}) = |\vec{r}|$.  
Level sets of squared distance are circles centered at origin. We are looking for the first intersection (or closest approach) with the parabola.  
Intersection is solving $x^2 + (\frac{1}{2}x^2-9)^2 = \rho^2$.  
We found that for $\rho^2=17$, there exist points satisfying this ($\pm 4$). For $\rho^2 < 17$, we would need to see if solutions exist.  
Since the minimum of the function $g(u) = u + (\frac{1}{2}u - 9)^2$ is 17 at $u=16$, and it's a global minimum for the continuous function over $\mathbb{R}$, this is the absolute smallest distance squared.  
So $a^2 = 17$.  

Let me check if there is any trick with "graph of". Usually means whole domain where defined. Here domain is all reals.  
Is it possible that origin is on the graph? $0 = \frac{1}{2}(0)^2 - 9$ is false. $9 \neq 0$. So origin is not on the graph.  
So distance is non-zero, so we are looking for a positive minimum.  

Let's quickly re-verify the calculation.  
Function to minimize: $h(x) = x^2 + (x^2/2 - 9)^2$.  
$h'(x) = 2x + 2(x^2/2 - 9)(x)$.  
Set to 0.  
$x=0$ is a solution ($0 + (-18)(0) = 0$).  
Non-zero solutions: $(x^2/2 - 9)x = -x \cdot x$? No, term was $2(x^3-9x)$. No.  
$h'(x) = 2x + (x^3 - 18x)$.  
$x^3 - 16x = 0$.  
$x(x^2 - 16) = 0$.  
$x = \pm 4$.  
$h(4) = 16 + (16/2 - 9)^2 = 16 + (8-9)^2 = 16 + 1 = 17$.  
$h(-4) = 16 + 1 = 17$.  
$h(0) = 0 + (-9)^2 = 81$.  
Minimum is 17.  

Could there be a trick with $y^2$ sign? No, distance involves squares.  
Could there be a geometric intuition to verify?  
Parabola $y=x^2/2 - 9$.  
Vertex at $(0, -9)$.  
Distance from origin to vertex is 9. Distance squared is 81.  
The tangent to the parabola at vertex is vertical line $x=0$ (since vertex is minimum). No, wait.  
Derivative at vertex is 0. So tangent is horizontal? Yes.  
Slope at $(0,-9)$ is 0. Horizontal tangent.  
Origin is $(0,0)$. Point is $(0,-9)$. Distance vector is vertical.  
As we move along parabola away from vertex ($x \neq 0$), the distance increases.  
At $x=4$, point is $(4, -1)$.  
Distance to origin: $\sqrt{16^2+1^2} = \sqrt{256+1}$ no. $\sqrt{17} \approx 4.12$.  
Distance at vertex is 9.  
So the distance goes from 9 to something larger or smaller?  
At vertex, $D=9$. At $x=4$, $D=\sqrt{17} < 9$.  
So the curve dips closer to the origin than the vertex? No, vertex is lowest point of parabola ($y=-9$). Origin is at $y=0$.  
The graph passes through $(-\infty, \infty)$ but for $x \ge 0$, $y \ge -9$.  
Points with large $x$ have large distance.  
So the minimum must be somewhere between vertex and infinity? No, vertex is a point on curve closest in terms of vertical projection (y=lowest y).  
Since $y_{vertex} = -9 < y_{origin}$? No origin is $(0,0)$, so $y_{origin}=0$.  
Graph goes from high up to the minimum at $x=0$ where $y=-9$.  
So as we go left or right from vertex, $y$ increases.  
Distance squared is $x^2 + y^2$.  
At $x=0$, distance squared is 81.  
As $x$ grows large, $x^2 \to \infty$, so distance squared $\to \infty$.  
So minimum must be near $x=0$ where $y$ is minimal. But since parabola opens up, as $|x|$ increases, $y$ becomes larger positive? No, $y = x^2/2 - 9$. For small $x$, $y$ is negative.  
At $x=0$, $y=-9$. $D^2=81$.  
As we move to $x=\pm \epsilon$, $y \approx -9 + \epsilon^2/2$.  
Then $D^2 = \epsilon^2 + (-9+\epsilon^2/2)^2 \approx 81 - 9\epsilon^2 + \epsilon^4/4 \approx 81 - 9\epsilon^2$.  
This suggests distance decreases as we move away from $x=0$ along the axis of symmetry?  
Let's check values.  
$x=0, D^2=81$.  
$x=1, y = 0.5 - 9 = -8.5$. $D^2 = 1 + (-8.5)^2 = 1 + 72.25 = 73.25$.  
$73.25 < 81$. So distance decreased!  
So the minimum is not at $x=0$. The vertex of the parabola (lowest y) happens to be closest in terms of vertical coordinate, but we want Euclidean distance.  
My derivative calculation showed that decreasing occurs near $x=0$ until some point, then it increases.  
Why did my quadratic check work?  
$h(u) = \frac{1}{4}u^2 - 8u + 81$. This is a parabola opening upwards.  
Minimum at $u=16$. Since $u=x^2$, this corresponds to $x=\pm 4$.  
Let's re-verify the derivative of $h(u)$ at $u=0$ (which is $x=0$).  
$h'(u) = \frac{1}{2}u - 8$.  
At $u=0$, $h'(0) = -8 < 0$. So as $u$ increases from 0, distance squared decreases.  
So minimum is NOT at $x=0$. It's when derivative is zero.  
Where does it hit 0? At $u=16$.  
For $u \in [0, 16]$, $h'(u) < 0$. So function is decreasing.  
So distance decreases as we move from vertex to $x^2=16$.  
At $u=16$, derivative is 0.  
Then for $u > 16$, derivative is positive, so function increases.  
So the minimum is indeed at $u=16$.  
And the value is 17.  

The confusion earlier was about vertex of parabola vs distance to origin.  
Vertex of curve is $(0,-9)$. This corresponds to $x=0$. Distance squared is 81.  
Points with smaller $x^2$ (closer to axis) have lower distance? No.  
At $x=1$, distance is $\sqrt{73.25} \approx 8.56 < 9$.  
So the points $(\pm 4, -1)$ are actually closer to origin than the vertex is.  
The vertex is at $y=-9$. Origin is at $y=0$.  
Any point with negative y (below origin) gets closer as x increases?  
Let's visualize.  
Parabola opens up. Vertex is at bottom.  
We want to find a point on this curve closest to the origin $(0,0)$.  
Since the parabola passes below the origin for $x$ close to 0, the distance is determined by how far "down" (negative y) we are from the origin and how far "out" (positive x) we are.  
The point $(0, -9)$ is at distance 9.  
Moving to $(\pm 4, -1)$. The point rises by 8 units. The point moves sideways by 4 units.  
Since the rise is $8^2=64$? No.  
Let's look at the vector components.  
At vertex: $\vec{v} = (0, -9)$. Length 9.  
At $(\pm 4, -1)$: $\vec{p} = (\pm 4, -1)$. Length $\sqrt{17}$.  
Note that $x^2+y^2$ is being minimized.  
The derivative of distance squared w.r.t x was negative for $|x|<4$.  
So the curve gets closer as it approaches $x=4$.  
At $x=0$, slope is 0 (horizontal tangent), meaning we are moving purely along a curve with positive curvature.  
We approach $(\pm 4, -1)$ and then go further away?  
Let's check $x=8$. $y = 32/2 - 9 = 16 - 9 = 7$.  
$D^2 = 8^2 + 7^2 = 64 + 49 = 113 > 17$.  
So yes, the minimum is between $x=0$ and large x.  
Specifically at $x=\pm 4$.  

Is there any other interpretation of "graph"? No.  
Is it possible to interpret $a^2$ differently? No.  
The result seems solid.  

Let's do a sanity check on the derivative logic again.  
We want $\min (x^2 + (\frac{1}{2}x^2 - 9)^2)$.  
Let $y = \frac{1}{2}x^2 - 9$.  
Then $x^2 + y^2$ is minimized.  
This is equivalent to finding the minimum of $\sqrt{x^2+y^2}$ or squared distance.  
Let's use Lagrange Multipliers? No, simple constraint optimization is enough.  
Function $f(x,y) = x^2 + y^2$. Constraint $y - \frac{1}{2}x^2 + 9 = 0$.  
Gradients: $\nabla f = (2x, 2y)$. Normal to constraint surface $\nabg = (-x, 1)$? No, normal vector is gradient of constraint function.  
Let $g(x,y) = \frac{1}{2}x^2 - y + 9 = 0$. Then $\nabla g = (x, -1)$.  
Lagrange: $2x = \lambda x$ and $2y = \lambda (-1) = -\lambda$.  
From first eq: $x(2 - \lambda) = 0$.  
Case A: $x=0$. Then $y = 9$. Distance squared is $0^2 + 9^2 = 81$.  
Case B: $\lambda = 2x$.  
Substitute into second eq: $2y = -\lambda = -2x \implies y = -x$.  
Now substitute $y=-x$ into constraint equation: $\frac{1}{2}x^2 - (-x) + 9 = 0$. No.  
Constraint is $y = \frac{1}{2}x^2 - 9$.  
So $-x = \frac{1}{2}x^2 - 9$.  
$\frac{1}{2}x^2 + x - 9 = 0$.  
$x^2 + 2x - 18 = 0$.  
Roots: $x = \frac{-2 \pm \sqrt{4 - 4(1)(-18)}}{2} = \frac{-2 \pm \sqrt{4 + 72}}{2} = \frac{-2 \pm \sqrt{76}}{2} = -1 \pm \sqrt{19}$.  
So critical points are at these x coordinates.  
Distance squared would be $x^2 + (-x)^2 = 2x^2$ or something? No.  
If $y = -x$, then point is $(x, -x)$.  
But this assumes the constraint was $y=x^2/2-9$ AND we are on the line $y=-x$.  
So intersection of $y = x^2/2-9$ and $y=-x$.  
$x^2/2 - 9 = -x \implies x^2 + 2x - 18 = 0$.  
Then distance squared is $x^2 + (-x)^2 = 2x^2$.  
From equation $x^2 = 18 - 2x$. So $x^2 \approx 9$ if $x=-1$.  
$x^2 = -1 + \sqrt{19}$. Or similar.  
So distance squared is not minimized at infinity in this branch.  
But let's re-evaluate the Lagrange multiplier derivation.  
Minimizing $x^2+y^2$ subject to $\frac{1}{2}x^2 - y + 9 = 0$.  
$\nabla f = (2x, 2y)$. $\nabla g = (x, -1)$ where $g(x,y) = \frac{1}{2}x^2 - y + 9$.  


## Answer

*(none: the token cap hit during thinking)*
