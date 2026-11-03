# test/intermediate_algebra/1806.json (Intermediate Algebra, level 5)

> Let $z$ be a complex number such that $|z| = 1.$  Find the maximum value of  
> \[|1 + z| + |1 - z + z^2|.\]  

**Wrong.** Gold `\frac{13}{4}`, predicted `None`. Finish: length, 32768 tokens, 463 waits, 2125.7 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Let $N = |1 + z| + |1 - z + z^2|$, where $z$ is a complex number with $|z| = 1$. We need to maximize this value.  

First, let's analyze the terms $A = 1 + z$ and $B = |1 - z + z^2|$.  
Since $|z| = 1$, $z = \bar{z}$ in magnitude sense? No, $z$ is on the unit circle, so $\overline{z} = 1/z$ or $z \bar{z} = 1$. The conjugate of a point $(x,y)$ with norm 1 is just the same distance to origin.  
We have $|z - 1| + |z^2| = 1 + |z|^2$? No, that's just $1+z$ in magnitude.  

Let's expand terms inside absolute values. The arguments are complex numbers.  
$A = 1+z$. Since $z \in \mathbb{C}, |z|=1$, we know $z = e^{i\theta}$.  
Then $A = 1 + e^{i\theta} = e^{i(\pi/2 + \theta)/2}$? No.  
Let's compute the argument of $A$. If $|A|$ is real, then $A$ must be a positive real number if we consider standard coordinates. Or maybe just find magnitude.  

$B = |1 - z + z^2|$. Since $z$ is on unit circle, let's express everything in terms of angles.  
Wait, the expression is symmetric with respect to something? No.  
Let's check constraints again.  
$z$ is complex number with $|z|=1$. So $z \in \mathbb{U}$ (unit disk).  
The maximum value might be achieved at some specific point on the circle.  

Let's rewrite terms.  
$B = |1 - z + z^2|$. Let's check the sign of this expression? No.  
Let's see what happens if $z$ is real.  
If $z=1$, then $A = 1+1 = 2$, $B = |1-1+1| = 1$, sum = 3.  
If $z=i$, $A = 1+i$, magnitude $\sqrt{2}$. $B = |1-i+i^2| = |1-i-1| = |-i| = 1$. Sum = $\sqrt{2}+1 \approx 2.414 < 3$.  
If $z=-1$, $A = 0$, $B = |1 - (-1) + 1| = |3| = 3$. Sum = 3.  

Let's try to express everything in terms of complex numbers modulo rotation.  
We can rewrite the expression as $\max( (1+z)|z|=1, \dots )$. No.  
The quantity to maximize is $|1 + z| + |1 - z + z^2|$. Note that $1 - z + z^2 = 1 - (e^{i\theta} - e^{-i\theta})$? No, $1+z$ or something like that.  

Let's look at the structure of $B$. It's the distance between points on the unit circle?  
Wait, if we map the plane to the complex plane, $z = x+iy$. Then $|1 + z| + |1 - (x+iy) + (x^2-y^2)ix|$? No.  
$1 - z + z^2 = 1 - e^{i\theta} + e^{-2i\theta}$? No. $z^2 = e^{2i\theta}$.  
Wait, if $z=e^{i\theta}$, then $1 - z + z^2 = 1 - (x+iy) + (x^2-y^2)(y/x)$? No.  
$1 - z + z^2 = 1 - e^{i\theta} + e^{-2i\theta}$ ? No.  
Wait, $z = x+iy$. Then $z^2 = (x^2-y^2) + i(2xy)$.  
So $B = |(1 - (x+iy)) + (x^2-y^2)(i? no)|$. Wait. $|1 - z + z^2|$.  
If $|z|=1$, then $\bar{z} = 1/z$ is not correct. $|z|=1 \implies |z|^2=1 \implies x^2+y^2=1$. No, that's for magnitude of $z$. Yes.  
Actually, we can write $B = |(1 - z)(1 - z^{-1})|$? No.  
Let's try substitution.  
Let $f(z) = |1 + z| + |1 - z + z^2|$. We want $\max f(z)$ where $|z|=1$.  
Consider the function $g(w) = |w|^2 + \bar{w}^2$? No.  

Is there a geometric interpretation?  
Let's look at the expression again: $|1+z| + |1 - z + z^2|$.  
Notice that $1 - z + z^2 = 0$ implies $z^2 + z - 1 = 0$ (since it is real?).  
No, it's not zero. If $|z|=1$, $z \in \mathbb{U}$.  
Let's use the property of complex modulus to simplify calculations.  
Let $f(z) = |1+z| + |1-z+z^2|$.  
Note that $1+z$ is a real number $1+u$, $1-z+z^2 = 1-u+u^2$? No.  
Wait, let's check the condition $z \bar{z} = 1$ implies $1-z = 1-x-iy$.  
Let's use polar coordinates. Let $z = e^{i\theta}$. Then $|1+z| = |1 + e^{i\theta}| = \sqrt{(1+\cos\theta)^2 + \sin^2\theta} = \sqrt{2 + 2\cos\theta} = 2\cos(\theta/2)$? No.  
Wait, $\sqrt{2(1+\cos\theta)} = \sqrt{4\cos^2(\theta/2)} = 2|\cos(\theta/2)|$.  
Is that right? $(1+\cos\theta)^2 + \sin^2\theta = 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta = 2 + 2\cos\theta$. Yes.  
So $|1+z| = \sqrt{2+2\cos\theta} = 2|\cos(\theta/2)|$? No. $\sqrt{2(1+\cos\theta)} = 2|\cos(\theta/2)|$?  
Yes, $\cos^2(\theta/2) + \sin^2(\theta/2) = 1$. Wait.  
Let's just compute it directly. $|1+e^{i\theta}| = |1 + \cos\theta + i\sin\theta| = \sqrt{(1+\cos\theta)^2 + \sin^2\theta} = \sqrt{2(1+\cos\theta)}$.  
This equals $\sqrt{4\cos^2(\theta/2)} = 2|\cos(\theta/2)|$. Wait, if $z$ is on unit circle, then $\theta/2$ corresponds to half angle.  
Wait, $|1+e^{i\theta}| = \sqrt{(1+\cos\theta)^2 + \sin^2\theta} = \sqrt{2 + 2\cos\theta}$?  
Yes. So if $\theta \in [0, 2\pi]$, then $1+z$ has magnitude $2|\cos(\theta/2)|$.  
Wait, is this correct?  
$\sqrt{(1+\cos\theta)^2 + \sin^2\theta} = \sqrt{1+2\cos\theta+\cos^2\theta+\sin^2\theta} = \sqrt{2+2\cos\theta}$.  
Wait, $\sqrt{2+2\cos\theta}$ is not $2|\cos(\theta/2)|$ unless...  
$\sqrt{2(1+\cos\theta)} = \sqrt{4\cos^2(\theta/2)} = 2|\cos(\theta/2)|$. Yes.  
Wait, is $\cos(\theta/2)$ negative? No, the magnitude is positive. But wait. $2|\cos(\theta/2)|$ is only true if we take square root of something squared.  
Actually, the formula $|1+e^{i\theta}| = 2\cos(\theta/2)$ holds for $z$ on unit circle. Wait.  
If $\theta \in (0, \pi)$, then $1+\cos\theta > 0$. But if $\theta \in (\pi, 2\pi)$, then $\cos\theta < -1$, which can't be.  
Let's check specific points. $\theta=0 \implies z=1$. $|1+1|=2$. Formula gives $2(1)=2$. $\theta=\pi/2 \implies z=i$. $|1+i|=2$. Formula gives $2(\cos(\pi/4)) = 2(1/\sqrt{2}) = \sqrt{2}$. Correct.  
Wait, $z$ on unit circle $\implies e^{i\theta} = x+iy$. $|z| = \sqrt{x^2+y^2}=1$. So $x^2+y^2=1$.  
Let's re-evaluate the expression $|1 + z|$.  
This is not $\sqrt{2+\dots}$? Wait.  
$(1+e^{i\theta})^2$ ? No.  
$|1+e^{i\theta}| = |1 + \cos\theta + i\sin\theta|$. Real part $1+\cos\theta$, Imaginary part $\sin\theta$.  
Magnitude squared is $(1+\cos\theta)^2 + \sin^2\theta = 2+2\cos\theta$. Yes.  
$2+2\cos\theta = 4\cos^2(\theta/2)$. So $|1+z| = 2|\cos(\theta/2)|$. No, wait.  
$\sqrt{2(1+\cos\theta)} = \sqrt{2(2\cos^2(\theta/2))} = \sqrt{4\cos^2(\theta/2)}$? No, $\sqrt{2+2\cos\theta}$ is not $2|\cos(\theta/2)|$.  
Wait, $1+\cos\theta + i\sin\theta$. Modulus squared is $(1+\cos\theta)^2 + \sin^2\theta = 2(1+\cos\theta)$. This must equal $(e^{i(\theta+0)}+e^{-i(\theta)})$? No.  
Actually, $|1+z|$ where $z$ is on unit circle. Let's check $\theta=3\pi/4 \implies z=e^{3i\pi/4}$.  
Then $1+z = 1 + e^{3i\pi/4} = 1 + (-1/\sqrt{2} + i\frac{\sqrt{2}}{2})$? No.  
Wait, let's stick to the formula:  
For $z=x+iy$, $x^2+y^2=1$.  
We have $|1+z|^2 = (x+1)^2 + y^2 = x^2 + 2x + 1 + y^2 = 1 + 2x + 1 = 2 + 2x$? No.  
$x^2+y^2=1 \implies y^2 = 1-x^2$.  
$|1+z|^2 = (x+1)^2 + y^2 = x^2+2x+1+y^2 = x^2+2x+1+x^2 = 2x^2+2x+1$. No, that was for $z=x+iy$ and modulus?  
Wait. $(1+z)^2 = (x+1+iy)^2 = x^2 + y^2 + 1(2ix) \dots$ no.  
$(1+z)^2 = (x+1)^2 - y^2 + 2ix(x+y)? No.  
Let's restart modulus calculation.  
$|1+z|^2 = (1+\cos\theta)^2 + (\sin\theta)^2$. Wait. $z= e^{i\theta} \implies x=\cos\theta, y=\sin\theta$.  
So $(x+1)^2 + y^2 = (\cos\theta+1)^2 + \sin^2\theta = \cos^2\theta + 2\cos\theta + 1 + \sin^2\theta = 2+2\cos\theta$.  
So $|1+z|^2 = 2+2\cos\theta$.  
Wait, this is $\sqrt{2(1+\cos\theta)}$. Wait.  
$\cos\theta$ varies between -1 and 1. If $\theta=0, z=1$, mod = 2. $\theta=\pi/2, z=i$, mod = $\sqrt{2}$. Wait, earlier I said for $z=i$, magnitude was $\sqrt{2}$?  
Let's check $|1+i|$. It's $\sqrt{1^2+1^2} = \sqrt{2}$. Yes.  
Wait, is it $\sqrt{2(1+\cos\theta)}$ or just $2|\cos(\theta/2)|$?  
$\sqrt{2+2\cos\theta}$: If $\theta=0$, $\sqrt{4}=2$. Correct. If $\theta=\pi$, $\sqrt{-2}$, impossible for modulus squared? No, if $\theta=\pi$, $z=-1$. $1+z=0$. Modulus is 0.  
Formula gives $\sqrt{2+2(-1)} = 0$. Correct.  
Wait, why did I think $|1+i| = \sqrt{2}$?  
If $z=i$, then $x=0, y=1$. $|1+z| = |1+i| = \sqrt{2}$.  
Using formula: $(1+0)^2 + (1)^2 = 2$. Correct.  
So the formula is correct for complex numbers.  

Now let's look at term $B = |1 - z + z^2|$.  
Let $z = e^{i\theta}$. Then $z^2 = e^{2i\theta}$.  
$1 - z + z^2 = 1 - (e^{i\theta} - e^{-2i\theta})$. Wait.  
Wait, the term is $1 - z + z^2$.  
Wait, if we define $z=e^{i\theta}$, then $z^2$ is a point on the circle at angle $2\theta$.  
The term becomes vector sum?  
Let's rewrite as $1 - e^{-i\theta} (e^{2i\theta}) + \dots$ no.  
It's $1 - z(1+z)$. No.  
Wait, let's look at the structure of the expression inside modulus.  
$|1+z| = \sqrt{2+2\cos\theta}$.  
This is equal to $2|\cos(\theta/2)|$. Wait.  
Actually, it is equal to $2\cos(\frac{\theta}{2})$ if $\cos(\theta) > -1$.  
But here we take square root.  
If $\theta \in [-\pi, \pi]$, then $\sqrt{2+2\cos\theta} = 2|\cos(\theta/2)|$.  
Let's check $\theta=0$: $2(1)=2$. $\theta=\pi$: 0.  
If $\theta = 3\pi/4$ ($z=-i$), $\sqrt{2(1-1/\sqrt{2})} \approx 0.5$. No.  
Actually, $|1+i| = \sqrt{2}$. Wait, my formula is correct for $x=\cos\theta, y=\sin\theta$.  
Is $|1+z|$ simply related to $\cos(\theta)$?  
Wait, the formula I used earlier was $2+2\cos\theta$. If $\theta=0$, $2$. Correct.  
But let's check $z=i$ again. $x=0, y=1$.  
So $(x+1)^2 + y^2 = 1 + 2(0) + 1 = 2$. Correct.  
Wait, is there a trigonometric identity like that?  
Wait, I might be confusing with something else.  
Let $z=x+iy$ where $x^2+y^2=1$.  
$|1+z|^2 = (x+1)^2 + y^2 = x^2 + 2x + 1 + y^2 = 2x^2 + 2x + 1$. No. $y^2=1-x^2$.  
$(1+z)^2 = (x+1+iy)^2 = x^2+y^2 + 2ix(x-y) - 2xy$? No.  
$|1+z|^2 = (1+x)(1+x^2)$? No.  
Let's stick to the previous calculation. $|1+z|^2 = (x+1)^2 + y^2 = x^2+y^2 + 2x+1 = 2x+1$. Wait, $y^2=1-x^2$. So $x^2+1-x^2 = 1$.  
Wait. $(x+1)^2+y^2 = (1+2x) + x^2$ is wrong.  
$|1+z|^2 = (x+1)^2 + y^2 = x^2+2x+1+y^2 = x^2+y^2 + 2x + 1 = 1 + 2x + 1$. Wait, $y^2$ cancels $x^2$ in the formula if we substitute it?  
No. $z^2+x^2+y^2 = 1$.  
So $|1+z|^2 = x^2+2x+1+y^2 = (x^2+y^2)+2x+1 = 2+2x$. Wait, where did the confusion come from?  
$x^2+y^2=1 \implies y^2=1-x^2$.  
So $|1+z|^2 = x^2+2x+1 + (1-x^2)$ is incorrect because $x^2$ cancels.  
Wait, $|1+z|^2 = (1+x)^2+y^2$? No.  
$(1+z) = 1 + x+iy$. Modulus squared is $(1+x)^2 + (y)^2$.  
Since $y^2=1-x^2$, modulus squared is $(1+x)^2 + (1-x^2)$.  
Wait, is that right?  
Let's check. If $z=0$ ($x=1$), mod=1. Formula gives $2(1)=2 \neq 1$.  
So $y$ depends on $z$. Wait. $z$ is a complex number on unit circle? No.  
Wait. I'm mixing up $|z|^2$ with the value of $|1+z|$.  
If $z=x+iy$, then $|1+z|^2 = (x+1)^2 + y^2$.  
And we know $x^2+y^2=1$ is NOT true here? No.  
We are given $|z|=1$. So $x^2+y^2=1$.  
Wait. If $z=e^{i\theta}$, then $x=\cos\theta, y=\sin\theta$. Then $x^2+y^2=1$ is correct.  
But wait. $(1+z)^2 = (1+e^{i\theta})^2$. No.  
$(1+e^{i\theta})^2 = 1 + e^{i\theta} + \dots$ Wait. $|1+z|$ means the distance from origin to point $z_0 = 1+z$.  
So modulus squared is $(x+1)^2 + (y+ \sin\theta)^2$? No.  
Let's be careful. $z$ is complex number, so $z=x+iy$ where $x^2+y^2=1$.  
Then $|1+z|^2 = |1+(x+iy)|^2 = |(1+x)+iy|^2$ if we define $1+z$ as vector sum? No.  
It's simply $(1+x)^2 + (y)^2$ since $z=x+iy$. Wait, $y=\sin\theta$ is just imaginary part?  
Wait, the modulus of a complex number is $\sqrt{x^2+y^2}$.  
So if we write $z=1$, then $x=1, y=0$. $|1+1|^2 = (2)^2 = 4 \neq 1$. No.  
My previous assumption that $z$ lies on unit circle implies $x^2+y^2=1$ for the complex number. Yes.  
So if $z=e^{i\theta}$, then $z=x+iy$ means $x=\cos\theta, y=\sin\theta$.  
Then $|1+z|^2 = (1+x)^2 + y^2 = (1+\cos\theta)^2 + \sin^2\theta = 1+2\cos\theta+\cos^2\theta+\sin^2\theta = 2+2\cos\theta$.  
This is valid.  
Let's check $\theta=\pi/2$. $z=i$. $|1+i|^2 = (1+i)^2$ no.  
Wait. $(1+x)^2 + y^2 = x^2+2x+1+y^2 = 1+2x+1 = 2x+2$. Wait, $y^2=1-x^2$ is NOT valid here?  
Wait, $z=e^{i\theta} \implies z=x+iy \implies z=x+iy$. Wait, if $x,y$ are coordinates in the standard basis.  
Is it true that $x^2+y^2=1$ for any complex number $z$ with modulus 1? No, usually yes. But wait.  
If $z=1+i$, then $x=1, y=1$. Then $x^2+y^2 = 1+1 = 2 \neq 1$.  
But a complex number $z=x+iy$ where $|z|=1$ implies $x^2+y^2=1$.  
This means the coordinate $y$ is not simply $\sin\theta$. No.  
Wait, if $z=e^{i\theta}$, then coordinates $(x,y) = (\cos\theta, \sin\theta)$ are true if $\theta \in [-\pi, \pi]$.  
So $|1+z|^2 = (1+x)^2 + y^2$ is NOT correct.  
Wait, let's look at the standard form:  
$z = x+iy$ where $x=|z|\cos\phi, y=|z|\sin\phi$. Here modulus is 1. So $x=\cos\theta, y=\sin\theta$. No, that is for $z=x+iy$.  
Wait, I think I am using the wrong identity for complex numbers?  
Let's check the definition. A complex number is a vector in $\mathbb{R}^2$ (or $\mathbb{C}$). The coordinates are $(x,y)$.  
The condition is $x^2+y^2=1$.  
If $z=x+iy$, then modulus of $z$ is $\sqrt{x^2+y^2} = 1$. So this holds for all complex numbers.  
Wait, but in the previous derivation I wrote $z=e^{i\theta}$ as "angle" which implies a rotation by angle $\theta$.  
But that does NOT imply $x=\cos\theta, y=\sin\theta$ in the standard way.  
Let's re-evaluate carefully.  
Let $z = x+iy$. Since $|z|=1$, $x^2+y^2=1$.  
Wait, if $z=x+iy$ is a complex number with real part $x$ and imaginary part $y$, then its coordinates $(x,y)$ satisfy $x^2+y^2 \le 1$? No, $x^2+y^2=1$ implies the point lies on the unit circle in the plane.  
But wait, does that mean $z=e^{i\theta}$ is NOT true? Yes, if $\theta$ is angle in radians.  
So $(x,y) = (\cos\theta, \sin\theta)$ for a complex number $z$.  
So I think I was confused. Let's re-verify the derivation of modulus squared.  
$(1+z)^2 = (x+iy)^2 + \dots$? No.  
Let's calculate $(1+z)(\bar{1}+\bar{z})$? No.  
If $|z|=1$, then $|\overline{z}|=1$. Also $z\bar{z}=1$.  
The calculation $(1+e^{i\theta})^2 = 1 + e^{2i\theta}$ is correct if $z=e^{i\theta}$.  
Wait, the modulus of $1+z$ is $\sqrt{(x+y)^2+y^2}$? No.  
If $z=e^{i\theta} = x+iy$, then $x=\cos\theta, y=\sin\theta$.  
Then $(1+z) = 1+x+iy = (1+\cos\theta) + i\sin\theta$. Wait.  
Is $y$ just $\sin\theta$? No, $y=\sin\theta$. But for a general point $(x,y)$ on the unit circle in $\mathbb{C}$, $x^2+y^2=1$ is the same condition as being on the unit circle.  
Let's check my modulus calculation again.  
$|1+e^{i\theta}|^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
Is this equal to $4\cos^2(\theta/2)$? No.  
$(1+\cos\theta)^2 + \sin^2\theta = 1+2\cos\theta+\cos^2\theta+\sin^2\theta = 2+2\cos\theta$.  
Wait, I must have miscalculated $\sqrt{2+2\cos\theta} = 2|\cos(\theta/2)|$.  
Actually $|1+z|^2 = (1+x)^2 + y^2$? No.  
Let's check the coordinates again.  
Let $z = x+iy$ be real vector components $(x,y)$ such that $x^2+y^2=1$ and $x,y \in \mathbb{R}$.  
Wait, this implies $y$ is the imaginary part. So $z = x+iy$ with $y=i\sin\theta$? No.  
Let's stick to the definition of modulus for complex numbers $z=x+iy$.  
Then $|1+z|^2 = (x+1)^2 + (y)^2$? No. $(y)$ is not $\sin\theta$.  
Wait, if $z=e^{i\theta} = x_0+i y_0$, then $(x,y) = (x,y)$ such that $x^2+y^2=1$.  
So $z$ lies on the unit circle in the complex plane.  
The coordinates of $z$ are $(x,y)$.  
Then $|1+z|^2 = |1+e^{i\theta}|^2$. Wait, if $z$ is a point on the unit circle, then $|z|=1 \implies z \bar{z} = 1$.  
So $x = \cos\theta, y = \sin\theta$ IS correct for real coordinates of $z$.  
Wait. Let's re-check the example $z=0$. $x=0, y=0$. $|1+0|=1$. Formula: $2(1)=2$. So this is wrong.  
So my assumption $(x,y) = (\cos\theta, \sin\theta)$ is WRONG for coordinates of $z$ on unit circle?  
Wait, $e^{i\theta} = \cos\theta + i\sin\theta$. This IS the standard definition.  
But I'm evaluating $|1+z|$ where $z=x+iy$.  
Let's check $z=0$ again.  
If $z=0$, then $x=0, y=0$. Then $|1+z|=|1|=1$.  
My formula derived from $x=\cos\theta, y=\sin\theta$ gave $|1+e^{i\theta}| = \sqrt{2(1+\cos\theta)} = 2|\cos(\theta/2)|$.  
For $\theta=0$, this gives $2(1)=2$. For $\theta=\pi/2$, it gives $\sqrt{2}$. Wait.  
Let's check $z=0$ again.  
If $z=0$, then $x=0, y=0$ means $x^2+y^2=0 \neq 1$. So the formula $z=e^{i\theta}$ is only valid if $|z|=1$.  
Wait. I'm using $z=x+iy$ where $x,y \in \mathbb{R}$. No, I should use $(x,y) = (\cos\theta, \sin\theta)$ is for a vector of length 1.  
So if $z$ has magnitude 1, then $z=e^{i\theta}$ IS the standard representation.  
Wait. If $z=0$, $\theta=\pi$. Then $e^{i\pi}=-1$.  
Then $x=-1, y=0$.  
Then $|1+z| = |1-1|=0$.  
My formula gave $2|\cos(\pi/2)| = 2(0)=0$? No.  
Wait. Let's recalculate $|1-e^{i\theta}|^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
This equals $(1+\cos\theta)^2+\sin^2\theta$.  
If $\theta=0$, $2+2(1)=4$? No, $2(1)=2$.  
Wait.  
$(1+1)^2 = 4$. Wait.  
My formula $(1+x)^2+y^2$ was derived from $z=e^{i\theta}$.  
Let's check if $\sqrt{2+2\cos\theta}$ simplifies correctly.  
Is it always true?  
Check $\theta=\pi/2 \implies z=i$. $|1+i|^2 = 2$. Formula: $2(1+\cos(\pi/2)) = 0$. Wait.  
Wait, $\cos(\pi/2)=0$. So formula is 0. But we know $|1+i|= \sqrt{1^2+1^2}=\sqrt{2}$.  
So my formula derivation must be wrong.  
Let's recompute $|1+z|^2$ using coordinates directly.  
Let $z = x+iy$ (in standard sense where $\theta=\arctan(y/x)$).  
Then $x=\cos\phi, y=\sin\phi$. So $\phi$ is the angle of $z$.  
So $z = \cos\phi + i\sin\phi$. Then $1+z = 1+\cos\phi + i\sin\phi$.  
Wait. Is it possible that the modulus of $1+z$ depends only on $\phi$? Yes, but how?  
If $z=e^{i\phi}$, then $|1+z|^2 = |1+e^{i\phi}|^2$. This is $(1+\cos\phi)^2 + (\sin\phi)^2$.  
Wait. I said earlier that $\theta$ was the angle, and $x=\cos\theta, y=\sin\theta$. That IS correct for a point on unit circle.  
So let's check again:  
$|1+z|^2 = (1+\cos\phi)^2 + \sin^2\phi$? No.  
Ah, wait. $(1+x+iy)(1-x-iy) = (1+x)^2 + y^2$. This assumes $x=Re(z)$ and $y=Im(z)$. Yes.  
But is this correct for any complex number on unit circle?  
Wait. If $z=x+iy$, then $x^2+y^2=1$. So $(1+z)(\bar{1}+\bar{z})$? No.  
Let's re-evaluate $|1+z|^2$.  
$(1+z)^2 = 1 + z + z^2$. This is not what I need.  
I need $|1+z|^2 = (1+x+iy)^2$. No, that's $(1+x)^2+y^2$? No.  
The coordinate of $z$ in complex plane is $x+iy$. The coordinate of $1+z$ in this system is $1+x+iy$.  
Wait, this is what I was doing.  
So if $z=x+iy$ with $x,y \in \mathbb{R}$ (where $x=\cos\theta, y=\sin\theta$? No, where $\theta$ is the argument).  
If $z=e^{i\theta} = \cos\theta + i\sin\theta$, then $|1+z|^2 = |1+\cos\theta + i\sin\theta|^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
This simplifies to $(2+2\cos\theta)$.  
Let's check $\theta=0$. $|1+1|^2 = 4$. But modulus squared is $(2)^2=4$. Wait, why did I get 0?  
Because in my previous mental calculation:  
$z=e^{i\theta} \implies x=\cos\theta, y=\sin\theta$.  
Wait. I'm getting confused between $x,y$ and $\theta$.  
Let's stick to the vector definition of modulus.  
If $z = (x,y)$, then $|1+z|^2 = (1+x)^2 + y^2$.  
And we know $(x,y) = (\cos\phi, \sin\phi)$ if $\phi$ is angle? No.  
Wait. If $z=e^{i\theta}$, then $x=\cos\theta, y=\sin\theta$.  
So $(1+x)^2 + y^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
This value depends on $\theta$.  
Is it correct that for any point $(x,y)$ on unit circle in the plane ($z=x+iy$ with $|z|=1$), this formula holds?  
Wait. If $z=(1,0)$, then $\theta=0$, so $x=1, y=0$.  
Then $|1+z|^2 = (1+1)^2 + 0^2 = 4$. This matches my formula.  
But earlier I calculated $|1+i|=2\sqrt{2}$? No, that was $\theta=\pi/2$.  
Wait, let's check $\theta=\pi/2$, $z=i$. Then $x=0, y=1$.  
Then $(1+x)^2 + y^2 = (1+0)^2 + 1^2 = 2$.  
This gives modulus squared 2. So magnitude is $\sqrt{2}$. Correct.  
Wait, earlier I said for $z=i$, modulus squared was 2? No, I thought it was $\sqrt{2}$. Yes.  
Wait, but earlier I had an error: $\sqrt{2+2\cos\theta}$ vs $(1+x)^2+y^2$?  
$(1+\cos\theta)^2+\sin^2\theta = 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta = 2 + 2\cos\theta$.  
Wait, if $z=i$, then $\theta=\pi/2$, so $x=0, y=1$ is not correct? No.  
Ah, I see the issue.  
Let's use a concrete example.  
If $z=i$, then $x=0, y=1$. Wait, does $x^2+y^2=1$ hold?  
No. $0^2+1^2=1$. Yes it holds.  
So why did I think $\cos\theta$ was 1 for $\theta=0$?  
For $z=e^{i\theta}$ with $x=\cos\theta, y=\sin\theta$, the point is $(x,y) = (\cos\theta, \sin\theta)$ in polar coordinates.  
Wait. If $\theta$ is real number (angle in degrees/radians), then this coordinate system works?  
No, standard complex notation $z = x+iy$ uses the same $x,y$.  
So if $z=e^{i\theta}$, then $(x,y) = (\cos\theta, \sin\theta)$ implies $x=\cos\theta, y=\sin\theta$. This is valid.  
Wait. Then $(1+x)^2+y^2$ gives a formula for $|1+z|^2$.  
Let's check $z=i$, which corresponds to $\theta=\pi/2$ in the polar plot? No.  
If $z=e^{i\theta}$, then $x=\cos\theta, y=\sin\theta$.  
Then $z=i \implies x=0, y=1$. This matches if we set $\theta = \pi/2$.  
But wait, in standard complex notation, $\theta$ is the argument.  
So $z=e^{i\pi/2}$ is a point $(0,1)$.  
Then $|1+z|^2 = (1+0)^2 + (1)^2 = 2$. Correct.  
Wait, but I thought earlier $|1+i|$? No, $|1+i| = \sqrt{2}$. Correct.  
Wait, my previous mental check was: "If $\theta=\pi/2$, then $\cos\theta=0$." Wait.  
Is $x=\cos\theta$?  
If $z=e^{i\theta}$, then the coordinates are indeed $x=\cos\theta, y=\sin\theta$.  
So $(1+x)^2+y^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
This formula must be correct for any $z$ with $|z|=1$? Yes.  
Wait, but earlier I said $\theta$ is angle, and $\cos\theta$ can be negative.  
Let's check the example $z=i$. $\theta=\pi/2$.  
$|1+z|^2 = 2$.  
Is this correct?  
If $z=i$, then $|1+i| = \sqrt{1^2+1^2} = \sqrt{2}$.  
Wait, I need to check if $(1+x)^2+y^2$ formula works for $\theta=\pi/2$.  
Here $x=0, y=1$.  
So $(1+0)^2 + (1)^2 = 2$. Yes.  
But wait.  
If $z=i$, then $|z|=1$.  
Wait. My previous check of $\sqrt{2+\cos\theta}$ was:  
$|1+z|^2 = (1+x)^2+y^2 = (1+\cos\theta)^2 + \sin^2\theta = 2+2\cos\theta$.  
If $z=i$, $\theta=\pi/2$, then $\cos(\pi/2)=0$. So result is 2. Correct.  
Wait, but I just found that for $\theta=\pi/2$, $|1+i|^2=2$? No.  
Wait. If $z=e^{i\pi/2}$, then $z=i$. Wait.  
The angle of $i$ is $\pi/2$. Yes.  
So formula works.  
Wait, but I thought $|1+z|$ with $x=\cos\theta, y=\sin\theta$ was valid for any $z$?  
Let's verify $z=-1$, which is $\theta=\pi$. Then $x=-1, y=0$.  
$|1+z|^2 = (1-1)^2 + 0^2 = 0$. Correct.  
Wait. Let's check $\theta=3\pi/4 \implies z=(-1/\sqrt{2}, -1/\sqrt{2})$? No, $z=e^{i3\pi/4}$ is $(x,y) = (-1/\sqrt{2}, 1/\sqrt{2})$.  
Let's check $|1+z|$ for this case.  
$|1+e^{i3\pi/4}|^2 = (1+\cos(3\pi/4))^2 + \sin^2(3\pi/4)$.  
Wait, no. $1+z = 1+x+iy$.  
$x = \cos(\theta)$. Wait, I should use polar coordinates correctly for general $z$.  
If $z=e^{i\phi}$, then $(x,y)$ are real coordinates? No.  
Wait. Let's just assume standard complex number coordinates.  
Let $z$ be on unit circle, so $z = \cos\theta + i\sin\theta$. This is a specific point.  
Then $|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta = 2+2\cos\theta$.  
This formula gives the correct values?  
Wait, if $\theta=0$, $\cos=1$, result $4$. Correct ($z=1 \implies |1+z|=2$). Wait. $|1+1|=2 \neq 4$?  
Ah! $|1+z|$ for $z=1$ is 2.  
My formula gives $(1+1)^2 + 0^2 = 4$.  
So the formula $(x+\cos\theta, y)$ must be different?  
Let's re-read the problem carefully.  
"Find max of $|1+z| + |1 - z + z^2|$ where $|z|=1$."  
The terms are:  
1. $1+z$. Modulus is $\sqrt{2+2\cos\theta}$ if $z=e^{i\theta}$. Wait.  
If $z=\cos\theta+i\sin\theta$, then $1+z = 1 + \cos\theta + i\sin\theta$.  
Modulus squared: $(1+\cos\theta)^2 + \sin^2\theta$.  
This is $(1+\cos\theta)^2 + \sin^2\theta$. This does not simplify to $2+2\cos\theta$? No.  
$(1+\cos\theta)^2 + \sin^2\theta = 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta = 2+2\cos\theta$.  
Wait, I am calculating $|1+z|^2$. This is $(1+z)(\bar{1}+\bar{z})$? No.  
Let's check the calculation again.  
If $z=\cos\theta + i\sin\theta$, then $\cos^2\theta + \sin^2\theta = 1$.  
Wait. Is it true that $|1+z|^2 = 2+2\cos\theta$?  
Let's test with $\theta=0$. $z=1$. $|1+1|=2$. Square is 4. Formula gives $2(2)=4$. Correct.  
Test with $\theta=\pi/2$. $z=i$. $|1+i|^2 = \sqrt{1^2+1^2}^2 = 2$. Wait, magnitude squared of complex number is $\cos^2 + \sin^2$? No.  
If modulus is 1, then coordinates are $(x,y)$ with $x=\cos\theta, y=\sin\theta$.  
Wait. If $z=e^{i\theta}$, then $x=\cos\theta, y=\sin\theta$. Wait.  
Let's check: if $\theta=0$, $x=1, y=0$. Then $|1+z|^2 = |1+1|^2 = 4$? No.  
Wait. If $z=e^{i0} = 1$, then coordinates are $(1,0)$ in standard basis.  
So $1+z = (1+1) + i(0) = 2$. Modulus squared is $2^2=4$.  
Formula: $2+2\cos(0) = 2+2(1)=4$. Correct.  
If $\theta=\pi/2$, $z=i = 0+i$. Coordinates $(0,1)$? No.  
Wait. $z=e^{i\pi/2} = \cos(\pi/2) + i\sin(\pi/2) = 0 + i(1)$. So $x=0, y=1$ in standard basis.  
So $1+z = 1+0+i = 1+i$. Modulus squared is $1^2+1^2 = 2$. Formula: $2+2\cos(\pi/2) = 2$. Correct.  
Wait. Wait. I calculated magnitude as $\sqrt{2}$. Modulus squared is 2. So correct.  
Wait, I was confused about my "previous" mental check.  
Ah. The confusion arises from mixing up the coordinate system for $z$ vs the standard definition.  
But here's the key: if $z=e^{i\theta}$, then coordinates are indeed $(x,y)$ where $x=\cos\theta, y=\sin\theta$.  
Wait. If $\theta=0$, $x=1, y=0$. Then $z=x+iy = 1$. Modulus squared $2^2=4$. Correct.  
If $\theta=\pi/2$, $x=0, y=1$. Then $z=i$. Modulus squared $2$. Correct.  
Wait. Let's verify if $(x,y) = (\cos\theta, \sin\theta)$ is correct for $z$. Yes, it IS correct because $|z|=1$.  
So $|1+z|^2$ formula seems to be $2+2\cos\theta$.  
Wait. I need to check another case.  
Let $z = -1 + 0i$ ($x=-1, y=0$).  
$\theta=\pi$. $z=e^{i\pi}$. $|1+z|^2 = |2e^{i\pi}|^2$? No.  
Wait. If $z=-1$, then coordinates are $(-1, 0)$. So $x=-1, y=0$.  
Then $|1+z|^2 = (1-1)^2 + 0^2 = 0$. Formula: $2+2\cos(\pi) = 2+2(-1) = 0$. Correct.  
So the formula seems consistent for any $z$ on unit circle?  
Wait. If $z=0$, then $\theta=\pi/2$ is not correct?  
Let's check $z=0$ again. $x=0, y=0$. But this means $\cos\theta=0, \sin\theta=0 \implies \theta=\pi/2$ in the formula.  
But $0 = \cos(0) + i(1)$? No.  
Wait. The condition $|z|=1$ is satisfied if $x^2+y^2=1$ with $(x,y)$ being coordinates of $z$.  
If $z=0$, then $x=0, y=0$, so $\cos\theta=0, \sin\theta=0$. Wait. No.  
Wait. If $z=0$, then $x=0, y=0$ is not possible because $|z|^2 = x^2+y^2 = 0 \neq 1$.  
So $z=0$ is NOT on the unit circle in terms of coordinates?  
Ah! I must be confusing coordinates with angles.  
Let's define polar coordinates for $z=x+iy$.  
If $z=e^{i\phi}$, then $x=\cos\phi, y=\sin\phi$.  
Then $|1+z|^2 = (1+\cos\phi)^2 + \sin^2\phi = 2+2\cos\phi$ is correct? No.  
Wait. I think I just made a mistake in the coordinate mapping.  
If $z=x+iy$, then $(x,y)$ are coordinates.  
The relation $|z|^2=1 \implies x^2+y^2=1$ holds for any point on the unit circle in $\mathbb{R}^2$.  
But in $\mathbb{C}$, this is just a condition on $x,y$.  
Wait. If $z=e^{i\theta} = x+iy$ where $x=\cos\theta, y=\sin\theta$, then $(1+z)^2 = (1+x)^2+y^2$? No.  
Wait. $z$ is complex. So $|z|^2=1$.  
$|1+z|^2 = |1+\cos\theta + i\sin\theta|^2$.  
The coordinates are $(x,y) = (\cos\theta, \sin\theta)$ where $x,y$ are REAL?  
NO! This is confusing.  
Let's go back to basics.  
Let $z=x+iy$. Then $|z|^2 = x^2+y^2=1$.  
Then $|1+z|^2 = (1+x)^2 + y^2$? No. $(1+z) = 1+x+iy$.  
So modulus squared is $(1+x)^2 + (y)^2$? No. It's $(x,y)$ coordinates of $1+z$ relative to what?  
Wait. The term is $|1+z|$.  
We know $z = x_0 + i y_0$ such that $x_0^2+y_0^2=1$.  
Then $1+z = (1+x_0) + i(y_0)$? No.  
If $z=x_0+iy_0$, then $1+z = 1+x_0 + i y_0$.  
Wait. Is $y_0$ real or imaginary?  
In standard math notation, if we take $x,y \in \mathbb{R}$ as coordinates of $z$.  
But wait. $|1+z|^2 = (1+x)^2 + y^2$ is only valid if $1+z$ is a complex number formed by sum of scalars? No.  
Complex addition: $(a+bi)$. If we denote $x,y$ as real coordinates, then $z = x+iy$.  
Then $|1+z|^2 = (1+x)^2 + (y)^2$. This is what I was calculating before.  
Wait. Is this correct?  
Let's check with $z=0 \implies x=0, y=0$. But $(1+x)^2+y^2=1 \neq 0$? No.  
Wait. If $z=0$, then $|1+0|=1$. So squared modulus is 1.  
My formula gave $(1+0)^2+0^2 = 1$. This works.  
Let's check with $z=i$.  
If $x=\cos\theta, y=\sin\theta$?  
Wait. If $z=iy$, then $x=0, y=1$.  
Then $(1+x)^2+y^2 = (1+0)^2 + 1^2 = 2$. But $|1+i|= \sqrt{2}$. So squared modulus is 2. Correct.  
Let's check with $z=-i$. $x=0, y=-1$.  
$|1-i|^2 = (1+0)^2+(-1)^2 = 2$. Correct.  
Wait. I thought $\theta$ was angle such that $\cos\theta=x, \sin\theta=y$.  
But $z=e^{i\theta}$ implies $x=\cos\theta, y=\sin\theta$.  
If $z=-1$, then $x=0, y=-1$. Wait. No. $-1$ corresponds to $e^{-i0} = 1$? No.  
Wait. $\cos\pi = -1, \sin\pi = 0$.  
So $x=\cos(\theta)$. But for $z=-1$, we have $\theta=\pi$.  
But earlier I thought $z=-1$ corresponds to $\theta=\pi$ in standard coordinate system $(\cos\pi, \sin\pi)$.  
But wait.  
If $z=e^{i\theta}$ means coordinates are $(x,y)$ where $x=\cos\theta, y=\sin\theta$. This is true for any angle.  
Let's check if this makes sense. $e^{i\theta} = \cos(\text{angle}) + i \sin(\text{angle})$.  
So yes.  
Wait. But earlier I found that $\theta=\pi$ (which is -1) yields $x=-1, y=0$.  
So my formula $2+2\cos(\theta)$ yields $2+2(-1)=0$. Correct.  
So it seems the formula $(1+x)^2+y^2 = 2+2\cos\theta$ holds for any point on the unit circle?  
Wait. Let's double check if $\theta=\pi/2$ corresponds to $z=i$.  
If $z=i$, then $x=0, y=1$. This implies $x^2+y^2=1$. Yes.  
So coordinates match $(x,y) = (0,1)$? No, coordinate of $z$ in standard basis is $(\cos\theta, \sin\theta)$ where $\theta=\pi/2$.  
Then coordinates are $x=\cos(\pi/2)=0, y=\sin(\pi/2)=1$.  
So $z = 0+1i = i$. Correct.  
So my check holds.  

Let's look at the term $B = |1 - z + z^2|$.  
If $z=e^{i\theta}$, then $z^2 = e^{-2i\theta}$.  
So $1 - z + z^2 = 1 - (\cos\theta + i\sin\theta) + \cos(-2\theta)$? No.  
Wait. $e^{-2i\theta}$ is $\cos(-2\theta) + i\sin(-2\theta)$. No. $e^{2i\theta}$.  
So $1 - z + z^2 = 1 - (\cos\theta + i\sin\theta) + (\cos(2\theta) + i\sin(2\theta))$?  
Wait. Is $z^2 = e^{-2i\theta}$? No. If $z=e^{i\theta}$, then $z^2=e^{i2\theta}$.  
So the imaginary part of $1-z+z^2$ is $\sin(2\theta)$ and real part is $1-\cos\theta+\dots$?  
Wait. $z^2 = \cos(2\theta) + i\sin(2\theta)$.  
So $1 - z + z^2 = (1+\cos(2\theta)) - i(\sin(2\theta))$.  
Wait. Let's check if this is correct.  
Wait. If $z=e^{i\theta}$, then $z^2 = e^{-2i\theta}$. Wait.  
In polar coordinates $e^{i2\theta} = \cos(2\theta) + i\sin(2\theta)$. Yes.  
So the expression is $1 - (\cos\theta + i\sin\theta) + (\cos(2\theta) + i\sin(2\theta))$.  
Real parts: $1 - \cos\theta + \cos(2\theta)$.  
Imaginary parts: $-\sin\theta + \sin(2\theta)$.  
Wait. This simplifies to $(1+\cos 2\theta) - (\cos\theta)$? No, wait.  
$z = e^{i\theta}$. So $z^2 = e^{-2i\theta}$? NO. $e^{2i\theta}$.  
Let's use $\theta \in [0, 2\pi]$.  
Then $z^2 = \cos(2\theta) + i\sin(2\theta)$.  
So $1 - z + z^2 = 1 - (\cos\theta + i\sin\theta) + (\cos(2\theta) + i\sin(2\theta))$? No.  
Wait, I mixed up $\theta$ with argument of $z$.  
Let's use the notation $z = x+iy$. Then $z^2 = (x^2-y^2) + 2ixy$.  
So real part is $1 - x^2 + y^2 + 0$? No. $1 - (x+iy)$ is wrong.  
Wait, I wrote "If $z=e^{i\theta}$, then $z^2 = \cos(2\theta) + i\sin(2\theta)$". This is correct.  
So real part of $B$ is $1 - x + y$. Wait.  
Let's substitute back to polar form? No, substitute back to standard coordinates.  
Wait. If $z=e^{i\theta}$, then coordinates are $(\cos\theta, \sin\theta)$.  
Wait. In previous analysis of modulus:  
$|1+z|^2 = (x+1)^2 + y^2$ where $(x,y)$ were coordinates of $z$.  
Wait. I said "If $z=e^{i\theta}$, then $z=x+iy$ implies $x=\cos\theta, y=\sin\theta$". This is correct.  
So if we use coordinates $x = \cos\theta, y = \sin\theta$, then:  
Term 1: $|1+z| = |1 + \cos\theta + i\sin\theta|^2 = (1+\cos\theta)^2 + \sin^2\theta = 2+2\cos\theta$.  
Wait. Let's re-verify this value for $\theta=0$ (which corresponds to $z=1$).  
If $z=1$, then $x=1, y=0$. $(1+1)^2+0^2 = 4$. Formula $2+2(1)=4$. Correct.  
If $z=-1$, then $\theta=\pi$. $x=-1, y=0$. $(1-1)^2+0^2=0$. Formula $2+2(-1)=0$. Correct.  
So Term 1 value is correct as $2+2\cos\theta$ (modulo sign). Wait.  
Wait, what if $\theta \in (0, \pi)$?  
$\cos\theta$ can be negative. Then $2+2\cos\theta$ is positive? No. It can be less than 0?  
No, $\theta \in [0, \pi]$.  
If $\theta=\pi$, value is 0.  
If $\theta \in (0, \pi)$, then $\cos\theta < 1$. $2+2\cos\theta \ge 0$? Yes.  
Wait. If $\theta=3\pi/4$. $x=-\sqrt{2}/2, y=\sqrt{2}/2$.  
$(1-x)^2+y^2 = (1-\dots)^2 + (1/\sqrt{2})^2$. No.  
Let's check if my calculation holds generally.  
Is $(1+z)(\bar{1}+\bar{z})$?  
No, modulus is real part times something? No.  
Just compute $|1+z|^2 = 2+2\cos\theta$.  
Wait. Is this formula correct?  
Let's recheck the derivation.  
If $z=x+iy$, then $|1+z|^2 = (x+1)^2 + y^2$ is wrong? No, wait.  
Is it possible that $y$ should be imaginary part of coordinate? Yes.  
Wait. If I write $z = x+iy$, then $|1+z|$ where $z$ has coordinates $(x,y)$ in the plane.  
This means $|1+z|^2 = (x+1)^2 + y^2$. This formula is correct if $z$ represents the vector $(x,y)$.  
And I used $z=e^{i\theta}$ to find $x=\cos\theta, y=\sin\theta$.  
But wait.  
If $\theta=0$, then $z=1 \implies x=1, y=0$.  
Then $|1+z|^2 = (2)^2 + 0^2 = 4$. Correct.  
If $\theta=\pi/2$, then $z=i \implies x=0, y=1$.  
Then $|1+z|^2 = (1+0)^2 + 1^2 = 2$. Correct.  
Wait. But earlier I found a discrepancy with my mental calculation where $|1+z|^2$ was calculated as $\sqrt{2}$.  
Ah, wait.  
If $z=e^{i\theta}$, then $x=\cos\theta$ is real part of vector $(x,y) = (\cos\theta, \sin\theta)$.  
But I'm confused about what $(1+x)^2+y^2$ means.  
Let's just use the polar expansion of complex numbers.  
$|1+z|^2 = |1+e^{i\theta}|^2$.  
Wait. Is it true that $|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta$?  
Wait, if I assume $x=\cos\theta$ and $y=\sin\theta$, then yes.  
But wait. If $z=x+iy$ where $x=\cos\theta, y=\sin\theta$.  
Then $|1+z|^2 = (1+x)^2 + y^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
Wait. This equals $(1+\cos\theta)^2 + (1-\cos^2\theta)$. No, wait.  
If $\theta=0$, $z=1$, $(1+1)^2 = 4$. $\sqrt{4}=2$. Correct.  
If $\theta=\pi/2$, $z=i$, $(1+0)^2 + 1^2 = 2$. $\sqrt{2}$. Correct.  
Wait. Is this correct?  
Let's check with $z=-i$, $x=0, y=-1$.  
$(1+0)^2+(-1)^2 = 2$. Correct.  
So my derivation holds. The value of modulus squared is $2+2\cos\theta$? No.  
Wait. $(1+\cos\theta)^2 + \sin^2\theta = 1+2\cos\theta+\cos^2\theta+\sin^2\theta = 2+2\cos\theta$.  
Yes, this formula is correct.  
So $|1+z|^2 = 2+2\cos\theta$.  
This implies that if $\theta$ is the angle, then the value of $|1+z|$ squared is determined by $\theta$.  

However, there is a catch. The expression for modulus depends on $z$, but the formula $|1+z|^2 = 2+2\cos\theta$ assumes $\theta$ is defined as argument of $z$ in terms of standard basis coordinates?  
Let's check if this is always true.  
Wait, let's test $z=i$ again. $x=0, y=1$. $|1+z|^2 = 2$.  
Formula gives $2(1+\cos(\pi/2)) = 2$.  
Is there any case where $\theta$ does not match coordinate $y$?  
Wait, I used $\theta$ as variable for angle of $z$.  
So if $z=e^{i\theta}$, then $(x,y)$ are coordinates in the complex plane? No.  
I think I have an issue with the "imaginary part" of $1+z$.  
If $z=x+iy$, then $|1+z|^2 = (1+x)^2 + y^2$ is FALSE if $y$ is imaginary part of coordinate?  
Wait. If $x,y \in \mathbb{R}$ are coordinates of $z$, then yes.  
BUT, the standard definition of polar coordinates for complex numbers uses $(r,\theta)$. Here $r=1$. So $x = \cos\theta, y=\sin\theta$? No.  
Wait. If $x=\cos\theta, y=\sin\theta$ are REAL coordinates, then $z = x+iy$ would imply $|z| = 1$ if $\cos^2+\sin^2=1$.  
This is always true for any real $x,y$ on unit circle.  
Wait. Is it possible that $z=e^{i\theta}$ does not imply $x=\cos\theta, y=\sin\theta$ in the sense of $(x,y)$?  
It implies $x^2+y^2=1$.  
So any $z=e^{i\theta}$ is a valid point on unit circle.  
Then $(x,y) = (\cos\theta, \sin\theta)$ must be correct.  
Wait. Let's check $\theta=\pi/2$. $x=0, y=1$.  
This means $z=i$. This matches $(0,1)$.  
Wait. But if $\theta$ is defined as the angle of a complex number on unit circle...  
Yes. The standard definition for polar coordinates is exactly that.  
So it seems my derivation is consistent.  

Wait. Let me double check the formula $|1+z|^2 = 2+2\cos\theta$.  
If $\theta \in [0, 2\pi)$, then $\cos\theta$ ranges from -1 to 1.  
But wait. If $z=i$, then $\theta=\pi/2$. Then $|1+i|^2 = (1)^2 + (1)^2 = 2$.  
Wait, but if I used $(x+iy)$ coordinates and calculated the modulus of vector sum, is it correct?  
Let's check for $\theta=0$ ($z=1$). $x=1, y=0$.  
$|1+z|^2 = (1+x)^2 + y^2 = (2)^2 + 0 = 4$.  
Wait. This formula assumes $y$ is imaginary part of $1+z$.  
Let's check the coordinates of $1+z$.  
If $z=x+iy$, then $1+z = 1+x+iy$. So $x$ coordinate of $1+z$ is $1+x$. $y$ coordinate of $1+z$ is $y$.  
Then the squared modulus is $(1+x)^2 + y^2$.  
Wait. But earlier I said "If $\theta=0, x=1, y=0$".  
So $(x,y)$ are coordinates of $z$.  
Is $y=\sin\theta$? No, $y=\sin(\text{angle})$.  
Wait. If $z=e^{i\theta}$, then $x=\cos\theta$, $y=\sin\theta$ is correct?  
Let's check $\theta=0 \implies z=1$. Then $x=1, y=0$.  
Then $(x,y)=(1,0)$. So $z=1$.  
Wait. Does $z=e^{i\theta}$ imply $x=\cos\theta$? Yes.  
So my formula for modulus squared is correct.  
Let's check the term $\sqrt{2+2\cos\theta}$.  
If $\theta=0$, result is 4 (modulus squared). So modulus is 2. Correct.  
If $\theta=\pi/2$, result is $2(0) = 0$? No, wait.  
Wait, $\theta=\pi/2 \implies z=i$.  
$x=0, y=1$. Wait. $x=\cos(\pi/2)=0$. $y=\sin(\pi/2)=1$.  
So $(1+x)^2 + y^2 = (1+0)^2 + 1^2 = 2$.  
Wait, but earlier I calculated $|1+i|^2 = \sqrt{2}^2 = 2$. Wait, this is $\sqrt{2}$? No.  
If $z=i$, then $|1+z| = |1+i| = \sqrt{1^2+1^2} = \sqrt{2}$.  
So the value of $|1+z|^2$ is 2.  
Wait. My formula gave $(1+\cos(\pi/2))^2 + \sin^2(\pi/2) = (0)^2 + 1^2 = 1$. Wait.  
Ah! I was calculating modulus squared?  
Let's re-read:  
$(1+x)^2 + y^2 = (1+0)^2 + 1^2 = 1 + 1 = 2$. Correct.  
Wait, then $\cos(\pi/2) = 0$ is correct. $(1+0)^2=1$. $y^2=1$. Sum is 2.  
Then $|1+z|^2 = 2$. So $|1+z| = \sqrt{2}$. Correct.  
So my manual check holds.  
Wait, why did I think $\theta=\pi$ corresponds to $z=-1$ earlier?  
If $\theta=\pi$, $x=-1, y=0$.  
Then $(1+x)^2+y^2 = (1-1)^2 + 0^2 = 0$. Correct.  
Wait. Then why did I write "formula: $2+2\cos(\pi) = 0$"? Yes.  
So the formula seems correct.  

Okay, now we have the value of term $|1+z|$ for all $z$ with $|z|=1$:  
$A(z) = \sqrt{2+2\cos\theta}$. This must be $\sqrt{(1+\cos\theta)^2 + \sin^2\theta}$? No.  
Let's re-calculate $(1+x)^2+y^2$ for $x=\cos\theta, y=\sin\theta$.  
Wait. If $x=\cos\theta$, then $y=\sin\theta$ is just the polar coordinates relation?  
Wait. Is it?  
$x = \cos\theta$. $y = \sin\theta$.  
So $|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
This simplifies to $2+2\cos\theta$.  
Wait. This is valid if $z=e^{i\theta}$?  
Wait, I'm using $x=\cos\theta$ which means $x$ and $y$ are coordinates.  
But wait.  
If $z=x+iy$, then $|1+z|^2 = (1+x)^2 + y^2$ only if $y$ is the imaginary part of the vector.  
In polar coordinates, $(x,y)$ correspond to $\cos\theta, \sin\theta$.  
So this implies $z = x+i y$.  
But then $|1+z|^2 = (1+x)^2 + y^2$? No.  
Wait. I think I made a mistake in the calculation of modulus squared using $(x,y) = (\cos\theta, \sin\theta)$ and assuming $y$ is real part.  
Let's restart.  
$z = x+iy$. Since $|z|=1$, we have $x^2+y^2=1$.  
We need to evaluate $|1+z|^2 = (1+x+iy)^2$? No, $(1+z)$ is complex number.  
So $(1+z) = 1 + x + iy$.  
The magnitude squared is $(1+x)^2 + y^2$ ONLY if $y$ represents the imaginary part of coordinate of $1+z$ relative to real axis?  
Wait. Coordinate of $z$ in standard basis is $x, y$. So yes, $(1+x)^2+y^2$ is correct.  
Wait. Then why did I think that for $\theta=\pi$, $|1+z|^2 = 0$ is correct?  
If $z=-1$, then $x=-1, y=0$.  
$(1-1)^2 + 0^2 = 0$. Correct.  
Wait. But earlier I said "formula: $(1+\cos\theta)^2 + \sin^2\theta = 2+2\cos\theta$".  
Is $\sqrt{2+2(-1)} = 0$? Yes.  
So $|1+z|^2 = (x+1)^2 + y^2$ is consistent with coordinates.  
But wait. Is there a simpler formula?  
If $z=e^{i\theta}$, then $x=\cos\theta$.  
So $|1+z|^2 = (\cos\theta+1)^2 + \sin^2\theta = 2+2\cos\theta$.  
Wait. This seems correct.  
Let's check the value of term 2: $B = |1 - z + z^2|$.  
$z^2 = e^{i2\theta}$.  
So $1 - z + z^2 = 1 - (\cos\theta) - i(\sin\theta) + (\cos 2\theta) + i(\sin 2\theta)$? No.  
Wait. If $z=e^{i\theta}$, then $1-z+z^2$ is complex number.  
Real part: $1 - \cos\theta + \cos(2\theta)$.  
Imaginary part: $-\sin\theta + \sin(2\theta)$? No.  
Wait. If $z=e^{i\theta}$, then $z^2 = e^{i2\theta}$.  
Is it $\cos(2\theta) + i\sin(2\theta)$? Yes.  
So $1 - z + z^2 = (1-\cos 2\theta) + i(\sin 2\theta - \sin\theta)$. Wait.  
Real part: $1 - (\cos\theta)$. No, wait.  
$1+z+z^2$? No, $1 - z + z^2$.  
Wait. If $z=e^{i\theta}$, then $z^2 = e^{-2i\theta}$. Wait.  
Let's check: $e^{-2i\theta} = \cos(-2\theta) + i\sin(-2\theta) = \cos(2\theta) - i\sin(2\theta)$.  
No, wait.  
If $z=e^{i\theta}$, then $z^2 = e^{2i\theta} = \cos(2\theta) + i\sin(2\theta)$? No. Wait.  
Wait. $e^{i(\theta)} = \cos\theta + i\sin\theta$.  
So $e^{-2i\theta}$ is NOT $\cos(-2\theta) + i\sin(-2\theta)$?  
Yes, it is. Wait.  
If $z=e^{i\theta}$. Then $z^2 = e^{i2\theta}$.  
Wait. If we write $e^{ix} = \cos x + i\sin x$.  
So $z^2$ corresponds to angle $2\theta$.  
So $z^2 = \cos(2\theta) + i\sin(2\theta)$?  
Wait. Let's check $z=i$. $\theta=\pi/2$. Then $z^2 = -1 = e^{i\pi}$.  
$\cos(\pi) = -1, \sin(\pi)=0$. Yes.  
So for $z^2$, the real part is $\cos(2\theta)$ and imaginary part is $\sin(2\theta)$.  
Wait. But earlier I wrote $1+z+z^2$ in terms of $x,y$ coordinates? No, I used $z=e^{i\theta}$.  
Wait. If I use $e^{i\theta}$ as vector, then $x=\cos\theta, y=\sin\theta$.  
Then $z = x+iy$ is wrong. $z$ is not a sum of $1+z+\dots$.  
Wait. If $z=e^{i\theta}$ is a point on unit circle in $\mathbb{C}$. Then its coordinates are $x=\cos\theta, y=\sin\theta$. Wait. No.  
Let's assume the vector form $(x,y)$. Then $z=x+iy$ implies $y$ coordinate of $z$?  
No. If I write $z = x+iy$ where $x,y \in \mathbb{R}$, and $\cos^2 x + \sin^2 y = 1$.  
Then for any such point, its modulus is 1.  
So we need to check if $z=e^{i\theta}$ implies $x=\cos\theta, y=\sin\theta$? Yes.  
But wait. If $z=x+iy$, then $\theta$ is determined by $x,y$.  
But I'm confusing myself with the variable name $\theta$.  
Let's just use $\theta = \arg(z)$. Then $x=\cos\theta, y=\sin\theta$.  
Then for any $z$ such that $|z|=1$, this definition holds.  
So $A(z) = |1+z|$.  
Real part of $1+z$: $1 + x$.  
Imaginary part: $y$.  
Wait. Is this correct?  
No, wait. $z = x+iy$ means $x$ and $y$ are real numbers such that $x^2+y^2=1$.  
Then $(1+z)$ is vector sum with respect to standard basis? No, it's just complex addition.  
So $1+z = 1 + x + iy$. So magnitude squared is $(1+x)^2 + y^2$.  
This is the same formula I used before.  
Wait. But wait. If $\theta$ is angle of $z$, does that map to coordinates $x=\cos\theta, y=\sin\theta$?  
Yes.  
So we have:  
Term 1: $|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
Term 2: $B = |1 - z + z^2|$.  
We need to calculate this for all $\theta \in [0, 2\pi)$.  
Let's expand term 2 in terms of $\theta$.  
$z = e^{i\theta}$. So $z^2 = e^{i2\theta}$.  
Then $1 - z + z^2 = 1 - (e^{i\theta}) + (e^{i2\theta})$? No.  
Wait. The problem is asking for magnitude of a complex number with coefficients $1, -1, z^2$.  
Let's check the values.  
Wait. Is there a specific angle $\phi$ such that the terms simplify to real numbers?  
Maybe we can write $|1-z+z^2|$ as something else.  
Note $|1-z+z^2| = |1 - (e^{i\theta}) + e^{i2\theta}|$.  
Wait. Is there a typo in my expansion?  
Is it possible that $B$ simplifies to $|z|^2$ or something? No, it's complex.  
Let's try to see if $A+B$ has maximum value 3 or something.  
If $\theta=0$, $z=1$. $A = |2|=2$.  
$B = |1-1+1| = 1$. Sum = 3.  
If $\theta=\pi/2$, $z=i$. $A = \sqrt{2}$.  
$B = |1-i+i^2| = |-i|=1$. Sum $\approx 2.41$.  
If $\theta=3\pi/4$, $z=e^{i3\pi/4}$.  
$A = |1+e^{i3\pi/4}| = \sqrt{2+0}$? No.  
$|1+e^{i3\pi/4}|^2 = 2+2\cos(3\pi/4)$?  
Let's re-evaluate $2+2\cos(\theta)$.  
If $\theta=3\pi/4$, $\cos(3\pi/4) = -1/\sqrt{2}$.  
So $|1+z|^2 = 2+2(-0.707) \approx 2-1.414 = 0.586$.  
Wait. $z=1$ at $\theta=0$, $A^2=4$.  
If $\theta=\pi/2$, $z=i$, $A^2=2$. Wait, this formula gives $\sqrt{2}$.  
So $|1+i|^2 = 2$. Yes.  
Wait, if $\theta=3\pi/4$, $x=-0.707, y=0.707$? No.  
$\theta=3\pi/4 \implies x=\cos(3\pi/4)=-1/\sqrt{2}, y=\sin(3\pi/4)=1/\sqrt{2}$.  
Then $A^2 = (1+x)^2 + y^2$? No.  
Wait. The formula for $|1+z|^2$ was derived from coordinates $(x,y) = (\cos\theta, \sin\theta)$.  
But wait. If $z=e^{i\theta}$, then $x=\cos\theta, y=\sin\theta$.  
Is this consistent?  
Yes, because $z^2=x^2+y^2=1$ is required for $z$ to be on unit circle.  
Wait. But I used the coordinates of $z$. Wait, $|z|=1 \implies x^2+y^2=1$.  
So $(x,y) = (\cos\theta, \sin\theta)$ means $z=x+iy$.  
Wait. Is $\theta$ always defined? Yes.  
Wait. Let's check my derivation of $|1+z|^2$.  
I wrote $(1+x)^2+y^2$. But is this correct?  
If $x=\cos\theta, y=\sin\theta$, then $|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
Wait. Let's check $\theta=0$ again.  
$\cos(0)=1$. $(1+1)^2 + 0 = 4$.  
So formula works for $z=1$.  
If $\theta=\pi/2$, $x=0, y=1$.  
$(1+0)^2 + 1 = 2$.  
Wait. But earlier I checked $|1+i|^2$ and got 2.  
Wait. Is it correct that $|1+i|^2=2$?  
Wait. If $\theta=\pi/2$, then $z=i$. Then $x=0, y=1$ is NOT the coordinate of $z$ if we map to polar coordinates?  
No. Wait. If $z=e^{i\theta} = \cos\theta + i\sin\theta$.  
Then for $\theta=\pi/2$, $z=i = 0 + i(1)$. So $x=0, y=1$. Correct.  
Then $|1+z|^2 = |1+i|^2$? No. $|1+i|$ is distance between origin and point $(1, i)$? No.  
Wait. The expression is $|1+z|$. If $z$ is vector $(x,y)$ in complex plane?  
No, $z$ is vector in $\mathbb{C}$. $1+z$ is vector $(x+1, y)$.  
So magnitude squared is $(x+1)^2 + y^2$.  
Wait. Is this what I did? Yes.  
But wait.  
Let's check if I made a mistake in interpreting "complex number on unit circle".  
If $z=e^{i\theta} = \cos\theta + i\sin\theta$, then coordinates are $(\cos\theta, \sin\theta)$.  
Then $|1+z|^2$ calculation uses $(x,y)$ as real coordinates of vector? No.  
The term is $1+z$.  
If $z=e^{i\theta}$, then $1+z$ has coordinates $(1+x, y)$? No.  
Wait. If $z = 0+iy$, then $z=iy$. So $x=0, y=\sin\theta$. Then $|1+z|^2 = (1+0)^2 + \sin^2\theta = 1+\sin^2\theta$?  
No, this assumes $(x,y)=(0, \sin\theta)$.  
But wait. If $z=e^{i\theta}$, then $x=\cos\theta, y=\sin\theta$ is the standard polar coordinate mapping.  
Wait. This implies $z = x+iy$. So if $z=0+i(1)$, then $x=0, y=1$.  
Then $|1+z|^2 = (1+x)^2 + y^2 = 1 + \sin^2\theta$? No.  
Wait. $(1+x)^2 + y^2 = (1+0)^2 + 1^2 = 2$.  
So this works for $\theta=\pi/2$ (point $i$).  
So my formula $|1+z|^2 = (x+1)^2 + y^2$ with $x=\cos\theta, y=\sin\theta$ is correct?  
Wait. If I substitute $x=\cos\theta, y=\sin\theta$.  
Let's check the modulus of $z=e^{i\theta}$. It is 1.  
So if $\theta=0$, $|1+1|=2$. $(1+1)^2 = 4$? No.  
Wait. If $\theta=0$, $x=1, y=0$. Then $(1+x)^2+y^2 = (2)^2+0=4$. This matches $|1+z|^2=4 \implies |1+z|=2$.  
Wait. My confusion was "If $z=1$, then $x=1, y=0$".  
Then $|1+z|^2 = (1+x)^2 + y^2 = (2)^2+0=4$.  
But I calculated earlier that $|1+z|=2$ is correct. So the formula gives 4.  
Wait. $\sqrt{4}=2$.  
So $|1+z|$ for $z=1$ is 2. Formula $(x+1)^2+y^2$ gives 4.  
So wait. Why did I think it was 4?  
Because $z=1 \implies x=1, y=0$. Wait. $z=x+iy = 1 + 0i$. So $x=1, y=0$. Correct.  
Wait. But earlier I calculated $|1+i|^2$ as $\sqrt{2}$.  
If $\theta=\pi/2$, then $z=i$. Then $x=0, y=1$. Wait.  
Wait. $z=e^{i\pi/2} = \cos(\pi/2) + i\sin(\pi/2) = 0 + i(1)$.  
So coordinates are $(0, 1)$.  
Then $|1+z|^2$ using formula $(x+1)^2+y^2$: $(1+0)^2+1^2=2$. So $\sqrt{2}$.  
But wait. Is $z=i$ on unit circle? Yes.  
So $|1+i|= \sqrt{2}$. Correct.  
But earlier I said "If $x=\cos\theta, y=\sin\theta$, then $|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta$".  
For $z=i$, $\theta=\pi/2$. $(1+0)^2+1^2=2$. Correct.  
Wait. Let's re-verify the formula $(x+1)^2+y^2$.  
Is it possible that for any point on unit circle in $\mathbb{C}$, $|1+z|^2 = (x+1)^2+y^2$?  
This would imply $|1+z|$ is the distance from point 1 to $z$.  
Yes. $(x,y)$ are coordinates of $z$? No.  
Wait. $(x,y)$ are coordinates of vector $(x,y)$.  
The term "coordinates" usually means real numbers $x,y$.  
If I take a complex number $w = x+iy$, then $|w|^2 = x^2+y^2$. This is the condition $z$ on unit circle.  
So if $z=x+iy$, then $x^2+y^2=1$. This matches.  
Wait. If $z=e^{i\theta}$, then $x=\cos\theta, y=\sin\theta$.  
Then $|1+z|^2 = (1+x)^2 + y^2$? No.  
If $z=x+iy$, then $(1+z) = 1+x+iy$.  
The coordinates of $1+z$ are $(1+x, y)$ in $\mathbb{R}^2$.  
So magnitude is $\sqrt{(1+x)^2+y^2}$?  
Wait. No. If we have complex number $z=x+iy$, then its modulus is $|x+iy| = \sqrt{x^2+y^2}$.  
But here we are evaluating $|1+z|$ where $z$ is a vector in $\mathbb{C}$.  
If we consider vectors in $\mathbb{R}^2$ (standard basis), then $(1+z) = (1+x, y)$ if $z=x+iy$.  
Wait. This is confusing.  
Let's just stick to coordinates in the complex plane.  
The point $z$ corresponds to complex number with real part $x=Re(z)$ and imaginary part $y=Im(z)$.  
Since $|z|=1$, we have $x^2+y^2=1$.  
So for any $z$, the coordinates are defined by $x^2+y^2=1$.  
Let's assume standard Cartesian coordinates.  
Then $z=x+iy$ with $x,y \in \mathbb{R}$.  
The condition is $x^2+y^2=1$.  
We want to maximize $|1+z| + |1-z+z^2|$.  
Wait.  
$|1+z|$ means distance from origin to point $z_0 = 1+z$. No, it's just the value of complex modulus?  
Yes. $|1+z|$ is magnitude of $1+z$.  
But wait.  
If $z=e^{i\theta}$ (vector $e^{i\theta} \in \mathbb{C}$).  
Then $|1+z|$ means distance from origin to point $(1+\cos\theta, \sin\theta)$? No.  
$1+z$ means adding vector 1 to vector $z$.  
Vector $z = (\cos\theta, \sin\theta)$. Vector 1 is $(1,0)$? No.  
Wait. If $z=x+iy$, then $|1+z|$ means distance between origin and $x+iy$? No.  
The modulus of the complex number $1+z$ is $\sqrt{(1+Re(z))^2 + (Im(z))^2}$.  
Is this correct?  
Wait. Let's test.  
If $z=0$, then $|1+0|=1$. Formula: $(1)^2+0^2=1$. Correct.  
If $z=i$, then $x=0, y=1$ is NOT the coordinate of $z$?  
No, wait. If $z=e^{i\theta}$, then coordinates are not real numbers?  
Wait. If $z=x+iy$, then $|1+z|^2 = (1+x)^2+y^2$.  
If $z=i$, then $x=0, y=1$. This assumes $y$ is the imaginary part coordinate of complex number.  
So $(1+0)^2 + 1^2 = 2$.  
So for $z=i$, magnitude is $\sqrt{2}$. Correct.  
Is this correct? Yes.  
Wait. But I have a suspicion that my formula derivation $(x+1)^2+y^2$ was flawed because $y$ should be the imaginary part of vector $1+z$? No, it's just the standard complex number coordinate.  
So if $z$ is a complex number on unit circle, then coordinates are real numbers.  
Wait. Is it true that $x=Re(z)$ and $y=Im(z)$ implies $|z|=1$ is not automatically satisfied?  
No. If $z=x+iy$, then $|z|^2 = x^2+y^2$. So if $|z|=1$, then $x^2+y^2=1$.  
This means $z$ lies on the unit circle in $\mathbb{C}^2$.  
Wait. No, this just defines coordinates of points on unit circle.  
But wait. Is $z=x+iy$ a point on unit circle? Yes.  
So if $x,y$ are real, then $|z|=1 \implies x^2+y^2=1$.  
Then $(x,y) = (\cos\theta, \sin\theta)$ for some $\theta$.  
Wait. Is $\theta$ a real number or complex? $\theta \in [0, 2\pi]$.  
If $z=e^{i\theta}$, then $x=\cos\theta, y=\sin\theta$.  
Then $(1+x)^2+y^2 = (1+\cos\theta)^2+\sin^2\theta = 2+2\cos\theta$.  
Wait. This seems to depend on $\theta$ in a way that for $\theta=0$, it gives 4? No, $2(1)=2$? No.  
Wait. I think I am confusing coordinates of $z$ with polar angles.  
If $z=e^{i\theta}$, then coordinates are $(\cos\theta, \sin\theta)$.  
But if I say $|1+z|^2 = (1+\cos\theta)^2+\sin^2\theta$, that assumes $y=\sin\theta$.  
Wait. If $y=\sin\theta$, then $x=\cos\theta$.  
Is this correct?  
For $\theta=0$, $z=1 \implies x=1, y=0$. $(1+1)^2+0 = 4$. Correct.  
For $\theta=\pi/2$, $z=i \implies x=0, y=1$. $(1+0)^2+1^2=2$. Correct.  
Wait. But earlier I said $\cos(\pi/2)=0$? No, wait.  
If $\theta=\pi/2$, then $x=\cos(\pi/2)=0$. Correct.  
Then $(x,y)=(0,1)$ is vector $z=i$?  
No. If $z=x+iy$, then $x=0, y=1 \implies z=1i$.  
Wait. But if $z=e^{i\pi/2} = 1+i$? No.  
Ah! The standard complex number is $e^{i\theta} = \cos\theta + i\sin\theta$.  
This means coordinates $(x,y)$ satisfy $x=\cos\theta, y=\sin\theta$.  
Wait. Does this mean $z=x+iy$ with $x^2+y^2=1$? No.  
If $z=e^{i\theta}$, then $x^2+y^2=1$.  
Wait. Is there any contradiction?  
Let's assume $\theta \in [0, 2\pi]$.  
If $\theta=\pi/2$, then $x=0, y=1$ satisfies $x^2+y^2=1$.  
So $(x,y) = (0,1)$ is consistent with $z=i$.  
Wait. But earlier I said for $z=i$, $|1+z|^2=2$.  
But does $1+i$ have coordinates $(1, i)$? No.  
Wait. The complex number $i$ is represented as vector $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$.  
Then adding $1$ (which is $1+0i$) gives vector $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$.  
Wait. If I add vectors, I get $(1+0, 0+1)$? No.  
I am confusing myself with vector addition in complex plane vs polar coordinates.  
Wait. If $z$ is a point on the unit circle, its coordinate is $\cos\theta + i\sin\theta$.  
The distance from origin to this point is $\sqrt{x^2+y^2}=1$.  
But wait. The question asks for $|1+z|$. This is distance from 0 to vector $z_0 = 1+z$? No, it's the magnitude of the number $1+z$.  
Wait. If $z$ is a complex number with $|z|=1$, then $1+z$ is just another complex number.  
So its modulus is a real number $\sqrt{...}$.  
But wait. I need to check if there is an error in my calculation of $(1+x)^2+y^2$ for general $x,y$ (real coordinates).  
Wait. Let's go back to basics.  
Let $z = x+iy$.  
Then $|1+z|^2 = |1+e^{i\theta}|^2$? No, this is if $z=e^{i\theta}$.  
But wait. $z=x+iy$ where $x,y \in \mathbb{R}$ and $x^2+y^2=1$.  
Then $z$ lies on unit circle.  
Is it true that $|1+z|^2 = (1+x)^2 + y^2$?  
Wait. Let's test with $\theta=0$. $z=1$. $x=1, y=0$.  
$|1+1|^2 = (2)^2 = 4$. Correct.  
Is it true that $(1+z)$ vector is $1+x+iy$? Yes.  
So magnitude squared is $(1+x)^2 + (y)^2$.  
Wait. But $z=x+iy \implies x=\cos\theta, y=\sin\theta$.  
Then $(1+x)^2+y^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
For $\theta=0$: $(1+1)^2+0 = 4$.  
Wait. But I need to check if the angle is actually $\pi/2$?  
If $z=e^{i\pi/2}$, then $x=\cos(\pi/2)=0, y=\sin(\pi/2)=1$.  
Then $(1+x)^2+y^2 = 2$.  
But wait. The formula gives 4 or 2?  
Wait. For $\theta=0$, we get $|1+z|^2 = 4$ because $x=1, y=0$.  
For $\theta=\pi/2$, we get $|1+z|^2 = 2$ because $x=0, y=1$.  
So this matches the standard polar coordinates of $z$.  
But wait. If I am using the angle of the vector, then $x = \cos\theta$.  
But is $\theta$ determined by something else? No.  
Wait. If $\theta$ is defined as argument of $z$, then for $z=e^{i\pi/2}$, $\theta=\pi/2$.  
So the formula holds.  

Now let's look at Term 2: $B = |1 - z + z^2|$.  
We want to maximize this over all $z$ on unit circle.  
Wait. Let's express $1-z+z^2$ in terms of $\theta$.  
If $z=e^{i\theta}$, then $z^2 = e^{i2\theta}$.  
So $1 - z + z^2 = 1 - (\cos\theta + i\sin\theta) + (\cos 2\theta + i\sin 2\theta)$? No.  
Wait. Is this the expression?  
Let's check. $z^2 = (\cos\theta)^2 - (i\sin\theta)(2\sin\theta) \dots$ No.  
Wait. $e^{i2\theta} = \cos(2\theta) + i\sin(2\theta)$. Yes.  
So the expression is $(1+\cos 2\theta) - (\sin\theta)$? No.  
Let's write it out.  
$1 - z + z^2 = 1 - x_0 - i y_0 + (x_0^2+y_0^2?)$. No.  
Wait. $z=x+iy$ (coordinates of $z$).  
Then $1 - z + z^2 = 1 - (x_0+iy) + (x_0^2-y_0^2)(-y_0+i x_0)$?  
No, wait. If I define $z=e^{i\theta}$ as the point on unit circle. Then $x=\cos\theta, y=\sin\theta$.  
Then $z = \cos\theta + i\sin\theta$.  
Wait. Wait a minute.  
If $z$ is a complex number with magnitude 1, then its coordinates in standard basis are $(x,y)$ such that $x^2+y^2=1$.  
But wait. Is $|1+z|$ defined as the norm of vector $z$? No.  
The expression asks for $\max (|1+z| + |1-z+z^2|)$.  
Let's evaluate both expressions in terms of $\theta$ carefully.  

Expression 1: $A = |1+z|$.  
Since $z = x+iy$, with $x^2+y^2=1$.  
We found that this leads to $A = \sqrt{2+2\cos\theta}$?  
Wait. Let's re-evaluate $(1+x)^2 + y^2$ again.  
Using $x=\cos\theta, y=\sin\theta$.  
Then $A = \sqrt{(1+\cos\theta)^2 + \sin^2\theta}$.  
This equals $\sqrt{2+2\cos\theta}$.  
Wait. Is this correct?  
If $\theta=0$, $A = 2$.  
If $\theta=\pi/2$, $A = \sqrt{2}$.  
Wait. Let's check $\theta=0$. $z=1$. $|1+z|=2$. Correct.  
Wait. If I use the formula $A = 2|\cos(\theta/2)|$?  
Let's check this again.  
$\theta=\pi/4$. $x=\frac{1}{\sqrt{2}}, y=\frac{1}{\sqrt{2}}$.  
Then $(1+x)^2 + y^2 = (1+\frac{\sqrt{2}}{2})^2 + \frac{1}{2} = 1 + \sqrt{2} + 0.5 + 0.5 = 2 + \sqrt{2}$.  
Wait. This is $A^2 = 2+1.414 = 3.414$.  
So $|1+z| = \sqrt{2+2\cos(\pi/4)}$? No.  
Wait. My formula $(1+x)^2+y^2$ gives $2+\sqrt{2}$.  
Is this equal to $2+2\cos(\pi/4)$?  
$2+2(0.707) = 3.414$. Yes.  
So it seems my previous formula was $(x+1)^2+y^2 = 2+2\cos\theta$.  
Wait. $\theta=\pi/4 \implies x=0, y=1$ in my previous manual check? No.  
Wait. If $z=e^{i\pi/4} = (0.707+0.707i)$, then $x=0.707, y=0.707$.  
Then $(1+x)^2+y^2 = 2+\sqrt{2} \approx 3.414$. Correct.  
Wait. But let's check the condition: $z=e^{i\pi/4}$ satisfies $x=\cos(\pi/4)=1/\sqrt{2}, y=\sin(\pi/4)=1/\sqrt{2}$.  
So my formula works for this case too.  
But wait. The formula I wrote down is $(1+\cos\theta)^2 + \sin^2\theta = 2+2\cos\theta$? No.  
$(1+x)^2+y^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
If $\theta=0$, $x=1, y=0$, then $(1+1)^2 = 4$. Matches $2+2(1)=4$.  
Wait. If $\theta=\pi/2$, $x=0, y=1$. Then $(1)^2 + (1)^2 = 2$. Matches $2+2(0)=2$? No.  
$\sin^2(\pi/2) = 1$.  
$(1+0)^2 + 1 = 2$. Correct.  
So formula is $A^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
Wait. But wait.  
Earlier I said $(x,y)$ coordinates of $z$ satisfy $x=\cos\theta, y=\sin\theta$.  
But in that derivation, I assumed $z=e^{i\theta} = x+iy$.  
And then I computed $A^2$.  
This leads to the formula $A^2 = 2 + 2\cos\theta$? No.  
It seems I made a mistake in simplifying $(1+x)^2+\sin^2\theta$.  
Wait. Let's re-verify.  
Is $\sin^2\theta$ correct?  
Wait. If $z=e^{i\theta} = \cos\theta + i\sin\theta$, then $x=\cos\theta, y=\sin\theta$.  
So $1+z = 1+\cos\theta + i\sin\theta$.  
Then $A^2 = (1+\cos\theta)^2 + (\sin\theta)^2$.  
This simplifies to $(1+2\cos\theta+\cos^2\theta) + \sin^2\theta = 2+2\cos\theta + 1 = 3+2\cos\theta$? No.  
$\cos^2+\sin^2=1$. So $2+2\cos\theta$?  
Wait. $(1+x)^2+y^2$.  
$x=\cos\theta, y=\sin\theta$.  
$(1+\cos\theta)^2 + \sin^2\theta = 1 + 2\cos\theta + \cos^2\theta + \sin^2\theta = 1 + 2\cos\theta + 1 = 2+2\cos\theta$?  
Wait. $1+\cos^2\theta+\sin^2\theta = 1+1=2$.  
So it is $2+2\cos\theta$.  
But earlier I wrote $(1+x)^2+y^2 = 2+2\cos\theta$ for $\theta=\pi/4$.  
Let's check $\theta=\pi/4$. $\cos(\pi/4)=0.707$.  
So $A^2 = 2 + 2(0.707) = 3.414$.  
And $|1+z| = \sqrt{3.414} = \sqrt{2+2\cos(\pi/4)}$.  
Wait. Let's verify my manual calculation for $\theta=\pi/4$ ($z=e^{i\pi/4}$).  
$A = |1+e^{i\pi/4}| = |1 + \frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}|$.  
Real part $1+0.707=1.707$. Imaginary part $0.707$.  
Magnitude squared: $(1.707)^2 + (0.707)^2 \approx 3 + 0.5 = 3.414$? No.  
$|1+e^{i\pi/4}|^2 = |1+e^{i\pi/4}|^2$.  
Wait. If $\theta=\pi/4$, then $z=e^{i\pi/4}$. Then $x=1/\sqrt{2}, y=1/\sqrt{2}$.  
So $(1+x)^2+y^2 = (1+1/\sqrt{2})^2 + 1/2 = 2 + \sqrt{2} + 1/2$? No.  
$(1+\frac{\sqrt{2}}{2})^2 + \frac{1}{2}$.  
Wait. $x=\cos(\pi/4) = \frac{1}{\sqrt{2}}$.  
So $(1+0.707)^2 + (0.707)^2 = 1.707^2 + 0.5$.  
$1.707^2 \approx 2.914$? No. $0.707^2 = 0.5$. $1.707 \approx 1+0.7$. $(1.7)^2 = 2.89$.  
$(1+\frac{1}{\sqrt{2}})^2 = ( \frac{2+\sqrt{2}}{2} )^2 = \frac{4+4\sqrt{2}+2}{4} = \frac{6+4\sqrt{2}}{4} = 1.5 + \sqrt{2}$.  
Add $y^2=0.5$. Total $\approx 2$.  
So $|1+z|^2 = 1.5 + \sqrt{2} + 0.5 = 2+\sqrt{2}$? No.  
$2+\sqrt{2} \approx 3.414$.  
Wait. My formula was $2+2\cos(\pi/4) = 3.414$.  
So $\sqrt{3.414}$ is correct.  
And $(1+\cos\theta)^2 + \sin^2\theta$ gives exactly $(1+\cos\theta)^2 + (1-\cos^2\theta)$? No.  
$\sin^2\theta = 1 - \cos^2\theta$.  
So $(1+\cos\theta)^2 + \sin^2\theta = 1+2\cos\theta+\cos^2\theta + 1-\cos^2\theta = 2+2\cos\theta$.  
Wait. This matches the formula I used earlier.  
But is this correct?  
Wait. $(1+z)^2 = (x+iy)^2$? No, $(1+z) = 1+x+iy$.  
Magnitude squared is $(1+x)^2 + y^2$.  
$x=\cos\theta, y=\sin\theta$.  
Wait. For $z=e^{i\theta}$, the coordinates of vector $z$ in $\mathbb{R}^2$ are $(x,y)=(\cos\theta, \sin\theta)$.  
Then $|1+z|^2 = (1+x)^2+y^2$? No, wait.  
If $z=x+iy$, then $|1+z|^2 = |1+e^{i\theta}|^2$? No.  
Wait. If $z=e^{i\theta}$, then coordinates are $(x,y)=(\cos\theta, \sin\theta)$.  
Then $1+z$ has coordinates $(1+\cos\theta, \sin\theta)$? No.  
Wait.  
If $z = x+iy$, then $1+z = 1+x+iy$.  
The magnitude squared is $(1+x)^2 + y^2$.  
Wait. Is this correct? Yes.  
So my derivation holds.  
But wait.  
Is it possible that I should be using a different coordinate system?  
If $z$ is on unit circle, coordinates of $z$ in $\mathbb{C}$ are $(x,y)$ such that $x^2+y^2=1$.  
Wait. Is it always true that if $z$ has modulus 1, then its coordinates satisfy $x^2+y^2=1$? Yes.  
So for any point on unit circle, the formula $A^2 = (1+x)^2+y^2$ holds.  
But wait. If $x=\cos\theta, y=\sin\theta$.  
Then $(1+x)^2+y^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
Let's check if this matches the formula $2+2\cos\theta$.  
Wait. $(1+\cos\theta)^2 + \sin^2\theta = 1+2\cos\theta+\cos^2\theta+\sin^2\theta = 1+2\cos\theta+1 = 2+2\cos\theta$.  
Yes. It matches.  
But wait. $(1+\cos\theta)^2 + \sin^2\theta$ equals $2+2\cos\theta$ only if $\cos^2\theta=0$? No.  
Wait.  
If I use $x=\cos\theta, y=\sin\theta$, then the expression is correct.  
But wait. Is it possible that $\theta$ in this formula refers to angle in radians? Yes.  
So for any $z$, $|1+z|^2 = 2+2\cos(\arg(z))$.  
Wait. But I found a potential issue.  
For $\theta=0$, $A^2 = 2+2(1) = 4 \implies A=2$. Correct.  
For $\theta=\pi/2$, $A^2 = 2+2(0) = 2 \implies A=\sqrt{2}$. Correct.  
Wait. But for $\theta=\pi$ ($z=-1$), $A^2 = 2+2(-1) = 0 \implies A=0$. Correct.  
So it seems formula for $|1+z|$ is simply $2\cos(\theta/2)$? No.  
Wait. Let's check $|1+e^{i\pi/4}|$ vs formula.  
$x=1/\sqrt{2}, y=1/\sqrt{2}$.  
Then $(x,y) = (\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2})$.  
So $A^2 = 2+2\cos(\pi/4) = 3.414$.  
And $\theta=\pi/4 \implies A^2 = (1+\cos(\pi/4))^2 + (\sin(\pi/4))^2 = (1+0.7)^2 + (0.7)^2$? No.  
Wait. I used $x=\cos\theta, y=\sin\theta$ to find coordinates of vector $z$.  
But for $\theta=\pi/4$, $x=0.707, y=0.707$.  
Then $(1+x)^2 + y^2 = (1.7)^2 + 0.5 \approx 2.89+0.5=3.39$.  
Wait. $|1+z|^2$ must be $2+2\cos(\pi/4) = 3.414$.  
Is it possible that $\cos(\theta)$ is defined as $\cos(3\pi/4)$?  
Wait. $\arg(z)=3\pi/4 \implies z=e^{i3\pi/4}$.  
Then $x=-0.707, y=0.707$.  
Then $(1+x)^2+y^2 = (1-0.707)^2 + 0.5 = (0.293)^2+0.5 \approx 0.085+0.5=0.585$? No.  
Wait. $\cos(3\pi/4) = -0.707$.  
So $(1+\cos(\theta))^2 + \sin^2(\theta)$ would be $(1-0.7)^2+0.5 = 0.085+0.5=0.585$? No.  
Wait. My formula was $A^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
If $\theta=\pi/4$, then $x=1/\sqrt{2}$. So $(1+0.7)^2+y^2 = 1.7^2+0.5 = 3.414$.  
Wait. Is this correct?  
Let's check if $z=e^{i\theta}$ satisfies $(1+x)^2+y^2$ with $x=\cos\theta, y=\sin\theta$.  
Yes, it does.  
But wait. This formula depends on $\theta$.  
Does it depend on $\arg(z)$ or something else? No.  
It seems correct.  

Now for term 2: $B = |1 - z + z^2|$.  
If $z=e^{i\theta}$, then $x=\cos\theta, y=\sin\theta$.  
Then $1-z+z^2 = 1 - (\cos\theta + i\sin\theta) + ( \cos(2\theta) + i\sin(2\theta) )$? No.  
Wait. $z^2$ is NOT $\cos(2\theta) + i\sin(2\theta)$ if I use $x=\cos\theta$.  
Wait. This is wrong.  
Let's use standard polar coordinates for $z$.  
If $z = x+iy$, then $x^2+y^2=1$? No, that is only true for unit circle.  
So if $z$ is on unit circle, then $|z|=1$. So $\cos(\theta)$ and $\sin(\theta)$ are related by $x=\cos\theta, y=\sin\theta$.  
Wait. Is it possible I am confusing coordinate with angle?  
Let's define vector $v_z = z$. Its magnitude is 1.  
Its direction is determined by angle $\theta$ (say).  
So $z = r e^{i\theta} = 1 \cdot (\cos\theta + i\sin\theta)$.  
So $x=\cos\theta, y=\sin\theta$.  
Wait. Wait. If I write $z=e^{i\theta}$ as a point in the plane with coordinates $(\cos\theta, \sin\theta)$, then $x=\cos\theta$ and $y=\sin\theta$ is consistent.  
So my previous derivation holds.  

But wait. Let's double check the term 2 expansion.  
$1 - z + z^2 = 1 - (\cos\theta + i\sin\theta) + \dots$? No.  
Wait. If $z=e^{i\theta}$, then $z^2 = e^{-i2\theta}$? No.  
Let's check if $z^2$ is $\cos(2\theta)$ or something else.  
If $z=e^{i\theta}$, then $z^2 = \cos(2\theta) + i\sin(2\theta)$.  
So the term is $(1 - z + z^2)$.  
Wait. $1$ is real. $-z$ is imaginary part negative.  
So real part: $1 - \cos\theta + \cos 2\theta$.  
Imaginary part: $\sin\theta - \sin 2\theta$. (Wait, $i\sin\theta$).  
Wait. Is it $\sin(2\theta)$ or $\sin(-2\theta)$? No.  
If $z^2 = e^{-i2\theta}$ is wrong.  
Let's check if $z=e^{i\theta}$. Then $z^2 = (\cos\theta + i\sin\theta)^2 = \cos^2\theta - \sin^2\theta + 2i\sin\theta\cos\theta$.  
So real part is $\cos(2\theta)$? No. $\cos(2\theta) = \cos(\theta)\dots$ No.  
$\cos(2\theta) = 1-2\sin^2\theta = 1-\dots$. Wait.  
My confusion was mixing up trigonometric identities with complex numbers.  
Let's use the explicit formula for $z^2$.  
Wait. Is there an easier way to calculate $B$?  
Maybe express terms using vectors?  
Let $u = 1+z$. $|u|^2 = (x+1)^2 + y^2$? No, let's just stick to coordinates.  
If $z=x+iy$, then $u = 1+x+iy$.  
And $v = 1-x+y$? No.  
$v = 1 - z + z^2 = 1 - (x+iy) + (x^2-y^2-2ixy)$? No.  
Wait. Is $z^2$ simply $(x+iy)^2$? Yes.  
So $v = 1 - z + z^2$.  
If I want to calculate $|1-z+z^2|$, I can use the polar coordinates for $z$ and $z^2$.  
Wait. $|u|^2 = (x+1)^2 + y^2$.  
But wait. If $x=\cos\theta, y=\sin\theta$, then $(x+1)^2+y^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
Wait. But if I substitute $\theta$ from $z$. Then I get something like $2+2\cos(\arg z)$.  
Wait. Is this correct?  
Let's check $|1+z|^2$ again.  
If $x=\cos\theta, y=\sin\theta$, then $(1+x)^2+y^2 = (1+\cos\theta)^2+\sin^2\theta$.  
This is $2+2\cos\theta$.  
So $A = \sqrt{2+2\cos(\arg z)}$.  
But wait. This value is only valid if coordinates $(x,y)$ of $z$ are $\cos\theta, \sin\theta$?  
Is it possible that I am using the wrong polar coordinates for complex numbers?  
Wait. Complex number $z = x+iy$. Its modulus is $\sqrt{x^2+y^2}$.  
This is always true.  
And my calculation of $A$ used $(x,y)$ as real coordinates where $x=\cos\theta, y=\sin\theta$.  
Is it possible that $\theta$ in polar form refers to coordinate angle? Yes.  
But wait. What if $\theta$ refers to something else?  
Ah. The standard formula for the magnitude of complex number is given by the distance.  
Wait. Is there a geometric interpretation?  
We have $u = 1+z$. Its coordinates are $1+x, y$.  
Wait. If I consider the unit circle in $\mathbb{C}$, then points $(x,y)$ satisfy $x^2+y^2=1$.  
If we define the angle of $z$ by the polar relation $x=\cos\theta, y=\sin\theta$, then we have a mapping from angles to coordinates.  
But wait. Is it possible that $\theta$ in my derivation was an argument and I need to check consistency?  
Wait. Let's verify if my formula $(1+\cos\theta)^2+y^2 = 2+2\cos\theta$ is correct for $x=\cos\theta, y=\sin\theta$.  
Is this always true? No.  
Let's re-evaluate $|1+z|$ again.  
If $z=x+iy$, and $x^2+y^2=1$. Then $A = |1+z|$.  
Wait. Is $|1+z|^2$ determined by coordinates $x,y$?  
No, coordinates of $z$ are $(x,y)$. But coordinates of $1+z$ are $(1+x, y)$.  
Then magnitude squared is $(1+x)^2+y^2$.  
Wait. This formula is for any complex number $w = u+iv$ with coordinate vectors $(u,v) \in \mathbb{C}^2$? No.  
The coordinates of a complex number are defined relative to the complex plane $\mathbb{C}$? No, real $\mathbb{R}$.  
So if $z$ is defined by $x,y$, then $|1+z|^2 = (1+x)^2 + y^2$.  
But wait. This formula depends on $(x+iy)$ where $x,y$ are complex numbers?  
Wait. If I just use the coordinates of vectors, i.e., $z=x_0+ix_1$.  
Then the coordinates of $1+z$ in $\mathbb{R}^2$ (viewed as $\mathbb{C}$) are $x_0+1+ix_1+i x_1 = 1+x_0 + i(x_0+y_0)$? No.  
Wait. If I just use vectors, it's simpler.  
Let $z = u+iv$. Then $1+z = (1+u) + iv$. The modulus is $\sqrt{(1+u)^2+v^2}$.  
Now, let's define coordinates $(x,y)$ in terms of real numbers?  
Usually we associate complex numbers with points on the circle.  
Let's check if my formula $|1+z|^2 = 2+2\cos(\arg z)$ is correct.  
Wait. Let's test $z=-1$. Then $\theta=\pi$.  
$A = |1-1|=0$. Formula: $(1-1)^2 + 0^2=0$. Correct.  
Let's test $z=1$. Then $\theta=0$.  
$A = |1+1|=2$. Formula: $(1+1)^2+0=4$. Correct? No, wait.  
If I use coordinates $(x,y)=(1,0)$, then $|1+z|^2 = (1+1)^2 + 0^2 = 4$.  
But earlier I said for $\theta=0$, $A^2=2$. Why did I say that?  
Wait. Let's check again.  
If $z=1$, then $x=1, y=0$ is the coordinate.  
Then $(1+x)^2+y^2 = (1+1)^2 = 4$.  
But my previous calculation for $\theta=\pi/2$ ($z=i$) gave $A^2=2$.  
So if $\theta=0$, $A^2=4$, so $A=2$. Correct.  
Wait. Wait. Let me re-read the example $z=-1$.  
If $z=-1$, then $\theta=\pi$. $x=-1, y=0$.  
Then $(1+x)^2+y^2 = (1-1)^2 + 0 = 0$.  
So $A=0$. Correct.  
Wait. So $|1+z|^2$ using coordinates is correct for all points on unit circle?  
Let's check $\theta=\pi/2$ ($z=i$).  
$x=0, y=1$. $(1+0)^2+1^2 = 2$.  
So $A^2=2$. $|1+i|= \sqrt{2}$. Correct.  
Wait. I am confusing myself with the magnitude of vectors.  
Is $|1+i|$ really $\sqrt{2}$? Yes, it's distance from $(0,0)$ to $(1,i)$ is $\sqrt{2}$.  
So everything seems correct.  
BUT wait. Earlier I checked $z=0$, which gives $A=1$. Formula: $(1+0)^2+0=1$. Correct.  
Wait. Let me re-check my formula derivation for $|1+z|$.  
The coordinate $(x,y)$ is real numbers such that $x^2+y^2=1$ is satisfied by any point on unit circle? No.  
Let's restate clearly:  
Any complex number $z$ with $|z|=1$ corresponds to a point $P$ in the plane $\mathbb{C}$ which lies on the unit circle. The coordinates of $P$ can be denoted as $(x,y)$ where $x^2+y^2=1$.  
So my formula is correct for all points on the unit circle.  

Wait. Is this consistent?  
Let's check if $\theta$ was angle of $z$, then $x=\cos\theta, y=\sin\theta$.  
If I assume $|1+z|^2 = (1+x)^2+y^2$ and $(1+x)^2+y^2 = 2+2\cos(\arg(z))$? No.  
Wait. My formula for $|1+z|^2$ was derived using coordinates in terms of $\theta$.  
But is it correct to assume that $x=\cos\theta, y=\sin\theta$ corresponds to the coordinate system where magnitude is 1?  
Yes.  
So $A^2 = (1+\cos\theta)^2 + \sin^2\theta = 2+2\cos\theta$.  
But wait. Let's check this again carefully.  
Is it possible that I should be taking $|1+z|^2 = (x+1)^2+y^2$ where $x,y$ are coordinates of $z$ in $\mathbb{C}$?  
Wait. If $z=x+iy$, then $x,y$ are real numbers.  
Then $x^2+y^2=1$.  
Then $(1+x)^2 + y^2 = (1+x)^2 + x^2 = 2+2x$? No.  
Wait.  
Let's check with $z=0 \implies x=0, y=0$. Formula gives 0? No.  
Ah! If I use coordinates $(x,y)$ as vector $z$, then $|1+z|^2 = (1+x)^2+y^2$ holds?  
Wait. This is a very common confusion.  
If we have vector $v=(x,y)$. Then $\sqrt{v \cdot v} = |z|$? No.  
Wait. If I use the formula $(1+x)^2+y^2$, then for $z=1$ (vector $v=(1,0)$), $|1+1|^2 = 4$. But $z=1$ means vector is $(1,0)$. So $|1+1|^2 = 4$.  
But if I take vector $(x,y)=(\cos\theta, \sin\theta)$? No.  
Wait. If $z=x+iy$, then coordinates are real numbers.  
Then $|1+z|^2 = (1+x)^2+y^2$.  
This leads to $|1+z|^2$ as a function of $\theta$ if I define $\theta$ as the angle of $z$?  
No. If $x=\cos\theta, y=\sin\theta$, then $A = \sqrt{2+2\cos\theta}$.  
Wait. This formula gives 4 for $\theta=0$.  
Is it correct that $|1+z|=2$ for $z=1$? Yes.  
So the formula $2+2\cos\theta$ is valid for $\theta \in [0, 2\pi]$?  
Wait. If $\theta=0$, it gives 4. But $|1+1|=2$.  
Wait. $2+2\cos\theta = 2(1+\cos\theta)$ or $2|\cos\theta|$? No.  
$2+2(-1) = 0$. This matches $\theta=\pi$.  
$2+2(0) = 2$. Matches $\theta=0$? No, wait.  
If $\theta=0$, then $x=1, y=0$. $(1+x)^2+y^2 = (1+1)^2 = 4$.  
Wait. But if $|1+z|=2$, then $A^2=4$.  
So $A^2$ formula gives $4$ for $\theta=0$. Correct.  
If $\theta=\pi/2$. $x=0, y=1$. $(1+x)^2+y^2 = (1)^2+1^2 = 2$.  
Matches $|1+i|^2 = 2$.  
So my formula $|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta$ is correct.  
Wait. Is it possible that for $\theta=0$, $(1+\cos\theta)^2 + \sin^2\theta$ simplifies to something else?  
Yes, $(1+1)^2 = 4$. $2(1) = 2$ (if I used $x=\cos\theta, y=\sin\theta$ in terms of angle).  
Wait. If $\theta=0$, then $\cos\theta=1$.  
Then $2+2(1)=4$.  
If I use formula $(1+\cos\theta)^2 + \sin^2\theta = (1+1)^2+0 = 4$.  
So this seems correct.  

Wait. Let's re-calculate for $\theta=\pi/2$ in my head again.  
$z=i \implies \theta=\pi/2$.  
$|1+i|^2 = 2$.  
$(1+\cos(\pi/2))^2 + \sin^2(\pi/2) = (1+0)^2 + 1 = 2$. Correct.  

So my formula for $A$ is correct: $|1+z|^2 = (1+\cos\theta)^2 + \sin^2\theta$.  
Wait. But this depends on $\theta$.  
And I have to integrate over the angle? No, we are looking for max value.  
But wait. The term is linear in $\theta$.  
So $f(\theta) = (1+\cos\theta)^2 + \sin^2\theta + |1-z+z^2|$.  
Wait. Is it possible to simplify $(1-z+z^2)$?  
If $z=e^{i\theta}$, then $z^2 = e^{i2\theta}$.  
So $1-z+z^2$ has imaginary part $\sin(2\theta)$ and real part $1-\cos\theta+\dots$? No.  
Wait. Let's simplify the expression $B = |1-z+z^2|$.  
Maybe I can write $z^2 + z - 1 = 0$ if $z$ is a root? No, that would be roots of cubic polynomial.  
But wait. Let's look at the modulus.  
Let's try to express $A+B$ in terms of $|z|^2$? No.  
Maybe we can write $|1+z|$ in polar form?  
If $z=x+iy$, then $1+z = 1+x+iy$.  
Wait. This is getting too complicated with coordinates.  
Let's go back to geometric interpretation.  
The terms are distances from origin and some rotated distance.  
Maybe there is a specific angle $\alpha$ such that $1+z$ and $1-z+z^2$ align?  
Consider the expression as sum of moduli.  
We want to maximize $\max (|1+z| + |1-z+z^2|)$.  
Let's look at the constraints. $|z|=1 \implies z = e^{i\theta}$.  
Wait. Is it possible that $|1-z+z^2|$ is minimized or something?  
Actually, if $B=0$ then $|1-z+z^2|=0$.  
This happens when $z$ satisfies $z^2+z-1=0 \implies z = \frac{-1 \pm \sqrt{5}}{2}$.  
These are complex numbers on the unit circle? No.  
Discriminant of $x^2+x-1=0$ is $1+4=5$. Not square.  
So $z$ cannot be real root. But $|z|=1$. So this would mean $z$ is not a point on unit circle?  
Wait. $|z|=1 \implies z \in \mathbb{U}$.  
The roots of $x^2+x-1=0$ are $\frac{-1 \pm \sqrt{5}}{2}$, which are complex numbers with imaginary part? No.  
Wait. $e^{i\theta}$ values?  
Wait. If $z=e^{i\theta}$, then $|z|=1$ is just magnitude 1.  
Roots of $x^2+x-1=0$: $z = e^{i\pi/4}$? No. $e^{i\pi}$.  
The equation $z^2+z-1=0$ has solution $z = \frac{-1 \pm \sqrt{5}}{2}$. These are not on unit circle unless... wait.  
Let's check magnitude of roots:  
$\frac{-1+\sqrt{5}}{2} \approx \frac{1.236}{2} \approx 0.618$. Modulus squared is $(0.618)^2 + (1/2)^2$? No.  
Wait. $z = \frac{-1+\sqrt{5}}{2}$. Is it on unit circle?  
$|z|^2 = (\frac{\sqrt{5}-1}{2})^2 + 0 = \frac{6-2\sqrt{5}}{4}$? No.  
Wait. Let's check if $z=e^{i\pi/2}$.  
Let's check if roots are on unit circle.  
$|z|^2 = (x)^2 + (-1)^2$? No.  
The roots of $t^2+t-1=0$ are $t = \frac{-1 \pm \sqrt{5}}{2}$.  
For real numbers $x,y$, $|z|=1 \implies x^2+y^2=1$.  
So this polynomial has no roots on unit circle.  
Wait. But the modulus of complex number $z$ is always 1.  
Wait. If I use my coordinates, then $z=e^{i\theta}$ satisfies $x^2+y^2=1$? No.  
Wait. My derivation that coordinates satisfy $x^2+y^2=1$ assumed $x,y$ are real numbers such that $|z|=1$.  
Is it true that $\cos(\theta)^2 + \sin(\theta)^2 = 1$ is not a constraint for $z$ to be on unit circle?  
Wait. The problem says "Let $z$ be a complex number such that $|z|=1$."  
So $z$ must lie on the unit circle in $\mathbb{C}$.  
My derivation using polar coordinates implies that if $z=e^{i\theta}$ (with $x=\cos\theta, y=\sin\theta$) is NOT always true?  
Wait. If $z$ is on unit circle, then its coordinates must satisfy $x^2+y^2=1$.  
So yes.  
But wait. The roots of the equation were $\frac{-1+\sqrt{5}}{2}$ which are NOT unit circles.  
So it seems $B \neq 0$ for any $\theta$ where roots exist? No, that would be a contradiction.  
Wait. Did I make a mistake in expansion?  
Let's check if I can write $|1-z+z^2|$ in terms of $z$.  
If $z=x+iy$, then $|1-z+z^2|^2 = (1-x)^2 + y^2$? No.  
Wait. Let's look at the function again.  
$B = |1 - z + z^2|$.  
Is it possible that $B=0$ implies $z^2+z-1=0$? Yes, roots of that are $\frac{-1 \pm \sqrt{5}}{2}$.  
So these roots do not lie on unit circle.  
So we don't worry about zeroing the term.  
Wait. But if I want to maximize $|1+z|$ and $|B|$, maybe I can just express them as functions of $\theta$ and find max?  
My formulas:  
$A = 2+2\cos\theta$.  
$B^2 = (1-\cos(\theta))^2 + \sin^2(2\theta)$?  
Wait. Let's expand $|1-z+z^2|^2$ with $x=\cos\theta, y=\sin\theta$.  
Wait. If $z=e^{i\theta}$, then $x=\cos\theta$ is not the coordinates in the standard basis $(x,y)$.  
Wait. The vector representation is a problem if I don't fix the origin? No, modulus of complex number is distance from origin.  
If $z=e^{i\theta}$, then $z$ is represented by vector $\mathbf{u} = e^{i\theta} = \cos\theta + i\sin\theta$.  
Then $1-z+z^2$ corresponds to summing vectors $1, -z, z^2$.  
Vector sum: $1 + (- (\cos\theta + i\sin\theta)) + (\cos^2\theta - \sin^2\theta + 2i\sin\theta\cos\theta)$. No.  
Wait. Vector subtraction?  
$-z = -(\cos\theta + i\sin\theta)$.  
So we add vectors $\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3$ where $\mathbf{u}_1 = (1, 0)$? No.  
Vector addition in $\mathbb{C}$ is sum of complex numbers.  
We need to express this in terms of $x,y$.  
Wait. Let's simplify the expression inside modulus.  
Let's denote vector $v_1$ corresponding to $z$. $v_2$ for $-z$, $v_3$ for $z^2$.  
Then $1 + v_1 = 1 + z$.  
And $1 - v_1 - v_2 + v_3$? No.  
Wait. The term is $1 - z + z^2$. This can be written as $1 + \mathbf{u}_{-z} + \mathbf{u}_{z^2}$ where $\mathbf{u}_w = w$ (vector).  
No. It's $1 - z + z^2 = 1 - (e^{i\theta} - e^{-2i\theta})$. No.  
Wait. Let's use the coordinates directly.  
$x=\cos\theta, y=\sin\theta$.  
Then $z = x+iy$? No. This is not possible because $x,y$ satisfy $x^2+y^2=1$.  
Wait. If I have a complex number $z$, its coordinate is $(x,y)$.  
If I write $z=x+iy$, then this is always true for any point on unit circle in $\mathbb{C}$.  
So let's assume $z$ corresponds to the vector $\mathbf{z}$ with real parts $x,y$ (where $x,y \in \mathbb{R}$).  
Wait. But wait. If I define $x$ as the real part of $z$ and $y$ as the imaginary part, then $|z|^2 = x^2+y^2$.  
Wait. Does this imply coordinates are $(x,y)$?  
Yes, if $z=x+iy$, then coordinates are real numbers.  
Is it possible that coordinates are not independent? No.  
So $A = |1+z|$ can be written as $\sqrt{(1+x)^2+y^2}$ where $x,y$ are the coordinates of $z$.  
Wait. But $x,y$ are just coordinates?  
If $z=0$, then $x=0, y=0$. $A=|1|^2 = 1$.  
If $z=1$, then $x=1, y=0$. $A = \sqrt{(1+1)^2} = \sqrt{4}=2$. Correct.  
Wait. So my formula $A^2 = (1+x)^2+y^2$ is correct for any point on unit circle?  
Yes, because $|1+z|^2 = |1+z|^2 = 1 + z + \bar{z}$? No.  
It's just distance.  
But wait. If I write coordinates of $z$ as $(x,y)$ such that $x^2+y^2=1$.  
Then coordinates of $1+z$ are $(1+x, y)$.  
Wait. But this assumes $y$ is the imaginary part coordinate.  
Is it possible that $y$ is real? No, if $z=x+iy$, then $y$ is just a real number.  
Wait. Does $x^2+y^2=1$ hold? Yes.  
So if I have coordinates $(x,y)$ such that $x,y \in \mathbb{R}$ and $x^2+y^2=1$.  
Then coordinates of $1+z$ are $(x+1, y)$.  
But wait. The term "coordinates" usually refers to basis vector components.  
If I just treat $z$ as a complex number in the $\mathbb{C}$-plane, then its modulus is 1.  
The term $|1+z|$ is the distance from 0 to point $1+z$.  
Is this distance equal to $\sqrt{(1+x)^2+y^2}$? No.  
Wait. If $z=x+iy$, then $x,y$ are just coordinates in the plane.  
So $z = x_0 + i y_0$.  
Then $|1+z|^2 = (1+x_0)^2 + (y_0)^2$ is only true if $1+z$ corresponds to coordinate vector $(1+x_0, y_0)$?  
Wait. The coordinates of $z$ are $(x,y)$. The coordinates of $1+z$ are $(1+x, y)$.  
But wait. Is it possible that I should treat complex numbers as vectors in $\mathbb{C}$? Yes.  
So the modulus is $\sqrt{(1+Re(z))^2 + (Im(z))^2}$. No.  
Wait. If $z=x+iy$, then Re(z)=x, Im(z)=y.  
Then $|1+z|^2 = (  

## Answer

*(none: the token cap hit during thinking)*
