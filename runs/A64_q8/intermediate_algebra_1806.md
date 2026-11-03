# test/intermediate_algebra/1806.json  (Intermediate Algebra, level 5)

- gold: `\frac{13}{4}`
- pred: `None`
- correct: False
- finish: length, tokens: 16384, waits: 28, secs: 1767.5

## Thinking (reasoning_content)

````text
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
$T_2^2 = |1 - z + z^2|^2 = |(-z)(1-z) + 1|^2$? No.
Let's use polar coordinates in the expression term.
Let $u = 1$.
Then we are maximizing $|u+z|$ subject to $|z|=1$ and minimizing/maximizing something related?
No, $T_2 = |u - v z^2 + \dots|$ ? No.
Let's factor out the constant term from the second modulus.
We can think of this as a geometric optimization problem on the unit circle in 2D.
We want to maximize $\sqrt{(1+x)^2+y^2} + |1-x+iyz^2 - \dots|$? No.
Let's use coordinates $(x,y)$. The constraints are $x^2+y^2=1$ for both points.
So we have the sum of distances from 0 to $w_1$ and 0 to $w_2$ where $w_1 = 1+z$ and $w_2 = z^2-z+1$ ? No.

Let's rewrite $B = |z^3-1| / \dots$? No.
Let's try to express $T_2$ as the distance of some points.
Notice that $1 - z + z^2$ is related to the polynomial with roots $\omega, \bar{\omega}$.
Let's look at the expression for $z=e^{i\theta}$ in terms of vectors on unit circle.
We want to maximize $\sqrt{(1+\cos\theta)^2 + \sin^2\theta} + |1 - z + z^2|$.
This is equivalent to maximizing $A+B$ where $A, B$ are magnitudes of complex numbers formed by $z$ itself.
The modulus of the second term is $\le 1+z+z^2$? No.

Let's check the maximum possible value for a single term.
We know that on the unit circle, we can have terms as far from each other?
Actually, look at the geometry in the complex plane.
We are considering points $P_1 = z$, $P_2 = 1-z+z^2$ ? No, $P_2 = 1 - z + z^2$.
Let's re-examine $|1-z+z^2|$.
The expression inside is $1 - (z-z) + \dots$
Maybe factor out $z$? $1 - z(1+z)$. No.
Is it possible to write $|1-z+z^2|$ in terms of $\sqrt{...}$?
Let's try substituting specific angles.
We want to maximize $f(\theta) = \sqrt{2+2\cos\theta} + |1 - e^{i\theta} + e^{i2\theta}|$.
We already tested a few angles:
$\theta=0 \implies z=1$, sum=3. (Here $\cos \theta = 1$)
$\theta=\pi/6 \implies z=e^{i\pi/6}$, $x=1/2, y=\sqrt{3}/2$.
Then $A = \sqrt{(1+1/2)^2 + (\sqrt{3}/2)^2} = \sqrt{9/4 + 3/4} = \sqrt{12/4} = \sqrt{3} \approx 1.732$?
Let's recalculate $A^2$.
$(1+1/2)^2 + (\sqrt{3}/2)^2 = (3/2)^2 + 3/4 = 9/4 + 3/4 = 12/4 = 3$. So $A = \sqrt{3}$.
For $B$, $z=e^{i\pi/6}$.
$z^2 = e^{i\pi/3} = 1/2 + i\sqrt{3}/2$.
$1 - z + z^2 = 1 - (1/2 + i\sqrt{3}/2) + (-1/2 + i\sqrt{3}/2) = 1 - 1 - i\sqrt{3} = -i\sqrt{3}$?
No, $-z$ term. $1 - e^{i\pi/6}$. $e^{i\pi/6} = \frac{1+i}{\sqrt{3}}$. No.
$e^{i\pi/6} = \cos(\pi/6) + i\sin(\pi/6) = \frac{\sqrt{3}}{2} + \frac{i}{2}$.
So $1-z+z^2 = 1 - (\frac{\sqrt{3}}{2} + \frac{i}{2}) + (-\frac{\sqrt{3}}{2} - \frac{i}{2})$? No, $z^2 = e^{i\pi/3} = \frac{1+\sqrt{3}i}{2}$?
$e^{i\pi/3} = \cos(\pi/3) + i\sin(\pi/3) = 1/2 + i\sqrt{3}/2$.
So $z^2 - z + 1$ is $0$ at $\theta=\dots$ no.
Let's recalculate $B$ for $\theta=\pi/6$.
$1-z+z^2 = 1 - (\frac{\sqrt{3}}{2} + \frac{i}{2}) + (-\frac{\sqrt{3}}{2} + \frac{i\sqrt{3}}{2})$? No.
Wait, $z = e^{i\pi/6}$. So $\cos(\pi/6) = \frac{\sqrt{3}}{2}$, $\sin(\pi/6)=1/2$.
Then $z^2 = e^{i2\pi/3} = -1/2 + i\sqrt{3}/2$? No.
$2\pi/3$ is $e^{i(2\pi/3)}$.
So $z=e^{i\theta}$, $z^2=e^{i2\theta}$.
So for $\theta=\pi/6$, $z^2 = e^{i\pi/3} = \frac{1}{2} + i\frac{\sqrt{3}}{2}$.
Then $1-z+z^2 = 1 - (\frac{\sqrt{3}}{2} + \frac{i}{2}) + (\frac{1}{2} + i\frac{\sqrt{3}}{2}) = 1 - \frac{\sqrt{3}}{2} - \frac{i}{2} + \frac{1}{2} + i\frac{\sqrt{3}}{2}$.
Real part: $1-1/2 - \frac{\sqrt{3}}{2} + \frac{\sqrt{3}}{2}$? No.
$1 - \frac{\sqrt{3}}{2} + \frac{1}{2} = 1 - 0.5\sqrt{3}$. Imaginary part: $-1/2 + \sqrt{3}/2 = (\sqrt{3}-1)/2$.
This term is not necessarily real or zero.
Let's calculate modulus.
Modulus squared: $(1 - \frac{\sqrt{3}}{2})^2 + ((\sqrt{3}-1)/2)^2$? No, $(-z)$ and ($z^2$) have same imaginary part sign?
$-z = -\frac{\sqrt{3}}{2} - i/2$.
$z^2 = \frac{1}{2} + i\frac{\sqrt{3}}{2}$.
Sum real: $1 - \frac{\sqrt{3}}{2} + 1/2 = 3/2 - \frac{\sqrt{3}}{2} = \frac{3-\sqrt{3}}{2}$.
Sum imag: $-1/2 + \frac{\sqrt{3}}{2} = \frac{\sqrt{3}-1}{2}$.
So magnitude squared is $\frac{1}{4}( (3-\sqrt{3})^2 + (\sqrt{3}-1)^2 ) = \frac{1}{4} (9 - 6\sqrt{3} + 3 + 3 - 2\sqrt{3} + 1)$.
$= \frac{1}{4} (16 - 8\sqrt{3}) = 4 - 2\sqrt{3}$.
This is approx $4 - 3.46 = 0.54$.
So $|B| = \sqrt{4-2\sqrt{3}}$. This is small.

Let's re-evaluate the value for $\theta$ near 1 radian? No, let's try a general approach.
We are maximizing $f(z) = |1+z| + |z^2-z+1|$.
Let's consider the geometric interpretation of this.
The term $T_2 = z^2-z+1 = (z-1/2)^2 - 3/4$? No.
Roots are $\frac{1 \pm i\sqrt{3}}{2}$. The value is related to these roots.
If we consider the triangle formed by $0$, $1+z$, and $1-z-z^2$? No.

Let's rewrite the second term in terms of polar angles.
We have $\theta$.
$T_2 = |1 - z(1+z)|$. Let's see if we can bound it.
Since $|z|=1$, we can write $|z| \le 1$.
So $T_2 \le |1| + |-z+z^2| = 1+|-i\sqrt{3}|$? No, let's use the triangle inequality:
$|A+B| \le |A|+|B|$. Here $A=1, B=z(1-z)$?
So $|z^2-z+1| = |z^2-z+z(z-1)| + |-z+z|$? No.
Let's just use the triangle inequality properly:
$|1 - z + z^2| \le 1 + |-z + z^2|$.
We want to bound $|-z + z^2| = |z(1-z)|$? No, $|z^2| = 1$.
So $|1 - z + z^2| \le 1 + |z(z-1)|$? No.
Actually $|A+B| \le |A|+|B|$. So we need to find the best lower bound for $|z-z^2|$ or similar.
However, note that $1 - z + z^2 = 1 - z(1-z)$.
We know that for any unit vector $z$, the quantity $1 - \cos\theta + i\sin\theta$ has modulus.
Let's use the polar form of the roots again.
The maximum value of $|w|$ on the circle $|w-1|=1$? No, we have the circle $|z|=1$.
The expression is $|1+z| + |z^2-z+1|$.
Let's define vectors $\mathbf{u} = 1+z$, $\mathbf{v} = z^2 - z + 1$.
This doesn't simplify to standard unit circle.

Let's go back to basic algebraic inequality on $T_2$.
$T_2^2 = (1-z+z^2)(\overline{1-z+z^2}) = |1-z+z^2|^2$.
We can expand this as $(1-\bar{z}+z^2)\dots$? No.
Consider the function $g(\theta) = \sqrt{2+2\cos\theta} + |1 - e^{i\theta} + e^{i2\theta}|$.
Is it possible that the maximum is attained at $\theta = \pi/3$?
Let's check $\theta=\pi/3$ again.
$\cos(\pi/3) = 1/2$. $z=e^{i\pi/3}$.
$T_1^2 = (1+1/2)^2 + (\sqrt{3}/2)^2 = 9/4 + 3/4 = 3$. So $|T_1|= \sqrt{3}$.
$T_2$: $z=e^{i\pi/3}$, $\cos=1/2, \sin=\sqrt{3}/2$.
$z^2 = e^{i2\pi/3} = \cos(120^\circ) + i\sin(120^\circ) = -1/2 + i\sqrt{3}/2$.
$T_2 = 1 - z + z^2 = 1 - (\frac{\sqrt{3}}{2} + i\frac{1}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})$.
Real part: $1 - 0.5(\sqrt{3}) + 0.5 = 1.5 - \frac{\sqrt{3}}{2}$? No, this is wrong.
$1 - (\frac{\sqrt{3}}{2} + i\frac{1}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})$.
Real parts: $1 - \frac{\sqrt{3}}{2} - \frac{1}{2} = \frac{1-\sqrt{3}}{2}$. No. $1 - 0.5(\sqrt{3}) + 0.5$?
Let's check: $\text{Re}(1) = 1$. $\text{Re}(z^2)$ is real part of $-1/2 + i\sqrt{3}/2$.
So Real(T2) = $1 - \cos\theta + \sin(2\theta)$? No, that's not true.
$1 - z + z^2$. $\text{Re}(1-z+z^2) = 1 - x + \cos(2\theta)$.
$\cos(\theta) = 1/2$. $x = 1/2$. So Real part = $1 - 0.5 + (-1/2)$? No.
$z^2$ has real part $\cos(2\theta) = \cos(\pi/3) = 1/2$.
So Real(T2) is $1 - x + (1/2)$ if we are using polar form. But $x$ is the real part of $z$.
If $z=e^{i\pi/3}$, then $x = \cos(\pi/3) = 1/2$, $y = \sin(\pi/3) = \sqrt{3}/2$.
Then $1 - z + z^2 = (1 - x + y)$? No.
Let's just use complex arithmetic.
$z = \frac{1}{2} + i\frac{\sqrt{3}}{2}$.
$z^2 = \cos(\pi/3) + i\sin(\pi/3)$?
No. $z = e^{i2\pi/6} = e^{i\pi/3}$. Wait, $\theta=\pi/6$.
Then $z=e^{i\pi/6}$. Real part $\frac{\sqrt{3}}{2}$. Imaginary part $\frac{1}{2}$.
$z^2 = e^{i\pi/3} = \cos(\pi/3) + i\sin(\pi/3) = 1/2 + i\frac{\sqrt{3}}{2}$.
So $1 - z + z^2 = 1 - (\frac{\sqrt{3}}{2}) + (-i\frac{\sqrt{3}}{2})$? No.
Real part: $1 - \frac{\sqrt{3}}{2} + 0.5$. So $\frac{3-\sqrt{3}}{2}$?
No, wait. I think the previous calculation of magnitude was wrong because I assumed signs.
Let's re-calculate carefully.
$z = e^{i\pi/6}$. Then $x=\cos(\pi/6)=\frac{\sqrt{3}}{2}$, $y=\sin(\pi/6)=\frac{1}{2}$.
Then $T_2 = 1 - z + z^2 = 1 - (\frac{\sqrt{3}}{2} + i\frac{1}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})$? No, this is incorrect.
$z^2$ has $\cos(2\pi/6) = \cos(\pi/3)=1/2$ and $\sin(2\pi/6)=\sin(\pi/3)=\sqrt{3}/2$.
So $T_2 = (1 - 1/2) + (-i/2 + i\sqrt{3}/2)$? No.
The coefficients are:
Real part of $T_2$: $1 - (\frac{\sqrt{3}}{2}) - \frac{1}{2}$. This is $\frac{3-\sqrt{3}}{2}$.
Imaginary part of $T_2$: $-0 + \frac{\sqrt{3}}{2}$? No.
$-z = -(\frac{\sqrt{3}}{2} + i\frac{1}{2})$. Imaginary part is $-\frac{1}{2}$.
$+z^2 = (\frac{1}{2} + i\frac{\sqrt{3}}{2})$. Imaginary part is $\frac{\sqrt{3}}{2}$.
Sum of imaginary parts: $-0.5 + 0.866 = 0.366 > 0$.
Sum of real parts: $1 - 0.866 - 0.5 = 0.5(1-2) + \dots$? No.
Real part sum: $1 - 0.866 - 0.5$. This is $\frac{3-\sqrt{3}}{2} \approx 0.16$.
So $T_2 \approx 0.16 + i0.37$.
The magnitude of $T_2$ seems small (maybe less than 2).

Wait, did I calculate the imaginary part correctly?
$-z = -\frac{\sqrt{3}}{2} - i\frac{1}{2}$. Imaginary part is $-0.5$. Correct.
$z^2 = \cos(2\pi/6) + i\sin(2\pi/6)$? No, wait. $z=e^{i\theta}$ where $\theta=\pi/6$. So $z^2=e^{i\pi}e^{i2\pi/3}$? No.
$z = e^{i\pi/6}$. Then $z^2 = e^{i2\pi/6} = e^{i\pi/3} = \frac{1}{2} + i\frac{\sqrt{3}}{2}$. Correct.
Then the imaginary part of $z^2$ is $\sqrt{3}/2 \approx 0.866$.
The real part of $z^2$ is $0.5$.
Imaginary part of $-z$ is $-1/2 = -0.5$. Real part is $\frac{\sqrt{3}}{2} \approx 0.866$. No, imag of $-z$ is $-y$ if we just take vector subtraction.
So imaginary part is $-y + z_{y}$.
$T_2$ has real part: $(1+x) + y^2 - (x + y) = 1+x+y^2-x-y$? No.
Let's use the expansion for $|1-z+z^2|$:
If we assume it is small, then maybe my assumption about magnitude is too big.
However, the maximum value of a sum involves checking the boundaries.

Let's try to maximize numerically.
Consider $\theta$ such that $T_1$ and $T_2$ align or something?
Maybe max occurs at $\theta = \pi$. Then $z=-1$.
Then $A=0$ (since $|1-1|=0$, but it's $\sqrt{(1+(-1))^2} = 0$).
$B = |1 - (-1) + (-1)^2| = |3| = \sqrt{9} = 3$.
Sum = 3.
Is this a local maximum? No, if $A$ is large (2), and $B$ is small, sum can be large.
At $\theta = \pi/2$, $z=i$. $A=\sqrt{2}$.
$T_2 = |1-i+(-1)| = |-i| = 1$. Sum $\approx 2.414$.
If we try to increase, maybe at $\theta = -\pi/2$? Same as $\pi/2$.
What if $z=i$, sum is $\sqrt{2}+1 \approx 2.414$.
Let's check $z=0$? No $|z|=1$.
Is there any point where $T_2$ is very large, or $A$ is small?
We found at $z=-1$, sum is 3. At $\theta=\pi/2$, sum is $\approx 2.41$. At $\theta=0$, sum is 3.
At $\theta=\pi/6$, we got something smaller.

Let's re-evaluate the function for $z=e^{i\theta}$.
We are looking for $M = \max_z (|1+z| + |z^2-z+1|)$.
Let's express everything using polar coordinates $\phi$ such that $1+z = R_1 e^{i\alpha}$? No.
Let $T_1(\theta) = |1+z|$ and $T_2(\theta) = |1-z+z^2|$.
We need to maximize $f(\theta)$.
$f(0) = 2+1 = 3$. (Since $\cos(0)=1$).
$f(\pi/2) = \sqrt{2} + 1 \approx 2.414$.
$f(\pi/3)$? $z=e^{i\pi/3}$, $x=1/2, y=\sqrt{3}/2$.
$A = \sqrt{(3/2)^2 + (\sqrt{3}/2)^2} = \sqrt{9/4+3/4} = \sqrt{3} \approx 1.732$.
$B = |1 - e^{i\pi/3} + e^{i2\pi/3}|$? No, $z^2=z^2$ is just $e^{i\theta}$.
Let's recompute $B(\pi/3)$. $T_2(0.5) = |1 - (\frac{\sqrt{3}}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})|$. No, this was for $\theta=\pi/6$.
Let's do it properly.
$z = \cos(\pi/6) + i\sin(\pi/6)$ (No, angle $\pi/6$).
Then $B(0) = 1 - e^{i\pi/6} + e^{i\pi/3}$? No, this is $\theta$.
If $z=e^{i\theta}$:
$A(\theta) = \sqrt{1+2\cos\theta}$.
$B(\theta) = |1 - z(1+z)|$? No.
The term is $|1-z+z^2|$.
Let's check if there is an identity for this.
Notice that $\text{Re}(1-z+z^2)$ and $\text{Im}(1-z+z^2)$ might be involved.
Is it possible to relate this to a geometric problem?
Consider points $P_1 = 1$, $P_2 = z$, $P_3 = z^2$. We are measuring distances from origin? No.
Actually, let's try to use the property that on the unit circle $|1+z|^2 + |1-z+z^2|^2$ might be minimized/maximized?
Or maybe $T_1 + T_2 \le 3\sqrt{...}$.

Let's try substituting specific values from the options (like angles).
We found $\theta=0 \implies z=1$, sum = 3.
$\theta=\pi/2 \implies z=i$, sum $\approx 2.414$.
$\theta=\pi \implies z=-1$, sum = 3.
What if we take a value where the modulus is small but real part is large?
For $A$ to be small, we need $\cos\theta$ close to $-1$ (so $z \approx -1$) or close to 0 ($z=0$ not allowed).
If $z \to -1$, $T_1 \to 0$. But $T_2 \to 3$. Sum $\to 3$.
So sum is 3.
At $z=i$, sum is 2.414? Let's check this again.
$A = |1+i| = \sqrt{1^2+1^2} = \sqrt{2}$.
$B = |-i| = 1$.
Sum $\approx 2.414$.
Is it possible to get a larger value?
Let's check if $z$ can be such that $\cos\theta$ is maximized for $T_1$, i.e., $\theta \to 0$ ($z=1$), sum = 3.
At $\theta=0$, sum=3.
What about at $\theta=-\pi/2$? Same as $\pi/2$.
Is there any $\theta$ where $A$ is small? No, min A is 0 (at $z=-1$).
At $z=-1$, sum = 3.
So we have a range of values between 3 and $\approx 2.41$.
Maybe the maximum is 3.

Let's double check my arithmetic at $\theta=0$ and $\pi/2$.
$\theta=0 \implies z=1$. $|1+z| = |2|=2$. $|1-z+z^2| = |1-1+1|=1$. Sum=3.
$\theta=\pi/2 \implies z=i$. $|1+z| = |1+i| = \sqrt{2}$. $|1-z+z^2| = |-i| = 1$. Sum $\approx 2.414$.
Is there any other critical point?
Let's check the function values for different angles.
At $\theta=\pi/3$:
$z=e^{i\pi/3} = 1/2 + i\sqrt{3}/2$.
$A^2 = (1+0.5)^2 + (\sqrt{3}/2)^2 = 2.25 + 0.75 = 3$. $A=\sqrt{3} \approx 1.732$.
$B^2$: Real part is $1 - x + x_2$. Imaginary part is $y_2 - y_1$.
Let's calculate $B$ again properly.
$z = \frac{1+i\sqrt{3}}{2}$.
$z^2 = e^{i2\pi/3} = \frac{-1 + i\sqrt{3}}{2}$.
Then $1-z+z^2 = 1 - \frac{\sqrt{3}+i}{2} - \frac{1-i\sqrt{3}}{2} = 1 - \frac{\sqrt{3}+1}{2} - i\frac{\sqrt{3}-1}{2}$?
Real part: $1 - \frac{\sqrt{3}+1}{2}$. Imaginary part: $\frac{-\sqrt{3} + \sqrt{3}}{2} = 0$?
No, imaginary part of $z^2$ is $\sqrt{3}/2$.
So Real(T) = $1 - (\frac{\sqrt{3}+1}{2}) + 0$? No.
Let's just calculate using the values: $x=1/2$, $y=\sqrt{3}/2$.
$T_2 = (1-x+y^2-xy)$? No.
The imaginary part of the expression is determined by $\sin(\theta) + \sin(2\theta)$ or something.
Let's recalculate $B$ for $\theta=0$ again to be sure.
If $\theta=0$, $x=\cos 0 = 1$, $y=0$.
Then $1 - z + z^2 = 1 - 1 + 1 = 1$. So $|B|=1$. Correct.

What about if we consider $\theta$ very large? No, unit circle is finite.
So let's check the derivative or geometry condition for maximum.
We have a function of $x,y$.
$f(x,y) = \sqrt{(1+x)^2+y^2} + |1 - x+iyz^2|$.
Since we maximize $f$, we want to see if $A+B$ can be greater than 3.
We found 3 and $\approx 2.41$. Let's check for any possibility of larger values.
Maybe I should calculate the maximum of the sum algebraically.
Consider vectors $\mathbf{u} = z-1$, $\mathbf{v} = z+1$? No.
We want to maximize $|1+z|$ and $|z^2-z+1|$.
The second term is related to a geometric mean?
Let's look at the term $B$. Is it possible that for some $z$, $|1-z+z^2| = |z^2-z+1| = \sqrt{3}$?
At $\theta=0$, $B=1$. Max of $B$ is 1? No, let's check.
Roots of $z^2-z+1$: $\omega, \bar{\omega}$. Magnitude is 1.
We want to maximize $|1 - z + z^2|$.
Let's rewrite $|1-z+z^2| = |z^2-z+1|$.
The roots of this are $\frac{1 \pm i\sqrt{3}}{2}$. These correspond to $e^{i2\pi/6}$ and $e^{-i2\pi/6}$.
Let's check the angle of these points. They are $e^{\pm i 2\pi/3}$.
These are points on the unit circle?
$|z^2-z+1|$ is the distance between origin, $z$ and $z^2$ shifted by something?
No, it's a complex number.
Actually, let's look at the triangle formed by $1$, $z$, $z^2$.
If we plot points in the complex plane: $P_1=1$, $P_2=z$, $P_3=z^2$.
The value of $B$ is the length of the vector connecting $1, P_3, P_2$? No.
It's just the modulus of a linear combination of points.
The function $z \mapsto |z^2-z+1|$ is convex/monotonic on circle?
Wait, let's look at the maximum value of $|z^2-z+1|$.
Let $f(z) = z^2-z+1$. Then $f(e^{i\theta}) = e^{i2\theta} - e^{i\theta} + 1$.
We want to maximize this modulus.
The roots of $z^2-z+1$ are $\omega, \bar{\omega}$ where $\omega = e^{i 2\pi/3}$?
No, roots of $x^2-x+1=0$ are $\frac{1 \pm i\sqrt{3}}{2}$.
The modulus is 1.
So $B$ is on the unit circle? No.
Actually $B(\theta)$ takes values such that $|B| \le 1 + |z^2-z|$? No.
If we take $\theta = \pi$, $z=-1$. Then $B = |1 - (-1) + 1| = |3| = 3$. This contradicts my previous calculation of $B$ being small or constant.
Let's re-check $B$ for $z=-1$.
$z=-1$. $z^2=1$.
$1 - z + z^2 = 1 - (-1) + 1 = 3$. Modulus is 3.
This was based on calculation error earlier? Wait, in $\theta=\pi$, $\cos\pi=-1$, $\sin\pi=0$.
If $z=-1$, then $x=-1$, $y=0$.
Then $A^2 = (1-1)^2 + 0^2 = 0$. $|A|=0$.
$B^2 = (1-(-1)+(-1))^2 = 3^2 = 9$. $|B|=3$.
So at $\theta=\pi$, sum is 3.
At $\theta=0$, sum is 3.
At $\theta=\pi/2$, sum is $\approx 2.414$.

What if we maximize using the triangle inequality?
$|A+B| \le A + B$. We know $B$ can be up to 3 (if $z=-1$). But at that point, $A=0$. So sum is small.
To get large sum, we need both terms to be non-zero and close to each other? No, to maximize sum, usually we want them to not interfere much, but if they have same phase they cancel or add?
Let's consider $z$ such that $\theta$ is small.
If $A \approx 2$, $B \approx 1$. Sum $\approx 3$.
Is it possible that one of the terms is large, say $|A|=1$, and $|B|$ is close to 2?
Let's check if $|A|$ can be 1. $|1+z|=1 \implies |z+1|=1$. This implies $z=-1$ or something else.
If $z=-1$, sum=3. If $z=i$, sum $\approx 2.41$. If $z=\sqrt{-1}$, $z^2=0$. Then $B = |-i - i| = |-2i| = 2$? No.
Let's check other points.
If $z$ is real number on circle (so $z \in [-1,1]$). $z \in \mathbb{R}$ implies $y=0$, so $z=x$. Then $x^2=1 \implies x=\pm 1$. So $A = |1 \pm 1| = 2$ or $0$. If $z=-1$, $A=0$, sum=3.
If $z$ is purely imaginary, $A=|1 \pm i|$. Max is $\sqrt{2}$. Then $B=|-i|=1$. Sum $\approx 2.414$.

Is there any point with higher values?
Let's try to express $B$ as $|e^{i\alpha} - z(1+z)|$? No.
Let's check the maximum of $A+B$ subject to $z \in \text{unit circle}$.
If we fix $\theta$, let's just evaluate for a grid or similar.
$\theta = 0 \implies A=2, B=1 \implies \sum = 3$.
$\theta = \pi/2 \implies A=\sqrt{2}, B=1 \implies \sum = \sqrt{2}+1 \approx 2.41$.
$\theta = \pi/6 \implies A=\sqrt{3}, B \approx 0.54$ (calculated earlier? Let's recheck).
Re-evaluate $B(\pi/6)$.
$z = e^{i\pi/6} = \frac{1+i}{2}$? No, $\cos=1/2, \sin=\sqrt{3}/2$.
So $x=1/2, y=\sqrt{3}/2$.
Wait, earlier I wrote $\theta=\pi/6$ as angle.
But let's check if I made a mistake in the polar form calculation for $B(\pi/6)$.
$z = e^{i\pi/6}$. $x=1/2$.
$A^2 = (1+1/2)^2 + (\sqrt{3}/2)^2 = 9/4 + 3/4 = 3$. $|A|=\sqrt{3} \approx 1.732$.
$z^2 = e^{i\pi/3} = 1/2 + i\sqrt{3}/2$.
Then $B^2 = |1 - x + z^2|^2$? No. $B^2 = |1-z+z^2|^2$.
Using $\cos\theta=0$, $\sin\theta=0$? No, $\pi/6$ gives 30 degrees.
Wait, $\cos(\pi/6)=\sqrt{3}/2 \neq 0$. So $A$ is not related to 0 directly.
Let's recalculate $B$ for $\theta=\pi/6$.
$x=1/2$.
$z^2 = e^{i\pi/3} = 1/2 + i\sqrt{3}/2$.
Then $1-z+z^2 = (1 - x) + z^2 - z$. No, this is not right.
Let's just do: $1-z+z^2$.
$z^2 = e^{i\theta} \cdot e^{i2\theta}$? No. $z=e^{i\theta}$.
So $z^2 = e^{i2\theta}$.
$B^2 = |1 - z + z^2|^2$.
With $\theta=\pi/6$, $x=1/2, y=\sqrt{3}/2$.
$1-z+z^2 = 1 - (\frac{1+i\sqrt{3}}{2}) + (-\frac{\sqrt{3}+i}{2})$? No.
Let's just use the formula: $A^2+B^2$.
Let's go back to $B^2$ in terms of $\cos(\theta)$ and $\sin(\theta)$.
We have $1 - z + z^2 = 1 - x - i y + (-x^2/4?)$
````

## Answer (content)

````text

````
