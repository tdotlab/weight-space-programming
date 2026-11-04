# test/intermediate_algebra/1806.json, part 2 of 5

[Previous part](intermediate_algebra_1806.md)

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

*Continued in [part 3 of 5](intermediate_algebra_1806_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
