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

*Continued in [part 2 of 3](intermediate_algebra_1806_p2.md): GitHub stops rendering math on pages this long, so the transcript is split.*
