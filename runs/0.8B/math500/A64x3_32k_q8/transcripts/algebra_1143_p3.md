# test/algebra/1143.json, part 3 of 5

[Previous part](algebra_1143_p2.md) · [Start](algebra_1143.md)

$r(x) = x^2 + y^2$.  
Substitute $y$: $r(x) = x^2 + (\frac{x^4}{4} - 9x^2 + 81)$.  
Simplify: $\frac{1}{4}x^4 - 8x^2 + 81$. (From my previous expansion).  
Derivative wrt $x$: $\frac{d}{dx}(\dots) = x^3 - 16x$.  
Set to 0: $x(x^2-16)=0$. Roots $x=0, \pm 4$.  
This means critical points are at $x=0$ and $x=\pm 4$.  
At $x=0$, $r(0)=81$.  
At $x=\pm 4$, $r(\pm 4) = 17$.  
Since derivative changes sign from negative to positive between 0 and 4 (check $u=1$? No, function of x).  
Is it decreasing until 4 or increasing?  
Let's check values.  
$x=2$: $r(2) = 4 + (\frac{2}{2}-9)^2 = 4 + (-7)^2 = 53$.  
Derivative at $x=0$ is 0.  
At $x=0$, derivative of polynomial expression was $x^3-16x$. So slope near 0 is 0.  
At $x=4$: slope is 0? No, slope near 4 is not necessarily positive/negative.  
Let's check the shape of $\frac{1}{4}u^2 - 8u + 81$ with respect to $x$.  
No, $r(x)$ is a function of $x$.  
$r'(x) = x^3 - 16x$.  
For $x>0$, $r'(x) < 0$ if $x > \sqrt{16}$? No.  
Roots at $x=4$.  
If $x \in (0, 4)$, say $x=2$, $r'(2) = 8 - 32 = -24$. Decreasing.  
At $x=4$, $r'(4) = 64 - 64 = 0$.  
So it starts decreasing after $x=0$? No, derivative is negative for small $x > 0$.  
So function decreases until $x=\sqrt{16}=4$?  
Let's check sign. $x^3 - 16x = x(x^2-16)$.  
If $0 < x < 4$, then $x>0$ and $x^2-16 < 0$. So product is negative.  
So $r'(x)$ is negative for $x \in (0, 4)$.  
This means $r(x)$ is decreasing from $x=0$ to $x=4$.  
At $x=0$, value is 81.  
At $x=4$, value is $r(4)=17$.  
So distance decreases from 81 to 17.  
But this contradicts the earlier finding that vertex of parabola was at $u=16$ giving 17.  
This implies $r(x)$ has a minimum at $x=4$, not $u=16$.  
The value is 17.  
Is 17 the global minimum?  
At $x=0, r(0) = 81$. At $x=\pm \sqrt{4} = \pm 4$, value is 17.  
Since derivative is negative for $x<4$, the function decreases monotonically from $x=0$ to $x=4$.  
Thus minimum is at $x=4$.  
This implies min distance squared is 17.  

Let's double check my expansion of $(\frac{x^2}{2}-9)^2$.  
Term $A = \frac{x^2}{2} - 9$.  
$A(x) = x^2/2 - 9$.  
$A'(x) = x$.  
$(A(x))^2 = (\dots)^2 = A^2 + 2AA' + (A')^2$? No.  
Derivative of $(\frac{1}{4}x^2-9)^2$ is $2(\frac{1}{4}x^2-9) \cdot x$.  
The derivative term I used in my "derivative of polynomial" calculation was:  
$\frac{d}{dx}(x^2+y^2) = 2x + 2y y'$.  
$y = \frac{1}{2}x^2-9$. $y'=x$.  
So derivative is $2x + 2(\frac{x^2}{2}-9)x$.  
Simplify: $2x + x^3 - 18x$.  
$= x^3 - 16x$? No. $2(x^2/2-9) = x^2 - 18$.  
So derivative is $2x + (x^3 - 18x)$? No, this term involves $(\frac{x^2}{2}-9)^2$ which is $A^2$.  
Let me re-evaluate the term $(\frac{x^2}{2}-9)^2$ carefully.  
It is a function of $x$. Let $f(x) = (\frac{x^2}{2}-9)^2$.  
$f'(x) = 2(\frac{x^2}{2}-9)(x/2)$? No, $\frac{d}{dx}(\frac{x^2}{2}-9)^2$ is derivative of squared function.  
Let $B(x) = \frac{x^2}{2}-9$. Then $f'(x) = 2B(x) B'(x)$.  
$B'(x) = x$.  
So $f'(x) = 2(\frac{x^2}{2}-9)x = x^3 - 9x$? No.  
$2(x/2)(x^2)$? No, derivative of $(x/2)^2$ is $2(x/2)x$? No.  
Let's check $(A(x))^2$. $\frac{d}{dx} A(x)^2 = 2 A(x) \frac{dA}{dx} = 2 (\frac{x^2}{2}-9) x = x^3 - 18x$.  
So $f'(x) = x^3 - 18x$? No, term is $\frac{x^4}{4}$? No.  
Let's check $(\frac{1}{2}x^2-9)^2$.  
$\frac{d}{dx}( \frac{1}{2}x^2 - 9 ) = x$.  
So $2(x)(x) = 2x^2$?  
No, derivative of $x$ is 1. So $(x^2/2-9)^2$.  
Derivative: $2(\dots)^2 \cdot (\frac{x}{2})$? No, $\frac{d}{dx}(\dots)^2 = 2(\dots) (\frac{x}{2})$ is derivative of square? No.  
Let's differentiate $(\frac{x^2}{2}-9)$ directly: $x$.  
So derivative of term is $2(x)(x) = 2x^2$.  
The term I wrote earlier was $(\frac{1}{4}x^4-9x^2+81)$.  
If this matches the original expansion, then $\frac{d}{dx}$ yields $x^3 - 18x$? No.  
The term is $\frac{x^2}{2}-9$. Its derivative is $x$.  
So $(\frac{x^2}{2}-9)^2$ derivative is $2(\frac{x^2}{2}-9)(x) = x^3 - 18x$? No, $2(1/2)x \cdot 1 = x$.  
Let's check algebra again.  
$B(x) = x^2/2 - 9$.  
Derivative of $B(x)$ is $x$.  
So derivative of $B(x)^2$ is $2 B(x) B'(x) = 2 (x^2/2 - 9) x$.  
This is $(x^3 - 18x)$? No.  
Term is $2(x)(x^2/2) = x^3$.  
And term is $-9 \cdot 2$? No, derivative of constant is 0.  
So term is $-9 \cdot 0$? No. It's just $(x^2 - 18x)$? No.  
It is $2(x/2)(x) = x^3$? No, it is $2(x/2)x = x^2$.  
And then $B(x) B'(x)$ where $B'(x)=x$.  
So term is $(x^2/2-9) \cdot x = x^3 - 18x$.  
No, $(x^2/2 - 9)^2$ derivative is not this. It's $2(\frac{x^2}{2}-9) \cdot \frac{d}{dx}(\frac{x^2}{2}-9)$? No.  
The chain rule: $\frac{d}{dx}[f(x)^n] = n f^{n-1}(x) f'(x)$.  
So here $n=2$, so $f^{1}=B$, $f'=x$. So term is $2 B \cdot x$.  
So derivative of $(\frac{x^2}{2}-9)^2$ is $2(\frac{x^2}{2}-9)(x) = x(\frac{x^2}{2}-9)$? No.  
It is $2(x/2)(x)$? No, $\frac{d}{dx}(\frac{x^2}{2}) = x$.  
So the term is $(\frac{x^2}{2}-9)x$ times 2?  
Yes. So $2 \cdot (\frac{x^2}{2}-9) \cdot x$.  
This simplifies to $x(x^2/2-9)$? No, it's $x( \dots )$? No, term is $2 \times (\frac{x^2}{2}-9) \times x = (x^3 - 18x)$?  
No. It is $(\frac{x^2}{2}-9)^2$ expansion? No.  
Let's just do arithmetic on coefficients.  
$x^2/2 - 9$. Square is $(A-B)^2$.  
$(A+B)^2 = A^2 + B^2 + 2AB$.  
Here $B=-9$. So $x^4/4 - 9x^2 + 81$ (with factor 2? No).  
Derivative of $x^4/4$: $x^3$.  
Derivative of $-9x^2$: $-18x$.  
Derivative of 81: 0.  
So $(\frac{x^2}{2}-9)^2 = x^4/4 - 9x^2 + 81$ is correct? No, this expression corresponds to the function value? No, it's the derivative of some squared term.  
I am getting confused between what I'm checking and what I calculated.  
Let's restart the simplification of $r(x) = x^2 + (\frac{x^2}{2}-9)^2$ using direct expansion.  
$r(x) = x^2 + \frac{x^4}{4} - 18x^2 + 81$. (This was derived from expanding $(\dots)^2$ as $(\frac{x^2}{2})^2 - 2(\frac{x^2}{2})(9) + (-9)^2 = x^4/4 - 9x^2 + 81$?  
Let's re-verify.  
$(A-B)^2$. $A=x^2/2, B=9$.  
$= (x^2/2)^2 - 2(x^2/2)(9) + 9^2 = x^4/4 - 9x^2 + 81$.  
This is a term.  
Then we have $x^2 + \dots$? No, $r(x)$ is $x^2+y^2$. So we add the first part of this expansion to itself? No.  
$r(x) = x^2 + (\text{Expansion of } y^2)$.  
So $y^2 = x^4/4 - 9x^2 + 81$.  
Then $r(x) = x^2 + \frac{x^4}{4} - 9x^2 + 81$.  
$= \frac{1}{4}x^4 - 8x^2 + 81$.  
This is what I had before.  
So critical points are $r'(x) = x^3 - 16x$.  
Set to zero: $x(x^2-16)=0$. Roots $0, \pm 4$.  
At $x=0$, value is 81.  
At $x=\pm 4$, value is $17$.  
So minimum distance squared is 17.  
But what if my expansion of $(\frac{x^2}{2}-9)^2$ is wrong?  
Let's check with specific values again.  
$x=0 \implies y=-9 \implies D^2 = 81$.  
$x=4 \implies y=-1 \implies D^2 = 17$.  
Is this the minimum?  
At $x=0$, $D^2$ is 81. At $x=\pm 4$, it's 17.  
If the function decreases then increases, minimum should be at boundary or vertex.  
But I found critical point $u=16$ (so $x=4$) giving value 17.  
Is this a minimum?  
Let's check behavior of $g(x)$ around $x=\pm 4$.  
$r''(x)$?  
If derivative is negative near $\pm 4$, then increasing.  
Since $r'(x) = x^3 - 16x$, for $x \in (-\sqrt{16}, \sqrt{16})$, say $x=0$, $r'(0)=0$.  
Derivative at $x=4$? $r'(4) = 64 - 64 = 0$.  
If $r''(x)$ is positive, then it increases.  
Let's check second derivative of $\frac{1}{4}x^4 - 8x^2 + 81$.  
$r''(x) = x^2 - 16$.  
At $x=0$, $r''(0) = -16$. (Minima would be convex).  
So the function has a local minimum.  
If $r''(x)$ is negative near $x=4$? No, for $x < 4$.  
Let's check sign of $r''(4) = 16-16 = 0$. Not well defined.  
At $x=-4$, same.  
So at $x=4$, value is 17.  
Since $x^2 - 16$ is negative for $|x|<4$, $r''(x) < 0$ implies concave down? No, $-8 < 16-16$? No.  
$r'(x) = x(x^2-16)$. For $|x| < \sqrt{16}$ (i.e., $(-4, 4)$), the first part is positive ($x>0$ and $x^2<16$), so $r'(x) > 0$.  
So function increases until $x=4$ or decreases if $r''(x) < 0$.  
But $r''(x) = x^2 - 16$.  
If $x < \sqrt{16}$ (i.e. $x<4$), then $r''(x)$ is negative? No, $x^2 < 16$ is false for all $x$.  
So $r''(x) = x^2 - 16$ depends on sign of $x$.  
If $x > \sqrt{16}$ ($x > 4$), then $r''(x)$ is positive.  
So it's convex up.  
For $0 < x < 4$, $x^2 < 16$, so $r''(x) < 0$.  
So function is concave down in $(0, 4)$.  
This means there exists a critical point (since $r'(4)=0$ and $r' \to -\infty$ as $x \to 4^+$? No, $r'(4)=0$).  
Let's check values around $x=2$.  
$r'(2) = -2(8-16) = -12$? No. $2^3 - 16(2) = 8 - 32 = -24$.  
So function is decreasing at $x=2$.  
Since it's decreasing from $x=0$ to $x=4$, the minimum must be at $x=4$.  
This implies min value is 17.  

Is it possible to go lower?  
Let's check my manual calculation of $r(u)$ derivative again.  
$f(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  
$g(x) = x^3 - 16x$. No, this is $r'(x)$.  
So critical points at $x=0$ and $\pm 4$.  
If it's decreasing then increasing? No.  
For concave down part ($0 < x < 4$): $f'(x) < 0 \implies r(x)$ decreases.  
At $x=4$, $r(x)$ has minimum slope?  
Let's check if $f''(x) = 0$. $r''(x) = -8x^2 + \dots$? No.  
$f'(x) = x^3 - 16x$.  
$f''(x) = 3x^2 - 16$.  
At $x=4$, $f''(4) = 3(16) - 16 = 48 > 0$.  
This means the function increases around $x=4$? No, that's wrong direction.  
If derivative is positive then it increases. If negative it decreases.  
At $x=4$, $r'(x)=0$. $f''(x)$ at $x=4$ is positive?  
$r''(x) = 3x^2 - 16$? No, $d/dx(x^3-16x)$ is $3x^2 - 16$.  
If $r'(x)$ has a zero, and second derivative is positive, then there must be a maximum.  
However, we found a critical point at $x=4$.  
Since it is the only critical point inside $(0, \infty)$?  
No, there is also a root at 0.  
Let's check sign of $r'(x)$ in intervals.  
$r'(x) = x^3 - 16x = x(x^2-16)$.  
If $x=0.5$, $r'(x) < 0$. (Positive term, negative quadratic).  
So decreasing for $x \in [0, 4]$.  
At $x=4$, derivative is zero.  
Is it increasing after?  
Check $r''(x)$? No.  
$r''(x)$ comes from $r'(x) = x(x^2-16)$.  
If $r''(x)$ changes sign, then critical point must be extremum or inflection.  
But we want min.  
Is $r(x)$ decreasing for $x \in (0, 4)$?  
Yes, $r'(x) < 0$ for $x \in (0, 4)$.  
At $x=4$, $r'(4)=0$.  
So it decreases until $x=4$ and then...  
Let's check value at $x=4$: $17$.  
Is it possible to go lower than 17?  
Check if I made an arithmetic error.  
$r(2) = 1^2 + (-3)^2$? No. $y = -7$?  
$x=2 \implies y = 0.5(4)-9 = -6$.  
Distance squared $D^2 = 4 + 36 = 40$.  
At $x=4$, $y=-1 \implies D^2=17$.  
So it decreased significantly as x increased from 0 to 4?  
But at $x=0, r(0)=81$. At $x=4, r(4)=17$.  
Is there a value smaller than 17 in between? No, since decreasing means minimum is approached.  
So $x^2-16$ should mean something else?  
Let me check the expansion of $(\frac{x^2}{2}-9)^2$ one more time.  
Term $A = x^2/2$.  
$x^2+(-9)^2 - 2(x^2/2)(-9)$? No, minus sign.  
$(x^2/2 - 9)^2 = x^4/4 - 9x^2 + 81$.  
Add $x^2$: $\frac{1}{4}x^4 - 8x^2 + 81$.  
This seems correct.  
But what if the problem meant something else?  
Maybe "distance between the origin and a point on the graph" means distance to origin in Euclidean metric.  
And the function is $y = \frac{1}{2}x^2 - 9$.  
Is there any chance that my derivative calculation $r'(x) = x(x^2-16)$ is wrong?  
Let's re-expand $(\frac{x^2}{2}-9)^2$ carefully.  
Term: $(\frac{x^2}{2} - 9)^2$.  
$(\frac{x^2}{2})^2 = \frac{x^4}{4}$. Correct.  
Cross term: $2(\frac{x^2}{2})(-9) = -9x^2$? No, $-\frac{36}{2}x^2 = -18x^2$?  
Let's multiply: $\frac{1}{2} \times 9 = 9/2$. $2 \times \frac{1}{2} x^2 \times (-9) = \dots$?  
Let's check: $2 \cdot (\frac{x^2}{2}) \cdot 9 = 9x^2$. No, there is a minus sign.  
So $-9x^2$.  
The term $(-9)^2 = 81$.  
Sum of coefficients for $x^4$, $x^2$, constant.  
$x^4$ coefficient 1/4.  
$x^2$ coefficient: From $(\frac{x^2}{2})^2$ we have 0? No, we are squaring the term.  
So $\dots - 9(x^2) \dots$.  
This gives $-9x^2$.  
So total coeff of $x^4$ is $1/4$. Coeff of $x^2$ is $-9 + 1 = -8$. Correct.  
Constant term is 81.  
So derivative $\frac{d}{dx} (\dots) = x^3 - 16x$.  
This gives critical points at $0, \pm 4$.  
So minimum distance is indeed $\sqrt{17}$.  

Is it possible that I made a mistake in calculating the value of function at $x=\sqrt{5/2}$?  
At $x^2=5/2$, $y = (5/4 - 36)/4 = (-31/4)^2$? No.  
$y = \frac{1}{2}(\frac{5}{2}) - 9 = \frac{5}{4} - \frac{36}{4} = -\frac{31}{4}$.  
Distance squared $x^2 + y^2 = \frac{5}{2} + (-\frac{31}{4})^2 = \frac{10}{8} + \frac{961}{16}$? No, $\frac{5}{2} = 20/8$.  
So $D^2 = \frac{20}{8} + \frac{961}{16} = \frac{40+961}{16} = \frac{1001}{16}$.  
$1001 > 17$. So $\sqrt{5/2}$ is not the minimum.  
So my calculation of derivative $r'(x) = x^3 - 16x$ yielding $u=16$ (corresponding to $x=4$) is consistent with the value being lower than at $u=0$.  
Is there any other critical point? No.  
The minimum is at $u=16 \implies x=\pm 4 \implies y=-1$.  
Min distance squared is 17.  

Let me check if $y^2$ has the term $\frac{9}{2}x^2$ or something.  
$(\frac{x^2}{2}-9)^2 = (\frac{x^2}{2})^2 - 2 \cdot \frac{x^2}{2} \cdot (-9) + (-9)^2$? No, minus sign is there.  
$(x^2/2)^2 - (2(x^2/2)(-9)?)$ No, it's $2(\dots)(9)$.  
Is the term $(\frac{x^2}{2} - 9)$ squared expansion correct?  
Yes, binomial expansion.  
So my calculation seems robust.  

But let me think. What if there is a typo in my understanding of the question or problem statement?  
"distance between the origin and a point on the graph".  
Is it possible that I am minimizing over complex points? No.  
The distance is $\sqrt{x^2+y^2}$.  
The result seems to be $17$.  
Let's check if any other critical point was missed.  
$D(x) = \sqrt{x^2 + (\frac{1}{2}x^2 - 9)^2}$.  
This function is continuous.  
Is it possible that the derivative has no roots?  
$r'(x) = x^3 - 16x$. No, it has roots.  
However, I should check $r''(x)$ for minimum.  
We want to know if $r(x)$ has a local minimum at these points.  
At $x=\pm 4$, $r' = 0$.  
$r''(x) = 3x^2 - 16$ (calculated from derivative of $r'(x)$).  
$r''(4) = 3(16) - 16 = 48 > 0$.  
So $x=4$ is a local minimum.  
Since this is the only critical point and it's the global one for $u \in [0, \infty)$ (or real domain), the answer should be 17.  

Let me verify the value at another point just to be absolutely sure.  
$x = 2$. $y = 8-9=-7$? No. $\frac{4}{2} - 9 = 2-9 = -7$.  
So distance squared $= 2^2 + (-7)^2 = 4+49 = 53$.  
$x = 1$. $y = 0.5-9 = -8.5$. Distance $1 + 72.25 = 73.25 > 17$.  
$u=1$ gave $D^2 = 53$.  
$r(u)$ decreases from 81 at $u=0$ to 17 at $u=4$.  
So the minimum is indeed 17.  

The problem asks for "smallest distance", so distance squared $a^2$.  
My calculation gave $r^2 = 17$.  
So $a^2 = 17$.  
Is there any reason to doubt?  
Let me double check if $x^2=5/2$ is a root of something.  
At $u=5/2$, $D^2 = \frac{1001}{16} \approx 62.56$.  
$81 - 62.56 = 18.44 > 0$. So this is not min.  
At $u=0$, $D^2=81$.  
So $x^2=16$ is indeed the local minimum of the function $\frac{1}{4}u^2 - 8u + 81$? No, that's a quadratic in $x^2$ with vertex at $u=16$.  
The minimum of $r(x)$ (distance) is at $x^2=16$ which implies $D^2 = \frac{256}{4} - 128 + 81$? No.  
$r(u) = \frac{1}{4}u^2 - 8u + 81$.  
Vertex is at $u=-b/2a = 8 / (2*1/4) = 16$.  
Value at vertex: $\frac{1}{4}(16)^2 - 8(16) + 81 = 64 - 128 + 81 = 17$.  
This assumes that my derivative $x^3-16x$ yields the same critical point.  
And it does. So min value is 17.  

There's a potential pitfall: domain of $x$. The function is defined for all real $x$.  
Is there any constraint I missed?  
Maybe the graph refers to something else? No, standard definition.  
Maybe the "distance" is minimal distance from origin to curve?  
Yes.  
So answer is 17.  

Let's check if there are any other critical points.  
$r''(u) = u-8$? No, we found $r'(u)$ derivative wrt $u$.  
My expression for $r(x)$ was $D^2(u) = \frac{1}{4}u^2 - 8u + 81$.  
Let's check $r''(x)$ wrt $u$?  
No, just checking if it's concave.  
If min is at vertex, it is a minimum.  
But what about endpoints?  
Domain of $u=x^2 \in [0, \infty)$.  
Endpoints: $u=0 \implies x=0$, $D^2=81$. $u=\infty \implies$ function $\to \infty$.  
So minimum is interior.  
Thus min value 17.  

Let me do a sanity check on the expansion of $(\frac{x^2}{2}-9)^2$.  
Is it possible I made an arithmetic error in binomial?  
$(x/2 - 9)^2 = x^2/4 - 2(x/2)(9) + 81$. No, $x^2/4$? No, $(x/2)^2 = x^2/4$.  
The term was $\frac{x^2}{2} - 9$.  
Square is $(\frac{1}{2}x^2 - 9)$.  
Square of $(A+B)$ where $A = x^2/2, B=9$? No.  
$(\frac{x^2}{2} - 9)$. Let's treat this as $X-Y$ where $X=x^2/2, Y=9$.  
Then $(X-Y)^2 = X^2 + Y^2 - 2XY$? Yes.  
So terms are $x^4/4 + 81 - 9x^2$? No.  
Let's re-calculate cross term: $-2(X)(Y)$.  
Here $Y=9$. So $-2(\frac{x^2}{2})(9) = -9x^2$?  
Yes.  
So term is $-9x^2$.  
Is it possible that I missed the constant $+81$? Yes.  
So the expression for $(\dots)^2$ is $\frac{1}{4}x^4 - 9x^2 + 81$.  
Adding $x^2$: $\frac{1}{4}x^4 - 8x^2 + 81$.  
This seems solid.  

What about the point $(0,-9)$? $D^2=81$.  
What about point $(\pm \sqrt{16}, -1) = (\pm 4, -1)$?  
$y=-1$, $x=4$. $x^2+y^2 = 17$.  
Is this the smallest distance?  
If we consider other points.  
Suppose we move closer to origin.  
$x^2 + y^2$.  
Since we can go as small as we like by choosing large negative $y$ relative to $x$, but here we have constraint $y = x^2/2 - 9$.  
If $x$ is very large, $y$ is large positive.  
If $x=0$, $y=-9$. $D^2=81$.  
Can we get $D^2 < 17$?  
Let's try small $x$ near 0. $y \approx -9$.  
$y = \frac{1}{2}x^2 - 9 \implies y^2 \approx 81 - 9x^2 + x^4/4$.  
So $D^2 \approx x^2 + 81 - 9x^2$.  

*Continued in [part 4 of 5](algebra_1143_p4.md): GitHub stops rendering math on pages this long, so the transcript is split.*
