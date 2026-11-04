# test/intermediate_algebra/1806.json (Intermediate Algebra, level 5)

> Let $z$ be a complex number such that $|z| = 1.$  Find the maximum value of  
> \[|1 + z| + |1 - z + z^2|.\]  

**Wrong.** Gold `\frac{13}{4}`, predicted `None`. Finish: length, 16384 tokens, 133 waits, 1437.3 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

The user wants to find the maximum value of the expression $E(z) = |1 + z| + |1 - z + z^2|$ subject to the constraint $|z| = 1$.  

Let's denote $a = 1$ and $b = 1 - z + z^2$.  
We are given that $z$ is a complex number on the unit circle, so $z = e^{i\theta}$ for some $\theta \in [0, 2\pi)$. The expression involves moduli of terms involving $z$, which are polynomials in $z$.  

Let's simplify the term $|1 - z + z^2|$.  
Notice that $1 - z + z^2$ is related to complex numbers.  
Recall that for a polynomial $P(z)$, we might find relations like $(1-z)^{n} + z^n \dots$ or similar identities using Chebyshev polynomials or geometric interpretations of the roots.  
Specifically, consider the points $z_0 = 1/2$ and $z_n = (-1)/2$ etc? No, that's not right.  

Let's look at the structure $|1+z| + |1-z+z^2|$.  
Since $|z|=1$, $z = e^{i\theta}$. Then $-z = -e^{i\theta}$.  
Also note that $1+z$ has modulus squared $(1+z)(1-\bar{z}) = 1 - z + \bar{z}$. No, modulus is not just product.  
The term $1-z+z^2$ can be rewritten using complex numbers.  
Note that $|1-z+z^2|$ suggests a geometric interpretation related to the distance between points or angles.  
Consider the expression $(1 + z)(1 - \bar{z}) = 1 - z + z$. Wait, $|1-z+z^2|^2$ is not easy unless we relate it to $(1+z)^2$.  

Let's rewrite the expression using properties of the modulus for complex numbers.  
Maybe there's a known identity or inequality? Or maybe substitution simplifies things.  
Let's look at the second term again: $|1 - z + z^2|$.  
This looks like distance from $0$ to $1, z+z^2$? No.  
Consider rotation by angle $\phi$ around some point on unit circle.  

Let's consider the geometric interpretation of the expression.  
The function $E(z)$ is defined on the unit circle $\Gamma$. We want to maximize it.  
By symmetry or geometry, we might guess that the maximum occurs at specific points.  
Since $|z|=1$, $z$ can be written as $x + iy$.  
Let's try a few values of $z$.  
If $z=1$, $|1+1| + |1-1+1^2| = 2 + 0 = 2$.  
Wait, if $z=-1$, $|1-1+1| = 1$ ? No.  
Let's plug in $z=-1$: $E(-1) = |1 + (-1)| + |1 - (-1) + (-1)^2| = 0 + |1+1+1| = 3$.  
Wait, let me recalculate for $z=-1$.  
$|1+z| = |1-1| = 0$.  
$|1-z+z^2| = |1 - (-1) + (-1)^2| = |1 + 1 + 1| = 3$.  
Sum is $0+3=3$.  

Let's plug in $z=i$.  
$E(i) = |1+i| + |1-i+i^2| = \sqrt{2} + |1-i-i^2| = \sqrt{2} + |1-i+(-i)(-i)|$? No.  
$|1-z+z^2|$ for $z=i$.  
$1 - i + (-i)^2 = 1 - i - 1 = -i$.  
So $E(i) = |\sqrt{2}| + |-i| = \sqrt{2} + 1$.  

Wait, the term is $|1+z| + |1-z+z^2|$.  
Let's try to find a general bound.  
If I can prove $|1-z+z^2| \leq c|z|^2$? No.  
Note that $(1 - z + z^2)^2 = (1-z)^2 + 2z(1-z) + z^4$ ? No.  
Let's use properties of complex modulus and polynomial roots.  
Consider the polynomial $P(z) = (z-1)^3$. Roots at 0, 1, -1? No.  

Let's try to express $|1+z|$ in terms of something.  
Let $w_1 = 1+z$ and $w_2 = 1-z+z^2$. Note that $(1+z)(1+1) = |1+z|^2 + |1-z|^2$? No.  
$|z| = 1$, so $|z|=1$.  
Let $x = z$. Then we want to maximize $f(x) = |1+x| + |(1-x+x^2)|$.  

Is there a simpler form?  
Wait, $1+z+z^2$ is not $(1-z)^2$ or similar.  
Maybe the second term relates to distance on complex plane from 0?  
Actually, $|1 - z + z^2|$ looks like modulus of something related to points on unit circle.  
If we view this as a function, maybe there's an inequality using triangle inequality?  
$|1+z| \leq |1| + |z| = 1+1 = 2$.  
$|1 - z + z^2|$ could be bounded by something like $|1-z|^2$. No.  

Let's check the case where $E(z)$ achieves maximum value.  
From previous values:  
$z=1 \implies E(1) = 2$.  
$z=-1 \implies E(-1) = 3$.  
Is it possible to get higher?  
Try $z=i/2$. No, must be on unit circle. Try $z=-1/\sqrt{2}$? No, check boundary cases.  
Let's analyze the function behavior more closely.  
We have terms $T_1 = |1+z|$ and $T_2 = |1-z+z^2|$.  
The modulus of $(1+z)(1 - \bar{z})$ is $0$?  
Wait, we know that for any complex number $z$, $|1+z|^2 = 1 + 2\text{Re}(1\cdot z) + |z|^2 = 1 + 2\text{Re}(1\cdot x - i \dots)$. Wait.  
$|1+x|^2 = (1+iz)(1-ix)$? No, $(1+z)(1-z^{-1})$.  
Let $u = 1+z$, $v = 1-z+z^2$. Note that $z=1/u - v$.  
Wait, if we fix $z$, what is the value of $|1+z|$?  
Let's consider the geometric interpretation.  
Consider the complex numbers $w_1 = 1+z$ and $w_2 = 1-z+z^2$.  
We want to maximize $|w_1| + |w_2|$.  

Let's use Cauchy-Schwarz or Minkowski inequality.  
$\sqrt{ |a|^2 + |b|^2 } \ge |a+b|$.  
Also $|\dots|^2$ can be written as product of terms?  
Actually, consider $z = e^{i\theta}$.  
Then $1+z = 1+e^{i\theta}$ and $1-z+z^2 = 1 - e^{i\theta} + e^{2i\theta}$.  
Notice that $1 - e^{i\theta} + e^{2i\theta} = (1-e^{i\theta}) - e^{i\theta}(e^{-i\theta} \cdot e^{\dots})$. No.  
Actually, let's write this as $\frac{z-1}{z} + z^2(1-\dots)$ ? No.  
Let's try to relate $|1-z+z^2|$ and $|1+z|$.  
$|1-z+z^2| = | (z-1)(z+1) - 2z + \dots|$? No.  
Recall that $1 + z^3 - z - 1/z$? No.  

Let's look at the identity $1 + z^2$.  
Consider the expression for $1-z+z^2$ in terms of angles.  
We know that $(1-e^{i\theta}) = e^{-i\theta/2}(e^{i\theta/2}-e^{-i\theta/2})$.  
$|1-z+z^2|^2 = (1 - 2z + z^2) = |z-1|^2$? No.  
$|1-z+z^2| = |z^2(1/z^2 - 1)(1-z) ...|$ ? No.  
Let's rewrite $1 - z + z^2$.  
Note that $|1-z+z^2|^2 = (1+z+iz+z^2+\dots)$? No.  

Let's try a substitution to make it symmetric.  
Let $w = 1+z$. Then $z = w-1$. Since $|z|=1$, $|w-1|=1$.  
Also $1-z+z^2 = (1-(w-1)) + (w-1)^2$? No.  
$1-z+z^2 = 1 - z + z^2$.  
$= 1 - (w-1) + (w-1)^2$ ? No, $(w-1)^2 = w^2 - 2w + 1$.  
$1-z+z^2 = 1 - w + 1 - w^2 + \dots$  
Wait, $z = w-1$.  
$1 - z + z^2 = 1 - (w-1) + (w-1)^2 = 2-w+w^2-2w+1$? No.  
$= 1 - w + 1 + \dots$ Wait.  
Let's compute the expression $E = |w| + |1-(w-1)+(w-1)^2|$. No.  

Wait, let's check for a simpler polynomial identity.  
Is it possible that $1-z+z^2 = (1-e^{i\theta})(e^{i\theta})^{-2}$? No.  
Actually, consider $(z-1)^3$? Roots of unity?  
Let's try substituting $z = e^{i\theta}$.  
We want to maximize $f(\theta) = |1 + e^{i\theta}| + |1 - e^{i\theta} + e^{2i\theta}|$.  
Let $a = 1, b = 1+z+z^2$ (modulus of something).  
Note that $(z-1)^3 = z^3 - 3z^2 + 3z - 1$.  
This doesn't seem to simplify nicely.  

Let's use the substitution $x = 1+z$ and $y = 1-z+z^2$.  
Then $x+y = 2$. So $y = 2-x$.  
We need to maximize $|x| + |y|$? No, $y$ depends on $z$, but we have a constraint.  
Is $y$ constrained?  
Let's re-evaluate the expression.  
Let $u_1 = 1+z$ and $u_2 = 1-z+z^2$.  
Then $|u_1|$ is $|w-1| + |z|$. No.  

Wait, let's try to factorize the second term.  
$1 - z + z^2 = (z+1)(z-1)$. No, that is $z^2-z+1$.  
Is it $(z^2+z+1)$?  
$(z-1)^2 = z^2-2z+1$. So $1-z+z^2 = -(z-1)^2 + 4z$.  
Let's check: $-(z^2-2z+1) + 4z - 4 = -z^2+2z-1+4z-4$? No.  

Actually, let's re-examine the structure of terms carefully.  
$|1-z+z^2|$.  
Consider points in complex plane. Let $z_0 = 1/2 + i/2$. Then $1-z_0 = \dots$. Not related to roots.  

Let's use the relation:  
$|a|^2 + |b|^2 \ge |a+b|$? No.  
Maybe we can find an upper bound for $E$.  
We have $u = 1+z$ and $v = 1-z+z^2$.  
Note that $z = u - 1$. Then $v = 1 - (u-1) + (u-1)^2 = 2-u + u^2 - 2u + 1$? No.  
$v = 1 - u + 1 - u^2 + u = 2-u+u^2$.  
Wait, $(z-1)(z+1)$ is not correct. $1-z+z^2 = z(z-1) + 1$.  
Let's check: $z^2 - z + 1$. This is different from $1-z+z^2$.  
$1-z+z^2 = (1+z)(1-z) - z^2$? No.  

Let's rewrite the modulus terms.  
We have $|1+z|^2 = (1+iz)(1-i \cdot i \cdot z)$ ?  
If we use polar coordinates, let $z = e^{i\theta}$.  
Then $|1+z|^2 = 1 + 2\cos\theta + 2\sin\theta$? No.  
Let's calculate $|1+z|^2 = (1+e^{i\theta})(1-e^{-i\theta})^* = (1+e^{i\theta})(1-e^{i(-\theta)})$. No.  
$(1+z)(1-z) = 1 - z^2$. No, that's not right.  
$|1+z|^2 = |1+e^{i\theta}|^2 = (1 + e^{i\theta})(1 + \bar{z})$? No.  
The term is $|1+z|^2 = 1+2\text{Re}(z) + |z|^2$.  
Since $|z|=1$, $\text{Re}(z) = \cos\theta$.  
So $|1+z|^2 = 1 + 2\cos\theta + 1 = 2 + 2\cos\theta$. This is wrong.  
$|1+z|^2 = (1+e^{i\theta})(1-\bar{z})$? No, that's $(1+e^{i\theta})(1-e^{-i\theta})$?  
Actually, $|1+z|^2 = |1+z|^2$.  
Also $1-z+z^2 = z + 1 - z + z^2$.  
If we consider $w = z$, the terms are related to distances from the origin and points on unit circle.  

Let's try a different approach.  
Let $P(z) = |1+z| + |1-z+z^2|$.  
We can write $1+z+z^2 = (z+1)^2 - 3z$. No, $(z-1)(z+1)$?  
Wait, $|1-z+z^2| = |\frac{1}{z}((z+z^2)-z(1))|$?  
Let's rewrite $|1-z+z^2| = |z(z) + 1 - z|$. No.  

Is there an identity like $(1-z+z^2)(1+z) = \dots$?  
$(1-z+z^2)(1+z) = (1-z^2) + (z-z+1)(z+1)$?  
Let's try to compute $P(z)^2$. No.  

Let's try a specific angle calculation again, maybe there is a symmetry.  
If $z=i$, we got $\sqrt{2} + 1 \approx 2.414$. If max is larger than 3.  
Wait, if $|1+z| \ge |1-z|$, then max sum? No.  
Let's calculate for other angles.  
$z=0$ (not allowed).  
$z=-1$: $E(-1) = 3$.  
$z=i/2$: not on unit circle.  
Let's check the maximum value.  
We have $|1+z| = |(1+z)(1-z^{-1}) - 1(1-z^{-1})|$. No.  

Let's look at the geometric interpretation: $|a+b|$ is distance between two vectors.  
If we fix one term, can we make the other large?  
Consider $|1-z+z^2| = |(1-e^{i\theta})(z-e^{i\theta}) - e^{i\theta}(z-1)|$ ? No.  

Let's assume the maximum occurs at $|z|=1$.  
Maybe use Cauchy-Schwarz inequality?  
Consider vectors $\mathbf{u} = (1, 1)$ and $\mathbf{v} = (x,y)$.  
Wait, let's rewrite $|1+z|$ as distance between point 0 and $z$ on the circle? No.  

Let's consider the function $f(z) = |1-z+z^2|^2 + |1+z|^2$ or something similar.  
Wait, $|1-z+z^2| = |z^2+z+1 - (z^2-2z)|$? No.  
Note that $(z^2-2z+1)(z) = z^3 - 2z^2 + z$. Not helpful.  

Let's re-examine the term $1-z+z^2$.  
If $z=e^{i\theta}$.  
The expression is $E(\theta) = |1+e^{i\theta}| + |1-e^{i\theta} + e^{2i\theta}|$.  
Let $w_1 = 1+e^{i\theta}$ and $w_2 = 1-e^{i\theta} + e^{2i\theta}$.  
Wait, $1-e^{i\theta} + e^{2i\theta} = e^{i\theta}(e^{-i\theta} - 1) + e^{2i\theta}$? No.  
$1 - e^{i\theta} + e^{2i\theta} = e^{-i\theta/2} (z-e^{\dots})$.  
Let's just compute $|w_1|^2$ and $|w_2|^2$.  
$|1+z|^2 = 1 + z + \bar{z} + |z|^2$? No, $(a+b)(\bar{a}+\bar{b}) = |a|^2 + |b|^2 + 2\text{Re}(ab)$.  
Here $a=1$, $b=z$. So $|1+z|^2 = 1+|z|^2 + 2\text{Re}(z)$? No.  
Wait, $(1+z)(1-z^{-1})$? No.  
Let's use $e^{i\theta}$.  
$|1+z|^2 = (1+e^{i\theta})(1-e^{-i\theta})^*$.  
This is not helpful directly.  

Let's rewrite the second term $1-z+z^2$ in terms of angles.  
$1-z+z^2 = \text{Re}( (1+z)e^{i\theta} ) / |z|$? No.  
Actually, note that $(1-z)(1+1/z)$.  
Is it possible that $|1-z+z^2| = |1|^2 - z - 1$? No.  

Let's try a numerical search with Wolfram Alpha logic mentally or just guess the pattern.  
We want to maximize $f(z) = |1+z| + |1-z+z^2|$ for $|z|=1$.  
For $z=1$: $E = 2+0 = 2$.  
For $z=-1$: $E = 0+3 = 3$.  
Let's check $z$ such that $|z|=1$.  
If we choose $z=i$, $E = \sqrt{2} + 1 \approx 2.414$.  
What about $z$ near $-i$? No, must be unit circle.  
Is there a point where $|1-z+z^2|$ gets large while $|1+z|$ is small?  
If $z=-1$, $1-z+z^2 = 3$.  
If $z=i$, $|1-z+z^2| = |-i|=1$.  
Wait, my previous calculation for $z=i$ was: $1-i + (-i)^2 = 1-i-1 = -i$. Yes.  
So $E(i) = |1+i| + |-i| = \sqrt{2} + 1 \approx 2.414$.  

Let's check if we can get higher.  
Maybe consider $z$ such that $1+z=0$, which means $z=-1$. But then $1-z+z^2 = 3$. Sum is 3.  
What if $z$ approaches $-1$? $E(z) \to 3$.  
What about $z=i/2$? No.  
Let's check specific values on unit circle.  
$|1-z+z^2| = |(1-z)(1+z)|$.  
Wait, is $1-z+z^2 = (1-z+z^2) + \dots$?  

Let's re-evaluate $|1-z+z^2|$ for general $z=e^{i\theta}$.  
Recall that $e^{i\theta} = -1/2 \sqrt{8 \cos(2\theta)}$... no.  
Let's look at the term inside modulus.  
It is $z^2 - z + 1$? Wait, $(1-z+z^2)$ is different from $z^2-z+1$.  
$z^2-z+1 = |1-z+z^2|$.  
For $\theta \in [0, 2\pi]$, the value of $z^2 - z + 1$ traces a path.  
The maximum of this polynomial (magnitude) is at its roots? No, max modulus for polynomial roots on unit circle?  
Let's see: The modulus of $1-z+z^2$.  
Consider $(1-e^{i\theta}) + e^{-i\theta}$?  
$(1 - \cos\theta + i \sin\theta) + (\cos\theta - i \sin\theta) = 1 + 2\cos\theta$. No.  

Actually, let's look at the identity:  
$1 + z^3$ etc.  
Consider $z = e^{i\alpha}$.  
$|1-e^{i\alpha}| + |1-z+z^2|$?  
Wait, let's consider the expression:  
$E(z) = |1+z| + |1-z+z^2|$.  
Notice that for $z=1$, $|1+1| = 2$.  
For $z=-1$, $|0| + 3 = 3$.  
What if we rewrite the second term:  
$|1-z+z^2| = |z^2(1/z) - z(z-1)/z + 1|$? No.  

Let's check the derivative of $E$ with respect to $\theta$.  
This is an optimization problem.  
Let $z = e^{i\theta}$.  
Then $1+z = 1+e^{i\theta}$ and $1-z+z^2 = 1-e^{i\theta} + e^{2i\theta}$.  
We want to maximize $f(\theta) = |1+e^{i\theta}| + |1-e^{i\theta}+e^{2i\theta}|$.  
Let's compute $g(\theta) = 1-e^{i\theta}+e^{2i\theta} = e^{-i\theta/2}(e^{3i\theta}-1)$. No, that's $e^{i(1+2\theta)} - e^{i\theta}$.  
Wait, let's use $\cos$ and $\sin$.  
$|1+z|^2 = 1 + |z|^2 + 2\text{Re}(z)$.  
$|1-z+z^2|^2 = (1-z+z^2)(1-\bar{z})$. Wait, $1-z+z^2 = (1-z)(1+z)$? No.  
Let's calculate explicitly:  
$(1-z+z^2)(1-z+\dots)$.  
Maybe use the substitution $w = 1-z$. Then $z = 1-w$. $|w-1|=1 \implies |w|=|1|$? No, that changes modulus.  
$|1+z|^2 = (1+w)^2 + w^2 - 2w$ ?  
Actually, let's just use $z=x+iy$.  
$z = x+iy$, so $|1+x+iy|$. This is getting messy.  

Let's assume there is a geometric interpretation where $1+z+z^2$ has a specific property relative to $1-z$.  
Recall that for any complex number $z$, we have $|z|^2 = 1 \implies |z| = 1$.  
So points lie on circle.  
Let's write $1+z+z^2 = (1+z)^2 + z$? No.  
$(1-z)(1+z+z) = 1-z+z$.  
Actually, $1-z+z^2 = (z-1)(z+1)$?  
Let's check for a specific value: $z=0$, term is 1.  
For $z=i$, term is -i. Modulus is 1.  
$|1+i|= \sqrt{2}$. $|-i|=1$. Sum $\approx 2.414$.  
Is it possible to get sum > 3?  
Try $z = -1 + i\epsilon$. No, on unit circle.  
Try $z = e^{i\phi}$.  
For $z=e^{i\pi}=-1$, we have $E=3$.  
Wait, for $z$ such that $1-z+z^2$ is real and positive?  
Let's check if $1-z+z^2$ can be large.  
We know $(z-1)^2 = 0 \implies z=1$ or something? No.  
$(1-z)(1+z)$. This is not the expression.  
Actually, consider $P(z) = 1 - z + z^2$.  
This is a polynomial of degree 2. On the unit circle, max modulus occurs when real part is max? No.  

Let's check for the specific value of $z$ maximizing $|1+z|$. This is simply $z \to -1$, giving $E=3$.  
For $|1-z+z^2|$: if $z=-1$, this term is $1-(-1)+1 = 3$.  
Wait, I calculated $E(z) = |1+z| + |1-z+z^2|$ for $z=-1$ earlier as $0+3=3$.  
Let's double check this.  
$|1+z| = |1-1| = 0$. Correct.  
$|1-z+z^2| = |1 - (-1) + (-1)^2| = |1 + 1 + 1| = 3$. Correct.  
So $E(-1) = 3$.  

Is it possible to have a larger value?  
Let's check $z=i/2$ again. It was not on unit circle.  
For $z=e^{i\phi}$, let's try to see if we can make $|1+z|$ large and $|1-z+z^2|$ small or vice versa.  
Actually, notice that $|1-z+z^2| \leq 3$.  
This is because $|1-z|^2 + |z|^2$? No.  
Let's look at the maximum of $|1-z+z^2|$.  
If $z=-1$, $|1-(-1)+(-1)^2|=3$.  
If $z=0$ (not allowed), $|1|=1$.  
The maximum of $|1-z+z^2|$ on the unit circle.  
Let $f(z) = 1 - z + z^2$. The max modulus is for $z \in [-1, 1]$? No, it's a polynomial.  
We want to maximize $|P(z)|$ where $|z|=1$.  
Let $P(z) = z^2 - z + 1$. This is actually the real part of $(1-z)(1+z)$?  
Wait, $P(z) = (z-1/2)^2 + \dots$ No.  
The roots are at $z_1, z_2 = \frac{1 \pm i\sqrt{3}}{2}$. Not on unit circle.  
So max modulus of polynomial is attained somewhere else?  
Wait, the maximum value of $|P(z)|$ for $|z|=1$ is not necessarily related to the coefficients' magnitudes in a simple way.  
Actually, $|z^2 - z + 1| \leq |z^2| + |-z+1|$? No.  
Let's just compute it directly.  
We have two terms: $T_1 = |1+z|$ and $T_2 = |1-z+z^2|$.  
$T_1 = |(1+z)(1-\bar{z})| = |1-z|^2$ if $\bar{z}=z^{-1}$? No.  
If $z=e^{i\theta}$, $T_1 = \sqrt{(1+e^{i\theta})(1-e^{-i\theta})}^2$? No.  
Let's use the expansion:  
$|1+z|^2 = (1+z)(1-z)^*$.  
$|1-z+z^2|^2 = (1-z+z^2)(1-z-z)$.  
Wait, no. $(A+B+C)^2 = A^2 + B^2 + C^2 + 2AB + \dots$ No.  

Let's look at the problem again. $|1+z| + |1-z+z^2|$.  
Is it possible that $|1-z+z^2| \leq 3$ always?  
Wait, $(z-1)(z+1) = z^2 - 1$. This is not $1-z+z^2$.  
Let's check the roots of $z^2 - z + 1 = 0$. They are $\pm i/2 \dots$  
Wait, roots are $e^{i\pi/3}$? No.  
The roots of $z^2 - z + 1 = 0$ are $\frac{1 \pm \sqrt{1-4}}{2}$. Complex roots not on unit circle except if coefficient is different.  
Actually, let's check if $|z^2-z+1|$ is maximized for some $z$.  
Let $z=x+iy$. $x^2-y^2+2ixy - xy = (x-0.5)^2 + \dots$ ? No.  

Wait, is there any constraint I missed? "Find the maximum value of $|1+z| + |1-z+z^2|$".  
Let's re-evaluate my calculation for $z=-1$.  
$E(-1) = 3$.  
What if $z=i$? $E(i) = \sqrt{2}+1 \approx 2.414$.  
Wait, maybe there is a point closer to origin where this sum grows.  
Let's check the function behavior near $-1$.  
If we vary $\theta$ from $\pi$ (where $z=-1$, $E=3$) to $\dots$.  
What if we approach $\theta = \pi/2$? $z=i$. $E(\pi/2) \approx 2.414$.  
So it seems max is around 3 or maybe larger.  
But wait, I found a value of 3 at $z=-1$.  
Let's check if we can make this sum larger.  
Maybe the term inside modulus is always bounded by something.  
We have $|1-z+z^2| = | (1-z) + z^2 | \leq |1-z| + |z^2|$? No, triangle inequality gives an upper bound on terms individually but we need sum of moduli.  
Actually, notice that $z^2 - z + 1 = z(z-1) + 1$. This is not bounded by $3$ generally.  
Wait, let's check if $|1-z+z^2|$ is always $\leq \dots$.  
We know that for any $z$, $|1+z|^2 + |1-z+z^2|^2 \ge (\dots)$?  

Let's try to express the sum in terms of distances from roots.  
Consider points $0, 1, z$.  
Maybe consider geometric interpretation:  
$E(z) = |\mathbf{p}| + |\mathbf{q}|$.  
Consider vectors representing $z$.  
Actually, notice that $|1-z+z^2|$ can be written as distance from $z$ to some point?  
Wait, the expression is $1 - z + z^2$. This looks like the value of polynomial at a point.  
Let's use the identity:  
$(1-e^{i\theta})(e^{-i\theta}) \dots$? No.  

Let's try a different substitution: $w = 1+z$. Then $z = w-1$.  
$|w|^2 + |1-z+z^2|^2 = |w| + |w - (z+1)|^2$? No.  
Maybe rewrite the second term using conjugate $1+\bar{z}$.  
$|1-z+z^2|^2 = |(1-z)(z+1) - z^2|$? No.  
Wait, let's factorize $1-z+z^2$.  
We know that if $|z|=1$, then $(1-z)(1-\bar{z}) = 1-z + \dots$?  
Actually, $1-z+z^2 = (z-1)^2 - 3z$? No.  

Let's look at the expression $f(z) = |1+z| + |1-z+z^2|$.  
Is it possible that this sum is equal to something related to $\sqrt{2}$ or similar?  
For $z=1$, value is 2.  
For $z=i$, value is $\approx 2.414$.  
Let's check the case where $|1-z+z^2|$ is maximized.  
Wait, $|1-z+z^2| = \frac{1}{|z|^2} \dots$ No.  
Actually, consider the geometric shape of the unit circle and the complex numbers.  
Consider the expression $\sum |n_i z - c_i|$.  

Let's re-evaluate my previous calculation for $z=i/2$ (not allowed) again.  
What if I made a mistake and check something else.  
Let's check $z = e^{i \pi/3}$. No, that's $\cos \pi/3 + i \sin \pi/3$.  
If $z=i$, then $|1-z+z^2| = |-i| = 1$.  
$|1+i| = \sqrt{2}$. Sum = $\approx 2.414$.  
If $z=-i$, $|1+(-i)+(-i)^2| = |1-i-1| = |-i| = 1$.  
$|1-i| = \sqrt{2}$. Sum = $\approx 2.414$.  

So at $z=1, E=2$. At $z=i, E=\approx 2.414$.  
Is it possible to find a point where $E > 2.414$?  
Wait, earlier I calculated $|1-z+z^2|$ at $z=-1$ as 3.  
But wait, let's re-calculate carefully for $z=-1$.  
$1-z+z^2 = 1 - (-1) + (-1)^2 = 1 + 1 + 1 = 3$.  
$|1+z| = |1-1| = 0$.  
So sum is 3.  
Wait, I calculated $\sqrt{2} \approx 1.414$. Wait, $E(i) = \sqrt{2} + |-i| = \sqrt{2} + 1$. Yes.  
Is there a point where the term $|1-z+z^2|$ is larger than 3? No, because $z$ on unit circle, max of polynomial modulus on unit circle is bounded by $\sum |coeffs|^2$? No.  
For a complex polynomial $P(z) = c_0 + c_1 z + c_2 z^2$. On unit circle, it can grow.  

*Continued in [part 2 of 2](intermediate_algebra_1806_p2.md): GitHub stops rendering math on pages this long, so the transcript is split.*
