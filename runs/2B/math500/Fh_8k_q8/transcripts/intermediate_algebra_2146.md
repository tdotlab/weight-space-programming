# test/intermediate_algebra/2146.json (Intermediate Algebra, level 4)

> Let $P(x)$ be a quadratic polynomial with real coefficients satisfying $x^2 - 2x + 2 \le P(x) \le 2x^2 - 4x + 3$ for all real  numbers $x$, and suppose $P(11) = 181$. Find $P(16)$.  

**Wrong.** Gold `406`, predicted `None`. Finish: length, 8192 tokens, 62 waits, 687.9 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Let the quadratic polynomial be $P(x) = ax^2 + bx + c$.  
We are given that for all real numbers $x$,  
$$ x^2 - 2x + 2 \le P(x) \le 2x^2 - 4x + 3 $$  
We need to find $P(16)$, given that $P(11) = 181$.  

Let's look at the bounds.  
The lower bound is $L(x) = x^2 - 2x + 2$.  
This can be rewritten as $(x-1)^2 + 1$.  
The upper bound is $U(x) = 2x^2 - 4x + 3$.  
This can be rewritten as $2(x^2 - 2x) + 3 = 2(x-1)^2 - 2(1)^2 + 3 = 2(x-1)^2 + 1$? No.  
Let's check the discriminant of the quadratic terms.  
$L(x)$ is a parabola opening upwards with minimum at $x=1$, value $L(1) = 1$.  
$U(x)$ is a parabola opening upwards with minimum at $x=2$ (wait, vertex at $x=4/2 \times (-1/-?) no$. Roots are $x^2-2x+(3/2)? No.  
Let's re-evaluate $U(x) = 2x^2 - 4x + 3$.  
The vertex is at $x = -(-4)/(2 \cdot 2) = 1$.  
$U(1) = 2(1)^2 - 4(1) + 3 = 2 - 4 + 3 = 1$.  
So, both bounds are minimum at $x=1$, and the value is 1.  
Let's check the lower bound again. $L(x) = x^2 - 2x + 2$.  
$L(1) = 1 - 2 + 2 = 1$.  
So $L(x)$ and $U(x)$ touch at $x=1$ with value 1.  
Also, $L(x) \ge 1$ for all $x$, as $(x-1)^2 \ge 0$.  
And $U(x) \ge 1$ for all $x$, since it is a parabola opening up and vertex at $(1,1)$.  

Let's factorize the difference.  
$D = U(x) - L(x) = (2x^2 - 4x + 3) - (x^2 - 2x + 2) = x^2 - 2x + 1 = (x-1)^2$.  
So we are given $L(x) \le P(x) \le U(x)$ for all $x$.  
Actually, the condition implies that $P(x)$ lies between these two functions.  
At $x=1$, $L(1)=1$ and $U(1)=1$. The interval is just $\{1\}$.  
So $P(1) = 1$.  

Wait, if $P(x)$ must be bounded by functions touching at one point (for $x=1$), does it imply anything about the range of coefficients?  
Let's check the difference $U(x) - L(x) = (x-1)^2$. This is always non-negative.  
So $U(x) \ge L(x)$ is satisfied for all $x$.  
We need to satisfy $P(11) = 181$.  

Let $Q(x) = U(x) - L(x) = (x-1)^2$.  
So we are looking for a polynomial $P(x)$ such that $L(x) \le P(x) \le U(x)$ and $P(11)=181$.  
Also $L(x) \le P(x) - U(x)$? No, $U(x) - L(x) = (x-1)^2$.  
So we have $1 \le P(x) - 1 \implies P(x) \ge 0$? Not quite.  
Let's consider $P(x) = U(x) - (x^2 + k x + m)$? No, simpler to think about the structure.  
$L(x) = x^2 - 2x + 2$. $U(x) = 2x^2 - 4x + 3$.  

Let's express $P(x)$ as a linear combination of these polynomials plus some other terms?  
Or better, let's look at the values of $x$ and $y$.  
We have $(x-1)^2 \le P(x) - L(x) = P(x) - (x^2 - 2x + 2)$? No.  
Let's rewrite the condition:  
$L(x) \le P(x) \le U(x)$  
This is equivalent to $P(x) \in [L(x), U(x)]$.  
So $0 \le P(x) - L(x) \le U(x) - L(x) = (x-1)^2$.  

Let's check specific points.  
$P(1) = 1$. This is consistent with $L(1)=1, U(1)=1$.  
We need to calculate $P(16)$ given $P(11) = 181$.  

The function $Q(x) = U(x) - L(x) = (x-1)^2$ describes the "gap" allowed between $L(x)$ and $U(x)$.  
Wait, the condition is just that $P(x)$ lies in the interval defined by these parabolas.  
Is there a specific relationship?  
Let's re-read carefully: "$x^2 - 2x + 2 \le P(x) \le 2x^2 - 4x + 3$".  
This means for all $x$, $P(x)$ is between them.  

Let's assume $P(x)$ has a form related to these bounds.  
Maybe we can define $Q(x)$ such that $P(x) = A(x-1)^2 + B(1-x^2) ...$? No.  
Notice the symmetry or relation between coefficients.  
$L(x) = x^2 - 2x + 2$. $U(x) = 2x^2 - 4x + 3$.  
Is it possible that $P(x)$ is a linear function of $(x-1)$? No, degree is at most 2.  
Since $U(x) - L(x) = (x-1)^2$, we can think of the "error" from the lower bound.  
Let $f(x) = P(x)$. The condition is $\int_0^x ...$? No.  

Let's consider the transformation $y = x+1$. No.  
Maybe let's try to express $P(x)$ using a basis of functions that behave nicely with the bounds.  
Notice that both bounds have roots or specific values related to $x=1, 2, \dots$  
$L(x) = (x-1)^2 + 1$. Roots are imaginary: $\pm i\sqrt{3}$? No $(x-1)^2 = -1$.  
$U(x) = 2(x-1)^2 + 1$. Roots are imaginary.  
Wait, $L(1)=1$, $U(1)=1$.  
At $x=0$: $L(0) = 2$, $U(0) = 3$.  
At $x=3$: $L(3) = 9 - 6 + 2 = 5$, $U(3) = 2(9) - 12 + 3 = 18 - 12 + 3 = 9$.  
At $x=-1$: $L(-1) = 1+2+2=5$, $U(-1)=2-4+3=1$. Wait.  
$U(-1) = 2(1) - 4(-1) + 3 = 2 + 4 + 3 = 9$. No, $2x^2 - 4x + 3$ at $x=-1$ is $2+4+3=9$.  
Let's re-evaluate $U(x)$ minimum. Vertex $x = \frac{4}{4} = 1$.  
Wait, derivative of $U(x)$ is $4x-4$. Zero at $x=1$.  
$U(1) = 2 - 4 + 3 = 1$.  
For $x=-1$, $U(-1) = 9$.  
So $L(x)$ and $U(x)$ cross or are ordered.  
$L(x)$ is always $\ge 1$.  
$U(x)$ is always $\ge 1$.  
Also $U(x) \ge L(x)$ since $(x-1)^2 \ge 0$.  
Wait, the condition says $L(x) \le P(x) \le U(x)$.  
Is this just a constraint that restricts the polynomial?  
Yes, but does it imply anything specific about $P(x)$ given $P(11)=181$?  

Let's look at the structure of $P(x) - x^2 + 2x - 2 \le 0$.  
And $P(x) - (2x^2 - 4x + 3) \ge 0$.  
Let's define a function $g(x)$ such that we can solve for coefficients.  
Since $P(11)=181$, maybe the bounds are tight? Or related?  
$P(16)$ might be related to $P(11)$ via symmetry or linearity?  
Wait, if we fix $x=1$, then $L(1) \le P(1) \le U(1)$ implies $P(1) \in [1, 1]$. So $P(1)=1$.  
Also note that $U(x)$ and $L(x)$ are "parallel" in some sense?  
$U(x) - L(x) = (x-1)^2$. This is the width of the interval.  
If we let $Q(x) = \max(L(x), P(x))$ and $R(x) = \min(U(x), P(x))$, it's simpler.  
Actually, consider the equation:  
$(x-1)^2 - (P(x) - L(x))^2$? No.  

Let's try to assume a specific form for $P(x)$ or use Lagrange interpolation if possible?  
We need a value at 16 given at 11. But $P(x)$ is quadratic, so it determines the whole polynomial uniquely once we know two points or one point and slope? No, $P(11)=181$. One condition doesn't determine a quadratic $P(x)$.  
Wait, but the condition "for all real $x$, $L(x) \le P(x) \le U(x)$" puts constraints on coefficients.  
Let's write $P(x) = ax^2 + bx + c$.  
Inequalities:  
1) $a x^2 + b x + c \ge x^2 - 2x + 2$ for all $x$.  
So $(a-1)x^2 + (b+2)x + (c-2) \ge 0$ for all $x$.  
Since this quadratic inequality must hold for all $x$, its discriminant must be $\le 0$.  
$D_1 = (b+2)^2 - 4(a-1)(c-2) \le 0$.  

2) $a x^2 + b x + c \le 2x^2 - 4x + 3$ for all $x$.  
So $(a-2)x^2 + (b+4)x + (c-3) \le 0$ for all $x$.  
Its discriminant must be $\ge 0$. Wait.  
For a parabola $Ax^2+Bx+C$, if it is always $\le 0$, then $A < 0$ and the maximum is at vertex? No, wait.  
If $A > 0$, it goes to $+\infty$. So for it to be $\le 0$, we need discriminant $\ge 0$? No, if $D \ge 0$ it touches 0 or crosses. But for all $x$, we want the graph to be below axis. That requires $A < 0$ and max value $\le 0$.  
Let's check. $(a-2)x^2 + (b+4)x + (c-3) \le 0$.  
The parabola opens downward (since coefficient is $a-2$). For this to be $\le 0$ for all $x$, it means $a-2 < 0$ and its max value is $\le 0$.  
So $(b+4)^2 - 4(a-2)(c-3) \ge 0$. Wait. If $a-2 > 0$, it goes to infinity, so cannot be $\le 0$ everywhere. So we need $a < 2$.  
Then max value occurs at vertex: $\frac{4(b+4)^2}{4(a-2)} + c$? No. Vertex height is $\frac{4ac}{4}$?  
Max value of $(Ax^2+Bx+C)$ is $C$ if vertex is on x-axis?  
Let's use standard form: $y_{max} = \text{something}$.  
For $Ay^2+By+C \le 0$ for all $y$, we need $A<0$ and $\frac{4B^2}{4A} + C \le 0$? No.  
The maximum value is $\frac{4(b/2)^2 - 4ac}{4b}$? No. Max value is at $x=-b/2a$.  
Max value = $c - b^2/4a + a(b/(-a))^2$? No.  
Value at vertex: $C - B^2/(4A) \le 0$? No, the expression is $\le 0$.  
So $C + \text{something}$?  
Let's restart with the discriminant condition for $\le 0$.  
If quadratic $y = A x^2 + B x + C$ is always $\le 0$:  
Case 1: $A=0$, then $Bx+C \le 0$ impossible (since linear function ranges over reals). So $B$ must be non-zero or impossible. Wait, if $A=0$, it's constant $C \le 0$. But here $x \to \infty$ leads to contradiction. So $A \ne 0$.  
Actually, for $\forall x, Ax^2+Bx+C \le 0$, we need:  
$A < 0$ (opens down). Max value is negative. Or just the vertex is max and it's below zero? No, if it goes to infinity at $\pm \infty$, but opens down, it goes to $-\infty$.  
Wait. $Ax^2+Bx+C$ where $A<0$. As $x \to \pm \infty$, $y \to -\infty$. It is never positive (unless between roots? No, outside).  
So the condition "for all real numbers x" implies it never crosses the axis and stays below or touches. Since $-\infty$ at both ends, if it's always $\le 0$, that means it never goes above 0.  
If $A < 0$, then as $x \to \pm \infty$, $Ax^2 \to -\infty$, so definitely $Ax^2+Bx+C < 0$ for large $|x|$. The only problematic case is near the vertex if we want $\le 0$. Wait.  
If a parabola opens downward ($A<0$) and goes to $-\infty$ at ends, it is always negative only if its vertex is below zero? No.  
Wait, if $A>0$, it opens up. To be always $\le 0$, it must never cross x-axis (so max value $\le 0$). So we need $(b/2a - \text{vertex})^2 ...$.  
Wait, I messed up the condition for $U(x) \ge L(x)$ earlier.  
$L(x) \le P(x) \le U(x)$.  
We derived $U(x) - L(x) = (x-1)^2 \ge 0$. So $U \ge L$ is always true.  
But the condition for $P(x) \le U(x)$ is that $P(x) - U(x) \le 0$ for all $x$.  
Let $Q(x) = P(x) - (2x^2 - 4x + 3)$. We need $Q(x) \le 0$. Since $U$ opens upward, if $P$ is "above" or equal, and $P$ must be $\le U$.  
This means $a \le 2$, otherwise $P(x)$ would go to $+\infty$.  
Actually if $a > 2$, $Q(x) \to +\infty$ as $x \to \pm \infty$, so there exists an interval where it is positive (if $Q$ crosses 0). Or just $Q(x)$ must be $\le 0$ everywhere.  
If $a > 2$, then for large $|x|$, $Q(x) > 0$. So we must have $a \le 2$.  
Wait, if $a=2$, $P(x) - U(x) = bx+c+... - (2x^2-4x+3)$? No.  
Let's go back to coefficients.  
$L(x) \le P(x)$: Since $U(x)$ is a quadratic with positive leading coefficient, let's just check conditions again.  

The condition $(x-1)^2 \le P(x) - L(x) \le U(x) - L(x) = (x-1)^2$.  
So $0 \le P(x) - L(x) \le (x-1)^2$.  
Let's denote $\Delta(x) = P(x) - L(x)$.  
Then $\Delta(x) \ge 0$ and $\Delta(x) \le (x-1)^2$.  
Also $P(x) = \Delta(x) + L(x)$.  
We are given $P(11) = 181$.  
So $\Delta(11) = 181 - L(11) = 181 - (11^2 - 22 + 2) = 181 - (121 - 20) = 181 - 101 = 80$.  
Also $\Delta(16) = P(16) - L(16)$. We need $P(16)$.  
Wait, if we can determine $P(x)$ uniquely or its range is constrained enough?  
Since $L(x) \le P(x) \le U(x)$ for all $x$, and at $x=1$, $P(1)=1$.  

Let's check the discriminant of $\Delta(x) = (a-1)x^2 + (b+2)x + (c-2)$.  
We need $\Delta(x) \ge 0$ for all $x$.  
This means $(a-1)(a-1) - \dots$? No.  
It means the minimum of $\Delta(x)$ is $\ge 0$.  
Minimum occurs when discriminant of $\Delta(x)$ is zero (touches axis)? Or vertex is minimum and is positive.  
Wait, if $A = a-1$, for $\Delta(x)$ to be $\ge 0$ everywhere:  
If $A=0$, then linear or constant non-negative. Since $\lim_{x \to \pm \infty} \Delta(x) = \pm \infty$, we must have constant term $\ge 0$. Wait, if $A=0$ and $B \neq 0$, it goes to $\infty$ or $-\infty$. If $A=0$, $Bx + C \ge 0$ impossible. So $A \neq 0$.  
So we must have vertex of $\Delta(x)$ at minimum, so $D_{\Delta} = (b+2)^2 - 4(a-1)(c-2) \le 0$.  

Now consider the upper bound condition: $\Delta(x) \le (x-1)^2 = x^2 - 2x + 1$.  
So $(a-1)x^2 + (b+2)x + (c-2) - (x^2 - 2x + 1) \le 0$ for all $x$.  
$\Delta U(x) = (a-2)x^2 + (b+4)x + (c-3) \le 0$ for all $x$.  
Let this be $V(x)$. We need $V(x) \le 0$ everywhere.  
Since $V(x)$ is a quadratic, it must open downwards to have max value $\le 0$.  
Wait, if $a-2 < 0$, then $x^2$ term has negative coeff, so parabola opens down. Max value is $\frac{4 \times (b+4)^2}{4(a-2)} + c - b^2/(4)?$ No.  
Let's just use the fact that $V(x) = 0$ at vertices? No.  
For $Ax^2+Bx+C \le 0$ for all $x$, we need $A < 0$ and discriminant $\ge 0$. Wait.  
If $A<0$ and it crosses the axis twice, it is positive between roots and negative outside. So "for all x" means it must not cross. But it goes to $-\infty$ so it's fine there. It can only be $\le 0$ everywhere if it does NOT go above 0.  
But if it crosses the axis, it goes below in between (negative) and above outside? No.  
Wait. Let's re-evaluate "quadratic $\le 0$ for all x".  
This requires $A < 0$ and maximum value to be $\le 0$. But max value occurs at vertex if $A<0$.  
Max value is negative or zero.  
Actually, usually we consider $\Delta(x) \ge 0$ for existence of intersection, etc.  
Wait, the condition $V(x) \le 0$ means the parabola is entirely in the lower half plane (including x-axis).  
This requires vertex value to be $\le 0$. But as long as vertex $\le 0$, does it imply $V(x) \le 0$ everywhere? Yes. Because for any $x$, $Ax^2+Bx+C$ is decreasing away from vertex or increasing. If max is negative, then all values are $\le 0$.  
Wait. If max value is $\le 0$, then $Ax^2+Bx+C \le \max(\dots) \le 0$. Yes.  
Is that correct? Yes.  
But wait, if it crosses the axis (has roots), between roots it is negative? No.  
Wait. Let's look at $y=x^2-1$. Roots $\pm 1$. Between -1 and 1 it is $\le 0$? No. At 0, $y=-1 \le 0$. At 2, $y=3 > 0$. So "all x" requires NO roots if max is positive.  
Wait. I am confusing the direction of inequality.  
$V(x) = ax^2+bx+c$. We want $V(x) \le 0$ for all $x$.  
This implies we never go above 0.  
Since parabolas open up if $a>0$, they are $\le 0$ only in the interval between roots. For "all x", this is impossible unless degree is constant or something (impossible here) or discriminant allows it?  
Actually, if $a>0$, $\lim_{x \to \infty} V(x) = \infty$. So $V(x)$ will eventually be positive. So we must have $a < 0$.  
If $a < 0$, then as $|x| \to \infty$, $V(x) \to -\infty$. The parabola opens down.  
It goes from $+\infty$ (wait no, $\lim = -\infty$) to max value $\le 0$.  
Actually, wait. If $a < 0$, it goes to $-\infty$. The maximum is at the vertex.  
For $V(x) \le 0$ for all $x$, we need $V(\text{vertex}) \le 0$.  
And since it's a downward parabola, the values are decreasing as we move away from vertex (downward), so if max $\le 0$, then whole graph is $\le 0$.  
Wait. If vertex is positive (above axis) with $a<0$, then there is an interval around it where it is positive. So we would violate $V(x) \le 0$ for those $x$.  
Wait, if $V(\text{vertex}) > 0$ with $a < 0$, the curve rises from below? No, opens down.  
If vertex $>0$, then near vertex it is positive. So $V(x)$ goes above 0.  
So we need vertex value $\le 0$.  

Let's recheck my logic:  
$a < 0$ (opens down).  
We want $V(x) \le 0$ everywhere.  
This means the entire graph lies on or below x-axis.  
Since it opens down, this is possible if and only if the maximum value $\le 0$.  
The max value is attained at the vertex.  
Wait, let me double check with an example. $y = -x^2 + 1$. Vertex $(0,1)$. Here max value is 1 > 0. It goes above 0. Correct.  
$y = -(x-1)^2 + 5$? No.  
Example: $y = -x(x-1)(x+1)$? Roots are $\pm 1$. At $0$, $y=0$. Between roots (between -1 and 1), is it positive? Yes, for odd degree with negative leading coeff? No, this is cubic.  
Quadratic: $y = -(x^2-1) = -x^2+1$. Max at $x=0$, value 1. Positive inside interval $(-\infty, \dots)$? No.  
If I take $-(x^2-1)$, it is $\le 0$ only outside $[-1, 1]$? No.  
Wait, the vertex of $-(x-1/2)^2$? No.  
Let's take $y = -x^2 + B$. Vertex $(0, B)$. If $B > 0$, then there are $x$ where $y>0$. Specifically $|x| < \sqrt{B}$. So condition fails.  
So we need vertex value $\le 0$.  
This implies that the quadratic touches or crosses x-axis and lies below? No.  
If it is always $\le 0$, it cannot go above. Since it opens down, it goes to $-\infty$ at ends. It could cross up?  
If it crosses up, i.e., has real roots $x_1 < x_2$, then on $(x_1, x_2)$ it is positive (since leading coeff negative? No).  
Wait. Let's trace:  
Start at $-\infty$ (left side), go down? No, parabola with $a<0$ goes to $-\infty$.  
So for very large negative $x$, value is very negative.  
For very large positive $x$, value is very negative.  
It must have a maximum somewhere.  
If max is $\le 0$, then entire graph is $\le 0$. Correct.  
Wait. Does it mean roots?  
If vertex value is 0, it touches at one point (discriminant = 0).  
If vertex value < 0, it intersects x-axis at two points and lies between them as $y>0$? No!  
Wait.  
Let's draw $y = -(x-1)^2 + 1$. Opens down. Vertex at $(1, 1)$. Max is 1. So some part is above 0.  
We want max $\le 0$.  
Example: $y = -(x-1)^2 - 1$. Max is -1. Then everywhere $\le 0$.  
So condition for $V(x) \le 0$ with $a < 0$ is indeed vertex value $\le 0$.  

BUT wait, I derived earlier $V(x)$ must satisfy discriminant $\ge 0$. Why?  
Let's check the logic again.  
For a quadratic $Ax^2+Bx+C$, if $A < 0$:  
It is concave down.  
If it has real roots, it lies between them as positive (if $A>0$) or negative (if $A<0$)? No.  
If $A>0$, roots $\implies \le 0$ outside, $\ge 0$ inside? No. Between roots it is positive.  
Wait, if $A>0$, parabola opens up. Between roots $Ax^2+Bx+C < 0$. So "all x" condition means no roots allowed (or discriminant < 0). But here we have a quadratic that must be $\le 0$ everywhere. This implies it cannot open up?  
Wait. If $A>0$, as $x \to \infty$, $Ax^2 \to \infty$. So for large x, $V(x) > 0$. So condition fails.  
Therefore, we MUST have $a < 2$ (i.e., $A = a-2 < 0$). This matches my deduction.  
And the vertex value must be $\le 0$.  
Wait. What if discriminant is negative? Then $Ax^2+Bx+C$ has no real roots. Since it opens down, and never reaches zero, it is strictly positive or negative everywhere. But since it goes to $-\infty$, it must be always negative.  
So actually, condition $V(x) \le 0$ for all $x$ requires:  
1. $A < 0$.  
   2. Vertex value $\le 0$.  
Wait, if vertex value is negative, say -1. Then everywhere $\le -1$? Yes. But does it satisfy "no roots" or can it cross axis?  
If vertex is at height -1, and opens down, it crosses x-axis at two points? No.  
Wait. If it's a parabola $y = A(x-h)^2 + k$ with $k < 0$ and $A < 0$.  
Then $A(x-h)^2 \le 0$ always? No, if $x \ne h$, then $A(x-h)^2 < 0$ (since $A<0$, $(\dots)^2 \ge 0$). Yes!  
Wait, is this logic correct?  
If $k < 0$, then for all $x$, $A(x-h)^2 + k \le A(0) + k = k < 0$.  
So if the vertex value is negative, and $a<0$, then $V(x)$ is always negative. This satisfies $V(x) \le 0$ everywhere.  
Does this mean I can have real roots? No. If I have a quadratic that goes to $-\infty$ at $\pm \infty$ (so opens down), and vertex value $<0$, then it cannot cross the x-axis.  
Wait. Why? Because if it crosses, it must go from positive to negative or vice versa. But it starts below? No.  
It ends up going lower than 0 at both sides.  
So it never touches or goes above 0.  
So the condition is simply: $a < 2$ and $(b+4)^2 \ge 4(a-2)(c-3)$?  
Wait. If I use discriminant $\Delta = (b+4)^2 - 4(a-2)(c-3)$.  
Let's check my previous logic with $y=x^2-1$ ($a=1>0$). It opens up. Crosses axis at $\pm 1$. Between roots $x^2-1 < 0$. Outside $x^2-1 > 0$. Not "all x".  
Let's check $y = -x^2 + 1$. Opens down. Crosses at $\pm 1$. Between roots, $y < 0$? No. At $x=0$, $y=1 > 0$. So not all x.  
Wait, $A(x-h)^2+k \le 0$.  
If $A < 0$, we want $A(x^2-...) + k \le 0$.  
Divide by negative? No.  
The condition "quadratic $\le 0$ for all x" is equivalent to $A < 0$ and vertex value $\le 0$?  
Wait, if $k > 0$, it will be positive at vertex. So no.  
If $k \le 0$. Since $A < 0$, then for all $y$, $y \le k$? No.  
Consider $-(x-0)^2 + k$. Max is $k$. If $k \le 0$, then graph is below or on x-axis. Correct.  
Wait, if I have roots $x_1, x_2$ with $A < 0$ ($A<0$), then between roots it's negative? No, for parabola opening down (concave down), it is positive *between* the roots?  
Let's check. Roots of $y = -(x-1)(x+1)$ are $\pm 1$. At 0, $y=1 > 0$.  
Ah, so a downward parabola is positive between its roots. It is negative outside.  
So if we require it to be $\le 0$ everywhere, we can't have "positive between roots".  
Wait. This contradicts earlier thinking about vertex value.  
Let's re-evaluate carefully.  
Parabola $y = Ax^2 + Bx + C$ with $A < 0$.  
Graph goes down at both ends. So it has a maximum at the vertex $( -B/2A, \frac{4BC-B^2}{4A} )$. Wait, max value is $\frac{4AC...}{4A}$? No.  
Let's look at the graph shape. "U" is up ($A>0$), inverted U is down ($A<0$).  
Inverted U goes from $+\infty$ to $-\infty$? NO.  
As $x \to \pm \infty$, $Ax^2$ dominates and since $A < 0$, $x^2 > 0 \implies Ax^2 \to -\infty$.  
Wait. I am confused.  
If $x \to +\infty$, $x^2 \to +\infty$. Then $A x^2 \to -\infty$ (if $A<0$). Correct.  
If $A > 0$, $Ax^2 \to +\infty$.  
So an inverted U goes from $-\infty$ to $+\infty$? No.  
Wait, "U" shape means min at vertex. $x \to \infty \implies y \to \infty$.  
If I rotate it 180 degrees ("N" shape), $x \to \infty \implies y \to -\infty$.  
Let's take $y = -x^2$. Vertex is 0. For $x=0$, $y=0$. For $x=1, y=-1$.  
This function never goes above 0? Wait.  
Is it possible to have $y > 0$? Yes, for all x, if $A < 0$.  
Wait, I am confusing myself with signs.  
Let's visualize $y = -x^2 + 1$. It crosses axis at $\pm 1$.  
Between  

## Answer

*(none: the token cap hit during thinking)*
