# test/intermediate_algebra/1806.json (Intermediate Algebra, level 5)

> Let $z$ be a complex number such that $|z| = 1.$  Find the maximum value of  
> \[|1 + z| + |1 - z + z^2|.\]  

**Wrong.** Gold `\frac{13}{4}`, predicted `None`. Finish: length, 16384 tokens, 13 waits, 2117.4 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Let $N = |1 + z| + |1 - z + z^2|$, where $z$ is a complex number such that $|z| = 1$.  
We want to maximize this expression.  

The first term is $f_1(z) = |1 + z|$.  
Since $|z| = 1$, we can think of $z$ on the unit circle in the complex plane.  
The second term is $f_2(z) = |1 - z + z^2|$.  

Let's expand the terms and consider geometric interpretations or properties.  
Let $\theta$ be an angle such that $z = e^{i\theta}$. Then $z = \cos \theta + i \sin \theta$, so $z^2 = \cos 2\theta - i \sin 2\theta$.  
However, it's not strictly required to use polar coordinates for the substitution, but it helps to simplify the expressions.  

Let's look at the expression term by term:  
1. $|1 + z|$: The magnitude of $1 + z$ where $z$ is on the unit circle. This can be written as $\sqrt{(1+\cos\theta)^2 + \sin^2\theta} = \sqrt{1 + 2\cos\theta + \cos^2\theta - \sin^2\theta}$?  
Let's stick to $z = e^{i\theta}$.  
$|1 + z| = |1 + e^{i\theta}|$.  
Also, for $z$ on unit circle, this quantity is related to the distance from $-1$ to the point $z$? No.  
It is $\sqrt{2}$ if $z=0$, but we are on the unit circle so $z \ne 0$.  
Let's use polar form for the magnitude:  
$|1 + z| = |e^{i\alpha} + e^{i\beta}|$ where $\theta$ is phase.  
Or simpler, if $z=e^{i\theta}$, then $|1+e^{i\theta}|^2 = 1 + e^{i\theta} + e^{-i\theta} + 1 = 2(1 + \cos\theta) + 0$ ? No.  
$|a+b|^2 = a\bar{b} + b\bar{a} + |a|^2 + |b|^2 - 2\text{Re}(a \bar{b})$.  
For $|1+e^{i\theta}|^2 = (1+\cos\theta)^2 + (\sin\theta)^2 = 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta = 2 + 2\cos\theta$.  
This is $|1+z|^2$ in terms of $\theta$.  
Max value of $|1+e^{i\theta}|$ on the unit circle?  
Actually, $z=e^{i\theta}$ means $z = \cos\theta + i\sin\theta$.  
Then $1+z = 1+\cos\theta + i\sin\theta = 2\cos^2(\theta/2) + e^{i\theta} - 1$? No.  
Let's calculate $|1+e^{i\theta}|^2$ directly.  
The expression is $\sqrt{2} \cdot \text{something}$? No.  
Let $z = e^{i\theta}$. Then $|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta = 2+2\cos\theta$.  
This is maximized when $\cos\theta = 1$, i.e., $z=1$, then value is $\sqrt{4} = 2$. Or minimized when $\cos\theta = -1$ ($z=-1$), value is $\sqrt{0}=0$.  
However, this is just $(1+z)^2 + z^2$. That's not right.  
$|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta$ is not correct because $z$ has imaginary part $\sin\theta$.  
Let $a=1$, $b=z=e^{i\theta}$. $|1+b|^2 = 1+|b|^2+2\text{Re}(b) = 1+\cos^2\theta + 2\cos\theta$? No.  
$|1+b|^2 = (1+\cos\theta)^2 - (\sin\theta)(-\sin\theta)?$ No.  
$(1+\cos\theta)^2 + \sin^2\theta = 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta = 2 + 2\cos\theta$. This is $|1+z|^2$ in terms of $\theta$ is correct.  
But if $z=e^{i\theta}$, then $1+e^{i\theta}$ has magnitude squared?  
Let's check again. $1 = e^{0}$. $z = e^{i\theta}$.  
$|1+z|^2 = (e^0 + z)(e^{-0} \overline{z})$ ? No, that's wrong.  
Magnitude of vector sum $a+b$. $|a+b|^2 = a\bar{b} + b\bar{a} + |a|^2+|b|^2 - 2(a\bar{b})\cos(\text{angle})$? No.  
Let's use formula: $|u+v|^2 = |u|^2 + |v|^2 + 2\text{Re}(u\bar{v})$.  
Here $u=1, v=z=e^{i\theta}$. $u \bar{v} = e^{-i\theta}$. $\text{Re}(e^{-i\theta}) = \cos\theta$.  
So $|1+z|^2 = |1|^2 + |z|^2 + 2\cos\theta = 1 + 1 + 2\cos\theta = 2(1+\cos\theta)$. This is correct.  
Since $z$ lies on unit circle, $|z|=1$, so $z^* z = 1$.  
The term is $\sqrt{|1+z|^2}$.  
The maximum of $|1+z|$ when $|z|=1$:  
Let $w = 1+z$. Then $|w|^2 = |1+e^{i\theta}|^2 = 2(1+\cos\theta)$.  
Max is when $\cos\theta=1$ i.e., $z=1$, giving $|1+w|=2$. But this value depends on the angle.  
The term we are maximizing is $|1+z|$ (magnitude). The max possible magnitude is 2, but that occurs at $z=1$.  
If $z=-1$, it's 0. If $z=i$, $1+i \to \sqrt{2}$.  

2. Term $|1 - z + z^2|$:  
Let $w = 1 - z + z^2$. We need to find the maximum of $|w|$ for $z=e^{i\theta}$? No, just finding max over $\theta$.  
Alternatively, notice $z^3 = 1$ corresponds to something.  
Let's write in terms of polynomials or complex numbers.  
Wait, there's a known identity involving $z^2+1+z$ etc?  
The expression is $|1 - z + z^2|$.  
Maybe substitute $w = z-1$? No.  
Consider the substitution $y=1-z$? Then $z = 1-y$.  
If $z=e^{i\theta}$, then $y = e^{-i\theta} - 1$.  
Let's try to rewrite $|1 - z + z^2|$.  
We know that if $w=1-z$, $w+1-z$ is not simple.  
Maybe express in terms of the roots? No.  
The expression looks like a determinant or something related to polynomials.  
$1 - z + z^2 = (z-1)(z-0)$? No, $(z-1)^2 + 1$? No.  
$z^3+1 = (z+1)(z^2-z+1)$. Not directly related to $|1+z|^2$.  
Let's see if we can factor it or rewrite.  
Consider $(z-1/2)^2$?  
Or consider geometric interpretation in the complex plane.  
Points on unit circle are $e^{i\theta}$.  
The term $1 - z + z^2$ corresponds to vector addition: $(1,0)$ and vectors $-z, z^2$? No.  
Let's visualize it in terms of angles.  
Or maybe write $|1 - z + z^2|$ as modulus of a complex number.  
Is there a relation with the polynomial roots?  
Consider $(1-z)(1+z)$ is not relevant.  
Let's try to see what the value is when $z$ is close to something.  
Or maybe $z$ must be such that $|1 - z + z^2|$ takes specific values.  

Let's use polar coordinates or substitution again.  
Let $z = e^{i\theta}$.  
Then $f_1(z) = |1+e^{i\theta}| = \sqrt{2(1+\cos\theta)}$.  
This is maximized when $\cos\theta=1 \implies z=1$, giving 2.  
Minimum is at $\cos\theta=-1 \implies z=-1$, giving 0.  
The term $f_2(z) = |1 - e^{i\theta} + e^{2i\theta}|$.  
Let's simplify this.  
$|1 - (z) + z^2|$?  
$1 - z + z^2 = \frac{z^3+1-z}{z}$ ? No.  
Notice $1+z+z^2$ roots are primitive cube roots of unity. $\omega, \omega^2, 1$. No, that's for $z^3-1=0$.  
For $z^3 + w$, the roots are complex cube roots of $-w$? No.  
Let's check the sum of powers.  
Note that if $z^2 = -1$, then $1-z+z^2 = 1-1=0$, which means max is attained when term is 0.  
For $z=-1$, term is 0.  
For $z=i$, $|1-i+i^2| = |1-i-1| = |-i| = 1$.  
For $z=i$, $|1+i| = \sqrt{2}$. Total $\approx \sqrt{3} > 0.7$?  
Let's check max for each term separately or together.  
Let's analyze the maximum of $f_1 + f_2$.  
Since we want to maximize the sum, maybe we should try to choose $z$ that minimizes one and maximizes the other, but they are not independent. They share variables.  
If $z = e^{i\theta}$, then $f_1(z) = |1+z|^2 + f_2(z)^2$? No.  

Let's rewrite $|1-z+z^2|$.  
We can expand this as a polynomial in $z$:  
If we substitute $w=z$, it is just evaluating the magnitude of a polynomial at a point on unit circle.  
Is there any way to use AM-GM inequality or something?  
Or maybe using conjugate symmetry.  
Since $|1+z|$ and $|1-z+z^2|$ are related to polynomials $P(z) = 1+z, Q(z) = 1+z+z^2$? No.  
Let's see: $|1+z|^2 + |1-z+z^2|^2$.  
This doesn't seem like an obvious maximum.  
However, note that $z = e^{i\theta}$ makes the expression depend on $\theta$.  
The magnitude is always positive real for some cases? No.  
Let's evaluate at specific values of $z$:  
$z=1 \implies f_1(1) = |1+1| = 2$.  
$f_2(1) = |1-1+1^2| = |1| = 1$.  
Sum = 3.  

$z=-1 \implies f_1(-1) = |1-1| = 0$.  
$f_2(-1) = |1-(-1)+(-1)^2| = |1+1+1| = 3$.  
Sum = 3.  

$z=i \implies f_1(i) = |1+i| = \sqrt{2}$.  
$f_2(i) = |1-i+i^2| = |0| = 0$.  
Sum = $\sqrt{2} \approx 1.41$.  

$z=-i \implies f_1(-i) = |1-i(-1)| = \sqrt{2+1}$? No.  
$f_1(-i) = |1-i|$.  
$f_2(-i) = |1-(-i)+(-i)^2| = |1+i-1| = 1$.  
Sum = $2\sqrt{3} + 0$? No, $\sqrt{2}$ and 1. Sum is $\sqrt{2}+1 \approx 2.41$.  

Is it possible to get more than 3?  
Let's test other angles for $f_1$. Max was 2 at $z=1$, min 0 at $z=-1$ (if that were allowed).  
$f_2$: Let's check the range of values.  
Wait, $f_2(z) = |1-z+z^2|$.  
Let's try to find max for this.  
The complex number $w = 1-z+z^2$.  
$z=e^{i\theta} \implies w(\theta) = e^{i(3\theta/2)} + 0 + 0$? No.  
Let's rewrite $w$.  
$1 - z + z^2$. This is not a standard polynomial evaluation at roots.  
But notice that if $|z|=1$, then $z^* = 1/z$.  
So $1-z+z^2$ evaluated on unit circle might be bounded?  
The term is bounded by triangle inequality:  
$|1 - z + z^2| \le |1 - (-1)| + |-1| + |0| = 2+1=3$ ?  
No, if $z=1$, it is 1. If $z=-1$, it is 3. If $z=i$, it is 0.  
If we use triangle inequality, the value could be large if $1-z+z^2 \approx z$.  
Let's check the maximum of $|1 - z + z^2|$ for $|z|=1$.  
Wait, is there a geometric bound?  
This expression looks like distance between points.  
Consider $x=1$, $y=-z+e^{i2\theta}$?  
Let's try to relate this to the roots of unity.  
Note that $w = 1 - z + z^2$ has magnitude squared:  
$|w|^2 = (1-z+z^2)(1-\overline{z}+\overline{z^2}) = (1-z+z^2) \frac{z}{\bar{z}}$ ? No.  
Let's calculate it properly using polar form or simply substitute $z$.  
Wait, there is a nice identity: $|z^3-1| \le 2|z|$? No.  

Let's go back to $|1+z|^2 = 2(1+\cos\theta)$ and $|1-z+z^2|^2$.  
Maybe I should calculate the value at $\theta = \pi/3$, $\pi, \dots$  
Actually, if I can find a better upper bound.  
Is there any simpler relation?  
Let's rewrite $1 - z + z^2$.  
If $z = e^{i\theta}$, let's consider $(z-1)$? No.  
Consider $(1-z+z^2) + (z-1+z^2) \dots$ No.  
Is there a substitution that maps this to something simpler?  
Maybe $u = z - 1/2$? No.  

Let's look at the expression again.  
We are looking for $\max_{|z|=1} (|1+z| + |1-z+z^2|)$.  
We found values:  
At $z=1$, sum = $2+1=3$.  
At $z=-1$, sum = $0+3=3$.  
At $z=i$, sum = $\sqrt{2} \approx 1.414$.  
At $z=-i$, sum = $|1-i| + |1+i-1| = \sqrt{2} + 1$.  

Let's check $z$ such that $z=i$ gives the max. $|1-z+z^2|$ is minimized when $z$ is close to something?  
If $z$ is large, magnitude of terms increases.  
Let's test $\theta = \pi/4$.  
$|1+i\sqrt{2}| + |1 - i + (-1)|$ ? No.  
$|1+z|$ for $\theta=\pi/4$ (real part 0): $|1+e^{i\pi/4}| = \sqrt{2}$.  
$|1-z+z^2|$ for $\theta=\pi/4$: $|1-e^{i\pi/4} + e^{-2i\pi/4}|$. No.  
$z=i$: $|1+e^{i\pi/2}| = |1+i| = \sqrt{2}$ (since $\sin^2 \theta = 1$, $2+0$).  
$f_2(\pi/4) = |1-i - i + (-1)|$? No, $z=1$ is $\theta=0$, $z^2=1$.  
$f_2(\pi/4)$ at $z=i$: $|1-i+i-1| = |-i| = 1$.  
So for $\theta=\pi/4$, sum is $2\sqrt{2}+1$? No.  
At $z=-i$, $f_1=|1-i|= \sqrt{2}$, $f_2=1$. Sum $2+\sqrt{2}$ approx 3.41.  

Let's check $\theta = -30^\circ$. Or something where terms align better.  
We want to maximize the sum. This usually happens when terms are large in magnitude.  
For example, if $z$ is near 1, $|1+z|$ is small (if we consider $|1-0|=1$).  
If $z=-1$, $f_1=0$.  
If $z$ is close to 0? No $|z|=1$.  
If $z = e^{i\pi} = -1$, $f_1 = 0$, $f_2 = 3$.  
If $z = e^{i \theta}$ such that $|1+z|$ is large, we need $\cos(\text{arg}(1+z)) = -1$? No.  
If $z$ is close to 0, not possible on unit circle.  
Max of $|1+z|$ is at $z=1$, value 2.  
Is it true that $|1-z+z^2| \le C |1+z|$? Or is the sum constrained by $|1+z|+|1-z+z^2| \le K$?  

Let's check values again.  
For $f_1 + f_2$, we found:  
$(z=-i) \to (\sqrt{2} + 1)$.  
$(z=1) \to (2+1) = 3$.  
Are there any points where sum is greater than 3?  
Maybe near $z=0$ but on unit circle? No.  
The maximum might be at an angle where trigonometric functions peak.  

Let's re-evaluate the function $f_2(z) = |1 - z + z^2|$.  
This is a continuous function on $S^1$. It must attain extrema.  
Since it is bounded, its max could be larger than 3? No, we have upper bound for each term.  
Let's check if the terms can be positive or negative independently? No, we want to maximize sum of magnitudes.  
We found $\max$ of first part is at $z=1$, value 2.  
Is it possible to get a larger total by optimizing the second part?  
No, the max for the whole expression would be bounded by $|f_1| + |f_2|$.  
Since $f_2 \le |1-z+z^2| = |z|^2 - 1 - z + z^2$? No.  
Let's use the property of magnitude: $|u| \le |u|^2$ is not true. $|u|^2 \ge 0$.  

Let's re-examine the expression.  
Is it possible to rewrite this as a product of complex numbers?  
Consider $1+z$ and $1-z+z^2$.  
Note that $1+z = (1+z)(1)$. $z=1$.  
Maybe we can express $1 - z + z^2$ in terms of $(1+z)^2$? No.  
Let's look at the polynomial identity.  
Let $P(z) = 1+z+z^2$. Then $|1+z|^2 = |e^{i0} + e^{i\theta}|^2$.  
Is it possible that $|1-z+z^2| = |z-1|^2 - \dots$ No.  

Let's try to substitute $z=e^{i\alpha}$.  
Then $f_1 + f_2 = |1+e^{i\alpha}| + |1-e^{i\alpha}+e^{-2i\alpha}|$.  
Note that $|1-e^{i\alpha}+e^{-2i\alpha}| = \sqrt{(1+\cos(3\theta/2)) (\dots)}$? No.  
Let's write $1-z+z^2$ in terms of complex numbers again.  
Consider the points on the unit circle corresponding to angles: $z_0$.  
The magnitude is distance from the origin in the plane?  
No, it is just a point on the complex plane.  
The expression is $g(z) = |1+z| + h(z)$ where $h(z)$ depends on $z$.  

Is there any symmetry to exploit?  
Let's look at $z=0$ again.  
If $z$ can be 0, then we have a trivial sum: $|1+0| + |1+0| = 2+1=3$.  
But constraint is $|z|=1$.  

Is it possible that max is not attained on unit circle?  
The problem asks for max value of $f(z)$ over complex numbers with $|z|=1$. So yes, on the circle.  
However, I recall something about a specific maximum value. Maybe related to 3 or similar integers.  
Let's check the case where terms might cancel or align in magnitude?  
For instance, if we could choose $f_2$ small and $f_1$ large. But $f_1 \ge 0$.  
We know $|z|=1 \implies |1+z|^2 = 2 + 2\text{Re}(z)$. This is max 4? No, at $z=1$, it's 4. At $z=-1$, it's 0.  
Is this true? $|1+e^{i\theta}|^2 = (1+\cos\theta)^2 + \sin^2\theta = 2 + 2\cos\theta$.  
Yes, range is $[0, 4]$. So $f_1(z)$ ranges from 0 to 2. The maximum value of the sum term $|1+z|$ is 2.  

For $h(z) = |1 - z + z^2|$. Let's evaluate it.  
Let's look at roots. Roots of $w(z)=1-z+w^2$? No.  
Roots of $z^3-1=0$ are $\pm e^{i\pi/3} \dots$  
What is the range of $h(z)$ on unit circle?  
$h(z) = |1-e^{i\theta}+e^{-2i\theta}|$. This looks like distance to origin.  
Let's rewrite it in terms of $z$:  
$|1 - z + z^2| = |(1-z)(1+z)| / \dots$? No.  
Let's look at the expression $z^3-1 = (z-1)(z^2+z+1)$? No, $z^2+z+1=0 \implies z^3=1$.  
$|1-z^2| = |1-z^2|$. Not really helpful.  

Let's try to simplify $1 - z + z^2$.  
Consider the function $f(z) = 1 - z + z^2$.  
We want max $|f(z)|$ where $|z|=1$.  
This is a problem of finding the maximum modulus of $1-z+z^2$ on unit circle.  
Let's evaluate at $z=1$, value is 1.  
At $z=-1$, value is $3$.  
At $z=i$, value is 0.  
At $z=e^{i\pi/4}$, we have $\theta= \pi/4$.  
$f(z) = |1 - (e^{i\pi/4}) + e^{-2i\pi/4}| = |1 - i(1+i)/(-1+1)?|$ No.  
Let's just plug in polar forms again for a specific angle.  
The function $f_2(\theta) = |1 - \cos\theta + i\sin\theta - \cos^2\theta|$.  
Since $z=e^{i\theta}$, $\bar{z} = e^{-i\theta}$.  
$f_2(z) = |1-z+z^2|$ is a distance from the point $(-1, 0)$? No.  
$1 = (1, 0)$.  
The points are on unit circle.  
Let's try to bound it using triangle inequality in complex plane.  
Consider $w = 1-z+z^2$. We know $|1+e^{i\theta}|$ and $|1-e^{i\theta}+e^{-2i\theta}|$.  
Note that $(z-1)^2 + z^2$? No.  
Let's use the fact that $f(z)$ is just a polynomial in $z$.  
But maybe there is a relation like $h(z) = \text{Re}(\dots)$ or something?  

Let's reconsider $|1+z|^2 = 4$ at $z=1$, so it's $2+0$.  
We need to maximize $\sqrt{2+2\cos\theta} + |1 - e^{i\theta} + e^{-2i\theta}|$.  
Is there a case where the second term is large and positive?  
Let's test specific angles.  
$\theta = \pi/6$.  
$|1+z|^2 = 2(1+\cos(\pi/6)) = 2(1+ \sqrt{3}/2) = 2 + \sqrt{3} \approx 3.73$. $|1+z| = \sqrt{3.73} \approx 1.93$.  
$f_2(\pi/6) = |1 - e^{i\pi/6} + e^{-2i\pi/6}|$.  
$e^{-2i\pi/6} = e^{-i\pi/3}$.  
So $f_2 = \sqrt{(1-\cos\frac{\pi}{6})^2 + (\sin\frac{\pi}{6}-0)^2}$? No.  
Let's simplify $f_2$:  
$1 - z + z^2$.  
If $z=e^{i\pi/6}$.  
$|1-z+z^2|^2 = |1 - z + e^{-2i\pi/3}|$.  
This is not a simple algebraic simplification.  
Let's check the values again carefully.  
Maybe there's a geometric interpretation of $z^2+1+z$? No.  

Let's use polar coordinates directly on complex numbers.  
We have $f_1(z) = |1+e^{i\theta}|$.  
This is $\sqrt{2 + 2\cos\theta}$. This can be written as $\sqrt{2(1+\cos\theta)}$? No, it's $\sqrt{2+2\cos\theta}$ but $z=e^{i\theta} \implies z=1$ corresponds to max.  
But we need to consider the value of $f_2(z)$.  
Is there a known inequality?  
Consider $|1 + e^{i\theta}|^2 = 2+2\cos\theta$.  
Let's try to bound $f_2(z)$ by something related to $f_1$.  
Note that $(1 - z + z^2) = (1-z)(1+z) - z^3$? No.  
$(z-1)^2 = 1-2z+1 = 2-2z$.  
Maybe substitute $u = z-1$. Then $z = u+1$. But $|u+1|=1$.  
Let's try substitution with $\theta$.  
We found:  
$\theta=0 \implies f_1=2, f_2=1$, sum 3.  
$\theta=\pi/2 \implies f_1=\sqrt{2}, f_2=|1-i+i^2| = 0$, sum $\sqrt{2}$.  
$\theta=\pi \implies f_1=0, f_2=3$, sum 3.  
$\theta=\pi/4 \implies f_1=\sqrt{2}, f_2=|-i-1+1|= |-i|=0$? No $f_2 = |1-i\sqrt{2}-i|$.  
At $\theta=\pi/4$: $z=i$. Then $f_1 = |1+i| = \sqrt{2}$. $f_2 = |1-i + (-i) - 1| = |-i-1+0|$? No, $z^2=-1$. So $1-z+z^2 = 1-i+(-1)=0$.  
$f_2=0$. Sum $\sqrt{2} \approx 1.414$.  
$\theta=3\pi/4$. $z=i$. Same as above? No, $z=e^{i3\pi/4}$.  
$z^2 = e^{i3\pi/2} = -i$.  
$f_1 = |1 + e^{i3\pi/4}| = \sqrt{2+2\cos(3\pi/4)} = \sqrt{2+0} = \sqrt{2}$.  
$f_2 = |1 - (e^{i3\pi/4}) + (-i)|$? No, $z^2=z^2 = i^*$. No.  
Let's just calculate $f_2(3\pi/4) = 1-z+z^2$.  
$z = \frac{-1+i}{\sqrt{2}}$. $z^2 = \dots$?  
Actually, let's check if the maximum is attained at an angle where terms align.  
The function $h(z) = |1-z+z^2|$ has a peak?  
Let's analyze $\sin(\theta)$ behavior.  
Consider $f_2(\theta)$. This is bounded by 3?  
$|1-e^{i\theta}+e^{-2i\theta}| = |1-z+z^2|$.  
Let $z=e^{i\theta}$. $z^2 = \cos 2\theta + i \sin 2\theta$.  
Then $f_2(\theta) = |(1-\cos\theta - i\sin\theta) + (\cos^2\theta+ i(2\cos\theta-1)?)$ No.  
$f_2^2 = (1-\cos\theta)^2 + (\sin\theta - (1-z)) ...$? No.  
Let's expand $f_2(\theta)$ using real and imaginary parts of $z$.  
$z = \cos\theta + i\sin\theta$.  
$f_2(\theta) = |1 - z + z^2|$.  
This is $\sqrt{(1 - (\cos\theta+\cos 2\theta))^2 + (0 + i(\sin\theta+\sin 2\theta))}^2$? No.  
$(1-z+z^2)$ has real part $1-\cos\theta+\cos^2\theta$. Imaginary part $\sin\theta+\sin 2\theta$ ? No.  
Let's expand carefully.  
Real part: $R(\theta) = \text{Re}(1 - z + z^2) = 1 - \cos\theta + \cos 2\theta$.  
Imaginary part: $I(\theta) = \sin\theta + \sin 2\theta$? No.  
$z = e^{i\theta}$.  
$\text{Re}(z) = \cos\theta$, $\text{Im}(z) = \sin\theta$.  
$f_2(z) = |1 - z + z^2| = |(1,0) - (\cos\theta, \sin\theta) + (\cos 2\theta, \dots)|$.  
No. The term is $z^2 = e^{i2\theta} = \cos 2\theta + i\sin 2\theta$.  
So $f_2(z)$ squared is $(1-\cos\theta+\cos 2\theta)^2 + (\sin\theta+\sin 2\theta)^2$? No.  
$f_2^2(\theta) = (1 - \cos\theta + \cos 2\theta)^2 + \dots$ no, that's not correct because of imaginary part sign.  
The imaginary part is $\sin\theta + \sin 2\theta$. No, $f_2(\theta)$ has imaginary part coming from $(1) - \dots + z^2$.  
Real part: $1-\cos\theta+\cos 2\theta$.  
Imaginary part: $\sin\theta + \sin 2\theta$ ? No.  
Let's check again.  
$f_2 = |a+ib| = \sqrt{a^2+b^2}$.  
$a = 1 - \cos\theta + \cos 2\theta$.  
$b = \sin\theta - (-\cos\theta)\dots$ No.  
The term $z$ has imaginary part $\sin\theta$. The term $z^2$ has imaginary part $\sin 2\theta$.  
So $b(\theta) = \sin\theta - \sin\theta + \sin 2\theta$ ? No.  
Let's check the expression carefully again:  
$f_2(z) = |1 - z + z^2|$.  
$\text{Re}(z) = \cos\theta$.  
$\text{Im}(z) = \sin\theta$.  
$\text{Re}(z^2) = \cos 2\theta$.  
$\text{Im}(z^2) = \sin 2\theta$.  
So $1 - z + z^2 = (1-\cos\theta+\cos 2\theta) + i(\sin\theta+\sin 2\theta)$? No.  
$1$ has no imaginary part. So $\text{Re}(z^2)$ is real.  
$b = \sin\theta$.  
But what is the $b$ in $z^2$?  
$z = \cos\theta + i\sin\theta$.  
So $\text{Im}(\dots)$ must be derived correctly.  
$f_1(z) = |1+z| = \sqrt{(1+\cos\theta)^2 + \sin^2\theta} = \sqrt{2+2\cos\theta}$.  
Let's check this: $(1+\cos\theta+i\sin\theta)(1-\cos\theta-i\sin\theta) = (1+\cos\theta-i\sin\theta)(1+\cos\theta) + i(\dots)$? No.  
$|1+z|^2 = 1+e^{i\theta}$. $= |e^0+e^{i\theta}|^2$.  
So the real part is $1$, imaginary part is $\sin\theta$.  
So $a = 1-\cos\theta+\cos 2\theta$. This seems right.  
Let's check imaginary part $b = \sin\theta - \sin(2\theta) + (-1)(- \dots)$? No.  
Just use expansion:  

*Continued in [part 2 of 2](intermediate_algebra_1806_p2.md): GitHub stops rendering math on pages this long, so the transcript is split.*
