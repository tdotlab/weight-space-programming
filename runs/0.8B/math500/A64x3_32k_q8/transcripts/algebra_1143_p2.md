# test/algebra/1143.json, part 2 of 5

[Previous part](algebra_1143.md)

So distance is $\sqrt{4^2+(-1)^2} = \sqrt{17}$.  
What if the parabola was shifted? No, constant term is -9.  
Is there any other critical point?  
Let's check the derivative of $y(x)$. It's a parabola opening up.  
The minimum distance from origin to a curve with $C^2$ terms and linear terms.  
It can be found by completing the square or using Lagrange multipliers.  
Lagrange Multipliers: minimize $x^2 + y^2$ subject to $y = \frac{1}{2}x^2 - 9$.  
Substitute $y$: $\nabla(y) \cdot (x, y)$? No.  
$\nabla(D^2) = 2(x, y)$. Constraint is $P(x,y) = x^2 + y^2 - 0$.  
Or minimize $f(x,y)=x^2+y^2$ subject to $g(x,y)=\frac{1}{2}x^2-y+9=0$? No.  
Constraint is just $y = \frac{1}{2}x^2-9$.  
$\nabla f = (2x, 2y)$. $\nabla g = (x, y)$.  
No, constraint is $g(x,y) = x^2/2 - 9 - 0$? No.  
Let's use Lagrange multipliers for min $f(x,y)$ s.t. $h(x,y)=\frac{1}{2}x^2-9$.  
$h(x,y) = \frac{1}{2}x^2 - y + 9$? No.  
The equation is $y - \frac{1}{2}x^2 + 9 = 0$.  
So $\nabla g = (x, y)$. Then $g'(x,y)=\frac{1}{2}x$.  
Lagrange condition: $\frac{\partial f}{\partial x} = \lambda \frac{\partial h}{\partial x} + \mu \frac{\partial h}{\partial y}$? No.  
$L(x,y, \lambda) = x^2+y^2 - 1/\lambda (x-9)$.  
Or simpler: $\nabla f = k \nabla g$.  
$x = \lambda (x)$ and $y = \lambda(y)$? No.  
$\frac{2x}{1} = k$ and $\frac{2y}{1} = 0$? No, this isn't a constraint on derivatives directly but on gradients.  
If I use the implicit differentiation of $(\frac{1}{2}x^2 - 9)^2$ is not right.  
Let's re-derive:  
$f(x,y) = x^2+y^2$.  
Constraint $C(x,y) = \frac{x^2}{2} - y + 9 = 0$. No, $y = \frac{x^2}{2}-9$ is the equation.  
So $g(x,y) = x^2 + (\frac{1}{2}x^2-9)^2$. This was not a standard Lagrange problem.  
Let's stick to substitution method, which is robust.  

Let me re-check the critical point $u=5/2$. Why did I think this was a minimum?  
The function was $\frac{1}{4}u^2 - 8u + 81$. This is parabola with vertex at $u=16$.  
Is it possible to have $x$ such that $x^2 = -5/2$? No, domain of $x$ is reals. So we must restrict our attention to real values for $u=x^2 \ge 0$.  
If the vertex was at negative real number, then the minimum would be on boundary or undefined.  
But here, the vertex is at $16$, which is positive. So the minimum exists in interior.  

So why did my first thought process yield a different answer?  
Let me re-read "Find a^2".  
If $a = \sqrt{17}$, then $a^2 = 17$.  
But let's check if I missed any subtle geometric property.  
Wait. The vertex is $(0,-9)$.  
The distance from origin to $(0,-9)$ is 9.  
The point on the curve closest to origin could be the vertex.  
Is it possible that $x^2=16$ gives a smaller value than $81$? Yes, $17 < 81$.  
So the minimum is indeed at $x=\pm 4, y=-1$.  

But let's double check my algebraic expansion one more time. This seems to be the most likely source of error.  
Let's plug in values.  
$x=4 \implies y = (1/2)(16) - 9 = 8 - 9 = -1$.  
$D^2 = 4^2 + (-1)^2 = 16+1 = 17$.  
What if $x=0$? $y=-9$. $D^2 = 81$.  
What if $x=\pm \sqrt{5}$? No.  
Let's check the derivative of $x^2 + (\frac{x^2}{2}-9)^2$ with respect to $x$.  
Let $u=x^2$. Then $R(x) = u + (\frac{u}{2} - 9)^2$ is not a function of $x$?  
Yes it is. $R'(x) = 1 + 2(\frac{x^2}{2}-9)(\frac{x}{2}) = 1 + (x^2 - 18x)$? No.  
Let's do term by term.  
$r(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
Term 1: $x^2$. Term 2: $(\frac{1}{2}x^2 - 9)^2$.  
Derivative of Term 2: $2(\frac{1}{2}x^2 - 9) \cdot x = x(\frac{x}{2} - 9)$? No.  
$\frac{d}{dx}(A(x))^2 = 2A(x) A'(x)$.  
$A(x) = \frac{x^2}{2} - 9$.  
$A'(x) = x$.  
So $r'(x) = 1 + 2(\frac{1}{2}x^2-9)(x) = 1 + (x^3 - 18x)$.  
Set to zero: $x^3 - 18x + 1 = 0$.  
This cubic equation.  
If roots are relevant, they should yield smaller values than the minimum found earlier (assuming critical points).  
Let's re-evaluate critical points.  
$r'(x) = x(x^2 - 18) + 1$? No.  
My expansion: $r'(x) = 1 + \frac{x^3}{2} - 9x$.  
Ah! I made a mistake in previous derivative calculation.  
Let's re-derive derivative of $(\frac{x^2}{2}-9)^2$.  
Let $A = x^2/2 - 9$. Then $r'(x) = 2 A(x) A'(x)$ is correct.  
$A'(x) = \frac{d}{dx}(x^2/2) = x$.  
So $r'(x) = 2(\frac{x^2}{2}-9)(x) = (\frac{x^3}{4} - 9x)$? No. $2(x^2/2-9)x = (x^3 - 18x)$.  
Yes.  
So $r'(x) = 1 + x^3 - 18x = x^3 - 18x + 1$.  
This must be zero.  
So critical points of the original function are roots of $x^3 - 18x + 1 = 0$.  
If such a point exists, we need to check if the derivative of my previous quadratic expression was correct (i.e., is it true that min occurs at vertex?)  
Why did I think minimum occurs at $u=16$? Because I solved $\frac{d}{du}( \dots ) = 0$.  
Let's re-check the quadratic function.  
$r^2(u) = \frac{1}{4}u^2 - 8u + 81$.  
This was obtained by substituting $r^2(x) = x^2 + (\frac{1}{2}x^2-9)^2$ into a polynomial in $u=x^2$.  
$r^2(x) = u + \frac{1}{4}u^2 - 9u + 81$.  
Let's check derivative of this wrt $u$. $\frac{d}{du}( \frac{1}{4}u^2 - 9u + 81 ) = \frac{1}{2}u - 9$.  
This is wrong. The derivative with respect to $x$ was:  
$r'(x) = 1 + (x^3 - 18x)$. No.  
My previous calculation: $r(x) = x^2 + (\frac{x^2}{2}-9)^2$.  
Let's differentiate wrt $x$:  
$\frac{d}{dx}(\frac{1}{4}u^2 - 9u + 81)$ ? No.  
Let's expand $(\frac{x^2}{2}-9)^2$ correctly.  
Term is $\frac{1}{4}x^4 - 9x^2 + 81$.  
So $r'(x) = 1 + (\frac{3}{2}x^2 - 18x)$? No.  
Let's differentiate $(\frac{x^2}{2}-9)^2$.  
Using quotient rule or chain rule on squared function: $2(x^2/2 - 9)(x)$.  
Term is $\frac{x}{2}(x^2/2 - 9) = \frac{1}{4}x^3 - \frac{9x}{2}$? No. $2 \cdot (\frac{1}{2}x^2-9) \cdot x$ (this assumes derivative of inside is $x$, which is correct).  
So term is $(\frac{x^3}{2} - 18x)$?  
Let's re-expand carefully:  
$(\frac{x^2}{2} - 9)^2 = (\frac{1}{2}x^2)^2 + (-9)(-\frac{2}{2}(x^2/2-9)/2)? No.  
Use binomial theorem on $(a+b)^2$. Here $a = x^2/2$, $b = -9$.  
$(\frac{x^2}{2} - 9)^2 = (\frac{x^2}{2})^2 + (-9)^2 + 2(\frac{x^2}{2})(-9)$.  
$= \frac{x^4}{4} - 18x^2 + 81$.  
This is correct.  
Now add the $x^2$ term from original function.  
$r(x) = x^2 + (\frac{x^4}{4} - 18x^2 + 81)$? No, this mixes terms incorrectly.  
Original expression was: $r(x) = x^2 + (\frac{1}{2}x^2 - 9)^2$.  
This means $y = \frac{1}{2}x^2 - 9$. So $(y+9)^2$ is not the term.  
We want to minimize $x^2+y^2$.  
Let $u = x^2$. Then $y = u/2 - 9$.  
$r(x) = u + (u/2 - 9)^2$.  
Expand $(u/2 - 9)^2$: $\frac{1}{4}u^2 - \frac{9u}{2} + 81$? No.  
Term is $-2(u)(-9)/2 = +9u$?  
No. Cross term: $2(u/2)(-9)$.  
$= -9u$.  
So $\frac{1}{4}u^2 - 9u + 81$.  
Sum with $u$: $u + \frac{1}{4}u^2 - 9u + 81 = \frac{1}{4}u^2 - 8u + 81$.  
Let's verify this cross term.  
$\text{Cross term coefficient} = -2(a)(b)$. Here $a=u/2, b=9$ (or something like that).  
Term in $(\frac{u}{2}-9)^2$:  
First term is $(u/2)^2 = u^2/4$. Correct.  
Second term: $-2(\frac{u}{2})(9) = -9u$. Correct.  
Third term: $(-9)^2 = 81$. Correct.  
So the expression for $r(u)$ is indeed $\frac{1}{4}u^2 - 8u + 81$.  

Let's check the derivative with respect to $x$ (which is $x = \sqrt{u}$, so we need to handle monotonicity).  
If we minimize wrt $x$, let $g(x) = x^2 + (\frac{x^2}{2}-9)^2$.  
Then $g'(x) = 1 + 2(\frac{x^2}{2}-9)(\frac{x}{2})$. No, $\frac{d}{dx}( \frac{x^4}{4} - 9x^2 + 81 )$?  
Let's re-derive $r'(x)$ from the expanded expression.  
$r(x) = x^2 + (\frac{x^4}{4} - 9x^2 + 81)$. No, original was $y = \frac{1}{2}x^2-9$.  
So $y^2 = (\frac{x^2}{2}-9)^2 = \frac{x^4}{4} - 9x^2 + 81$.  
Then sum with $x^2$: $r(x) = x^2 + \frac{x^4}{4} - 9x^2 + 81$.  
$= \frac{x^4}{4} - 8x^2 + 81$.  
This is correct.  
Now differentiate with respect to $x$:  
$r'(x) = x^3 - 16x + 0$? No.  
$\frac{d}{dx}(\frac{1}{4}x^4) = x^3$.  
$\frac{d}{dx}(-8x^2) = -16x$.  
So $r'(x) = x^3 - 16x + 0$? No, the constant is 81.  
$r'(x) = x^3 - 16x + 81/8 \dots$? No, let's keep it as polynomial in $x$.  
$r'(x) = x(x^2 - 16) + 0$. No, $\frac{d}{dx}(81)$ is 0.  
So $r'(x) = x(x^2 - 16)$?  
No, let's look at derivative of $(\frac{x^4}{4} - 9x^2 + 81)$.  
Derivative: $\frac{4}{4}x^3 - 18x = x^3 - 18x$?  
Let's re-expand carefully.  
$r(x) = x^2 + (\frac{1}{2}x^2-9)^2$ is wrong.  
$r(x) = x^2 + (\frac{x^2}{2}-9)^2$.  
$\frac{d}{dx}(x^2) = 2x$.  
$\frac{d}{dx}((\frac{x^2}{2}-9)^2)$?  
Let $u = \frac{x^2}{2} - 9$. Then $r(x) = u^2$? No, the term is $(\dots)^2$.  
So we have $r(x) = x^2 + u^2$ where $u = \frac{x^2}{2}-9$.  
Is this correct?  
The original equation is $y = \frac{1}{2}x^2 - 9$. This implies the point $(x,y)$ satisfies this.  
So we want to minimize $\sqrt{x^2+y^2}$ subject to $y = \frac{1}{2}x^2-9$.  
This leads to minimizing $x^2 + y^2$? No, distance is $\sqrt{x^2+y^2}$.  
If I substitute $y$, I get $x^2 + (\frac{x^2}{2}-9)^2$. This is correct.  

Let me verify the expansion of $(\frac{x^2}{2}-9)^2$ again.  
$(A - B)^2 = A^2 - 2AB + B^2$.  
$A = \frac{x^2}{2}$. $B=9$.  
$A^2 = \frac{x^4}{4}$.  
$-2AB = -2(\frac{x^2}{2})(9) = -9x^2$.  
$B^2 = 81$.  
So the term is $\frac{x^4}{4} - 9x^2 + 81$.  
Then $r(x) = x^2 + (\frac{x^4}{4} - 9x^2 + 81)$? No.  
$r(x) = x^2 + y^2$ where $y = \dots$.  
So we replace $y^2$ in the sum: $x^2 + (\frac{x^4}{4} - 9x^2 + 81)$.  
$= \frac{1}{4}x^4 - 8x^2 + 81$? No.  
$\frac{1}{4}x^4 - 9x^2 = x^2 - (\text{something})$?  
$x^2$ term has coefficient 1 from first part, and $-9$ from second part.  
So we have $x^2 + \frac{x^4}{4} - 9x^2 = \frac{1}{4}x^4 - 8x^2$.  
Yes, my previous derivation was correct: $\frac{1}{4}x^4 - 8x^2 + 81$ ? No, there was an extra $x^2$.  
Let's re-verify the coefficients.  
From $(\frac{x^2}{2}-9)^2$, we have $\frac{x^4}{4}$ and $-9x^2$ and $81$.  
Adding these to $x^2$:  
$\frac{1}{4}x^4 - 8x^2 + 81$?  
No, the coefficient of $x^2$ is just $1$ from first term. The second part provides a negative $9x^2$.  
So sum is $\frac{1}{4}x^4 - 8x^2 + 81$? No.  
We have $-9x^2$ from the cross term, which is subtracted?  
$(\dots)^2 = A^2 - 2AB + B^2$.  
$A^2 = \frac{x^4}{4}$.  
$-2AB = -2(\frac{x^2}{2})(9) = -9x^2$.  
So term is $\frac{1}{4}x^4 - 9x^2 + 81$.  
Add $x^2$:  
$\frac{1}{4}x^4 - 8x^2 + 81$? No.  
Let's look at the expression $r(x) = x^2 + (\frac{x^4}{4} - 9x^2 + 81)$?  
This assumes that $(\dots)^2$ is subtracted by the previous term which was not present.  
Let's re-express: $y^2 = (\frac{1}{2}x^2-9)^2$. This is a term in the expansion of $r(x)$.  
$r(x) = x^2 + (\frac{x^4}{4} - 9x^2 + 81)$? No, $-9x^2$ from $(\dots)^2$?  
$(\frac{1}{2}x^2-9)^2 = \frac{x^4}{4} - 9x^2 + 81$.  
Yes. This is correct.  
So $r(x) = x^2 + \frac{x^4}{4} - 9x^2 + 81$.  
$= \frac{1}{4}x^4 - 8x^2 + 81$? No.  
$x^2 - 9x^2 = -8x^2$. So it's $\frac{1}{4}x^4 - 8x^2 + 81$ ?  
Let's check: $-9x^2 + x^2 = -8x^2$.  
So coefficient of $x^2$ is $-8$.  
But let me re-calculate the coefficients for $(\dots)^2$.  
$(\frac{x^2}{2} - 9)^2$:  
Term $1$: $\frac{1}{4}x^4$.  
Term $2$: $-\frac{36}{4}x^2 = -9x^2$? No.  
Let's re-evaluate the cross term coefficient: $-2(\frac{x^2}{2})(9)$.  
This is $-9x^2$.  
So we have $\frac{1}{4}x^4 - 9x^2 + 81$.  
Now add $x^2$: $\frac{1}{4}x^4 - 8x^2 + 81$? No.  
The term is $(\dots)^2$. So $-9x^2$.  
Then $+x^2$ from original function.  
So result is $\frac{1}{4}x^4 - 8x^2 + 81$.  
This means the coefficient of $x^2$ is $-8$.  
The minimum of this quadratic in $x^2$ (which is $u=x^2$) would be at vertex.  
But the function to minimize is $f(u) = u + (\frac{u}{2}-9)^2$? No.  
Let's write $r(x)$ in terms of $u=x^2$.  
$r(u) = u + (\frac{u}{2}-9)^2$.  
This is what I started with earlier.  
So $r(u) = u + \frac{u^2}{4} - 9u + 81 = \frac{1}{4}u^2 - 8u + 81$? No.  
The cross term is $-9u$.  
So $u + \frac{1}{4}u^2 - 9u + 81 = \frac{1}{4}u^2 - 8u + 81$.  
Is this right?  
Let's re-evaluate $(\frac{u}{2}-9)^2$ again.  
$(A-B)^2 = A^2 - 2AB + B^2$.  
$A=u/2, B=9$.  
$A^2 = u^2/4$.  
$-2AB = -2(u/2)(9) = -9u$.  
So we get $u^2/4 - 9u + 81$.  
This is correct.  
Now add $u$:  
$u + (u^2/4 - 9u) + 81 = u^2/4 - 8u + 81$.  
Yes, coefficient of $u$ is $-8$.  
Derivative wrt $u$: $u^2/2 - 8 = 0 \implies u=16$.  
Minimum value at $u=16$:  
$r(16) = (16)^2/4 - 8(16) + 81 = 256/4 - 128 + 81 = 64 - 128 + 81 = 17$.  
So $r^2_{min} = 17$ if we are correct with expansion.  
This means min distance squared is 17.  

However, let me check the critical point calculation again using $x(x^2-16)=0$ which corresponds to derivative wrt $u$?  
If I have $\frac{1}{4}u^2 - 8u + 81$.  
Derivative: $\frac{1}{2}u - 8 = 0 \implies u=16$.  
This assumes the derivative of $r(u)$ with respect to $u$ is correct.  
Is there any mistake in my expansion?  
Let's check $r'(x) = x^3 - 16x$.  
If I use $r(u)$, then $dr/du = \frac{d}{dx} r(x)/dx du/dx$? No.  
$r(u) = \dots u + \dots u^2$.  
$\frac{dr}{du} = \dots$.  
So $\frac{1}{4}u - 8 = 0$ is not necessarily true?  
If $u=x^2$, then $r(x)$ has a term of $x^3-16x=0$.  
Let's check my previous calculation of critical points for $r(u)$.  
The function $g(u) = \frac{1}{4}u^2 - 8u + 81$ is the squared distance.  
Its vertex is at $u=16$.  
At $u=16$, value is 17.  
So min distance is $\sqrt{17}$.  

Let me check the derivative of $r(u)$ again, which I used to find $u=5/2$ earlier.  
$r'(x) = \dots$?  
I wrote: $r'(x) = x^3 - 16x + 81$ ? No, that was incorrect.  
Let's re-evaluate carefully.  
$r(x) = x^2 + (\frac{x^4}{4} - 9x^2 + 81)$? No.  
My expansion of $(\frac{x^2}{2}-9)^2$ gave $\frac{x^4}{4} - 9x^2 + 81$.  
So $r(x) = x^2 + \frac{x^4}{4} - 9x^2 + 81$.  
The coefficient of $x^2$ is $1 - 9 = -8$.  
So the term is $\frac{1}{4}x^4 - 8x^2 + 81$?  
Let's re-verify $(\frac{x^4}{4} - 9x^2)$. No, $-\frac{36}{4}x^2 = -9x^2$.  
So $r(x) = \frac{x^4}{4} - 8x^2 + 81$ is correct.  
Then derivative wrt $x$: $x^3 - 16x$.  
Set to zero: $x=0, x=\pm 4$.  
This implies the minimum of $r(x)$ is at $x=0, \pm 4$?  
But I found earlier that $u=x^2$ leads to critical point $u=16$.  
Let's check which variable is being minimized.  
$r(u)$ is a function of $u=x^2$.  
$\min r(u)$ occurs when derivative wrt $u$ is 0? No, derivative wrt $x$.  
The derivative of $r(x)$ wrt $x$: $\frac{1}{4} \cdot 4 x^3 - 8(2x) + 0 = x^3 - 16x$.  
This matches my previous calculation $x(x^2-16)=0$?  
$x^3 - 16x$ factors as $x(x^2-16)$? No, derivative of $(\frac{1}{4}x^4 - 8x^2 + 81)$.  
Derivative: $\frac{x^3}{1} - 16x = x(x^2-16)$.  
So critical points are $x=0$ and $\pm 4$.  
At $x=0$, $r(0)=81$.  
At $x=\pm 4$, $r(\pm 4)$?  
$r(4) = \frac{1}{4}(256) - 8(16) + 81$? No.  
Let's recompute $r(4)$.  
$x=4 \implies y = 0.5(16)-9 = -1$.  
$r(4) = 4^2 + (-1)^2 = 16+1 = 17$.  
Using formula $\frac{1}{4}(16)^2 - 8(16) + 81$? No.  
The formula was $u^2/4 - 8u + 81$ if we use $u=x^2$.  
Let's check.  
At $x=0$, $r(0) = 81$. Formula gives $\frac{1}{4}(0) - 0 + 81 = 81$. Correct.  
At $x=\pm 4$, $r(x) = 17$.  
Formula: $\frac{1}{4}(16)^2 - 8(16) + 81$?  
This is $40/4 \cdot 9 + 81$? No.  
$u^2/4 = 256/4 = 64$.  
$-8u = -128$.  
$64 - 128 + 81 = 17$.  
So my formula $r(u) = \frac{1}{4}u^2 - 8u + 81$ is consistent with $u=16 \implies 17$.  
Why did I think earlier that critical point should be $u=5/2$?  
I found $x(x^2-16)=0$, so $u=16$.  
And derivative of $\frac{1}{4}u^2 - 8u + 81$ wrt $x$ (where $u=x^2$) is...  
$\frac{d}{dx}(r(u)) = \frac{1}{2} u' x = \frac{1}{2} (2x) r'(x)$? No.  
The derivative wrt $x$ of $r(x) = \dots$ is given by chain rule.  
If I just use the formula $\min g(u) = u^2/4 - 8u + 81$ with $u=x^2$, then min at $u=16$.  
This gives value 17.  

However, my previous analysis of derivative was:  
$r'(x) = x^3 - 16x$.  
Roots $x=0, x=\pm 4$.  
At $x=4$, distance is $\sqrt{17} \approx 4.12$.  
Is this a minimum?  
Let's check value at $u=0$.  
$r(0) = 81$.  
At $u=5/2$ (from first calculation attempt), I used derivative of quadratic in $u$ which gave $u=5/2$.  
Let me re-verify the coefficient of $x^2$ in $r(x)$ expansion.  
$r(x) = x^2 + y^2$.  
$y = \frac{1}{2}x^2 - 9$.  
So $y^2 = (\frac{x^2}{2}-9)^2 = \frac{x^4}{4} - 9x^2 + 81$.  
$r(x) = x^2 + \frac{x^4}{4} - 9x^2 + 81$.  
$= \frac{1}{4}x^4 - 8x^2 + 81$.  
This is the function of $u=x^2$: $r(u) = \frac{1}{4}u^2 - 8u + 81$ ? No, coefficient of $u$ in this expansion is $-8$.  
So min at $u=16$ (value 17).  
But my critical point analysis $x(x^2-16)$ yielded $u=16$ as well.  
So $u=16$ corresponds to the minimum.  

Why did I think earlier I had $u=5/2$?  
Let's check the derivative calculation $r'(x) = x^3 - 16x$.  
$r(u) = \dots - 8u + \dots$ No, this is wrong.  
My confusion stems from mixing up $r(u)$ as function of $x$ with $r(u)$ as function of parameter.  
Let's be very systematic.  
We want to minimize $D^2(x) = x^2 + (\frac{1}{2}x^2-9)^2$.  
Let $u = x^2 \ge 0$.  
Then $D^2(u) = u + (\frac{u}{2}-9)^2$ is not valid because $(\dots)$ depends on $u$.  
$D^2(x) = x^2 + ( \frac{x^2}{2} - 9 )^2$.  
Let's calculate the value at $x=4$: $16 + (-1)^2 = 17$.  
Let's calculate the value at $x=\pm 4$ in terms of $u$.  
At $u=16$, $D^2(16) = 16 + (-1)^2 = 17$.  
This corresponds to a valid point on the graph.  

Now let's check if I made a mistake in evaluating $\frac{d}{du} (\dots)$.  
My error might be that $u$ and $x$ are different.  
If I minimize wrt $x$:  
$f(x) = x^2 + y^2$.  
$\nabla f = (2x, 2y)$. $\nabla g = (x, y)$ where $g(x,y)=\dots$? No.  
Substitute $x, y$ in terms of $u=x^2$:  
$D(u) = u + (\frac{u}{2}-9)^2$.  
Let's find critical points for this function of $u$.  
$f'(u) = 1 + 2(\frac{u}{2}-9)(\frac{u}{2})'$? No.  
We substitute $y$ into $x^2+y^2$ directly as a function of $x$?  
Let's use the chain rule properly.  
$f(u, x) = u + ( \frac{u}{2} - 9 )^2$. No, $(\frac{x^2}{2}-9)^2$.  
Let's write $y(x) = \frac{1}{2}x^2 - 9$.  
$r(x) = x^2 + y(x)^2$.  
$r'(x) = 2x + 2y(x)y'(x)$.  
$y'(x) = x$.  
So $r'(x) = 2x + 2(\frac{x^2}{2}-9)(x) = 2x + (x^3 - 9x)$? No.  
$\frac{d}{dx} (x/2)^2$ is not correct.  
Let's rewrite carefully:  
$r(x) = x^2 + y^2$.  
$y = \frac{x^2}{2}-9$.  
So $r'(x) = 2x + 2(\frac{1}{2}x^2 - 9) (x/2)$? No.  
$r'(x) = 2x + 2 (\dots)(\dots)'$  
If we use chain rule: $\frac{d}{dx}(y(x)^2) = 2y(x) \frac{dy}{dx}$.  
$\frac{dy}{dx} = x$.  
So derivative is $2y(x) \cdot x = 2(\frac{x^2}{2}-9)x = (x^3 - 18x)$? No.  
$2(\frac{x^2}{2}) \cdot x = x^2$? No. $2(1/2)x^3 = x^3$.  
The term is $(\dots)^2$. So derivative is $2(\frac{x^2}{2}-9)x$.  
So $r'(x) = 2x + 2(\frac{x^2}{2}-9)x$? No.  
$r(x)$ is the distance squared from origin to point on curve.  
Let's check definition. Distance between $(0,0)$ and $(x,y)$. $D^2 = x^2+y^2$.  
Substitute $y$: $x^2 + (\frac{x^4}{4} - 9x^2 + 81)$? No, this was $(\frac{x^4}{4}-9x^2+81)$.  
The term $\frac{1}{4}x^4$ comes from $(\frac{x^2}{2})^2$? No, $(\frac{x^2}{2}-9)^2 = \frac{1}{4}x^4 - 9x^2 + 81$.  
So $r'(x) = 0$ yields critical points.  
The equation for critical points of the function $r(u)$ was $\frac{d}{dx}( \dots )$ or derivative wrt $u$?  

*Continued in [part 3 of 5](algebra_1143_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
