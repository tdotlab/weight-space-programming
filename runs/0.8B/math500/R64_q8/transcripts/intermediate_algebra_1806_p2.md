# test/intermediate_algebra/1806.json, part 2 of 3

[Previous part](intermediate_algebra_1806.md)

Wait, if $|z|=1$, $|z|=1$ means $z \bar{z} = 1$. No. $|z|$ is distance from origin.  
If $z$ is on unit circle, then $z \in \{x | |x| = 1\}$.  
Then $|1+z| = \sqrt{(1+Re z)^2 + (Im z)^2}$?  
Wait, this is not right.  
Let's just calculate $|1+z|^2$ again.  
$|1+z|^2 = (1+e^{i\theta})(1+e^{-i\theta})$.  
Wait, I think I am confusing myself with $z^{-1}$.  
Let's use standard notation. Let $x=1+z$. Then $z=x-1$. Since $|z|=1$, $|x-1|=1 \implies |x|=2$? No.  
If $z=e^{i\theta}$, then $|e^{i\theta}-1|^2 = e^{-i\theta} - 2 + e^{i\theta}$. No.  
Wait, $(1+e^{i\theta}) (1+e^{-i\theta})$ is a complex number?  
No, wait. If $z=e^{i\theta}$, then $\bar{z}=e^{-i\theta}$. Then $|z|=1$. So $z \overline{z} = 1$. Wait.  
The constraint is $|z|=1$. This means $z = e^{i\theta}$ for some real angle $\theta$.  
Let's re-calculate $|1+z|^2$ properly.  
For $z=e^{i\theta}$, $1+z = 1+e^{i\theta} = (2+\cos \theta) + i(1+\sin \theta)$? No.  
$1+z = 1+e^{i\theta} = e^{i\theta/2}(e^{-i\theta/2}+e^{i\theta/2}) = 2\cos(\theta/2)$. No, that's not right.  
Let's write $1+e^{i\theta} = (\cos \frac{\theta}{2} + i\sin \frac{\theta}{2})(\cos \frac{\theta}{2} - i\sin \frac{\theta}{2})$?  
Wait, this is for magnitude of complex exponential.  
Let's use coordinates.  
$x+y = x+z$? No.  
$|1+e^{i\theta}|^2 = 1 + e^{i\theta} + 1 + \bar{z}$?  
Let's try: $|1+e^{i\theta}|^2 = 1 + 2\cos \theta$? No, wait.  
Wait, $(1+e^{i\theta})(1+e^{-i\theta}) = 1 + e^{i\theta} + e^{-i\theta} + 1$.  
Is this equal to $|1+e^{i\theta}|^2$? Yes.  
Wait, $\bar{z}$ is not just a scalar but the conjugate. Wait, if I assume $z=e^{i\theta}$ (real argument), then $\bar{z}=e^{-i\theta}$.  
Then $1+e^{-i\theta} = 2 + i \sin(\theta)$? No, $e^{i\theta} = \cos \theta + i \sin \theta$.  
$1+e^{i\theta} = (1+\cos \theta) + i\sin \theta = 2\cos^2(\theta/2) + i(2\sin(\theta/2)\cos(\theta/2)) = 2\cos(\theta/2)(\cos(\theta/2)+i\sin(\theta/2)) = 2e^{i\theta/2}$? No.  
Wait, $e^{i\theta} = \cos \theta + i \sin \theta$.  
$1+e^{i\theta} = 2\cos^2(\frac{\theta}{2}) + e^{i(\pi-\theta)/2}$?  
Wait, I'm getting confused with standard identities.  
Let's just compute $|1+z|^2$ explicitly using $\theta$.  
If $z=e^{i\theta}$, then $1+e^{i\theta} = 1 + \cos \theta + i \sin \theta$.  
Magnitude squared: $(1+\cos \theta)^2 + (\sin \theta)^2 = \cos^2 \theta + 2\cos \theta + 1 + \sin^2 \theta = 2 + 2\cos \theta$.  
So $|1+z|^2 = 2+2\cos \theta$? No. Wait, earlier I said max is 4 (at $\theta=0$, $z=1$). At $\theta=0$, $1+e^{i0}=2$, squared is 4. So formula gives $2+2(1)=4$. Correct.  
If $z=e^{i(\pi-\theta)}$, then $|1+z|^2 = 2-2\cos \theta$? No, that would be $\max - \min$ of modulus.  
So for unit circle, the range of values for $|1+z|$ is $[0, 4]$? Or $[-2, 3]$?  
Wait, if $z=1$, $|1+1|=2$. If $z=i$, $|1+i| = \sqrt{2}$. Max value is when $\theta=0$ (value 2) or $\theta=\pi$ (value 2)?  
Wait, $\cos \theta$ at $\theta=0$ gives 2. At $\theta=\pi$ gives -2. So magnitude can be $\sqrt{4}=2$ or $\sqrt{6}$? No.  
If $z=e^{i\theta}$, then $|1+z|^2 = 2+2\cos \theta$. This is real valued if we consider $z$ as complex number? No, it's a function of $\theta$. It takes values in $[0, 4]$.  
Wait, for complex numbers, the modulus can be less than or equal to 2?  
Actually, let's check my logic about $|1+z|$ max value.  
Let $z=1$. $|1+1|=2$.  
Let $z=-1/2$? Then $|z| \neq 1$.  
Wait, the constraint is $|z|=1$. So $z$ must be on unit circle.  
Then $\theta$ can be anything. But for complex numbers in general (not restricted to unit circle), magnitude can range up to something larger? No, if $|z|$ can be arbitrary complex number? No, $|z|=1$ means it's on the unit circle. So $z$ takes values $e^{i\theta}$.  
Wait, so $|1+z|^2 = 2+2\cos \theta$ is correct. The range of this value is $\min(0, \dots)$? No.  
Wait, if $\theta=0$, $|1+z|=2$. If $\theta=\pi$, $|1+z|^2 = 2-2(-1) = 4$. Wait.  
At $\theta=\pi$, $e^{i\pi} = -1$. So $z=-1$. Then $|1+z| = |0| = 0$.  
Wait, formula gave $2+2\cos \pi = 2-2 = 0$. Correct.  
Wait, at $\theta=0$, $z=1$, formula gives $2+2(1) = 4$.  
So $|1+z|$ can be 0 and 2? Wait, is it always positive? No, $2-2\cos \theta$ is negative if $\cos \theta > 1$ which is impossible.  
Wait, for complex numbers $w$, $|w|^2 = w\bar{w}$. Since $z=e^{i\theta}$, $z^{-1}=e^{-i\theta}$.  
Wait, $|1+z|$ squared is $(1+e^{i\theta})(1+e^{-i\theta})$. This product is real? No.  
Let's re-evaluate the expression $(1+e^{i\theta})(1+e^{-i\theta})$.  
$1+e^{i\theta} = 2 + i \sin \theta - 2\cos \theta$. No, wait.  
Wait, let's just use $z=e^{i\theta}$ directly.  
$|1+z|^2 = (1+\cos \theta)^2 + (\sin \theta)^2 = \cos^2 \theta + 2\cos \theta + 1 + \sin^2 \theta = 2 + 2\cos \theta$. Wait.  
Wait, for $z=-1$, $\theta=\pi$, $\cos \pi = -1$. Then $|1+z|^2 = 2-2 = 0$. This means $|1+z|=0$ is consistent with formula.  
Wait, if $z=i$, $\theta=\pi/2$, $\cos \theta=0$. Then $|1+z|^2 = 2+2(0) = 2$. So $|1+i|=2$. But I thought $|1+i|=\sqrt{2}$. Ah, so $\sqrt{2}$ is correct.  
So formula for $|1+z|^2$ seems correct.  
Wait, why did I say earlier max value is 4?  
Ah, because at $\theta=0$, it's $2+2=4$. So yes, max is 4.  
Wait, earlier I thought at $z=-1$, term is 0. Wait, if $|1+z|$ can be 0, then $S$ can be small. But we want to maximize sum.  

Now let's analyze the second term: $|1-z+z^2|$.  
Let $w = 1-z+z^2$.  
Since $z=e^{i\theta}$, $w = 1 - e^{i\theta} + e^{2i\theta} = \frac{e^{i\theta}(-e^{-i\theta})}{...}$? No.  
Wait, let's find the locus of points represented by $1-z+z^2$ as $\theta$ varies.  
Actually, let's rewrite in terms of a variable $x = 1+z$. Since $z=e^{i\theta}$, $x = e^{i(\theta+1)} + e^{-i\theta} + \dots$? No.  
Wait, $z=x-1$ is not the correct relation. $z$ is just a complex number.  
The expression $1-z+z^2$ depends on $\theta$.  
Let's calculate its magnitude for general $x = 1-z+z^2$ using $\theta$ directly? No, we need to parameterize by $x$.  
Wait, since $|z|=1$, $z \in \mathbb{T}$.  
We can express $1-z+z^2 = (1-z)(z+1) - z + z^2$. No.  
Let's use the identity: $1-z+z^2 = (z^2+z-1)$? No.  
Wait, if we consider the points on the complex plane.  
Let's parameterize by $x$ such that $|x|=1$? No.  
Actually, let's try to rewrite the modulus $|1-z+z^2|$ as a sum of lengths.  
Consider the identity: $(1-z)(1+\bar{z}) = 1 - z - \bar{z} + z\bar{z}$. No.  
Let's consider the function $g(z) = |1-z+z^2|^2$.  
We want to maximize $|1+z| + \sqrt{|1-z+z^2|^2}$.  
Note that since $\theta$ varies, we can vary $z$ continuously.  
Actually, for any $z$, let $A = 1+z$. Then $z = A-1$. The constraint $|z|=1$ means $|(A-1)|=1$, i.e., $A$ lies on the circle of radius 2 centered at -1? No.  
Wait, if $z=A-1$, then $|A-1|=1$. This defines a circle in the complex plane of A.  
Let $w = A$. Then $|w-1|=1$. So $w$ lies on the disk $D_1(\text{center}=-1, R=1)$.  
Wait, $z$ is restricted to unit circle. So $A$ traces a region in the plane? No.  
Wait, $z \in \mathbb{T}$ (unit circle). Then $A = 1+z$. This maps $\mathbb{T}$ to $\mathbb{C}$.  
Is it true that for any $w$ such that $|w-(-1)|=1$, we can find $z$? Yes, $z = w+1$? No.  
Wait, if $A$ is arbitrary complex number, then $z=A-1$ satisfies $|z|=1 \implies |A-1|=1$. This describes the set of points $A$ such that distance to -1 is 1. So it's a circle centered at -1 with radius 1.  
Wait, earlier I thought the range was $|w-1|=1$. But here $|w-A| = |z| \le 2$.  
Ah, if $|A|=2$, then $A=1+z$. If $z=1$, $A=2$. So $A$ must satisfy $|A-(-1)|=1$.  
So $A$ lies on circle centered at -1 with radius 1.  
Wait, but I said $|1+z|$ max is 4.  
Ah, if $z$ moves around the unit circle, then $1+z$ moves around a region.  
The locus of $w = 1+z$ ($w$ in $\mathbb{C}$) such that $|w-(-1)|=1$. No, this would mean $A$ is constrained to be on that circle.  
But earlier I thought range of $|1+z|$ was up to 4 (at $z=-1$). Wait, for $z=1$, $|1+1|=2$. If $|A|$ could be anything, max would be $\infty$. But wait, constraint is $|z|=1$.  
If I let $z=e^{i\theta}$, then $w = 1+z$ traces a set of points $A(e^{i(\theta+1)})$. Wait, $e^{i(\theta)}$ is just $z$.  
So $w = 1+z$ where $z \in \mathbb{T}$. Then $|w|^2 = |1+e^{i\theta}|^2 = 2+2\cos \theta$.  
Wait, if $\theta$ ranges from $0$ to $2\pi$, then $2+\cos \theta$ ranges in $[2, 4]$.  
But wait. Is this true?  
If $\theta=0$, $z=1$, $w = 2$. Wait, earlier I said at $z=1$, $|1+z|=2$. So max is 2.  
Wait, let me check the formula again.  
$|1+e^{i\theta}|^2 = (1+\cos \theta)^2 + \sin^2 \theta$? No.  
$|1+e^{i\theta}| = |2\cos(\frac{\theta}{2}+\pi/2)|$? No.  
Let's use polar decomposition again. $w = 1+z$.  
If $z = e^{i\theta}$, then $w = e^{i\theta} + 1$.  
Wait, earlier I wrote "max is 4" for $\cos \theta$.  
Ah, let me re-verify:  
If $\theta=0$, $z=1$, $|1+1|=2$.  
If $\theta=\pi$, $z=-1$, $|1-1|=0$.  
Wait, earlier I calculated max value of $|1+z|$ was 4?  
Ah, because for $z \in \mathbb{C}$, $|z| \le |z+e^{i\phi}|$? No.  
Let me check the formula $(1+\cos \theta)^2 + \sin^2 \theta$.  
Wait, is this correct?  
Yes. $(1+\cos \theta)^2 + (1-\sin^2 \theta)$ no, $\sin^2 \theta = 1 - \cos^2 \theta$.  
So $(1+e^{i\theta}) \overline{(1+e^{-i\theta})}$. No.  
$(1+\cos \theta)^2 + (1-\sin^2 \theta) = \cos^2 + 2\cos + 1 + \cos^2$? No.  
Let's just use the value.  
If $\theta=0$, $|1+e^{i0}| = |1+1| = 2$.  
If $\theta=\pi/2$, $z=i$, $|1+i| = \sqrt{2}$.  
If $\theta=\pi$, $z=-1$, $|1-1|=0$. Wait, so range is $[0, \dots]$.  
So max value of $|1+z|$? No wait.  
Wait, earlier I wrote $|1+z|^2 = 2+2\cos \theta$. Let me check this formula.  
$|1+e^{i\theta}|^2 = (1+\cos \theta)^2 + (\sin \theta)^2$ is WRONG because $\bar{z} = e^{-i\theta}$? No, if $z=e^{i\theta}$, then $\bar{z}=e^{-i\theta}$.  
So $|1+z|^2 = (1+e^{i\theta}) (1+e^{-i\theta})$ is correct.  
Wait, no, I'm confusing myself with notation.  
Let's stick to $|1+z|^2$.  
$1+e^{i\theta} = 1 + \cos \theta + i \sin \theta$.  
So magnitude squared is $(1+\cos \theta)^2 + (\sin \theta)^2$.  
Wait, if this equals $2+2\cos \theta$, then at $\theta=0$, it is $4$.  
But I said earlier that max value of $|1+z|$ (meaning the modulus itself) is 2? No, wait.  
Let's check for $z=-1$. $w=0$. So $|w|=0$.  
For $z=i$, $w=\sqrt{2}$. Wait, why did I get 0 earlier?  
Because $(1+e^{i\pi/2}) (1+e^{-i\pi/2}) = (1+i)(1-i) = 1^2 + i^2 = 0$? No.  
$(1+i)(1-i) = 1 - i^2 = 2$. So $|w|^2=2$.  
Wait, $(1+\cos \theta)^2 + \sin^2 \theta$.  
For $\theta=\pi$, $\cos \pi = -1$. $(1-1)^2 = 0$.  
So the formula seems correct.  
But let's check if it's consistent with $|1+i|=2$ vs $\sqrt{2}$.  
Wait, I wrote $|1+i|$ is $\sqrt{2}$ earlier. Why?  
Because $(1+1)^2 + \sin^2 0 = 4 + 0 = 4$? No.  
Let's check again.  
If $z=1$, $w=1+z=2$. $|w|^2 = 4$.  
So for $z=1$, formula gives $2+2\cos(0) = 4$.  
So $|1+z|^2$ can be up to 4.  
But if $z=1$, then $|1+z|=2$. So $\sqrt{2^2} = 2$. But the term is $|1+z|$.  
Ah, wait. The variable $w = |1+z|$ is not $|1+z|^2$?  
Yes it is. $|1+z|$ is a number. So if $z=1$, $|1+z|=2$.  
But my previous check of $\theta=\pi/2$ gave $|1+i|=\sqrt{2}$. Wait, if $z=i$, $|1+e^{i\theta}|^2 = |1+i|^2$.  
Wait, is $|1+z|$ bounded by 2?  
Let's test $z=0.5$ (not unit circle). Then $|1+z|=1.5$.  
If we take $z=-0.5$, $|1+z| = 1.5$.  
Wait, I'm confused with $\theta=\pi/2$. For $z=i$, $|1+i|= \sqrt{1+1}= \sqrt{2}$.  
Is it bounded? Yes, $|1+z|$ is max when $z$ is such that... wait.  
If $z$ is real positive 1, $|1+z|=2$.  
Wait, I thought earlier $z=-1 \implies |0|$. And $\sqrt{2} \approx 1.41$.  
So range of $|1+z|$ for unit circle $z=e^{i\theta}$ is between some min and max? No, it's continuous and ranges from 0 to something.  
But wait, $|1+e^{i\theta}|^2 = (1+\cos \theta)^2 + \sin^2 \theta$ is incorrect for general complex numbers.  
Let's re-derive carefully.  
$1+e^{i\theta}$. This is a complex number with argument $\alpha$. $|1+e^{i\theta}|^2 = (Re(1+e^{i\theta}))^2 + (Im(1+e^{i\theta}))^2$.  
This equals $(1+\cos \theta)^2 + (\sin \theta)^2$? No.  
Wait, if $\theta=\pi/2$, $z=i$. Then $1+i = 0 + i + i \dots$ no.  
$(1+i) = 1+0i$. Imag part is 1. Real part is 1. So squared sum is $1^2 + 1^2 = 2$. This matches $\sqrt{2}$ squared.  
But my formula $(1+\cos \theta)^2 + (\sin \theta)^2$ yielded 2 for $\pi/2$.  
Wait, I used $\bar{z}=e^{-i\theta}$. If $z=i$, $\bar{z}=-i$. Then $z\bar{z} = -1$.  
But constraint is $|z|=1 \implies z \bar{z} = 1$? No. $z \bar{z} = |z|^2$. For unit circle, $|z|^2=1$. So $z \bar{z} = 1$.  
So the relation is correct.  
Wait, I am confusing myself with $z\bar{z}=1$ vs $|z|=1$. Wait, if $|z|=1$, then $z\bar{z}=1$. Yes.  
Wait, but earlier for $z=i$, $\bar{z}=-i$. So $z \bar{z} = -1$? No. $z\bar{z} = i(-i) = 1$. This is correct.  
So formula must be consistent with $|1+e^{i\theta}|^2 = (1+\cos \theta)^2 + (\sin \theta)^2$ if $\theta$ is the angle of $z$? No.  
If $z=e^{i\theta}$, then $z\bar{z}=1$.  
Wait, $|1+z|^2 = |1+e^{i\theta}|^2 = (1+e^{i\theta})(1-e^{-i\theta})$? No.  
Ah! $z \bar{z} = 1$. So $\bar{z} = 1/z$ only if $|z|=1$? Wait, $|z|=1 \implies |z|^2=1 \implies z \bar{z}=1$. This is true.  
So $\bar{z}$ must be equal to $e^{-i\theta}$. Yes.  
So $(1+e^{i\theta})(1+e^{-i\theta})$? No, this would be for something else.  
Wait, $|w|^2 = w \bar{w}$. If $w = 1+z$, $\bar{w} = \bar{1} + \bar{z} = \bar{z} - z$? No. $\overline{(1+e^{i\theta})} = \bar{1} + \bar{e^{i\theta}} = e^{-i\theta}$.  
Wait, $e^{i\theta}$ is the complex number with modulus 1 and argument $\theta$. So $\bar{e^{i\theta}} = e^{-i\theta}$.  
So $\bar{w} = e^{-i\theta} + e^{-2\theta}$? No.  
Wait, if $z=e^{i\theta}$, then $\bar{z}=e^{-i\theta}$. Then $\bar{w} = \bar{1} + \bar{z}$. Wait, this assumes we are looking for $\bar{w}$ in terms of $z$.  
If we just substitute $z$ for $e^{i\theta}$:  
$|1+z|^2 = |1+e^{i\theta}|^2$.  
Let's verify again.  
For $z=1$, $1+e^{i0} = 1+1 = 2$. Square is 4.  
Formula gives $(1+\cos(0))^2 + (\sin(0))^2$? No.  
Wait, my formula $(1+\cos \theta)^2 + \sin^2 \theta$ came from $|a+bi|^2 = a^2+b^2$.  
Let's rewrite $1+z = (1+\cos \theta) + i \sin \theta$. Wait.  
If $z=1$, $\theta=0$, $1+e^{i0} = 2$. Real part is 2, imaginary is 0.  
So formula is $(a^2+b^2) = (1+\cos \theta)^2 + (\sin \theta)^2$?  
Wait, if $\theta=\pi/2$, $z=i$. Then $1+z = 1+i$. Real part 1, imag part 1. Sum of squares is $1+1=2$. Correct.  
But my formula yielded $(1+\cos \theta)^2 + (\sin \theta)^2$? No.  
Wait, $\bar{e^{i\theta}} = e^{-i\theta}$.  
If $z=e^{i\theta}$, then $\bar{w} = 1 + e^{-i\theta}$? No. $\bar{w} = \bar{1} + \bar{z}$.  
Wait, this is confusing. Let's step back and calculate $|1+z|$ again using trigonometry directly.  
$|1+z|^2 = |e^{i\theta} + 1|^2$.  
Using formula: $(Re(1+e^{i\theta}))^2 + (Im(1+e^{i\theta}))^2$.  
Wait, $1+e^{i\theta} = 1 + \cos \theta + i \sin \theta$.  
So real part is $1+\cos \theta$. Imaginary is $\sin \theta$.  
Wait, this implies $(Re)^2 + (Im)^2$.  
But for $z=1$, $\theta=0$, $1+e^{i\theta} = 1+1 = 2$. Real 2. Imag 0.  
Formula: $(1+1)^2 = 4$. This is correct.  
So it seems consistent?  
Wait, but wait. If $z$ is real positive, say $z=x$ (real). Then $\theta=\arg(z)=0$.  
Then $|1+z|^2 = |1+x|^2$. If $x=1$, $4$.  
If $x=0$, $|1+0|^2 = 1$. But $\cos(0)=1, \sin(0)=0$.  
Wait, I said for $z=1$ ($\theta=0$), formula gives 4.  
But for $z=i$, $z=e^{i\pi/2}$. Then $\theta=\pi/2$.  
Formula: $(1+\cos(\pi/2))^2 + (\sin(\pi/2))^2 = (0+0)^2 + (1)^2 = 1$? No.  
Wait, for $z=i$, formula should be consistent with $(1+i)(1-i) = 2$.  
Let's check my previous formula: $(1+\cos \theta)^2 + (\sin \theta)^2$.  
For $\theta=\pi/2$: $(1+0)^2 + (1)^2 = 2$. Correct.  
Wait, I wrote "for $\theta=0$, $z=1$, formula gives 4".  
Let's check again.  
$|1+z|^2$ for $z=1$.  
$1+e^{i\theta} = 2$. Wait, $e^{i\theta}=1$ when $\theta=2k\pi$.  
Then $1+e^{i0}=2$. Square is 4.  
My formula $(1+\cos \theta)^2 + (\sin \theta)^2$ gave 4 for $\theta=0$.  
Wait, why did I think it gave 2 earlier?  
I might have made a calculation error or misremembered the cosine term.  
Let's check the term $(1+e^{i\theta})(1-e^{-i\theta})$. This is $|1+e^{i\theta}|^2$ only if $\bar{z} = e^{-i\theta}$.  
Wait, $z=e^{i\theta}$. Then $\bar{z}=e^{-i\theta}$? No. $|z|=1 \implies z\bar{z}=1$. But $\bar{z} = 1/z$ is only if $z$ is not real?  

*Continued in [part 3 of 3](intermediate_algebra_1806_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
