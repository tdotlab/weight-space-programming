# test/algebra/1143.json (Algebra, level 5)

> The smallest distance between the origin and a point on the graph of $y=\frac{1}{2}x^2-9$ can be expressed as $a$.  Find $a^2$.  

**Correct.** Gold `17`, predicted `17`. Finish: stop, 7837 tokens, 1 waits, 656.5 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here is a thinking process to solve the problem:  

1.  **Understand the Goal:** The objective is to find the smallest distance between the origin $(0,0)$ and any point on the parabola given by the equation $y = \frac{1}{2}x^2 - 9$. Once found, I need to square this distance ($a$) and output $a^2$.  

2.  **Analyze the Curve:**  
    *   The equation is a parabola opening upwards because the coefficient of $x^2$ is positive ($\frac{1}{2} > 0$).  
    *   Vertex: Set the derivative to zero or use vertex form.  
        *   Derivative $y' = x$.  
        *   Critical point at $x = 0$.  
        *   Vertex point: $(0, -9)$.  

3.  **Analyze the Distance:**  
    *   Let $P(x, y)$ be a point on the graph of the parabola.  
    *   The coordinates of $P$ are $(x, \frac{1}{2}x^2 - 9)$.  
    *   The origin is $O(0, 0)$.  
    *   We want to minimize the distance $d(P, O) = \sqrt{(x - 0)^2 + (y - 0)^2}$.  
    *   Minimizing distance between two points is equivalent to minimizing the squared distance, as the square root function is monotonically increasing for positive arguments. Let $D^2$ be the squared distance.  
    *   $D^2 = x^2 + y^2$.  

4.  **Set up the Function to Minimize:**  
    *   Substitute $y$ into the expression for $D^2$:  
$f(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  

5.  **Find the Minimum:**  
    *   Expand the term $(\frac{1}{2}x^2 - 9)^2$:  
$(\frac{1}{2}x^2 - 9)^2 = (\frac{1}{4}x^4) - 2(\frac{1}{2}x^2)(9) + (-9)^2$  
$= \frac{1}{4}x^4 - 9x^2 + 81$.  
    *   Now substitute this back into $f(x)$:  
$f(x) = x^2 + \frac{1}{4}x^4 - 9x^2 + 81$  
$f(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  
    *   This is a quartic function in terms of $x$. To find the minimum, I can take the derivative with respect to $x$ and set it to zero. Alternatively, look at the graph. Since it's even (symmetric about y-axis), we can check $f(x)$ for $x \ge 0$.  
    *   $f'(x) = \frac{d}{dx}(\frac{1}{4}x^4 - 8x^2 + 81)$  
$= x^3 - 16x$.  
    *   Set $f'(x) = 0$:  
$x(x^2 - 16) = 0$.  
    *   Possible solutions for critical points:  
$x = 0$  
$x^2 - 16 = 0 \implies x = 4, x = -4$.  

    *   Evaluate $f(x)$ at these critical points:  
        *   At $x = 0$: $f(0) = \frac{1}{4}(0)^4 - 8(0)^2 + 81 = 81$.  
Distance squared = 81.  
        *   At $x = 4$: $f(4) = \frac{1}{4}(4^4) - 8(4^2) + 81$  
$= \frac{1}{4}(256) - 8(16) + 81$  
$= 64 - 128 + 81$  
$= 3.2$? No, let's re-calculate carefully.  
$64 - 128 = -64$.  
$-64 + 81 = 17$.  
        *   At $x = -4$: Same as $x=4$ due to symmetry in squared distance (though original function is a parabola, the distance calculation depends on $y^2$, which is even).  

    *   Compare values:  
        *   $f(0) = 81$. Distance $d_0 = \sqrt{81} = 9$.  
        *   $f(4) = 17$. Distance $d_4 = \sqrt{17}$. Since $\sqrt{17} < \sqrt{81}$ (which is 9), the minimum distance squared corresponds to $f(4)$?  
Let me double check the calculation.  

    *   **Recalculation Check:**  
Equation: $y = \frac{1}{2}x^2 - 9$.  
Point on graph: $(x, y)$. Origin: $(0,0)$.  
Distance squared $D^2 = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
Let $u = \frac{1}{2}x^2$. Then $x^2 = 2u$ and $x = \pm\sqrt{2u}$? No, this is getting complicated. Stick to $x$.  

$y = \frac{x^2}{2} - 9$.  
Vertex of parabola is $(0, -9)$.  
The distance from origin to a point on the parabola $y = x^2/4$ (shifted down by 9).  
Let's visualize.  
Parabola passes through vertex $(0, -9)$. Distance squared to origin from this point is $0^2 + (-9-0)^2 = 81$.  
As $x$ increases, the point moves right and up (since parabola opens up).  
The vertex is a local minimum of the distance in terms of geometry? No, the origin is "above" the vertex. The distance function $y(x)$ vs $y_{origin}$ is not what matters.  
Let's look at $f(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  
This is a quadratic in $z=x^2$. Let $g(z) = \frac{1}{4}z^2 - 8z + 81$.  
We want to find min $g(z)$ where $z \ge 0$ (since $x^2 \ge 0$).  
Vertex of parabola $g(z)$ occurs at $z = -\frac{-8}{2(1/4)} = \frac{8}{0.5} = 16$.  
Since $z=x^2$, the maximum value is not relevant here, we want the minimum.  
The vertex of $g(z)$ is a parabola opening upwards. So the minimum is at the "vertex" of this outer parabola $g(z)$.  
Is $z=16$ within the domain? Yes, since $x^2$ can be any non-negative real number.  
Calculate $g(16)$:  
$g(16) = \frac{1}{4}(16)^2 - 8(16) + 81$  
$g(16) = \frac{1}{4}(256) - 128 + 81$  
$g(16) = 64 - 128 + 81$  
$g(16) = 3.2$? No.  
Let's calculate $g(16)$ again.  
$64 - 128 + 81$.  
$64 + 81 = 145$.  
$145 - 128 = 17$.  
So min distance squared is 17.  

*   **Geometric Check:**  
Let the point on the graph be $(x, \frac{1}{2}x^2 - 9)$.  
Let the projection of this point on the x-axis be $(x,0)$? No, that's not useful directly.  
The origin is $(0,0)$.  
The tangent to the parabola at $x$ has slope $m = x$.  
Distance from origin to point $(x,y)$ is $\sqrt{x^2 + y^2}$.  
Is there a geometric trick? Maybe related to the reflection principle?  
Or Cauchy-Schwarz?  

We want to minimize $x^2 + (\frac{1}{2}x^2 - 9)^2$.  
Let's use AM-GM inequality.  
$A = x^2$, $B = \frac{1}{4}x^4 - 9x^2 + 81$. This doesn't look like a direct sum of squares product easily.  

Back to derivative method:  
$f(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
$f'(x) = 2x + 2(\frac{1}{2}x^2 - 9)(x) = 2x(1 + \frac{1}{2}x^2 - 9)$? No.  
$\frac{d}{dx}(\frac{1}{4}x^4) = x^3$.  
$\frac{d}{dx}(-8x^2) = -16x$.  
$f'(x) = x^3 - 16x = x(x^2 - 16)$.  
Roots are $0, 4, -4$.  
Let's re-evaluate the distance squared at $x=4$:  
$D^2(4) = (4)^2 + (\frac{1}{2}(4)^2 - 9)^2$  
$= 16 + (\frac{1}{2}(16) - 9)^2$  
$= 16 + (8 - 9)^2$  
$= 16 + (-1)^2 = 17$.  

Is it possible that the minimum is at another point?  
The derivative changes sign from negative to positive at $x=4$.  
For $x < -4$, say $-5$: $f'(-5) = -5(25-16) = -45$ (negative).  
For $-4 < x < 0$, say $-1$: $f'(-1) = -1(1-16) = 15$ (positive).  
So at $x=4$, it's a local minimum. Since the function goes to infinity as $x \to \pm \infty$, this is the global minimum.  

At $x=0$, $f'(0)=0$.  
$f(0) = 81$.  
For $x$ slightly negative, say $-0.1$: $f'(-0.1) > 0$. It increases from 0 to positive.  
Since $f(x)$ starts at 81 at $x=0$, goes down to 17 at $x=4$, then goes back up.  
So the minimum is indeed 17.  

*   **Verification of Calculation:**  
$y = x^2/2 - 9$.  
Point $(x, y)$. Origin $(0,0)$.  
Distance squared $D^2 = x^2 + y^2$.  
To minimize $D^2$, we can use geometric intuition. The normal to the curve passing through the origin is perpendicular to tangent.  
Slope of normal $m_n = -1/m_t = -1/x$ (assuming $x \neq 0$).  
This seems like overthinking. Calculus is robust here.  

Let's check the logic again.  
$y = 1/2 x^2 - 9$.  
We want to find a point $(x, y)$ on this curve such that distance to origin $\sqrt{x^2+y^2}$ is minimized. This means we are looking for the point where the tangent makes a right angle with some specific vector? No.  
Geometrically, the level sets of $D^2$ (spheres centered at origin) just touch the curve at some point. The distance from origin to the parabola vertex is 9. This is a candidate.  
However, the parabola goes "outwards" to infinity. For example at large $x$, distance is approx $\sqrt{x^2 + x^4/4} \approx |x^2|/\sqrt{4} = x^2/2$. As $|x|$ increases, this distance grows quadratically (actually cubically if looking at distance along tangent? No, simply $x^2 + (x^2/2)^2 \approx x^4/4$, so $\to \infty$).  
So we must look for a minimum between $x=0$ and infinity.  
The vertex is $(0, -9)$. Distance squared = 81.  
As we move away from the axis of symmetry (x-axis), the curve moves *up* to positive $y$. But at large positive x, it's high up, far from origin? No, origin is at $y=0$.  
Parabola vertex $(0, -9)$ is distance 9.  
At $x=4$: $y = 1/2(16) - 9 = 8 - 9 = -1$.  
Point $(4, -1)$. Origin $(0,0)$. Distance squared = $4^2 + (-1)^2 = 16 + 1 = 17$.  
At $x=-4$: $y = -1$. Point $(-4, -1)$. Distance squared = 17.  
Is there any point with smaller distance?  
Consider the curve passes through $(0, -9)$.  
Does the curve cross the x-axis? $1/2x^2 - 9 = 0 \implies x^2 = 18 \implies x = \pm \sqrt{18} = \pm 3\sqrt{2} \approx \pm 4.24$.  
If it crosses at $\sqrt{18}$, the point is $(3\sqrt{2}, 0)$. Distance squared $= (3\sqrt{2})^2 + 0 = 9(2) = 18$.  
18 is greater than 17. So the crossing doesn't help minimize distance.  

What about $y=-5$? $1/2x^2 - 9 = -5 \implies x^2/2 = 4 \implies x^2=8$. Point $(\pm \sqrt{8}, -5)$. Distance squared $= 8 + (-5)^2 = 33$.  

Let's check the function value again.  
$D^2(x) = x^2 + (x^2/2 - 9)^2$.  
We found critical point at $x^2 = 16 \implies |x|=4$.  
Then $D^2 = 17$.  
What about $x=0$? $D^2 = 81$.  
Is there any other constraint? No.  

So the minimum squared distance is 17.  
The problem asks for $a$, where $a$ is the smallest distance.  
So $a = \sqrt{17}$.  
We need to find $a^2$.  
$a^2 = 17$.  

6.  **Refining the Steps for Final Output:**  
    *   Identify coordinates of a point on the graph: $(x, y) = (x, \frac{1}{2}x^2 - 9)$.  
    *   State the condition to minimize distance from origin $(0,0)$: Minimize $D^2 = x^2 + y^2$.  
    *   Substitute $y$: $f(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
    *   Expand $f(x)$:  
$f(x) = x^2 + \frac{1}{4}x^4 - 9x^2 + 81$  
$f(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  
    *   Find the derivative with respect to $x$: $f'(x) = x^3 - 16x$.  
    *   Set derivative to zero: $x^3 - 16x = 0 \implies x(x^2 - 16) = 0$.  
    *   Solutions: $x = 0$, $x = 4$, $x = -4$.  
    *   Evaluate $f(x)$ at these points to find the minimum.  
$f(0) = 81$.  
$f(4) = \frac{1}{4}(256) - 8(16) + 81 = 64 - 128 + 81 = 17$.  
    *   Evaluate $f(-4)$: same as $f(4) = 17$.  
    *   Conclude the minimum squared distance is 17.  
    *   Identify $a$ (distance) and $a^2$.  
$a^2 = 17$.  

7.  **Is there an algebraic/AM-GM way to do this without calculus?**  
Let's check.  
We want to minimize $D^2 = x^2 + (x^2/2 - 9)^2$.  
Let $u = x^2/2$. Then $x^2 = 2u$ where $u \ge 0$.  
Substitute: $D^2 = 2u + (u - 9)^2 = 2u + u^2 - 18u + 81 = u^2 - 16u + 81$.  
We want to minimize $g(u) = u^2 - 16u + 81$ for $u \ge 0$.  
This is a parabola opening upwards. The vertex is at $u = -(-16)/(2*1) = 8$.  
Since $u=8 \ge 0$, this is the minimum.  
Calculate min value:  
$g(8) = (8)^2 - 16(8) + 81$  
$= 64 - 128 + 81$  
$= -64 + 81 = 17$.  
This confirms the previous result.  

Does this make sense geometrically?  
Let's check if there is any subtlety I missed.  
"Smallest distance between the origin and a point on the graph".  
The function $f(x)$ represents distance squared. The global minimum of $f(x)$ gives the answer.  
The substitution $u = x^2/2$ captures all non-negative values for $x^2$. If $x^2=16$, $u=8$, which is valid.  
Calculations are consistent.  

Let's double check arithmetic one more time.  
$y = 1/2 x^2 - 9$.  
Vertex $(0, -9)$. Distance squared to origin: $(-9)^2 + 0^2 = 81$.  
At $x = \sqrt{16} = 4$:  
$y = 1/2 (16) - 9 = 8 - 9 = -1$.  
Point $(4, -1)$.  
Distance squared: $4^2 + (-1)^2 = 16 + 1 = 17$.  
Is 17 smaller than 81? Yes.  
Why is the distance from vertex to origin greater than the distance at $x=4$?  
The point $(0, -9)$ is "far" in the y-direction. As we move right to x=4, we go down a bit in y? No, from -9 to -1, we go UP by 8 units in y. We move 4 units in x.  
The hypotenuse calculation: $\sqrt{4^2 + 1^2}$. This is the distance.  
Why isn't $x=0$ a minimum? At $x=0$, we are at $(0, -9)$. Distance is 9.  
At $x=4$, we are at $(4, -1)$. Distance is $\sqrt{17} \approx 4.123$.  
Since $4.123 < 9$, moving away from the x-axis (in terms of x) helps reduce distance significantly because the parabola dips towards the origin but then turns back up?  
Let's check the graph visually.  
Vertex at $(0, -9)$.  
At $x=0$, point is $(0, -9)$. Distance 9.  
As $x$ goes from 0 to 4, $y$ goes from -9 to -1. Point moves up towards x-axis (from below).  
Then as $x$ goes further, say to 8:  
$y = 32/2 - 9 = 16$.  
Point $(8, 16)$. Distance $\sqrt{64 + 256} = \sqrt{320} \approx 17.8$.  
So the curve goes down from y=-infinity? No, parabola opens up. It goes down to -9 then up.  
The "hole" in distance seems to be caused by the intersection with a lower $y$ that is not at vertex.  
The origin $(0,0)$ is above the vertex $(0,-9)$.  
The tangent at vertex is horizontal (perpendicular to normal passing through origin).  
But we want the line from origin to point on curve to be perpendicular? No, minimum distance implies tangent at that point passes through origin? Or rather the segment is perpendicular to the curve's normal? Yes, standard calculus property.  

Let's do a quick derivative logic check for geometric intuition.  
Distance $r^2 = x^2 + y^2$.  
Constraint: $y = 0.5x^2 - 9$.  
If we treat this as intersection of sphere and parabola, tangent is perpendicular to the plane? No, that's wrong. It means $\nabla D^2$ is parallel to tangent vector? No.  
Tangency condition: $\nabla (x^2+y^2) = (2x, 2y)$. This must be parallel to tangent vector $(1, y')$.  
So $2y / (2y') = x/1 \implies y/y' = x \implies y/y' - x = 0$.  
Substitute $y'$:  
$y' = x$.  
$y/x - x = 0$? No, that assumes derivative is with respect to parameter.  
Let's restate properly. Minimize distance from origin to curve.  
Tangent vector at $(x,y)$ is $\vec{v} = (1, x)$.  
The normal vector $\vec{n}$ must point from the tangent to origin? Or rather, the segment connecting origin and $(x,y)$ must be perpendicular to the tangent line of the curve.  
Slope of tangent $m_{tan} = dy/dx = x$.  
Slope of line from origin is $m_{line} = y/x$.  
Perpendicular condition: product of slopes $= -1$.  
$(y/x) * (x) = -1 \implies y = -1$.  
This happens for $x$ and $y$ coordinates.  
If $y = -1$, then on the curve $-1 = x^2/2 - 9 \implies x^2/2 = 8 \implies x^2 = 16 \implies |x|=4$.  
This matches the critical point found earlier ($f'(x)=0$).  
The condition is $\nabla D^2 \cdot \vec{v} = 0$. Or simply, $y' = -x/y * (something)$? No.  
Slope of secant line from $(0,0)$ to $(x,y)$ is $m_1 = y/x$.  
Slope of tangent is $m_2 = x$.  
If these are perpendicular at minimum distance: $m_1 m_2 = -1$.  
$(y/x) \cdot x = -1$? This implies $y = -1$.  
If $y=-1$, then $x^2/2 = 8 \implies x=4$ (since $x=0$ gives tangent undefined or vertical/horizontal?). At $x=0$, $y' = 0$. Tangent is horizontal. Line from origin to $(0,-9)$ is vertical. Vertical vs Horizontal are perpendicular!  
So at the vertex $(0, -9)$, the distance condition "minimizing" isn't about perpendicularity, it's about $y/x$ being undefined or limit?  
Actually, let's check if $(0,-9)$ satisfies perpendicularity.  
$y=-9 \implies y/x = -9/0 = \text{undefined}$. Tangent slope is 0 (horizontal). Perpendicular slope should be $\infty$ (vertical). The line from origin to vertex is vertical. So yes, the tangent at $(0,-9)$ is perpendicular to the radius vector.  
However, the perpendicular condition derived $y=-1$ is a local minimum condition?  
Let's check the algebra for that.  
Minimize $\sqrt{x^2+y^2}$ subject to $f(x,y)=0$.  
Lagrange Multipliers:  
$F = x^2 + y^2 - \lambda (y - 1/2x^2 + 9)$.  
$2x - \lambda(-xy')? No, derivative w.r.t x is not involved directly if implicit differentiation used.  
$\frac{\partial F}{\partial x} = 2x - \lambda(-xy?)$ no.  
Let's stick to the substitution method which was verified.  
The algebraic derivation led to $u^2 - 16u + 81$. This quadratic minimum is definitely a local min of the function defined for real $u$. Since it is convex (parabola opening up) and domain is $u \ge 0$, and vertex $u=8 > 0$, it is the global min.  
So, the distance squared is indeed 17.  

Let's double check the question wording. "Smallest distance ... can be expressed as a".  
This implies $a = \sqrt{17}$.  
Find $a^2$. So $a^2 = 17$.  

Is there any tricky interpretation of "on the graph"? Usually means points $(x, y)$ satisfying equation. Yes.  

Let's quickly review if $y=0$ is a solution.  
If $y=0$, then $x^2/2 - 9 = 0 \implies x^2 = 18$.  
Distance squared: $x^2 + y^2 = 18 + 0 = 18$.  
This is not the minimum (since $17 < 18$).  

Let's check if $a$ could be something else.  
"expressed as $a$".  
Usually this means $a$ is a value or expression. But here "can be expressed as $a$" and "Find $a^2$" implies finding the value of the square.  
So $a$ is the distance, which is $\sqrt{17}$.  
The answer to $a^2$ is 17.  

Let's check if there are any other interpretations.  
Could the graph be in a different orientation? No, "graph of $y = ...$" is standard Cartesian plane.  

Final verification of steps:  
1.  Minimize distance squared $D^2 = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
    2.  Let $u = \frac{1}{2}x^2$. Since $x$ is real, $u \ge 0$. Also $u = y_{shifted\_y}$? No $u$ represents the term inside squared distance's bracket?  
$D^2 = x^2 + (ux - 9)^2$.  
Let's check my substitution again.  
Original: $f(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
Let $X = x^2/2$. Then $x^2 = 2X$.  
$f(X) = 2X + (X - 9)^2 = 2X + X^2 - 18X + 81 = X^2 - 16X + 81$.  
This requires $x \in \mathbb{R} \implies x^2 \ge 0 \implies 2X \ge 0 \implies X \ge 0$.  
The function is a parabola in $X$ opening upwards.  
Minimum is at vertex $X = -(-16)/2(1) = 8$.  
Check if $X=8$ is valid: $8 \ge 0$. Yes.  
Value at min: $8^2 - 16(8) + 81 = 64 - 128 + 81 = 17$.  
    3.  The minimum squared distance is 17.  
    4.  Distance $a = \sqrt{17}$.  
    5.  Find $a^2 = 17$.  

Seems solid. No obvious pitfalls found.  

Double check arithmetic:  
$64 - 128 + 81$.  
$64 + 81 = 145$.  
$145 - 128 = 17$.  
Correct.  

Final Answer formulation.  
The value is 17.  

Could there be a trick with "distance between origin and point on graph"?  
Maybe distance in polar coordinates? No, usually Cartesian unless specified.  
Maybe $x$ is complex? No, standard problem implies real domain.  

The question asks to find $a^2$.  
It's just the value 17.  


## Answer

To find the smallest distance between the origin $(0,0)$ and a point on the graph of the parabola $y=\frac{1}{2}x^2-9$, let the coordinates of a general point $P(x,y)$ on the graph be $(x, \frac{1}{2}x^2-9)$.  

The squared distance $d^2$ from the origin to this point is given by:  
$$ d^2 = x^2 + y^2 $$  
Substituting the equation of the parabola for $y$:  
$$ d^2 = x^2 + \left(\frac{1}{2}x^2 - 9\right)^2 $$  

To find the minimum distance, we need to minimize this function with respect to $x$. Let's simplify the expression first. We can use a variable substitution or expand the term directly.  
Using substitution, let $u = \frac{1}{2}x^2$. Since $x$ is real, $u$ must be non-negative ($u \ge 0$). Note that $x^2 = 2u$, so if we find the minimum of the function in terms of $u$, it will be valid for any valid $u$.  
Rewrite the expression for squared distance in terms of $u$:  
$$ d^2(u) = 2u + (u - 9)^2 $$  
Expand $(u-9)^2$:  
$$ d^2(u) = 2u + u^2 - 18u + 81 $$  
$$ d^2(u) = u^2 - 16u + 81 $$  

Now, we want to find the minimum value of this quadratic function $g(u) = u^2 - 16u + 81$ for $u \ge 0$.  
This is a parabola opening upwards. Its vertex occurs at:  
$$ u = -\frac{b}{2a} $$  
Here, $a=1$ and $b=-16$.  
$$ u_{vertex} = \frac{-(-16)}{2(1)} = \frac{16}{2} = 8 $$  

Since the vertex value corresponds to a valid domain ($u=8 \ge 0$), we can use this point to find the minimum.  
Substitute $u=8$ back into the expression for $d^2(u)$:  
$$ d^2(8) = (8)^2 - 16(8) + 81 $$  
$$ d^2(8) = 64 - 128 + 81 $$  
$$ d^2(8) = -64 + 81 $$  
$$ d^2(8) = 17 $$  

We should also check endpoints or other critical points.  
The function is defined for $x \in \mathbb{R}$. If $x=0$, then $u=0$, which is not the minimum (value is $g(0)=81$).  
If $x^2=16$ (so $u=8$), this corresponds to points $(\pm 4, -1)$. The distance is $\sqrt{17} \approx 4.12$.  
Let's check the vertex of the original function directly just to be sure:  
$f(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  
$f'(x) = x^3 - 16x$. Roots are $0, 4, -4$.  
$f(0) = 81$.  
$f(4) = \frac{1}{4}(256) - 8(16) + 81 = 64 - 128 + 81 = 17$.  
The minimum value is indeed 17.  

So, the smallest distance $a$ satisfies:  
$$ a^2 = 17 $$  

\boxed{17}  
