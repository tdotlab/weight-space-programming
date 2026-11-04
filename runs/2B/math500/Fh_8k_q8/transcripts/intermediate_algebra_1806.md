# test/intermediate_algebra/1806.json (Intermediate Algebra, level 5)

> Let $z$ be a complex number such that $|z| = 1.$  Find the maximum value of  
> \[|1 + z| + |1 - z + z^2|.\]  

**Wrong.** Gold `\frac{13}{4}`, predicted `None`. Finish: length, 8192 tokens, 37 waits, 677.5 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Let $f(z) = |1 + z| + |1 - z + z^2|$. We are given that $|z| = 1$ for a complex number $z$.  
We need to find the maximum value of $f(z)$.  

Let's simplify the expression.  
$1 - z + z^2 = \frac{z^3-1}{z-1}$ if $z \neq 1$, but let's just stick to $z$.  
Since $|z|=1$, $z$ lies on the unit circle in the complex plane.  
Let $z = e^{i\theta}$. Then $|z|=1$ is satisfied for any real $\theta$.  

The expression is sum of two moduli.  
$|1+z| + |1-z+z^2|$.  

Let's evaluate $|1 - z + z^2|$ in terms of $z = e^{i\theta}$.  
Note that $z^2 - z + 1 = \frac{z^3-1}{z-1}$ (for $z \neq 1$).  
So $|z^2 - z + 1| = \left| \frac{z^3-1}{z-1} \right|$. Since $|z|=1$, $|\overline{z}|=1$, so $\left| \frac{z^3-1}{z-1} \right| = \frac{|z^3-1|}{|z-1|}$.  
$|z^3-1| = |e^{3i\theta} - 1|$. This is the chord length of $z^3$ on the circle relative to 1.  
Actually, $|z^3 - 1| = |3 \sin(\pi) + i ...|$ no.  
Let's use polar coordinates or geometry.  
$z^2 - z + 1$. Let $\omega = e^{i 2\pi/3}$. Then $\omega^2 - \omega + 1 = 0$.  
The polynomial $x^2-x+1 = (x-\omega)(x-\omega^2)$.  
So $z^2 - z + 1 = (z-\omega)(z-\bar{\omega})$ since $\bar{\omega} = e^{-i 2\pi/3} = \omega^5 = \omega^2$. No, $\omega^2 = e^{4\pi i/3} = e^{-2\pi i/3}$.  
Let's use the roots of $z^2-z+1=0$, which are $\frac{1 \pm i\sqrt{3}}{2} = -1/2 \pm i\sqrt{3}/2 = e^{\pm i 2\pi/3}$.  
So $|z^2 - z + 1| = |(z - e^{i 2\pi/3})(z - e^{-i 2\pi/3})|$.  
For any $z$ on unit circle, $|z - e^{i \alpha}|^2 = (z - e^{i\alpha})(\bar{z} - e^{-i\alpha}) = |z|^2 + 1 - z e^{-i\alpha} - z e^{i\alpha} = 2 - 2\text{Re}(z e^{-i\alpha})$.  
So $|z^2-z+1|^2 = (z-e^{i 2\pi/3})(\bar{z}-e^{-i 2\pi/3}) \dots$ wait, we have $z^2 - z + 1$. The product is $(z-z_1)(z-z_2)$.  
So $|z^2 - z + 1|^2 = |z-z_1|^2 |z-z_2|^2$. No, this is true.  
$|A|^2 = A\bar{A}$. So $|z^2 - z + 1|^2 = (z^2 - z + 1)(\overline{z^2 - z + 1})$.  
Let's use the identity for cosine again.  
$\cos(3\theta) - \dots$ no.  
$|z^2 - z + 1|^2 = z^2(z^{-1}-z+1) ...$ no.  
$|z^2 - z + 1| = \sqrt{ (e^{i2\theta} - e^{i\theta})^2 ... }$ No.  
Let $z = \cos \theta + i \sin \theta$.  
$z^2 - z + 1 = (\cos 2\theta - \cos \theta + 1) + i(\sin 2\theta - \sin \theta)$.  
Real part: $R = \cos^2 \theta - 2\sin^2 \theta + \dots$? No.  
$\cos 2\theta + 1 - \cos \theta$.  
$\cos 2\theta = 2\cos^2 \theta - 1$. So $R = (2\cos^2 \theta - 1) - \cos \theta + 1 = 2\cos^2 \theta - \cos \theta$.  
$R(\theta) = \cos \theta(2\cos \theta - 1)$.  
Wait, this looks simpler. Let me double check the identity $z^2 - z + 1$.  
The roots are $e^{i 2\pi/3}$ and $e^{-i 2\pi/3}$. These correspond to $\cos(2\pi/3) = -1/2$, etc.  
So $\frac{z-z_1}{z-z_2}$? No, we know that the magnitude is related to angles.  
Let's compute $|z^2 - z + 1|$ directly using geometry or algebraic expansion.  
$(e^{i\theta})^2 - e^{i\theta} + 1 = e^{i2\theta} - e^{i\theta} + 1$.  
$= (\cos 2\theta + i \sin 2\theta) - (\cos \theta + i \sin \theta) + 1$  
$= (1 + 2\cos^2 \theta - 1 - \cos \theta) + i(2\sin \theta \cos \theta - \sin \theta)$  
Real part: $2\cos^2 \theta - \cos \theta$.  
Imaginary part: $(2\cos \theta)\sin \theta - \sin \theta = \sin \theta (2\cos \theta - 1)$.  
Wait. Let me re-evaluate the imaginary part.  
$z^2 - z + 1 = \cos 2\theta - \cos \theta + i(\sin 2\theta - \sin \theta) + 1$? No. $e^{i2\theta}$ has $\cos 2\theta + i \sin 2\theta$.  
So Real part is $1 + \cos 2\theta - \cos \theta = 1 + (2\cos^2 \theta - 1) - \cos \theta = 2\cos^2 \theta - \cos \theta$. Correct.  
Imaginary part is $\sin 2\theta - \sin \theta = 2\sin \theta \cos \theta - \sin \theta = \sin \theta (2\cos \theta - 1)$. Correct.  
So $|z^2 - z + 1|^2 = (2\cos \theta)^2 + (\sin \theta(2\cos \theta - 1))^2$? No, just $(2\cos^2 \theta - \cos \theta)^2 + (\sin \theta (2\cos \theta - 1))^2$.  
Factor out $\cos \theta$:  
$= \cos^2 \theta (2\cos \theta - 1)^2 + \sin^2 \theta (2\cos \theta - 1)^2$? No.  
The terms are different. First term has $2\cos^2 \theta - \cos \theta$. Second has $\sin \theta(2\cos \theta - 1) = 2\sin \theta \cos \theta - \sin \theta$. Wait, $2\cos \theta \sin \theta$ is not factored out.  
Let's just use the factorization form:  
$|z^2 - z + 1|^2 = | (e^{i 2\pi/3} - e^{-i 2\pi/3}) z / ... |$ ? No.  
The polynomial $z^2 - z + 1$ divides by $(z - e^{i 2\pi/3})(z - e^{-i 2\pi/3})$.  
So roots are $\lambda_1 = e^{i 2\pi/3}$, $\lambda_2 = e^{-i 2\pi/3}$. Note $\lambda_1 \bar{\lambda}_2 = 1$ and $|\lambda|^2=1$.  
Actually, the roots of $x^2 - x + 1 = 0$ are primitive cube roots of unity. Let them be $\omega, \bar{\omega}$.  
So $|z^2 - z + 1|^2 = |z-\omega|^2 |z-\bar{\omega}|^2$.  
Let's check the magnitude of this expression.  
If $z$ is on unit circle, we can simplify.  
Wait, $z^2 - z + 1 = \frac{z^3-1}{z-1}$. This holds for $z \neq 1$. If $z=1$, $|1-1+1| = 1$, formula gives $0/0$. Limit is $3 \sin(\pi) ...$ derivative.  
Actually, limit of $\frac{z^3-1}{z-1}$ as $z \to 1$ is $3 \cdot 1 = 3$ (real). Wait, no. $x^3-1 \approx (x-1) 3$, so ratio $\approx 3(1)$.  
Let's check for $z=e^{i\pi}=-1$. $|-1 - (-1) + 1| = 1$. Limit formula: $(e^{-3 i \pi}-1)/(e^{-i \pi}-1) = (1-1)/(-2)=0$. So this is wrong.  
The identity is $\frac{z^3-1}{z-1} = z^2 + z + 1$. No! $z^3-1 = (z-1)(z^2+z+1)$.  
So the term in the problem is $|z^2 - z + 1|$, not $|z^2+z+1|$.  
My previous algebra check: $e^{i2\theta} - e^{i\theta} + 1$.  
Let's use $\cos \theta = x, \sin \theta = y$. $z^2-z+1 = (x^2-y^2) - i(2xy+y)(-1)?$ No.  
$z^2 - z + 1 = (\cos 2\theta + i \sin 2\theta) - (\cos \theta + i \sin \theta) + 1$.  
Real part $R = 1 + 2\cos^2 \theta - 1 - \cos \theta = 2\cos^2 \theta - \cos \theta$.  
Imaginary part $I = \sin 2\theta - \sin \theta = 2\sin \theta \cos \theta - \sin \theta = \sin \theta (2\cos \theta - 1)$.  
So $|z^2-z+1|^2 = R^2 + I^2 = (2\cos \theta)^2 - 4\cos^2 \theta \dots$?  
Wait, $R = \cos \theta (2\cos \theta - 1)$.  
$I = \sin \theta (2\cos \theta - 1)$.  
So $|z^2-z+1|^2 = (\cos \theta (2\cos \theta - 1))^2 + (\sin \theta (2\cos \theta - 1))^2$.  
$= (2\cos \theta - 1)^2 (\cos^2 \theta + \sin^2 \theta)$  
$= (2\cos \theta - 1)^2$.  
Wait. This is extremely simple. Let me re-verify.  
$\cos 2\theta = 2\cos^2 \theta - 1$. So $1 + \cos 2\theta - \cos \theta = \dots$  
Wait, $\cos 2\theta$ in the expression was from $z^2 = e^{i2\theta}$.  
But my expansion of real part $R$:  
Real part of $e^{i2\theta}$ is $\cos 2\theta$. Real part of $-z$ is $-\cos \theta$. Constant 1.  
So $R = \cos 2\theta - \cos \theta + 1$.  
This is $2\cos^2 \theta - 1 - \cos \theta + 1 = 2\cos^2 \theta - \cos \theta = \cos \theta(2\cos \theta - 1)$. Correct.  
Imaginary part of $e^{i2\theta}$ is $\sin 2\theta$. Imaginary part of $-z$ is $-\sin \theta$. Constant 0.  
So $I = \sin 2\theta - \sin \theta = 2\sin \theta \cos \theta - \sin \theta = \sin \theta (2\cos \theta - 1)$. Correct.  
Then $|z^2-z+1|^2 = (\cos \theta(2\cos \theta - 1))^2 + (\sin \theta(2\cos \theta - 1))^2$  
$= (2\cos \theta - 1)^2 (\cos^2 \theta + \sin^2 \theta)$  
$= (2\cos \theta - 1)^2$.  
Wow. Is it really this simple?  
Let's check for $z = e^{i 0} = 1$.  
Then $|1 - z + z^2| = |1 - 1 + 1| = 1$. Formula gives $(2(1)-1)^2 = 1$. Correct.  
Check for $z = e^{i \pi/3}$.  
$z = 1/2 + i\sqrt{3}/2$.  
$z^2 = -1/2 + i\sqrt{3}/2$.  
$z^2 - z + 1 = (-1/2 + i\sqrt{3}/2) - (1/2 + i\sqrt{3}/2) + 1 = -1/2 - 1/2 + 1 = 0$.  
Wait, if $z$ is a root of $z^2-z+1=0$, then the modulus is 0.  
Roots are $e^{i 2\pi/3} = -1/2 + i\sqrt{3}/2$ and $e^{-i 2\pi/3}$.  
Wait, $e^{i \pi/3}$ is not a root of $z^2-z+1=0$?  
The roots are $\omega, \omega^2$. $\omega = e^{i 2\pi/3} = -1/2 + i\sqrt{3}/2$.  
Angle of roots is $\pm 120^\circ$. Angle of $z=e^{i \theta}$ can be anything.  
Why did my calculation for $z = e^{i \pi/3}$ yield something else?  
Let's re-evaluate $z^2 - z + 1$ for $e^{i \pi/3}$.  
$z^2 = e^{i 2\pi/3} = \omega$.  
Then $z^2 - z + 1 = \omega - (\cos 60^\circ + i \sin 60^\circ) + 1$.  
$\omega = -1/2 + i\sqrt{3}/2$.  
$-z = -1/2 - i\sqrt{3}/2$.  
So sum is $(-1/2 + i\sqrt{3}/2) + (-1/2 - i\sqrt{3}/2) + 1 = -1 + 1 = 0$.  
Wait, I made a mistake in the calculation.  
$z^2 - z + 1 = \frac{z^3-1}{z-1}$.  
If $z = e^{i \pi/3}$, then $|z|=1$. $z^3=1$, so numerator is 0? No.  
Wait, if $z = e^{i \pi/3}$, then $z^2 + z + 1 = (e^{i\theta})^2 + e^{i\theta} + 1$?  
Recall roots of unity: $x^3-1 = (x-1)(x^2+x+1)$. Roots are $1, \omega, \omega^2$ where $\omega = e^{i 2\pi/3}$.  
So $z^2 - z + 1 = 0$ implies $z^2-z+1=0$. The roots of this polynomial are $\frac{1 \pm i\sqrt{3}}{2}$, which is $e^{\pm i 2\pi/3}$.  
My calculation for $z = e^{i \pi/3}$ gave result 0.  
Let's check again.  
$z = 1/2 + i\sqrt{3}/2$. This is $e^{i \pi/3}$.  
Roots of $z^2-z+1=0$: $\frac{1 \pm i\sqrt{3}}{2}$. These are at angles $60^\circ$? No, that's $z=e^{i \pi/3}$. Wait.  
Let's check magnitude of roots.  
Roots of $x^2-x+1=0$: sum 1, product 1. Modulus $\lambda_1 + \lambda_2 = 1$, $\lambda_1 \bar{\lambda}_1 = |\lambda|^2=1$. So they are on unit circle? No.  
Roots of $z^2-z+1$: Discriminant $D = (-1)^2 - 4(1)(1) = -3$.  
Roots are $\frac{1 \pm i\sqrt{3}}{2}$.  
These are indeed $e^{i \pi/3}$? No, $e^{i \pi/3} = 1/2 + i\sqrt{3}/2$.  
Wait. $\omega^2 - \omega + 1 = e^{-2\pi i/3} - e^{2\pi i/3} + 1$? No.  
$\lambda_1 = e^{i 2\pi/3}$ is a root? $e^{i 2\pi/3}$ squared is $e^{i 4\pi/3}$. $e^{i 4\pi/3} - e^{i 2\pi/3} + 1 = (-1/2 - i\sqrt{3}/2) - (-1/2 + i\sqrt{3}/2) + 1 = -i\sqrt{3} \neq 0$.  
Wait, $x^2-x+1$ roots are $e^{\pm i \pi/3}$? No.  
$|e^{i \theta}|=1$. Let's check $e^{i 2\pi/3}$. $\omega$. $\omega^2-\omega+1 = e^{-2\pi i/3} - e^{2\pi i/3} + 1 = -i\sqrt{3} \neq 0$?  
Ah. Roots of $x^2-x+1=0$. Let roots be $\lambda_1, \lambda_2$. Then $\lambda_1 + \lambda_2 = 1$, $\lambda_1 \lambda_2 = 1$.  
Since product is real and positive (1) and sum is real (1), the quadratic must have roots that are complex conjugates.  
Let's check magnitude of $e^{i \pi/3}$. Let $\alpha = e^{i \pi/3}$. $\alpha^2 - \alpha + 1 = 0$?  
$\alpha^2 = e^{i 2\pi/3} = -1/2 + i\sqrt{3}/2$.  
$\alpha = 1/2 + i\sqrt{3}/2$.  
$\alpha^2 - \alpha + 1 = (-1/2 + i\sqrt{3}/2) - (1/2 + i\sqrt{3}/2) + 1 = -1 + 1 = 0$.  
Yes! The roots of $z^2-z+1$ are at angles $\pi/3$ and... wait.  
Let's check conjugate: $\bar{\alpha} = e^{-i \pi/3}$.  
$\alpha^2 - \alpha + 1 = \frac{1 - i\sqrt{3}}{2} - \frac{1 + i\sqrt{3}}{2} + 1$? No.  
Let's re-evaluate $\lambda_1 + \lambda_2 = 1$. If $\lambda = r e^{i \phi}$, then $e^{i \phi} + e^{-i \phi} = 2 \cos \phi = 1$, so $\cos \phi = 1/2$, $\phi = \pm \pi/3$.  
So roots are at $\pm \pi/3$ and product is $|z|^2=1$? Wait.  
If $\lambda_1 = e^{i \pi/3}$, $\lambda_2 = e^{-i \pi/3}$. Then sum is 2/2? No.  
Sum of $e^{i \pi/3}$ and $e^{-i \pi/3}$ is $2\cos(\pi/3) = 1$. Product is 1.  
So the roots are indeed $e^{\pm i \pi/3}$. Wait, earlier I said they are $\omega$. Which one is it?  
Wait, $x^2-x+1$ has discriminant $1-4=-3$, so roots are complex.  
Roots formula: $z = \frac{1 \pm \sqrt{-3}}{2} = \frac{1 \pm i\sqrt{3}}{2}$.  
This matches $e^{i \pi/3}$ (and its conjugate). Wait, $e^{i 60^\circ}$ is $\cos 60 + i \sin 60 = 1/2 + i\sqrt{3}/2$.  
My roots were $\frac{1 \pm i\sqrt{3}}{2} = 1/2 \pm i\sqrt{3}/2$. Yes, that matches.  
Wait, I confused $\omega$ with $e^{i 2\pi/3}$ which are the primitive cube roots of unity.  
Primitive cube roots satisfy $x^2+x+1=0$? No, $x^3-1=(x-1)(x^2+x+1)$. So roots of $x^2-x+1$ are related to $\omega, \omega^2$?  
Let's solve $z^2-z+1=0$. Roots are $e^{i \pi/3}$ and $e^{-i \pi/3}$. Wait.  
$(e^{i \pi/3})^2 - e^{i \pi/3} + 1 = e^{i 2\pi/3} - e^{i \pi/3} + 1$. No.  
Wait, $x = e^{i \pi/3}$ satisfies $x^2-x+1=0$? Let's check again carefully.  
$x = 1/2 + i\sqrt{3}/2$.  
$x-1 = -1/2 + i\sqrt{3}/2 = \frac{-1+i\sqrt{3}}{2} = e^{i 2\pi/3}$? No.  
Wait, $x^2 = -1/2 + i\sqrt{3}/2 = e^{i 2\pi/3}$. This is $\omega^{-1}$ or something.  
Is $e^{i \pi/3}$ a root of $z^2-z+1=0$?  
The roots are $e^{i 2\pi/3}$ and $e^{-i 2\pi/3}$ if the polynomial was $z^2+z+1$.  
For $z^2-z+1$, roots must satisfy $\frac{1 \pm i\sqrt{3}}{2} = e^{\pm i \pi/3}$. Let's check.  
$e^{i \pi/3}$ is a root of $z^2+z-1=0$? No.  
Let's calculate $(z - e^{i \pi/3})(z - e^{-i \pi/3}) = z^2 - (z_1+z_2)z + z_1 z_2 = z^2 - (\frac{1+i\sqrt{3}+1-i\sqrt{3}}{1?})$. No.  
Sum is $e^{i \pi/3} + e^{-i \pi/3} = 2 \cos(\pi/3) = 1$.  
Product is $|e^{i \pi/3}|^2 = 1$.  
So roots of $z^2 - z + 1$ are indeed $e^{i \pi/3}$ and $e^{-i \pi/3}$.  
Wait, I must have messed up my check earlier.  
$z = e^{i \pi/3}$. $z^2 - z + 1 = 0$.  
This implies roots are $\omega$ where $\omega^3=1$. But roots of $x^2-x+1$ are cube roots of unity other than 1? No.  
$x^2+x+1=0 \implies x^3=1, x \neq 1$. Roots are $e^{i 2\pi/3}, e^{-i 2\pi/3}$.  
Then $x^2-x+1$ should have roots where? No.  
$x^2+x+1 = 0 \implies x^3-1=0, x \neq 1$. Roots are $\omega$.  
$x^2-x+1 = 0$. Let's solve $x^3-1$ for this? No.  
$(x-1)(x^2+x+1) = x^3-1$. So roots of $x^2+x+1$ are cube roots of unity excluding 1. These are $\omega, \omega^2$ where $\omega = e^{i 2\pi/3}$.  
Wait, let's re-verify the equation given in problem: $z^2-z+1$.  
This is different from $z^2+z+1$. The signs of coefficients are opposite.  
Roots of $z^2-z+1$: Sum=1, Prod=1. Roots are $e^{i \pi/3}$ and $e^{-i \pi/3}$.  
Check: $(e^{i \pi/3})^2 - e^{i \pi/3} + 1 = e^{i 2\pi/3} - (1/2 + i\sqrt{3}/2) + 1 = (-1/2 + i\sqrt{3}/2) - 1/2 - i\sqrt{3}/2 + 1 = -1/2 - 1/2 + 1 = 0$.  
Okay, so the roots are $e^{i \pi/3}$ and $e^{-i \pi/3}$. These correspond to angles $\pm 60^\circ$.  
Wait, if $z = e^{i \pi/3}$, then $|z^2 - z + 1| = 0$? Yes.  
So the modulus is 0 at $z = \frac{1}{2} \pm i\frac{\sqrt{3}}{2}$.  

Okay, let's look at the function again.  
$f(z) = |1+z| + |z^2-z+1|$.  
We know $|1+z|^2 = (1+\cos \theta)^2 + \sin^2 \theta = 1 + 2\cos \theta + \cos^2 \theta + \sin^2 \theta = 2 + 2\cos \theta$.  
So $|1+z| = \sqrt{2(1+\cos \theta)} = \sqrt{4\cos^2(\theta/2)} = 2|\cos(\theta/2)|$.  
Now let's look at the second term. $g(z) = |z^2-z+1|$.  
We found $g(z)^2 = (2\cos \theta - 1)^2$? No, that was derived earlier and I was unsure about it.  
Let's redo the calculation of $g(z)$ carefully.  
$z^2 - z + 1 = (\cos 2\theta - \cos \theta + 1) + i(\sin 2\theta - \sin \theta)$.  
Real part: $\cos 2\theta - \cos \theta + 1 = 2\cos^2 \theta - 1 - \cos \theta + 1 = 2\cos^2 \theta - \cos \theta = \cos \theta (2\cos \theta - 1)$.  
Imaginary part: $\sin 2\theta - \sin \theta = 2\sin \theta \cos \theta - \sin \theta = \sin \theta (2\cos \theta - 1)$.  
Modulus squared: $R^2 + I^2 = \cos^2 \theta (2\cos \theta - 1)^2 + \sin^2 \theta (2\cos \theta - 1)^2$  
$= (2\cos \theta - 1)^2 (\cos^2 \theta + \sin^2 \theta) = (2\cos \theta - 1)^2$.  
So $g(z) = |z^2-z+1| = |2\cos \theta - 1|$.  
Wait, earlier I said roots are $e^{\pm i \pi/3}$. Let's check if the condition holds.  
$2\cos(60^\circ) - 1 = 2(1/2) - 1 = 0$. So yes, for $\theta = \pi/3$, modulus is 0.  
But I derived $|z^2-z+1| = \sqrt{4\cos^2(\pi/6)}$? No.  
The formula gives $(2(1/2)-1)^2 = 0$. Correct.  
Wait, earlier I checked $\theta = \pi/3$ in the first derivation (roots check).  
And here $|z^2-z+1|$ is simply $|2\cos \theta - 1|$.  
Is that correct?  
Let's check another point. $\theta = \pi/2$. $z = i$.  
$z^2-z+1 = -1-i+1 = -i$.  
$|-i| = 1$. Formula: $|2(0) - 1| = |-1| = 1$. Matches.  
Let's check $\theta = \pi$. $z = -1$.  
$z^2-z+1 = 1 - (-1) + 1 = 3$.  
Formula: $|2(-1) - 1| = |-3| = 3$. Matches.  
So $g(z) = |2\cos \theta - 1|$.  

Wait, is it always true that $\sqrt{z^2-z+1}$ modulus equals $|2\cos \theta - 1|$?  
The formula derived from polar coordinates seems robust.  
Let me double check the identity $|z^2 - z + 1|^2 = (2\cos \theta - 1)^2$.  
This means $g(z) = |2\cos \theta - 1|$.  
Is it possible that this expression is wrong? Let's test with $\cos \theta = 1/2$ ($z = e^{i \pi/3}$). Modulus is 0.  
Let's check algebraically: $g(z)^2 = (z^2-z+1)(\bar{z}^2-\bar{z}+1)$.  
Since $\bar{z} = 1/z$, $\bar{z}^2 = 1/z^2$.  
$= (z^2-z+1)/z^2 \cdot (1-z^{-2}-z^{-1})$? No.  
$(1+z)^2 = 1 + 2z + z^2$ is not helpful.  
Let's check $|z^2-z+1|^2$ again using $z=e^{i\theta}$.  
$|e^{2i\theta} - e^{i\theta} + 1|^2 = | (e^{2i\theta}-1) - e^{i\theta}|^2$. No.  
Let's expand $(e^{2i\theta} - e^{i\theta} + 1)(e^{-2i\theta} - e^{-i\theta} + 1)$  
$= 1 + (-e^{i\theta}-e^{-i\theta}) + (-1+1) + \dots$?  
Term by term:  
Constant: $1 \cdot 1 = 1$.  
Linear in exponents:  
$e^{2i\theta} e^{-2i\theta} = 1$. Wait. $(z^2)(\bar{z}^2) = |z|^4 = 1$.  
$(z^2)(-\bar{z}) + (-z)(z^2 \bar{z}^{-2}) \dots$ No, this is messy.  
Let's use the identity: $|z^2 - z + 1|^2 = (z-z_1)(\bar{z}-\bar{z}_1) |z-\bar{z}_1 \bar{z}|$? No.  
Let's trust the trigonometric expansion. It was straightforward.  
Real part: $\cos(2\theta) - \cos(\theta) + 1$.  
$\cos(2\theta) = 2\cos^2 \theta - 1$. So $2\cos^2 \theta - \cos \theta$.  
Imag part: $\sin(2\theta) - \sin(\theta)$.  
$= 2\sin \theta \cos \theta - \sin \theta = \sin \theta (2\cos \theta - 1)$.  
Square sum: $(2\cos \theta - 1)^2 (\cos^2 \theta + \sin^2 \theta) = (2\cos \theta - 1)^2$.  
So $|z^2-z+1| = |2\cos \theta - 1|$.  
This looks very nice.  

So the problem reduces to maximizing  
$H(\theta) = 2|\cos(\theta/2)| + |2\cos \theta - 1|$ for $\theta \in [0, 2\pi)$.  
Let's rewrite in terms of $u = \cos \theta$. Since $\theta$ is real, $u \in [-1, 1]$.  
However, there are branches involved. $\cos(\theta/2)$ ranges from -1 to 1 as $\theta$ goes $0 \to 2\pi$, but it's a function of half-angle.  
Let's analyze the terms separately.  
Term 1: $A = |2\cos(\theta/2)|$. This can be written as $2 |\cos(\theta/2)|$. Let $u_1 = \cos(\theta/2)$.  
Note that as $\theta$ goes from $0$ to $2\pi$, $\theta/2$ goes from 0 to $\pi$.  
Then $u_1$ goes from $1$ to $-1$.  
So $A(\theta)$ ranges from 0 (at $z=-1, \theta=\pi$) to 2 (at $z=1, \theta=0$? No. At $\theta=0$, $|1+z|=2$, so $u_1=1$).  
Wait, at $\theta=0$, $z=1$. $|1+1| = 2  

## Answer

*(none: the token cap hit during thinking)*
