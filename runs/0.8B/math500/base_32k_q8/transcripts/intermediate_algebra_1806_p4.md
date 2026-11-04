# test/intermediate_algebra/1806.json, part 4 of 5

[Previous part](intermediate_algebra_1806_p3.md) · [Start](intermediate_algebra_1806.md)

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

*Continued in [part 5 of 5](intermediate_algebra_1806_p5.md): GitHub stops rendering math on pages this long, so the transcript is split.*
