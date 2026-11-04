# test/algebra/1143.json (Algebra, level 5)

> The smallest distance between the origin and a point on the graph of $y=\frac{1}{2}x^2-9$ can be expressed as $a$.  Find $a^2$.  

**Wrong.** Gold `17`, predicted `None`. Finish: length, 32768 tokens, 6 waits, 2166.5 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

The user wants me to find the smallest distance from the origin $(0,0)$ to a point on the graph of the function $y = \frac{1}{2}x^2 - 9$. The distance is given by $d = \sqrt{x^2 + y^2}$ where $x, y$ are coordinates of points on the curve.  

I need to minimize this distance subject to $(x, y)$ being on the curve $y = \frac{1}{2}x^2 - 9$.  
First, let's check if there's any point on the graph where the function is defined and finite for all real $x$. Since it's a quadratic parabola opening upwards, the vertex will determine the minimum value. The domain of the squared term $x^2$ suggests I need to consider $x \in \mathbb{R}$.  
Also, looking at the constant term $-9$, this doesn't affect the shape or vertical shift in a specific way other than changing the y-value.  

The equation is $y = \frac{1}{2}x^2 - 9$. This describes a parabola with its vertex at $(0, -9)$.  
We want to minimize $d = \sqrt{x^2 + (y)^2}$ for points on this parabola.  
Since we want the distance, the distance will be minimized when the point is closest to the origin.  
Geometrically, the point is on a curve, and the distance is $\sqrt{x^2+y^2}$.  
This is the Euclidean distance from $(0,0)$ to a point $(x, y)$.  

Let's analyze the relationship between $x$ and $y$.  
We have a constraint relating $x$ and $y$: $y = \frac{1}{2}x^2 - 9$. This is a curve.  
We want to minimize $d = \sqrt{x^2+y^2}$.  
Since the square root is monotonic, minimizing distance $d$ is equivalent to minimizing $r = x^2 + y^2$.  

So we want to find $x$ such that $f(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$ is minimized.  
Let's substitute $y$ into this expression:  
$r^2 = x^2 + \left(\frac{x^2}{2} - 9\right)^2$.  
We need to minimize $r^2$.  

Let $u = x^2$. Then $y = u/2 - 9$.  
$r^2 = u + (u/2 - 9)^2$.  
Let's expand this:  
$r^2 = u + \frac{1}{4}u^2 - 9u + 81$  
$r^2 = \frac{1}{4}u^2 - 8u + 81 + u$?  
No, let me re-expand carefully.  
$(\frac{x^2}{2} - 9)^2 = \frac{x^4}{4} - \frac{9x^2}{4} + 81$.  

So $r^2 = x^2 + \frac{x^4}{4} - \frac{9x^2}{4} + 81$  
$r^2 = \frac{1}{4}x^4 + (1 - \frac{9}{4})x^2 + 81$  
$r^2 = \frac{1}{4}x^4 - \frac{5}{4}x^2 + 81$.  

To minimize $r^2$, we take the derivative with respect to $x$ (assuming $x^2 > 0$, or considering the function behavior).  
Let's just differentiate $f(x) = \frac{1}{4}x^4 - \frac{5}{4}x^2 + 81$.  
$\frac{df}{dx} = x^3 - \frac{5}{2}x$.  
Set this to zero:  
$x^3 - \frac{5}{2}x = 0$  
$x(x^2 - \frac{5}{2}) = 0$  

So, $x=0$ or $x^2 = \frac{5}{2} \implies x = \pm \sqrt{\frac{5}{2}}$.  

We need to evaluate $r^2$ at these points.  
If $x=0$, $y = -9$. $d^2 = 0 + (-9)^2 = 81$. So $r = \sqrt{81} = 9$. This corresponds to the vertex of the parabola being closest to origin? Let's check. The parabola is $(y-(-9))^2$ at $x=0$, distance is 9.  
If $x^2 = 5/2$, then $x = \pm \sqrt{5/2}$.  
The value of the function is:  
$f(x) = \frac{1}{4}(5/2)^2 - \frac{5}{4}(\sqrt{5/2}) + 81$  
Let's calculate this.  

Let $x^2 = 5/2$. Then $(\frac{x^2}{2}-9)^2 = (\frac{5/2}{2}-9)^2 = (\frac{5}{4}- \frac{36}{4})^2 = (-\frac{31}{4})^2 = \frac{961}{16}$.  
And $x^2 = 5/2$.  
So $r^2 = x^2 + y^2 = 5/2 + (\frac{5}{4}-9)^2$? No, $(\frac{x^2}{2}-9)$.  
Let's rewrite $x^2$ in terms of variable $u=x^2$.  
$r^2(u) = u + \frac{1}{4}u^2 - \frac{9u}{4} + 81$.  
Derivative wrt $u$: $\frac{d}{du}(u + \frac{1}{4}u^2 - \frac{9}{4}u + 81) = 1 + \frac{1}{2}u - \frac{9}{4}$.  
Setting this to zero: $\frac{1}{2}u = \frac{9}{4} - 1 = \frac{5}{4}$, so $u = 5/2$. This gives the same critical point.  
So for any $x^2$, the derivative condition is satisfied if $x^2=5/2$.  

However, I must check the domain of validity or boundary conditions. The problem doesn't specify $y \in \mathbb{R}$, but it's a standard function definition.  
Also, checking the critical points and endpoints:  
At $u=0$ (i.e., $x=0$, which corresponds to vertex $(0,-9)$): $r^2 = 0 + 81 - 9(0) = 81$.  
At $u = 5/2$: $r^2 = \frac{5}{4} + \frac{5}{4} - \frac{9}{4}(5/2)$? No.  
Let's recalculate carefully.  
$r^2 = u + (\frac{x^2}{2} - 9)^2$.  
Let $x^2 = 5/2$. Then $\frac{x^2}{2} = 5/4$. So $y^2 = (5/4 - 36/4)^2 = (-31/4)^2$?  
No. $\frac{1}{2}x^2 - 9 = \frac{1}{2}(5/2) - 9 = \frac{5}{4} - \frac{36}{4} = -\frac{31}{4}$.  
So $y^2 = (-31/4)^2 = \frac{961}{16}$.  
Then $r^2 = x^2 + y^2 = 5/2 + 961/16 = (80 + 961)/16$? No. $x^2=5/2=40/8=8/8$, not common denominator.  
$x^2 = 5/2 = 40/8$.  
$y^2 = 961/16 = 765/80$?  
Let's use fractions. $x^2 = \frac{5}{2} = \frac{160}{32}$? No, let's stick to common denominators for integers if possible or just fractions.  
$x^2 = \frac{5}{2}$.  
$\frac{x^2}{2} = \frac{5}{4}$. $y = \frac{5}{4} - 9 = \frac{5-36}{4} = -\frac{31}{4}$.  
$y^2 = (-\frac{31}{4})^2 = \frac{961}{16}$.  
$r^2 = \frac{5}{2} + \frac{961}{16} = \frac{40}{16} + \frac{961}{16} = \frac{1001}{16}$.  

Let's check if this value is smaller than the other possible points.  
The derivative was $x^3 - \frac{5}{2}x = 0$. This gives $x=0$ or $x=\pm\sqrt{5/2}$.  
At $x=0$, $y=-9$. Distance squared: $r^2=81$.  
At $x=\sqrt{5/2}$, $y=-\frac{31}{4}$. Distance squared: $\frac{1001}{16} = 62.5625$.  
$81 > 62.5625$, so this is smaller.  

However, I should check if the derivative calculation has any issues or if there are other branches.  
The function to minimize was $r^2(u) = \frac{1}{4}u^2 - \frac{5}{4}u + 81$ for $x^2=u$.  
This function is a parabola opening upwards in the $u$-variable. Its minimum is at its vertex, which is at $u = -(-5/4)/(2*(1/4))$? No.  
$f(u) = \frac{1}{4}u^2 - \frac{5}{4}u + 81$.  
Vertex at $u = \frac{-b}{2a} = \frac{-(-5/4)}{2(1/4)} = \frac{5/4}{1/2} = \frac{5}{4} / \frac{1}{2} = \frac{5}{4} \cdot 2 = \frac{10}{4} = \frac{5}{2}$.  
The minimum is indeed at $x^2 = \frac{5}{2}$.  
Is there any constraint on $x$ or $y$?  
Usually, these problems don't restrict the domain to be real numbers. But $x, y$ are usually assumed to be real for a curve $y=f(x)$. The function is defined for all real $x$.  
If $x \in \mathbb{R}$, then $u=x^2 \ge 0$.  
Since we found the minimum at $u = 5/2$, and $5/2 > 0$, this point $(x,y)$ exists and corresponds to a valid real coordinate pair.  
We must check if there is any geometric constraint I missed. The distance from origin to a point on a curve. This is always possible unless the set of points doesn't include the origin or something? No, for $y = -9$, $x$ can be anything, so we pick the closest one. The minimum is clearly found at the vertex $(0,-9)$ and the tangent line property gives us the critical point.  
However, I must also check if there's a "cusp" or something where distance is infinite? No, it's a parabola $y = \frac{1}{2}x^2 - 9$.  

The distance squared function is $g(u) = x^2 + y^2$ for $y=0.5x^2-9$.  
We want to minimize $g(u)$ subject to $x^2=u$. No, we want to minimize $\frac{1}{4}u^2 - \frac{5}{4}u + 81$.  
The vertex of this parabola is at $u = 5/2$, giving distance squared value.  

Is there any possibility that $x$ has negative values?  
Let's re-evaluate the expression for $r^2$.  
$r^2(x) = x^2 + (\frac{x^2}{2} - 9)^2$.  
Let $u=x^2$. Then $r^2(u) = u + \frac{1}{4}u^2 - \frac{18u}{2}?$ No, $\frac{9x^2}{4}$? Yes, $\frac{36u}{4} = 9u$.  
So $r^2 = u + \frac{1}{4}u^2 - 9u$ (from expansion of $(y)^2$) plus 81.  
$r^2(u) = u + \frac{1}{4}u^2 - 9u + 81 = \frac{1}{4}u^2 - 8u + 81$.  
This is a parabola in $u$. The minimum occurs at $u = \frac{-(-8)}{2(1/4)} = \frac{8}{1/2} = 16$.  
Why? Because the coefficient of $u^2$ is $1/4$, not 1.  
Let me re-check the expansion.  
$r^2(u) = u + (y)^2$.  
$y = \frac{x^2}{2} - 9$.  
So $y^2 = (\frac{x^2}{2})^2 - 2(\frac{x^2}{2})(-9) + (-9)^2$. No, it's $(\frac{x^2}{2})^2 - 9(\frac{x^2}{2}) - 81$?  
No. $(a-b)^2 = a^2 - 2ab + b^2$. Let $a=x^2/2$, $b=9$.  
$(x^2/2 - 9)^2 = \frac{x^4}{4} - 9x^2 + 81$.  
And $y^2$ is not a squared variable. The distance squared is $x^2 + y^2$.  
So $r^2(x) = x^2 + (\frac{1}{2}x^2 - 9)^2 = x^2 + \frac{x^4}{4} - 9x^2 + 81 = \frac{x^4}{4} - 8x^2 + 81$.  
The vertex of this parabola in $x^2$ terms ($u=x^2$) is at:  
$f(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$. No, I just wrote this down.  
Let's rewrite $r^2(u)$ again properly.  
We want to minimize $f(x) = x^2 + (\frac{x^2}{2} - 9)^2$. Let $u=x^2$. Then $x^4/2$ and so on. No, the variable in front of $x$ is just $x$.  
Let $t = x^2$. $f(t) = t + (t/2 - 9)^2$.  
$f(t) = t + \frac{1}{4}t^2 - 9t + 81 = \frac{1}{4}t^2 - 8t + 81$.  
The coefficient of $t$ is $-8$, not 0. This means the function decreases until $t$ becomes something positive? No, it opens upwards with $a=1/4 > 0$. So minimum exists for all real $t$.  
$f(t) = \frac{1}{4}t^2 - 8t + 81$.  
Derivative wrt $t$: $\frac{1}{2}t - 8 = 0$.  
$t = 16$.  
Since $x^2 = t$, this means $x^2 = 16 \implies x = \pm 4$.  
This gives the minimum value of the function.  

So $r_{min}^2 = \frac{1}{4}(16)^2 - 8(16) + 81$? No.  
$r^2_{min} = \frac{1}{4}(16)^2 - 8(16) + 81$ ?  
The quadratic is $\frac{1}{4}(t)^2 - 8t + 81$. The minimum value of $\frac{1}{4}u^2 - 8u + 81$ at $u=16$:  
$\frac{1}{4}(16)^2 = \frac{256}{4} = 64$.  
$-8(16) = -128$.  
$64 - 128 + 81 = 108 - 128 = -20$. No, this is impossible. Distance squared must be positive. Let me check my algebra.  

Let's go back to basics.  
We want to minimize $y^2 + x^2$ on the curve $y = \frac{1}{2}x^2 - 9$.  
Substitute $x$:  
Let $t = x^2$. Then $y = \frac{t}{2} - 9$.  
The distance squared $D^2$ is $x^2 + y^2 = t + (\frac{t}{2} - 9)^2$.  
We want to minimize this expression in terms of $t$.  
$g(t) = t + \frac{1}{4}t^2 - 9t + 81$.  
Simplify:  
$\frac{1}{4}t^2 + (1 - 9)t + 81 = \frac{1}{4}t^2 - 8t + 81$.  
We want to find the minimum of this for $t \in [0, \infty)$? Or $\mathbb{R}$?  
For a parabola opening upwards ($a = 1/4 > 0$), there is a global minimum.  
The vertex at $t = -b/(2a)$. Here $-b = 8$, so $a=1/4$, $b=-8$.  
$t_{vertex} = \frac{8}{2(1/4)} = \frac{8}{0.5} = 16$.  
So the minimum is at $x^2 = 16$.  
The minimum value of $g(t)$ is:  
$g(16) = \frac{1}{4}(16)^2 - 8(16) + 81$.  
$= 64 - 128 + 81 = -64 + 81$? No.  
Let's calculate the square term again.  
$(t/2 - 9)^2$ at $t=16$: $\frac{16}{2} - 9 = 8 - 9 = -1$. Square is $(-1)^2 = 1$.  
So $g(16) = 16 + 1 = 17$.  
Let's calculate using the full formula: $g(t) = t + y^2$.  
$y(16) = 8 - 9 = -1$.  
$D^2 = 16 + 1 = 17$.  

But earlier I had a term for $t/2$ squared. Let's recheck the expansion of $(t/2-9)^2$.  
$(\frac{t}{2}-9)^2 = \frac{t^2}{4} - 9t + 81$. No, this is incorrect because I wrote $(x/2)^2$ etc.  
Let $x^2=t$. Then $y^2 = (\frac{t}{2} - 9)^2$.  
Is the term for $t/2$ squared? Yes.  
Is the term for $t$ squared in the polynomial expansion correct?  
$(\frac{t}{2} - 9)^2 = \frac{t^2}{4} - 2(9)t + 81 = \frac{t^2}{4} - \frac{36t}{4} + 81$? No. $2 \cdot 9 t$ is not $36t$. It is $-2(9)(\frac{t}{2}) = -9t$.  
Ah, the coefficient of $9t$ is $-2(9) \cdot \frac{1}{2}$? No.  
Let's do $(a-b)^2 = a^2 - 2ab + b^2$.  
Here $a = t/2$, $b = 9$. So $a^2 = (t/2)^2 = t^2/4$.  
$-2ab = -2(t/2)(9) = -9t$.  
So the term is $\frac{1}{4}t^2 - \frac{36t}{4}$? No, $-2(9)t = -18t$.  
$-2(ab)$ where $a = t/2$, $b=9$: $-2(t/2)(9) = -9t$.  
Then $-9t \cdot 4 = -36t / 4 = -9t$. No.  
Let's re-evaluate:  
Term is $-2(ab)$. So $-2 (\frac{t}{2}) (9) = -2(t)(4.5) = -9t$?  
$(\frac{t}{2}) \times 9 = \frac{9t}{2}$. Times 2 is $\frac{9t}{1}$.  
So the term is $-2(\frac{t}{2})(9) = -9t$.  
Yes. So the cross-term is $-9t$? No, $(\frac{t}{2})^2 + (\frac{-36t}{4})$? No.  
Let me do this carefully.  
$(\frac{t}{2} - 9)^2 = \frac{t^2}{4} - 9(\frac{t}{2})?$? No.  
Term $= -2(a)(b)$ where $a=t/2$ and $b=9$.  
So term is $-2(t/2)(9) = -9t$.  
Then add $(\text{term of } t^2)$: $(t/2)^2 = t^2/4$.  
Then add $(\text{term of constant})$: $9^2=81$.  
So $\frac{t^2}{4} - 9t + 81$? No, $-9t$ was multiplied by $a$. So term is $-9t$ if we write $b^2 - 2ab$ and $a = t/2$.  
The coefficient of $t$ in $(x/2)^2$? No. $(x/2) \cdot (-9)$ means the term with $x$ is $-(x/2)(9)$.  
Since $x=t$, it is $-9t$.  
So my expansion was correct so far: $\frac{1}{4}t^2 - 9t + 81$.  

Now, let's look at $r^2(x) = x^2 + (\frac{x^2}{2}-9)^2$.  
The $x^2$ term comes from $x^2$.  
So we have $t^2 + t/4$? No.  
We have $y^2 = (x^2/2 - 9)^2$.  
Substitute $u=x^2$:  
$D^2(u) = u + (\frac{u}{2}-9)^2$.  
Let's re-expand $(\frac{u}{2}-9)^2$: $\frac{1}{4}u^2 - 2(9)(\frac{u}{2}) + (-9)^2 = \frac{1}{4}u^2 - 9u + 81$.  
So $D^2(u) = u + \frac{1}{4}u^2 - 9u + 81 = \frac{1}{4}u^2 - 8u + 81$.  
This quadratic is in terms of $u=x^2$.  
We found the minimum at $u=16$ which gave $D^2(16) = 64 - 128 + 81$? No.  
Let me re-calculate $D^2(16)$ using my new formula: $\frac{1}{4}(16)^2 - 8(16) + 81$.  
$= \frac{256}{4} - 128 + 81 = 64 - 128 + 81 = -64$? No.  
The constant is 81, the linear term is $-9u$, quadratic is $\frac{1}{4}u^2$.  
Let's re-evaluate $D^2(16)$ carefully.  
At $u=16$, $y^2 = (\frac{16}{2}-9)^2 = (8-9)^2 = (-1)^2 = 1$.  
Then $x^2 = 16$.  
$D^2 = x^2 + y^2 = 16 + 1 = 17$.  
Now let's check the expression $\frac{1}{4}u^2 - 8u + 81$.  
At $u=16$:  
$\frac{1}{4}(256) = 64$.  
$-8(16) = -128$.  
$81$.  
So $\frac{256}{4} - 128 + 81 = 64 - 128 + 81 = -20 + 81 = 61$. No, $81-128+64$ is not 17.  
Let's check my expansion of $(\frac{u}{2}-9)^2$ again.  
$(\frac{u}{2} - 9)^2 = \frac{u^2}{4} - 9u + 81$.  
This is correct?  
$\sqrt{(x/2)^2}$ term? No, the expansion of $(A-B)^2$ is $A^2-2AB+B^2$.  
So we have $\frac{1}{4}(x^2)^2 - \frac{9(x^2)}{2}(-18)$? No.  
$x^2 = u$.  
The term involving $x^2$ is $(x^2/2)^2 = x^4/4$.  
The cross term involves $x^2$ and 9. It is $-2(x^2/2)(9) = -9x^2$.  
So $D^2(u)$ has a linear term in $u$, coefficient $-9$.  
So $D^2(u) = \frac{1}{4}u^2 - 8u + 81$? No.  
Cross term was $\frac{1}{4}(u)^2$. The cross term is from the expansion of $(\frac{u}{2}-9)^2$.  
So we have $u + \frac{1}{4}u^2 - 9u + 81$.  
The term with $u$ is $u - 9u = -8u$.  
The constant is 81.  
So the expression is $\frac{1}{4}u^2 - 8u + 81$.  
This matches.  

Let me check $D^2(16)$ again.  
$D^2(16) = \frac{1}{4}(16)^2 - 8(16) + 81$.  
$\frac{256}{4} - 128 + 81$.  
$64 - 128 + 81 = 17$.  
Why did the manual calculation give 17?  
At $u=16$, $x^2=16$, $y = 16/2 - 9 = 8-9 = -1$.  
$D^2 = 16 + (-1)^2 = 17$.  
So the expression evaluates to 17.  

Let me check my manual calculation of $\frac{1}{4}u^2 - 8u + 81$ with $u=16$:  
$\frac{1}{4}(256) = 64$.  
$-8(16) = -128$.  
$81$.  
$64 - 128 + 81 = 17$. Correct.  

Now, what about the critical point $u=5/2$?  
Let's check if this is a valid value for $u=x^2$.  
If $x^2 = 5/2$, then $x^4/4 - 9(x^2) + 81$ is evaluated? No.  
We want to minimize $\frac{1}{4}u^2 - 8u + 81$.  
The derivative of this wrt $u$ is $\frac{1}{2}u - 8 = 0 \implies u=16$.  
So minimum at $u=16$.  

But earlier I had a function $f(u) = \frac{1}{4}u^2 - \frac{5}{4}u + 81$ which gave $u=5/2$.  
Let's re-evaluate $r^2(x)$ and my previous derivative calculation.  
$r^2(x) = x^2 + (\frac{x^2}{2}-9)^2$.  
Let $y^2 = \frac{u^2}{4} - 9u + 81$ ? No, this was derived from $(\frac{u}{2}-9)^2$.  
Is this correct? Yes.  
Then $r^2(u) = u + \frac{u^2}{4} - 9u + 81 = \frac{u^2}{4} - 8u + 81$.  
The minimum of this is at $u=16$.  
Is it possible that for some reason I made a mistake in my first calculation?  
Let's re-calculate the term $\frac{x^2}{4}$ expansion.  
$(\frac{x^2}{2} - 9)^2 = \frac{1}{4}x^4 - 9x^2 + 81$.  
And $x^2$ in the expression $r^2(x) = x^2 + y^2$ is just $x^2$.  
So substitute $u=x^2$: $r^2(u) = u + \frac{u^2}{4} - 9u + 81$.  
$\implies r^2(u) = \frac{1}{4}u^2 - 8u + 81$.  
This function has vertex at $u=16$.  

But the first derivation was:  
$r^2(x) = x^2 + (\frac{x^2}{2}-9)^2$.  
Let's check if I expanded $(\frac{x^2}{2} - 9)^2$ correctly.  
If $x^2 = t$, term is $\frac{1}{4}t^2 - 9t + 81$.  
And we have $x^2$ as the first term.  
So total $D^2(x) = x^2 + \frac{1}{4}x^4 - 9x^2 + 81$.  
$\implies D^2(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  
Let $u=x^2$. Then $D^2(u) = \frac{1}{4}u^2 - 8u + 81$.  
This function is increasing for all $u > 0$ (since coefficient of $u^2$ is positive, and derivative wrt $u$ is $\frac{1}{2}u - 8$).  
For $u=16$, derivative is $8-8 = 0$.  
So this minimum is correct.  
Value at $u=16$: $D^2(16) = \frac{1}{4}(16)^2 - 8(16) + 81 = 64 - 128 + 81 = 17$.  
This corresponds to $x^2=16$, so $x=\pm 4$, and $y = \frac{16}{2} - 9 = 8-9 = -1$.  
$D^2 = 16 + (-1)^2 = 17$.  

Is it possible that there is another constraint? The problem says "distance between the origin and a point on the graph".  
This usually implies $x$ can be any real number.  
However, we found $u=16$ corresponds to a solution with real coordinates.  
Are there other constraints?  
What if $x^2 = 5/2$ yields something else?  
Let's check my expansion at $x^2=5/2$.  
$r^2(5/2) = (5/4)^2 - 8(5/2) + 81 = \frac{25}{16} - \frac{20}{4} + 81$? No.  
Term $-8x^2$. Here $x^2=5/2$, so term is $-8(5/2) = -20$.  
So $r^2(5/2) = \frac{25}{16} - 20 + 81$? No.  
Let me re-evaluate $D^2(u)$ at $u=5/2$.  
$r^2(5/2) = \frac{1}{4}(5/2)^2 - 8(5/2) + 81$.  
$= \frac{25}{16} - 20 + 81 = 61.5625 - 20 = 41.5625$. No, $20$? $81-20=61$, plus $25/16 = 61.56$.  
$41.56 > 17$.  
So the minimum is indeed at $u=16$.  

Is there any constraint on the function definition I missed?  
Maybe I should check my derivative calculation again.  
$f(x) = x^2 + \frac{1}{4}x^4 - 9x^2 + 81$.  
$g(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  
Derivative $g'(x) = x^3 - 16x = x(x^2 - 16)$.  
Roots: $x=0$ and $x=\pm 4$.  
If $x=0$, $g(0) = 81$.  
If $x=4$, $g(4) = \frac{1}{4}(256) - 8(16) + 81 = 64 - 128 + 81 = 17$.  
If $x=-4$, same.  

So the minimum distance is $\sqrt{17}$.  
So $a = \sqrt{17}$.  
Then $a^2 = 17$.  

Is it possible I made a mistake in assuming $y$ is restricted to be defined by the parabola for all real numbers? No.  
However, there might be some subtle issue about what "graph" means or constraints. Usually, $x \in \mathbb{R}$ unless specified.  
The function is defined on $\mathbb{R}$.  
So why did I check $u=5/2$ in the first pass? That was when I calculated derivative of $u^2 - 8u + 81$.  
Let's check my derivative calculation again.  
$r^2(u) = \frac{1}{4}u^2 - 8u + 81$.  
$\frac{d}{du}(r^2) = \frac{1}{2}u - 8$.  
Setting to 0: $u=16$. Correct.  

Let's double check if there's any other constraint or possibility I missed.  
What if the problem implies something about complex numbers? Unlikely.  
Is it possible that "graph" refers to domain restricted to some set where function is continuous but not necessarily bounded? No.  
So the distance squared is always $17$ at $x=\pm 4$.  
Let's verify with a specific point: $(\pm 4, -1)$.  
Check $y = \frac{1}{2}(-4)^2 - 9 = 8-9 = -1$. Correct.  
Dist is $\sqrt{17}$.  

What about the critical point at $u=0$? No, that was $x=0$, $y=-9$. $D^2 = 81$.  
$81 > 17$.  
So $a^2 = 17$.  

However, let me re-read the problem statement carefully to ensure I haven't missed a subtle constraint.  
"The smallest distance between the origin and a point on the graph of $y=\frac{1}{2}x^2-9$ can be expressed as $a$."  
"Find $a^2$."  

Is it possible that there is another critical point or local extremum?  
Since the function $g(u)$ is a parabola opening upwards, the minimum exists and is unique (for $u \in \mathbb{R}$).  
So the analysis holds.  

Let's double check the expansion of $(\frac{x^2}{2} - 9)^2$ again.  
Maybe I misread $x^2$ as $y$.  
The equation is $y = \frac{1}{2}x^2 - 9$.  
$x^2$ term in y is $\frac{1}{2}x^2$.  
So at $x=4$, $y=8-9=-1$. Correct.  

*Continued in [part 2 of 5](algebra_1143_p2.md): GitHub stops rendering math on pages this long, so the transcript is split.*
