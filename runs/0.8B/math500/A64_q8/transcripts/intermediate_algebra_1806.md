# test/intermediate_algebra/1806.json (Intermediate Algebra, level 5)

> Let $z$ be a complex number such that $|z| = 1.$  Find the maximum value of  
> \[|1 + z| + |1 - z + z^2|.\]  

**Wrong.** Gold `\frac{13}{4}`, predicted `None`. Finish: length, 16384 tokens, 28 waits, 1767.5 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Let $A$ be the expression we want to maximize. The variables are complex numbers.  
Let $z = x + iy$.  
The condition is $|z| = 1$, which means $x^2 + y^2 = 1$, so $-1 \le x, y$ satisfy a unit circle.  
Wait, $z$ is a point on the unit circle, so $|z|^2 = 1$. Let $z = e^{i\theta}$. Then $x=\cos \theta, y=\sin \theta$.  

We want to maximize $f(z) = |1 + z| + |1 - z + z^2|$.  
Let's expand the terms in polar form or use triangle inequalities.  
$A = 1+z$, $B = 1-z+z^2$. We know that $|z|=1$ implies $|1| = 1$.  

Let $z = e^{i\theta}$.  
Then $1+z = 1 + \cos\theta + i\sin\theta = (1+\cos\theta) + i\sin\theta$.  
This can be written as $e^{i\phi}$ for some $\phi$.  
$|1+z|^2 = 1 + 2\text{Re}(z) + z^2 = 1 + 2\cos\theta + \cos(2\theta)$ ? No.  
Let's re-evaluate the terms.  

Term 1: $T_1 = |1+z|$. Since $|z|=1$, we have $|1+z|^2 = |e^{i0} + z|^2 = |1+z|^2$.  
$|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta = 1+2\cos\theta+2\cos^2\theta$.  
Let's check the expansion. $1+z = e^{i0} + z$ is not helpful directly, just using modulus.  
$|1+z|^2 = (1+\cos\theta)^2 + (\sin\theta)^2 = 1+2\cos\theta+1-2\sin^2\theta$. No.  
Let's use $|w|^2 = w \bar{w} = |1+z|^2$. Wait, that is not true. $|a+b|$ is modulus of sum.  
Actually $z$ is on the unit circle. So $z = e^{i\theta}$ means $x^2+y^2=1$, $\text{Re}(z)=x$, $\text{Im}(z)=y$.  
$T_1 = |1+z| = \sqrt{(1+x)^2 + y^2} = \sqrt{1+2x+x^2+y^2}$. Since $x^2+y^2=1$, this is $\sqrt{1+x^2+y^2-2x}$ ? No.  
It's just $(1+z)$ in the sense of complex number. So $|1+z|^2 = (1+z)(1+\bar{z}) = 1 + z + \bar{z} + z\bar{z} = 1 + 2\text{Re}(z) + |z|^2$.  
Since $|z|=1$, $|z|^2=1$. So $|1+z|^2 = 2 + 2\text{Re}(z)$? No.  
Let's re-calculate carefully.  
$|1+z|^2 = (1+z)(1+\bar{z})$ is incorrect because $(1+z) \neq \overline{(1+z)}$.  
The term is $|w|$ where $w=1+z$. We have $z = e^{i\theta}$.  
So $|1+z|^2 = |e^{i0} + z|^2$. This is not correct. The modulus of the complex number $a+bi$ is $\sqrt{a^2+b^2}$.  
Let's just compute it directly using polar coordinates for $z$.  
$z = \cos\theta + i\sin\theta$.  
$1+z = 1 + \cos\theta + i\sin\theta$.  
Modulus squared: $(1+\cos\theta)^2 + (\sin\theta)^2 = 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta = 1 + 2\cos\theta + 1 = 2(1-\cos\theta)$? No.  
$1 + 2\cos\theta + 1$ is wrong. It's $1+\cos\theta+1$.  
Let's do the sum: $(1+z)(1+\bar{z})$. No, that's not right.  
$|1+z|^2 = (1+z)(1+\bar{z})$ only if we treat it as a complex number product. But $z$ is complex.  
If $z=1$, $|1+1|=2$, but $(1+z)(1+\bar{z}) = 3$.  
Let's stick to algebraic definitions.  
$A = |1+z|$, $B = |1-z+z^2|$.  
$A^2 + B^2$? No.  

Let's express everything in terms of $x, y$. Since $x^2+y^2=1$, we have the constraint.  
$A = \sqrt{(1+x)^2 + (y-xi)^2} = \sqrt{(1+x)^2 + y^2 - 2xy}$.  
No, let's just use complex numbers: $|z|=1$.  
Term 1: $|1+z| = |e^{i0} + z|$. Let $f(z) = e^{iz}$. Then we are looking for max $|z-1|$? No.  

Let's simplify the terms using polar coordinates.  
$1+z = 2\cos(\theta/2 + \pi/4)?$ No. $1+e^{i\theta} = (1+\cos\theta) + i\sin\theta$.  
The maximum of $|1+z|$ is when $z=-1$, then $|1+z|=2$. But here $z$ can be anywhere on the circle. So $A = \sqrt{(1+x)^2 + y^2}$.  

Let's simplify term 2: $B = |1 - z(1+z)|$? No.  
$1-z+z^2 = (1-z)(1+z+z)$? No.  
$z^2 - z + 1 = z(z-1) + 1 = \dots$  
Let's factor or complete the square.  
$|1 - z(1+z)| = |1 - e^{i\theta}e^{-i\theta}|$? No. $z^2-z= z(z-1)$.  
The expression inside is $1 - z(1+z) = 1 - (z+z^2)$? No. It's $1 - (z + z^2)$ ?  
$B = |1 - z(1+z)|$. This doesn't look simpler.  

Let's factor it: $1 - z + z^2 = 1 - z(1-z) = 1 - z(1-z)$.  
Or $1 - z + z^2 = (1+z)(1-z) = 1 - z^2$? No.  
$(1+z)(1-z) = 1 - z^2$. So it's not a multiple of this.  

Let's go back to geometry. We have points in the complex plane $|z|=1$ and we are looking for distances between points or values at those points? No, just maximizing a sum of two terms.  
Let $x = \text{Re}(z)$, $y = \text{Im}(z)$. Constraint: $x^2+y^2=1$.  
$|1+z| = \sqrt{(1+x)^2 + y^2}$. Since $x^2+y^2=1$, let's substitute.  
$(1+x)^2 + y^2 = 1 + 2x + x^2 + y^2 = 1+2x+1 = 2+x$? No. $x^2+y^2=1$. So it is $2-x$ no. $y^2 = 1-x^2$.  
So $|1+z|^2 = (1+x)^2 + y^2 = 1+2x+x^2+y^2 = 1+2x+1 = 2+x$.  
Thus $A = \sqrt{2+x}$. No, $\sqrt{(1+x)^2+y^2}$ is not $(1+x) + y$? Yes it is.  
Is $x=2$? Max value of $2+x$ subject to $x^2+y^2=1$?  
This would require $x \ge 0$. Max $x = 1$ (if $y=0$), then $A=\sqrt{3}$. But $z=i$, then $1+z = 1+i$. Modulus is $\sqrt{2}$. No.  
Let's check my arithmetic. $|1+e^{i\theta}|^2 = (1+\cos\theta)^2 + \sin^2\theta = 1+2\cos\theta+1=2+2\cos\theta$?  
$2+x$ was based on $x$. If $z=e^{i\theta}$, $x=\cos\theta$. So it is $2+\cos(2\theta)$? No.  
$(1+\cos\theta)^2 + \sin^2\theta = 1+2\cos\theta+1 = 2\cos^2\theta$?  
Let's re-calculate $|1+z|^2$.  
$z = e^{i\theta} = \cos\theta + i\sin\theta$.  
$1+z = (1+\cos\theta) + i\sin\theta$.  
$|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta = 1+2\cos\theta+\cos^2\theta + \sin^2\theta = 2+2\cos\theta$.  
Okay, $|1+z|^2 = 2+2\cos(2\pi/\text{something})$.  
Let $\theta$ be angle such that $x=\cos\theta$, $y=\sin\theta$. Then $|1+z|^2 = 2+2\cos\theta$. This assumes real part of $z$? No.  
The modulus of $a+bi$ is $\sqrt{(a)^2+(b)^2}$. So here the term is $(1+\cos\theta) + i\sin\theta$. The square modulus is $(1+\cos\theta)^2 + \sin^2\theta = 2+2\cos\theta$.  
So $A = \sqrt{2+2\cos\theta}$.  

Now for term 2: $B = |1-z+z^2|$. Let's rewrite it.  
$z(1-z) + z(z^2-1) + z^3$? No.  
$1 - z + z^2 = (1+z)(1-z) = \dots$ no.  
$1 - z + z^2 = 0$ is satisfied if $z$ satisfies $z^2-z+1=0$. Roots are complex cube roots of unity. But $|z|=1$, so such roots exist.  
However, we need to maximize $|1+z+z^2|$? No. The expression is $|1-z+z^2|$.  
Note that $1+z = e^{i(0+\theta)}$? No.  
We can factor out $1$: $1 - z + z^2 = 1 - z(1-z)$.  
Actually, $z^2 - z + 1 = (z-1)^2 + 2z$? No.  
Let's rewrite the expression to use geometry directly.  
We have a sum of two magnitudes: $M_1 = |1+z|$, $M_2 = |1-z+z^2|$.  
Since $x^2+y^2=1$, we can parameterize.  
$A(z) = \sqrt{(1+x)^2 + (y-xi)^2}$. This is not quite right. Let's use vector notation.  
Let $\mathbf{u} = 1+z$. Then the second term is related to $z$.  
Actually $B = |1 - z(1+z) + z^2|$ ? No, that's just magnitude of a complex number.  
Let's expand $(1-z)(1+z)$? No.  
$1 - z(1+z) = 1 - (z+z^2)$? No. $z^2 - z = -z(1-z)$.  
So $|1-z+z^2| = |1 - z + z^2|$.  
Let's express the second term using polar form or geometric properties.  
$B = |1 - z(1+z)|$? No, $1 - z + z^2 = 1 - (z-z) \cdot \dots$.  
Consider $f(z) = 1-z+z^2$. We have $\sqrt{16}$.  
Let's rewrite in terms of $z$.  
$f(z) = 1 - z(1-z)$? No.  
$f(z) = 1 + (z^2-z+1) = 1 + \dots$ no.  
We know $|z|=1$, so $z^{-1} = \bar{z}/|z|^2$ is not correct.  

Let's use the property that $|w| = \max(|a+b|, |a-c|, \dots)$? No.  
This looks like maximizing $f(z) + g(z)$ where $g$ is a transformation.  
Is it possible to simplify $|1+z|$ and $|1-z+z^2|$ into linear forms or quadratics?  
Notice that $z^2 - z + 1 = (z-1/2 + i\sqrt{3}/2)(z-1/2 - i\sqrt{3}/2)$? No. The roots of $z^2-z+1$ are $\omega, \bar{\omega}$.  
Let's find the angle of the term $|1-z+z^2|$.  
We can write $f(z) = 1 - z(1-z)$. This does not simplify easily.  
Let's use coordinates for clarity. Let $z = e^{i\theta}$.  
$T_1 = |1+e^{i\theta}|^2 = 2 + 2\cos\theta$ (calculated before). So $|T_1| = \sqrt{2+2\cos\theta}$.  
$T_2 = |1-e^{i\theta} + e^{i2\theta}| = |1 - e^{i\theta}(e^{i\theta} - 1)| = |1 - (z^2 - z)|$? No.  
$1 - z(1-z)$. Let's expand the second term inside: $|1 - z + z^2|$.  
This is equivalent to $|1 + \omega z|$ where $\omega = e^{i\theta}$. Not quite.  
Let's just use polar expansion of $1-z+z^2$ in terms of real and imaginary parts directly, since this will be easier to maximize with geometry.  

Let $z = \cos\theta + i\sin\theta$.  
Term 1: $|1+e^{i\theta}|^2 = (1+\cos\theta)^2 + \sin^2\theta = 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta = 2 + 2\cos\theta$.  
So $A = |1+z| = \sqrt{2+2\cos\theta}$.  
Note that since $\theta$ is real, $-1 \le \cos\theta \le 1$, so $A \in [0, 2]$. Max possible is when $\cos\theta=1$, i.e., $z=-1$ (modulus 1). But this is a specific case. The term inside the modulus for $|1+z|$ is not $e^{i\theta}$?  
No, $1+z = 1+e^{i\theta}$. If $\cos\theta=1$, $z=1$. Then $1+z=2$ (real), so $|1+z|=2$.  
So $A \le \sqrt{4}=2$. The minimum of $\cos\theta$ is -1, max is 1. So $A$ goes from $\sqrt{0}$ to $\sqrt{4}$.  
But since $z=e^{i\theta}$, we have $|1+z|^2 = 2+2\cos\theta$. Since $2+2\cos\theta \in [0,4]$? No, $\cos\theta \in [-1,1]$. So max modulus is when $\cos\theta=1$ (z=-1), gives 4. But at z=1, we get 2. At z=-i, $1-i = 1+(-i)i^2$?  
If $z=i$, $1+i = \sqrt{2}$, so $|1+i|=\sqrt{2}$. $\cos\theta=0$.  
So $A$ is bounded by 2.  

Now for Term 2: $B = |1 - z + z^2|$. Let's find its modulus squared? No, we need to maximize the sum of magnitudes. The sum might be unbounded?  
Let's rewrite $z^2 - z + 1$. Roots are complex. But since we have constraints, maybe it is bounded.  
Is it possible that $B$ is always large enough?  
Let's try to relate $B$ to a circle or triangle inequality.  
Consider $z = e^{i\theta}$. Let $A = \sqrt{2+2\cos\theta}$, $B = \dots$  
Actually, the term inside the second modulus has magnitude $\le 1$? No.  
$|1-z+z^2| = |e^{-i0} - e^{i0} + e^{i20}|$ ? No.  
Let's rewrite $|1-z+z^2|$ using factorization of difference of squares: $(1-z)(1-z+z^2) = 1$. This is not helpful.  

Let's go back to $T_2 = |1 - z + z^2|$.  
Since $z$ is a complex number on the unit circle, we have $\overline{z} = \bar{z} = e^{-i\theta}$. No, that's just $\bar{z}$.  
We know $z^2+z=1-z$. So $1 - z + z^2 = (1+z)^{-1}(something)$? No.  
Let's use the identity $|w|^2 \le w \bar{w}$ for any complex $w$? No, triangle inequality.  
$|T_2| \le |1| + |-z| = 1+1=2$. So max is 2? Not necessarily.  

Is it possible that we need to consider the sum of absolute values? Or something like this.  
Let's try to relate $T_2$ to a geometric distance.  
Consider the triangle formed by points corresponding to coefficients.  
Wait, if $|z|=1$, then $|z|^2 = 1$.  
We want to maximize $S = |1+z| + |1 - z + z^2|$.  
Let's factor terms using properties of complex numbers.  
$1+z$ is just a vector. $z$ is another vector.  
$1-z+z^2$. Let's rewrite the second term as $e^{i\theta}$.  
Consider a specific case to see if it goes high.  
If $\theta = 0$, $z=1$. Then $|1+1|=2$, $|1-1+1|=1$. Sum=3.  
If $\theta = \pi/2$, $z=i$. Then $|1+i|=2$, $|1-i+i^2| = |1-i-1| = |-i| = 1$? No, $1 - i + (-1) = -i$?  
Let's calculate: $z=i$, $z^2 = -1$. So $1 - z + z^2 = 1 - i + (-1) = -i$. Modulus is 1. Sum = $\sqrt{2}+1$.  
If $\theta = \pi$, $z=-1$. Then $|1-1-1|=1$? No, $z^2=1$. $1-(-1)+1 = 3$.  
Let's calculate: $1 - (-1) + (-1)^2 = 1 + 1 + 1 = 3$. Modulus is $\sqrt{9} = \sqrt{3} \approx 1.73$.  
Sum = 2? No, $|1+z|=0$ if $z=-1$, no $z=-1$ means $A=0$?  
If $z=-1$, $|1+z|=0$, $|1-z+z^2| = |1 - (-1) + (-1)| = 1$. Sum = 1.  
So at $\theta = \pi/2$, sum is $\sqrt{2}+1 \approx 2.414$.  
Is it possible to have a larger value?  
Let's check $\theta$ such that $z^3=1$. Then $|1+z|$ and $|1-z+z^2|$ values might be related.  

Let's analyze the expression $f(z) = |1+z| + |1 - z + z^2|$ using trigonometric substitution directly.  
$A = \sqrt{2+2\cos\theta}$.  
For $T_2 = |1-z+z^2|$, substitute $z=e^{i\theta}$ again? No, $z$ is a specific value.  
Let's write $|1 - z(1-z)| = |1 - (e^{i0}- e^{-i0})|$? No.  

Let's check the maximum possible value of $B$. We have constraints on $A$ and $B$.  
We need to determine if the sum can exceed a certain bound.  
The expression looks like $|z|^2 + 1 + |z(1+z)-1| + \dots$.  
Actually, look at $T_2 = |1 - z + z^2|$.  
Note that for $z=1$, $T_2 = 1$. $A = |2| = 2$. Sum = 3.  
Let's check if the sum can be higher than 4?  
For $z=e^{i\theta}$.  
We need to maximize $\sqrt{2+2\cos\theta} + |1 - z + z^2|$.  
The second term magnitude is bounded by $\sqrt{(1- \text{Re}(z))^2 + (1)^2}$?  
Actually, $|1-z+z^2| \le 1 + |-1|$? No.  
Let's consider the maximum value of $B$. Since $\sqrt{4} = 2$ and sum is bounded by 3, maybe max is small?  
Let's re-evaluate my calculation for $z=i$.  
$z=i \implies z^2 = -1$.  
$1+z = 1+i$. Magnitude $\sqrt{2}$.  
$1-z+z^2 = 1 - i - 1 = -i$. Magnitude 1.  
Sum is $\sqrt{2} + 1 \approx 2.414$.  

Let's test $z=i/2$. $|z|=1/2$? No, modulus must be 1.  
Wait, if we scale it by a factor?  
No, the expression depends on $z$.  

Let's check $z^3 = 1 \implies z = e^{i\theta}$ such that $\cos \theta = \pm 1, \sin \theta = 0$ or something.  
Let's assume we can find an angle $\alpha$ and $\beta$ for the vectors inside.  
Wait, $T_1$ depends on $\cos \theta$.  
Actually, let's write the term $|1-z+z^2|$ as $|z| |e^{i\pi/3} - z|$. No.  

Let's go back to vector addition or polar form.  
For a given angle $\alpha$, we have points $P_1 = 1$, $P_2 = z$, $P_3 = z^2$?  
No, the variables are in the complex plane.  
Consider points on the unit circle with angles $\theta$.  
We need to find max of $|1+z|$ and $|1-z+z^2|$.  
Let's analyze $B(z) = |1 - z + z^2|$.  
$B(\theta) = |1 - e^{i\theta} + e^{i2\theta}|$.  
Note that if $\theta=0$, $z=1$, then $1-z+z^2 = 1-1+1 = 1$, so $|B|=1$.  
If $\theta=\pi/3$, $z=e^{i\pi/3}$.  
Then $1 - e^{i\pi/3} + e^{i2\pi/3} = 1 - (1/2 + i\sqrt{3}/2) + (-1/2 - i\sqrt{3}/2) = 1 - 1 - i\sqrt{3} - i\sqrt{3}/2$? No.  
$e^{i2\pi/3} = \cos(2\pi/3) + i\sin(2\pi/3) = -1/2 + i\sqrt{3}/2$.  
Wait, $z = e^{i\theta}$ with $\theta=\pi/3$ gives $e^{i2\theta} = e^{i2\pi/3}$? No.  
The angle is not relevant to $z^2$.  
Let's check $T_2 = |1 - z + z^2|$.  
Using polar form: $1 - \cos\theta - i\sin\theta + (-0.5+0.866i?)$ No.  
The roots of the polynomial are $\zeta_k = e^{i 2k\pi/3}$? No, $e^{\pm i2\pi/3}$.  
We have $|1 - z + z^2| \le |1-z| + |z+z^2|$? No.  

Let's try to bound the sum using triangle inequality directly.  
$A = |1+z| \le 1+|z|=2$? No, this is a loose bound. Max $|1+z|$ when $z=-1$ is $0$.  
If $z=-i$, $1+z = 1-i$. Modulus $\sqrt{2}$.  
Max of $A^2$ when $z=e^{i\pi}$ gives $0$. When $z=-1+i\epsilon$, etc.  

Let's look at the term $B(z)$.  
Notice that $z^2 + z + 1 = (z+1/2)^2 + 3/4$.  
Actually, let's write $B = |1 - z(1+z)|$? No.  
$1 - z + z^2 = 1 - z + z^2$.  
Let $f(z) = |1-z+z^2|$.  
Consider the points in complex plane:  
Point $P_1 = 1$. Point $P_2 = z$. Point $P_3 = z^2$.  
But $z$ is a variable point. Let's fix $\theta$, let's consider vectors corresponding to coefficients of powers.  
We have $|1+z|$ and $|1-z+z^2|$.  
Let's rewrite $B(z)$ as $|e^{-i\pi/6} - e^{i\pi/6} + \dots|$ No.  

Let's try a substitution. Let $z = x+iy$ with $x^2+y^2=1$.  
We want to maximize $\sqrt{(1+x)^2+y^2} + |1-x-y+z(x-ix)|$? No.  
Wait, $B = |1 - z + z^2|$. This is a function of two variables $(x,y)$ subject to circle constraint.  
This looks like the problem of maximizing distance from 0 to complex numbers?  
Actually, let's express it as distance between points on the unit circle or similar.  
Let $w = 1+z$. Then $z = w-1$. Since $|z|=1$, $|w-1|=1$. So $w$ lies on circle centered at 1 radius 1.  
So we want to maximize $|w| + |1 - (w-1) + (w-1)^2|$.  
This simplifies to:  
Maximize $S = |w| + |1-w+1-w^2|$. No, that's not quite right.  
Substitute $z$ back. The term inside the second modulus is $1-z+z^2$.  
Let's use geometric interpretation on the unit circle.  
The points are $1$, $-1$ (for $z=-i$) etc.  
Let's rewrite $|1 - z + z^2|$ in terms of $w=1+z$.  
Then $z = w-1$.  
Substitute $z$:  
$1-z+z^2 = 1 - (w-1) + (w-1)^2 = 1 - w + 1 + w^2 - 2w + 1 = w^2 - 3w + 3$.  
So the expression becomes:  
Maximize $|1+w| + |w^2 - 3w + 3|$? No.  
Let's check substitution carefully.  
We have $z$ such that $z^2-z+1=0$. This is not a general variable.  
The term inside the modulus is $B = 1-z+z^2$.  
Using $z=w-1$: $B = 1 - (w-1) + (w-1)^2 = 1 - w + 1 + w^2 - 2w + 1 = w^2 - 3w + 3$.  
So we want to maximize $S = |1+w| + |w^2 - 3w + 3|$, subject to the constraint that $|z|=1$ implies $|w-1|=1$, so $w$ lies on the circle centered at 1 with radius 1.  
Also $z$ can be any point on the unit circle?  
The substitution is valid only if we pick a specific value for $w$. No, $w$ is determined by $z$. But here $B$ depends on $w$ directly as well?  
Is it true that $|1-z+z^2|$ can be written as something related to the distance?  
Actually, let's check.  
Given $z \in \mathbb{C}$ with $|z|=1$, we have $|1+z|$.  
Let's use polar coordinates for $z$ again.  
We found earlier:  
$A = \sqrt{2+2\cos\theta}$.  
$B = |1 - z + z^2|$.  
Is there a relation to the maximum distance?  
Let's check if we can simplify $B$.  
$1 - z + z^2 = 1 + z(1-z)$? No.  
Consider $T(z) = |z+1/z|$ ? No.  

Let's use the fact that for $z \in \mathbb{C}$ with $|z|=1$, we have $z^{-1} = \bar{z}$.  
$|1 - z + z^2| = |1 - (z+z^2)| = |1 - z(1+z)|$ ? No.  
Let's just expand for $\theta$.  
Let's re-evaluate the problem using complex numbers directly without polar coordinates if possible, maybe with some inequalities.  
Actually, the maximum value is likely related to the roots of unity or unit circle geometry.  
Let's check $A + B$ again.  
Is it possible that $|1+z|$ and $|1-z+z^2|$ are related such that sum $\le$ something?  
Maybe using $z^3=1$. Then $T_2 = |1 - z + z^2| = |1 - e^{i\pi/3} e^{i0}| \dots$ No.  
Let's try to bound the modulus of terms individually.  
We have $T_1 = |1+z| \le 1+|z|=2$. So $A \le 2$.  
We have $T_2 = |1-z+z^2|$. Let's check the value when $z=i$.  
If $z=i$, $A=\sqrt{2}$. $B=|-i|=1$. Sum $\approx 2.414$.  
If $z=-1+i\epsilon$, then $z \to -1$, so $A \to 0$. But we need to check if it's possible for $B$ to be large while $A$ is small.  
Suppose $z = e^{i\theta}$. Then $T_2 = |1 - z + z^2|$.  
Is there a point where this term is close to 2?  
Let's check if the expression can exceed 4 or something large.  
Let's use Cauchy-Schwarz inequality on sums of squares? No.  

Let's rewrite $T_1$ and $T_2$ in terms of trigonometric functions to bound them by max values at the circle points.  
For a general point $z$ on the unit circle:  
We have $|1+z|^2 = 1 + |z|^2 + 2\text{Re}(z) = 1+2\cos\theta$.  
So $T_1^2 = 2+2\cos\theta$? No, $(1+x)^2+y^2$.  
If we take the modulus: $|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta = 2 + 2\cos\theta$.  
Yes.  
Now for $T_2$:  

*Continued in [part 2 of 3](intermediate_algebra_1806_p2.md): GitHub stops rendering math on pages this long, so the transcript is split.*
