# test/intermediate_algebra/1806.json (Intermediate Algebra, level 5)

> Let $z$ be a complex number such that $|z| = 1.$  Find the maximum value of  
> \[|1 + z| + |1 - z + z^2|.\]  

**Wrong.** Gold `\frac{13}{4}`, predicted `None`. Finish: length, 16384 tokens, 2 waits, 1960.9 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Let $n=5$ be the degree of a polynomial. We are given that $z$ is a complex number such that $|z|=1$. We want to maximize the expression  
\[ f(z) = |1 + z| + |1 - z + z^2|. \]  

First, note that $z$ satisfies $|z|=1$, which means $z$ is on the unit circle. Also, $z$ is a root of some polynomial? No, $z$ is just on the unit circle.  

Let's analyze the terms in $f(z)$.  
The first term is $|1 + z|$. Since $z$ is on the unit circle, let $z = e^{i\theta} = \cos \theta + i \sin \theta$, with $\theta \in [0, 2\pi)$.  
The distance from the origin to a point $w$ in the complex plane is $|w|=1$. This is just saying $w$ lies on the unit circle.  
Let's rewrite the expression in terms of polar coordinates or maybe using Cauchy-Schwarz inequalities? Or by analyzing specific points on the unit circle.  

The term $|1 - z + z^2|$ can be rewritten. The degree of the polynomial is 3. $z^3=1$ if we think of roots as being related to something else, but here we just have a sum of terms.  
We need to check if $f(z)$ depends only on $z$.  

Let's rewrite $|1 - z + z^2|$. We know that $|z|=1$. So $z^2 = \bar{z}^{-1}$? No, $z\bar{z}=1$.  
We can write $|1 - z + z^2| = | \frac{z+3}{1-z} |$? No.  
Let's try to express $|1 - z + z^2|$ in terms of $|z|=1$.  
Maybe we can use the triangle inequality to find an upper bound, but for a maximum, we might need equality to hold.  

Let's compute the value for specific points on the unit circle.  
Case 1: $z = 1$.  
Then $f(1) = |1 + 1| + |1 - 1 + 1^2| = |2| + |1| = 3$. This is a possible value.  

Case 2: $z = i$.  
$f(i) = |1 + i| + |1 - i + (-i)^2|$  
$f(i) = |1+i| + |1 - i - 1| = \sqrt{2} + |-i| = \sqrt{2}$  
$f(i) = \sqrt{2}$. This is smaller.  

Case 3: $z = -i$.  
$f(-i) = |1 + (-i)| + |1 - (-i) + (-i)^2|$  
$f(-i) = \sqrt{1^2+1^2} = \sqrt{2}$ and $|1+i| = \sqrt{2}$. The second term is $|1 - i + (-1)| = |-i|=1$. So total sum is $2$? No, $|1-i-1|=|-i|=1$, first term $\sqrt{2}$.  
$f(-i) = 1 + \sqrt{2}$ ? No.  
Let's recalculate carefully.  
If $z = -i$, $|z|=1$.  
$|1+z| = |1 - i| = \sqrt{1^2+(-1)^2} = \sqrt{2}$.  
Second term: $1 - z + z^2 = 1 - (-i) + (-i)^2 = 1 + i - 1 = i$.  
$|i| = 1$.  
So $f(-i) = \sqrt{2} + 1 \approx 2.414$.  

Case 4: $z = e^{i\pi/3} = \cos(60^\circ) + i\sin(60^\circ) = \frac{1}{2} + i\frac{\sqrt{3}}{2}$.  
First term $|1+z| = |1.5 + 0.866i|$? No.  
$1+\frac{1}{2}+\dots = 1.5 + \dots$.  
$f(z)$ for $z$ on circle.  

Case 5: $z = e^{i\pi/4} = \frac{\sqrt{2}}{2}(1+i)$.  
First term $|1+z| = |1 + (\sqrt{2}/2)(1+i)|$.  
Second term $|1 - z + z^2|$.  

Let's check the function $g(z) = |1 - z + z^2|$. This is the modulus of a polynomial evaluated at $z$ on the unit circle.  
The roots of the equation $1+z+z^2 = 0$ are the points where $z$ lies. These roots can be found by Vieta's formulas? No.  
Let's write $1 - z + z^2$. Let $w=1-z$. Then $|1+w+w^{-1}|$? No, that's not right.  

Also $|1 - z + z^2|$ could be related to the maximum modulus principle on a curve? No.  

The term is $\max |z| = 1$.  
We can consider the function $h(z) = |1 - z + z^2|$.  
For real $z$, $|1 - z + z^2| = | (1-z)(1+z) + \dots |$?  
Let's check real values on the unit circle, $z=x+iy$. Then $y=0$. $f(x) = |1+x| + |1-x|$.  
If $x=1$, $f(1)=2+0=2$? No.  
$f(z) = |1+z| + |1 - z + z^2|$.  
For real $z=x \in [-1, 1]$ (since $|z|=1$), we have $|z|=1$. If $x=-1$, $f(-1)=|-2| + |-2-0|=2+|-2|=4$? No.  
Let's check $x=-1$: $z=-1$. $f(-1)=|1-1|+|1-(-1)|=0+2=2$. This matches.  
For $x=i$, we got $\sqrt{2}$.  

Let's analyze the expression inside the modulus for $z=x+iy$.  
$|1+z|^2 = (1+x)^2 + y^2$.  
$|1 - z + z^2|^2$? No. Let's write $|1-z+z^2|^2$ in terms of something simpler?  
$1 - z + z^2 = \frac{z^2}{-1} + z - 1$.  
Actually, let's just use the fact that for any $z$, $z^{-1}=\bar{z}$ if $|z|=1$ and $\overline{z}=z^{-1}$? No.  
If $z=e^{i\theta}$, then $z^2=e^{2i\theta}$.  
So we want to maximize $A + B$, where $A = |1+z|$ and $B = |1-z+z^2|$.  

Let's try to write $B = | (1-z)^{-1} \dots |$?  
Consider the triangle inequality. $|1+z| + |1-z+z^2| \le 2 \max(|1+z|, |1-z+z^2|)$.  
We want to find $\max (|1+z| + |1-z+z^2|)$.  

Let's try substitution or geometric interpretation.  
Consider the function $f(z) = |z+1| + |z - 1/2 \pm i \dots|$? No.  
Let's rewrite the second term in terms of conjugates if possible.  
$|1-z+z^2|^2$? Maybe not directly useful for upper bound estimation unless it simplifies nicely.  

Is there any geometric constraint? $z \in \partial \mathbb{D}$.  
Let $w = 1 - z + z^2$.  
We want to maximize $|1+z| + |w|$.  
$1+z = \frac{z-1}{z+1}$? No.  
For $|z|=1$, $|z|^2=1$.  
Maybe we can express $|1-z+z^2|$ using polar form.  
Let's check the maximum of the expression $A(z) + B(z)$ on $\mathbb{C} \setminus \{0\}$? No, it's bounded by 4?  
If $z=1$, sum is $3$. If $z=-1$, sum is $2$.  
Is it possible to get higher values? Let's try $z=i$, we got $\sqrt{2} + 1$ earlier.  
Let's re-evaluate $z=i$. $|1+i| = \sqrt{2}$. $|-i|=1$. So sum is $\sqrt{2}+1$. This is approx 2.414.  
Is it possible to get larger values than that?  

Let's check the function for $z$ on the circle. Let's parameterize $z = e^{i\theta}$.  
$A(z) = |1 + e^{i\theta}|$. This is $\sqrt{2} \cos(\frac{\theta}{2}) - 1$? No.  
$1 + e^{i\theta} = e^{i\theta/2}(e^{-i\theta/2} + e^{i\theta/2}) = 2 \cos(\theta/2)$.  
So $A(z) = |2 \cos(\theta/2)| = 2 |\cos(\theta/2)|$.  
The second term is $B(z) = |1 - z + z^2|$.  
$z^2+1-z = (1-e^{-i\theta})(z-0.5 \pm i \sin \dots)$? No.  
Let's try $z=e^{i\theta}$ directly in terms of trigonometric functions or just complex numbers.  
Let's simplify the expression inside the second modulus by factoring out 2 or something.  
$|1 - z + z^2| = |1 + \overline{z}(\overline{z}-1) + z^2|$? No.  

Let's try a simpler approach: $f(z) = |1+z| + |1-z+z^2|$.  
Is it possible that $f(z)$ attains its maximum at some specific point or is bounded by something simple like $\sqrt{3}$? Or 4?  
Since the domain is a circle (infinite), and we can approach any point on the circle, maybe we need to check boundaries? No, the sum of functions.  

Let's use the property of $z$. For real numbers, it's a specific value.  
$|1+z| = 2 \cos(\theta/2)$ if $z=e^{i\theta}$ is real? No. If $z=x$, then $\theta=0 \implies |1+1|=2$.  
If $z=x$, then $f(x) = |1+x| + |x^2+1-x| = 2$ for $x=-1$? No.  
If $z=-1$, $A=0, B=2 \implies f(1)=2+2=4$? No.  

Let's check the values again carefully.  
$x = -1$:  
$A = |1-1| = 0$.  
$B = |1 - (-1) + 1(-1)|^2 = |2 - 1| = 1 \implies B=1$.  
$f(-1) = 0+1 = 1$? No.  
Let's recheck $x=-1$. $f(x) = |1+x| + |1-x+x^2|$.  
For $z=x$, if $x=-1$, $z^2=1$, so $1-(-1)+1 = 3$. $B=|3|=3$? No.  
If $z=1$, $A=2, B=1+0=1 \implies f(1)=3$.  
If $z=i$, $A=\sqrt{2}, B=\sqrt{2} \implies f=\sqrt{2}$? No.  
$|1-i|^2 = 2$. So $\sqrt{2}$.  
For $x=-i$, $z^2=-1$, so $B = |1+i + (-1)| = 1$? No, $B=|1+(-i)+(-1)|=|-i|=1$.  
$f(-i) = \sqrt{1^2+1} = \sqrt{2}$? No. $A = |1-i|=1$. $B=|-i|=1$. Sum $= 1+1=2$.  
$|1-i|^2 = 2$, so $\sqrt{2}$.  
For $x=i$, $f(i) = \sqrt{2} + |-i| = \sqrt{2}$.  
For $z=-1$, let's check. $z^2-1-z+1$.  
$A=|1+z|=0$. $B=|1-(-1)+(-1)^2| = |1+1-1| = 1$. Sum = 1.  
So it seems max is greater than 2?  
Let's try a point where $z$ is near something else.  

Let's check the value at $z = -i \cdot i^k = e^{ik\pi/2}$ for various integer $k$.  
$k=1, z=i$: $\sqrt{2} + 1 = \approx 2.414$.  
$k=-1, z=-i$: $1+1=2$? No, $f(-i) = \sqrt{2}$.  
Let's re-evaluate $z=i$ properly.  
$f(i) = |1+i| + |1-i+(-i)^2|$.  
$|1+i| = \sqrt{2}$.  
$|-i|^2 = 1$ (since $z^2=1$).  
So $|1-i+(-i)^2| = |1-i-1| = |-i| = 1$.  
Sum = $\sqrt{2} + 1$.  

Let's re-evaluate $z=-i$ properly.  
$f(-i) = |1+(-i)| + |1-(-i)+(-i)^2|$.  
$|1-i| = \sqrt{2}$.  
$|-i|^2 = -1$? No, $(-i)^2 = -1$. So term is $1+(-i)+(-1) = 1-i+1-i+1$? No.  
Let's write it clearly. $z=-i$, so $z^2=(-i)(-i) = (-i)^2 = -1$.  
Term 1: $1+z = 1-i$. Modulus $\sqrt{1^2+(-1)^2} = \sqrt{2}$.  
Term 2: $1 - z + z^2 = 1 - (-i) + (-1) = 1+i-1 = i$.  
Modulus $|i| = 1$.  
Sum = $\sqrt{2}+1$.  

Let's re-evaluate $z=-i$ for the modulus calculation.  
If $z=i$, term is $1+z+z^2$?  
For $z=1$: $1-1+1 = 1$. No, $1-1+1=1$.  
Term 1: $|1+1|=2$.  
Sum = $2+1=3$.  

So far max is around 2.414? Or 3?  
Is it possible to get something larger than 3?  
Consider $z$ such that $f(z)$ is maximized.  
Since $A$ and $B$ are lengths of vectors, this can be related to the distance from origin or sum of vectors.  
But the terms depend on $z$.  

Let's rewrite the expression:  
$f(z) = |1+z| + |1 - z + z^2|$.  
Note that $z$ is a complex number on the unit circle. Let's parameterize $z = \cos \theta + i \sin \theta$.  
Since $\cos^2 \theta + \sin^2 \theta = 1$.  
$f(\theta) = |1 + \cos \theta + i \sin \theta| + |1 - (\cos \theta + i \sin \theta) + (\cos^2 \theta - \sin^2 \theta)|$? No.  
The second term is $1 - (x+iy) + (x^2-y^2)$. It's complicated with complex algebra.  
Let's rewrite in polar form.  
$z = e^{i\phi}$.  
Term 1: $|1 + z| = |1 + \cos \phi + i \sin \phi|$.  
$= \sqrt{(1+\cos \phi)^2 + \sin^2 \phi} = \sqrt{2 - 2\cos \phi}$. No.  
$(1+\cos \phi)^2 + \sin^2 \phi = 1 + 2\cos \phi + \cos^2 \phi + \sin^2 \phi = 2 + 2\cos \phi$.  
So $|1+z|^2 = 2+2\cos \phi$. Thus $|1+z| = \sqrt{2(1+\cos \phi)} = 2|\cos(\phi/2)|$. This is correct.  

Term 2: $|1 - z + z^2|$.  
$z^2 = e^{2i\phi}$. So we have $\cos 2\phi + i \sin 2\phi$? No, just $1 - (\cos \phi + i \sin \phi) + e^{2i\phi}$.  
Let's compute the modulus.  
Modulus squared: $(1 - x)^2 + y^2 + (x^2-y^2)$? No.  
Let $a = 1-x$, $b=x, c=y$. No.  
Let $u = 1-z+z^2$. $|u|^2 = |1-z+z^2|^2 = (1 - x + z^2 \bar{z})$?  
Since $\overline{z} = \bar{z}$ and $z^2 = \bar{z}^{-1}$ if $|z|=1$.  
Let's just use the algebra.  
$1 - z + z^2 = 1 - z + (1/\bar{z}) \cdot z / \bar{z}$? No.  
Use the identity $(1-z+z^2) = (z+1)(z-1) + z^2 + z$? No.  
$(z+1)^2$ expansion is $z^2+2z+1$. So $(z+1)(z-1)$?  
Let's just use algebraic manipulation on the modulus squared $|u|^2 = 1 - 2 \text{Re}(z) + z^4 - z^{-2} + z$? No.  

Let's try to relate this to $z=0$.  
At $z=i$, we have $\sqrt{2}$ and 1.  
At $z=-i$, we have $\sqrt{2}$ and 1.  
The sum is at least $\sqrt{2}+1 \approx 2.414$.  
Let's consider the expression for $\theta=0$? No, $|z|=1$ usually means on circle.  
Is it possible to make the term $|1-z+z^2|$ large and $|1+z|$ small?  
If $z = -i$, term 1 is $\approx 1.414$. Term 2 is $\approx 1$. Sum $\approx 2.414$.  
What if we move away from $i$?  
Let's check values for real $x$.  
$f(x) = |1+x| + |1-x+x^2|$.  
For $x=0$: $f(0)=|1+0| + |1|=2$.  
For $x=-1$: $f(-1)=|0| + |3| = 3$? No. $|1+(-1)|=0$. $|-i|=1$.  
If $z=x+iy$, $f(z) \ge 0$ always.  
If $x=1$, $z=i$. $A=\sqrt{2}$. $B=1$. Sum $\approx 2.414$.  
Let's check the maximum over all $z$.  

Consider the function $h(z) = |1 - z + z^2|$. Note that for $|z|=1$, this is equivalent to finding points on the circle where this value is maximized.  
Since $f(z) = |1+z| + h(z)$, and $h$ is continuous, let's check critical points or boundary conditions? The domain is compact (circle).  
If we can find an argument for the maximum being larger than 3, it would be better. But if max is at least 3, then max could be 3.  

Let's test a few other values.  
$x = e^{i\theta}$. $A = |1+z|$, $B = |1-z+z^2|$.  
We want to find $\max (A+B)$.  
Is it possible that $A$ and $B$ cancel out? No, magnitudes are positive.  
Let's see if $f(z)$ is bounded above by something simple like 4.  
Consider the point $z = -1$ again? No, sum was 1? Let me recheck that.  
$z=-1$.  
$|1+z| = |0| = 0$.  
$|1 - z + z^2| = |1 - (-1) + (-1)|^2 = |3|^2 = 9$? No.  
The term is $|1-z+z^2|$.  
If $z=-1$, this is $|1-(-1)+(-1)^2| = |1+1-1| = |1| = 1$.  
My previous calculation was correct, the modulus of something squared?  
Let's re-calculate carefully.  
$z = -1$.  
Term 1: $1+z = 0 \implies A=0$.  
Term 2: $1-z+z^2 = 1-(-1)+(-1) = 3 \implies B=3$?  
Why did I think 1 earlier? Because of a sign error or magnitude error.  
$z^2 = (-1)^2 = 1$. So $1 - (-1) + 1 = 3$.  
Is it possible to have $|1-z+z^2|$ large when $|z|=1$?  
Let's check with another point.  
Try to make $1-z+z^2$ small and 0?  
For this we want $|z^2+1-z|=0 \implies z^2+z-1=0$. $z = \frac{-1 \pm \sqrt{5}}{2}$.  
Since we require $|z|=1$, we need $z$ to satisfy the equation.  
Let's check if any solution to $z^2+z-1=0$ has modulus 1.  
$z = e^{i\theta} \implies 1 + i\sin \theta - \cos \theta$.  
Discriminant $\Delta = 4 - 4(-1) = 8$. Roots are $\frac{-1 \pm \sqrt{8}}{2} = -0.5 \pm \sqrt{2}$. No modulus is 1.  
Let's find another case where $B$ could be 3.  
If $|1-z+z^2|=3$, then $|1+z| \le |1+z|$? Not helpful.  

Is there a specific point maximizing the sum?  
Let's parameterize the sum more carefully.  
For real numbers, we saw $x=0 \implies 2$. $x=-1 \implies 3$ if term 1 is $0$ and term 2 is $3$. But I need to re-verify my manual arithmetic for $x=-1$.  
At $z=-1$, $|1+z|=0$. $|1-z+z^2|=|1+1+(-1)|=1$. Sum = $0+1=1$.  
So at $z=-1$, sum is 1.  
My previous calculation was confusing myself because I thought $z^2=1$ for $z$ near $-i$? No, $z^2=-1$ for $z=i$.  
If $z=i$, sum is $\approx 2.414$.  

Let's re-evaluate at $z=-i$.  
$A = |1 + (-i)| = \sqrt{1^2+(-1)^2} = \sqrt{2}$.  
$B = |1 - (-i) + (-1)| = |1+i-1| = |-i| = 1$? No. $|-i|=1$. Correct.  
Sum = $\sqrt{2}+1$.  

Let's look at the expression more closely.  
Maybe we can use Cauchy-Schwarz or Minkowski inequalities directly without polar form.  
We want to maximize $A+B$.  
Note that $z^2+z-1=0$ has roots with moduli $\approx 1.618$. But we need $|z|=1$.  

Is it possible that the function is bounded by 3?  
Let's check for any constraints on the modulus of $1-z+z^2$.  
By the triangle inequality, $|1-z+z^2| \le |1+z| + |z^2| = |1+z|+1$. Not useful.  
$|1-z+z^2| \le |1+z| + |z(z-1)| = A+B$.  
Let's rewrite the second term.  
$|1 - z + z^2| = |1 - (z-\overline{z})^{-1}|$?  
Let's use complex algebra to simplify the expression.  
Since $|z|=1$, $\bar{z} = 1/z$.  
$1 - z + z^2 = \frac{1}{z} (z^3 - z^3 + z - z)$. No.  
$1 - z + z^2 = \frac{z+1}{z} (1-z)$? No.  
Let's try substitution $w = 1/z$. Then $w=1/z$ and $|z|=1$ means $|w|=1$.  
Then $|1+z| = |1+w^{-1}|$. And $|1 - z + z^2| = |1 - w^{-1} + (w^{-2})|$? No, $z = w^{-1}$ is false. If $|z|=1$, then $\bar{z} = 1/z$ so $\bar{z}^{-1} = z$.  
So $z^2+1-z = \dots$  
If $z = w^{-1}$? No, $\overline{w^{-1}} = w$. So if $|z|=1$, then $z^{-1} = \bar{z}$.  
Let's write $f(z)$ in terms of $u = 1/z$.  
$f(u^{-1}) = |1+u^{-1}| + |1 - u^{-1} + u^{-2}|$?  
No, this doesn't help because $|1-u+u^{-2}|$ is related to roots.  

Let's try a different perspective.  
The expression is $f(z)$.  
Consider the function $g(t) = |1+t|$ for real $t$.  
If $z=x$, we are maximizing $A+B(x)$.  
Maybe the maximum occurs at $x=0$? No, 2.  
Maybe at some point near imaginary axis?  
Let's look at the modulus of $1-z+z^2$.  
$|1-z+z^2| = |z(z+1/z)-1-z|$? No.  
$1-z+z^2 = (1-z)(1+z) + z(1-z)$? No.  
Let's write $|1-z+z^2|^2$ as a function of $z$.  
Or maybe relate to $|1+z|$ using Cauchy-Schwarz.  
We want $\max (A+B)$.  
Consider the vectors $\mathbf{v}_1 = 1+z$, $\mathbf{v}_2 = 1-z+z^2$. No, the second term is a scalar modulus? No, it's $| \cdot |$.  
So we have $|\mathbf{v}_1| + |\mathbf{v}_2|$ where $\mathbf{v}_2$ is related to $z$.  
Let's try to find an upper bound.  
By triangle inequality, $A \le 2$, $B \le |1+z| + 1$?  
If we pick $z$ close to something such that $|1-z+z^2|$ is large, say $z$ near $i$, then $B \approx 1$.  
At $z=0$, $A=1, B=1 \implies f(0)=2$.  
At $z=i$, $A=\sqrt{2} \approx 1.414$, $B=1 \implies f(i) \approx 2.414$.  
Is there a point where both are large?  
We know that if $|z|=1$, then $|1-z+z^2|^2 \le |z|^2 + |1-z|^2$? No.  

Let's try to express $|1-z+z^2|$ using $z$.  
Let $w=1/z$. Then $f(z) = |1+1/w| + |1-1/w+w^{-2}|$.  
The first term is $| \frac{w+1}{w} | = \frac{|w+1|}{|w|} = |w+1|$ since $|w|=1$.  
So $f(z) = |w+1| + |1 - w^{-1} + w^{-2}|$ where $|z|=1$.  
Is it better?  
Let's analyze the second term again.  
$1 - z + z^2 = 1 - (1/w) + 1/w^2$. No, that's not correct.  
If $w=1/z$, then $z^{-1} = w$. Then $|z|=1 \implies |w|=1$.  
Term is $1 - w^{-1} + w^{-2}$? No, the polynomial was $1-z+z^2$.  
So if $z=w^{-1}$, term becomes $1-w+w^{-2}$?  
Let's check substitution again.  
$z = \bar{w}$ since $|z|=1$ and $\overline{z}=1/w$? No.  
If $|z|=1$, then $z=\bar{z}^{-1}$. So $z = \bar{w} \implies w=\bar{z}^{-1}$.  
This is not helpful as variables are swapped.  

Let's assume the question has a nice answer like $\sqrt{3}$ or 4.  
Let's re-verify my calculations for specific points and boundaries.  
Is there any point where $f(z) \le 4$?  
Max possible values of $|1+z|$ is when $z$ is on unit circle.  
The range of $A$ is $[0, 2]$. The maximum is 2 at $z=1$.  
At $z=1$, $B=1$. Sum = 3.  
Is there any point where $A$ and $B$ are larger?  
Suppose we find $z$ such that $A \le 1.5$ and $B \le 2$?  
Let's check $z$ near $-i$. $A=\sqrt{2}, B=1$. Sum $\approx 2.414$.  
What if $z$ is a root of something?  
If $z = i$, $f = \sqrt{2}+1$.  
Let's try to maximize $B(z) = |1-z+z^2|$.  
Since $z^2 = \bar{z}^{-1}$, we have $|1-z+z^2|^2 \le |1-\bar{z}|^2 + |z^2|$. No.  
Consider the geometric interpretation: points in complex plane are vectors.  
Let's rewrite $f(z)$ as distance from origin to a point plus another distance?  
No, $|1+z|$ is length of segment from $0$ to $1+z$.  
And $|1-z+z^2|$ is length of vector $\mathbf{v}_2$.  

Let's try a substitution. Let $z = \cos \theta + i \sin \theta$.  
Then $A(\theta) = |2 \cos(\theta/2)|$? No.  
$1+z = 1 + e^{i\theta} = e^{i\theta/2}(e^{-i\theta/2}+e^{i\theta/2}) = 2 \cos(\theta/2) e^{0}$.  
So $A = 2 |\cos(\theta/2)|$.  
This is correct.  
Now for $B(z) = |1 - z + z^2|$.  
$z^2 = e^{2i\theta}$.  
So term is $1 - (x+iy) + x^2-y^2 = 1 - x + i(1-y) + y^2$?  
Let's use polar coordinates.  
$1 - z + z^2 = 1 - r e^{i\theta} + r^2 e^{2i\theta}$? No.  
The sum is a function of $e^{i\theta}$.  
Let's denote $\zeta = z$. We want to maximize $A(\theta) + B(\theta)$ where $A(\theta)=2|\cos(\theta/2)|$, $B(\theta)=|1-\zeta+\zeta^2|$.  
Let's check the values of $B(\theta)$.  
$z = e^{i\theta} \implies z^2 = e^{2i\theta}$.  
Note that $z^3 = e^{3i\theta}$? No.  
Is there any relation between $A$ and $B$?  
If we let $z = 1 + e^{i\alpha}$ where $e^{i\alpha}$ is small? No, modulus of $z$ is 1.  
Let's consider $\mathbf{A}(\theta) = |1+z|$? No.  
Maybe there is a geometric relation between $|1+z|^2 + |1-z+z^2|^2$.  
We can try to bound $f(z)$ by something like $\sqrt{3}$ or something similar.  

Let's test the value 3 again. It came from $z=1$. But at $z=-1$, we got sum 1. At $z=i$ we got 2.414.  
So maybe max is 3? Or higher.  
Let's check if we can approach a point with value > 3.  
We want to find $A+B$ such that $A = \max |1+z|$.  
Max of $A$ over unit circle is 2 (at $z=1$).  
Max of $B$ is what?  
Let's check $B(z) = |1 - z + z^2|$.  
If $z$ approaches 0? No, on unit circle.  
Let's find where $B(z)$ attains maximum.  
Consider the polynomial $P(z) = z^3 - z^2 - z - 1$? No.  
Let's analyze $B(z)$ for $z=e^{i\theta}$.  
If $z=i$, term is $|-i|=1$.  
If $z=-i$, term is $|-i|=1$ and first term is $\sqrt{2}$, sum $\approx 2.414$.  
Is there any other point with small $A$?  
If we want to increase sum, we should make $A$ small and $B$ large.  
But $A = |1+z|$. If $z=0$, $A=1$. $B=1$. Sum 2.  
If $z=1$, $A=2$. $B=1$. Sum 3.  
If $z=-1$, $A=0$. $B=1$. Sum 1.  
If $z=2$ (on circle? No).  
Let's check if there is any point where sum is greater than 2.414.  

Let's use polar coordinates for $f(z)$.  
We have $A = \sqrt{2+2\cos \theta}$.  
$B = |1 - e^{i\theta} + e^{2i\theta}|$? No.  
$z^2$ is complex, so we have magnitude $|1-z+z^2| = | (1-e^{i\theta})(1-e^{-2i\theta}) \dots |$? No.  
Let's just evaluate the expression using polar form for the term inside.  
Let $\theta = 0$: $z=1$. $A = 2$, $B = |1-1+1| = 1$. Sum 3.  
Let $\theta = \pi/2$: $z=i$. $A=\sqrt{2}$, $B=|-i|=1$. Sum $\approx 2.414$.  
Let's check $\theta$ such that $\cos(\theta/2) = -1/2$? No.  
The value of $f(z)$ seems to depend on $\theta$.  
If $\cos(\theta/2) = \sin(\theta/2) \implies \tan(\theta/2)=1 \implies \theta=2k\pi$.  
Let's check if $B$ can be larger than 1.  
Is it possible to have $B > 1$?  
Consider $z^2+z-1=0$. Roots are $\frac{-1 \pm \sqrt{5}}{2}$. Modulus of roots is $\approx \phi^{-1}$ or something.  
If $|z|=1$, does such a $z$ exist for which $B$ is maximized?  
The polynomial $1-z+z^2 = 0$ has solutions $z= -1/3 + i \frac{\sqrt{6}}{6}$? No.  
Discriminant of $t^2+t-1$ (roots are not on unit circle).  

Let's rewrite $B(z)$ as:  
$|1-z+z^2| = | \dots |$? No, we can't factor it easily.  
Is it possible that for any $z$, $|1-z+z^2| \le |1+z| + 1$?  
Then $f(z) \le |1+z| + |1+z| + 1 = 2 |1+z| + 1$.  
If $|1+z|$ can be close to 0, then $f(z)$ is small.  
But max of $|1+z|$ is 2 (at $z=1$). So this upper bound is 5. This doesn't help with the minimum value or max value unless we know $|1+z|=0$ at some point.  

Let's try to find a lower bound for the maximum.  
We know at $z=1$, sum is 3.  
So maybe $\sqrt{3}$? Or something related to equilateral triangle geometry.  
Consider the case where $|z^2+1-z|=0$. Roots are $-1/2 \pm \dots$ no modulus 1.  

Let's look at the function values again.  
At $z=1$, sum=3.  
Is it possible to get > 3?  
For $z=i$, sum is $\approx 2.414$.  
What if we take $z = -i/2$? No, modulus must be 1.  
Let's check $z$ on the unit circle again.  
We can write $f(z) = |1+z| + |1 - z + z^2|$.  
If we define $\alpha$ such that $z = e^{i\alpha}$.  
Then $f(\theta) = 2 |\cos \theta/2| + |1 - e^{i\theta} + e^{2i\theta}|$.  
Let's try to find the max of $B(\theta)$ directly.  
$|1 - z + z^2| = |z^{-1}(z^3-1+z)| = |1-z+z^2|$? No.  
Let's compute modulus for $\theta$.  
$1 - e^{i\theta} + e^{2i\theta} = (1-e^{i\theta})^2 \times (\text{something})$?  
No.  
$e^{2i\theta} = 4 \cos^2 \theta - 1$.  
Let's try specific values again.  
If $z=i$, term is $|-i|=1$.  
If $z=-i$, term is $|-i|=1$.  
If $z=e^{i(\pi/3)}$: $\approx 0.647 + 0.809 i$.  
$|1+z| \approx 2$. No, $1+0.5+i=1.5+0.809i$. $|1+z|^2 = 2.25+1.6+3\approx 3.85$. $\sqrt{3.85} \approx 1.96$.  
$1 - z + z^2 \approx 1 - (0.647+0.809i) + (0.419-1.33i)$? No.  
$z^2 = e^{2i\pi/3} = -1/2 + i\sqrt{3}/2$.  
$1 - z + z^2 \approx 1 - (0.65+0.87i) + (-0.5+0.87i) = 1 - 1 + i(0.87-0.5)?$ No, $1-z+z^2$.  
$1-(-0.64+...)$ no $z^2=-1/2+i\sqrt{3}/2$.  
Let's do exact arithmetic for this case.  
$\theta = 60^\circ$.  
$z = \frac{1}{2} + i \frac{\sqrt{3}}{2}$.  
$A = |1+z| = |1.5 + \dots|$.  
$B = |1 - z + z^2|$. $z^2 = e^{i 120^\circ} = -\frac{1}{2} + i \frac{\sqrt{3}}{2}$? No, $e^{i2\pi/3}$.  
$z^2 = \cos(120^\circ) + i \sin(120^\circ) = -0.5 + i0.866$.  
$B = |1 - (\frac{1}{2} + i\frac{\sqrt{3}}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})| = |1 - 1 + i\frac{\sqrt{3}}{2} - \frac{\sqrt{3}}{2} i|$  
$= |0 + i(\frac{1}{2} + \frac{\sqrt{3}}{2})| = 1$. No, this is getting confusing.  
Let's use complex numbers directly.  
$z = \cos(60) + i \sin(60) = \frac{1}{2} + i\frac{\sqrt{3}}{2}$.  
$z^2 = (\cos 120 + i \sin 120) = -\frac{1}{2} + i \frac{\sqrt{3}}{2}$.  
Then $B = |1 - z + z^2|$.  
$1 - z + z^2 = 1 - (\frac{1}{2} + i\frac{\sqrt{3}}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})$.  
This equals $1 - 1 + \dots$? No.  
$1 - z + z^2 = (1 + (-1/2) + (-1/2)) + (-i\sqrt{3}/2 - i\sqrt{3}/2)$? No.  
The real part: $1 - 1/2 - 1/2 = 0$.  
The imaginary part: $- \sqrt{3}/2 - \sqrt{3}/2 = -\sqrt{3}$.  
So $B = |i(-\sqrt{3})| = \sqrt{3}$.  
This is larger than $\sqrt{2}$ (which was sum for $z=i$).  
Let's check the calculation again.  
At $z=i$, $A=\sqrt{2}, B=1$. Sum=1.414+1=2.414.  
At $z=e^{i\pi/3}$, $B=\sqrt{3} \approx 1.732$.  
At $z=i$, we got $|1-z+z^2| = |-i| = 1$? No, I calculated $\frac{1}{2} - \dots$ earlier and got $0$ for the first term. Let's re-verify carefully.  
At $z=i$: $1 - z + z^2 = 1 - i + (-1) = 1 - i - 1 = -i$. Modulus is 1. Correct.  
At $z=e^{i\pi/3}$: $1 - e^{i\pi/3} + e^{2i\pi/3}$.  
Real part of $1$ term: $1$. Real part of $-z$: $-\cos(60) = -1/2$. Real part of $z^2$: $\cos(120) = -1/2$. Sum = $1 - 1/2 - 1/2 = 0$.  
So real part is 0.  
Imaginary part of $z$: $+1 \cdot \sin(60) = \sqrt{3}/2$.  
Imaginary part of $z^2$: $\sin(120) = +\sqrt{3}/2$.  
Sum of imag parts = $i(\sqrt{3}/2 + \sqrt{3}/2) = i\sqrt{3}$.  
So the term is $i \sqrt{3}$? No.  
Let's check complex algebraic simplification again.  
$1 - z + z^2 = 1 - (\frac{1}{2} + \frac{\sqrt{3}}{2}i) + (-\frac{1}{2} + \frac{\sqrt{3}}{2}i)$.  
$= (1 - \frac{1}{2} - \frac{1}{2}) + i(\frac{\sqrt{3}}{2} - \frac{\sqrt{3}}{2}) = 0 + 0i = 0$? No, this was for $z^2$.  
I missed that $z^2 = e^{2i\pi/3} = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$?  
$e^{i120^\circ} = \cos(120) + i \sin(120) = -1/2 + i\sqrt{3}/2$. Correct.  
So $z^2$ is not a real number.  
Let's re-evaluate $1-z+z^2$.  
$1 - (\frac{1}{2} + i\frac{\sqrt{3}}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})$.  
The term is $0$ (real) and $i\frac{\sqrt{3}}{2} - i\frac{\sqrt{3}}{2}$? No.  
$1 - z = 1 - \frac{1}{2} - i\frac{\sqrt{3}}{2} = \frac{1}{2} - i\frac{\sqrt{3}}{2}$.  
Then add $z^2$: $\frac{1}{2} - i\frac{\sqrt{3}}{2} + (-\frac{1}{2} + i\frac{\sqrt{3}}{2}) = 0$.  
So if $z=e^{i\pi/3}$, then $B=0$.  
Then the sum is $|1+z| = \sqrt{2+2(-1/2)} = |1.5 - 0.866i| = \dots$. No.  
$A = \sqrt{(1.5)^2 + (\sqrt{3}/2)^2} = \sqrt{2.25+0.75} = \sqrt{3}$. No, $1/2$ is not correct for $z^2$.  
Let's re-calculate the imaginary part carefully.  
$A = |1+z|$.  
$z = 1/2 + i\sqrt{3}/2$.  
Real part of $1+z$: $1.5 - \dots$? No, real part is $1+0.5=1.5$. Imaginary part $\frac{\sqrt{3}}{2}$.  
$|1+z|^2 = 1 + 0.5^2 + (\sqrt{3}/2)^2$? No. $A^2 = (1-0.5)^2 + (\dots)$?  
No. $z = \cos(60) + i\sin(60)$.  
$|1+z|^2 = 1 + 1 - \text{Re}(z)? No. |1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
$(1+0.5)^2 + (0.866)^2 = 2.25 + 0.75 = 3$. $|1+z|=1.732$? No, that's $\sqrt{3}$.  
Is this correct? $1+\frac{1}{2} + i\frac{\sqrt{3}}{2}$. $A^2 = (1+0.5)^2 + (\sqrt{3}/2)^2$? No.  
$(1+\cos\theta)^2 + \sin^2\theta$.  
For $\theta=60^\circ$, $z = e^{i\pi/3}$, $z = \frac{1}{2} + i\frac{\sqrt{3}}{2}$.  
$|1+z|^2 = 1^2 + (\cos(\pi/3))^2 + 2(1)(0) + (i \dots)^2$? No.  
Let's use the formula $A = |e^{i\theta/2} (e^{-i\theta/2} + e^{i\theta/2})|$.  
No, that was $e^{i\theta/2}(2\cos(\theta/2))$. This is only true for $1+e^{i\theta}$? No.  
$1+z = 1 + \cos \theta + i \sin \theta$.  
For $\theta=60^\circ$:  
$A^2 = (1+1/2)^2 + (\sqrt{3}/2)^2 = 2.5 + 0.75 = 3.25$. $A = \sqrt{3.25} \approx 1.8$.  
My previous calculation was $\sqrt{3}$, which would be if term is $0$ or something else.  
Let's re-verify.  
$\theta=60^\circ$, $z=e^{i\pi/3} = 0.5 + i0.866$.  
$|1+z|^2 = (1.5)^2 + (\sqrt{3}/2)^2$? No.  
$|w+1|^2 = |1+w|^2$. Here $w=1+z$. So $w^2 = 2z - z^2 \dots$ no.  
$A^2 = (1+x)^2 + y^2$.  
$x = \cos(60^\circ)$? No. $\theta = 60^\circ$, so angle of $x+i$. No, argument is not just $\cos$.  
Let's use standard polar form. $z = e^{i\phi}$.  
$A = |1+e^{i\phi}|$.  
If $\phi=60^\circ$: $z = \frac{1}{2} + i\frac{\sqrt{3}}{2}$.  
$|1+z|^2 = (1/2 - 1)^2 + (\sqrt{3}/2)^2 + 0$? No.  
$(1/2+i\sqrt{3}/2)$ is not the point $e^{i60^\circ}$? Yes it is.  
Let's write $1+z$. It is $1+\cos(60) + i\sin(60)$.  
No. $(1)(1+1/2) + i(\sqrt{3}/2)$ is the real and imaginary parts.  
$|1+z|^2 = 1^2 + (1)^2 + \dots$ No.  
$(1+\cos\theta + i\sin\theta)$. Real part is $1+\cos\theta$. Imaginary is $\sin\theta$.  
No. $\arg(1+z) = \arctan(\frac{\sin\theta}{1+\cos\theta})$.  
Let's just calculate the value for $z=e^{i60^\circ}$.  
$A = |1+e^{i\pi/3}|^2 = (1.5 - 1/2)^2 + (\dots)$? No.  
The modulus is $\sqrt{(1+\cos \phi)^2 + \sin^2 \phi}$? No, the complex number $w=1+z$.  
$w = 1+0.5+i\sqrt{3}/2 = 1.5 + i\sqrt{3}/2$.  
$\cos(60^\circ) = 1/2$. $\sin(60^\circ) = \sqrt{3}/2$.  
So $|1+z|^2 = (1.5)^2 + (\frac{\sqrt{3}}{2})^2$ is incorrect? No.  
The real part of $w$ should be $(1+\cos\theta)$. Yes, $\cos 60 = 1/2$. So $1 + 1/2 = 3/2$.  
Imaginary part is $\sin 60 = \sqrt{3}/2$.  
So $|1+z|^2 = (3/2)^2 + (\sqrt{3}/2)^2 = 9/4 + 3/4 = 12/4 = 3$.  
So $A = \sqrt{3}$.  
My previous calculation was correct for modulus squared.  
$A=\sqrt{3} \approx 1.732$.  
Then $B=0$? Let's check $B$.  
$z^2 = e^{i2\pi/3} = -1/2 + i\sqrt{3}/2$.  
$B = |1 - z + z^2|$.  
Real part: $1 - 0.5 + (-0.5) = 0$.  
Imaginary part: $\sin(60^\circ) - \sin(120^\circ) = \sqrt{3}/2 - \sqrt{3}/2$? No, the imaginary part is $-z_{imag} + z^2_{imag}$?  
No. The term is $1 - (\frac{1}{2} + i\frac{\sqrt{3}}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})$.  
The imaginary part of $1$ is 0.  
Imaginary part of $-z$ is $-(\sqrt{3}/2)$.  
Imaginary part of $z^2$ is $(\sqrt{3}/2)$.  
Sum = $-(\sqrt{3}/2) + \frac{\sqrt{3}}{2} = 0$.  
So the imaginary part is 0.  
Real part: $1 - 0.5 - 0.5 = 0$.  
So $B=0$? No, I made a mistake in previous calc.  
Let's check again.  
If $z^2 = e^{i2\phi}$ with $\phi = \pi/3$. Then $e^{i120} = -1/2 + i\sqrt{3}/2$.  
$z^2$ is not real.  
$B = |1 - z + z^2|$.  
Real part of $1-z+z^2$: $1 + \text{Re}(z) - \text{Re}(z^2)$? No, coefficients are 1, -1, -1.  
Coeffs for real terms in expression: $1$ (real).  
Term $-z$: Real part $\cos(\pi/3) = 1/2$.  
Term $z^2$: Real part $\cos(2\pi/3) = -1/2$.  
So sum of Re parts is $1 - 1/2 - (-1/2)$? No.  
Real part of sum $1 - z + z^2$ is $1 - (0.5) - (-0.5)$? No, $1-z+z^2 = 1 - (\frac{1}{2} + i\frac{\sqrt{3}}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})$.  
Real part of $z$ is $\frac{1}{2}$. Real part of $z^2$ is $-\frac{1}{2}$.  
So real part of sum is $1 - 1/2 - (-1/2) = 1.5$? No, $-0.5$?  
Let's check signs.  
Term $-z$: Real part is $\cos(60^\circ) = 1/2$.  
Term $z^2$: Real part is $\cos(120^\circ) = -1/2$.  
Sum of real parts: $1 - 1/2 - (-1/2) = 1 - 0.5 + 0.5 = 1$? No, $-0.5$ is added. So sum is $1$.  
No, $-z^2$: $1 + (-(-1/2)) = 1 + 1/2 = 3/2$.  
Let's be systematic.  
$1 - z + z^2$.  
Real part:  
For $z=e^{i60}$, $x=0.5, y=\sqrt{3}/2$.  
For $z$, real part is $\cos(60)=0.5$.  
For $z^2$, real part is $\cos(120)=-0.5$.  
So real part of expression is $1 - 0.5 - 0.5 = 0$.  
Imaginary part:  
$-y + x$? No, $y = \sqrt{3}/2$. Imaginary part of $z$ is $\sin(60) = \sqrt{3}/2$.  
Imaginary part of $z^2$ is $\sin(120)=\sqrt{3}/2$.  
So real part is 0.  
Imaginary part is 0.  
So if this holds, then $B=0$.  
Let's check carefully.  
Expression: $1 - (\frac{1}{2} + i\frac{\sqrt{3}}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})$.  
The complex number is $1 - \frac{1}{2} + (-\frac{1}{2}) + i(\frac{\sqrt{3}}{2} - \frac{\sqrt{3}}{2})$? No.  
The imaginary part of sum: $\text{Im}(1) - \text{Im}(z) + \text{Im}(z^2)$.  
$\text{Im}(1) = 0$.  
$\text{Im}(z) = \frac{\sqrt{3}}{2}$.  
$\text{Im}(z^2) = \frac{\sqrt{3}}{2}$.  
Sum is $-0.5 + 0 = -0.5$? No, it's sum of imaginary parts.  
$1$ has $\sin(60)=\sqrt{3}/2$ as the term is imaginary.  
No, $z^2$ is also complex.  
Let's write out $1 - z + z^2$.  
$= 1 - (\cos \theta + i \sin \theta) + e^{2i\theta}$.  
Here $\theta = 60^\circ$.  
$e^{2i\theta} = \cos 120 + i \sin 120 = -0.5 + i \frac{\sqrt{3}}{2}$.  
$z = 0.5 + i \frac{\sqrt{3}}{2}$.  
$1 - z = 1 - 0.5 - i\frac{\sqrt{3}}{2} = 0.5 - i\frac{\sqrt{3}}{2}$.  
Then add $z^2$: $(0.5 - i\frac{\sqrt{3}}{2}) + (-0.5 + i\frac{\sqrt{3}}{2}) = 0$.  
So if this calculation holds, the value is $0$?  
Is it possible that I made a mistake in my sign of $\sin(120)$ or similar?  
Let's re-calculate $z^2$.  
$z^2 = e^{i2\phi}$ where $\phi = 60^\circ/2 = 30^\circ$? No, $e^{i\theta}$.  
The previous calculation for $\cos \theta$ used the identity.  
If $z=e^{i\pi/3}$, then $z^2 = e^{i2\pi/3}$.  
So $z^2 = -1/2 + i\sqrt{3}/2$.  
Term 1: $1-z+z^2$.  
Real part: $1 + (-1/2) + (-1/2) = 0$? No.  
Real part is $1 - (Re z) + (Re z^2)$.  
$Re(z) = \cos(60) = 1/2$.  
$Re(z^2) = \cos(120) = -1/2$.  
So real part is $1 - 0.5 - (-0.5) = 1$.  
No, that would be $1-0.5+0.5 = 1$.  
What about imaginary part?  
$\sin(60) - \sin(120)$? No, the terms are multiplied by $\pm i$.  
The term $-z$ has imaginary part $-\frac{\sqrt{3}}{2}$.  
The term $z^2$ has imaginary part $\frac{\sqrt{3}}{2}$.  
So sum is 0.  
So $B=0$?  
Is it possible that $B=0$ for this specific $z$?  
This means $1-z+z^2 = 0$.  
Let's check if there is a point on the unit circle such that $1-z+z^2=0$.  
$z^2+z-1=0$.  
Discriminant $\Delta = -4(1) \dots$ No, $4 - 4(-1) = 8$. Roots are $\frac{-1 \pm \sqrt{5}}{2}$. Real part is roughly $-0.618$. Modulus squared is roughly $0.618^2 + (-0.32)^2 \dots$  
$\cos(60)$, $\sin(60)$ etc are correct? No.  
The roots of $x^2+x-1=0$ are $e^{i\theta}$? No.  
If the roots were on unit circle, then $|z|=1$. But they are real numbers.  
$\frac{-1+\sqrt{5}}{2} \approx 0.618$. Modulus $\approx 0.97$.  
So this point is not on unit circle.  
Thus for this $z$, $B$ is not zero.  
Let's re-verify the calculation of $B$ for $z=e^{i\pi/3}$.  
Term: $1-z+z^2 = 1 - (0.5 + i\sqrt{3}/2) + (-0.5 + i\sqrt{3}/2)$.  
Real part: $1 - 0.5 - 0.5 = 0$.  
Imaginary part: $- \frac{\sqrt{3}}{2} + \frac{\sqrt{3}}{2} = 0$.  
So $1-z+z^2$ is purely imaginary? No, real and imag parts are zero. So it's 0?  
Is this correct?  
Let's check $z=i$. $\theta=90^\circ$.  
$1-i+(-1) = -i$. Real part 0, Imaginary part $-1 \neq 0$.  
My calculation for $B$ at $z=e^{i\pi/3}$ gave zero imaginary part and zero real part. This means $B=0$.  
This contradicts my previous manual calc where I found $B = |-i|=1$? No, I wrote that down as a check for another point.  
Let's re-calculate $B(i)$.  
$z=i \implies z^2=-1$.  
Term: $1 - i + (-1) = -i$.  
Modulus $|-i| = 1$.  
My calculation using complex arithmetic gave imaginary part 0? No, I assumed the term was purely imaginary and found it zero.  
For $z=i$: $x=0, y=\dots$  
Term is $1 - (i) + (-1)$. $Re=1-0-0 = 1$? No. $1-i+(-1) = 0$.  
So $1-z+z^2$ for $z=i$ gives $0$ in the complex plane?  
Let's check. $z^2+1=z$.  
$1 - z + z^2 = 1 - z + (-1/z)$? No, if $|z|=1$, $z^{-2}$. No, $z^2 = \bar{z}/z^2$? No.  
If $|z|=1$, then $z^2+1-z = (z-0)(z-1) + 0$?  
Let's check $1 - i + (-1)$?  
For $z=i$: $1 - i - 1 = -i$. Modulus 1.  
My complex calculation:  
$Re(1-z+z^2) = 1 - 0 + (-1) = 0$ (since $\cos 90=0$, $\sin 90=1$).  
$\Im(1-z+z^2) = \dots$  
$z=i$: $-z=-i$. $z^2=-1$.  
So $Re=1 - (-i) + (-1)$? No.  
The imaginary part of $z^2$ is $\sin 90 = 1$.  
So $B = |-i| = 1$.  
My calculation using trigonometric functions gave imaginary part $-i \sqrt{3}/2 + i\sqrt{3}/2$ which was zero? No, I used sine values.  
Sine of 60 is $\sqrt{3}/2$. Sine of 120 is $\sqrt{3}/2$.  
This corresponds to angles $30^\circ$ and $90^\circ$.  
For $z=i$, angle is $\theta=90^\circ$? No. I used $\cos(60) = 1/2$ which is wrong for $z=e^{i\pi/3}$.  
If $z=e^{i\pi/3}$, then $z^2$ has angle $2 \times 60 = 120^\circ$.  
$\sin(120) = \sqrt{3}/2$.  
My calculation was for $\theta=60^\circ$, so angles are $60, 120$.  
So for $z=e^{i\pi/3}$ (angle 60):  
$Re(z^2) = -1/2$.  
Imaginary part of $z^2$: $\sin(120)$? No. The imaginary part is $\cos \phi$.  
Let's be precise.  
If $z=1$, $B=1$.  
If $z=i$, $B=-i$ (so magnitude 1).  
My trig calculation gave zero imaginary part for $\theta=60^\circ$ which suggests I used $z^2$ with correct angles?  
Let's re-evaluate the terms for specific angles.  
$\theta = 90^\circ$. $z=i$. $A=\sqrt{2}$. $B = |1-i-1| = |-i|=1$. Sum $\approx 2.414$.  
$\theta = 180^\circ$. $z=-1$. $A=0$. $B = |1 - (-1) + 1(-1)| = |3|=3$? No, $|-1|=1$. So sum $0+1=1$.  
$\theta = 0^\circ$. $z=1$. $A=2$. $B = |1-1+1| = 1$. Sum $2+1=3$.  
For $\theta=60^\circ$, let's recalculate carefully.  
$z^2 = e^{i(2\pi/3)} = -0.5 + i \sqrt{3}/2$.  
$B = |1 - z + z^2|$.  
Real part: $1 - 0.5 + (-0.5) = 0$.  
Imaginary part: $\sin(60) - \sin(120)$? No.  
Term is $z$. $z=i$ in my previous calculation was angle $90^\circ$.  
In my trig calc for $z=1$, I used $z$ as real, so $\sin 0 = 0$.  
If $z=e^{i\pi/3}$, then $z$ is $0.5 + i \sqrt{3}/2$.  
Imaginary part of $z$ is $\sqrt{3}/2$.  
Imaginary part of $z^2$ is $\sin(120) = \sqrt{3}/2$.  
So sum is 0 for the imaginary part.  
So $B=|1 + i 0 - 0| = |0| = 0$? No, I am getting confused between "real and imaginary parts of 0".  
If both are zero, then the modulus is 0. But this implies $z^2+1-z=0$.  
Let's check if there exists a solution for $\theta$.  
For $B(z)$ to be non-zero.  
My previous calculation for $z=i$ yielded sum 3? No, it was $\approx 2.414$.  
At $z=1$, sum is 3.  
Is it possible that max is 4?  

Let's look at the question again. "Find the maximum value of $|1 + z| + |1 - z + z^2|$".  
Usually these problems have an answer like $\sqrt{5}$ or something related to integers.  
Or maybe just 3, 4, $\pi$?  
The maximum is achieved when $A = \max |1+z| = 2$ and $B=0$.  
But if $z$ must be on the unit circle, can we have $z^2+1-z=0$? No.  
Does $1 - z + z^2 = 0$ have any solutions on the unit circle? No, as I checked earlier (roots are not on unit circle).  
So $B \ge 0$.  
If $B=0$, then we must check if $A$ can be larger.  
The max value of $|1+z|$ is 2 at $z=1$. At $z=1$, $B=1$. Sum 3.  
Can we have $B > |1+z|$? No, triangle inequality: $B \le |1+z| + |z^2 - 0|$? No.  
$A+B \le |1+z| + |1-z+z^2|$.  
We want to maximize this sum.  

Let's try to prove $A \le B$ or $B \le A$ for the max.  
At $z=1$, $A=2, B=1$. Sum 3.  
At $z=-1$, $  

## Answer

*(none: the token cap hit during thinking)*
