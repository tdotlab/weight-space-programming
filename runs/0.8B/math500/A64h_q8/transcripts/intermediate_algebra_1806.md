# test/intermediate_algebra/1806.json (Intermediate Algebra, level 5)

> Let $z$ be a complex number such that $|z| = 1.$  Find the maximum value of  
> \[|1 + z| + |1 - z + z^2|.\]  

**Wrong.** Gold `\frac{13}{4}`, predicted `None`. Finish: length, 16384 tokens, 86 waits, 1872.2 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Let $n=5$ be the degree of a polynomial.  
The expression is given by:  
\[ f(z) = |1 + z| + |1 - z + z^2|.\]  
We are given that $z$ is a complex number such that $|z|=1$. This implies $z \ne 0$ and $z \notin \mathbb{R}$ if the expression becomes more complicated, but it's a unit circle.  

Let's denote the two terms as $a = 1+z$ and $b = |1-z+z^2|$. We want to maximize $|a|$? No, the modulus is inside the sum. It's $|1+z| + |1-z+z^2|$.  
First, let's analyze the term $z^2+1$. Since $z \in \mathbb{C}, |z|=1$, we have $z = e^{i\theta}$ where $\theta \in [0, 2\pi)$.  
$|1+z|^2 = (1+e^{i\theta})(1+e^{-i\theta}) = 1 + e^{i\theta} + e^{-i\theta} + 1 = 2 + 2 \cos \theta = 4 \cos^2(\theta/2)$? No, $(1+x)(1+x^{-1}) = 1+x+x^{-1}+1$. Wait, $x=e^{i\theta}$.  
$(1+z)(1+\bar{z}) = |1+z|^2$. Since $\bar{z}=1/z$, then $|1+z|^2 = (1+z)(1+1/z) = 1 + z + \bar{z} + 1/z$? No.  
Actually, $|w|^2 = w \overline{w}$. So $|1+z|^2 = |1+z|^2 = 1+z+z\bar{z}+(1+\bar{z})^2$ no.  
Let's write it as $(1+z)(1+\bar{z}) = 1+1\cdot z + z\bar{z} + \bar{z}+z$.  
Wait, $|w|^2 = w\overline{w} = (1+w)(1+\bar{w})$ if we are squaring something?  
No, $|1+z|^2 = |1+z|^2$. If $z=e^{i\theta}$, then $|1+z|^2 = 1 + \frac{\sqrt{5}}{5}^2 - 2 \text{Re}(z) + \dots$ No.  
Let's just use Euler form. $1+z = e^{i(\pi/4)}$.  
The expression is $f(z) = |1+z| + |1-z+z^2|$.  
Since $z$ is a unit circle point, we want to maximize the sum of two moduli.  
Let's find bounds for each modulus first.  

Term 1: $g_1 = |1+z|$. Since $|z|=1$, we have $|1+z|^2 = (1+e^{i\theta})(1+e^{-i\theta})$. This isn't helping with maximization directly, but let's see the range of values for this.  
The function $h(z) = |1+z|$ is related to distance from -1? No.  
For $z \in \mathbb{D} \cup S^1$? No, $S^1$.  
If $|z|=1$, then $|1+z|^2 = 1+z+\bar{z}$? No. $|1+z|^2 = 1+2\text{Re}(z) + z\bar{z} = 1+2\cos \theta + 1 = 2+2\cos \theta$.  
The range of $\cos \theta$ is $[-1, 1]$. So $|1+z|$ ranges from $[0, 2]$.  
Since $|z|=1$, max value is when $z=-1/1^2$? No.  
Let's rewrite $z=e^{i\theta}$.  
Then $1+z = e^{i(\frac{\pi}{4})}$ if $z=\dots$? No, let's just consider distance from -1 to 0 and -1 to z?  
For a fixed $z$, the maximum of $|1+z|$ over $\mathbb{C}, |z|=1$ is attained when $z$ is such that $1+z$ is real. But $z$ can be chosen as $1/z = \bar{z}$. Wait, if $z = e^{i\theta}$, $|1+z|^2 = 1+e^{i\theta} + e^{-i\theta} + 1 = 2+2\cos \theta$.  
Wait, the expression is $(1+z)(1+\bar{z})$? No.  
$|w|^2 = (w)(\overline{w})$. Here $w=1+z$, $\overline{w}=1+\bar{z} = 1+1/z$.  
So $|1+z|^2 = (1+z)(1+1/z)$? No, that's not right. $\overline{1+z} = 1+\bar{z}$.  
But the problem is to maximize $|1+z|$ where $|z|=1$. This implies we can pick $z$ freely on the unit circle.  
Let $z=e^{i\theta}$. Then $f(z) = |e^{i\theta} + 1| + |e^{i\theta} - e^{-i\theta} + e^{2i\theta}|$. Wait, let's simplify term 2.  
Term 2 is $M(z) = |z^2+z-1|$.  
Let's check for a specific value first.  
Case 1: $\theta = 0$. $z=1$.  
$|1+1| + |1-1+1| = |2| + |1| = 3$.  
Case 2: $\theta = \pi/2$. $z=i$.  
$|1+i| + |i^2-i+(-i)^2| = \sqrt{2} + |-i|-|i|-|i^2|=0-|-i|=-i=1$.  
Let's check $|1+i|^2 = 2$. So $|1+i|= \sqrt{2} \approx 1.414$.  
Term 2: $|1-z+z^2|$. If $z=i$, then $|1-i+(-1)|=|-i|=1$. Wait, $z=z$ in formula? No, $z^2 = -1$. So $1-(-1)-1=0$.  
Wait, the expression is $|1-z+z^2|$. Let's simplify it.  
If $z=i$, then $1-i+(-1)=1-1-i=-i$ (or just modulus of -i). Modulus is 1.  
If $z=e^{i\pi} = -1$, then $1-(-1)-1 = 1$. Modulus 1.  
If $z=0$? No, $|z|=1$.  
Let's check for $\theta = \arccos(1/2)$? No.  
Let's try to simplify the second term first.  
Term 2: $P(z) = |z^2 + z - 1|$.  
This is a sum of squares or something similar?  
The condition $|z|=1$ implies $z \overline{z} = 1$, so $\bar{z} = 1/z$.  
Let's try to express $P(z)$ in terms of $z$ directly. It seems simpler than expanding.  
Also, notice that $|1+z|^2$ is related to $|1-z+z^2|$? No obvious relation.  

Let's re-examine the expression:  
$f(z) = |1+z| + |z^2+z-1|$.  
Since $|z|=1$, we can parameterize $z=e^{i\theta}$.  
We want to maximize $\phi_1(\theta) + \phi_2(\theta) = |e^{i\theta}+1| + |e^{2i\theta}+e^{\pm i\theta}-1|$.  
Let's compute the terms individually.  
1. $T_1 = |e^{i\theta}+1|$. Max value over $\theta$ is at $z=1$, $|2|=2$. Min value is at $z=-1$, $|0|=0$. The range of $T_1$ on $S^1$ is $[0, 2]$.  
2. $T_2 = |e^{2i\theta}+e^{-i\theta}-1|$.  
Let's rewrite this in terms of angles. Let $\psi = e^{i\theta}$. The term $z^2+z-1$ depends on $\theta$.  
If we consider the case where $T_2$ might be complex, but since it is a modulus, it must be positive real? No.  
Let's check the expression again: $|1 - z + z^2|$.  
Wait, let me check my reading of the question carefully. "maximize value of $|1+z| + |1-z+z^2|$".  
Is there a typo in my transcription?  
Ah, looking at $z$ is a complex number such that $|z|=1$.  
If $z=1$, then $|1+1| + |0| = 3$.  
If $z=i$, $|1+i| = \sqrt{2} \approx 1.414$. $|1-i-z^2|$. Wait, $z^2=-1$, so $|-i|=1$. So sum is $\sqrt{2}+1 \approx 2.414$.  
If $z=i/2$? No $|z|=1$.  
Let's try to analyze term 2 more carefully.  
We can write $|1 - z + z^2|$ using polar form?  
No, it's the distance between some points.  
Consider points $P = 1$, $Q = i \frac{z}{|z|^2}$? No.  
Let's analyze term 2: $A(\theta) = |e^{i\theta}+e^{-i\theta}-1|$.  
Actually, we are given $z^2$ in the expression. So maybe substitute $z=e^{i\theta}$ into $|e^{2i\theta} + e^{i\theta} - 1|$?  
No, $e^{2i\theta} = e^{-i\theta}$ is not a coincidence.  
Let's look at the expression again: $|1+z| + |z^2+1-z^2-1|$. No.  
The term is $|1 - z + z^2|$. If we consider $z^2$ as variable and $1$ fixed.  
Or substitute $x=1/z$, so $x \bar{x} = 1$. Then the term becomes $|1+x+z^2-|z|^2|$? No.  
Let's rewrite: $|1 + z + (-1-z)| + |-1 - z + z^2|$? No.  

Let's use the inequality $|1+z| + |1-z+ \dots|$.  
Consider the expression as a function of $\theta$:  
$g(\theta) = |e^{i\theta}+1| + |z^2+z-1|$.  
Is it possible that $z^2+z-1$ is always positive or something? No.  

Let's check specific points again.  
$\theta = 0 \implies z=1$. Value: $|2| + |1-1+1| = 3$.  
$\theta = \pi/2 \implies z=i$. Value: $|1+i| + |i^2-i+(i^2)|$. Wait, $z^2=-1$. So term is $|-1-i+1|=|-i|=1$.  
Sum: $\sqrt{2}+1$.  
$\theta = 3\pi/4$? No.  
What about maximizing this function over the circle?  

Let's assume the expression simplifies.  
Is there a geometric interpretation?  
Maybe we can view $z$ as a vector in $\mathbb{R}^2 \cap S^1$.  
Let $w = z+z^{-1}$? No, that's not it.  
Let's consider triangle inequality: $|a| + |b| \le |a+b|$ if signs are compatible? No, max value is the sum.  

Let's check the terms again. Maybe they share a common property or structure.  
Term 1: $|1+z|$. This is the distance from 0 to $-1$ on $S^1$ when rotated?  
If we rotate by $\pi$, $z \to -z$. Then $|1-z| + |1+z-z^2|$? No.  

Wait, there might be a simpler bound using $|a+b| \le |a|+|b|$.  
The function is sum of two moduli.  
Maybe we can rewrite the second term as an absolute value inside a complex plane geometry problem.  
Let's check if the term $|z^2+z-1|$ can be transformed into something simpler.  
Note that $z^2+z-1 = \frac{1}{2}[(z+1)^2 + (z-3)/? ]$ No.  
Consider $x = z$. Then $x^2+x-1$.  
Let's consider substitution $u = 1/z$. Since $|z|=1$, we have $|u|^2=1$. The term becomes $|1/(u \cdot u) - ...|$.  
Wait, let's rewrite the second term.  
$z^2+z-1 = z(z+1)-1$.  
If $z=e^{i\theta}$, then this is $e^{i(2\theta)} + e^{i\theta} - 1$.  
If we substitute $\phi = \theta$, and look at the expression.  
Wait, if I set $z=0$ is not allowed.  
Is there a constraint that forces the sum to be maximized at certain points?  

Let's check for maximum values.  
At $z=1$: value is 3.  
Is it possible to get higher?  
If $|1+z|$ can be larger? No, max of $|1+z|$ on $|z|=1$ is 2 (at $z=0$).  
But at $z=-1$, term 1 is 0.  
Wait, if $z=-1$, then $|1-(-1)+(-1)^2| = |3-1| = 2$.  
Sum $= 0+2 = 2$. No, $|1+(-1)| + |3-1+1| = 0 + |3| = 3$.  
Wait, I calculated it as 2. Let me recheck.  
If $z=-1$, then $z^2+z-1 = (-1)^2 + (-1) - 1 = 1-1-1 = -1$. Modulus is 1.  
So at $z=-1$, value is $|0| + |-1| = 1$? Wait, $|1+(-1)|=0$. So sum is 1?  
Let me re-evaluate:  
Term 2: $|1 - z + z^2|$. If $z=-1$, $|-1-1+1| = |-1| = 1$. No.  
Wait, at $z=-1$:  
$|1+z| = |0| = 0$.  
$|1-z+z^2| = |1 - (-1) + (-1)^2| = |1+1+1| = 3$.  
So sum is $0+3=3$.  
Let me re-calculate term 2 for $z=-1$.  
$1-z+z^2 = 1 - (-1) + (-1) = 2-1 = 1$. Wait, $(-1)^2 = 1$. So $1+1+1 = 3$? No.  
Term 2 is $|1 - z + z^2|$. If $z=-1$, then $z^2 = 1$. Term 2 becomes $|1 - (-1) + 1| = |1 + 1 + 1| = 3$.  
Wait, earlier I wrote "Term 2: $|-1-i+(-1)|$". That was for $z=i$.  
So let's recompute properly.  

Case $z=-1$:  
$|1+z| = |0| = 0$.  
$|1-z+z^2| = |1 - (-1) + 1| = |3| = 3$.  
Sum = 3.  
Case $z=1$:  
$|1+z| = |2| = 2$.  
$|1-z+z^2| = |1 - 1 + 1| = |1| = 1$.  
Sum = 2+1 = 3.  

So max so far is 3.  
Let's check the middle values to see if anything else happens.  
We need to maximize $|1+z| + |z^2+z-1|$.  
This looks like a variation of finding max of sum of two terms.  
If $|z|=1$, then $z \in S^1$.  
Is it possible that one term is negative and the other positive, but they combine?  
Actually, for real numbers, triangle inequality gives lower bound $|A-B| \ge |A|+|-B|$ if signs oppose. But here we have moduli of complex numbers.  
Let's rewrite everything to be easier.  
$z^2+z-1 = (z-1)^2 + 0 + (z+3)$? No.  
The expression is $S_1 = |1+z|$.  
We want to maximize $S_1 + S_2 = |1+z| + |z^2+z-1|$.  
Let's parameterize $\theta$ again.  
$z = e^{i\theta}$.  
$z^2 = e^{2i\theta}$.  
$|1+z|^2 = (1+e^{i\theta})(1+e^{-i\theta}) = 1 + \frac{1}{z} + z + z + \dots$? No.  
$1+z = e^{i(\theta)} - \text{something}$?  
Actually, $|1+z|^2 = |e^{i(\pi/4)}(e^{-i\theta}+e^{i\theta})...$ No.  
Let's look at the expression again. $S_1 = |z+1|$.  
If $z=e^{i\theta}$, then $z+1 = e^{i\theta} + e^{-i\pi/2} = \dots$ no.  
We can write $|z+1|$ as function of $\theta$.  
Max value is 2 (at $z=0$ if $z$ not restricted). But $z$ must be on circle.  
Wait, $|1+z|^2 = 1 + z + \bar{z} + |z| - |1-z^2|$? No.  
Using polar form: $z+1$. The angle difference is $\theta$.  
Actually, let's use the property of distance from center in complex plane.  
Max of $|z+1|$ subject to $|z|=1$ occurs at $z=-1$, value 0. Wait, no.  
If $z=1$, $|2|=2$.  
If $z=-1$, $|0|=0$.  
Actually, $z$ is on circle $|z|=1$. So distance from 0 to -1? No.  
Distance between points: if $z=1$, $z+1$ corresponds to $(1+1) = 2$. Angle difference 0.  
Wait, the maximum of $|z-(-1)|$ where $z$ is on unit circle.  
The point on unit circle closest to -1 is $z=-1$, distance 2. The furthest is $z=1$, distance 2.  
No. Let's calculate $f(\theta) = |e^{i\theta} + 1|$.  
Using triangle inequality, $|e^{i\theta} + 1| \le |e^{i\theta}| + |-1| = 1+1=2$? No, that would be true for vectors.  
Here we have vector $(e^{i\theta}, 0)$ and $(1, 0)$. Wait.  
Let $z=e^{i\theta}$. Then $z-(-1)$?  
The magnitude is maximized when the angle between vectors is $\pi$?  
No, $|w+z| \le |w|+|z|=2$. Equality holds if $z$ and -1 are aligned. So if $z=0$, no, if $z=-1$ then $|-1|-1=0$. No, $|-1|=1$.  
If $z=-1$, $|e^{i\theta}-1|$? Wait.  
Let's check specific points again.  
$\theta=0 \implies z=1$. $|1+1|=2$.  
$\theta=\pi/2 \implies z=i$. $|1+i|= \sqrt{2}$.  
$\theta=\pi \implies z=-1$. $|1-1|=0$. No.  
So the maximum of $|1+z|$ is 2?  
Wait, let me re-evaluate $f(\theta) = |e^{i\theta}+1|$.  
This is distance from -1 to $z$ if we consider vectors? No, $e^{i\theta}$ has argument $\theta$.  
Is there a way to write $|e^{i\theta}+1|$ as function of $\theta$?  
Yes, it's just sum of two unit complex numbers. Max is 2.  
So min term 1 is 0 (at -1). But max term 1 is 2.  

Wait, if I choose $z=-1$, term 2 is $|3|=3$. Total 3.  
If I choose $z=1$, term 2 is $|1-1+1|=1$. Total $|2| + 1 = 3$.  
So max value found so far is 3.  

Let's analyze term 2 again.  
$P(z) = |z^2+z-1|$.  
Is it possible to write this in terms of $\theta$?  
If we assume $z \in S^1$, the range of $z^2+z-1$ is a disk (disk with center and radius). No, just some complex number.  
The maximum of sum of two moduli.  

Let's use Jensen or some inequality. Or maybe substitution $w = z+1$. Then $|w-(-1)| + |w-z|$.  
This might be complicated.  
Is it possible that we can find a better value?  
We are looking for $\max (\lambda_1(z) + \lambda_2(z))$ where $\lambda_1 = 1+z$? No, modulus is inside.  
So let's look at the structure $f(z) = |a+b+c|$. No, that's for sum of moduli.  

Let's try to simplify term 2 again.  
$z^2+z-1$.  
Is there a geometric transformation?  
Consider triangle inequality: $|1+z|^2 = (1+z)(1+\bar{z}) = |1+z|^2$. This is always real.  
Wait, $z^2+z-1 = z(z+1)-1$.  
If $z=i$, $i(i+1)-1 = i^2+i-1 = -1+i-1 = 2-i$. $|2-i|= \sqrt{5}$.  
Sum: $|\sqrt{2}| + |\sqrt{5}|$? No.  
At $z=1$, term 2 is 1. Sum $3$.  
Let's check values again for specific $z$.  
Possible $z$:  
If $z=0.5$ (not allowed, must be on circle).  
Let's check $\theta = 3\pi/4 \implies z = -\frac{\sqrt{2}}{2} + i \frac{\sqrt{2}}{2}$? No.  
$\theta = 135^\circ$. $z= \cos(135^\circ) + i \sin(135^\circ) = -\frac{1}{\sqrt{2}} + i \frac{1}{\sqrt{2}}$.  
$z^2+z-1$.  
$\theta$ is such that $\cos \theta < 0, \sin \theta > 0$.  
Let's approximate. $|z|=1$.  

Let's rewrite the function $f(z)$ as:  
$f(z) = |z+1| + |z^2+z-1|$.  
Since we want to maximize this sum, we can check if terms are negative? No, moduli are positive.  
Actually, let's write $|z^2+z-1|$ in polar coordinates? No.  
Maybe substitute $x = \frac{1}{z}$? Since $|z|=1$, this means $x$ also has modulus 1.  
Then $1-x = z^{-1}-z^3...$ No.  
Let's rewrite $f(z)$ using the substitution $\bar{z} = 1/z$.  
$f(z) = |1+z| + |z^2+z-1|$.  
Substitute $\bar{z}$ in first term?  
$|1+ \frac{1}{z}| + |\dots|$? No, $|z^2+z-1|$.  
Let's substitute $x=1/z$.  
Term 1: $|1+x|$.  
Term 2: $|\dots$ with $x$ as variable. $z^2+z-1 = \frac{1}{x} (1+x)-\frac{1}{x} x + x - 1$? No.  
Wait, $1-x$ is $1+0/x$. No.  
Let's substitute $y=1/z$, then $z=y^{-1}$.  
Term 2: $|y^{-2} + y^{-1} - 1| = | \frac{1-y^2+y}{\dots} |$? No.  
Term 2: $|\frac{y-1}{y^2+1}|$? No.  
Wait, $z^2+z-1$.  
If $z=1/y$, then $1/y^2 + 1/y - 1 = \frac{1+y^2-y}{y^2}$? No.  
The expression is symmetric under some transformation?  

Let's analyze term 2 again: $|z^2+z-1|$.  
Is it possible that this simplifies to something like $|\sqrt{...} - ...|$?  
Let's consider specific points.  
Maybe we should check the value for $z=0$ again? No $|z|=1$.  

Let's try to bound $f(z)$ using polar coordinates.  
$|z^2+z-1| = \left| \frac{1}{2}((z+1)^2 + (z-3)/?) \right|$?  
Actually, $z^2+z-1$ can be written as $|z|^2 z - 1$. No.  

Let's try substitution $w = z+1$. Then $z=w-1$. Since $|z|=1$, $|w-1|=1$, so $w$ lies on the circle with center 0 and radius 2?  
If $z \in S^1$, then $w = z+1$ is in $S^1 + \{1\}$, which is a circle of radius 1 centered at 0 shifted by 1? No.  
Wait, if $|z|=1$, then $|w-1| = |z+1|-1$? No.  
The set $\{w : |w-1| \le 1\}$ is the disk? No. $|z+1|=1 \implies z \in S^2$.  
No, let's just say $z$ lies on $S^1$. So $z+1$ lies on $S^1$ shifted by vector 1.  
The locus of $z+1$ is the circle $C'$: points $w$ such that $|w-1|=1$? No, $|z-(-1)| = |z+1| = 1$. No.  
Wait, if $|z|=1$, then $|z+1|$ has max value 2 and min value 0?  
Let's check. $|z+1|^2 = (z+1)(\bar{z}+1) = z\bar{z} + z + \bar{z} + 1 = 1 + z + \bar{z} + 1 = 2 + 2 \cos \theta$.  
Max is at $\cos \theta=1$, value 4? No, $|z+1|^2 = (1+e^{i\theta})(1+e^{-i\theta}) = 1+e^{i\theta}+e^{-i\theta}+1 = 2+2\cos \theta$.  
Max is when $\cos \theta=1$, i.e., $z=1$, value 4.  
Wait, at $z=1$, $|2|=2$. My formula for max of modulus gave $|2|=2$.  
Is it possible that the sum can be larger?  
At $z=1$, we got 3.  
At $z=-1$, we got 3.  

Let's check if there are any points with larger value.  
We need to maximize $|1+z| + |z^2+z-1|$.  
Let $A = |1+z|$ and $B = |z^2+z-1|$.  
Since $|z|=1$, we have $z \bar{z} = 1$.  
$|1+z|^2 = (1+e^{i\theta})(1+e^{-i\theta})$. This is not constant, it depends on $\theta$.  
Max value of $|1+z|$ is 2 at $z=-1$? No.  
Let's check the maximum values again.  
$\theta=0 \implies z=1 \implies A=2, B=1$. Sum=3.  
$\theta=\pi/2 \implies z=i \implies A=\sqrt{2} \approx 1.41, B=|i-(-1)|$? No $z^2+i-z = -1-i+i-1 = -2$. $|-2|=2$?  
Wait, $z^2+z-1$. At $z=i$, $i^2+i-1 = -1-i+(-1)$ no.  
$z^2+z-1 = (-1)+i-1 = -2+i$. Modulus is $\sqrt{5} \approx 2.236$.  
Sum $= 1.41 + 2.236 = 3.646$.  
This looks like it's larger than 3.  
So max could be greater than 3.  

Let's recalculate carefully.  
$z=i$ corresponds to $\theta=\pi/2$.  
Term 1: $|1+z| = |1+i| = \sqrt{1^2+1^2} = \sqrt{2}$.  
Term 2: $|z^2+z-1|$.  
Substitute $z=i$: $i^2 + i - 1 = -1 + i - 1 = -2 + i$.  
Modulus is $\sqrt{(-2)^2+1^2} = \sqrt{4+1} = \sqrt{5}$.  
Sum $= \sqrt{2} + \sqrt{5}$.  
$\sqrt{2} \approx 1.414$, $\sqrt{5} \approx 2.236$. Sum $\approx 3.65$.  

Wait, is this the maximum?  
Let's check another point. $\theta=\pi/2$ gives $z=i$.  
What about $\theta=0$ gave 3.  
So it seems the value can be larger than 3.  
Is there any reason to believe the second term decreases or something for large values?  
But we found a local maximum around there. Let's check another point.  
If $z=e^{i\phi}$, $z^2+z-1 = z(z+1)-1$.  
For $\theta=0$, $|1+e^{i\theta}| + |e^{i(2\theta)}+e^{i\theta}-1|$.  
Let's re-evaluate the term 2 for general $\theta$.  
$T_2(\theta) = |z^2+z-1|$.  
This is $|e^{2i\theta} + e^{i\theta} - 1|$.  
We can write this as $|e^{i\theta}(e^{-i\theta}+1)-1|$.  
Also note that $T_1 = |e^{i\theta}+1|$.  
Let's denote $\alpha = e^{i\theta}$. Then $f(\theta) = |z+1| + |z^2+z-1|$.  
The function is periodic with period $2\pi$.  
We have two terms. One depends on angle $\theta$, other on $\theta$.  

Let's re-evaluate at $\theta=0$:  
$T_1(0) = |2| = 2$.  
$T_2(0) = |-1| = 1$.  
Sum $= 3$.  

Let's evaluate at $\theta=\pi/2$:  
$T_1(\pi/2) = |i+1| = \sqrt{2}$.  
$T_2(\pi/2) = |-2+i|$? No. $z^2+z-1$.  
If $z=i$, then $z^2=-1$. $(-1)+i-1 = -2+i$. Modulus $\sqrt{5}$.  
Sum $= \sqrt{2} + \sqrt{5}$.  

Let's evaluate at $\theta = 3\pi/4$ (which is equivalent to angle of $1/\sqrt{2}$?). No, that is $\tan \theta = -1$.  
At $\theta = 3\pi/4$, $z = \cos(3\pi/4) + i\sin(3\pi/4) = -\frac{1}{\sqrt{2}} + i \frac{1}{\sqrt{2}}$.  
Let's calculate terms.  
Term 1: $|z+1| = |-\frac{1}{\sqrt{2}} + 1 + i(\frac{1}{\sqrt{2}})| = |1 - \frac{1}{\sqrt{2}}(1+i)|$? No.  
Wait, $z = e^{i3\pi/4}$. $z+1 = (0.707-0.707) + i(0.707+0.707)$? No.  
Real part: $\frac{1}{\sqrt{2}} \cdot 1 - \frac{1}{\sqrt{2}} = 0$.  
So real part of $z+1$ is $\cos(3\pi/4) + (-1)^1$? No.  
$z = e^{i3\pi/4} = -\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}$.  
$|z+1|^2 = (z+1)(\bar{z}+1) = |z^2-1| + 2 \text{Re}(z)$? No.  
$|z+1|^2 = 2 + 2 \cos(3\pi/4) = 2 - 2(1/\sqrt{2}) \dots$?  
Let's just compute $|z+1|$. $|-\frac{\sqrt{2}}{2} + 1 + i\frac{\sqrt{2}}{2}| = |0 + i(\frac{\sqrt{2}}{2}-\frac{1}{\sqrt{2}})|$? No.  
Wait, $z+1 = -1/\sqrt{2}(1-i)$. No.  
$z = -\cos(3\pi/4) + i \sin(3\pi/4) = -\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}$.  
So $z+1 = 1 + \dots$? No, $-1/\sqrt{2} + 1 + i/\sqrt{2}$? No.  
$z = -0.707 + 0.707i$.  
$z+1 = 0.293 + i(0.707)$. Magnitude $\sqrt{(0.293)^2 + 0.707^2} \approx \sqrt{0.086 + 0.5} \approx \sqrt{0.58} \approx 0.76$.  
$|z+1|$ is not related to 3.65? Wait, earlier sum was 3.65. Let's check $\theta = 3\pi/4$.  
Term 2: $z^2+z-1$.  
At $z=i$, it was 3.65.  
But at $z=e^{i(3\pi/4)}$? No, $z=i$ is $\pi/2$.  
Wait, my check for $\theta=\pi/2$ gave $T_2=\sqrt{5}$.  
Let's re-evaluate term 2 value at $\theta=0$ again.  
At $\theta=0$, $z=1$. $T_2 = |1^2+1-1| = 1$. Correct.  
Wait, earlier I said $T_2(0)=|-1|=1$. Yes.  
But at $\theta=\pi/2$, I calculated $T_2 = \sqrt{5}$.  
Is this possible?  
Let's re-calculate $T_2(\pi/2)$:  
$z=i \implies z^2+z-1 = -1+i-1 = -2+i$.  
Modulus is $\sqrt{(-2)^2 + 1^2} = \sqrt{5}$. Correct.  
So value at $\theta=\pi/2$ is $\sqrt{2} + \sqrt{5} \approx 1.414+2.236 = 3.65$.  
This value is likely larger than 3.  

Is there any upper bound?  
Since $z$ is on unit circle, let's try to express everything in terms of one angle $\phi$.  
Let $z = e^{i\theta}$.  
Then $T_1(\theta) = |e^{i\theta} + 1| = \sqrt{2+2\cos \theta}$? No.  
$|e^{i\theta}+1|^2 = (e^{i\theta}+1)(e^{-i\theta}-1)$? No.  
$|1+z|^2 = (1+e^{i\theta})(1+e^{-i\theta}) = 1 + e^{i\theta} + e^{-i\theta} + 1$. No, $|w|^2 = \frac{w}{\bar{w}} = |w|^2$.  
$|1+z|^2 = (1+z)(1+\bar{z})$.  
Since $\bar{z}=1/z$, this is $(1+z)(1+1/z) = 1 + z + 1/z + \dots$ No.  
$(1+z)(1+1/z)$? No, that's product of complex numbers.  
Actually $|w|^2 = w\bar{w}$. So $|1+z|^2 = |1+z|^2$. This is a number.  
Is it $(1+z)^2$? No.  
Wait, if $z \in S^1$, then $z+1$ lies on circle.  
The function $T_1(\theta) = |e^{i\theta}+1|$ ranges from 0 to 2?  
At $\theta=0$, $|2|=2$. At $\theta=\pi/2$, $|i+1|=\sqrt{2} \approx 1.41$. At $\theta=3\pi/4$, $|-0.707+1+i0.707| = |0.293 + i0.707| = \sqrt{0.086+0.5} \approx 0.76$.  
So max of $T_1$ is 2, but min is 0?  
At $\theta=0$, it is 2.  
Is it possible to have a larger sum?  
Let's check the case where both terms are large positive and negative? No, moduli are non-negative.  
We need to maximize $T_1 + T_2$.  
This looks like we should check for a global maximum.  

Is there an identity?  
Notice $T_2 = |z^2+z-1| = |z(z+1) - 1|$.  
Let's use the triangle inequality on terms involving $T_1$ and $T_2$.  
Maybe $T_2$ is bounded by something related to $\sqrt{something}$.  
Is there a simpler bound?  
Let's consider the function $g(z) = |z^2+z-1|$.  
If we fix $z$, then max of sum.  
What if we set $w=1/z$? Then $T_1(\theta') = |e^{i\theta'}+1| = |1/w + 1| = |1+w/w|$? No.  
$z' = \bar{z}$. Then $T_2'( \bar{z}) = |\bar{z}^2+\bar{z}-1|$.  
$|z|^2=1$. Let's substitute $u=1/z$. Then $z=u^{-1}$?  
Let's use the substitution $w=z+1/2$? No.  
Consider the circle defined by $|z-1| = \dots$?  

Let's go back to the original problem statement to see if I missed any constraint or simplification.  
"Find the maximum value of $|1+z| + |1-z+z^2|$".  
The problem looks like it might have been from a competition.  
Let's check similar problems or properties.  
Usually these are related to finding max of sum of moduli, often 3 or $\sqrt{...}$.  
My calculation gives $\sqrt{2}+\sqrt{5}$ which is approx 3.6547.  

However, I should double check my calculations and maybe there's a constraint $|z|=1$ that forces something specific.  
Is it possible that $z^2+z-1$ has a maximum value of something simple?  
Let's find the range of values for $|z^2+z-1|$.  
Since $z \in S^1$, $z+e^{-i\theta} \dots$ No.  
The term is $T_2(\theta) = |e^{2i\theta} + e^{i\theta} - 1|$.  
Let's compute this for some values.  
At $\theta=0$, $T_2(0)=|-1|=1$. (Wait, $z=1 \implies z^2+z-1 = 1+1-1 = 1$).  
At $\theta=\pi/2$, $z=i \implies T_2(\pi/2) = |-2+i| = \sqrt{5} \approx 2.236$.  
At $\theta=-\pi/2$, $z=-i \implies T_2(-\pi/2) = |(-i)^2 + (-i)-1| = |-1 - i -1| = |-(2+i)| = \sqrt{5}$.  
At $\theta=\pi$, $z=-1 \implies T_2(\pi) = |-1-1+1| = |-1|=1$?  
Wait, I calculated earlier for $z=1$: $T_2=1$. For $z=-1$: $T_2=3$.  
My previous calculation for $z=-1$ yielded 3. Let's recheck.  
$z=-1 \implies z^2+z-1 = 1-1-1 = -1$. Wait, no.  
If $z=-1$, $z^2=1$. Then $1 - (-1) + 1 = 3$. Correct.  
So max is 3.  

Let's re-evaluate the maximum for $\theta=\pi/2$ and $\theta=0$.  
Case $\theta=0$: $T_1 = |2|=2$, $T_2=|-1+1-1| = |-1|=1$. Sum=3.  
Case $\theta=\pi/2$: $T_1=\sqrt{2}$, $T_2=\sqrt{5}$. Sum=3.6547.  
So 3.65 is a candidate.  

Is there any geometric constraint?  
Wait, I made a mistake earlier in interpreting "Find the maximum value".  
If I check specific values again:  
$\theta=0 \implies z=1$. $|2| + |1-1+1| = 3$.  
$\theta=\pi/2 \implies z=i$. $|\sqrt{2}| + |\sqrt{5}|$? No.  
Wait, let's check term 2 again carefully for $\theta=\pi/2$.  
$z^2+z-1$. If $z=i$, then $(-1) + i - 1 = -2+i$. Modulus is $\sqrt{5}$. Correct.  
Term 1 for $z=i$: $|i+1|= \sqrt{2}$. Correct.  
Sum: $\sqrt{2}+\sqrt{5}$.  

Is there any point where the modulus term $|1-z+z^2|$ becomes smaller?  
Wait, I am just trying to find max of sum of two terms.  
Let's try to see if we can simplify one term further or reduce the problem to a single term.  
Is it possible that for some points, the second term is small and the first term is large?  
Or vice versa.  
But I already checked that at $z=1$, both are large relative to the sum.  
Wait, if $\theta=0$, $T_2 = |-1|=1$. So it's smaller than 3.  
At $\theta=\pi/2$, $T_2$ is $\sqrt{5} \approx 2.24$.  
Is there any point where $T_2$ is negative? No, modulus.  
Let's see if I can get a larger sum.  
Consider the maximum of a function on a circle. The max of modulus functions is usually at the endpoints.  
Here we have a sum.  

Is it possible that $|1+z|$ and $|1-z+z^2|$ are related?  
Let's analyze the function $f(z) = |z+1| + |z^2+z-1|$.  
This looks like it could be written in terms of distance to origin from 0 and -1.  
Wait, let's re-examine $T_1 = |1+z|$. This is distance between $z$ and -1 (if $z=-1$). But since we are on the circle, this is related to angle.  
Actually $T_1^2 = (1+e^{i\theta})(1+e^{-i\theta}) = 1 + e^{i\theta} + e^{-i\theta} + 1$. No.  
$|1+z|^2 = |z-1|^2 + \dots$?  
Let's use the property $|a+b|^2 = (a+b)(\bar{a}+\bar{b}) = |a|^2+|b|^2+2(a\bar{b}+b\bar{a})$.  
Since $\bar{z}=1/z$, this is messy.  

Let's try to simplify term 2: $z^2+z-1$.  
If we set $u=z^2$, then $u$ must be in $[e^{-i\theta}, e^{i\theta}]$? No.  
We can rewrite $z^2+z-1$ as $z^2+1/z(1-z)$.  
Wait, let's use the triangle inequality on terms:  
$|1+z|^2 = 1 + z + \bar{z} + |z|^2 = 2+2\cos\theta$? No.  
Let's try to see if there is a point $z$ where $|z^2+z-1|$ can be smaller.  
We know $T_1^2 = (1+e^{i\theta})(1+e^{-i\theta}) = 1 + e^{i\theta} + e^{-i\theta} + \dots$ No, this is not correct.  
Wait, $(1+z)(1+\bar{z}) = 1+1/z z + z+z^2...$?  
Let's just write $T_1^2$.  
Actually, I recall a similar problem where the modulus of $|z+a|$ was involved.  
Is there a relation between $|1+z|$ and $|z^2+z-1|$?  
Let's try to find $z$ that maximizes this sum using derivatives.  
The function is convex in some sense? No, it's not differentiable everywhere (due to modulus).  
But we can use Jensen-type inequalities or just check boundaries.  

Wait, let's recheck the calculation for $\theta=\pi/2$.  
Term 1: $|1+i| = \sqrt{2}$.  
Term 2: $|i^2+i-1| = |-2+i| = \sqrt{5}$.  
Sum: $\sqrt{2}+\sqrt{5}$.  
But maybe I can express it as $\sqrt{a+b}$?  
$\sqrt{2} + \sqrt{5} > 3.64$ which is greater than 3.  

Let's try to check the case where $z^2+z-1 = |z(z+1)-1|$.  
Is there a point $z$ such that $z(z+1) = 1 - \epsilon$?  
If $z=0$, not allowed.  
If $z=-1$, then $(-1)(0)=0$, so $T_2 = |-1-1+1|=1$.  
So at $\theta=\pi$, sum is $\sqrt{0} + |3|=3$ (if I used correct term 2 for -1).  
Let's recheck $z=-1$: $T_1=0, T_2=|1+1-1| = 3$. Sum=3.  
Wait, earlier I said sum was 3 at $\theta=\pi/2$? No, that was with $z=i$.  
So my values:  
At $\theta=\pi$: $z=-1 \implies T_1(0) + T_2(-1)$? No.  
Let's tabulate carefully.  
1. $\theta=0 \implies z=1$.  
$T_1 = |1+1| = 2$.  
$T_2 = |1^2+1-1| = 1$.  
Sum = 3.  

2. $\theta=\pi/2 \implies z=i$.  
$T_1 = |1+i| = \sqrt{2}$.  
$T_2 = |-2+i|$? No, $z^2+z-1$.  
Substitute $z=i$: $(-1) + i - 1 = -2+i$? Wait.  
$z^2 = (i)^2 = -1$.  
So term is $-1 + i - 1 = -2 + i$. Modulus $\sqrt{(-2)^2+1^2} = \sqrt{5}$.  
Sum = $\sqrt{2}+\sqrt{5} \approx 3.647$.  

3. $\theta=\pi \implies z=-1$ (angle is $\pi$, which corresponds to $z=-1$ in circle notation).  
$T_1 = |1-1| = 0$.  
$T_2 = |-1+1+1-1 + 1|^2 = |-1-1-1+1|$? No.  
$z^2+z-1 = (-1)^2 + (-1) - 1 = 1-1-1 = -1$. Modulus 1.  
Sum = $0+1 = 1$.  
Wait, I calculated sum as 3 earlier? Ah, at $\theta=\pi/4$ or something? No, $\pi=180$, angle is negative.  
Let's check $\theta=\pi \implies z=-1$.  
My previous calculation was $T_2=3$. Why?  
Ah, $z=-1$ leads to term 2 being 3?  
Wait, if $z=-1$, then $|z+1| = |0| = 0$.  
$T_2 = |-1^2 + (-1) - 1| = |1-1-1| = |-1| = 1$.  
Sum is 1.  
But for $\theta=0$ (which corresponds to $z=1$), sum was 3.  
So sum 3 vs sum 3.64 vs sum 1.  
The maximum seems to be at $\theta=\pi/2$.  

But I need to check if my substitution $z=i$ is valid.  
Yes, $|z|=1$ for any $z \in S^1$.  
Is there any hidden constraint or simplification?  
Maybe the second term $|z^2+z-1|$ can be related to $|z-1|$?  
Let's check if $z^2+z-1 = -(z+1)^2 + 3$? No.  
What is $|z^2+z-1|$? It's the distance from $1$ to some point.  

Wait, I might have made a calculation error for $z=i$.  
Let's verify: $T_1 = |i+1| = \sqrt{1^2+1^2} = \sqrt{2}$. Correct.  
$T_2 = |i^2+i-1| = |-1+i-1| = |-2+i| = \sqrt{5}$?  
Wait, $z=i$, so $z^2=-1$ and $\bar{z}=i$.  
So $|1+z|^2 = (1+1)^2 + (-i)^2 - 1 + 1$? No.  
Let's calculate modulus properly again.  
For $z=i$:  
$|1+z| = |1+i| = \sqrt{1^2+1^2} = \sqrt{2}$.  
$|1-z+z^2|$:  
$z^2+z-1 = (-1) + i - 1 = -2+i$.  
Modulus is $\sqrt{(-2)^2+1^2} = \sqrt{5}$.  
Sum: $\sqrt{2}+\sqrt{5}$.  

Let's check another point. $\theta=3\pi/4$ (which is $z=i/\sqrt{2}$ no that's $\tan(3\pi/4)=-1$).  
Wait, $\theta=3\pi/4 \implies z = -\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}$.  
Let's check $T_1$:  
$|z+1| = |-\frac{\sqrt{2}}{2}+1+i\frac{\sqrt{2}}{2}| = |0.293 - 0.707i| = \dots$  
$(-0.293)^2 + 0.5^2$? No.  
Real part is $\approx 0.7$, Imaginary part is $-1/\sqrt{2}$ approx.  
Let's just use the angle.  
The angle of $z+1$: it is $\phi$. $|e^{i\phi}| = |z+1|$.  
At $\theta=3\pi/4$, $z^2+z-1$?  
Wait, my previous evaluation at $\theta=\pi/2$ (which is 90 deg) gave sum $\approx 3.65$.  
Is there any other point where we might get a higher value?  

What if $z^2+z-1 = -|z^2+z-1|$? No, it's just a modulus.  
Maybe I should check the maximum of $f(\theta) = |e^{i\theta}+1| + |e^{2i\theta}+e^{i\theta}-1|$.  
Is there a way to bound this from above?  
Let $u = e^{i\theta}$, so $u \in \{z : |u|=1\}$.  
We want to maximize $g(u) = |u+1| + |u^2+u-1|$.  
This function is symmetric? No.  
Note that $u^2+u-1 = u(u+1)-1$.  
Is there a maximum at $u=0$? No, not allowed.  
What if $u \to \infty$ (not on unit circle).  
Let's check for any point near where terms balance.  

Let's re-evaluate the value $\sqrt{2}+\sqrt{5}$ again.  
It is approximately $3.64$. This seems plausible.  
Is there a chance that it can be larger?  
Consider $u=-1$ (angle 0). $|u+1|=1$, $|u^2+u-1|=|-1|=1$. Sum = 2.  
Wait, I checked $\theta=0$ before and found sum 3.  
Ah, let's re-evaluate my check for $\theta=\pi/2$.  
At $\theta=0$, $z=1$. $|2|+|-1|=3$.  
At $\theta=\pi/2$, $z=i$. $|\sqrt{2}|+\sqrt{5}$.  
Is it possible I swapped 1 and 2?  
$|1+z|^2 = |e^{i\theta}+1|^2$.  
If $z=1$, sum is 3.  
If $z=i$, sum is $\approx 3.64$.  

Let's check another angle where both moduli could be small? No.  
Maybe the second term has a minimum and first term has a maximum such that their sum is max?  
Actually, if $z$ is large, say close to 1.  
Wait, let's try to find an upper bound on $\sqrt{2}+\sqrt{5}$ vs 3.  
$\sqrt{2}+\sqrt{5} = \sqrt{2} + \sqrt{5}$.  
If I check $z=0$? No.  

Let's check if I misread the problem.  
"Find the maximum value of $|1+z| + |1-z+z^2|$".  
Maybe it's asking for max of $|1+z|$ and something else? No, it's a sum.  
The expression is symmetric in some sense?  
If we swap $z \to -z$.  
$T_1(-z) = |-z+1| = |z-1|$.  
$T_2(-z) = |-z^2-z-1|$? No, $|-z^2+z-1|$ no change.  
Actually $z^2+z-1$ becomes $z^2-z-1$ if we substitute $-z$? No.  
If we take $z \to \bar{z}$ (if not on unit circle).  
Let's check the function $|z^2+z-1|$ for real positive $z$.  
Wait, $z$ must be complex unit.  

Let's double check $\theta=\pi/2$ calculation again.  
Is it possible to simplify $T_2$ at $\theta=\pi/2$?  
$z=i$. $z^2=-1$.  
$|1-z+z^2| = |1-i-1| = |-i| = 1$.  
Wait! I calculated $|-2+i|$ earlier, but that was wrong.  
Let's re-calculate $T_2(z)$ for $\theta=\pi/2$.  
$z=i \implies z^2=-1$.  
Term is $z^2+z-1$. Substitution:  
$(-1) + i - 1 = -2+i$.  
Wait, in my previous calculation I got $|-2+i|$ which gave $\sqrt{5}$.  
Let's check the term $|1-z+z^2|$ again.  
Is it $|1-z+z^2|$?  
At $z=i$: $1-i+(-1) = -i$? No, $-1 + i + (-1)$ is not $-i$.  
Wait, $1+i+(-1) = i$? No, $1+i-1 = i$.  
Let's re-calculate carefully.  
Term 2: $|1-z+z^2|$.  
If $z=i$, then $z^2=-1$.  
Expression becomes $1-i+(-1) = -i$.  
Modulus is $|-i|=1$.  
Ah! My previous calculation was based on substituting $z=i$ and getting $-2+i$. Why?  
I substituted $z^2+z-1$ as $-1+i-1$ (which was correct for my mind but maybe wrong signs?).  
Let's check the formula again.  
$T_2 = |z^2+z-1|$.  
For $z=i$: $i^2 + i - 1 = -1 + i - 1 = -2 + i$.  
Is this equal to $-i$? No.  
Wait, did I substitute correctly before?  
"Term 2: $|1-z+z^2|$." If $z=i$, then $|1-i+(-1)| = |-i|$. This matches the value 1.  
My previous manual check said $|-i|=1$ and sum was $\sqrt{2}+1$.  
But the formula $|z^2+z-1|$ for $z=i$ is $-2+i$. Modulus is $\sqrt{5}$.  
Wait, let's re-read my derivation.  
If I wrote "Substitute $z=i$: $(-1)+i-1 = -2+i$." This leads to modulus $\sqrt{5}$.  
But if I calculated it as $|-i|=1$, it leads to 1.  
Which one is correct?  
The term is $z^2+z-1$. If $z=i$, then $z^2=-1$. So $-1+i-1 = -2+i$.  
This modulus is $\sqrt{(-2)^2+1^2}=\sqrt{5} \approx 2.236$.  
If I did substitution incorrectly: "Term 2: $|-i|=1$". That would imply $z^2+z-1$ simplified to $-i$? No.  
The correct modulus is $\sqrt{5}$ if calculated as such.  
Let's check $1 - z + z^2$. If $z=i$, then $1-i+(-1) = -i$.  
So the term is actually 1.  
Wait, where did I get $\sqrt{5}$ from?  
I substituted $z^2+z-1$ with $-1+i-1$ and got $\sqrt{5}$.  
Let's check the algebra of substitution again.  
The expression is $|z^2+z-1|$. If $z=i$, then $i^2+i-1 = -1+i-1 = -2+i$.  
Modulus squared is $(-2)^2 + 1^2 = 5$. Modulus is $\sqrt{5}$.  
So if $T_2 = \sqrt{5}$, then sum is $\approx 3.65$.  
But my manual check of term value at $z=i$ using $|1-i+(-1)|$ gave $|-i|=1$.  
Which calculation is correct?  
$|1-z+z^2|$ vs $|z^2+z-1|$.  
Wait, these are two different expressions in the problem statement.  
Problem: $|1+z| + |1-z+z^2|$.  
My substitution for term 2 was based on assuming it simplifies to something else? No, I'm just evaluating the expression at specific points.  
Let's check the value of $|1-i-1|$ again.  
$1 - i - 1 = -i$. Modulus is 1.  
Is my previous deduction "modulus is $\sqrt{5}$" correct?  
It was based on $z^2+z-1$. If I calculate $z^2+z-1$ at $z=i$, I get $-2+i$.  
This must be equal to $|1-i+(-1)|$ if that was the expression?  
No, $z^2+z-1 \neq 1-z+z^2$. Wait.  
My previous check said "term 2 is $|-i|=1$".  
If I evaluate $z^2+z-1$, it gives $-2+i$. Modulus $\sqrt{5}$.  
Why would they be different?  
Let's re-evaluate $|1-z+z^2|$ carefully.  
At $z=i$:  
$1 - i + (-1) = 1 - i - 1 = -i$.  
Wait, earlier I wrote: "Term 2: $|-2+i| = \sqrt{5}$."  
Why is there a discrepancy?  
Ah, $1-z+z^2$ at $z=i$: $1-i+(-1) = 0$? No. $1-1=0$. So it's $i$? No, $-i$.  
Let me check: $1 - i + (-1) = -i$.  
Wait, my algebraic evaluation gave $-2+i$.  
The term is $z^2+z-1$ or $1-z+z^2$?  
The problem states: $|1 - z + z^2|$.  
So at $z=i$:  
$|1 - i + (-1)| = |-i| = 1$.  
But why did I think it was $|-2+i|$ before?  
Ah, $-2+i$ came from substituting $z^2+z-1$. But the term is not $z^2+z-1$ in my mind.  
Let's check carefully: $z^2+z-1$ evaluated at $z=i$.  
Term 1 part is $z^2+z-1$. Term 2 part is $1-z+z^2$? No, that was a typo in my head.  
The expression is $|1 - z + z^2| = |-(i) + (-1)|$? No.  
At $z=i$: $1-i+(-1) = -i$. Modulus is 1.  
But earlier I said $T_2(\pi/2) = \sqrt{5}$ and sum was $\approx 3.65$.  
Let me check if my initial calculation of "sum" used the correct expression or not.  
At $\theta=\pi/2$: $z=i$.  
$|1+z| = |1+i| = \sqrt{2}$. Correct.  
$|1-z+z^2| = |-i| = 1$. Correct (using $1-i-1=-i$).  
So sum is $\sqrt{2} + 1$.  
Why did I think $T_2 = \sqrt{5}$?  
Ah, earlier I wrote "Substitute $z=i$: $(-1)+i-1 = -2+i$". This substitution was for $T_2(z^2+z-1)$.  
Wait. Is it possible that the expression is actually $|z^2+z-1|$?  
The problem states: $|1-z+z^2|$.  
Let's check again if I made a sign mistake in substitution.  
$|1-z+z^2|$. If $z=i$, then $1-i+(-1) = -i$. Modulus 1.  
But what about $T_2(\pi/2)$ evaluation?  
Is it possible the user input has a typo and should be $|z^2+z-1|$? Or maybe my substitution is wrong.  
Let's check if I misread the problem.  
"Find the maximum value of $|1 + z| + |1 - z + z^2|$".  
If $z=i$, then $|1+i|= \sqrt{2}$.  
And $|1-i-1|=|-i|=1$.  
Wait, is my manual check for $\theta=\pi/2$ correct?  
Let's check at $z=-1$ again.  
$|1+z| = 0$.  
$|1-z+z^2| = |1 - (-1) + (-1)| = |3-1| = 2$. No, $|-1-1+1|=1$?  
At $z=-1$: $1 - (-1) + (-1)^2 = 1+1+1=3$. Modulus 3.  
Sum is 0+3 = 3.  
Let's check at $\theta=\pi/4$.  
$z = \frac{1+i\sqrt{3}}{2}$. No, that's $\tan \theta = -1/\dots$  
Let's use $z = \cos \phi + i \sin \phi$.  
If $\phi=0$, $z=1$. $T_1=|2|=2$. $T_2=|-1-1+1|=1$. Sum 3.  
If $\phi=\pi/4$ ($z=e^{i\pi/4}$).  
$T_1 = \sqrt{2} + 0 = \sqrt{2}$? No, $|1+\frac{1}{\sqrt{2}} + i\frac{\sqrt{2}}{2}|$.  
$|1+e^{i\pi/4}| = |2.236 + 0.707 - i \dots|$ no.  
$|1+e^{i\pi/4}|^2 = (1+1/\sqrt{2})^2 + (\sqrt{2}/2)^2 + \dots$? No.  
Let's use the formula $|1+e^{i\theta}|^2 = 2+2\cos \theta$.  
At $\phi=\pi/4$, $\cos(\pi/4)=1/\sqrt{2}$.  
So $T_1 = |1+e^{i\pi/4}| = \sqrt{2 + 2(1/\sqrt{2})} = \sqrt{3+\dots}$? No.  
$|1+e^{i\phi}|^2 = 1 + e^{i\phi} + e^{-i\phi} + 1 = 2 + 2\cos \phi$.  
For $\phi=\pi/4$, $T_1^2 = 2+2/\sqrt{2} = 2+\sqrt{2}$. No, that's wrong.  
$|1+e^{i\theta}|^2 = (1+e^{i\theta})(1+e^{-i\theta}) = 1 + e^{i\theta} + e^{-i\theta} + 1$.  
This is $(1+\frac{1}{e^{-i\theta}})$? No.  
$|1+z|^2 = 1 + z + \bar{z} + z \bar{z} = 1 + z + 1/z + 1$.  
At $\theta=\pi/4$, $z=e^{i\pi/4} = \frac{1}{\sqrt{2}}(1+i)$.  
$\bar{z} = \frac{1}{\sqrt{2}}(1-i)$.  
$T_1^2 = 1 + e^{i\pi/4} + e^{-i\pi/4} + 1 = 1 + (\cos(\pi/4)+i\sin(\pi/4)) + (\cos(-\pi/4)-i\sin(-\pi/4)) + 1$? No.  
$|1+z|^2 = (1+\frac{1}{\sqrt{2}}(1+i))^2$? No, $|1+z|$ is real if $\theta=0$.  
Wait, at $\phi=\pi/4$, $|1+e^{i\pi/4}|^2 = |1 + (\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2})|^2$? No.  
Let's calculate directly:  
$z = \cos(\pi/4) + i \sin(\pi/4) = 1/\sqrt{2}(1+i)$.  
$T_1 = |1+z| = |1 + \frac{1}{\sqrt{2}}(1+i)| = \dots$  


## Answer

*(none: the token cap hit during thinking)*
