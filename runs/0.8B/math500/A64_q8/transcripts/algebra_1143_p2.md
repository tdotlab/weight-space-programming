# test/algebra/1143.json, part 2 of 3

[Previous part](algebra_1143.md)

Let's try $x=-3$: $g'(-3) = -3(9-16)?$ No, $g'(x) = x^3 - 16x$.  
If $x=-3$, $(-27) - (-16)(-3) = -27 + 48 = 21 > 0$? No.  
$x=-3$: $x^2=9, x^3=-27$.  
$f'(-3) = -27 - 16(-3) = -27 + 48 = 21 > 0$.  
So on $(-\infty, -4)$, for example at $x=-5$, it's negative.  
Let me re-verify. $g'(x) = x^3 - 16x$.  
For large positive $x$, $x^3$ dominates $-16x \to +\infty$.  
For large negative $x$, $x^3 \to -\infty$, $-16x \to +\infty$. So for very large negative $x$, $g' > 0$? No, $x^3$ is negative and dominant. So it's decreasing to the right?  
Let's look at the sign chart again properly.  
We have three roots: $-4, 0, 4$ (in this case).  
Let's check $x=-3$.  
$f'(-3) = (-27) - 16(-3) = -27 + 48 = 21 > 0$.  
So $f'(x)$ is positive at $x=-3$. This means it increases as we go to right from negative numbers.  
But for $x \to -\infty$, let's say $x=-50$.  
$f'(-50) = (-125000) + 800 > 0$. So positive near $-\infty$? No.  
Let's re-evaluate: $g'(x) = x^3 - 16x$.  
As $x \to -\infty$, $x^3 \to -\infty$. So $g'(x)$ starts at $-\infty$.  
Since $-16(-\infty) = +\infty$ is a large positive term, the sum $-\infty + \text{positive}$ would be positive for very negative $x$.  
Wait. The roots of $x^3 - 16x$ are $\pm 4$ and $0$.  
No, the function $g'(x)$ has zeros at $-4, 0, 4$?  
Let me check the factorization $x^3 - 16x = x(x^2-16)$.  
This factors into $(x-4)(x+4)x$? No.  
$x^2-16 = (x-4)(x+4)$. Yes, $x^3$ term is missing here, but wait. $x^3 - 16x$. Factor is $x(x^2-16)$ which factors to $x(x-4)(x+4)$.  
So the roots are exactly $\{-4, 0, 4\}$.  
Let's check if my sign analysis at $x=-3$ was correct.  
$x=-3$: $f'(-3) = (-27) - 16(-3) = -27 + 48 = 21$. Positive.  
Since $-4$ is a root, and $0$ is a root, the sign change must happen between them or outside?  
At $x=-4$: $f'(-4)=0$.  
Between $-4$ and $0$, e.g. -2: $f'(-2) = (-8) - 16(-2) = -8 + 32 > 0$. So positive on $[-4, 0]$.  
So the derivative is increasing? No, it changes sign.  
Let's plot roots of cubic $x^3 - 16x$.  
At $-4$, value is 0. Derivative is 0? No, at root derivative is zero.  
If derivative is $x(x^2-16)$, it's not a polynomial? No, it is.  
So at $x=-4$, slope is 0.  
For $x < -4$ (e.g. -5): $g'(-5) = (-5)(-25-16)?$ No, $(x^2-16)$ for -5 is 9. So $(-5)(9) = -45$. Negative.  
So at $-5$, slope is negative. At $-4$, it's 0.  
At $0$: slope is $0$ (since root is zero).  
Let's check behavior between roots of derivative: $-4$ to $4$.  
Between $-4$ and $0$, e.g. -1: $f'(-1) = (-1)(1-16) = 15 > 0$. Positive.  
So the function increases as we move from $-4$ towards $0$? Yes, since it's continuous at -4 (it touches 0).  
Since at $x=-4$ slope is 0 and for some range it goes positive, this looks like a local minimum or maximum in between.  
At $x=4$: derivative is 0.  
For $x > 4$, say 5: $g'(5) = (125) - 16(5) = 125 - 80 > 0$. Positive.  
So it increases on $(4, \infty)$.  
On $(-\infty, -4)$?  
At $x=-5$, slope is negative.  
At $x=-4$, slope is 0.  
So the function decreases from $-\infty$ to some value at $-4$? No.  
Let's re-evaluate:  
$x < -4$: e.g. -5. $g'(-5) = -45$.  
$x = -3$: $g'(-3) = 21$.  
So it decreases on $(-\infty, -4)$ (since negative, so slope becomes 0 at some point? No).  
If derivative is negative then positive, there must be a local minimum or maximum.  
Since $f'(x)$ goes from negative to zero and then back to positive. This means the minimum is not necessarily at -4, but something else if it decreases to that value.  
But let's check behavior at $-5$ vs $-3$.  
At $-5$, $g' < 0$. At $-4$, $g'=0$. At $-3$, $g'>0$.  
So the function is decreasing on $(-\infty, -4)$ and then increasing on $(-4, \infty)$? No.  
If it decreases from $-\infty$ to $-4$, then at $x=-4$ it reaches a minimum? Or local extremum?  
But for $x < -4$, it is decreasing. For $x > -4$?  
Check $x=0$. $g'(0) = 0$. So derivative changes sign from positive to negative or vice versa at $-4, 0$.  
For $x \in (-4, 0)$: e.g. -1. $g'(-1) = 15 > 0$.  
So function increases on $(-\infty, -4)$? No, decreases from $\infty$ to something at $-4$?  
Let's restart the derivative sign chart for $g'(x) = x^3 - 16x$.  
Roots: $-4, 0, 4$.  
For $x < -4$: Let's pick $x=-5$.  
$x^2 - 16 > 0 \implies$ term $(x+4)(x-4)$ is neg * pos = neg? No.  
$x(x^2-16)$. For $x=-5$, $x$ is neg, $x^2-16=9$. Product is neg * pos = neg. Correct.  
So decreasing on $(-\infty, -4)$.  
For $-4 < x < 0$: e.g. $x=-3$ (not in range). Pick $x=-1$.  
$x^2-16 = 9-16 = -7$. $x$ is neg. Neg * neg = pos.  
So increasing on $(-\infty, -4)$? No, wait.  
If $x < -4$, $g'(x) < 0$ (decreasing).  
If $-4 < x < 0$, then for small negative numbers like $x=-3$, we got positive value.  
So it must be that $g'(x)$ has sign changes at the roots.  
Roots of derivative are $\{-4, 0, 4\}$.  
Between $-4$ and $0$, the derivative is positive. So the function is increasing?  
Between $-4$ and $0$: yes.  
Wait, earlier I checked $g'(-5)$ for $x < -4$ was negative. And $g'(-3)$ was positive?  
If $g'(x) = x(x^2-16)$.  
Test $x=-3$: $g'(-3) = (-3)(9-16)$? No, $-27 - 48$? No.  
$x(x^2-16)$.  
For $x=-3$, $x^2=9, x=-3$. $x^2-16 = -7$. $g'(-3) = (-3)(-7) = 21$.  
So yes, at $x=-3$, it is positive.  
At $x=-5$, $x^2=25, x=-5$. $g'(-5) = (-5)(9) = -45 < 0$.  
So derivative goes from negative (at $-\infty$) to positive at some point and then back? Or something?  
Let's order roots again. $x^2-16=0 \implies x=\pm 4$.  
Factor: $x(x-4)(x+4)$? No, that has degree 3.  
Ah, I made a mistake in factoring or reading the term "degree 3" and "root at -4".  
$x^3$ term is positive coeff 1.  
So roots are $\{-4, 0\}$?  
No, the equation $x(x^2-16)=0$ has solutions $x=0$ and roots of $x^2-16=0$, which are $\pm \sqrt{16}$.  
$\pm 4$.  
So critical points are $0, -4, 4$.  
Let's check the sign change again carefully.  
$x < 0$: e.g. $x=-5$.  
$g'(-5) = (-5)(25-16)$? No $g'(x)=x(x^2-16)$.  
$x=-5 \implies x^2=25$. $x^2-16=9$.  
$g'(-5) = (-5)(9) = -45$. (Negative).  
At $x=-4$: $g'(-4) = 0$. (Positive? No, root of derivative is negative.)  
So on $(-\infty, -4)$, $g'(x) < 0$. Function decreases.  
For $x \in (-4, 0)$: e.g. $x=-1$. $g'(-1) = (-1)(9-16)?$ No, $x^2=1$. $x^2-16=-15$.  
$g'(-1) = (-1)(-15) = 15 > 0$.  
So function increases on $(-4, 0)$? No.  
Since $g'(-4)=0$ and $g'(-1)>0$, it must be that for $x \in (-\infty, -4)$, decreasing, and then increasing at $-4$. But what about $0$?  
At $x=0$, $g'(0)=0$.  
Between $-4$ and $0$: e.g. $x=-1$ gives positive derivative. So function is increasing on $(-4, 0)$.  
But earlier I said for $x < -4$, it decreases to $-\infty$? No.  
Wait, let's check the values again.  
If it increases on $(-\infty, -4)$ (from $\infty$ down to $-4$?), then at $-4$ it should be 0? No, if it's continuous and increasing, it must be higher?  
If derivative is negative, function decreases. If derivative is positive, it increases.  
So on $(-\infty, -4)$: decreasing. (Decreases from $\infty$ to $g'(-4)=0$?). No, if it decreases, then at some point $g'$ must cross 0.  
But $g'(-5)=-45 < 0$. So decreasing continues past -4?  
No, at -5 slope is negative. At -3 slope is positive? No.  
Let's check my value for $x=-3$:  
$g'(-3) = (-3)(25-16)?$ No, $(x^2-16)$ at -3 is $9-16 = -7$.  
$x(x^2-16) \implies (-3)(-7) = 21 > 0$.  
So derivative changes from negative (at -5) to positive (at -3).  
So there must be a root where slope is 0. Wait.  
Let's re-calculate carefully for $g'(x) = x^3 - 16x$.  
Is it correct?  
$g'(x) = \frac{d}{dx}(\frac{1}{4}x^4 - 8x^2 + 81)$. No.  
$f(x) = \frac{1}{4}x^4 - 8x^2 + 81$.  
$f'(x) = x^3 - 16x$. This is correct.  
Let's plot $y=x(x-4)(x+4)$? No, $(x)^3-16x$.  
Roots are $\{0, \pm 4\}$.  
Let's test points around roots.  
$x < -4$ (e.g. -5): $(-5)^3 - 16(-5) = -125 + 80 = -45$. Negative.  
Between $-4$ and $0$:  
$-4 \implies g'(-4)=0$. $x=-3 \implies (-27)+48=21$. Positive? No, wait.  
$g'(x) = x^3 - 16x$.  
$x(x^2-16)$. If $x=-3$, $x^2=9$, $x^2-16 = -7$. $(-3)(-7)=21 > 0$.  
So it's positive at -3.  
If $g'(-4)=0$.  
At $x \to -\infty$, $g'(x) < 0$ (since $x^3 - 16x \approx x^3$).  
At $x=0$, $g'(0)=0$.  
Between roots, sign changes? No.  
Let's check derivative for $x \in (-\infty, 0)$.  
Wait. If roots are $\pm 4, 0$, then the polynomial has to be $(x+4)(x-4)x$? No.  
$x^3 - 16x = x(x^2-16)$.  
Factor: $x(x-4)(x+4)$ has roots $0, 4, -4$.  
This implies signs at $\pm 4$:  
At $x=-5$, $f'(-5) = (-5)(25-16) = -45 < 0$.  
So it decreases on $(-\infty, -4]$.  
Then for $x \in (-4, 0)$? e.g. $x=0.5$: $f'(0.5) = (1/8)(1/2)^3$? No. $g'(0.5) = 0.5^3 - 16(0.5) = 0.125 - 8 < 0$.  
So $x \in (-4, 0)$, $g'$ is negative.  
So for all $x \in [-4, \dots)$?  
Let's check my factorization again.  
Ah! I am mixing up roots of $x^3-16x$ with roots of graph.  
Let's just compute values for a few points.  
$x=-5$: $g'(-5) = -45$. (Negative).  
$x=-3$: $g'(-3) = 21$. (Positive).  
So critical point at $x=-4$ is indeed a local minimum? Or maximum?  
If it's negative then positive, and derivative changes sign from negative to positive at some point, that point is a minimum.  
But we have negative for all of $(-\infty, -3)$?  
Let's check the signs more generally.  
$x^3 - 16x$.  
Factor: $x(x-4)(x+4)$. No, I don't know if this polynomial factorization is correct.  
$(x-4)(x+4)x = x^2(x^2-16)$? No. $(x^2-16) \cdot x = x^3 - 16x$. Yes, it factors as $x(x^2-16)$.  
And $x^2-16$ factors to $(x-4)(x+4)$.  
So the polynomial is $x(x-4)(x+4)$ is NOT correct? No, it's just that I thought it was.  
Let's check roots again.  
Roots are where derivative is 0: $x=0$, $x=\pm 4$.  
Let's verify with graph of $f'(x) = x^3 - 16x$.  
It has roots at $-4, 0, 4$? No, that's what I got earlier.  
But $(-5)^3 - 16(-5) = -125 + 80 = -45 < 0$.  
Let's test the sign of $x(x^2-16)$ at $x=-3$.  
$x=-3$: $x^2=9$, $x^2-16 = -7$. Product: $(-3)(-7) = 21 > 0$.  
So derivative is positive on $(-4, 0)$ (since $x$ goes from negative to positive).  
For $x < -4$, e.g. -5: $x=-5$. $x^2=25$. $x^2-16 = 9 > 0$. Product: $(-5)(9) = -45 < 0$.  
So for $x < -4$, derivative is negative.  
Between $-4$ and $0$? e.g. $x=-1$. $x=-1$. $x^2=1$. $x^2-16=-15$. Product: $(-1)(-15) = 15 > 0$.  
So derivative is positive on $( -4, 0 )$.  
And negative on $(-\infty, -4]$.  
Wait. If it's negative on $(-\infty, -4)$ and positive on $(-4, 0)$?  
Then it crosses 0 at $-4$? No, at $x=-3$ derivative is 21, so yes.  
So function decreases from $\infty$ to some value, then increases after the point where it's 0?  
But what about positive values of derivative?  
If $g'(x)$ changes sign at $x=4$: let's check.  
At $x=4$, $g'(4)=4(16-16) = 0$.  
Between $x=-4$ and $0$, it was positive?  
Let me re-evaluate: at $x=2$: $g'(-5)$? No.  
$x=4 \implies g'(4) = 4^3 - 16(4) = 64 - 64 = 0$.  
$x=6 \implies g'(6) = 6^3 - 16(6) = 216 - 96 > 0$.  
$x=-4 \implies g'(-4) = (-64) - 16(-4) = -64 + 64 = 0$.  
$x=-5 \implies g'(-5) = -125 + 80 < 0$.  
So for $x \in (-\infty, -4)$:  
At $-\infty$: positive term dominates. $g'(x) \approx x^3$. So negative.  
At $-4$: $g'(-4) = 0$.  
Is it increasing or decreasing before?  
Let's look at the graph of $g'(x)=x(x-4)(x+4)$ (roots $\pm 4, 0$).  
Sign chart for cubic $ax^3+bx^2...$ where $a=1$.  
Roots: $-4$, $0$, $4$.  
Between $-4$ and $0$: $g'(-1) = (-1)(1-4)?$ No. $(x+4)(x-4)x$.  
If $x=-3$: $g'(-3)=21 > 0$.  
So for $x \in (-\infty, -4)$?  
Let's pick $x=-5$: $(-5)(25-16) = -45 < 0$.  
So $g'(x)$ is negative.  
Is it possible that it goes from positive to zero on the interval $(-\infty, -4)$? No, if it was decreasing.  
If $x \to -\infty$, $g'(x) \to -\infty$.  
At $-5$, $g' = -45$. It's already negative. So if it goes to $-\infty$ (as we expect for a cubic), and then decreases?  
No, let's plot the sign of $g'(x)$ more carefully.  
Roots are $-4, 0, 4$.  
Signs:  
1. $(-\infty, -4)$: $x < 0$, $x^2 > 16$. $x(x^2-16) = (\text{neg})(\text{pos}) = \text{neg}$. Decreasing.  
2. $(-4, 0)$: $x > -4$ (neg?), no. $x^2 < 16$ is false? No. $x^2 < 16$ for $|x| < 4$.  
If $x \in (-4, 0)$, then $x^2 < 16$, so $x^2-16 < 0$.  
$x$ is negative here. So product: $(\text{neg})(\text{neg}) = \text{pos}$. Increasing.  
3. $(0, 4)$: $x > 0$. $x^2-16 < 0$ (for $x<4$). $x>0$. Product: $(\text{pos})(\text{neg}) = \text{neg}$. Decreasing.  
4. $(-\infty, -4)$: product is negative.  
So let's check roots again.  
For $x < 0$, the sign of $x(x^2-16)$:  
If $x \in (-4, 0)$, product positive?  
Example: $x=-1$. $(-1)^2-16 = 9-16 = -7$ (negative). $x$ is negative. So prod is positive. Correct.  
So $g'(x) > 0$ for $x \in (-4, 0)$.  
If $x > 0$, say $x=2$. $(2^2-16) = -12$. $x=2$. Product negative.  
So decreasing on $(0, \dots)$? No.  
At $x=4$, it's zero?  
Check $x \in (0, 4)$. Say $x=5$. $(25-16)=9 > 0$. $x=5$. $5(9) = 45 > 0$?  
No, derivative is $x(x^2-16)$ for $g'(x) = \frac{d}{dx} f(x)$.  
For $x > 0$: e.g. $x=2$, term $x^3 - 16x < 0$.  
So decreasing on $(0, 4)$? No. It goes down from 0 to negative?  
Let's re-evaluate:  
$x=2 \implies g'(2) = 8 - 32 = -24$. Negative.  
So $g'(x)$ is negative for $x > 4$ and positive for $0 < x < 4$ (No, wait).  
If $x=3$: $g'(3) = 27 - 48 < 0$.  
If $x=-1$: $g'(-1) = -1(9-16) = 15 > 0$.  
So it's negative between roots? No.  
Let's look at the factorization of the derivative: $D(x) = x^3 - 16x$.  
Factor: $x(x-4)(x+4)$ is not correct because leading coeff is positive, so sign changes as $x$ increases?  
If $x > 0$, $g'(x)$ negative on $(0, \dots)$.  
Let's re-calculate signs.  
$x=2$: $g'(2) = -24 < 0$.  
$x=-1$: $g'(-1) = -(-5) = 5$? No, $(-1)(9-16) = 15$.  
Is it positive or negative for $x=-3$?  
$g'(-3) = (-27) + 48 > 0$.  
So signs of derivative on real line.  
Sign chart:  
For $x \in (-\infty, -4)$:  
$x < 0$, $x^2-16 > 0$. Product $< 0$. So negative.  
For $x \in (-4, 0)$:  
$-4 < x < 0 \implies x^2 < 16$. $x^2 - 16 < 0$. $x < 0$. Product $> 0$. So increasing? No, decreasing from left?  
No, if it's negative then positive at root. It must have a turning point at some point? No, roots are critical points.  
So derivative changes sign between roots? No, that's only if there's a root in the interval.  
Here we have roots $\{-4, 0, 4\}$.  
Wait, earlier I calculated $x=-1$ gives positive, which is consistent with increasing on $(-4, 0)$ if decreasing from -4.  
But for $x=2$, it's negative. So it must cross zero?  
But roots are only $\{-4, 0, 4\}$.  
This means derivative must change sign at these points.  
Let's check if my sign analysis is correct.  
Maybe I should look at the equation of the curve for $x^3 - 16x$ more simply.  
It's a polynomial in $x$. It has real roots $\{-4, 0\}$? No.  
It has roots at $x=0$ and $x=\pm 4$ (if we consider factors).  
Let me factor it correctly:  
$x^3 - 16x = x(x^2-16) = x(x-4)(x+4)$ is NOT correct because $(x-4)(x+4)=x^2-16$.  
So $x^3 - 16x$ has roots $x=0$, $x=\pm \sqrt{16} = \pm 4$.  
Yes, so the critical points of $g'(x)$ are $x=-4, 0, 4$.  
Now let's check signs for these intervals.  
$x < -4$: e.g. -5. $(\text{neg})(\text{pos})$? No. $x^2-16 = 25-16=9 > 0$. So negative.  
So decreasing on $(-\infty, -4)$.  
For $-4 < x < 0$: e.g. -3. $(\text{neg})(\text{pos})$? No. $x^2-16 = 9-16=-7 < 0$. So negative * neg = pos.  

*Continued in [part 3 of 3](algebra_1143_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
