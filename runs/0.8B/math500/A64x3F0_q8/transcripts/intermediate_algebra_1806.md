# test/intermediate_algebra/1806.json (Intermediate Algebra, level 5)

> Let $z$ be a complex number such that $|z| = 1.$  Find the maximum value of  
> \[|1 + z| + |1 - z + z^2|.\]  

**Wrong.** Gold `\frac{13}{4}`, predicted `None`. Finish: length, 16384 tokens, 16 waits, 1952.4 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Let $N = |1 + z| + |1 - z + z^2|$, where $z$ is a complex number with $|z| = 1$. We need to maximize this value.  

Let's simplify the expression inside the first absolute value, since $|z|=1$ means we are on the unit circle in the complex plane.  
Since $|z| \neq 0$, $\frac{1+z}{|z|} = z + \bar{z}$. The condition $|z| = 1$ implies that if $z$ is a complex number, then $z$ is on the unit circle. The term $1-z^2$ or something similar?  
The expression is $S(z) = |1+z| + |1 - z + z^2|$.  

Let's break down the first term: $T_1 = 1+z$. Since $|z|=1$, we can use trigonometric arguments or simply polar form.  
$z = e^{i\theta}$ for some $\theta \in [0, 2\pi)$. Then $1+z = 1 + e^{i\theta} = (e^{i\theta/2})^2 + 1 = -\cos(\theta) + i \sin(\theta)$? No.  
$z+1$ has modulus $|z+1| \le |1| + |z| = 2$ by triangle inequality. Equality holds if $z$ is real and positive, i.e., $z=1$. But here $z=e^{i\theta}$ with $|\theta|<\pi/2$.  
The maximum modulus of $1+z$ for $z \in D(0, 1)$ is at $z=1$ or $z=-1$, but we have unit modulus. So the max is 2? No, that's not right.  
Let $w = 1+z$. Since $|z|=1$, $z^{-1} = 1/z = \bar{z} + z$ no.  
We know $\frac{1+z}{|z+1|}$. Let's just compute the values for specific points or use polar coordinates.  

Let $z = e^{i\theta}$. Then $S(\theta) = |1 + e^{i\theta}| + |1 - e^{i\theta} + e^{2i\theta}|$.  
$1+z = 1 + \cos\theta + i \sin\theta$. So $|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta = 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta = 2 + 2\cos\theta$.  
Thus $|1+z| = \sqrt{2+2\cos\theta} = 2|\cos(\frac{\theta}{2})|$? No.  
$2+2\cos\theta = 2(1+\cos\theta) = 4\cos^2(\frac{\theta}{2})$. So $|1+z| = 2\cos(\frac{\theta}{2})$. This is only valid for $\cos(\frac{\theta}{2}) \ge 0$, i.e., $\theta \in [-\pi/2, \pi/2]$.  
If we are not restricting $\theta$ to that range, then $|1+z|$ could be negative? No modulus is non-negative.  
The modulus formula is $|w| = \sqrt{A+B} = \sqrt{(1+\cos\theta)^2 + \sin^2\theta}$ which simplifies to $\sqrt{2+2\cos\theta} = 2|\cos(\frac{\theta}{2})|$? No, $\sqrt{2(1+\cos\theta)} = \sqrt{4\cos^2(\frac{\theta}{2})}$. This is correct. However $|w| \le 2$ is always true for any $z$ on the unit circle if $z \neq 0$.  
But $z$ has $|z|=1$, so $z+1$ could be larger than 2?  
If $z=-1$, $|1+z|=2$. If $z=1$, $|1+z|=2$. If $z$ moves away from unit circle, the distance is smaller. So $|1+z| \le 2$.  
The formula $2\cos(\frac{\theta}{2})$ implies that for $|z|=1$, we must have $\cos(\frac{\theta}{2}) \ge 0$, which means $|\theta| \le \pi/2$? No, let's check.  
Let $z=e^{i\theta}$. Then $1+z = 1+\cos\theta + i\sin\theta$. Modulus is $\sqrt{2(1+\cos\theta)} = \sqrt{4\cos^2(\theta/2)} = 2|\cos(\frac{\theta}{2})|$. Since $z$ is on the unit circle, this formula works if $w=1+z$.  
But for general $|z|=1$, $\cos(\theta/2)$ can be negative. If we want to maximize $|1+z|$, we need to check if $\theta \in [0, \pi]$ or something else.  
The maximum of $2\cos(\frac{\theta}{2})$ on $[0, 2\pi]$ is 2 (when $\theta=0$). But here $z$ is a specific number? No, it's a set of possible numbers. $z$ can be chosen to maximize the modulus.  
However, $|1+z|$ depends only on $\cos(\frac{\theta}{2})$, so $\cos(\theta)$ matters.  
Let $x = \arg(1+z)$. If we choose $z$ such that $1+z=0$, then $|1+z|=0$. That's not what we want. We are looking for the maximum of a sum.  

Now let's look at the second term: $T_2 = |1 - z + z^2|$.  
We can use the identity $z^2 = (1-z)(1+z)$? No, $z^2+2z-1=0$ etc.  
Let's write everything in terms of polar coordinates or trigonometric functions.  
Let $z = \cos \theta + i \sin \theta$. Then $\cos 2\theta = (z+1/z)/\dots$  
Actually, simpler: Let $z = e^{i\phi}$ for some angle $\phi \in [0, 2\pi)$.  
Then $T_1 = |1+z| = 2|\cos(\frac{\phi}{2})|$? No.  
Let's check again.  
$|1 + e^{i\phi}|^2 = |e^{-i\phi}(e^{i(2+\phi)}-1)|^2$ ? No.  
$|1+e^{i\phi}|^2 = 1+e^{i\phi} + e^{-i\phi} + 1 = 2 + 2\cos\phi$.  
So $|1+z| = \sqrt{2+2\cos\phi} = 2|\cos(\frac{\phi}{2})|$ is wrong.  
$1 + e^{i\phi} = e^{i\phi/2}(e^{-i\phi/2} + e^{i\phi/2}) = e^{i\phi/2}(2\cos(\frac{\phi}{2}))$.  
So $|1+z|^2 = |2\cos(\frac{\phi}{2})|^2 = 4\cos^2(\frac{\phi}{2})$.  
Ah, I made a mistake in my initial thought. Let me recompute $|1+e^{i\phi}|^2$.  
$1 + e^{i\phi} = (1+\cos\phi) + i\sin\phi$.  
Modulus squared: $(1+\cos\phi)^2 + \sin^2\phi = 1 + 2\cos\phi + \cos^2\phi + \sin^2\phi = 2+2\cos\phi$.  
This is equal to $4\cos^2(\phi/2)$. Yes, it is. So $|1+z| = 2|\cos(\frac{\phi}{2})|$.  
However, the maximum value of $\cos(\phi/2)$ is 1 (when $\phi=0$), which gives max modulus $2(1)=2$. But $\cos(\phi/2)$ can be negative? No, modulus.  
But $\cos(\phi/2)$ cannot be negative because it's a square root inside the absolute value.  
So actually, $|1+z|$ is just $2|\cos(\frac{\phi}{2})|$. This means $|1+z|$ ranges in $[0, 2]$.  
However, if we choose $\phi = \pi$, $z=-1$, $|1+z|=2$. If we choose $\phi = 3\pi/4$, $|1+z|=\sqrt{2+2(-\frac{\sqrt{2}}{2})}...$ No.  
$\cos(\pi/2)=0 \implies |1+z|=0$. But this is possible for $z=i$? No. For $\phi = 3\pi/4$, $|1+i e^{i\pi/4}| = |1+e^{-i\pi/4} + i\sin(\pi/4)| = \sqrt{...}$  
Let's just use the polar form of $z$.  
The expression is $|1+z| + |1 - z + z^2|$.  
Note that $|1-z+z^2|$ looks like a rotated version of the problem.  
Wait, if we let $w = 1+z$, then $z = w-1$.  
Then $|z|=1$ implies $|w-1|=1$. So $w$ lies on a circle centered at 1 with radius 1.  
Let's analyze this substitution.  
The term is $T_2 = |1 - (w-1) + (w-1)^2| = |-1 + w - 1 + w^2 - 2w + 1|$ ? No.  
$1 - z + z^2$. With $z = w-1$, $z+w-1 = ...$ no.  
Let's check the substitution again.  
The term is $|1+z|^2$ and $|1-z+z^2|^2$.  
This looks like we want to maximize sum of moduli, or maybe minimize something?  
Let's look at the expression again.  
Let $w = 1+z$. Since $z \in D(0, 1)$, $w \in D(1, 1+1) = D(1, 2)$. No, $\arg w \in [0, \pi]$.  
$|z|=1 \implies z \in S^1$. $w = z+1$. The points $z+1$ form the unit circle plus origin shifted? No.  
$z \in D(0, 1)$ (unit disk). Then $z = e^{i\theta}$.  
$|1+z|^2 = 2 + 2\cos\theta$. Since $z$ is on unit circle, $w$ lies in the region where $Re(w) = 1 \pm |z|\cos(\dots)$? No.  
The set of points $\{ z+1 : |z|=1 \}$ is the set $\{ w : |w-1|=1 \}$. This is a circle centered at 1 with radius 1. It lies in the complex plane.  
So $w$ must satisfy $|w-1|=1$.  
Thus $w = e^{i\pi/2} + i(1)$? No, $w$ satisfies $|w-1|=1$. So $w=1+i$, $1-i$, $1+e^{i\theta}$.  
The expression is $f(w) = |w| + |1 - z + z^2|$. Since $z=w-1$, this becomes $|w| + |1 - (w-1) + (w-1)^2|$.  
Let's re-examine the second term.  
$T_2 = |1 - w + 1 + w - 1 - (w-1)^2 + \dots|$ ? No.  
Substitute $z$:  
$T_2 = |1 - z + z^2|$. Since $z = w-1$, this is $|(1) - (w-1) + (w-1)^2| = |-1+w+1 + (w-1)|...$ No.  
Let's simplify the substitution correctly.  
$1-z+z^2 = 1 - (w-1) + (w-1)^2$.  
$= 1 - w + 1 + (w^2 - 2w + 1) = 2 - w + 1 + w^2 - 2w + 1$ ? No.  
Wait. $z^2 = w^2 - 2w + 1$.  
So $T_2 = |1 - z + z^2| = |-1 + (w-1) + (w-1)^2|$? No, that's wrong.  
The term is $1 - z + z^2$. So substituting $z$:  
$1 - (w-1) + (w-1)^2 = 1 - w + 1 + w^2 - 2w + 1 = w^2 - 3w + 3$? No.  
Let's check $1-z+z^2$.  
$z=w-1 \implies z^2 = w^2 - 2w + 1$. So $1 - z + z^2 = 1 - (w-1) + w^2 - 2w + 1 = 1 - w + 1 + w^2 - 2w + 1$ ? No.  
$1 - w + 1 + w^2 - 2w + 1$. This looks complicated.  
Let's just simplify: $1 - z + z^2 = (z-1)(z+z) ...$?  
Wait, let's write it as $(1-z) + (1-z)z...$ No.  
Let's use the form $1-x+x^2$. This looks like $(x-1)^2$ shifted? No.  
Let's try to calculate $T_2$ for specific points on the unit circle, or simplify algebraically.  
Note that $z+w=1+z+(w-z) = z + 1 - (z-w+1)$ no.  
$1 - z + z^2$. We know $|z|=1$, so $z^2 = \bar{z}^{-1}$. No.  
The value $T_2$ is bounded? Or maybe it simplifies to a constant.  
Let's use the substitution $u = 1-z+z^2$.  
$u - (1+z) + z^2 = u - z + z^2 - z - 1$? No.  
Let's look at the structure: $T_1 = |z+1|$, $T_2 = |z^2 + z - 1|$ no, $1-z+z^2$.  
Is there a geometric interpretation?  
For $z \in D(0, 1)$, $1-z$ maps to something?  
Let's go back to substitution $w = 1+z$. Then $|w|=1+|z|\le 2$? No.  
If $|z| < 1$, then $|w| = \sqrt{1+z^2} \dots$ no, modulus of $w$ is between 1 and 2? No.  
The set $S_1 = \{ z : |z|=1 \}$ maps to $w = 1+z$. The image is a circle in the complex plane?  
Let's check if $w$ lies on the unit circle or something else.  
We have $|z|=1 \implies |z+1 - 1 + 1|...$ no.  
The set $\{1+z : z \in S^1\}$ is just a circle with radius 1 centered at 1.  
Let's call this circle $C_1$. $C_1 = \{ w \in \mathbb{C} : |w-1| \le 1, \arg(w) \in \text{something} \}$.  
Since $z$ is on unit circle, $z$ can be anywhere.  
The set $\{ z+1 : |z|=1 \}$ is a circle centered at 1 with radius 1? No.  
If $z = e^{i\theta}$, then $w = 1 + e^{i\theta}$.  
This curve lies in the unit disk? No, it's a circle of radius 2? No. The maximum of distance from 0 is 2. It can be larger.  
But if $z$ moves such that $|z|=1$, then $w$ must be on the locus of points satisfying $|w-1|=1$.  
No, this is wrong.  
If $z$ is a variable satisfying $|z|=1$, then $w = z+1$ can take any value with $|w-1|=1$.  
So $w$ lies on a circle $C_w$ centered at 1 with radius 1? No, it's just the locus of all points $z$ such that $|z|=1$. Then $z+1$ is the set $\{ w \in \mathbb{C} : |w-1|=1 \}$. This is a circle.  
Let me double check this.  
Let $z = e^{i\theta}$. Then $w = 1+z$. $|w-1|^2 = |e^{i\theta}|^2 + 0^2 - ...$ no.  
$|z+1|$. Since $z \in D(0, 1)$? No, $z$ can be anywhere on the unit circle? Yes.  
So $z \in S^1$. Then $w \in \{ w : |w-1|=1 \}$. This is a curve of points at distance 1 from $w=0$?  
Let's visualize. $|z|=1 \implies z$ lies on the unit circle in $\mathbb{C}^2$.  
Then $w = z+1$ traces out the set of points $w = 1+z$ for all such $z$. This is a curve that wraps around the origin? No, it's just the circle centered at $(1,0)$ with radius 1.  
So $w$ lies on the circle arc defined by $\theta \in [0, 2\pi]$? Or $\arg(z)$.  
If $z=e^{i\theta}$, then $w=1+e^{i\theta} = e^{i(\theta/2)}(2\cos(\theta/2))$ is not right.  
Let's write $z \in S^1$. Then $w = 1+z$ lies on a circle of radius $\sqrt{1^2 + 0^2} + ...$  
Actually, if $z \in S^1$, then $|z|=1$.  
The distance $|z+1|$ can range from 0 (at $z=-1$) to 2 (at $z=1$).  
But we have the term $T_1 = |1+z|$ which is $\le 2$. This doesn't restrict the choice of $w$.  
Let's go back to the original expression:  
$|1+z| + |1 - z + z^2|$.  
This looks like an application of triangle inequality or maybe some algebraic identity.  
Note that $T_2 = |z^2 + z - 1|$? No, $1-z+z^2 = z(z-1) + (z-1) = ...$  
Let's try to express $1-z+z^2$ using $(z+1)(z-1)$? No.  
Maybe write in terms of $\omega$ where $\omega = e^{i\pi/4}$?  
Actually, let's consider the transformation $w = 1+z$. Then $z = w-1$.  
Then $T_2 = |1 - (w-1) + (w-1)^2| = |-1+w+1 + w^2 - 2w + 1| = |-w+2+w^2|$. No.  
Let's simplify the algebra:  
$1-z+z^2 = 1 - z + z(z)$.  
$= z^2 - z + 1$. This is $z(z-1) + 1$.  
So $T_2 = |z(z-1) + 1|$.  
Since $|z|=1$, we have $z \in D(0, 1)$? Or $S^1$?  
If $z=e^{i\theta}$, then $z(z-1)+1 = e^{i\theta}(e^{i\theta}-1)+1$.  
$= e^{2i\theta} - e^{i\theta} + 1$. This has modulus.  
$T_2 = |1+z^2-z|$. Since $z$ is on unit circle, let's check the max of $|1-z+z^2|$ again.  
Let $z=x+iy$. Then $|1-(x+iy) + (x^2-y^2+2ixy)|...$ No.  
The problem statement asks for "maximum value".  
If we have a function $f(z)$ on the boundary of a region, its maximum is usually attained at vertices or center. But here it's not a real number.  
Let's use the substitution $z \to z^2$. No.  
Is there an identity? $|1+z| + |1-z+z^2|$.  
Let's check specific values.  
If $z=i$, then $T_1 = |1+i|= \sqrt{2}$.  
$T_2 = |1-(-1) + (-1)^2| = |1+1+1| = 3$. So sum is $\sqrt{2}+3 \approx 5.9$.  
If $z=1$, then $T_1 = 2$. $T_2 = |1-1+1| = 1$. Sum is $2+1=3$.  
If $z=-1$, then $T_1 = |-2|=2$. $T_2 = |1-(-1) + 1| = 3$. Sum is $2+3=5$.  
If $z=i/2$ (in unit circle?), let's see.  
Let's parameterize by angle $\phi$.  
Let $u = e^{i\theta}$. We want to maximize $\sqrt{2(1+\cos\theta)} + |e^{-i\theta}+e^{2i\theta}|...$ No, $|z-z^2+z|$?  
No, the second term is $|1-z+z^2|$.  
Let's simplify $T_2 = |1 - e^{-i\theta} + e^{-2i\theta}|$? No.  
The condition $|z|=1$ implies $z^2 \in S^1$.  
We want to maximize $f(\phi) = \sqrt{2+2\cos\phi} + |1 - e^{i\phi} + e^{2i\phi}|$? No, $\phi$ was used for angle.  
Let's use $\alpha$ such that $z = e^{i\alpha}$.  
Term 1: $|1+z| = |1+e^{i\alpha}| = \sqrt{2+2\cos\alpha}$.  
Since $\cos\alpha$ can be negative, let's just keep it as is. But modulus is positive.  
Actually, I said earlier that for $z \in D(0, 1)$ the term was $T_2 = |z(z-1)+1|$.  
Is it possible that $T_2$ simplifies to a constant? Or can be maximized by specific angles.  
Let's substitute $\phi = \pi/2$ ($z=i$). Then $|1+i| + |1-i+(-1)| = 1.414 + |0| = 1.414$.  
No, that term is wrong. For $z=-i$, $T_1 = |-1+i|= \sqrt{2}$. $T_2 = |1-(-i) + (-i)^2| = |1+i+1 - i^2|$? No, $(z-1)z$?  
Let's evaluate $|1-z+z^2|$ at $z=i$.  
At $z=i$: $1-i+(-1) = 0$. So modulus is 0. Sum is $\sqrt{2}$.  
At $z=1$: $|1| + |1-1+1| = 1$. No, $1+z$ is 2. Modulus 2. $|1-z+z^2|=|1-1+1|=1$. Sum 3.  
At $z=-1$: $|2| + |1-(-1)+1|=4$? No, $|1-(-1)+1| = 3$. Sum 5.  
So it can be larger than sum at $\pi/2$.  
Let's find the maximum of $|1-z+z^2|$ for $z \in D(0, 1)$.  
If we choose $z=i$, $T_2=0$. If we choose $z=-i$, $T_2 = |1-i+(i)^2| = |1-1+(-1)|$? No.  
For $z=i$, $z^2=-1, z=i$.  
Expression: $1 - i + (-1) = 0$.  
So max of first term is $\approx 1.414$ at some $z$.  
But for $z=i$, the modulus is small.  
Let's re-evaluate at $z=i$:  
$|1+i| \approx 2$? No, $|1+i|= \sqrt{1^2+1^2} = \sqrt{2} \approx 1.41$.  
And $|1-z+z^2| = |1-i+(-1)| = |0| = 0$.  
Sum is $\sqrt{2} \approx 1.41$.  
At $z=1$, $T_1=2, T_2=1 \implies 3$.  
At $z=-1$, $T_1=2, T_2=3 \implies 5$.  
Let's check $T_2$ for some other points.  
The maximum of $|1-z+z^2|$ on $D(0, 1)$? Or circle $C_1 = \{z : |z|=1\}$?  
Let's check if it can be arbitrarily large.  
If we approach a line like $z=-i$.  
Max modulus for $|1-z+z^2|$ might occur at boundary or interior.  
We need to maximize $\sqrt{2(1+\cos\alpha)} + |e^{2i\theta} - z|...$  
Let's use complex numbers directly with trigonometric substitution.  
Let $z = e^{i\theta}$.  
Term 1: $T_1 = \sqrt{2+2\cos\theta} = 2|\cos(\frac{\theta}{2})|$. (Assuming $\theta \in [0, \pi]$ for now? No.)  
$1+z^2 = z(1-z) + 1$.  
Let's simplify the term inside absolute value.  
Term $U = |z^2 - z + 1|$.  
We want to maximize $S(\theta) = 2|\cos(\frac{\theta}{2})| + |e^{2i\theta} - e^{-i\theta}|...$ No.  
Let's go back to $T_2 = |z^2 - z + 1|$.  
We know $|z|=1$, so $z \neq 0$.  
Let's use the polar form of complex numbers:  
$u = |z^2 - z + 1|$.  
If $z=e^{i\theta}$, then $z^2=e^{2i\theta}$. So we want to maximize $|e^{2i\theta} - e^{i\theta} + 1|$.  
Note that $e^{2i\theta} = \bar{e^{-2i\theta}}$? No.  
Let's use the rotation property.  
Since $z$ is on unit circle, we can write $z$ as $r e^{i\theta}$ with $r=1$.  
Then $|1-z+z^2| = |1 - z + z^2|$.  
If $z$ is real positive (say 1), value is 1. If $z=-1$, value is 3.  
Let's try to find where the term $|1-z+z^2|$ can be maximum.  
This looks like a problem where we want to maximize sum of two absolute values.  
Usually, this happens when the arguments add up to something.  
Let's see if we can write the expression as a product or something? No.  
Is there an identity for $|1+z|^2 + |1-z+z^2|^2$?  
$S^2 = (2+2\cos\theta) + (|z^2-z+1|^2 - 2 \text{Re}(\dots))$. No.  
Let's expand $|1-z+z^2|^2$.  
This is $(1-z+z^2)(\overline{(1-z+z^2)}) = 1 - z + z^2 + (z-1) + \bar{z}(z-1)$? No.  
$|a+b+c|^2 = |a|^2 + |b|^2 + |c|^2 + 2\text{Re}((a)(\bar{b}) + (b)(\bar{c}) + (c)(\bar{a}))$.  
Here $a=1, b=-z, c=z^2$.  
$|1-z+z^2|^2 = |1|^2 + |-z|^2 + |z^2|^2 + 2(\text{Re}(1\cdot(-z) + (-z)(z^2/ \dots))$? No.  
The term is $|1 - (e^{i\theta}) + (e^{i2\theta})|^2$.  
This looks like a circle problem.  
Let's simplify the modulus inside: $z^2+z-1 = z(z+1)-1$? No, $z^2+z-1$.  
The condition is $|z|=1$. Let $z=e^{i\theta}$.  
Then we maximize $\sqrt{2(1+\cos\theta)} + |e^{2i\theta}-1-e^{i\theta}|$.  
This seems to be a maximization problem on the circle.  
Let's analyze the term $|1-z+z^2|$.  
If we fix $z$ on unit circle, $z \in D(0, 1)$ (since $z$ is complex).  
The function $g(\theta) = |e^{i\theta}-1-e^{2i\theta}|$. No.  
Let's rewrite $z^2+z-1$.  
Actually, there is a nice property for the expression $\sqrt{A(z)} + B(z)$ when $z$ is on circle.  
Let's check the function value at specific points again.  
Points where it can be maximized:  
Maybe $z=i$ gave sum 1.41? No, that was small.  
We found for $z=-1$, sum is 5.  
For $z=1$, sum is 3.  
Let's check if there's a better point.  
Consider points near 0 and $\pm 1$.  
What about $z$ such that $z^2+z-1$ has large modulus?  
Since $|z|=1$, let's consider the maximum of $|1-z+z^2|$.  
Let's use the identity $(1-z+z^2) = (1-e^{i\phi}) - \dots$ No.  
Note that if we take $z=e^{i\pi/3}$, $\cos(\theta)=1/2$, $\sin(\theta)=\sqrt{3}/2$.  
Term 1: $|1+1/2 + i\sqrt{3}/2| = \sqrt{(5/2)^2+(3/2)^2} = \frac{1}{2}\sqrt{25+9}= \frac{4.88}{2} = 2.44$.  
$z=1$, $T_2=1$. Sum $= 2(1) + 1 = 3$? No, at $z=1$, $|1-z+z^2|=|0|=1$? No.  
At $z=e^{i\theta}$, $T_2 = |e^{i2\theta} - e^{i\theta} + 1|$.  
For $z=1$, $\theta=0$, term is $|1-1+1|=1$.  
For $z=i$, $\theta=\pi/2$, term is $|0|-0$? No. $|e^{-i\pi} - e^{-i\pi/2} + 1| = |-1 - i + 1| = |-i| = 1$. Sum $= |1+i| + 1 = \sqrt{2}+1$.  
At $z=-1$, $\theta=\pi$, term is $|e^{-2i\pi} - e^{-i\pi} + 1| = |1 - (-1) + 1| = 3$. Sum $= |-2| + 3 = 5$.  
Is it possible to have larger?  
Let's try $z \to i$. No, I got 1.41 earlier.  
Let's check $z=e^{i(\dots)}$.  
Maybe we can find a point maximizing $\sqrt{2+2\cos\theta} + |e^{2i\theta}-e^{i\theta}+1|$.  
Let's analyze the second term first. Let $w_2 = e^{2i\theta} - e^{i\theta} + 1$. We want to find $\max |w_2|$.  
Then we want to maximize $\sqrt{2+2\cos\theta}$ such that $|w_2|$ is achieved.  
The first term $\sqrt{2(1+\cos\theta)}$ is maximized when $\cos\theta = 1$, i.e., $z=1$, then term is 0? No.  
At $z=1$: $|1+1|=2$. At $z=-1$: $|2|=2$.  
So max of first term is 2.  
Is it possible to make second term large too?  
Let's check points on the circle.  
$T_1$ can range up to 2 (if $z$ approaches boundary).  
$T_2$ ranges?  
For a given $\theta$, $|e^{2i\theta}-e^{i\theta}+1|$ can be computed.  
Let's denote this value by $h(\theta) = |e^{2i\theta}-e^{i\theta}+1|$.  
We want to maximize $g(\theta) = |e^{i\theta} - 1| + |e^{-2i\theta} - e^{-i\theta}|$? No.  
The first term is $\sqrt{2(1+\cos\theta)}$. The second is $\sqrt{(e^{2i\theta}-e^{i\theta})^2 + \dots}$? No.  
Let's use a substitution $z = e^{i\theta}$.  
$T_1 = 2|\cos(\theta/2)|$. (This was my mistake before, let me check it again.)  
$|1+z|^2 = |e^{-i\theta/2} + \frac{1}{2}(1+\sin\theta) ...|$ No.  
$|1+e^{i\theta}|^2 = (1+\cos\theta)^2 + \sin^2\theta = 2 + 2\cos\theta$.  
$\sqrt{2(1+\cos\theta)} = 2|\cos(\theta/2)|$.  
Is this valid? Yes, if we assume $\cos(\theta/2)$ is real. But the modulus of $w$ is non-negative. So yes, it's valid for any $\theta$.  
However, $|z|=1$, so $\cos\theta \in [-1, 1]$.  
Thus $|T_1| = |2|\cos(\theta/2)|| \le 2$.  
At $\theta=0$, $T_1 = 2(1) = 2$. At $\theta=\pi$, $T_1 = 2(0)=0$.  
So the first term ranges in $[0, 2]$. The minimum is 0 and max is 2.  
The second term $|e^{2i\theta} - e^{i\theta} + 1|$? No.  
Let's re-evaluate the expression $T_2$ with correct algebraic form.  
Original: $T_2 = |1 - z + z^2|$.  
Using substitution $z=e^{i\theta}$, we get $e^{-i\theta}(z-1) \dots$? No.  
The term is $1-z+z^2$. If $z=1$, this is 0.  
If $z=-1$, this is 3.  
If $z=i$, this is $|1-i+(-1)| = 0$.  
Let's check if there's a specific point where the expression becomes $\sqrt{A} + \sqrt{B}$ with max? No.  
We want to maximize $\sqrt{2(1+\cos\theta)} + |e^{2i\theta}-z^2+z|$.  
Let's rewrite $|1-z+z^2|$ as a sum of moduli?  
Actually, there is a known identity for $|z^2+az+b|...$ No.  
Let's look at the structure $|1+z| + |1-z+z^2|$.  
Note that $|1-z+z^2|$ can be related to $|1-z^2|$? No.  
Let's use the identity $(z+1)(z-1) = z^2-z+1$. This is exactly the second term!  
So $T_2 = |z^2 - z + 1|$.  
We want to maximize $\sqrt{2(1+z^2)}$? No, $|z|=1$, so $z \neq 1$. But if $z=1$, it's 2.  
If we have $T_1 = |z+1|$ and $T_2 = |z^2-z+1|$.  
We can factorize:  
$T_1 = |z+1|$.  
$T_2 = | (z-1)z + z - 1/z \dots|$ No.  
Let's try to relate the two terms.  
Consider $w = 1+z$. Then $|w| \le 2$. Also $w^2$ is involved?  
No, let's substitute $w = z+1$. Then $z=w-1$.  
Then $T_1 = |w|$.  
And $T_2 = |(w-1)^2 - (w-1) + 1|$ ? No.  
Let's check the substitution in $T_2$:  
$|1-z+z^2| = |1 - (w-1) + (w-1)^2|$.  
We found earlier that this is $|-w+2+w^2|$.  
This looks complicated. Let me re-evaluate it carefully.  
$1 - z + z^2 = 1 - w + 1 + w^2 - 2w + 1$? No.  
Let's do algebraic expansion:  
$(w-1)^2 - (w-1) + 1 = w^2 - 2w + 1 - w + 1 + 1$? No.  
$1 - (w-1) + (w-1)^2 = 1 - w + 1 + w^2 - 2w + 1 = w^2 - 3w + 3$.  
Let's check for $z=-1$, $w=0$. $T_1 = 2, T_2 = |3|=3$. Formula gives $0-0+3=3$. Correct.  
For $z=1$, $w=2$. $T_1 = 2, T_2 = |1-3+1| = |-1| = 1$. Formula: $4 - 6 + 3 = 1$. Correct.  
For $z=-1/2$? No $|z|=1$.  
If we use $w = z+1$, then $T_2 = |w^2-3w+3|$.  
We want to maximize $\sqrt{2(1+\cos\theta)} + |w^2-3w+3|$.  
Since $w = e^{i\phi}$ is the variable (since $z \in D(0,1)$ implies $w$ can be anything in disk of radius 1 around 0? No.)  
Let's analyze the condition again. $|z|=1$. So $w$ lies on the circle $|w-1|=1$ ?  
No, for any point $z$ with $|z|=1$, we have $w = z+1$.  
So $|w-1|=|z| = 1$.  
So $w$ lies on the circle centered at 0 with radius 1? No.  
If $z = e^{i\theta}$, then $w = e^{i\theta} + 1$.  
The locus of $w$ is $\{ w : |w|=2 \text{ or } |w|=... \}$.  
Let's check distance from origin. $|w|^2 = |e^{i\theta}+1|^2 = (1+\cos\theta)^2 + \sin^2\theta = 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta = 2+2\cos\theta$.  
So $|w| = \sqrt{2(1+\cos\theta)}$. This is in $[0, 2]$.  
Also note that if $\theta$ is such that $\cos\theta > 1$, then it's larger. But $\cos\theta \le 1$ always.  
So the maximum of $|w|$ is 2 when $\theta = 0$, i.e., $z=1$. And minimum 0 when $\theta=\pi$, i.e., $z=-1$.  
And we need to find $\max |w^2-3w+3|$.  
Let's consider the function $h(w) = w^2 - 3w + 3$ on the circle $|w|= \rho(\theta)$ where $w=e^{i\theta}$. No.  
We want to maximize $S = |1+z| + |1-z+z^2|$.  
Substitute $z = e^{i\theta}$ into both terms.  
Let's check if we can express the sum as a function of a single variable $\theta$.  
Term 1: $f_1(\theta) = |1+e^{i\theta}| = \sqrt{2(1+\cos\theta)}$.  
This function ranges from 0 to 2. Specifically $2|\cos(\theta/2)|$ if we assume $z$ is in right half plane? No.  
The maximum of $\sqrt{2(1+\cos\theta)}$ is 2 at $\theta=0$.  
Term 2: $f_2(\theta) = |1-e^{i\theta}+e^{2i\theta}|$. This is not the same as I derived earlier.  
Let's re-evaluate $T_2$. The term in my derivation was $|1-z+z^2|$.  
Is there an error in the formula?  
$1 - z + z^2 = 1 - z + (z-1)(z) ...$ No.  
$1-z+z^2$. Let's use polar coordinates for this again carefully.  
Let $e^{i\theta} = z$. Then $|z|=1$.  
$T_2 = |1 - e^{i\theta} + e^{2i\theta}|$.  
Is there a geometric relation between these?  
Note that $e^{2i\theta} = (e^{i\theta})^2$.  
Let's write $f(\theta) = |1+e^{i\theta}| + |e^{i\theta}(e^{i\theta}-1) + 1|$. No.  
Let's simplify the second term using trigonometric identities.  
$T_2 = |1 - \cos\theta + i\sin\theta + e^{2i\theta}|$? No.  
$1 - z+z^2 = (z-1)z + 1$.  
This is not zero or something simple.  
Let's use the substitution $w = 1+z$. Then $|w|=2$ for $\theta=0$ and $|w|$ varies between $0$ and 2.  
Also $T_2 = |(1+z)^2 - (1+z) + ...|$ ? No.  
We derived earlier that $1-z+z^2 = z(z-1)+1$.  
For a fixed $\theta$, let's check if we can use the geometric property of points on the unit circle.  
Let $A$ be the point corresponding to $z$. The term is related to vectors? No.  
The modulus is always real? No, sum is complex.  
We are looking for a maximum value.  
Let's consider the function $g(z) = |1+z| + |z^2 - z + 1|$.  
We found that if $z=1$, value is $2+1=3$. If $z=-1$, value is $2+3=5$.  
Is there any point where it can be higher?  
Let's check points on the circle where $\cos\theta = \dots$  
The maximum of $|1-z+z^2|$ for $|z|=1$ is bounded by 3.  
Let's see if I can prove that $|1-z+z^2| \le 3$.  
If so, $T_1 + T_2 \le 5$. This seems a strong candidate.  
Is it always true?  
We know $|1-z+z^2|^2 = |z^2 - z + 1|^2 = |e^{i\theta}(z-1) + 1|^2$? No, $1-z+z^2$.  
Let's use the formula for modulus.  
$|1-z+z^2|^2 = (1-z+z^2)(\bar{1-z+z^2})$.  
Since $z^2 = \bar{z}^{-1}$ if $|z|=1$? No, $\overline{z^2} = z^2$ is false. $\overline{e^{i\theta}} = e^{-i\theta}$.  
Let's substitute in moduli:  
$|w|^2 + \dots$  
The expression looks like it can be related to $|1-z+z^2| \le 2+|z|=3$.  
But we have the first term $\sqrt{2(1+\cos\theta)} \le \sqrt{2(2)} = 2\sqrt{2}$? No.  
Let's check if the maximum is 5 or 7 or something.  
If $z=-1$, sum is 5. If $z=1$, sum is 3.  
Are there points closer to $\pi$ than $\theta=\pi/4$ or something?  
At $\theta = \pi/2$, $T_1 = \sqrt{2}$, $T_2=0$. Sum $\approx 1.41$.  
The term $\sqrt{2(1+\cos\theta)}$ is symmetric about $\pi$. It's minimized at $\pi$. Maximized at $\pi/2$? No. $\cos(\theta)$ varies from $-1$ to $1$.  
So it ranges between 0 and 2. Max value is 2 when $z=1$.  
The term $|e^{i\theta}(z-1)+1|$ has max possible value at $\theta=0$? No.  
At $\theta=\pi$, $T_2 = 3$.  
So sum $\le 5$ or something larger?  
Let's re-evaluate the maximum of $|1-z+z^2|$ for $z=e^{i\theta}$.  
We have $w = e^{i\theta}+1$. This corresponds to points on a circle in the complex plane (since $|z|=1$, this is just a circle centered at 0? No, it's the set of all points).  
The point $w=e^{i\theta}+1$ lies on the circle passing through $(-1,0)$ and $(0,1)$? No.  
Let's check if there is a point maximizing $|e^{2i\theta}-z^2+z-1|$.  
Actually, let's check the function $T(z) = |1-z+z^2|$.  
If we take $z=i$, we get 0. If $z=1$, we get 0. If $z=-1$, we get 3.  
The maximum of $|1-z+z^2|$ is indeed bounded by something like $\sqrt{5}$? No, 3.  
But we have to add $T(z) = |1+z|$.  
If $z$ approaches 0 (not possible since $|z|=1$), but if it's near $-1$, then $|1+z|$ is close to 2, and $|1-z+z^2|$ is close to 3. Sum 5.  
What about points on unit circle?  
We want to maximize $\sqrt{2(1+\cos\theta)} + |e^{i\theta} - e^{-i\theta}| ...$ no.  
Let's simplify the term $T_2$.  
$|1-z+z^2| = |(z-1)(z+1)|$? No.  
Is there an identity for $|1-z+z^2|$?  
We know that $(z-1) + z^2 + 1/z ...$ no.  
Let's try to use the property of points on circle.  
If we interpret the expression as a geometric mean or something?  
Let's check if there is an algebraic substitution $u = 1+z$ and $v = \dots$.  
Since we know $|z|=1$, this suggests we might be working with complex numbers on unit circle.  
Let $x = z+1$. Then $|x|=2$. No, that was wrong. $|z|=1$ means $z$ is on unit circle.  
Then $x=z+1$. So $x$ lies on circle centered at 0 with radius $\sqrt{1^2+2\cdot \cos\phi}$? No.  
$x=e^{i\theta}+1$.  
The expression becomes:  
Maximize $\sqrt{2(1+\cos\theta)} + |e^{i\theta}-z+z^2|$? No, this is just substituting back.  
Let's try a different substitution to eliminate the modulus constraints if possible.  
Let $z = \omega$. Then $|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta = 2+2\cos\theta$.  
The term $T_2 = |1-z+z^2| = |1-e^{i\theta}+e^{2i\theta}|$. Let's factorize.  
$1 - e^{i\theta} + e^{2i\theta} = (1-e^{i\theta})(1+i e^{-i\theta}) ...$? No.  
Let's just expand in terms of $\cos$.  
$|1-z+z^2|^2 = (1-z+z^2)(1- \bar{z} + \bar{z}^2)$ since $|z|=1$? No, $\bar{1} = 1$. $\bar{z}^{-1} = z$. No.  
The term is a polynomial in $z$. Modulus of polynomial $P(z)$.  
$P(z) = 1-z+z^2$.  
Modulus can be bounded using triangle inequality?  
But we want to maximize the sum.  
Let's consider specific points on unit circle again.  
For $\theta=0$, $z=1 \implies |1+1| + |1-1+1|=2+1=3$.  
For $\theta=\pi$, $z=-1 \implies |-1+1|- = |-2| + |...|$ ? No, $T_2$ for $\theta=\pi$ was 0?  
No. For $z=-1$:  
$T_1 = |1-1|=0$.  
$T_2 = |1 - (-1) + (-1)^2| = |2+1|=3$. Sum is 3.  
So at $\theta=0$, sum=5 (with different calculation).  
Let's re-calculate carefully.  
For $z=-1$:  
$T_1 = |1-1|=0$. No, $T_1 = |1+z| = |-1+1| = 0$.  
But I said before $z=-1 \implies T_2=3$.  
Let's recheck the term calculation for $z=-1$:  
$|1 - z + z^2| = |1 - (-1) + (-1)^2| = |1+1+1|=3$. Correct.  
$T_1 = |-1+1| = 0$. Wait, earlier I calculated $|-2|$?  
The term $|z|=1$, so if $z=-1$, $z$ is on the circle at angle $\pi$.  
$|1+z| = |1-1| = 0$.  
Why did I get 5 before?  
Ah, because $T_2$ for $z=-1$ was 3. So sum is 3.  
But if $T_1=0$, then max value might be 3+something.  
Let's re-verify my "at $\theta=0$ gives 5" thought process.  
At $z=1$: $|1+z|=2$. $|1-z+z^2| = |1-1+1|=1$. Sum $= 2+1=3$.  
So for $z=1$, sum is 3.  
For $z=-1$, $T_1=0$. $T_2=3$. Sum is 3.  
Is there a larger value?  
Let's try $\theta = \pi/2$ ($z=i$).  
$T_1 = |1+i| = \sqrt{2}$.  
$T_2 = |1-i+(-1)| = |-i|$? No, $|1-i-1| = |-i|=1$? No.  
Let's re-calculate $1-z+z^2$ for $z=i$.  
$1 - i + (i)^2 = 1 - i - 1 = -i$.  
Modulus is 1.  
So sum is $\sqrt{2} + 1 \approx 2.414$.  
This is less than 3 and less than 5.  
Let's check $\theta = 0$ ($z=1$). Sum 3.  
Let's check $\theta = \pi/3$?  
$\cos\theta = 1/2$. $T_1 = \sqrt{2(3/2)} = \sqrt{3} \approx 1.732$.  
$T_2 = |1 - e^{i\pi/3} + e^{2i\pi/3}| = |1 - (1/2 + i\sqrt{3}/2) + (-1/2 + i\sqrt{3}/2)|$? No.  
$z = 1/2 + i \sqrt{3}/2$.  
$z^2 = (1/2 + i\sqrt{3}/2)^2 = 1/4 - 3/4 - i\sqrt{3} = -1/2 - i\sqrt{3}$.  
So $T_2 = |1 - z + z^2| = |1 - (1/2 + i\sqrt{3}/2) + (-1/2 - i\sqrt{3})|$.  
$= |3/2 - 3i\sqrt{3}| = \sqrt{2.5^2 - 9(3)^2} ...$ No, modulus formula: $a+ib = a^2+b^2$.  
Real part: $3/2 - 1/2 = 1$. Imaginary part: $-3\sqrt{3}/2$.  
$|T_2|^2 = 1 + (9 \cdot 3 / 4) = 1 + 27/4 = 31/4 > 0$.  
Magnitude: $\frac{5}{2} \sqrt{5} ...$ No.  
$\sqrt{3.5^2 - 27}$? No. $1 + (27/4) = 31/4$.  
So $T_2 = \sqrt{31}/2 \approx 2.56$.  
Sum $T_1+T_2 = \sqrt{3} \approx 1.732 + 1.27 = 3.0$? No.  
Let me check calculation again.  
$z=1/2+i\sqrt{3}/2$. $\cos(\theta) = 1/2$.  
$T_1 = |1+e^{i\pi/3}| = \sqrt{(1/2 + i\sqrt{3}/2)^2} = \dots$ No, $|1+z|^2 = 2(1+\cos\theta)$?  
At $\theta=0$, $z=1$, $T_1 = |2|=2$. Correct.  
So my formula for $T_1$ was correct.  
The calculation for $T_2$ at $\pi/3$:  
$|1 - z + z^2| = |e^{2i\theta} + 2e^{-i\theta} - ...|$? No.  
Let's use the polynomial identity directly.  
We are looking for max of $\sqrt{2+2\cos\theta} + |e^{2i\theta} - e^{i\theta} + 1|$.  
Note that if $z=1/2+i\sqrt{3}/2$ (which is on unit circle), then $T_1 = \sqrt{2+2(0.5)} = \sqrt{3}$? No, $\cos(\pi/6)$?  
No, $\cos(\theta) = 1/2$. So $|1+z|$? No, $T_1 = |1+z|$.  
If $z$ is at $\pi/3$, then $|1+z|^2 = (1.5)^2 + (\sqrt{3}/2)^2$? No.  
$z = \cos\theta + i\sin\theta$.  
$T_1^2 = 2(1+\cos\theta)$.  
For $\theta=\pi/3$, $|1+z|^2 = 2(1+0.5) = 3$. So $T_1 = \sqrt{3}$.  
$T_2$: let's use the exact value.  
$z=e^{i\pi/3}$.  
$T_2^2 = |e^{2i\theta} - e^{i\theta} + 1|^2 = |1+2e^{-i\theta}-...|$? No.  
Let's simplify $|e^{2i\theta} - e^{i\theta} + 1|^2$.  
Let $\psi = \pi/3$. Then $z = \frac{1}{2} + i \frac{\sqrt{3}}{2}$.  
$T_2^2 = |1-z+z^2|^2$.  
Let's use the identity for modulus squared.  
Actually, if we consider $z$ on the circle $|z|=1$, let $z=e^{i\theta}$.  
We have two terms: $f(\theta) = \sqrt{2+2\cos\theta}$ and $g(\theta) = |e^{2i\theta} - e^{i\theta} + 1|$.  
Let's check values of $\theta$ for $f(\theta)$.  
At $\theta=0$: $f=2, g=1 \implies 3$.  
At $\theta=\pi/3$: $f = \sqrt{3}$? No. $T_1^2 = 2(1+\cos\theta)$. At $\theta=\pi/3$, $T_1^2 = 3$. $T_1 = \sqrt{3}$.  
Is this right? $|1+e^{i\pi/3}|^2 = |1+\cos(\pi/3)+i\sin(\pi/3)|^2 = (1.5)^2 + (\sqrt{3}/2)^2$? No.  
$1 + e^{i\theta} = 1 + \cos\theta + i \sin\theta$.  
So $|1+z|^2 = 1+\cos\theta + \sin^2\theta = 2(1+\cos\theta)$. Yes, this is correct.  
At $\theta=\pi/3$, $T_1 = \sqrt{3}$.  
Let's check $T_2$ at $\theta=\pi/3$.  
$g(\pi/3)^2 = |e^{2i\pi/3} - e^{i\pi/3} + 1|^2$.  
Note $z = e^{i\pi/3}$ is complex.  
Let's compute $T_2^2 = |(1+e^{-i\pi/3} + ...)|$?  
Wait, the expression for $T_2$ is $|1 - z + z^2|$.  
For $z=e^{i\theta}$, we have $|1-z+z^2|^2 = |e^{-i\theta}(e^{i(2+\theta)} - 1)|^2$? No.  
Let's just plug in values and see if I can derive an upper bound.  
For $\theta=0$, value is 3.  
For $\theta=\pi/2$, $T_1 = \sqrt{2}$. $z=e^{i\pi/2}=i$.  
$T_2^2 = |1-i+(-1)|^2 = |-i|^2 = 0$. Sum is $\sqrt{2} \approx 1.414$.  
For $\theta=\pi$, $T_1=0, T_2=3$. Sum is 3.  
It seems to be getting between 3 and $\infty$? No.  
Is it possible that my initial calculation for $z=i$ gave a higher value?  
Let's check the problem statement carefully. "Find the maximum value of $|1 + z| + |1 - z + z^2|$."  
The points I considered are all on the unit circle? No, I considered points where $|z|=1$.  
So we want to maximize over all $z$ with $|z|=1$.  
We found:  
At $\theta=0$: sum 3.  
At $\theta=\pi/2$: sum 1.414.  
At $\theta=\pi$: sum 3.  
Let's check a point where sum might be larger.  
Consider $z$ such that $|1+z|$ is maximized ($\approx 2$) and $T_2$ is also maximized.  
If we pick $z=0.5+i\sqrt{0.5}$? No, we need $z$ on unit circle.  
Let's check $T_1 + T_2$.  
Consider the function $F(z) = |1+z|^2 + |z^2-z+1|^2$? No.  
The maximum is likely at a specific point.  
Since we have 3 points of symmetry or something.  
At $\theta=0$, term is 3.  
Let's check if there is any other point where the sum could be larger than 3.  
For $z=-1$, term is $|2| + |3| = 5$.  
Is $z=-1$ a valid choice? Yes, $|-1|=1$.  
So the value 5 is achievable.  
Let's re-verify my calculation for $T_2$ at $z=-1$.  
At $z=-1$, $1 - z + z^2 = 1 - (-1) + 1 = 3$. Modulus is 3.  
$|1+z| = |1-1| = 0$.  
Sum is 3.  
Why did I think it was 5? Because earlier I wrote $T_1=2, T_2=3$. That was $z=-1$ case for modulus of something else.  
Let's re-evaluate:  
At $z=-1$:  
$|1+z| = |1-1| = 0$.  
$|1-z+z^2| = |1 - (-1) + (-1)^2| = |1+1+1| = 3$.  
Sum is 3.  
So my initial thought that max was higher than 3 was based on incorrect calculation or confusion between $T_1$ and $T_2$.  
Let me double check $z=1$.  
At $z=1$:  
$|1+z| = |1+1| = 2$.  
$|1-z+z^2| = |1-1+1| = 1$.  
Sum is 3.  
So at $\theta=\pi$, sum is 3.  
At $\theta=0$, sum is 3.  
So for these boundary points, max is 3.  
Is there a point where sum is $> 3$?  
Let's check points with large imaginary parts but close to real axis.  
Try $z = -1$ again. Sum is 3.  
What about $z=i$.  
$|1+i| + |1-i-1|^2$ ? No, modulus of term 2.  
At $z=i$:  
$T_1 = |1+i| \approx 1.414$.  
$T_2 = |1-i+(-1)| = |-i|=1$.  
Sum $\approx 2.414$.  
This is less than 3.  
What about $z=-i$.  
At $z=-i$:  
$|1-i^2| + |1-(-i) + (-i)^2| = |2+i+1-1| = |2+i| \approx 2.414$.  
Sum $\approx 5$ is false.  
Let's check $T_2$ again at $z=-i$.  
$T_2 = |1 - (-i) + (-i)^2| = |1+i-1| = |i| = 1$.  
Sum $= \sqrt{2} + 1$? No.  
$|1+z| = |-1+1| = 0$.  
So at $z=-i$, sum is 1?  
Let's re-evaluate for $z=i$:  
$T_1 = |1+i| = \sqrt{2}$.  
$T_2 = |1-i+(-1)| = |-i| = 1$.  
Sum $\approx 2.414$.  
Is there any point where sum is higher?  
Let's check $z=1$ again. $|1+z|=2$, $|1-z+z^2|=1$. Sum 3.  
So max possible seems to be somewhere else.  
But the calculation at $z=-i$ giving sum $\approx 2.414$ or $\sqrt{2} \approx 1.414$?  
Let's check $T_2$ for $z=i$.  
Wait, I might have made a sign error in substitution somewhere.  
Is it possible that the question implies $|1 - z + z^2|$ is something else?  
Maybe it's $(1-z)^2 + z^2$? No.  
Let's check my values at $\theta=0, \pi/3, \pi$.  
At $\theta=0$, sum 3.  
At $\theta=\pi$, sum 3.  
At $\theta=\pi/2$, sum 1.414.  
So it seems the max is 3?  
Let's check if I missed something. Maybe $z$ could be negative real?  
If $z=-1$, then $|1-z+z^2|=3$.  
$|1+z|=0$. Sum = 3.  
This is consistent with 5 thought (which was probably wrong).  
Let's check $T_2$ at $\theta=0$. $|1-1+1|=1$. $|1+1|=2$. Sum 3.  
At $\theta=\pi/2$: $|1-i-1|=|-i|=1$. $|1+i|= \sqrt{2}$. Sum $\approx 2.414$.  
So it seems max is 5 or something?  
Let's re-read the first term.  
$|1+z| + |1-z+z^2|$.  
Is it possible that the second term can be arbitrarily large?  
Let's check $T_2$ again.  
$T_2 = |z^2 - z + 1|$.  
If $z=e^{i\theta}$, $T_2^2 = (e^{2i\theta} - e^{i\theta} + 1)(\bar{e}^{-2i\theta} - \dots)$.  
Is it possible that the second term can be larger?  
Actually, there is a geometric interpretation of this.  
$|z^2+z-1|$ is the distance to line? No.  
Let's try substitution $z=e^{i\alpha}$.  
We want to maximize $\sqrt{2+2\cos\alpha} + |e^{2i\alpha}-e^{-i\alpha} + 1|$? No.  
Let's re-evaluate the expression $|1-z+z^2|$.  
Using $z = e^{i\theta}$.  
$1 - z + z^2 = (1+z)(1-z) - 1$? No.  
$1 - z + z^2 = z(z-1) + 1$.  
If we consider complex numbers on the unit circle, let's use polar coordinates again.  
Actually, there is a much simpler approach.  
The expression $|1+z|$ can be written as $|z+1|$.  
We want to maximize $|z+1| + |z^2-z+1|$.  
Since $z$ is on the unit circle, we can interpret $|z+1|$ as distance from origin (pointwise) + shift.  
But let's use geometric interpretation of terms in the plane.  
Let $A$ be the point $(-1,0)$ or something?  
The term $|1-z+z^2|$ seems to be related to the triangle inequality.  
Let's check the maximum value using the known max of $\sqrt{2(1+\cos\alpha)}$.  
We need to maximize $\sqrt{2+2\cos\theta} + |e^{i\theta}(z-1) + 1|^2$? No, $|1-z+z^2|$.  
Let's rewrite the modulus using triangle inequality.  
$|A+B+C|$ is minimized? No.  
The problem is to maximize sum.  
So we want terms to add up in magnitude? Or at least have same phase?  
Consider points on unit circle.  
Is it possible that $T_2 \ge T_1$?  
If we set $T_2 = k$, and $T_1=0$. Then max is $k$.  
But $|z^2-z+1| \le 3$?  
If $z=-1$, $|1-(-1)+1|=3$.  
If $z=i$, $|1-i+(-1)| = |-i| = 1$.  
If $z=1$, $|1-1+1|=1$.  
So max of $T_2$ seems to be 3.  
Is it possible to make $T_2 > 3$?  
Let's check. $|z^2-z+1|^2 = z(z-1) + ...$  
The maximum of $|z^2+z-1|$ is bounded by...  
Since $z^2+z-1 = (z+1)^2 - 2(z+1)+1$? No.  
Let's check the value at $\theta=0$.  
$|1-z+z^2| = |1-1+1|=1$.  
This is consistent with max being 3?  
If max of $T_2$ was 3, then sum would be $0+3=3$ or $5+...  

## Answer

*(none: the token cap hit during thinking)*
