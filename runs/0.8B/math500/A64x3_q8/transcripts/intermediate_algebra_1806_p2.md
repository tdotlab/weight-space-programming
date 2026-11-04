# test/intermediate_algebra/1806.json, part 2 of 2

[Previous part](intermediate_algebra_1806.md)

$|1-z+z^2|^2 = (1-\cos\theta+\cos 2\theta)^2 + (\sin\theta - \sin 2\theta + \dots )^2$?  
The imaginary part is $\text{Im}(z) = \sin\theta$.  
Is that it? No, $z^2$ has imag part $\sin 2\theta$.  
But $f_2(\theta)$ must also have a real part.  
Real part of $(1-z+z^2)$ is $1 - \cos\theta + \cos 2\theta$.  
Imaginary part is $\sin\theta + \sin 2\theta$? No, that's $z+ \dots$.  
Let's check:  
$z = \cos\theta + i\sin\theta$.  
$z^2 = \cos 2\theta - i\sin 2\theta$. (Since $\text{Re}(z)=\cos\theta$, $\text{Im}(z)=\sin\theta \implies z=\cos\theta+i\sin\theta$).  
So $1-z+z^2 = (1-\cos\theta+\cos 2\theta) + i(\sin\theta - \sin 2\theta)$? No.  
The term $z$ is real and imaginary part $\sin\theta$. The term $-z$ adds a real part $\sin\theta$ to the imaginary part of something? No.  
Let's just write it out:  
$f_1(z) = \sqrt{2 + 2\cos\theta}$.  
We want max over $\theta$ for this quantity. Let's look at its range again.  
At $\theta=0$, $z=1$, value is 2.  
At $\theta=\pi$, $z=-1$, value is 0.  
At $\theta=\pi/2$, $z=i$, value is $\sqrt{2}$.  
The maximum of the square is $4$. The max of the expression itself (magnitude) is not necessarily related to this.  
However, note that for $f_1(z)$, we have $|1+z|^2 = 2(1+\cos\theta)$. This is maximized when $\cos\theta=1$ ($z=1$), where value is 4? No.  
At $z=1$, $|1+1|=2$, squared is 4. Correct.  
So range of $|1+z|^2$ is $[0, 4]$.  

Now for $f_2(z)$. We need to maximize $|1-z+z^2|$ on unit circle.  
This looks like the magnitude of a polynomial evaluated at points on the unit circle.  
Let's use the substitution $w = z + 1/2$? No.  
Let's look at it as distance from origin to $(1, -z+ \dots)$.  
Actually, consider the complex numbers $z^3-1 = (z-1)(z^2+z+1)$ is not helpful directly.  
Is there a connection with $\cos(\theta/2)$?  
Let's substitute $z$ such that we can simplify terms.  
Note that for any $|z|=1$, $z^* = 1/z$.  
Let's try to find the maximum of $f_2(z)$.  
$f_2(z) = |1 - z + z^2|$.  
Let's rewrite this as a polynomial in terms of $(z-1)^2$? No.  
Consider $\theta$ such that $\cos\theta$ and $\sin\theta$ are nice values.  
What if we use the identity $|a+b|^2 = (a+b)(a+\bar{b})$? No.  
What about geometric interpretation?  
The point $w_1 = 1+z$. $z=e^{i\theta}$, so $w_1$ is at distance $\sqrt{4+2\cos\theta}$.  
This is on the circle of radius $\sqrt{2+2\cos\theta}$. No.  
The locus of $w_1$ is a circle? No.  
Let's try to relate this to the problem from "Max of |z^3+1+z|"? No, problem text says "Find the maximum value".  

Let's check for values near 3. We saw sum was 3 at $\theta=\pi$ (z=-1) or $\theta=0$ (z=1).  
Are there points where it exceeds 3?  
Try $z=i \implies f_2=0$. Sum $\approx 1.41$.  
Try $z=e^{i 60^\circ} = \frac{1}{2} + i\frac{\sqrt{3}}{2}$.  
$|1+z| = \sqrt{(1+0.5)^2 + (\sqrt{3}/2)^2} = \sqrt{2.25 + 0.75} = \sqrt{3} \approx 1.732$.  
$f_2 = |1 - z + z^2|$.  
$z = e^{i\pi/6}$.  
$z^2 = e^{i\pi/3}$.  
$f_2 = |1 - (\frac{1}{2} + i\frac{\sqrt{3}}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{3})|$.  
$z^2+1 = 1 - \cos(60) + \sin(60)$? No.  
$1+z-z^2$ ? $1-(e^{i\pi/6})+(\dots)$.  
This seems tedious.  

Let's try to find an upper bound or a specific point.  
If the maximum is 3, then for all $\theta$, $|1-z+z^2| \le 3$. This is likely not true because at $z=i$ we have 0, but near $z=-1$ it's 3.  
At $\theta=\pi$, $f_2=3$. At $\theta=0$, $f_2=1$.  
The maximum of the second term for $|z|=1$ is likely 3? Or maybe higher?  
Let's recheck $z=i$. Then $f_2 = |1-i+i^2| = |-i| = 1$.  
Is it possible to have a larger value?  
Consider $\theta$ such that $z=1$.  
If we approach $\theta=0$, $z \to 1$, then $f_1 \to 2, f_2 \to 1$, sum $\to 3$.  
At $\theta=\pi$, $z=-1$, $f_1 \to 0, f_2 \to 3$, sum $\to 3$.  
So max seems to be around 3.  

Let's verify if any other point gives more than 3.  
What about $z$ such that $|1+z|$ is small? No, min of $f_1$ is 0 at $z=-1$.  
We want $|1-z+z^2|$ to be large but not too large relative to the previous one.  
However, if $|1-z+z^2|$ is large, then it suggests that $z$ is far from the roots of unity or something?  
What if we consider complex numbers such that $1-z+z^2$ has a specific structure.  
Maybe use the substitution $w = z+1/2$. No.  

Let's analyze the expression more generally.  
We want to maximize $|z^3-1|$? No.  
Consider $(z+1)(z^2+z+1) + 1 - z + z^2 = \dots$?  
Maybe consider $(z^2-1)^2$? No.  

Let's try to use Cauchy-Schwarz or AM-GM on the terms directly.  
Is there any identity relating $|1+z|$ and $|1-z+z^2|$?  
Recall that $|1+z|^2 + |1-z+z^2|^2 \le 4$?  
If we can prove this, then sum $\le 2$. But this is for product or something.  
Actually, if $z=i$, $f_1=\sqrt{2}$, $f_2=0$, so $2\sqrt{2} > 3$. No, that was my previous check?  
$\sqrt{2} + 0 \approx 1.414 < 3$. So max is definitely at least 3.  

Let's test if there's a constraint $f_2 \le f_1$ or similar?  
Or maybe $|1-z+z^2|^2 = (1-z+z^2)(1-\bar{z}+\bar{z^2})$.  
Since $z^* = 1/z$, $\overline{z} = \cos\theta - i \sin\theta$? No, $\bar{z} = e^{-i\theta}$.  
$f_1(z) |w| = |1+z|^2$.  
Also note that $f_2(z) = |1-z+z^2| = |z^3-1|/|z|$ ? No.  
Let's try to write $|1-z+z^2|^2$ in terms of something else.  
Wait, let's rewrite $z^2+1$. No.  

Let's calculate at $z=e^{i 2\pi/3}$.  
$f_1 = |1+e^{i 2\pi/3}| = \sqrt{3+2}$?  
$|1+e^{i(60^\circ)}|^2 = 1+e^{i 60} + e^{-i 60} + 1$.  
Let's calculate exactly.  
$z = e^{i2\pi/3} = -1/2 + i\sqrt{3}/2$.  
$|1+z|^2 = |1 + (-1/2) + i(\sqrt{3}/2)|^2 = |-1/2 + i\sqrt{3}/2 + \dots|$? No.  
$|1+z|^2 = 1+e^{i60} + e^{-i60}$ is false.  
$|1+z|^2 = |1+z|^2$.  
Let's use the formula $|1+e^{i\theta}|^2 = (1+\cos\theta)^2 + \sin^2\theta = 2+2\cos\theta$.  
For $\theta=60^\circ$ ($2\pi/3$), $f_1(z) = \sqrt{4-0.5(2)} = \sqrt{3}$? No, max of $f_1$ is 2 at $\theta=0$, min 0 at $\theta=\pi$.  
So $|1+z|$ for $z=e^{i2\pi/3} = -1/2 + i\sqrt{3}/2$:  
$f_1^2 = 2+2(-1/2) = 1$. So $f_1=1$.  
Is it?  
$z=-1/2 + i\sqrt{3}/2$. $1+z = 1/2 + i\sqrt{3}/2$. Modulus is $\sqrt{1/4+3/4} = 1$. Yes.  
So sum for $z=e^{i2\pi/3}$: $f_1=1, f_2=\dots$  
Let's calculate $f_2(\theta) = |1 - z + z^2|$ at this angle.  
$f_2^2 = |1 - (-1/2+i\sqrt{3}/2) + (-1/2-i\sqrt{3}/2)|^2$? No, $z^2 = e^{i4\pi/3} = -1/2 - i\sqrt{3}/2$.  
So term is $1 - z + z^2 = 1 - (-1/2+i\sqrt{3}/2) + (-1/2-i\sqrt{3}/2) = 1.5 - \sqrt{3}/2 - \sqrt{3}/2$? No.  
Sum: $1 + 0.5 - 0.5 - i(\dots)$.  
Real part: $1 + (-1/2) - (-1/2) = 1$. No, let's calculate carefully.  
$z = -\frac{1}{2} + i \frac{\sqrt{3}}{2}$.  
$-z = \frac{1}{2} - i \frac{\sqrt{3}}{2}$.  
$z^2 = e^{i(60^\circ) \times 2}$? No. $e^{i4\pi/3} = -1/2 - i\sqrt{3}/2$.  
Sum: $1 + (-1/2+i\sqrt{3}/2) + (-1/2-i\sqrt{3}/2)$? No.  
The term is $1 - z + z^2 = 1 - z + z^2$ where $z=e^{i\theta}$.  
$f_1(z) = \sqrt{2(1+\cos\theta)}$.  
$f_2(z) = |1-z+z^2|$.  
Let's try $\theta = 3\pi/4$.  
$z = -1/\sqrt{2} + i 1/\sqrt{2}$.  
$|1+z|^2 = 2(1+\cos(3\pi/4)) = 0$. So $f_1=0$.  
$f_2(z) = |1 - z + z^2|$.  
Real part of $z$: $\frac{-1}{\sqrt{2}}$. Imaginary part: $1/\sqrt{2}$.  
$-z$: $\frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}}$.  
$z^2$: $\cos(3\pi/2) + i\sin(3\pi/2)$? No, $e^{i 3\pi/4} = \frac{-1+i}{\sqrt{2}}$. $z^2 = -\frac{1-i}{\sqrt{2}}$.  
Sum real: $1 - (-\frac{1}{\sqrt{2}}) + (-\frac{1}{\sqrt{2}})$.  
Real part of $(1-z+z^2)$ is $1 - 0.5(1+ \dots)$? No.  
$1 + \cos 60 = 3/4$?  
Let's check real part:  
$Re(1 - z + z^2) = 1 - \text{Re}(z) + \text{Re}(z^2) = 1 - (-\frac{1}{\sqrt{2}}) + \frac{-1}{\sqrt{2}} = 1$.  
Real part is 1.  
Imaginary part:  
$0 - \sin\theta + \sin(3\pi/4) = - (1/\sqrt{2}) + (\sqrt{2}/2) = 0$? No, $\cos(\theta)$ and $\sin(\theta)$ are real.  
$\text{Im}(z) = 1/\sqrt{2}$.  
$\text{Im}(z^2) = -1/\sqrt{2}$? No, $3\pi/4$ is second quadrant.  
$e^{i(3\pi/4)} = \cos(3\pi/4)+i\sin(3\pi/4)$. Real part is $-0.577$. Imaginary part is 0.577? No, $\sqrt{2}/2$ is approx 0.707.  
$\sin(135^\circ) = \frac{\sqrt{2}}{2}$.  
So $\text{Im}(z) = \sqrt{2}/2$.  
$\text{Im}(z^2) = -\sin(90^\circ)$? No, $2\theta$ goes from 270.  
Let's use values: $135^\circ$. $\cos= -\frac{\sqrt{2}}{2}$, $\sin=\frac{\sqrt{2}}{2}$.  
$\text{Im}(z) = \frac{\sqrt{2}}{2}$. $\text{Re}(z) = -\frac{\sqrt{2}}{2}$.  
$z^2$: $375^\circ$. $\cos(67.5)$? No, $3\pi/4 + 2\pi$ ? No. $e^{i3\pi/4} \cdot e^{i\pi} = -1 - i$. No, just rotate by $90$.  
$z^2 = e^{i(3\pi/2) } = -1$.  
So $z^2 = -1$?  
Let's check: $\theta=135^\circ$.  
$z = (-1/\sqrt{2}) + i (1/\sqrt{2})$.  
$\text{Re}(z^2) = \cos(270)$? No. $e^{i 3\pi/4}$? No. $z = e^{i\theta}$. $z^2$ is $e^{i2\theta}$.  
If $\theta=135^\circ$, then $2\theta = 270^\circ$. $e^{i270} = -i$.  
So real part 0, imag part 0. No. Real part of $z^2$ is $-1/2$, no.  
$\text{Re}(e^{i270}) = \cos(3\pi/2) = 0$. Imaginary part $\sin(3\pi/2) = -1$. No, $\text{Im}(-i) = -1$.  
So $z^2 = 0 + i(-1)$?  
No. $\cos(270) = 0$. $\sin(270) = -1$. So $z^2$ is purely imaginary.  
My mistake earlier was thinking $z^2=0$.  
Let's re-calculate properly.  
$\theta = 3\pi/4$.  
$z = \cos(135^\circ) + i \sin(135^\circ) = -\frac{1}{\sqrt{2}} + i \frac{1}{\sqrt{2}}$.  
$z^2 = e^{i 270^\circ} = -i$.  
So $f_2(z) = |1 - (-\frac{1}{\sqrt{2}} + i \frac{1}{\sqrt{2}}) + (-i)| = |1 + \frac{1}{\sqrt{2}}(1-i) - i|$.  
This is getting complicated.  

Let's try to calculate $f_2$ using polar form.  
$f_2^2 = (1-\cos\theta+\cos 2\theta)^2 + (\sin\theta-\sin 2\theta \dots)$? No.  
We need to be very precise with $\text{Im}$ part.  
$f_2(z) = |1 - z + z^2|$.  
Let $a(\theta) = 1-z+z^2$.  
$f_2^2(\theta) = (1-\cos\theta+\cos 2\theta)^2 + \dots$?  
No, the imaginary part is $\text{Im}(z) + \text{Im}(z^2)$? No.  
The term is $-z+z^2$.  
$\text{Im}(-z) = -\sin\theta$.  
$\text{Im}(z^2) = \sin 2\theta$.  
So imaginary part of the sum is $\sin 2\theta + \cos(\dots)$? No.  
$-i\sin\theta + i\sin 2\theta = i(\sin 2\theta - \sin\theta)$.  
Real part is $1 - \cos\theta + \cos 2\theta$.  
So $f_2^2 = (1-\cos\theta+\cos 2\theta)^2 + (\sin(2\theta) - \sin\theta)^2$. No.  
Is that all?  
We also need to consider the real part of $\bar{z} z^2$ terms?  
No, just $(a+ib)^2 = a^2-b^2$.  
Let's re-evaluate $f_1(z)$ and $f_2(z)$.  
At $z=1$, $f_1=2, f_2=1$. Sum=3.  
$f_1(i)=\sqrt{2}, f_2=0$.  
Is it possible that $f_2$ can be $-3$? No, magnitude.  
Is it possible to get value 4?  
Suppose we pick $z=i$, sum is $\approx 1.41$.  
So max is likely around 3.  

Let's double check the constraint $|z|=1$.  
If $z=1$, $|1+z| = 2$, $|1-z+z^2| = |1| = 1$. Sum 3.  
If $z=-1$, $|1+z| = 0$, $|1-(-1)+(-1)| = |1+1+1| = 3$. Sum 3.  
What if $z=i$? $f_1=\sqrt{2}, f_2=0$. $\approx 1.41$.  
Is it possible to get larger than 3?  
Suppose $z=i\theta$.  
$f_1^2 = 2(1+\cos\theta)$.  
$f_2^2 = (1-\cos\theta+\cos 2\theta)^2 + (\sin\theta + \sin 2\theta - \sin\theta)^2$? No.  
Let's re-evaluate $f_2(\theta)$ properly.  
$f_2(\theta) = |1 - e^{i\theta} + e^{-2i\theta}|$.  
Using polar forms for $z^2$:  
$f_2^2(\theta) = (1-\cos\theta+\cos 2\theta)^2 + (\sin\theta - (-\sin 2\theta + \dots))^2$? No.  
Let's just calculate the modulus of complex number.  
$|a+ib|^2 = a^2+b^2$.  
Here $a = 1-\cos\theta+\cos 2\theta$.  
$b = -\sin\theta - (-\sin 2\theta) + \dots$?  
Let's check the imaginary part.  
The complex number is $z^2 - z + 1$. No, that's not it.  
Wait, the expression is $1 - z + z^2$.  
If we expand $|1-z+z^2|^2$:  
This is a sum of terms?  
$|a+ib|^2 = a^2+b^2$.  
The real part $a = 1-\cos\theta+\cos 2\theta$.  
The imaginary part $b = \sin\theta - \sin(2\theta)$? No.  
We know that $\text{Im}(-z+z^2) = \text{Im}(e^{-i\theta} + e^{-2i\theta})$? No, $-z$.  
$\text{Im}(-z) = -\sin\theta$.  
$\text{Im}(z^2) = \sin 2\theta$.  
So the imaginary part of $1-z+z^2$ is $\sin 2\theta - \sin\theta$?  
Let's check with values.  
If $z=e^{i\pi/4}$. $z=i\frac{\sqrt{2}}{2}$? No, $z=e^{i\pi/4} = \frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}$.  
$-z = -\frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}}$.  
$z^2 = e^{i\pi/2} = i$. No, $e^{-2i\theta}$ is $e^{-i\pi/2} = -i$? No.  
$-z+z^2$ at $\theta=\pi/4$:  
$-(\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}) + (-\frac{1}{\sqrt{2}} + \dots)$?  
Let's check $z=e^{i\pi/3}$? No.  
At $\theta=\pi$, $z=-1$.  
$\sin(2\pi)=0, \sin\pi=0$.  
Real part: $1-(-1)+(-1) = 1$. Imaginary: $0-0=0$.  
So $|1-z+z^2| = |1|=1$.  
If $z=-i$. $\theta=-\pi/2$.  
$z=-1/\sqrt{2} - i/\sqrt{2}$.  
Real part of $1-z+z^2$: $1 - (-1/\sqrt{2}+i/\sqrt{2}) + (-1) = 0.5/\dots$?  
This is tedious.  

Let's check the maximum of $|1-z+z^2|$ using polar form again.  
$|a+ib|^2 = a^2+b^2$.  
$a(\theta) = \cos\theta - i\sin\theta - 1 + \dots$? No.  
Let's just look at the geometry.  
The expression is sum of distances from origin to points on unit circle? No.  
It's sum of lengths of chords or something.  
Let's consider $f_2(z)$ as distance between $(z+1, z^2)$? No.  

Let's check if there are any known results for this type of problem.  
Maximize $|1+z|^2 + |1-z+z^2|^2$? Or sum of moduli?  
The maximum is likely at one of the points where terms align in magnitude.  
If we consider $\theta = -\pi/6$. No, just testing random values:  
$f_1 = \sqrt{4-1} = \sqrt{3}$? No. $f_1^2 = 2+2\cos(-\pi/6) = 2+2(\sqrt{3}/2) = 2+\sqrt{3}$. $f_1 \approx \sqrt{3.73} \approx 1.93$.  
$f_2 = |1 - z + z^2|$ at $\theta=-\pi/6$.  
$z = e^{-i\pi/6}$.  
$z = \frac{1}{2} - i\frac{\sqrt{3}}{6}$? No. $e^{i(-\pi/6)} = \cos(-30) + i\sin(-30) = \sqrt{3}/2 - i(1/2)$.  
$z^2 = e^{-i\pi/3}$.  
Real part of $1-z+z^2$: $1 - (\sqrt{3}/2-1) + (-1)$? No.  
Let's just evaluate: $|1-( \frac{\sqrt{3}}{2} - i\frac{1}{2}) + ( (\frac{\sqrt{3}}{2})^2 - i(-\frac{\sqrt{3}}{2} ) )|$? No.  
$z^2 = \cos( -60^\circ) + i\sin( -60^\circ)$? No, $e^{-i\pi/6}$.  
$z^2 = \frac{1}{2} - i\frac{\sqrt{3}}{6}$? No. $\cos(-30)=\sqrt{3}/2$, $\sin(-30)=-1/2$.  
So $z^2 = \frac{\sqrt{3}}{2} - i\frac{1}{2}$.  
Then $1-z+z^2 = 1 - (\frac{\sqrt{3}}{2}-i\frac{1}{2}) + (\frac{\sqrt{3}}{2}-i\frac{1}{2})$?  
$z^2$ is not $\frac{\sqrt{3}}{2}$. $e^{-i\pi/6}$ angle is $-30^\circ$.  
$\cos(-30) = \sqrt{3}/2$, $\sin(-30) = -1/2$.  
So $z^2 = \frac{\sqrt{3}}{2} - i\frac{1}{2}$.  
Real part sum: $1 - (\sqrt{3}/2 - 1/2) + (\sqrt{3}/2 - 1/2)$? No.  
$1 - z + z^2 = 1 - z + z^2$.  
Term 1: $1$. Term 2: $-z$. Term 3: $z^2$.  
Wait, $-z$ means subtract $e^{-i\pi/6}$.  
So $Re(1-z+z^2) = 1 - \cos(-30^\circ) + \cos(270^\circ)$? No.  
$\text{Re}(e^{i\theta}) = \cos\theta$. $\text{Im}(e^{i\theta}) = \sin\theta$.  
$z^2 = e^{-i\pi/3}$ angle is $-60^\circ$.  
$\cos(-60) = 1/2$. $\sin(-60) = -\sqrt{3}/2$.  
So $z^2 = 1/2 - i\sqrt{3}/2$.  
$Re(1-z+z^2) = 1 - \frac{\sqrt{3}}{2} + \frac{1}{2} = 3/2 - \frac{\sqrt{3}}{2} > 0$.  
$\text{Im}(1-z+z^2) = -\sin(-30^\circ) + (-\sin(-60^\circ))$?  
Term $-z$: $\text{Im}(-z) = -\sin(-30) = -(-1/2) = 1/2$.  
Term $z^2$: $\text{Im}(z^2) = \sin(-60) = -\sqrt{3}/2$.  
Sum: $1/2 + (-\sqrt{3}/2)$.  
So real part is positive, imaginary part negative.  
$|1-z+z^2|^2 = (3/2-\frac{\sqrt{3}}{2})^2 + (\frac{1}{2}-\frac{\sqrt{3}}{2})^2$.  
Let's calculate this value.  
$(3/2 - 0.866)^2 \approx (1.5-0.866)^2 = 0.634^2 \approx 0.4$.  
$(0.5 - 0.866)^2 \approx (-0.366)^2 \approx 0.134$.  
Sum $\approx 0.53$.  
This is much smaller than 3.  

Let's try to find the maximum of $f_2(z)$ over $\theta$ again.  
It seems to peak when $z=e^{i\pi} = -1$. Value is 3.  
Is it possible for $f_2$ to be larger?  
Consider $\theta$ such that terms align.  
Maybe at some angles we get something like $4$? No, max modulus of polynomial is bounded by sum of coeffs if no cancellation?  
But here we have modulus.  
Let's try a different substitution: $z = e^{i\phi}$.  
$f_2(\phi) = |1 - e^{i\phi} + e^{-2i\phi}|$.  
Notice that $(1-e^{i\phi}+e^{-2i\phi})(1-z+z^2)$? No.  
Is there a relation between $z$ and $\bar{z}$?  
Note that $z^3-1 = (z-1)(z^2+z+1)$.  
Maybe substitute $w=1-z$. Then $|w|^2 + |w-z| = |w|(1+\dots)$?  
Let's assume the maximum value is 3.  
Let's try to prove that for any $z$ on the unit circle, $f_1(z) \le 2$ and $|1-z+z^2| \le 2 + 2\sqrt{2}$? No.  

Let's reconsider $f_2$.  
We can write $1 - z + z^2 = (z-1)(z+1) - z$? No.  
Actually, $1 - z + z^2 = (1-z+z^2)$.  
Note that for any $\theta$, $|1-z+z^2|^2 = (1-\cos\theta+\cos 2\theta)^2 + (\sin(3\theta/2))^2$? No.  
Let's just evaluate numerically with a random point and check the trend.  
Points: $0, \pi/4, \pi/2, 2\pi/3, 5\pi/4, \dots$  
$\theta=0$: sum=3.  
$\theta=\pi/2$: sum=$\sqrt{2}+1 \approx 2.41$. (Using $f_2(\pi/2)=|1-i+i^2|=|-i|=1$, no $|1-z+z^2|$ with $z=i$. $1-i-1=0$. Sum $\sqrt{2}$.)  
$\theta=\pi$: sum=3.  
$\theta=-\pi/6$: approx 0.53.  
$\theta = -\pi/4$?  
Let's check $z=e^{-i\pi/6}$.  
Sum $\approx \sqrt{3} + |1-z+z^2|$. No, we are looking for $f_1+f_2$.  
$f_1(e^{-i\pi/6}) = \sqrt{2+2\cos(-\pi/6)} = \sqrt{2+\sqrt{3}}$. $\approx 2.9$.  
$f_2$ at $-\pi/6$: we calculated earlier roughly $|0.4 + \dots| \approx 0.53$.  
Sum $\approx 3.43$.  
Is this correct?  
Let's recheck the value for $f_1(e^{-i\pi/6})$.  
$z=e^{i(-\pi/6)} = e^{-i\pi/6} = \frac{1}{2} - i\frac{\sqrt{3}}{6}$? No. $\cos(-30)=\frac{\sqrt{3}}{2}$, $\sin(-30)=-\frac{1}{2}$.  
So $z = \frac{\sqrt{3}}{2} - i\frac{1}{2}$.  
Then $|1+z|^2 = (1+\cos(\theta))^2 + \sin^2(\theta)$ with $\theta=-30$.  
$= (1+\frac{\sqrt{3}}{2})^2 + (-1/2)^2 = 1 + \sqrt{3} + 3/4 + 1/4 = 2+\sqrt{3}$.  
So $|1+z| = \sqrt{2+\sqrt{3}} \approx \sqrt{3.73} \approx 1.93$.  
Now for $f_2$:  
$z^2 = e^{i(-60^\circ)}$. $\cos(-60)=\frac{\sqrt{3}}{2}$, $\sin=-\frac{1}{2}$.  
So $z^2 = \frac{\sqrt{3}}{2} - i\frac{1}{2}$.  
$|1-z+z^2|^2$:  
Real part: $1 - z + z^2$.  
Real part of $-z$ is $-\sin\theta = -(-1/2) = 1/2$.  
Real part of $z^2$ is $\cos(2\theta)$? No, $e^{i(-60)}$ angle is $3\pi  

## Answer

*(none: the token cap hit during thinking)*
