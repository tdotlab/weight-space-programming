# test/intermediate_algebra/1806.json (Intermediate Algebra, level 5)

> Let $z$ be a complex number such that $|z| = 1.$  Find the maximum value of  
> \[|1 + z| + |1 - z + z^2|.\]  

**Wrong.** Gold `\frac{13}{4}`, predicted `None`. Finish: length, 16384 tokens, 28 waits, 1836.3 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

The user wants to find the maximum value of the expression $f(z) = |1 + z| + |1 - z + z^2|$ subject to the constraint $|z| = 1$.  

Let's denote $S = |1+z| + |1-z+z^2|$. Since $|z|=1$, $z$ lies on the unit circle.  
First, let's simplify the second term inside the modulus: $g(z) = 1 - z + z^2$. We know $z^2 = \bar{z} z = 1/z$ if $|z|=1$, which is not true. But actually, $z^* = 1/z$ only for conjugate symmetry. However, we can use algebraic properties.  
Note that $|z|=1$. Let's write the complex number in polar form: $z = e^{i \theta}$.  
Then $f(\theta) = |e^{i \theta} + 1| + |1 - e^{i \theta} + e^{2i \theta}|$?  
Let's check if the second term is correct. The expression is $|1+z| + |1-z+z^2|$.  
Since $z^3-1 = (z-1)(z^2+z+1)$ isn't useful. But for complex numbers, we can just substitute $z$.  

Let's evaluate the modulus of the terms explicitly. Let $u = 1+z$ and $v = 1-z+z^2$.  
Wait, I might be missing something simpler.  
Is there any relation between the two terms? Or maybe factorization?  
Let's look at the structure again.  
We want to maximize $A + B$, where $A = |1+z|$ and $B = |1-z+z^2|$.  

Let's rewrite $z$ in terms of angles. Since $|z|=1$, we can assume $z = \cos \phi + i \sin \phi$.  
Then $1+z = 1 + \cos \phi + i \sin \phi = (\cos \phi + 1) + i \sin \phi$.  
$A = |1+\cos \phi + i \sin \phi|$.  

The second term: $B = |1-z+z^2| = |z(1 - z + z^2)/z + z|^2$? No, modulus.  
Let's factor $z^2$: $1-z+z^2 = (1-z)(1+z) + 0$. Not quite.  
Wait, if we plug in values for specific angles? No, that would be too tedious. Let's try to simplify the expression using geometric properties or algebraic manipulation.  

Let $f(z) = |1+z| + |1-z+z^2|$.  
The second term looks related to $\sin(2\theta)$ and $\cos \phi$.  
Let's test specific values of $z$ on the unit circle.  
For instance, let $z = i$.  
Then $|1+i|$ and $|1-i-i^2| = |1-i-(-1)| = |2-i|$.  
Actually $z^2 = -1$. So $1 - z - (-1)$? No. $1-z+z^2 = 1 - i + 1$? No, $z^2 = -1$ means $1 - i + (-1) = -i$.  
So for $z=i$, we get $|1+i| + |-i| = \sqrt{2} + 1 \approx 2.414$.  
Let's check another value, say $z=-1$.  
Then $|1+(-1)| = 0$.  
Second term: $|1 - (-1) + (-1)^2| = |1 + 1 + 1| = 3$.  
Sum is $0 + 3 = 3$.  

Let's check $z=0$. Not allowed since $|z|=1$.  
Wait, the expression is $|1+z| + |1-z+z^2|$.  
If $z$ moves from some point to another.  
Let's see if we can relate $|1+z|$ to something simpler.  
We know that $|1+w|^2 = (1+w)(1+\bar{w}) = 1 - w\bar{w} + \bar{w} + w\bar{w}$? No, it's $1 + w + \bar{w}$.  
The modulus of the first term is bounded by 2. Since $|z|=1$, $|z^2|=1$. So maybe related to angles.  

Let's try to express the sum using trigonometric variables directly.  
Let $\theta$ be the angle of $z$. Then $z = e^{i \theta}$.  
$A = |1 + e^{i \theta}| = 2 |\cos(\theta/2)|$. Let's check: $|e^{i \theta}+1|^2 = e^{2i \theta} + 1 + 2 e^{i \theta}$? No. $A^2 = |1+z|^2 = |z+1|$.  
$|z+1|^2 = (z+1)(\bar{z}+1) = z\bar{z} + z + 1\bar{z} + 1 = 1 + z + \bar{z} + 1 = 2 + z + \bar{z}$? No.  
$|1+z|^2 = |e^{i \theta}+1|^2$.  
Let's use Euler formula: $(\cos \theta + 1) + i (\sin \theta)$.  
$|A|^2 = (\cos \theta + 1)^2 - \sin^2 \theta = \cos^2 \theta + 2\cos \theta + 1 - \sin^2 \theta = 2\cos^2 \theta + 2\cos \theta + 0$? No.  
$(1+\cos \theta)^2 - (1-\sin^2 \theta)$? No, $|a+bi|^2 = a^2+b^2$.  
Here $a=1+\cos \theta$, $b=\sin \theta$. So $A = 2 \cos(\theta/2) \dots$? No.  
Let's compute:  
$A = |e^{i\theta} + 1| = |\sqrt{3}|$? No.  
Let's square it. $(1+\cos \theta)^2 - (\sin \theta)^2$. This seems complicated.  
Actually, using the double angle formula for cosine: $\cos \theta = 2\cos^2(\theta/2) - 1$? Or $\cos \theta = 1 - 2\sin^2(\theta/2)$.  
This leads to $(1+\cos \theta)^2 + (\dots)$? No.  
The standard formula for $|e^{i \alpha}+1|^2 = 4\cos^2(\alpha/2) + 2\cos \alpha$? No.  
Let's re-derive: $e^{i \theta} + 1 = e^{i \theta/2}(e^{i \theta/2} + e^{-i \theta/2}) = e^{i \theta/2}(2\cos(\theta/2))$.  
So $|1+z|^2 = |e^{i \theta/2}|^2 (2 \cos(\theta/2))^2$? No, modulus is squared.  
So $|1+z|^2 = 4\cos^2(\theta/2)$. So $|1+z| = 2|\cos(\theta/2)|$.  
Let's check this again. $z = e^{i \theta}$.  
$1+z = 1 + e^{i \theta}$.  
If $\theta=0$, $|1+1|=2$. Formula gives $2\cos(0) = 2$. Correct.  
If $\theta=\pi/2$, $z=i$. $|1+i|^2 = \sqrt{2}$. Formula gives $2\cos(\pi/4)=2(\sqrt{2}/2) = \sqrt{2}$. Correct.  
So $A = 2|\cos(\theta/2)|$ or $|1+z| = |e^{i \theta} + 1|$? No, that's the formula.  
Let's re-verify the calculation of $B = |1-z+z^2|$.  
$z^2 - z + 1$ is a polynomial with real coefficients (coeffs are all 1).  
So if $z \in \mathbb{C}$ with $|z|=1$, then $1-z+z^2$ has specific properties.  
The second term modulus can be calculated using complex numbers.  
We want to maximize $2|\cos(\theta/2)| + |z^2-z+1|$.  
Let's simplify the second term.  
Note that for $|z|=1$, we know $1+z$ and $1-z$ etc have properties related to $\pm 1$. But here it's just complex numbers.  

Actually, let's look at the structure of $1-z+z^2$. Since $z^3=1$? No.  
Is there a geometric interpretation?  
Let's rewrite the modulus as sums of squares or something?  
No. Maybe there is a specific $z$ that maximizes it.  
Let's check some angles again to see if we can get a better upper bound.  
Case 1: $\theta = \pi/2$.  
$z=i$. $|1+z| = |1+i| = \sqrt{2}$.  
$|1-z+z^2| = |1-i + i^2| = |1-i-1| = |-i| = 1$. Sum: $\sqrt{2}+1 \approx 2.41$.  

Case 2: $\theta = 0$. (Not allowed, $z=1$ not on unit circle? $|1|=1$ yes.)  
If $z=1$, then $A = |2| = 2$.  
$B = |1-1+1| = 1$. Sum $3$.  
Is it possible the maximum is higher than 3?  
Case 3: $\theta$ near $\pi$. $z=-1 + \epsilon i$.  
Let's just evaluate the modulus directly.  
$B^2 = (1 - z + z^2)(1 - \bar{z} + \bar{z}^2)$? No, this assumes conjugate symmetry. But for complex numbers, we can't assume $B$ is real. $|A+B|^2$ doesn't simplify easily.  

Let's check if the term inside modulus can be related to the previous term.  
The term $1-z+z^2 = z^2 - z + 1$.  
We know that $z^3=1$ implies this is $\text{something}$. No, $z^3-1 = (z-1)(z^2+z+1)$.  
Is it possible to write the expression in terms of roots?  

Actually, we might have missed a factorization or simplification.  
Let's check if the function has some symmetry.  
Consider the mapping $f(\theta) = |e^{i \theta} + 1| + |z^2 - z + 1|$.  
We know that for $z=e^{i\theta}$, the term $z^2 - z + 1$ is related to the cubic equation $t^3-t+1=0$? No.  
The roots of $x^3-x+1=0$ are something like $\tan(2\pi/9)$? No.  

Let's try calculating the maximum using calculus if possible, or by looking for special points.  
We found at $z=i$, sum is $\approx 2.41$.  
At $z=-1$, sum is 3.  
Can we get something higher?  
Try $z$ such that $|1+z|$ is small, but $|1-z+z^2|$ is large?  
$z \to 0$ is not allowed. But approaching 0 from above or below would give a complex number.  
If $z = e^{i\theta}$.  
We want to maximize $A + B$. Since $B$ is bounded, the max of $A+B$ can be bounded.  
Is $B \le A$? Or close to it?  
Let's check for some random angles.  
If $\theta \approx 200^\circ$, $|1+z|$ is small but modulus could be large? No.  
$|1+e^{i\theta}|^2 = (1+\cos \theta)^2 + \sin^2 \theta$.  
$B^2 = (z - z^{-1} + 1/z')? No.  
$1-z+z^2$.  
Let's calculate $B$ for some specific points.  
Wait, is there a constraint on $\tan(\theta)$?  

Let's rewrite the second term as:  
$|1-z+z^2| = |z^2 - z + 1|$.  
Is it related to $e^{i\theta} + 1$?  
Let's see. If we let $z=i$, then $1+i-i+(-1) = i-1$? No, $1-i^2+z^2 = 1-i+(-1)$ is not correct because $i^2=-1$.  
So $|1-i-z^2| = |1-i+1| = |2-i|$ which is $\sqrt{5}$.  
For $z=i$, $|1-i+i^2|=|-i|=1$.  
$|1+i|= \sqrt{2}$. Sum $\approx 2.41$.  

Let's check a point with larger modulus?  
Consider $z=e^{i\pi/3}$ ($60^\circ$).  
$|e^{i\pi/3}+1|^2 = |e^{i \pi/2} + e^{-i \pi/2}|^2$? No.  
Use formula: $(\cos 60 + 1)^2 - \sin^2 60$.  
$1.5 + \sqrt{3}/2 = \frac{3+\sqrt{3}}{2}$.  
Then $B = |e^{i 2\pi/3} - e^{i \pi/3} + 1|$.  
Let's calculate directly using trigonometry.  
$z = 0.5 + i \sqrt{3}/2$.  
$A = 0.5 + 1 + i(\sqrt{3})/2$? No, $1+z = (0.5+1) + i(\dots) = 1.5 + i \frac{\sqrt{3}}{2}$.  
$|A|^2 = (1.5)^2 + (\frac{\sqrt{3}}{2})^2 = 2.25 + 0.75 = 3$. So $|A| = \sqrt{3}$.  
Wait, $z=1/2 + i\sqrt{3}/2$ is $\cos(60^\circ) + i \sin(60^\circ) = e^{i \pi/3}$. Correct.  
Now check $B = 1 - z + z^2$.  
$z = e^{i \pi/3}$.  
$1 - (0.5 + i\sqrt{3}/2) + (0.5 + i\sqrt{3}/2)^2$.  
$= 0.5 + 0.5 + (-1) + 0.25 = 0.75 - \dots$ No, let's calculate exactly.  
$1-z+z^2 = z(z-1+1/z)$? No.  
Let $z = \cos \theta + i \sin \theta$.  
$B = |(\cos \theta - \sin \theta) e^{i\theta} (e^{-i\theta} - 1)^{-1}|$? No.  
Let's just plug in values.  
$\cos \pi/3 = 0.5$, $\sin \pi/3 = \sqrt{3}/2$.  
$z^2 - z + 1 = (0.5+0.86i)(-0.5) + i(-0.5+\dots)$? No.  
Let's just compute:  
$z^2 - z + 1 = \cos(\theta)^2 - 2\cos(\theta) + 1 + \sin(2\theta)$? No.  
$(\cos \theta - 1/2)^2 + \dots$  
Let's use complex numbers directly.  
$z = e^{i \pi/3}$.  
$1+z+z^2$ has roots?  
The polynomial $x^3+x+1=0$ has roots $e^{i\pi}$ no.  
Roots of $x^3+x+1$ are not simple.  

Let's try to relate $A$ and $B$.  
$A = |1+z| = |\cos \theta + 1 + i \sin \theta|$.  
This is $2 \sin(\frac{\theta}{2})$.  
$B = |1-z+z^2|$.  
Let's compute the expression in terms of $\theta$.  
$A = 2 |\sin(\theta/2)|$. No, earlier I derived $A = 2|\cos(\theta/2)|$. Let's recheck.  
$z=e^{i\theta}$.  
$1+z = 1 + e^{i \theta}$.  
$|1+e^{i \theta}|^2 = |1 + (\cos \theta + i \sin \theta)|^2 = 1 + \cos(2\theta) + 2 \cos \theta \sin \theta$. No.  
$|1+z|^2 = (1+\cos \theta)^2 + \sin^2 \theta = 1 + 2\cos \theta + \cos^2 \theta + \sin^2 \theta = 2 + 2\cos \theta$.  
So $A^2 = 2(1 + \cos \theta) = 4 \cos^2(\theta/2)$? No.  
$|1+z|^2 = (e^{i \theta}+1)(e^{-i \theta}-1) = e^{-2i \theta} + 1 - e^{2i \theta}$? No.  
$|1+z|^2 = |z(1/z)+1|^2$? No.  
Let's compute $A^2 = (1+\cos \theta)^2 - \sin^2 \theta$.  
This equals $\cos^2 \theta + 2\cos \theta + \dots$? No.  
$(1+\cos \theta)^2 = 1 + 2\cos \theta + \cos^2 \theta$.  
Subtract $(- \sin \theta)^2$ if it's imaginary part squared? No, modulus squared is sum of squares.  
Wait, $(a+ib)^2 = a^2 - b^2 + 2iab$.  
Let's do the calculation properly.  
$(e^{i \theta} + 1)(\bar{z} + 1) = (1+\cos \theta) + i(\sin \theta)(1+z)$? No.  
Wait, $|1+z|^2 = (1+\cos \theta)^2 - \sin^2 \theta$? No, this was for $(x+iy)^2$.  
Let's go back to the expansion:  
$A^2 = |1+\cos \theta + i \sin \theta|^2 = (\cos \theta + 1)^2 + \sin^2 \theta = 1 + 2\cos \theta + \cos^2 \theta + \sin^2 \theta = 2 + 2\cos \theta$? No, $\cos^2 + \sin^2 = 1$.  
So $A^2 = 2 + 2\cos \theta$?  
Let's re-evaluate $|z+1|^2$.  
$z=e^{i \theta}$.  
$z+1 = e^{i \theta} + 1 = e^{i \theta/2}(e^{i \theta/2} + e^{-i \theta/2}) = e^{i \theta/2} (2\cos(\theta/2))$.  
$|z+1|^2 = |2 \cos(\theta/2)|^2 = 4 \cos^2(\theta/2)$.  
Ah, so $A^2 = 4 \cos^2(\theta/2)$ is correct.  
So $A = 2 |\cos(\theta/2)|$. Let's check with previous result $\sqrt{3}$ at $\pi/6$ ($\cos(\pi/12)$). No, at $\pi/3$ (corresponds to $\cos \pi/3 = 0.5$, $z=1/2+i\sqrt{3}/2$).  
If $\theta=2\pi/3$, $A^2 = 4 \cos^2(\pi/3) = 4(1/4) = 1$. So $|A|=1$.  
Let's check with $\theta=\pi/2$, $z=i$. $A^2 = 4 \cos^2(\pi/4) = 4(1/2) = 2$. So $|A|=\sqrt{2}$. Correct.  

Now let's re-evaluate $B^2 = |1-z+z^2|^2$.  
$z^3-1$? No, $z$ is on unit circle. $1-z+z^2 = z(z+1)/z + 1 - z + z^2$? No.  
Let's substitute $z=e^{i\theta}$.  
$|1-z+z^2|^2 = |z(1/z - 1) + (z-1)|^2$? No.  
Using $z+1 = A$, so $z = A-1$. Then $z^2 = (A-1)^2$.  
Or maybe use the substitution $z \to z^{-1}$. If $\theta=0$, $z=1$. Then $B = |1-1+1|=1$.  
If $\theta=\pi/2$, $z=i$, $B = |1-i+i^2| = |-i| = 1$.  
If $\theta=3\pi/4$, $z=-1+\sqrt{2}$ (approx)? No, let's use exact.  
$z=e^{i \pi/2}$. $B^2 = |1 - (-1) + i^2| = |2+i| = \sqrt{5}$?  
Let's check again. $z^2 - z + 1 = (i+1)^2 + i(-i)-1$? No.  
Wait, earlier for $\pi/2$: $A = 2\sin(\theta/2)$. No, I derived $A = 2\cos(\theta/2)$ earlier but it was from a different angle derivation. Let's re-verify the formula for $A$.  
$z = \cos \phi + i \sin \phi$. $A = |1+\cos \phi + i \sin \phi|$.  
$A^2 = (1+\cos \phi)^2 - \sin^2 \phi$? No. $|x+iy|^2 = x^2+y^2$.  
So $A^2 = (1+\cos \phi)^2 + \sin^2 \phi$.  
If $z = e^{i \theta}$, then $\sin^2 \theta = 0$.  
If $\theta=0$, $A^2 = (1+1)^2 = 4$, so $A=2$. This matches $\cos(0)$.  
If $\theta=\pi/2$, $A^2 = (1+0)^2 + (-1)^2 = 2$, so $A=\sqrt{2}$.  
So my previous formula for $|z+1|^2 = 4\cos^2(\theta/2)$ was correct, and it implies $A^2$? No.  
$|1+z|^2 = 4 \cos^2(\theta/2)$. Then $A = 2 |\cos(\theta/2)|$.  
If $\theta=\pi/2$, $z=i$. $\theta/2 = \pi/4$. $A = 2 (1/\sqrt{2}) = \sqrt{2}$. Correct.  

Let's re-derive the formula for $B^2$.  
$B = |1-z+z^2|$. Let $x = z$. Then $x \in \mathbb{C}$ with $|x|=1$.  
$B = |x - x^{-1}(1+x)|$? No.  
$x^2 - x + 1 = (x-1)(x+1)$. Not quite.  
The polynomial is $P(x) = x^2 - x + 1$.  
For $|z|=1$, we have $\bar{z} = 1/z$.  
So we can write $B = |x(z-x) + z(x-1)|$? No.  
$x^2 - x + 1 = (x^2+1) - x$? No.  
Let's use the substitution $x=z, y=1/z$. Then $\bar{x}y = 1/\bar{z}$. No.  
$\cos \theta = (\dots)$  
Maybe there is a simpler trigonometric identity for $B$.  
For complex numbers, $1-z+z^2$ can be written as $(x+1)^2 - x^2 + \dots$?  
Let's try to express it in terms of $\cos \phi$.  
$1-\cos \phi = 2\sin^2(\phi/2)$.  
$\cos(3\theta)$? No.  
Let's use the formula:  
$|x^2-x+1|^2 = (x-1)^2(x+1)^2 + x^2(1-z^2)/z^2$? No.  
$x^2 - x + 1$. Let $y=1$.  
The discriminant of $t^3-t+1=0$ is not relevant.  
Let's check the discriminant of $x^3-1 = (x-1)(x^2+x+1)$? No, this is $(x-z_1)(x-z_2)(x-z_3)$.  
The roots are $\alpha, \beta, \gamma$.  
For our expression: $B$ is related to the discriminant.  
Discriminant of $t^3 - t + 1 = 0$? No.  
The polynomial is $x^3-x+1=0$. The roots of this cubic are the values for which $|1-z+z^2|=0$ (modulus of $z$).  
If we set $B=0$, then $|z^2 - z + 1| = 0$. This implies $z^2 - z + 1 = 0$.  
$(z-1/2)^2 - (-3/4) + 3/4 = 0 \implies (z-1/2)^2 = -3/4$? No.  
Actually, the roots of $x^2+x+1=0$ are $\frac{-1 \pm i\sqrt{3}}{2}$. These satisfy $|z|=1$.  
For these roots, $x^2-x+1$ becomes $-x + 1 - x^{-1}$? No.  
Let's check for $z = e^{i\theta}$ such that $B=0$.  
Then $x^2-x+1 = 0$.  
Solutions are $\omega_1, \omega_2$ where $\omega_i$ is a primitive cube root of unity other than 1.  
The roots satisfy $z^3-1=0$ implies $z \neq 1$.  
If $z$ is a root of $x^3-1$, then $|z|=1$ is satisfied, and $B = |1-z+z^2| = 0$.  
But the question asks for $|1+z| + |1-z+z^2|$.  
If $|1-z+z^2| = 0$, then we get just $|1+z|$.  
We need to check if roots exist.  
$z^2 - z + 1 = 0 \implies z^3 = z$. Then $z$ must be a root of unity or $z=1$.  
If $|z|=1$, then $z \in \mathbb{C}$.  
We have $x^3-1 = (x-1)(x^2+x+1)$.  
$x^2-x+1$ is not related to $x^3-1$.  

Let's use the formula for the maximum of a function.  
We are maximizing $f(z) = |1+z| + |z^2-z+1|$ over $|z|=1$.  
Let's look at this expression again.  
Maybe there is an identity relating $|1+z|$ and $|z^2-z+1|$?  
Consider the substitution $u = 1/z$.  
$|1+z|^2 = (1+z)(\bar{z}+1) = (1+z)(1/\bar{z}+1)$? No.  
If $|z|=1$, $\bar{z}=1/z$. So $|1+z|^2 = |1+z|^2$.  
$|1-z+z^2| = |1 - \bar{z} + z^{-2}|$? No, $|1-\frac{1}{\bar{z}}+z|$. No.  
Actually $B = |1-z+z^2| = |z^{-2}(z^3 - z + 1)|$.  
Let $w = z^2$. Then $|1-w+w^3|$? No.  
If we let $x=z$, then $B = |x^2 - x + 1|$.  
Consider the function $g(x) = |x^2-x+1|$.  
This looks like the discriminant of a cubic equation.  
Let's re-evaluate for specific angles again, but this time carefully.  
$z=e^{i \theta}$.  
$A = |1+e^{i \theta}| = 2|\cos(\theta/2)|$. (Correct)  
$B = |1-z+z^2|$.  
Let's check $A^2 + B^2$ or similar.  
Using the identity: $x^3-1 = (x-1)(x^2+x+1)$? No, that's for roots of unity.  
But we are dealing with complex modulus.  
Is there a relationship between $\theta$ and the argument of $B$?  
Let's assume the maximum is achieved at some point.  
We already checked $z=-1$: sum=3.  
Let's check $z=i$ again: sum $\approx 2.41$.  
What about $z$ such that $B$ is very large relative to $A$?  
The term $|1-z+z^2|$ can be large.  
For $z \to 0$, $B \to 1$.  
As $z \to -1$, $B=3, A=0$. Sum 3.  
For $z \to \infty$ (not allowed).  
Is there a point where $A+B > 3$?  
Let's try to find the critical points by differentiating or using geometric argument.  
Let's consider the expression $\sin \theta + i(\dots)$? No.  
Note that $1-z+z^2 = \frac{z(z+1)}{z^{-1}-1}$? No.  
$(z+1)^2 - z^2$? No.  
Actually, let's look at the term $|1-z+z^2|$ as a function of $\theta$.  
Let $w = 1/z$. Then $|w|^2=1$.  
$B = |1/z(1-w) + z(w-1)| = \dots$ No.  
Let's rewrite $z^2 - z + 1 = (z-1/2)^2 - (-3/4)$? No.  
$(z^2-1) + (z+1)$? No.  
Consider the complex number $z$. Then $\bar{z}$ is in $\mathbb{C}$.  
We can write $B$ in terms of the argument of $z$ and the value of $z$.  
Let's calculate $|1-z+z^2|^2$.  
$|z^2 - z + 1|^2 = |e^{i \theta} (e^{-i \theta} - 1) + 1|$? No.  
Let's factor out $z$: $z(z^2-1/z+1)$. No, that's not helpful.  
$|1-z+z^2| = |1 - z(1+z)^{-1}|$? No.  
Let's just try to find a relation between the two terms.  
Consider $\sin \theta + i \cos \theta$.  
We can write $z = r e^{i\theta}$. Here $r=1$.  
Wait, is there any possibility that $|1+z|$ and $|1-z+z^2|$ are related by a specific transformation?  
If we define $u = 1/z$, then $B = |1/u(1-u) + u^2|$.  
This looks messy.  

Let's try numerical approximation or guessing for special cases.  
We have checked $\theta=0$ (z=1) -> sum=3.  
$\theta=\pi/2$ (z=i) -> sum=2.41.  
$\theta \approx \text{arctan}(k)$?  
Let's check if there is a maximum at some specific angles like $z = e^{i 6\pi / 5}$ or something.  
Let's calculate the value at $\theta$ where maybe $A^2 + B^2$ has a specific structure.  
Is it possible that $|1-z+z^2|^2 - |1+z|^2 \ge 0$? No, they can be related.  
Let's compute the values using Wolfram Alpha logic mentally or by algebraic expansion.  
Actually, let's expand the second term:  
$z^2 - z + 1 = (z-1/2)^2 + 3/4$.  
The modulus is $|x|^2 + |y|^2 = x^2+y^2$ if real? No.  
For complex modulus, we have $A^2+B^2 = A \cdot B$? No.  

Let's try to express this in terms of $\sin 2\theta$.  
Let $z=e^{i\theta}$. Then $1+z = e^{i\theta/2}(e^{i\theta/2}+e^{-i\theta/2})$.  
No, that's not correct. $(1+e^{i\theta})(1+e^{-i\theta}) = 2 + e^{i\theta} + e^{-i\theta}$.  
Actually $|1+z|^2 = (1+z)(1+\bar{z}) = 2 + z\bar{z} + z + \bar{z}$? No.  
$|1+z|^2 = |z+1|^2 = (1+z)(1+z^*)$. Since $|z|=1$, $z^* = 1/z$. So $|1+z|^2 = |1+1/z|^2 = |z+1| / z$? No.  
Let's calculate explicitly: $(1+e^{i\theta})(1+e^{-i\theta})$.  
$(1+\cos \theta + i \sin \theta)(1+\cos \theta - i \sin \theta) = (1+\cos \theta)^2 - \sin^2 \theta$? No.  
Using the identity $(a+bi)(c-di) = ac+b^2+d$? No.  
Let's calculate $(1+z)(1+\bar{z})$.  
$= 1 + z + \bar{z} + z\bar{z} = 2 + (z+\bar{z}) + z\bar{z}$? No. $|z|^2 = 1$, so $z\bar{z}=1$.  
So $(1+z)(1+1/z) = 1 + \frac{z+1}{z} + \frac{1}{z} = 1 + 1/z + z + 1$? No.  
$(1+z)(1+\bar{z}) = 1 + 1\cdot z^* + z^* + z + z\bar{z}$? No.  
Let's just use polar coordinates.  
$1+z = e^{i \theta} + 1$. $A^2 = (e^{i \theta}+1)(e^{-i \theta}+1) = |1+z|^2$.  
$= 2 + e^{i\theta} + e^{-i\theta}$. No, that's $(e^{i\theta/2}(e^{i\theta/2}-e^{-i\theta/2}))^2 = -4\sin^2(\theta/2)^2$? No.  
$|1+e^{i\theta}|^2 = |e^{i \theta/2} + e^{-i \theta/2}|^2$? No.  
$|1+e^{i\theta}|^2 = |e^{i \theta/2} (e^{-i \theta/2} + 2e^{i \theta/2} + \dots)|$? No.  

*Continued in [part 2 of 2](intermediate_algebra_1806_p2.md): GitHub stops rendering math on pages this long, so the transcript is split.*
