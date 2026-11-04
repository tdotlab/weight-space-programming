# test/intermediate_algebra/1806.json (Intermediate Algebra, level 5)

> Let $z$ be a complex number such that $|z| = 1.$  Find the maximum value of  
> \[|1 + z| + |1 - z + z^2|.\]  

**Wrong.** Gold `\frac{13}{4}`, predicted `None`. Finish: length, 8192 tokens, 0 waits, 665.3 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Let $f(z) = |1 + z| + |1 - z + z^2|$ where $z$ is a complex number with $|z|=1$. We want to maximize this value.  
Since $|z|=1$, we can write $z = e^{i\theta}$ for $\theta \in [0, 2\pi)$.  
Let's express the terms in absolute values.  
$|1 + z| = |e^{i\theta/2} + e^{i(\theta-\phi)}|$? No, let $z=e^{i\theta}$.  
$|1 + e^{i\theta}| = |e^{-i\theta/2}(e^{i\theta/2} + e^{-i\theta/2})| \dots$ no.  
$|1+z| = |e^{i\phi} (z-e^{i\pi})|$?  
Let's use the standard expansion $|a+b|^2 = |a|^2+|b|^2+2\text{Re}(ab^*)$. Since $z=e^{i\theta}$, $\bar{z}=1/z=e^{-i\theta}$.  
$|1+z|^2 = (1+z)(1+\bar{z}) = 1 + z + \bar{z} + 1 = 2 + 2\cos\theta = 4\cos^2(\theta/2)$.  
So $|1+z| = 2|\cos(\theta/2)|$.  
Also, for $|z|=1$, $\theta$ ranges from $0$ to $2\pi$. The cosine term is non-negative in $[0, \pi)$ and non-positive in $(\pi, 2\pi]$. So the maximum of $|\cos|$ is 1 when $\theta/2 = k\pi$, i.e., $\theta = 2k\pi$. But then $z=1$, and $|1+z|=2$.  
If $z=-1$, $\theta=\pi$, $|1+z|=0$. If $z=i$, $\theta=\pi/2$, $|1+i|=\sqrt{2}$.  

Now consider the second term: $|1 - z + z^2|$.  
$|1 - z + z^2|^2 = (1 - z + z^2)(1 - \bar{z} + \bar{z}^2)$.  
Since $\bar{z} = 1/z$, this is $(1 - z + z^2)(1 - 1/z + 1/z^2) = (z^2 - z + 1)(z^{-2} - z^{-1} + 1) / |z|^4$? No, let's just expand.  
The denominator is $z \bar{z} \dots$ no.  
Let's use the geometric interpretation. $|1+z|$ is distance from $-1$ to $z$. Since $|z|=1$, it's chord length.  
$|1 - z + z^2| = |1 - (z-z^2)|$? No, that's not simplifying much.  
Let's factor out something?  
If we treat the argument inside modulus as complex numbers:  
$1+z = e^{i\alpha}(z-z_0)$? No.  
Let's use $\cos(\theta/2)$. $|1+z| = 2|\cos(\theta/2)|$.  
Let $w = -z + z^2 = z(z-1)$. Then we have $|1+z+w|$.  
$1 - z + z^2 = (1-z) + z^2$.  
Is there a geometric interpretation of the points?  
Let $A=1$, $B=z$. $|AB|$ is distance from 0 to $z$? No, it's $|1+z|$.  
$C=1, D=z, E=0$. $|D+C|$? No.  
The term is $|1-z| + |z-(-1)|$ in some sense? No.  
Let $f(\theta) = 2|\cos(\theta/2)| + |1 - e^{i\theta} + e^{2i\theta}|$.  
Let's simplify the second term:  
$|1 - z + z^2| = |(z^2+z-1)/?|$ No.  
$|1-z+z^2| = |-(z-e^{-i\theta})(something)|$?  
Let $x = e^{i\theta}$. We want to maximize $|1+x| + |1-x+x^2|$.  
Note that $1-x+x^2 = \frac{1-(-x)^3}{1+x}$? No.  
$x^3 - x^2 + x - 1$? No.  
Let's use the factorization of quadratic.  
$z^2 - z + 1 = (z - e^{i\pi/3})(z - e^{-i\pi/3})$ ?  
Roots of $t^2 - t + 1 = 0$ are $e^{\pm i\pi/3}$? No.  
$t = \frac{1 \pm \sqrt{1-4}}{2} = \frac{1 \pm i\sqrt{3}}{2} = e^{\pm i\pi/3}$.  
So $|1-z+z^2| = |z-e^{i\pi/3}| \cdot |z-e^{-i\pi/3}|$? No.  
The roots of $z^2 - z + 1 = 0$ are $\omega = e^{i\pi/3}$ and $\bar{\omega} = e^{-i\pi/3}$.  
So $z^2 - z + 1 = \omega(z-\bar{z})$? No.  
It is $(z-\omega)(z-\bar{\omega})$.  
Then $|z^2-z+1| = |z-\omega||z-\bar{\omega}|$.  
$\omega = e^{i\pi/3} = \cos(60^\circ) + i\sin(60^\circ)$.  
$|\omega|=1$.  
Also $\bar{\omega}$ is on unit circle.  
Since $|z|=1$, $z$ can be written as $e^{i\theta}$.  
We want to maximize $g(\theta) = |1+e^{i\theta}| + |1-e^{i\theta} + e^{2i\theta}|$.  
Let's rewrite the arguments.  
The roots of unity are special.  
$z^2 - z + 1 = \frac{z^3-1}{z-1}$. This is true if $z \neq 1$.  
So $|1-z+z^2| = \left|\frac{z^3-1}{z-1}\right|$ for $z \neq 1$.  
For $z=1$, the second term is $|1-1+1| = 1$. The first term is $|1+1|=2$. Sum is 3.  
Let's check the formula: $\lim_{z\to 1} \frac{z^3-1}{z-1} = 3$. Correct.  
So we want to maximize $h(z) = |1+z| + |\frac{z^3-1}{z-1}|$.  
$|1+z| = |z-(-1)|$. This is distance between $z$ and $-1$.  
$|1-z+z^2|$ is distance related? No, it's $|\frac{z(z^2+z)-1}{z-1}|$? No.  
It's $\left|\frac{z^3-1}{z-1}\right|$. Let's use this form.  
Let $u = z^3 - 1$. The second term is $\frac{|u|}{|z-1|}$.  
So we want to maximize $|z+1| + \frac{|z^3-1|}{|z-1|}$.  
Note that $|z^3-1|$ is $|e^{3i\theta}-1|$. This depends on $z$ only via its angle.  
Also $|z+1|^2 = |e^{i\theta}+1|^2 = 2 + 2\cos\theta = 4\cos^2(\theta/2)$. So $|z+1| = 2|\cos(\theta/2)|$.  
And $\frac{|z^3-1|}{|z-1|} = \left|\frac{z^3-1}{z-1}\right|$.  
Let's simplify $\frac{z^3-1}{z-1}$. Let $z=e^{i\theta}$.  
$\frac{z^3-1}{z-1} = \frac{(z-1)(z^2+z+1)}{z-1} = z^2+z+1$.  
Ah, I made a mistake. $\omega = e^{i\pi/3}$ and $e^{-i\pi/3}$.  
Roots of $z^2-z+1$ are not unit roots?  
Let's check: $r^2-r+1=0 \implies r = (1 \pm i\sqrt{3})/2 = \cos(60^\circ) \pm i\sin(60^\circ) = e^{\pm i\pi/3}$. Yes, roots are on unit circle.  
So $z^2 - z + 1 = (z-e^{i\pi/3})(z-e^{-i\pi/3})$. This factorization holds for complex numbers $e^{i\pi/3}$.  
But earlier I wrote $\frac{z^3-1}{z-1} = z^2+z+1$. Yes, this is a well known identity.  
So $1-z+z^2$ is not the factorization of something simple with roots on unit circle directly like that.  
The term we have is $|1 - z + z^2|$.  
Using the identity $\frac{z^3-1}{z-1}$:  
$\frac{z^3-1}{z-1} = 0$ if $z^3=1$, i.e., $z=1, \omega_1=e^{2\pi i/3}, \omega_2=e^{4\pi i/3}$.  
If $z=1$, value is $1-z+z^2 = 1-1+1=1$. Formula gives $\lim = 3(1) = 3$? No. $|z^3-1|/(z-1)$ is distance from $0$ to 1 on circle divided by distance from 1 to $z$?  
Let's re-evaluate the term $|1-z+z^2|$.  
We have two cases:  
Case 1: $z=1$. Value is 1. Total sum = $2+1=3$.  
Case 2: $z \neq 1$. We know that if $|z|=1$, then $\frac{1-z+z^2}{1+z} \dots$? No.  
Let's stick to the form $|1+z| + |\frac{z^3-1}{z-1}|$. This requires $z \neq 1$.  
Is it equal?  
$\frac{z^3-1}{z-1} = z^2+z+1$.  
Then $|1-z+z^2| = |-(z-1)(z-(-1/2) + i\dots)|$ No.  
Let's factor $z^2 - z + 1 = (z-e^{i\pi/3})(z-e^{-i\pi/3})$.  
So $|1-z+z^2| = |e^{i\theta} - e^{i\pi/3}| \cdot |e^{i\theta} - e^{-i\pi/3}|$? No.  
The roots are complex conjugate. $z^2 - z + 1 = (z-\omega)(z-\bar{\omega})$ where $\omega = e^{i\pi/3}$.  
So $|1-z+z^2| = |\omega|^0 |e^{i(\theta-2\pi/3)}| \dots$ No.  
Let's just use polar coordinates for each term.  
Term 1: $T_1 = |1+e^{i\theta}|$. As established, $T_1 = 2|\cos(\theta/2)|$.  
Term 2: $T_2 = |1 - e^{i\theta} + e^{2i\theta}|$.  
$T_2 = |(1 + z + z^2)$? No.  
If I substitute $z = \frac{1-z+z^2}{?}$ no.  
Let's try to express $1 - z + z^2$.  
$z^3 - 1 = (z-1)(1-z+z^2)$.  
So $|1-z+z^2| = |\frac{z^3-1}{z-1}| = |e^{i3\theta}-1| / |e^{i\theta}-1|$ (for $z \neq 1$).  
Let's verify this. $z=e^{i\theta}$.  
LHS: $|1-e^{i\theta}+e^{2i\theta}|$.  
RHS: $|\frac{e^{3i\theta}-1}{e^{i\theta}-1}|$.  
Numerator: $| \cos(3\theta) - i\sin(3\theta) - 1 | = | (\cos(3\theta)-1) - i\sin(3\theta) | = \sqrt{(-2\sin^2(3\theta/2))^2 + (-2\cos^2(3\theta/2)\sin(3\theta/2)?) }$.  
Let's use half angles. $e^{i\alpha}-1 = e^{i\alpha/2}(e^{i\alpha/2}-e^{-i\alpha/2}) = e^{i\alpha/2} 2i\sin(\alpha/2)$.  
So $|e^{i3\theta}-1| = |2i\sin(3\theta/2)| e^{-i3\theta/2}$? No, modulus is $|2\sin(3\theta/2)|$.  
And $|e^{i\theta}-1| = 2|\sin(\theta/2)|$.  
So $T_2 = \frac{2|\sin(3\theta/2)|}{2|\sin(\theta/2)|} = \left| \frac{\sin(3\theta/2)}{\sin(\theta/2)} \right|$.  
We can expand $\sin(3x) = 3\sin x - 4\sin^3 x$.  
So $\left| \frac{3\sin(x) - 4\sin^3(x)}{\sin(x)} \right| = |3 - 4\sin^2(x)|$ where $x = \theta/2$.  
Let's verify the expression for $T_1$.  
$T_1 = |1 + e^{i\theta}| = |1 + \cos\theta + i\sin\theta| = \sqrt{(1+\cos\theta)^2 + \sin^2\theta} = \sqrt{1+2\cos\theta+\cos^2\theta+\sin^2\theta} = \sqrt{2+2\cos\theta} = \sqrt{4\cos^2(\theta/2)} = 2|\cos(\theta/2)|$.  
Note $\sin(3x)/\sin(x) = \frac{\sin x \cdot (3 - 4\sin^2 x)}{\sin x} = |3 - 4\sin^2 x|$.  
So we want to maximize $f(\theta) = 2|\cos(\theta/2)| + |\frac{3\sin(3\theta/2) - 4\sin^3(\theta/2)?}{ \dots }|$ no.  
It is $T_2 = | \frac{\sin(3x)}{\sin x} |$ where $x=\theta/2$.  
Using $\frac{\sin 3x}{\sin x} = 3 - 4\sin^2 x = 3 - 4(1-\cos^2 x) = 4\cos^2 x - 1$.  
Or using half angles of $T_2$ directly:  
$\left| \frac{\sin(3x)}{\sin x} \right| = |3 - 4\sin^2 x| = |4\cos^2 x - 1|$.  
Let's check $z=1$. $\theta=0$, $x=0$. Limit is 3. Formula $|4(1)^2-1|=3$. Matches.  
So we want to maximize $g(\theta) = 2|\cos(x)| + |4\cos^2(x)-1|$ subject to $x \in [0, \pi/2]$.  
Why range is limited? $\theta \in [0, 2\pi]$, so $x \in [0, \pi]$.  
Since $\sin(\theta)$ and $\sin(3\theta)$ behave differently. But modulus depends on absolute value.  
Let's check the sign of $\frac{\sin 3x}{\sin x} = 4\cos^2 x - 1$? No.  
$\frac{\sin 3x}{\sin x} = 3 - 4\sin^2 x$.  
If $x \in [0, \pi/2]$, $\sin^2 x \in [0, 1]$.  
Then $3 - 4\sin^2 x$ goes from $3$ down to $-1$ and back up.  
So it can be negative. The modulus handles it.  
We want to maximize $h(x) = 2|\cos x| + |4\cos^2 x - 1|$ for $x \in [0, \pi/2]$.  
Note: $z=e^{i\theta} \implies x=\theta/2$. The term $\cos(\theta/2)$ could be negative for $\theta \in [\pi, 2\pi]$. But modulus is always non-negative.  
However, the factorization $|1-z+z^2|$ leads to $\frac{|z^3-1|}{|z-1|} = |\frac{e^{i3x}-1}{e^{ix}-1}|$ where $x=\theta/2$.  
If $x \in [0, \pi]$, then $\sin x \ge 0$. So $|e^{i\theta}-1| = |1-e^{i\theta}| = |\dots|$ depends on magnitude.  
The modulus calculation $|\frac{z^3-1}{z-1}|$ is correct for any $z$ on unit circle except $z=1$.  
So let's define $x \in [0, \pi]$. $T_1 = 2\cos x$ if $x \in [0, \pi/2]$ and $2(-\cos x) = -2\cos x$? No modulus is positive.  
$|1+z|^2 = 4\cos^2 x$. So $T_1 = 2|\cos x|$.  
If we consider $z=e^{i\theta}$, then $x=\theta/2$. As $\theta$ goes $0 \to 2\pi$, $x$ goes $0 \to \pi$.  
The term $T_2 = |4\cos^2 x - 1|$.  
Since $T_2$ involves modulus of something that is real? No, $z=e^{ix}$.  
$\frac{\sin(3x)}{\sin x} = 4\cos^2 x - 1$ ?  
Let's re-verify: $\sin 3x = \sin x (3 - 4\sin^2 x) = -\sin x (4\cos^2 x - 1)$. No.  
$\sin 3x = 3\sin x - 4\sin^3 x = \sin x (3 - 4(1-\cos^2 x)) = \sin x (4\cos^2 x - 1)$. Yes.  
So $T_2 = |4\cos^2 x - 1|$.  
$T_1 = 2|\cos x|$.  
We need to maximize $F(x) = 2|\cos x| + |4\cos^2 x - 1|$ for $x \in [0, \pi/2]$.  
Note that the domain of interest is $x \in [0, \pi/2]$ or we could use symmetry?  
$\theta$ goes from $0$ to $2\pi$. $x = \theta/2$ goes from $0$ to $\pi$.  
Let's analyze the function $k(u) = 2u + |4u^2 - 1|$ where $u = |\cos x|$. But $\cos x$ can be negative in $[\pi/2, \pi]$.  
Let's check the values for $x \in [0, \pi]$.  
Case A: $x \in [0, \pi/2]$. Then $\cos x \ge 0$, so $|\cos x| = \cos x$.  
$F(x) = 2\cos x + |4\cos^2 x - 1|$.  
Subcase A1: $4\cos^2 x - 1 \ge 0 \implies \cos x \ge 1/2 \implies x \in [0, \pi/3]$.  
Then $F(x) = 2\cos x + 4\cos^2 x - 1$. Let $t = \cos x$, $t \in [1/2, 1]$.  
$g(t) = 4t^2 - 1 + 2t = 4t^2 + 2t - 1$. This is increasing for $t \ge -1/4$. So max at right endpoint.  
At $t=1$, $F(\pi/3) = 4(1)^2 + 2(1) - 1 = 5$.  
Let's check endpoints: $x=\pi/3 \implies t=1/2$.  
$F(\pi/3) = 2(1/2) + 0 = 1$. No, formula for subcase was $4\cos^2 x - 1$. At $\pi/3$, it's $4(1/4)-1 = 0$. So sum is $2(1/2) + 0 = 1$.  
So we check max at critical points and boundaries.  
Subcase A1 boundary: $t=1$ ($x=0$). $F(0) = 2 + |-1| = 3$. This corresponds to $\theta=0$, $z=1$.  
At this point, $4\cos^2(0)-1 = 3$. Term 2 is 3?  
Let's check. $z=1 \implies |1+1| + |1-1+1| = 2+1=3$.  
Using formula: $2\cos(0) + (4(1)^2-1)$? No, subcase A1 is $\cos x \ge 1/2$.  
At $x=0$, $\cos x = 1 \ge 1/2$. So formula valid.  
But at $x=0$, $T_2 = |4(1)-1| = 3$? No, $z^3-1 / (z-1)$ is undefined limit?  
The original sum was $|1+z| + |1-z+z^2|$. At $z=1$, it is $2+1=3$.  
My formula for $T_2$ derived via trigonometric identity is valid everywhere except $z=1$?  
Let's check. $T_2 = |\frac{z^3-1}{z-1}|$.  
If $x \to 0$, $\frac{\sin 3x}{\sin x} \to 3$. So $T_2 \to 3$. But original sum is $2+1=3$.  
Why discrepancy? $T_1$ at $z=1$ is 2. My trig formula gave 2.  
So at $x=0$, $F(x) = 2(1) + (4(1)-1)$?  
If I use $\cos^2 x - 1/4$, then at $x=0$, it's $1-0.25=0.75$.  
Let's look at the expression derived: $T_2 = |4\cos^2 x - 1|$.  
At $x=\pi/3$ ($z=e^{i\pi/3}$), $\theta=60^\circ$.  
$z = \cos 60 + i \sin 60 = 1/2 + i\sqrt{3}/2$.  
$|1+z| = |3/2 + i\sqrt{3}/2| = \sqrt{9/4+3/4} = \sqrt{3}$? No. $|3/2 + i\sqrt{3}/2|^2 = (9+3)/4 = 3$.  
So $|1+z| = \sqrt{3}$.  
Formula $T_1 = 2|\cos(30^\circ)| = 2(\sqrt{3}/2) = \sqrt{3}$. Correct.  
$T_2$: At $z=e^{i\pi/3}$, $1-z+z^2 = (1/2)^2 - 1/2 + 1$ ? No.  
$1 - (\frac{1}{2} + i\frac{\sqrt{3}}{2}) + (\frac{1}{4} - \frac{i\sqrt{3}}{4})$.  
Real part: $1 - 1/2 + 1/4 = 3/4$. Imaginary part: $-\sqrt{3}/2 - \sqrt{3}/4$ no.  
$\sin(60) = \sqrt{3}/2$. $\sin^2(60)=3/4$.  
$z^2 = e^{i2\pi/3} = -1/2 + i\sqrt{3}/2$.  
$1-z+z^2 = (1-1/2+1/4) + i(-\sqrt{3}/2-\sqrt{3}/2)?$ No.  
Real: $1 - 1/2 + (-1/2) = 0$. Imaginary: $-\frac{\sqrt{3}}{2} + \frac{\sqrt{3}}{2} = 0$? No, $\bar{z}$ term is not involved in expansion of $z^2-z+1$ directly.  
Let's compute $z^2+z+1$ for $e^{i\pi/3}$ (which corresponds to roots of $z^2-z+1$?). No.  
Roots of $z^2-z+1=0$ are $\omega = e^{i\pi/3}$.  
So at $z=e^{i\pi/3}$, $z^2-z+1 = 0$. So $T_2 = 0$.  
My formula gave $T_2 = |4(1/2)^2 - 1| = 4/4-1=0$. Correct.  
So sum is $\sqrt{3} + 0 = 1.732$.  
Is that max? No, at $x=0$, sum is 3.  

Let's look at the function $g(x) = 2\cos x + |4\cos^2 x - 1|$ for $x \in [0, \pi/2]$.  
The range of $\cos x$ is $[0, 1]$.  
We have two branches:  
1. $x \in [0, \pi/3]$: $\cos x \ge 1/2 \implies 4\cos^2 x - 1 \ge 0$.  
Expression: $h_1(x) = 2\cos x + 4\cos^2 x - 1$.  
Let $u = \cos x \in [1/2, 1]$.  
$h_1(u) = 4u^2 + 2u - 1$.  
Max at $u=1$ (since increasing). Value at $u=1$ is $4+2-1=5$.  
This corresponds to $x=0$, $\theta=0$, $z=1$.  
Check value: $|1+1| + |1-1+1| = 2+1=3$. Why did I get 5?  
Ah. $u=\cos x$. At $x=\pi/3$, $u=1/2$.  
The function is quadratic in $u$.  
Is $u$ defined as $\cos x$ or $\cos(\theta)$?  
Let's re-evaluate $T_1 = 2|\cos(x)|$. Here $x=\theta/2$.  
If $z=1$, $x=0$, $T_1 = 2(1) = 2$.  
If $z=e^{i\pi}$, $x=\pi/2$, $T_1 = 2(0) = 0$.  
The quadratic is $4u^2+2u-1$? No.  
Let's check the term $|4\cos^2 x - 1|$ again.  
It was derived as $T_2$.  
$T_2 = |\frac{\sin 3x}{\sin x}| = |4\cos^2 x - 1|$.  
At $x=\pi/3$, $\theta=60^\circ$. $z=e^{i\pi/3}$.  
$T_2 = |4(1/4)-1| = 0$. Correct.  
$T_1 = 2|\cos(\pi/3)| = 2(1/2) = 1$.  
Sum at $\theta=60^\circ$ is $1 + 0 = 1$. Not 5.  
Where did I get the factorization error?  
Ah, in my analysis of subcase A1, I set $t=\cos x$. Then $T_2 = |4t^2-1|$.  
At $x=0$, $t=1$, so $T_2 = 3$ (since $|3|$). No.  
If $x=0$, $\theta=0$. $z=1$.  
Then $T_1 = 2(1) = 2$.  
$T_2 = |4(1)^2-1| = 3$?  
Let's check $T_2$ at $z=1$. $T_2 = |1-1+1| = 1$.  
My formula $|4\cos^2 x - 1|$ gives 3. Why?  
The identity $\sin 3x / \sin x = 3 - 4\sin^2 x = 4\cos^2 x - 1$ is correct.  
But this leads to $T_2 = 0$ at $x=\pi/3$.  
Does the limit $z=1 \implies T_2 = 1$ match $x \to 0$?  
If $\sin x \approx x$, then $T_2 \approx (3x - 4x^3)/x = 3 - 4x^2$.  
As $x \to 0$, limit is 3. But $T_2(1) = 1$.  
So the expression for $T_2$ is not simply $|4\cos^2 x - 1|$?  
Let's re-calculate $\frac{z^3-1}{z-1}$ at $z=e^{ix}$.  
$z^3-1 = e^{i3x}-1$. At $x=0$, $0/0$ limit is 3.  
But the original expression $|1-z+z^2|$ is not $\frac{z^3-1}{z-1}$?  
$1 - z + z^2 = \frac{1-z+z^2}{1}$. No, it's just that value.  
Let's factor $1-z+z^2$ as $\frac{-(z^3-1)}{z-1}$.  
So the expression is $|\frac{z^3-1}{z-1}|$?  
If $z=1$, numerator 0, denominator 0. Limit is 3.  
But actual value is $|1-1+1|=1$.  
Why is limit 3 different from actual value 1?  
The identity $\frac{z^3-1}{z-1} = z^2+z+1$ holds for $z \neq 1$.  
At $z=1$, $1-1+1 = 1$.  
$1^2+1+1 = 3$.  
So $\frac{z^3-1}{z-1}$ is discontinuous at $z=1$ if we consider the function $f(z) = z^2+z+1$.  
But $(z^3-1)/(z-1)$ goes to 3 as $z \to 1$.  
The term in problem is $|1-z+z^2|$.  
So at $z=1$, value is $|1| = 1$.  
At $z=e^{ix}$, if $z \neq 1$, then $1-z+z^2 = -(z-1)(1-z+z^2) / (-(1-z+z^2))$? No.  
Let's check factorization: $z^2-z+1 = (z-e^{i\pi/3})(z-e^{-i\pi/3})$.  
Also $1-z+z^2 = -(z-1)(1-z+z^2)$? No.  
$1-z+z^2$ is exactly the polynomial.  
Note that $\frac{z^3-1}{z-1} = \frac{(z-1)(z^2+z+1)}{z-1} = z^2+z+1$.  
And $1-z+z^2 = -(z^2+z-1)$? No.  
Let's check if $1-z+z^2 = - (z^3-1)/(z-1)$ for roots of unity.  
Let $z=e^{i\theta}$. $\frac{e^{3i\theta}-1}{e^{i\theta}-1} = e^{2i\theta} + e^{i\theta} + 1$.  
So $1-z+z^2 = -(e^{2i\theta} + e^{i\theta} - 1)$? No.  
The identity $\frac{z^3-1}{z-1} = z^2+z+1$ is correct.  
Thus $|1-z+z^2| = | \dots |$.  
We have to check relation between $1-z+z^2$ and the quotient.  
Is $1-z+z^2 = (z^{-1}-1)(\frac{z-1}{?})$ no.  
Let's check if $1-z+z^2 = -(z-1) + \dots$? No.  
$1-z+z^2$ has roots at $\omega, \bar{\omega}$. So $1-z+z^2 = (z-\omega)(z-\bar{\omega})$.  
Also $\frac{z^3-1}{z-1}$ has roots at 1, $\omega$, $\bar{\omega}$? No.  
Roots of $z^3-1$ are $1, e^{i2\pi/3}, e^{i4\pi/3}$.  
Roots of $z-1$ is 1.  
So $| \frac{z^3-1}{z-1} | = | \prod (z-z_k) | / |z-1|$? No, it's product of moduli if factors were linear? No.  
$\frac{z^3-1}{z-1} = z^2+z+1$. Roots are $-\omega, -\bar{\omega}$?  
Let's check roots of $z^2+z+1=0$. $z^2+z+1=0 \implies z  

## Answer

*(none: the token cap hit during thinking)*
