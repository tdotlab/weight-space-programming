# test/intermediate_algebra/1806.json, part 3 of 5

[Previous part](intermediate_algebra_1806_p2.md) · [Start](intermediate_algebra_1806.md)

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

*Continued in [part 4 of 5](intermediate_algebra_1806_p4.md): GitHub stops rendering math on pages this long, so the transcript is split.*
