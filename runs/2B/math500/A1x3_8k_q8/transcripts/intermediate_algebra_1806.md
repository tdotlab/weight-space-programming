# test/intermediate_algebra/1806.json (Intermediate Algebra, level 5)

> Let $z$ be a complex number such that $|z| = 1.$  Find the maximum value of  
> \[|1 + z| + |1 - z + z^2|.\]  

**Wrong.** Gold `\frac{13}{4}`, predicted `None`. Finish: length, 8192 tokens, 9 waits, 666.9 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Let the given expression be $E(z) = |1 + z| + |1 - z + z^2|$. We are given that $z$ is a complex number with modulus 1, i.e., $|z|=1$. We want to maximize this quantity.  

Let $z = e^{i\theta}$ where $\theta \in [0, 2\pi)$.  
Then $E(z)$ becomes a function of $\theta$.  
$|1 + z| = |1 + e^{i\theta}|$.  
We know that for any complex number $w$, $|1+w|^2 = (1+w)(1+\bar{w}) = 1 + w + \bar{w} + |w|^2$. Since $|z|=1$, $\bar{z} = 1/z = e^{-i\theta}$.  
So $|1 + z|^2 = 1 + e^{i\theta} + e^{-i\theta} + 1 = 2 + 2\cos\theta = 4\cos^2(\theta/2)$.  
Thus, $|1 + z| = \sqrt{2(1+\cos\theta)} = \sqrt{4\cos^2(\theta/2)} = 2|\cos(\theta/2)|$.  

Now let's look at the second term: $|1 - z + z^2|$.  
$1 - z + z^2$ is a geometric series sum? No, it's related to roots of unity or cyclotomic polynomials.  
Note that $z^3-1 = (z-1)(z^2+z+1)$. This doesn't seem immediately helpful with the $|1-z+z^2|$ form.  
Let's use Euler's formula again.  
$1 - z + z^2 = 1 - e^{i\theta} + e^{2i\theta}$.  
The modulus is $|e^{2i\theta} - e^{i\theta} + 1|$.  
We can try to simplify the expression.  
Let's analyze the triangle inequality or maybe geometric interpretation.  
Consider the points in the complex plane. Let $P_0 = 1$, $P_1 = z$, $P_2 = z^2$.  
The points are related by rotations? No.  
Let's consider the values of the terms separately.  
Case 1: $\theta \in [0, \pi]$. Then $\cos(\theta/2) \ge 0$, so $|1+z| = 2\cos(\theta/2)$.  
For the second term, let's look at $1 - z + z^2$.  
Let $w = 1-z+z^2$.  
$z^2 - z + 1 = \frac{z^3+1}{z+1}$ is false because $(z^3+1)/(z-1) = z^2+z+1$.  
The sum is $1 + z + z^2$? No.  
If $z^3=1$, then $z^2+z+1=0$, so $|1-z+z^2|$ might be related to something else.  
Actually, $|z^3-1| = |z-1||z^2+z+1|$ if we factor $z^3-1$.  
But the expression is $1 - z + z^2$.  
Note that $z^2 - z + 1 = -(z-1/2)^2 + \frac{5}{4}?$ No.  
Let's just evaluate $|1 - e^{i\theta} + e^{2i\theta}|$.  
Using the formula derived for $|1-z+z^2|$?  
We know that $|1-z+z^2|^2 = (1-z+z^2)(1-\bar{z}+\bar{z}^2) = 1 - z + z^2 - \bar{z} + |z|^2(1+z) + \dots$ No, this is messy.  
Let's use the cosine expansion again.  
$(1-e^{i\theta}+e^{2i\theta})(1-e^{-i\theta}+e^{-2i\theta})$  
This is $|1 - z + z^2|^2$.  
Also note that $\frac{1-z+z^2}{z-1}$?  
Actually, $1 - z + z^2 = -(z - 1/2)^2 + \dots$ No.  
Let's rewrite the term in terms of half angles or something.  
We know $|1+z| = |z^2+1|$ is not quite right because $z^3-1$.  
However, $z^3=1$ implies $1-z+z^2 = -z(z-1) + 1$? No.  
If $z=e^{i\theta}$, then $1-z+z^2 = 1 - (e^{i\theta} - e^{-2i\theta}/(e^{2i\theta}-1/e^{i\theta}))$... too confusing.  

Let's use the explicit modulus squared expression.  
$A = |1+z|$. We found $A = \sqrt{4\cos^2(\theta/2)} = 2|\cos(\theta/2)|$. Let's assume $\theta \in [0, 2\pi]$. Since the expression involves squares of real parts, symmetry around 0 matters.  
$B = |1 - z + z^2|$.  
Let's compute $B^2$.  
$(1-z+z^2)(1-\bar{z}+\bar{z}^2) = (1-z+z^2)(1-e^{-i\theta}+e^{-2i\theta})$? No, $\bar{z}$ is simpler.  
Let $w = 1 - z + z^2$. Then $\bar{w} = 1 - \bar{z} + \bar{z}^2$.  
$B^2 = (1-z+z^2)(1-\bar{z}+\bar{z}^2)$.  
Let's expand this polynomial in $z$.  
$(1-z+z^2)(1-z^{-1}+z^{-2})$. This assumes we divide by $z$, but it's simpler to substitute $\bar{z}=1/z$.  
$B^2 = (z^3-1)^2 / z^3$? No.  
Let's multiply polynomials:  
$(z-1)(-z+1) - 1 + z^2$... No.  
Factor out $1-z+z^2$.  
Note that $1-z+z^2 = -(1-z)(1-z^{-1}?)$?  
Wait, $z^3-1 = (z-1)(z^2+z+1)$. Also $(z^2-z+1)$ is related to $e^{i\theta} - e^{-2i\theta}$?  
Let's just calculate the modulus of the roots of unity. The polynomial is $\frac{z^3-1}{z-1}$ if $z \ne 1$. No, it's $\frac{z^3+1}{z+1}$? No.  
$z^2-z+1 = 0$ has roots $e^{i\pi/3}, e^{-i\pi/3}$.  
For $|z|=1$, let $z = e^{i\theta}$.  
$B^2 = |1 - z + z^2|^2 = (1 - z + z^2)(1 - \frac{1}{z} + \frac{1}{z^2}) = \left( \frac{z^2-z+1}{z} \right) \left( \frac{z^2-z+1}{z} \right)$ ?  
No, $1/z - 1/z^2$ term.  
Actually, $(1-z+z^2)(1-1/z+1/z^2) = (1-z+z^2)\frac{z^2-z+1}{z^2}$? No, $\bar{z} = 1/z$.  
The conjugate of $1 - z + z^2$ is $1 - \bar{z} + \bar{z}^2$. Since $|z|=1$, $\bar{z}=1/z$.  
So $B^2 = |z^3-1|^2 / (z+1)^2$?  
Let's recheck. $z^3-1 = z^3 - 1$. The denominator is $z^2-z+1$. No relation.  
But $z^3-1 = (z-1)(z^2+z+1)$.  
Also $z^2-z+1$ has modulus related to something else.  
Let's go back to expansion:  
$(1 - z + z^2)(1 - \bar{z} + \bar{z}^2) = 1 - z + z^2 - (z^{-1}) + |z|^{-1}(1+z)?$ No.  
Just substitute $\bar{z} = z^{-1}$:  
$B^2 = |1 - e^{i\theta} + e^{2i\theta}|^2$.  
This is $|(1-e^{i\theta})(1-e^{-i\theta}?)|?$ No.  
Let's use the cosine of differences formula.  
Actually, there is a known identity for $|1-z+z^2|$.  
$|1 - z + z^2|^2 = 3 - 2\cos(2\theta)$? No.  
Let's calculate it carefully.  
$B^2 = |1 - z + z^2|^2$.  
This is a polynomial in $z$ and $\bar{z}$.  
Since $|z|=1$, $\bar{z} = 1/z$.  
So $B^2 = \frac{(1-z+z^2)(1-1/z+1/z^2)}{1} = (z^3 - z^2 + z) / z$? No.  
Let's just multiply: $(1-z+z^2)(1 - 1/z + 1/z^2) = (1 - z + z^2) (\frac{z^2-z+1}{z^2})$. This looks like circular dependency if I write $B^2 = \dots$  
The conjugate polynomial is $P(\bar{z}) = 1 - \bar{z} + \bar{z}^2$.  
So $|P(z)|^2 = P(z) \overline{P(z)} = (1-z+z^2)(1-\frac{1}{z}+\frac{1}{z^2})$.  
Multiply by $z^3$: $(z-1+1/z?)$ No.  
Let's multiply $(1-z+z^2)$ and $(z^{-2}-z^{-1}+1)$.  
Common denominator $z^2$: $\frac{(z^2-z+1)(1-z^{-1}+z^{-2})}{1}$?  
Actually, let's simplify the fraction inside modulus first.  
Note that $(z-1)^3 = z^3 - 3z^2 + 3z - 1$.  
Let's check $(z^2-z+1)$.  
We know that $|z-1|^2 = 2(1-\cos\theta)$.  
And $|z+1|^2 = 2(1+\cos\theta)$.  
For the second term, $|1 - z + z^2|^2 = |(1-z+z^2)(1-\bar{z}+\bar{z}^2)| = (1-z+z^2)(1-1/z+1/z^2)$.  
$(1-z+z^2)(\frac{z^2-z+1}{z^2}) = \frac{z^{-2}(z^2-z+1)^2 - z^{-1}z(z^2-z+1) + 1^2?}{z^2}$... no.  
Let's just expand carefully.  
$(1-z+z^2)(1-1/z+1/z^2) = (1-z+z^2)( \frac{z^2-z+1}{z^2})$ is not correct, $\bar{z} = z^{-1}$ means $\overline{1-z+z^2} = 1 - \frac{1}{z} + \frac{1}{z^2}$.  
Let's check the algebra.  
Is $(1-z+z^2)$ related to $\frac{z^3+1}{z+1}$? No, that is $z^2+z+1$.  
The roots of $z^2-z+1=0$ are $e^{\pm i \pi/3} = -\frac{1}{2} \pm i \frac{\sqrt{3}}{2}$.  
So if $z = e^{i\theta}$, we can check values.  

Let's try specific values.  
If $z=1$, $|1+1| + |1-1+1| = 2 + 1 = 3$.  
If $z=i$ ($\theta = \pi/2$), $|1+i| + |1-i+(-1)| = |1+i| + |-i| = \sqrt{2} + 1$.  
If $z=-1$, $|0| + |1-(-1)+1| = 0 + 3 = 3$.  
If $z=-i$, $|1-i| + |1+i+(-1)|$... No, $|1-z+z^2|$.  
$z=i \implies 1-i+i^2 = 1-i-1 = -i$. Modulus is 1. $|1+z|= \sqrt{2}$. Sum $\approx 1.414+1 = 2.414$.  
If $z=1$, sum is 3.  
Let's find if max can be higher than 3.  
Let's use the property of triangle inequality.  
$|A+B| \le |A| + |B|$. Here $E(z) = |1+z| + |1-z+z^2|$. This is sum of two non-negative numbers.  
We want to maximize this sum.  
The maximum of a sum usually occurs at boundaries or critical points.  
Since it's continuous on the compact set $\{|z|=1\}$, max exists.  

Let's look for an algebraic identity for $|1-z+z^2|^2$.  
$B^2 = (1-z+z^2)(1-\bar{z}+\bar{z}^2)$.  
Substitute $\bar{z} = 1/z$:  
$B^2 = \frac{(z^3-1)}{z} \cdot \frac{(z^2+z+1)}{z}$? No.  
The expression is $1 - z + z^2$.  
If we substitute $x=z$, consider the polynomial $Q(z) = 1-z+z^2$.  
We want $|Q(e^{i\theta})|^2$.  
This is equivalent to finding max of $f(\theta) = \sqrt{4\cos^2(\theta/2)} + \sqrt{|1-e^{i\theta}+e^{2i\theta}|^2}$.  
Let's analyze $|1 - e^{i\theta} + e^{2i\theta}|^2$.  
Using $a^n + b^n$? No.  
Let's use the identity for $\frac{1-z+z^2}{z^3-1}$? No.  
Let's rewrite $1 - z + z^2$ in terms of distance.  
It is the length of vector $(1, -i) - (0,0) + \dots$?  
Consider the triangle with vertices 1, z, z^2?  
The points are on the unit circle.  
If we rotate the origin, it's a polygon or something.  
Let's calculate $|1 - e^{i\theta} + e^{2i\theta}|$.  
Note that $e^{2i\theta} = \frac{e^{i\theta}(e^{i\theta}-1)}{1}$? No.  
$z^3-1 = (z-1)(z^2+z+1)$.  
$|z^3-1| = |z-1||z^2+z+1|$. Not directly helpful.  

Let's try to express $|1 - z + z^2|$ using $\cos$.  
$|1 - e^{i\theta} + e^{2i\theta}|^2 = (1 - \cos\theta + i\sin\theta)^2$? No, modulus is squared.  
Let's use the formula: $|A-B+C|^2$ isn't helpful directly.  
However, we can express $1-z+z^2$ as a vector sum.  
This might be related to $z-1/z$ terms.  
We know that $\frac{1}{z} = \bar{z}$ for unit modulus.  
So $|1 - z + z^2|^2 = |(1 - z)^2 - 1|^2$? No, $(1-z+z^2)$ is not a difference of squares nicely unless $z^3=1$.  
Let's go back to the polynomial multiplication.  
$(1-z+z^2)(1-\bar{z}+\bar{z}^2) = (1-z+z^2)(1-1/z+1/z^2)$.  
Multiply by $z^3$? No, let's just multiply directly.  
Let $P(z) = 1 - z + z^2$.  
$|P(z)|^2 = P(z) \overline{P(z)}$.  
Since $\bar{z}=z^{-1}$, $\overline{P(z)} = 1 - z^{-1} + z^{-2} = \frac{z^2 - z + 1}{z^2}$.  
So $|P(z)|^2 = |z^3-1|^2 / |z^2(z+1)(z-1)|$? No.  
$P(z) = -(z^2-z-1)$? No.  
Let's look at $z^2 - z + 1$.  
We know that for any complex number $w$, $|w|^2$ is real positive.  
Let's simplify the product term:  
$\frac{z^3+z}{z} (1/z) = \dots$  
Actually, let's expand in terms of exponentials.  
$|1 - e^{i\theta} + e^{2i\theta}|^2$.  
This can be evaluated by summing squares.  
$1 - e^{i\theta} + e^{2i\theta} = 1 - (\cos\theta + i\sin\theta) + \cos(2\theta) + i\sin(2\theta)$?  
Let $z_0 = 1, z_1 = e^{i\theta}, z_2 = e^{2i\theta}$.  
$|1 - z_1 + z_2|^2 = (1-z_1+z_2)(1-\bar{z}_1+\bar{z}_2) = (1-z_1+z_2)(1-e^{-i\theta}+e^{-2i\theta})$.  
Let $u = e^{i\theta}$. Then $\bar{u} = 1/u$.  
$(1-u+u^2)(1-1/u+1/u^2) = (1-u+u^2)\frac{u^2-u+1}{u^2} = \frac{(1-u+u^2)^2}{u^2}$?  
Let's check the factorization again.  
Is $1-u+u^2$ related to $u^3-1$? No.  
But $(1-u+u^2)(u^2-u+1) = (u^2-u+1)^2$.  
However, we have $(1-u+u^2)(1-1/u+1/u^2)$.  
Is $1-1/u+1/u^2$ related to $u^2-u+1$?  
Let's multiply term by term:  
$1 \cdot 1 = 1$.  
$1 \cdot (-1/u) = -1/u$.  
$1 \cdot (1/u^2) = 1/u^2$.  
$-u \cdot 1 = -u$.  
$-u \cdot (-1/u) = 1$.  
$-u \cdot (1/u^2) = -1/u$.  
$u^2 \cdot 1 = u^2$.  
$u^2 \cdot (-1/u) = -u$.  
$u^2 \cdot (1/u^2) = 1$.  
Summing them up:  
$(1 + 1 + 1) + (-1/u - 1/u + 1/u^2) + (-u - u) + (u^2)$.  
$= 3 - 2(1/u) - 2(u) + (1/u^2 + u^2)$? No.  
Terms: $1, -1/u, 1/u^2, -u, 1, -1/u, u^2, -u, 1$.  
Real sum: $1 - u + u^2 - (-1/u) - (1/u) ...$  
Let's group by conjugate pairs or something.  
The product is $(1-u+u^2)(1-\bar{u}+\bar{u}^2)$.  
Since $\bar{u} = 1/u$, let's just multiply polynomials with real coefficients? No, $u$ is complex.  
Let's use the property that for unit circle, $|a+b|^2 = (a+b)(\bar{a}+\bar{b})$.  
So we have $(1-u+u^2)(1-\frac{1}{u}+\frac{1}{u^2})$.  
This is exactly $\frac{(1-u+u^2)(u^2-u+1)}{u^2}$?  
No, $1/u = \bar{u}$ implies the factor $1 - 1/u + 1/u^2$ is indeed the conjugate term.  
So let's look at $(1-u+u^2)$ and $\frac{(u-1)(u^{-1}-1) ...}{...}$.  
Let's use $x = e^{i\theta}$.  
$|1 - x + x^2|^2 = \left| \frac{x^3-1}{x-1} \right|^2$? No, that is $\frac{(1-x)^3+3(1-x)}{...}$ no.  
Is $1-x+x^2$ factorable over $\mathbb{R}$? $(x-\omega)(x-\bar{\omega})$.  
Yes, $x = \cos\theta + i\sin\theta$.  
So we can write $|1-x+x^2|^2 = | (e^{i\pi/3} - z)(\dots) |^2$? No.  
Let's use the result $|1-z+z^2|^2 = 3 - 2\cos(2\theta)$ if possible. Let's test with $z=1$.  
If $z=1$, LHS $= |1-1+1|^2 = 1$. RHS $= 3-2(1) = 1$. Matches.  
Test with $z=i$ (where $\theta=\pi/2$). LHS $= |-i|^2 = 1$. RHS $= 3-2\cos(\pi) = 5 \ne 1$. So that formula is wrong.  
Let's re-evaluate the modulus squared expression algebraically.  
We want to simplify $(1-u+u^2)(1-\bar{u}+\bar{u}^2)$ where $|u|=1$.  
Since $\bar{u}=1/u$, this is $(1-u+u^2)(1-1/u+1/u^2) = (u^3-u+1)\frac{1}{u^2}$? No.  
$(1-u+u^2)(1-\frac{1}{u}+\frac{1}{u^2})$. Multiply top and bottom by $u^2$ in the second factor to match numerator degree?  
Let's multiply $(1-u+u^2)$ and $(u^{-2}-u^{-1}+1)$. No.  
Multiply by $z^3 = u^3$. The first term becomes $(z^3-z^2+z)$. The second becomes $(z^3-z+1)$. No, that's not right.  
Actually, let's compute $A = 1-u+u^2$ and $\bar{A} = 1-1/u+1/u^2$.  
$\bar{A} u^2 = (u^2-u+1) \cdot u^{-2} \cdot u^3$? No.  
Let's look at the expression $z^2-z+1$ again. It is related to $\frac{z^3-1}{z-1}$? No.  
The polynomial $z^2-z+1$ has roots $e^{i\pi/3}, e^{-i\pi/3}$.  
This means for these values, the modulus is 0. For $|z|=1$, $|z|=1 \implies z=1$.  
So at $\theta = \pm \pi/3$, the term is zero? No, modulus squared is 0 implies term is zero? No.  
If $z=e^{i\pi/3}$, $z^2-z+1 = 0$? Let's check.  
$(e^{i\pi/3})^2 - e^{i\pi/3} + 1 = e^{i2\pi/3} - ( \frac{1}{2} + i\frac{\sqrt{3}}{2} ) + 1$.  
$= (-1/2 + i\sqrt{3}/2) - 0.5 - 1.5 i\sqrt{3} / 2 ...$ No.  
Let's check $e^{i2\pi/3} = -1/2 + i\sqrt{3}/2$.  
Sum is $(-1/2+1 - \sqrt{3}/2) = 0$. Yes, $1-z+z^2=0$ if $z=e^{i\pi/3}$? No.  
If $z = e^{i\pi/3}$, then $z^3=1$, so $z^2+z+1=0$. Thus $-(z^2-z-1) \ne 0$.  
The equation $z^2-z+1=0$ implies $z = \frac{1 \pm i\sqrt{3}}{2} = e^{\pm i \pi/3}$.  
So for $z=e^{i\pi/3}$, $1 - z + z^2 = 1 - (\frac{1}{2} + i\frac{\sqrt{3}}{2}) + (\frac{-1}{2} + i\frac{\sqrt{3}}{2})$? No.  
$z^2 = -\frac{1}{2} - \frac{i\sqrt{3}}{2}$ if $z = e^{i2\pi/3}$?  
Let's calculate carefully.  
Roots of $z^2-z+1=0$: $\omega, \bar{\omega}$ where $\omega = e^{i\pi/3}$.  
$|\omega|^2=1$. So if $z=e^{i\pi/3}$, then $z^2-z+1 = 0$?  
Let's check: $z^2 = -\frac{1}{2} - \dots$ No.  
The roots are $\cos(\pi/3) \pm i \sin(\pi/3)$? No.  
Roots of $x^2-x+1=0$: $x = \frac{1 \pm \sqrt{1-4}}{2} = \frac{1}{2} \pm i\frac{\sqrt{3}}{2}$? No, $\sqrt{-3}/2 = i\sqrt{3}/2$.  
So roots are $\frac{1 + i\sqrt{3}}{2} = e^{i\pi/3}$.  
Then $x^2-x+1 = (e^{i\pi/3})^2 - e^{i\pi/3} + 1 = e^{i2\pi/3} - e^{i\pi/3} + 1$.  
$e^{i2\pi/3} = -1/2 + i\sqrt{3}/2$. $e^{i\pi/3} = 1/2 + i\sqrt{3}/2$.  
Difference: $(-1/2 - 1/2) + (0 - \sqrt{3}) = -1 - i\sqrt{3}$. No, real part is $-1$, imaginary part is $\sqrt{3}/2 - \sqrt{3}/2$? No.  
Imaginary part of $e^{i2\pi/3}$ is $\frac{\sqrt{3}}{2}$. Imaginary part of $e^{i\pi/3}$ is $\frac{\sqrt{3}}{2}$. They cancel out.  
So imaginary part is 0. Real part: $-1/2 - 1/2 = -1$.  
So $z^2-z+1 \neq 0$.  
What I calculated before was wrong.  
$z^2+z+1=0$ roots are $e^{i\pi/3}$? No.  
$z^3-1 = (z-1)(z^2+z+1)$. Roots of $z^3-1$ are 1, $\omega = e^{2\pi i/3}, \bar{\omega}$.  
So $e^{i\pi/3}$ is not a root of $z^2-z+1=0$.  
Roots of $z^2-z+1=0$ are $\frac{1}{2} \pm i\frac{\sqrt{3}}{2}$.  
These correspond to angles $\pi/3$ and $-\pi/3$ (or $5\pi/3$).  
Let's check again. $(e^{i\pi/3})^2 - e^{i\pi/3} + 1$.  
Let's use Euler form.  
$(\frac{1}{2} + i\frac{\sqrt{3}}{2})^2 - (\frac{1}{2} + i\frac{\sqrt{3}}{2}) + 1$? No, $\omega = e^{i2\pi/3}$ is root.  
Roots of $x^2-x+1=0$ are roots of unity for 6th roots?  
$x^2+x+1=0$ gives $e^{i4\pi/3}, e^{i5\pi/3}$.  
$x^2-x+1=0$ is the same as $x^2+x+1$ with sign change? No.  
The roots are $\frac{1 \pm i\sqrt{3}}{2}$. These are $\cos(60) + i\sin(60)$ etc.  
Let's calculate $z^2-z+1$ at $\theta = 60^\circ$.  
$\omega = e^{i\pi/3}$. $\omega^2 - \omega + 1 = e^{i2\pi/3} - e^{i\pi/3} + 1$.  
$= (-1/2 + i\sqrt{3}/2) - (1/2 + i\sqrt{3}/2) + 1 = -1 + 1 = 0$.  
Ah, I made a mistake in the subtraction earlier.  
Let's re-subtract:  
Real parts: $-1/2 - 1/2 + 1 = 0$.  
Imaginary parts: $i\sqrt{3}/2 - i\sqrt{3}/2 + 0 = 0$? No, there is no constant term in subtraction of imaginary. The last term is 1 (real). So imag part is $\sqrt{3}/2 - \sqrt{3}/2 = 0$.  
So indeed $z^2-z+1 = e^{i\pi/3} - e^{-i\pi/3}$? No.  
It is 0 at $\theta = \pi/3$ and $\theta = -\pi/3$.  
Since the modulus squared of this term vanishes at these angles, we found that $B=0$ if $z=e^{\pm i\pi/3}$.  
Let's verify again.  
If $z = e^{i\pi/3}$, then $z^2 - z + 1 = (\cos \frac{60}{?})$. No, just numbers.  
$\omega = e^{i\pi/3}$. $\omega^2 = e^{i2\pi/3}$.  
$e^{i2\pi/3} - e^{i\pi/3} + 1 = (\cos 120 + i \sin 120) - (\cos 60 + i \sin 60) + 1$  
$= (-1/2 + i\sqrt{3}/2) - (1/2 + i\sqrt{3}/2) + 1 = -1/2 - 1/2 + 1 + i(\dots) = 0$.  
Okay, so $|1-z+z^2|^2$ has a minimum of 0 at $z=e^{i\pi/3}, e^{-i\pi/3}$.  
The term is zero when $z^3=1$.  
No, $z^3=1 \implies z=1, \omega, \bar{\omega}$.  
Here $\omega = e^{i2\pi/3}$? No.  
Let's check roots of $z^2-z+1=0$ again. Discriminant $D = 1-4=-3$. Roots $(1 \pm i\sqrt{3})/2 = e^{\pm i\pi/3}$.  
These correspond to angles $\pi/3$ and $-\pi/3$.  
So at these points, the second term is 0.  
But $|1+z|$ at $z=e^{i\pi/3}$ is $\sqrt{2(1+1/2)} = \sqrt{3}$.  
At $z=e^{-i\pi/3}$, it's also $\sqrt{3}$.  
So values are $\sqrt{3}$ and $|0|=0$. Sum = $\sqrt{3} + 0 = \sqrt{3} \approx 1.732$.  
But earlier we found max is likely larger, e.g. at $z=1$, sum is $3$. At $z=-1$, sum is $3$.  
So this local minimum of the second term doesn't prevent a larger global maximum.  

Let's check if there is a general formula for $|1-z+z^2|^2$.  
We have $(1-e^{i\theta}+e^{2i\theta})(1-e^{-i\theta}+e^{-2i\theta})$.  
$= (1 - e^{i\theta} + e^{2i\theta}) (\frac{e^{-i3\theta}-1}{e^{-i3\theta}})?$ No.  
Let's multiply by $e^i \dots$?  
Consider the identity $\sin(2\pi/3) = 0$.  
We have $(1-z+z^2)(z-1/z+1/z^2)$... no.  
Actually, notice that for $z=e^{i\theta}$, $|1-z+z^2|^2$ can be expressed using cosine?  
Recall $z^2 - z + 1 = \frac{z^3+1}{z-1} \times (-1)$? No.  
$z^3-1 = (z-1)(z^2+z+1)$. Not useful.  
However, if we look at the roots of $|1-z+z^2|$ being zero is only at $e^{i\pi/3}$ etc.  
Let's rewrite $|1 - z + z^2| = |e^{i\pi/3}| = 1$? No.  
Consider the geometry.  
We want to maximize $|z-(-1)| + |z^2-z+1|$? No, it is $|1+z| + |1-z+z^2|$.  
Let's rewrite terms using $e^{i\theta}$.  
$|1+z|^2 = 4\cos^2(\theta/2)$. So $|1+z| = 2|\cos(\theta/2)|  

## Answer

*(none: the token cap hit during thinking)*
