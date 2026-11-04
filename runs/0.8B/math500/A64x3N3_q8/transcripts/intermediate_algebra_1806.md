# test/intermediate_algebra/1806.json (Intermediate Algebra, level 5)

> Let $z$ be a complex number such that $|z| = 1.$  Find the maximum value of  
> \[|1 + z| + |1 - z + z^2|.\]  

**Wrong.** Gold `\frac{13}{4}`, predicted `None`. Finish: length, 16384 tokens, 16 waits, 1891.3 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

The user wants to find the maximum value of the expression $E(z) = |1 + z| + |1 - z + z^2|$ subject to the constraint $|z| = 1$.  

Let's denote $a = 1$ and $b = z$.  
We are looking for a complex number $z$ with $|z|=1$.  
The expression is a sum of absolute values, but it can be interpreted geometrically.  
$|1+z|$ is the distance between $1$ and $-1$ if we think of points as vectors in $\mathbb{C} \cong \mathbb{R}^2$? Or rather, complex numbers lie on a circle in $\mathbb{C}$.  
Let's work with real coordinates. Let $z = x + iy$ where $x,y$ are real numbers and $x^2+y^2=1$.  
Then $|z| = \sqrt{x^2+y^2} = 1$.  

We can rewrite the term inside the modulus:  
$T_1 = |1 + z|$  
$T_2 = |1 - z + z^2| = |(1+z)(1-z) - (z-1)^2|$? Wait.  
Let's try to relate $1+z$ and $1-z$.  
Since $z \bar{z} = 1$, we know that $z \in \mathbb{C}$ means $z = x+iy$ with $x^2+y^2=1$.  
We can consider the expression in terms of polar coordinates. Let $z = e^{i\theta}$.  
Then $|z|=1$.  
The expression becomes:  
\[ E(\theta) = |1 + e^{i\theta}| + |1 - e^{i\theta} + (e^{i\theta})^2|\]  
Note that $1 - z + z^2$ can be factored as $(z-1)(z^2+1)$? Let's check.  
$1 - e^{i2\theta}$ is $1 - (\cos 2\theta + i \sin 2\theta)$. This doesn't help much immediately with the structure of the modulus.  

Let's try to factor the second term differently.  
Is there a relation between $(1-z)$ and $(z+1)$? Yes, since $z^2 = -w^2$ is not true, $z^2 \neq 1$ generally unless $z=\pm 1$.  
Since $z \in S^1$, $1+z$ is on the line through origin with angle $\theta + \pi/2$?  
Let's visualize in the complex plane.  
Let $1+z = r_1 e^{i\phi_1}$. The magnitude is $|1+z| = r_1$.  
The expression $T_2$ involves terms related to $1-z$ and $z^2$.  
Let's consider rotating points by some angles?  
Note that for any complex number $w$, if we substitute $z^2 = 1/z$ (not applicable here) or $z=1/w$...  

Let's use the geometric interpretation of $|w|^2 + |z - w| \ge 0$.  
Consider the function $f(z) = |1+z| + |1-z+z^2|$.  
We are looking for a maximum over $z \in \mathbb{C}$ such that $z$ is on the unit circle.  

Let's try substituting specific values.  
If $z = 1$, then $E(1) = |1+1| + |1-1+1^2| = |2| + |1| = 3$.  
Is this the maximum?  
If $z = -1$, $E(-1) = |1-1| + |1-(-1)+(-1)^2| = |0| + |1+1|=2$? Let's check.  
$T_1 = |1-1| = 0$.  
$T_2 = |1 - (-1) + 1| = |3| = 3$.  
Total sum $= 0 + 3 = 3$.  

If $z = -i$, then $E(-i) = |1-i| + |1 - (-i) + (-i)^2|$.  
$T_1 = |1-i| = \sqrt{1^2+(-1)^2} = \sqrt{2}$.  
$T_2 = |1 + i - 1| = |i| = 1$.  
Total sum $= \sqrt{2} + 1 \approx 2.414$.  

If $z = 1/i$, then $E(1/i) = |-1-1| + |1 - (1/i) + (1/i)^2|$ ?  
$T_1 = |2i^{-1}| = |-2| = 2$? Wait.  
Let's rewrite terms more carefully.  
$T_1 = |1+z|$  
$T_2 = |z+1-z^2|$. Since $z = e^{i\theta}$, $z^2 = e^{2i\theta}$.  
So $|z+1-z^2| = |(1-z)(1-z+z) - (z^2-1)|$? Let's check the factorization again.  
Let $z=e^{i\theta}$.  
Term 1: $1+z$. Modulus is $\sqrt{(1+x)^2 + y^2}$ where $x=\cos \theta, y=-\sin \theta$ (using standard $z=x+iy$).  
Actually $|1+z|^2 = (1+e^{i\theta})\overline{(1+e^{-i\theta})}$.  
Let's check if there is a relation between the terms.  
Note that $1-z = 1 - e^{i\theta}$? Or is it $(1-z) + z^2$?  
Maybe rewrite $|1-z+z^2|$ as sum of two absolute values?  
Consider triangle inequality: $|A+B| \le |A|+|B|$.  
So we have an upper bound on the expression. The maximum of the sum occurs when all terms add up.  
Is there a relation between $T_1$ and $T_2$?  
Let's try to find specific points where $T_2 = 0$ or something similar. If $T_2 = T_1 + \epsilon$.  

Alternative approach:  
The expression is symmetric with respect to some operation?  
$|1+z|$ vs $|z^2-1-z|$?  
If we substitute $z \to 1/z$? Then $|1+1/z| + |1 - 1/z + 1/z^2| = |-1/(z) + (1+1/z)| / |z^3|?$.  
Actually, let's try to see if $T_2$ simplifies using properties of $|w| \ge |u-v|$?  
Let's consider the complex numbers.  
Let $x=1$, then we have $|x+z| + |x- (1-z) + z^2|$. This is getting messy.  

Let's try to interpret the modulus as a dot product or something similar?  
$|w|$ is the length of vector $w$.  
We want to maximize $|a+w_1| + |a+w_2| + \dots$  
Let $z^2 = k$. Then we have $T_1 = |1+z|$ and $T_2 = |(1-z)+z^2| = |(1- (z+1)) + z^2|$.  
Is it possible to factor out $(1+z)$?  
$(1+z) = 1 + \bar{z}$.  
$1-z+z^2 = (1+z)(1+z^{-1}) - z$?  
Let's try a different transformation.  
Let $u = 1+z$. Then $z = u-1$. Since $|z|=1$, we have $(u-1)^2 + |u|^2 = 1 \implies u\bar{u} + u^{-1}$... this is just substitution.  
Let's stick to the variables.  

Geometric interpretation for a simpler sum:  
$|a+b+c|$?  
Consider the point $z$ in the complex plane.  
The terms are distances from points on the unit circle to some origin/vertices.  
Specifically, we have two terms:  
1. Distance between $-1$ and $z$. $|z+1| = \sqrt{(x+1)^2+y^2} = |e^{i\theta} - 1|$?  
Let's re-read the problem statement carefully.  
Find the maximum value of $|1 + z| + |1 - z + z^2|$.  

Let's try to manipulate the second term: $1 - z + z^2$.  
Note that $(1+z)^2 = 1 + 2z + z^2$.  
Is there any identity relating these?  
Maybe we can write this as a sum of two terms using polar decomposition?  
We know that for $|w| \le 1$, let's consider the function $\phi(w) = |w-1| + |w+1|$?  
The expression looks like $|1+z| + |(z+1)(1+z^{-1}) - z|$?  
Let's try substituting $w = z$.  
We want to maximize $|1+z| + |1-z+z^2|$.  
If we use polar coordinates, let $z = e^{i\theta}$.  
$1+z = 1 + \cos \theta + i \sin \theta = \cos(\theta+ \alpha) + i \sin(\theta+ \alpha)$?  
Magnitude squared is $|1+z|^2 = (1+\cos \theta)^2 + \sin^2 \theta = 1 + 2\cos \theta + 1 = 2 + 2\cos \theta = 4 \cos^2 (\theta/2)$. So $|1+z| = 2 |\cos(\theta/2)|$.  
Similarly, the second term magnitude squared:  
$|1 - z + z^2|^2 = |e^{i\pi} - 2 + e^{-i\pi}| \dots$?  
$z+1-z^2 = 1+e^{i\theta} - e^{2i\theta}$.  
Magnitude squared is $(1-\cos(2\theta))^2 + (0)^2$?  
Let's check: $1 - z + z^2$. $z = \cos \theta + i \sin \theta$.  
Real part: $1 - \cos 2\theta = 1 - (\cos^2 \theta - \sin^2 \theta)$.  
If $\theta = \pi/4$, then $z=i, z=-1$?  
Let's check the expression again.  
The second term is $|1 - z + z^2|$.  
For any complex number $z$, this looks like the magnitude of something related to triangle inequality on the plane.  

Let's re-examine the terms:  
1. $|1+z|$ corresponds to distance between the origin and point $-1$?  
Let $w = 1+z$. Since $|z|=1$, $z = \bar{w}$ is not generally true, but $w = 1+z$ can be anything on $\mathbb{C} \setminus \{-1\}$. But since $z$ is unitary, $w$ is also a complex number with modulus at most $\sqrt{3}$.  
So $|1+z|$ is distance from origin.  
2. $|1-z+z^2| = |(1+z)(1-z) + (z^2-1)|$?  
Let's expand: $1 - z + z^2 = 1 + z(z+1)$.  
Also, $1+z+z^2 = z(1+iz)$?  
Let's try factorization $1+z+z^2 = (1+z)(1-z+z^{-1})$?  
Let's try substituting $u = z$.  
Then we have $|1+u| + |1-u+u^2|$.  
The second term is $|(1+u)(1-u) - (u-1)^2|$. This doesn't look helpful.  
How about expressing it as $\sqrt{3} \cos(\dots)$?  
If we take $u$ to be a root of unity, maybe the value varies.  
Let's test roots of unity.  
Possible values for $z = e^{i\theta}$.  
If $\theta = 0 \implies z=1$, $E = |2| + |1+1|=3$.  
If $\theta = \pi/2 \implies z=i$, $E = |1+i| + |1-i-(-1)|$?  
$|i+1 - i - (-1) + i^2|$?  
Let's calculate:  
Term 1: $|1+i| = \sqrt{2}$.  
Term 2: $|1-i+(i^2)| = |1-i-1| = |-i| = 1$.  
So sum is $\sqrt{2} + 1 \approx 2.414$.  
If $\theta = \pi \implies z=-1$, $E = |0| + |1+1-(-1)|$?  
$|1+z| = |0| = 0$.  
$|1-z+z^2| = |1 - (-1) + (-1)| = |3-1| = 2$.  
So sum is $0+2=2$?  
Let's check the calculation.  
For $z=-1$, $1-z+z^2 = 1-(-1)+1 = 3$. Absolute value is 3?  
My previous manual calculation was:  
$T_1 = |1+(-1)| = 0$.  
$T_2 = |1 - (-1) + 1| = |3| = 3$.  
Sum $= 3$.  
Why did I think it was 3 before? Because I calculated $|1-i+1|$ earlier.  
The term is $1 - z + z^2$. If $z=-1$, this is $1 - (-1) + (-1)^2 = 1 + 1 + 1 = 3$.  
Ah, $T_2 = 3$. $T_1 = 0$. Sum = 3.  
What about $\theta = \pi/4$? $z=i$.  
$T_1 = |1+i| = \sqrt{2}$.  
$T_2 = |1-i-1| = |-i| = 1$.  
Sum = $\sqrt{2} + 1 \approx 2.414$.  

Let's check $z=i$. Is there another combination?  
Maybe use the triangle inequality: $|1+z| + |1-z+z^2| \le |1+z| + |(1+z)(1-z)|$?  
$T_2 = |1-z+z^2| = |1 - z + z^2|$. Note that $z^2 = 1/z \bar{z} / z = 1/z^3$ ?  
Let's look at the structure $|1-u+v|$ and $|1+u-v|$.  
Let $a = |1+z|$, $b = |1-z+z^2|$.  
Can we bound this?  
We have $(1-z)^2 + z^2$?  
$(1-z)^2 + z^2 = 1 - 2z + z^2 + z^2 = 1 - 2z + 2z^2$.  
Is there a relation? $1-z+z^2$.  
What if we set $x = |1+z|$, $y = |1-z+z^2|$?  
Let's check the case where the modulus is constant.  
Since the expression depends on $z$, let's see if the maximum occurs at some point on the boundary or interior.  
But here it's just the unit circle $S^1$.  

Let's try to transform the expression into something else.  
Is there a geometric interpretation involving $1, z$ and $z^2$?  
Consider triangle with vertices $0$, $-1$, $z$.  
We have distances $|1+z|$ which is length of side connecting origin to point on unit circle (say at angle $\theta$ relative to 1).  
Let's use the property that $|1+z| = |z-(-1)|$.  
And we want to maximize $|z-(-1)| + |1-z+z^2|$.  
Note that $1-z+z^2$ is a number on the unit circle?  
If $z=e^{i\theta}$, then $1-z+z^2 = 1-e^{i\theta} - e^{-i\theta}$ (since $e^{i\theta} = z$).  
$|1 - (\cos \theta + i \sin \theta) + \cos 2\theta - i \sin 2\theta|$?  
$z^2 = e^{2i\theta}$.  
Let's compute $|1 - z + z^2|^2 = (1-z+z^2)(1-\bar{z}-\bar{z^2})$?  
Actually, let's try to express $|1-z+z^2|$ as a distance.  
Consider points $A=1$, $B=-1$. Then $T_1 = |A + z|$. This is the distance from origin to a point $z \in S^1$.  
$C = 1 - z + z^2$. Note that $(1-z) = (z^{-1}+1)$?  
Actually, $1-z+z^2 = 1 - e^{i\theta} + e^{2i\theta}$.  
Let's use the fact that $|w| \ge |\bar{w}|$.  
Consider vectors in $\mathbb{C}$.  
If we rotate coordinates such that one of the terms aligns?  
Let's check if there's a simpler inequality.  
$1-z+z^2 = (z+1) - z^2 + z^2$?  
Is $|1-z+z^2|$ related to $\max( |z-1|, \dots)$?  
Consider vectors:  
$v_1 = 1$, $v_2 = -z$. Then $1-z+z^2 = v_1 - v_2 + z^2$. This doesn't seem helpful.  

Let's consider the geometric interpretation again.  
The problem is maximizing $|1+z| + |1-z+z^2|$.  
We know that for a fixed point $z$, the expression is constant if we vary something else?  
Let's fix the argument of $z$.  
Is there a relation between terms using complex algebraic geometry or optimization problems?  
Let's assume the maximum occurs at some specific angle.  
Possible candidates: $z=1, z=-1, i, -i$.  
$z=1 \implies 3$.  
$z=-1 \implies 0 + 3 = 3$.  
$z=i \implies \sqrt{2} + 1 \approx 2.414$.  
Is it possible the max is larger?  
Consider $z = e^{i\theta}$.  
Let's expand: $|1+z|^2 + |1-z+z^2|^2$.  
$= (1+x)^2 + y^2$.  
Let's try to express everything as vectors.  
We are looking for maximum of $|u| + |v|$ where $u = 1+z$, $v = 1-z+z^2$.  
Note that $z \in S^1$.  
We can consider the rotation of vectors.  
Since $z$ is on a circle, if we fix an angle $\alpha$, say for any point on the circle.  
If we rotate $z$ by some amount, we change both terms.  

Let's try to factor the second term $|1-z+z^2|$.  
Note that $z \in S^1$.  
Consider the complex numbers as vectors in $\mathbb{C}$.  
We are maximizing $|u+v|$ subject to conditions?  
$u = 1+z$, $v = 1-z+z^2$.  
Notice that $(1+z) + z^2$ is just $z+z^2+1$. This looks like roots of unity.  
Let's try to use the inequality $|a+b|^2 + |c+d|^2 \ge 0$ or something.  
Consider the identity: $|1-z+z^2| = |(z-1)(z+1)|$?  
No, $z+1 \neq z-1$.  
Let's try to write $v = -(z^2-1) + (1-z) + z^{-1} + 1$?  
Let's look at the expression again.  
$E(z) = |1+z| + |1-z+z^2|$.  
If we choose $z = -i$, $E = \sqrt{2}+1$.  
If we choose $z = e^{i\pi/3} = 1/2 + i \sqrt{3}/2$.  
Then $z^2 = e^{i(2\pi/3)} = -1/2 + i \sqrt{3}/2$.  
$1-z+z^2 = 1 - (1/2 + i \sqrt{3}/2) + (-1/2 + i \sqrt{3}/2) = 1 - 1/2 - 1/2 = 0$.  
So at $\theta = 60^\circ$, $1-z+z^2 = 0$. Thus $|1-z+z^2| = 0$.  
Then the sum is just $|1+z|$.  
$z = e^{i\pi/3}$. Then $z-1/2 = \dots$.  
$1-z+z^2 = 1 - (1/2 + i\sqrt{3}/2) + (-1/2 + i\sqrt{3}/2) = 0$.  
So this gives $E(60^\circ) = |1+1/2 + i\sqrt{3}/2| = |3/2 + i\sqrt{3}/2| = \sqrt{9/4 + 3/4} = \sqrt{3}$.  
So $E(z) = \sqrt{3} \approx 1.732 < 3$.  
This is a valid point, but not maximum.  

Let's look for points where $|1-z+z^2|$ might be 0. This occurs if $1-z+z^2 = 0$.  
$z^2 - z + 1 = 0$. The roots are complex.  
$z = \frac{1 \pm i\sqrt{3}}{2} = e^{i\pi/6}$?  
No, $\frac{1}{2} + \frac{\sqrt{3}}{2}i$. This is not on unit circle? $r^2 = 1+3=4$. Not valid.  
The equation has solutions in $\mathbb{C}$ but we want roots on the unit circle (actually $S^1$).  
$z = e^{i\theta}$. The polynomial is $x^2-x+1=0$. Discriminant is $1-4 = -3$. Roots are $\frac{1 \pm i\sqrt{3}}{2}$, which are not on the unit circle.  
So for any real $\theta$ (and thus any $z$), does this happen?  
The roots of $z^2-z+1=0$ are at angle $\pi/6$.  
Let's check if we can choose $\theta$ such that $z^2 - z + 1 = 0$ is possible.  
$z$ must be on unit circle, so $|z|=1$.  
Then $z \bar{z} = 1$, etc.  
But the roots are not real, they have imaginary parts $r= \frac{1}{2}$?  
Let's recheck: $\frac{1 \pm i\sqrt{3}}{2}$.  
This has modulus squared $\frac{4 - 6i \sqrt{3}}{4} = \frac{1}{2}(2-3i) \neq 1$ if $|z|^2=1$?  
Modulus is $\frac{1}{\sqrt{2^2+1}}$?  
If the root has modulus squared, it's not on unit circle.  
So $|1-z+z^2|$ cannot be 0.  

Let's re-evaluate:  
We want to maximize $|1+z| + |1-z+z^2|$.  
This looks like we need to bound this sum from above.  
Consider the identity $|1 - z + z^2| = |z-1 - z^2 + z| = |(z+1) - z - z^2|$?  
Let's try to rewrite the modulus in terms of distance.  
If we consider vectors $\mathbf{u}, \mathbf{v}$ corresponding to $1+z$ and $1-z+z^2$, then their sum has magnitude?  
Actually, let's look at the function as a sum of functions of $\theta$.  
Let $z = e^{i\theta}$.  
$|1+z| = \sqrt{(1+e^{i\theta})^2}$ (using $|z|^2=1$) ?  
The problem is to maximize this over unit circle.  

Is there a property of $1 - z + z^2$ related to $(1-z)$?  
Consider the vector $\mathbf{v} = 1$.  
Let's consider $u = 1+z$ and $w = 1-z+z^2$.  
Then $w = (1-z)(z) + 1 - z$?  
We know that for unit vectors, $|a+b+c|^2 \ge |a+b|^2 - |b-c|^2$?  
Let's rewrite terms.  
Consider points $A=1, B=z, C=-z$. Then $1-z+z^2 = A-B+B-A+C-C+...$  
This doesn't seem right.  

Let's try to use the property that $|u| + |v| \ge 0$?  
Maybe substitute $z=e^{i\phi}$?  
Consider the term $z^2 - z + 1$.  
If we take $z = e^{i\phi}$.  
Term 1 is $|1+e^{i\phi}|$.  
Term 2 is $|1-e^{i\phi}-e^{-i\phi}|$?  
Let's factor the second term:  
$1 - z + z^2 = (z-1)(z+1) - z - \dots$  
Maybe write it as $|(1+z)(1-z) - z|$?  
This seems complicated.  

Let's use the AM-GM or something related to complex numbers.  
We have $|1+z| + |1-z+z^2| = |1+z| + |(z-1)(z+1) - 1(z-1)|$?  
Let's rewrite the second term in terms of distance to points $0, z, -z$.  
Consider vectors $\mathbf{w} = 1-z$, $\mathbf{v} = z^2$.  
$|1-z+z^2|$ is not a sum.  

Let's try to bound it using the triangle inequality.  
$|1+z| + |1-z+z^2| \le |1+z| + |(1-z)(z^{-1}+z)|$?  
Note that $z^2 = z^{-1} - 1/z \cdot (1)$.  
Actually, $(1-z)^2 + z^2$ is not helpful.  
What about $|1-z+z^2|$ using polar coordinates?  
Let's assume the question implies a maximum value of the form $\sqrt{3}$ or something related to roots of unity.  

Let's try specific angles again.  
If we pick $z$ such that $1-z+z^2 = 0$, we get 0 for the second term and $|1+z|$ is the max distance.  
The maximum of $|1+z|$ on unit circle is $\sqrt{2}$ (for $z=1/\sqrt{2} + i/\sqrt{3}$?  
$1+z$ can be anything in complex plane, not restricted to circle radius 1?  
Yes, if we vary $z$, $1+z$ traces a circle of radius $\sqrt{(1+r)^2 - r^2} = \dots$?  
Let's look at the range of values for $|1+z|$ when $z=e^{i\theta}$.  
$(1+e^{i\theta})^2 = 1 + 2e^{i\theta} + e^{2i\theta}$.  
Real part: $\cos(\theta+\pi) \dots$?  
$|1+z|^2 = (1+e^{i\theta})\bar{(1+e^{-i\theta})} = (1+\cos \theta)^2 + (\sin \theta - i \sin \theta)^2$.  
$= 1 + 2\cos \theta + \cos^2 \theta + \sin^2 \theta - 2i \sin \theta \cos \theta$  
$= 2 + 2\cos \theta = 4 \cos^2(\theta/2)$.  
So $|1+z| = 2 |\cos(\theta/2)|$. The maximum of this is 2 (when $\theta = 0$).  
When $\theta = 0$, $z=1$, $|1+z| = 2$, sum = $2+|1-1+1| = 3$.  
The max value of the sum is clearly at least 3.  
Is there any case where it exceeds 3?  

Let's check if we can make the sum arbitrarily large.  
If $z$ is close to imaginary axis, say $\theta \to -\pi/2$. $z = i$.  
$|1+z| = \sqrt{2}$.  
$|1-z+z^2| = 1$. Sum $\approx 2.414$.  
If we take $\theta = \pi/2$, $z=-i$.  
$|1+z| = |0+i| = 1$.  
$|1-z+z^2| = 3$. Sum = 4.  
Let me re-calculate this one carefully.  
Case: $z = -i$.  
$T_1 = |1+z| = |-1-i| = \sqrt{1^2 + (-1)^2} = \sqrt{2}$.  
$T_2 = |1 - (-i) + (-i)^2| = |1 + i - 1| = |i| = 1$.  
Sum = $\sqrt{2} + 1 \approx 2.414$.  
My previous calculation $|0+3|$ was wrong. $T_2 = |1-z+z^2|$ with $z=-1$ is $|1 - (-1) + 1| = |3| = 3$.  
With $z=-i$, $T_2 = |1-i-1| = |-i| = 1$.  
My previous check was likely confused about $z=1$ or something.  

Let's check a point where $T_2 = 0$ is impossible.  
We found roots of $z^2-z+1=0$ are not on unit circle. So max modulus is never attained there.  
What if we want $|1+z| + |1-z+z^2|$ to be large?  
Consider $\theta$ such that $z$ approaches something close to boundary?  
Let's try $\theta = \pi$. $z=-1$.  
$T_1 = 0$.  
$T_2 = |1 - (-1) + 1| = 3$.  
Sum = 3.  

Let's try $\theta = -\pi/2$? That is $z=0$ (not allowed).  
Let's try to find the maximum of $E(\theta) = |1+e^{i\theta}| + |1-e^{i\theta}-e^{-2i\theta}|$.  
$|1+e^{i\theta}|^2 = 4 \cos^2(\theta/2)$?  
Let's use $z=e^{i\theta}$.  
$|1+z|^2 = (1+\cos \theta)^2 + \sin^2 \theta = 2+2\cos\theta$.  
So $|1+z| = 2|\cos(\theta/2)|$. The range of this is $[0, 2]$.  
However, we also have the second term.  
$T_2 = |1-z+z^2| = |(1-z) + z^2|$?  
Let's substitute $z$ by its polar coordinates $e^{i\theta}$.  
$T_2^2 = (1-e^{i\theta}+e^{-2i\theta})(1-\bar{e}^{-2i\theta}+\bar{e}^{-i\theta})$?  
Let's calculate $T_2^2$:  
$|1-z+z^2|^2 = |1 - (\cos \theta + i \sin \theta) + (\cos 2\theta + i \sin 2\theta)|^2$.  
Real part of modulus:  
$\text{Re}(A)$?  
Let $A = (1-z)(z+1)$?  
$|1+z|^2 = 4 \cos^2(\theta/2)$.  
For $T_2$, let's check if it relates.  
Notice that $|1-z+z^2| = |1 - e^{i\theta} + e^{2i\theta}|$.  
Let $f(\theta) = (1-\cos \theta)^2 + (\sin \theta)^2 - 2i \dots$?  
The magnitude squared is $(1-e^{i\theta})^2(e^{-2i\theta})(e^{i\theta}-1)$?  
$|1-z+z^2|^2 = (1 - \bar{z} + z^2)(1-z)\bar{1-z}?$  
Actually, let's rewrite $1-z+z^2$.  
If we use the substitution $w = e^{i\theta}$, then $T_2 = |(1-w) + w^2|$?  
$|1-w|^2 = 2 - w^2/2$?  
Let's calculate explicitly for different $\theta$.  
$\theta = \pi \implies z=-1 \implies |1+z| = 0$, $T_2=3$, sum = 3.  
$\theta = 0 \implies z=1 \implies |1+z| = 2$, $T_2=2$ (using $1-1+1$), sum = 4?  
Let's re-evaluate $T_2(1)$.  
$T_2 = |1-1+1^2| = |1| = 1$.  
So $\theta=0 \implies T_2 = 1$, not 2.  
My previous calc was wrong.  
$\theta = 0$: $z=1$. $1-z+z^2 = 1-1+1 = 1$. $T_2=1$.  
$|1+e^{i0}| = |2|=2$.  
Sum $= 3$.  

Let's check the derivative approach.  
We want to maximize $f(\theta) = |1+z| + |1-z+z^2|$.  
Let $A = 2|\cos(\theta/2)|$ and $B = |1-e^{i\theta}-e^{-2i\theta}|$.  
At $\theta = \pi$, $z=-1$: $T_2 = 3$. $A=0$. Sum=3.  
At $\theta = -\pi/2$? (This is $z=i$): $T_2 = 1$. $A=\sqrt{2}$. Sum=2.414.  
At $\theta = \pi/2$ ($z=-i$): Same as before?  
Let's check:  
$\theta = \pi/2$: $z=i$.  
$T_1 = |1+i| = \sqrt{2}$.  
$T_2 = |1-i + 1^2|$?  
$1-z+z^2 = 1-i+(-1)^2 = 1-i+1 = 2-i$.  
$|1-i-1| = |-i| = 1$.  
Sum $= \sqrt{2}+1 \approx 2.414$.  
So max is not at $\pi$.  

Let's check $T_2^2$ for general $\theta$.  
$T_2^2 = (1-e^{i\theta}-e^{-2i\theta})(\dots)$.  
Using polar coordinates, we can write $|a|^2 + |b|^2 \ge 0$.  
But we have a sum.  
Is it possible that the max is $\sqrt{3}$ or similar?  

Let's try to use AM-GM or Cauchy-Schwarz?  
Consider complex numbers $u, v$. We want to bound $|1+z| + |1-z+z^2|$.  
Note that $1+z$ and $1-z+z^2$ have a relation.  
$(1-z)^2 + z^2 = 1 - 2z + 2z^2$?  
Consider the function $g(\theta) = |1+e^{i\theta}| + |1-e^{i\theta}-e^{-2i\theta}|$.  
Let's rewrite this in terms of distance from origin and something else.  
Actually, look at the modulus:  
$|1+z| = \sqrt{2} |\cos(\theta/2)|$ ?  
If $\theta=0$, $z=1$, sum=3.  
If $\theta=\pi$, sum=3.  
At $\theta = \pi/2$, sum $\approx 2.41$.  
What about $\theta = 60^\circ$?  
$z = e^{i\pi/3}$. $|1+z|^2 = (1+1/2)^2 + (\sqrt{3}/2)^2 = 9/4 + 3/4 = 3$.  
So $|1+z| = \sqrt{3}$.  
$T_2 = |1-e^{i\pi/3}-e^{-i\pi/3}|$?  
$e^{-i\pi/3} = \cos(-60) + i \sin(-60) = 1/2 - i\sqrt{3}/2$.  
$T_2 = |1 - (1/2 + i\sqrt{3}/2) - (1/2 - i\sqrt{3}/2)| = |1 - 1 + i\sqrt{3}| = \sqrt{3}$.  
So sum is $2\sqrt{3} \approx 3.46$?  
Let's calculate carefully.  
$z = e^{i\pi/3}$.  
$T_1 = |1+e^{i\pi/3}| = \sqrt{(1+0.5)^2 + (\sqrt{3}/2)^2} = \sqrt{2.25 + 0.75} = \sqrt{3}$. Correct.  
$T_2 = |1-z+z^2| = |1 - (e^{i\pi/3}) + e^{-i\pi/3}|$?  
$z^2 = e^{-i\pi/3}$.  
So $1 - e^{i\pi/3} + e^{-i\pi/3} = 1 - (\cos 60 + i \sin 60) + (\cos 60 - i \sin 60)$?  
$z^2 = e^{-i\pi/3}$ is correct.  
So term is $1 - z + z^2$.  
Let's evaluate this:  
$1 - (1/2 + i\sqrt{3}/2) + (1/2 - i\sqrt{3}/2)$  
$= 1 - 1/2 - i\sqrt{3}/2 + 1/2 - i\sqrt{3}/2 = 0.5 - i\sqrt{3}$?  
Let's recalculate the real part: $1 - 1/2 + 1/2 = 1$.  
Imaginary part: $-i\sqrt{3}/2 - (-i\sqrt{3}/2) = 0$?  
Let's check the terms carefully.  
$z = 1/2 + i \sqrt{3}/2$.  
$z^2 = e^{-i\pi/3}$.  
$1-z+z^2 = 1 - (1/2 + i\sqrt{3}/2) + (1/2 - i\sqrt{3}/2)$?  
$z^2$ is $\cos(-60^\circ) + i \sin(-60^\circ)$. So $1/2 - i\sqrt{3}/2$.  
So $1-z+z^2 = 1 - (1/2 + i\sqrt{3}/2) + (1/2 - i\sqrt{3}/2) = 1 - 1 + (-i\sqrt{3} - (-i\sqrt{3}))$?  
No.  
Real part: $1 - 1/2 + 1/2 = 1$.  
Imaginary part: $-i\sqrt{3}/2 - (-i\sqrt{3}/2) = 0$.  
So $T_2 = |1| = 1$.  
Sum is $\sqrt{3} + 1 \approx 2.732$.  
This is less than 3.  

Let's try to check if we can get sum $\ge 4$?  
Consider $\theta \to 0$. $z=1$. Sum=3.  
Consider $\theta = -\pi/2$. $z=-i$.  
$T_1 = \sqrt{2}$.  
$T_2 = |1+i-1| = 1$.  
Sum = $\sqrt{2} + 1 \approx 2.414$.  
Consider $\theta$ small positive?  
If $z \to e^{i0}$, then $T_1 \to 2$, $T_2 \to 1$, sum $\to 3$.  
Is it possible to have a larger value?  
Let's try $\theta$ such that $T_2$ is very large.  
If $T_2$ can be made larger than $|1+z|$ or something?  
Note the expression $1-z+z^2$ looks like distance from $z$ to $(0, 0)$ rotated by 90 degrees?  
Let's try to calculate $T_2^2$.  
$T_2^2 = (1 - z + z^2)(\bar{1} - \bar{z} - \bar{z^2})$?  
If we interpret this as complex numbers, maybe use the property that for $w \in S^1$, $|w-1| + |w^{-1}-1|$ is something.  

Let's try to see if $E(z) = |1+z| + |1-z+z^2|$ has a minimum of 0?  
We established $T_2$ can be zero only for specific points on circle?  
If $z^2 - z + 1 = 0$, roots are complex, not on unit circle.  
So $T_2$ cannot be zero unless $|1+z|$ is large, but we saw max value of sum is bounded.  

Let's try to find a configuration where $E(z) > \sqrt{3}$.  
Is there any constraint I missed?  
"Find the maximum value of".  
Maybe I should consider the geometric interpretation differently.  
Consider vectors $\mathbf{u}$ corresponding to $1+z$ and $\mathbf{v}$ corresponding to $z^2 - z + 1$.  
Let's rewrite the second term: $|1-z+z^2|$.  
Note that $(1+z)^2 = 1 + 2z + z^2$. Not directly related.  
However, note that if we replace $z$ with $\bar{z}$?  
Since $|z|=1$, let $z=e^{i\theta}$. Then $\bar{z}=e^{-i\theta}$.  
The expression is symmetric under $\bar{z}$?  
$|1+z|$ changes.  
$|1-\bar{z}+\bar{z}^2| = |1-z+1/z|$. Since $|z|=1$, $|1-z^2 + z^{-1}|$?  
Actually, the term is symmetric under conjugation if we ignore $z \to -z$ (since square changes to $\bar{z}^2$).  
Let's check $E(-\bar{z})$.  
$|1-\bar{z}| + |1-\bar{z}-\bar{z}^2|$?  
$E(z) = |1+z| + |1-z+z^2|$.  
$E(\bar{z}) = |1+\bar{z}| + |1-\bar{z}+ \bar{z}^2|$.  
We know $|1+\bar{z}| = |1-z|$ (since $z, \bar{z}$ are conjugates).  
Also $|1-z+z^2|$. If $z=e^{i\theta}$, $\bar{z}=e^{-i\theta}$. Then $(z+\bar{z})$ is real.  
Let's substitute $\bar{z}$ for $z$.  
If $E(z) = |1+z| + |1-z+z^2|$, and we swap $z \to \bar{z}$.  
$E(\bar{z}) = |1+\bar{z}| + |1-\bar{z}+\bar{z}^2|$.  
Note that $|1+\bar{z}| = |1-z|$ since $\bar{z} + 1$ is the same as $1+z$.  
So $E(\bar{z}) = |1-z| + |1-\bar{z}+\bar{z}^2|$.  
Since $z \to \bar{z}$ implies we look at the point in conjugate plane.  
For $z=e^{i\theta}$, $E(\theta)$ is the distance function on unit circle.  

Let's try to express $1-z+z^2$ as a sum of squares or product terms.  
Consider the identity: $|a+b| \le |a|^2 + |b|^2$ (for positive real numbers).  
But here complex modulus.  

What if we interpret $1+z$ and $1-z+z^2$ as distances from the origin?  
The expression is $\sqrt{u^2} + \sqrt{v^2}$ where $u, v$ are vectors.  
Let's try to express it in terms of a function $f(\theta) = 4\cos^2(\theta/2)$ and another term involving $\sin$.  
Let $z = \tan(\phi)$. Then $\theta$ is not necessarily $\pi/4$.  
Actually, let's substitute $z = e^{i\theta}$ into the expression.  
$E(z) = |1+e^{i\theta}| + |1-e^{i\theta}+e^{-2i\theta}|$.  
This can be written as:  
$E(z) = \sqrt{(1+\cos\theta)^2 + \sin^2\theta} + | (1-\cos 2\theta - 2\sin\theta \dots)?  
The second term: $|1-e^{i\theta}-e^{2i\theta}|$.  
Let's try to simplify this sum using complex numbers.  
Consider the function $f(w) = |w-1|^2 + |w^2+...|$.  
Note that for $z \in S^1$, we can use $z=e^{i\theta}$.  
$E(z) = \sqrt{4\cos^2(\theta/2)} + |(1-\cos 2\theta)^2 + (\sin 2\theta)^2|^{1/2}$?  
Let's simplify the second term modulus squared.  
$(1-e^{i\theta}+e^{2i\theta})^2$ is messy.  

Let's use the identity $|1-z+z^2| = |1-z+z^2|$ (using symmetry $\bar{z}$).  
Consider the points in the complex plane:  
We want to maximize distance from 0 for $T_1$, plus distance from origin?  
Is there a point on the unit circle that minimizes this sum?  
Or maybe find a specific angle where values are maximal.  

Let's re-evaluate $\theta = \pi/3$ ($z = e^{i\pi/3}$).  
$|1+z|^2 = 3$, $|1+z|=\sqrt{3}$.  
$T_2$:  
$z^2 = e^{-i\pi/3}$.  
$1-z+z^2 = 1 - (e^{i\pi/3}) + e^{-i\pi/3}$.  
Using Euler: $1 - (\cos \theta + i \sin \theta) + (\cos \theta - i \sin \theta)$.  
With $\theta=\pi/3$: $\cos=-1/2$, $\sin=-\sqrt{3}/2$?  
$\theta = 60^\circ$.  
$z = e^{i\pi/3} = \cos 60 + i \sin 60 = 1/2 + i\sqrt{3}/2$.  
Then $-z = -1/2 - i\sqrt{3}/2$.  
And $z^2 = e^{-i\pi/3} = 1/2 - i\sqrt{3}/2$.  
So $1-z+z^2 = 1 - (1/2 + i\sqrt{3}/2) + (1/2 - i\sqrt{3}/2)$.  
$= 1 - 1/2 - i\sqrt{3}/2 + 1/2 - i\sqrt{3}/2$.  
$= 1 - i\sqrt{3}$.  
The magnitude $|1-i\sqrt{3}| = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{4} = 2$.  
So at $\theta = 60^\circ$, the sum is $\sqrt{3} + 2 \approx 2.732 + 2 = 5.732$?  
Let me re-calculate $|1-i\sqrt{3}|$.  
Real part: $1$. Imaginary part: $-\sqrt{3}$.  
So magnitude is $\sqrt{1 + 3} = \sqrt{4} = 2$.  
Sum was $\sqrt{3} + 2 \approx 3.732$?  
Let me re-check the calculation of $T_2$.  
$|1-z+z^2|$ with $z=e^{i\pi/3}$.  
$1-z+z^2 = 1 - (1/2 + i\sqrt{3}/2) + (1/2 - i\sqrt{3}/2)$.  
Real part: $1 - 1/2 + 1/2 = 1$.  
Imaginary part: $-i\sqrt{3}/2 - (-i\sqrt{3}/2) = 0$?  
No. $z^2$ has imaginary part negative.  
Let's use $z^2 = e^{i(-60)} = \cos(-60) + i \sin(-60)$.  
So $1-z+z^2 = 1 - (\cos 60 + i \sin 60) + (\cos 60 - i \sin 60)$.  
Real part: $1 - 1/2 + 1/2 = 1$.  
Imaginary part: $-i\sqrt{3}/2 - (-i\sqrt{3}/2) = 0$?  
No.  
Let's write it explicitly:  
$z = \frac{1}{2} + i \frac{\sqrt{3}}{2}$.  
$z^2 = e^{-i\pi/3} = \frac{1}{2} - i \frac{\sqrt{3}}{2}$?  
$e^{ix} \cos x + i \sin x \sin x$.  
$z = e^{i 60}$. $z^2 = e^{-i 60}$ (if using $-60$, which is $120$ degrees).  
$e^{i \pi/3} = \cos(60) + i \sin(60) = 1/2 + i\sqrt{3}/2$.  
Then $z^2 = e^{-i \pi/3} = \cos(-60) - i \sin(-60)$?  
$e^{-i 60}$ is $\cos 60 + i \sin 60$ if we write $\theta$ positive.  
So $z^2 = \frac{1}{2} - i \frac{\sqrt{3}}{2}$ is correct if we take principal value for angle?  
Usually, $e^{i \phi} = \cos \phi + i \sin \phi$.  
So $z^2$ corresponds to angle $-60^\circ$.  
So $\cos(-60) = 1/2$, $\sin(-60) = -\sqrt{3}/2$.  
Then $z^2 = 1/2 - i\sqrt{3}/2$.  
The term is $1-z+z^2$.  
Real part: $1 - 1/2 + 1/2 = 1$?  
$\cos(-60) = 1/2$, so $\cos(60)$?  
The imaginary part for $z$ (angle $\pi/3$):  
$-i \frac{\sqrt{3}}{2}$.  
So term: $1 - z + z^2$.  
Real part: $1 - 1/2 + 1/2 = 1$.  
Imaginary part: $-i\sqrt{3}/2 - i(-\sqrt{3}/2) = 0$?  
Let's re-evaluate carefully.  
Real part of $z$: $1/2$.  
Imaginary part of $z^2$: $\cos(-60) - i \sin(-60) = 1/2 + i(\sqrt{3}/2)$?  
Or $\cos(60) = 1/2$, $\sin(60) = \sqrt{3}/2$.  
If $e^{i\theta} = \cos \theta + i \sin \theta$.  
For $\theta = -60^\circ$: $\cos(-60) = 1/2$, $\sin(-60) = -\sqrt{3}/2$.  
So $z^2 = 1/2 - i\sqrt{3}/2$?  
Then $1 - z + z^2 = 1 - (1/2 + i \sqrt{3}/2) + (1/2 - i\sqrt{3}/2)$?  
Real part: $1 - 1/2 + 1/2 = 1$.  
Imaginary part: $-i\sqrt{3}/2 - (-i\sqrt{3}/2) = 0$?  
Let's check again.  
$z^2 = e^{-i\pi/3} = \cos(-60) - i \sin(-60)$?  
$\cos(-60) = 1/2$.  
$\sin(-60) = -\sqrt{3}/2$.  
So $z^2 = 1/2 + i(-\sqrt{3}/2)$?  
Yes.  
So real part: $1 - 1/2 + 1/2 = 1$ is wrong?  
Real part of $1-z+z^2$:  
$z = 1/2 + i\sqrt{3}/2$.  
$z^2 = 1/2 - i\sqrt{3}/2$. (Note: $e^{-i \pi/3} = e^{i(-\pi/3)} = \cos(-\pi/3) + i \sin(-\pi/3)$).  
$\theta=-60$ is $\pi/3$ in some contexts, but standard notation $\theta$.  
So $\cos(60)=1/2$, $\sin(60)=\sqrt{3}/2$.  
$\theta = -60$.  
Real part: $1 - 1/2 + 1/2 = 1$.  
Imaginary part: $-i\sqrt{3}/2 - (-i \frac{\sqrt{3}}{2}) = 0$?  
This implies $z^2$ has same imaginary part as $z$?  
$z = e^{i\pi/3}$. Imaginary part is $\sqrt{3}/2$.  
So $z^2 = e^{-i\pi/3}$ (if we use polar angle).  
If $\theta = -60$, $e^{i(-60)}$. $\cos(-60)=1/2$.  
$\sin(-60) = -\sqrt{3}/2$.  
So real part: $1 - 1/2 + 1/2 = 1$.  
Imaginary part: $- \frac{\sqrt{3}}{2} - (- \frac{\sqrt{3}}{2})$?  
This depends on $z^2$.  
Let's stick to coordinates.  
$z = \cos 60^\circ + i \sin 60^\circ = 1/2 + i\sqrt{3}/2$.  
Then $z^2 = e^{-i(60)}$?  
If $\theta = -60$, then $e^{i(-60)} = \cos(-60) + i\sin(-60)$.  
$\cos(-60)=1/2$.  
$\sin(-60)=-\sqrt{3}/2$.  
So $z^2 = 1/2 - i\sqrt{3}/2$.  
Then $1-z+z^2 = 1 - (1/2 + i\sqrt{3}/2) + (1/2 - i\sqrt{3}/2)$?  
$= 1 - 1/2 + 1/2 = 1$.  
Imaginary part: $-i\sqrt{3}/2 - (-i\sqrt{3}/2) = 0$.  
So term is $|1-i\sqrt{3}|$?  
Real part: $1$, Imaginary part: $\sqrt{3}$ (if from $-z+z^2$).  
Let's calculate properly:  
$1 - z + z^2 = 1 - (\cos 60 + i \sin 60) + (\cos(-60) - i \sin(-60))$.  
Real part of sum: $1 - 1/2 + 1/2 = 1$.  
Imaginary part of sum: $-i\sqrt{3}/2 - (-i\sqrt{3}/2)$?  
$z = e^{i60}$. $\sin 60 = \sqrt{3}/2$.  
So term is $-i(\sqrt{3}/2)$.  
$z^2 = e^{-i60}$. $\sin(-60) = -\sqrt{3}/2$.  
So imaginary part is $-(1/2) - (-i\sqrt{3}/2)?$  
Let's write out terms:  
Real: $1 + (1/2-1/2) = 1$?  
Imag: $- \sin(60) - (- \sin(-60))$.  
$\sin(60)=\sqrt{3}/2$.  
$\sin(-60)=-\sqrt{3}/2$.  
So Im part is $-i(\frac{\sqrt{3}}{2}) + i(\frac{\sqrt{3}}{2}) = 0$?  
This means real part and imag parts cancel out.  
Is there a mistake in my calculation of imaginary part?  
$1 - z + z^2$.  
If $z = e^{i\pi/3}$, then $z^2 = e^{-i\pi/3} = 1/2 - i\sqrt{3}/2$.  
$z = 1/2 + i\sqrt{3}/2$.  
So $1-z+z^2 = 1 - (1/2 + i\sqrt{3}/2) + (1/2 - i\sqrt{3}/2)$?  
Let's check the signs.  
$i\sin \theta$ terms.  
Real: $1 - 1/2 + 1/2 = 1$.  
Imag: $- \sqrt{3}/2 - (-\sqrt{3}/2) = 0$?  
If $\theta=60$, $z^2$ is at angle $-60$.  
So $z^2 = \cos(-60) + i \sin(-60)$.  
$\cos(-60)=1/2$.  
$\sin(-60)=-\sqrt{3}/2$.  
So $z^2 = 1/2 - i\sqrt{3}/2$.  
Then $1-z+z^2 = 1 - z + z^2 = 1 - (1/2 + i\sqrt{3}/2) + (1/2 - i\sqrt{3}/2)$?  
Real part: $1 - 1/2 + 1/2 = 1$.  
Imaginary part: $-i\sqrt{3}/2 - (-i\sqrt{3}/2)$ is NOT correct.  
Let's re-evaluate imaginary parts.  
$z$ term is $-(i\sqrt{3}/2)$.  
$z^2$ term is $+(-i\sqrt{3}/2)$.  
Sum: $-1/2 + (-1/2 - i\sqrt{3}/2)$?  
Real part of $-z$: $-(1/2 + i\sqrt{3}/2)$, so real part $-1/2$.  
Imaginary part is $-i(\sqrt{3}/2)$.  
$z^2$ term: $+(1/2 - i\sqrt{3}/2)$. So imag part is $+(-i\sqrt{3}/2)$.  
Sum of imaginary parts: $- \frac{\sqrt{3}}{2} - \frac{\sqrt{3}}{2}$?  
Let's write it properly.  
$1 - z + z^2 = 1 - z + z^2$ ?  
$z = 1/2 + i\sqrt{3}/2$.  
$z^2 = 1/2 - i\sqrt{3}/2$.  
$1 - z + z^2 = 1 - (1/2 + i\sqrt{3}/2) + (1/2 - i\sqrt{3}/2)$?  
Is $1/z = e^{-i60} = 1/2 - i\sqrt{3}/2$?  
Let's re-evaluate the sum.  
Real part: $1 - 1/2 + 1/2 = 1$.  
Imaginary part: $- \frac{\sqrt{3}}{2} - (-i(\sqrt{3}/2))$.  
The imaginary term of $z$ is $+i\sqrt{3}/2$.  
The imag term of $z^2$ is $-i\sqrt{3}/2$.  
So sum: $- \frac{\sqrt{3}}{2} - (- \frac{\sqrt{3}}{2}) = 0$.  
This means the imaginary part cancels out.  
Is this true?  
Let's re-evaluate $z^2$.  
$z^2 = e^{i(2\pi/3)}$ or something else.  
If $\theta = -60$, then $e^{i(-60)} = \cos(-60) + i \sin(-60)$?  
This is $1/2 - i\sqrt{3}/2$. Yes.  
So sum is 0.  
Then term magnitude is $\sqrt{1^2 + 0^2} = 1$.  
So at $\theta=60$, $T_2 = 1$.  
And $T_1 = \sqrt{3}$.  
Sum $\approx 2.732$.  

Let's try a different point.  
If we take $z$ such that $1-z+z^2 = 0$.  
This requires roots of unity equation: $z^2 - z + 1 = 0$.  
Roots are complex, magnitude not 1.  
So this term is never zero on unit circle.  

Let's check the geometric interpretation again.  
We have $1+z$ and $1-z+z^2$.  
Maybe use the identity $|a+b|^2 + |c+d|^2 \ge 0$.  
Is there a point where $T_2 = T_1$? Or $T_2 = \sqrt{3} - T_1$?  
Try $\theta = \pi/3$. $T_1 = \sqrt{3}$. $T_2=1$. Sum $=\sqrt{3}+1$.  
Try $\theta = 0$. $z=1$. $T_1=2$. $T_2=1$. Sum $=3$.  
Try $\theta = -\pi/6$ ($z = e^{-i\pi/6} = \cos(-30) + i \sin(-30)$).  
$z^2 = \cos(150) = -\sqrt{3}/2$?  
$\sin(-30)=-1/2$.  
Let's check $T_2$ magnitude for general $\theta$.  
We can maximize $|1+z|^2 + |1-z+z^2|^2$.  
Using polar coordinates:  
$|1+z|^2 = 4\cos^2(\theta/2)$.  
$|1-z+z^2|^2$?  
Let's compute $(1-z+z^2)(1-\bar{z}-\bar{z^2})$.  
We know $|a+b-c|^2 = |a-b+c|^2$.  
Actually, $T_2 = |(1+z)^{-1}(1 - \dots)|$?  
Let's try to express $T_2$ in terms of $z$.  
Is there an algebraic structure?  
Maybe use substitution $w = z^2$. Then $|1+w^{1/2} + 1 - w^{-1}|$?  
Or simply:  
$E(z) = \sqrt{(1+\cos\theta)^2+\sin^2\theta} + | \sqrt{(1-\cos\theta)^2+\sin^2\theta} \dots$?  
Actually, the second term $|1-z+z^2|$ can be written as $\sqrt{ (1-\cos\theta) + \cos(2\theta) }^2$?  
$|1-z+z^2|^2 = |(1-z)+z^2||1+\dots|$?  
Let's check the term $1-z+z^2$.  
It is a rotation of vector $(1, -1)$ by angle...  
Consider the triangle inequality: $|1-z+z^2| \le |1-z| + |z^2-1|$?  
Also note that $1-z+z^2 = 1 - z + e^{i\theta}$.  
Let's go back to the idea of vectors.  
We want to maximize $|A| + |B|$ where $A=1+z$ and $B=1-z+z^2$.  
Note that for any complex number $w$, if we consider $z$ as vector $\mathbf{v}$, then $1+z$ is vector $\mathbf{u} = 1+\mathbf{v}$.  
The term $1-z+z^2$ is not simply $|u|$ and $|v|$.  
It looks like $T_2 = |z(1) + (1-z)(1-z^{-1})|$?  
Is there a relation between these vectors?  
Let's try substituting $x \to z/2$.  
If we use the property of maximums in such problems, often it occurs when terms align.  
Let's try to maximize with respect to the argument $\theta$ for fixed real part.  

Wait! I might have missed something about the term $1-z+z^2$.  
Is it possible that $|1-z+z^2|$ can be bounded by something like $\sqrt{2}$?  
Consider the identity:  
$|1-z+z^2|^2 = | (z-1)(z+1) - z^2 + \dots |$  
Actually, let's use the property of unit circle.  
Let $z \to e^{i\theta}$.  
$T_1 = 2|\cos(\theta/2)|$.  
$T_2 = |\sqrt{3}| \cos(\alpha)$?  
Let's compute $T_2^2$ explicitly for various $\theta$.  
$\theta = \pi$: $z=-1$. $T_1=0, T_2=|1-(-1)+1|=3$. Sum=3.  
$\theta = 2\pi/3$: $z=e^{i2\pi/3}$.  
$z^2 = e^{i4\pi/3}$.  
$T_1 = |1+e^{i2\pi/3}| = \sqrt{ (1+\cos 60)^2 + (\sin 60)^2 } = \sqrt{(5/4) + 3/4} = \sqrt{2}$?  
Let's calculate properly. $|1+z|^2 = 1+2\cos(60)+\cos^2(60) = 1+1+1 = 3$?  
$z=e^{i2\pi/3} = -1/2 + i\sqrt{3}/2$.  
$1+z = 1/2 + i\sqrt{3}/2$. Magnitude $\sqrt{1/4+3/4} = \sqrt{1}=1$?  
No. $1/2$ is real, $i\sqrt{3}/2$. Sum of squares is $1/4 + 3/4 = 1$. So magnitude is 1.  
So $T_1=1$.  
$T_2 = |1-z+z^2|$.  
$z = -1/2 + i\sqrt{3}/2$.  
$z^2 = e^{-i2\pi/3} = -1/2 - i\sqrt{3}/2$.  
$1-z+z^2 = 1 - (-1/2 + i\sqrt{3}/2) + (-1/2 - i\sqrt{3}/2)$?  
Real: $1 - (-1/2) + (-1/2) = 1$.  
Imag: $- \sqrt{3}/2 - (-\sqrt{3}/2) = 0$.  
So magnitude is 1.  
Sum is $1+1=2$.  

$\theta = 0$: Sum = 3.  
$\theta = \pi/2$: $z=i$.  
$T_1 = |1+i| = \sqrt{2}$.  
$T_2 = |1-i-1| = |-i| = 1$.  
Sum is $\sqrt{2}+1 \approx 2.414$.  

Is there a case where $T_2^2 + T_1^2$ is large?  
Let's try to find the maximum of this expression numerically or analytically.  
Maybe the answer involves solving an inequality like $\sqrt{3} + |\dots| \le \dots$.  
The problem statement: "Find the maximum value".  
If the max is 3, and we found a point where sum is 3 (z=1), that's valid.  
Can we get larger?  
Consider $z = -1/2 + i\sqrt{3}/2$ (which has magnitude 1). $T_1=1$.  
If we take $z=e^{i\pi}$, $z=-1$. Sum=3.  
So 3 is a possible maximum.  

Let's check $|1+z|$ and $|1-z+z^2|$ values again.  
Is it possible to have $T_2$ larger than $|1+z|$?  
If we set $T_2 = T_1$, sum is $2\sqrt{...}$.  
Let's look at the expression:  
$|1+z| + |z^2 - z + 1|$? (Since $z^2-1-z+1=z(z-1)$?)  
$1-z+z^2 = z(z+1)$.  
So $|z(z+1)|$.  
Then we have $|1+z| + |z^2(1+z)|$?  
Actually $1-z+z^2 = (1+z)(1+z^{-1}) - z$?  
Let's factor: $1-z+z^2 = 1 - z + z^2 = z(z  

## Answer

*(none: the token cap hit during thinking)*
