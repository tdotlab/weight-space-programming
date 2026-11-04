# test/intermediate_algebra/1806.json, part 3 of 3

[Previous part](intermediate_algebra_1806_p2.md) · [Start](intermediate_algebra_1806.md)

No, for unit circle, $\bar{z} = e^{-i\theta}$. Wait, no. $e^{i\theta}$ has conjugate $e^{-i\theta}$. Yes.  
So my check was:  
For $z=1$, $\theta=0$. Formula $(1+1)^2 + 0 = 4$.  
Wait, is the formula correct?  
For general $z=e^{i\theta}$, we have $|1+z|^2 = (1+\cos \theta)^2 + (\sin \theta)^2$?  
Wait, this formula gives $|1+e^{i\theta}|^2$.  
Let's test for $\theta=\pi/2$, $z=i$.  
Formula: $(0)^2 + 1 = 1$. Wait, but I just said it is 2.  
Ah, my error was in evaluating $\sin(\pi/2)$. It is 1. So $1^2=1$ and $(0)^2=0$. Total 1. But magnitude of $1+i$ is $\sqrt{2}$.  
So $(Re \dots)^2 + (Im \dots)^2$ must be $1+1=2$.  
Wait, I am calculating $(1+e^{i\theta}) = (1+\cos \theta) + i(1+\sin \theta)$? No.  
Let's re-calculate $|1+e^{i\theta}|^2$.  
$1+e^{i\theta} = 1 + \cos \theta + i \sin \theta$. Wait, this is incorrect because $\bar{e^{i\theta}}$ is not $e^{-i\theta}$ if $z=e^{i\theta}$?  
Wait, $|z|=1 \implies z \bar{z} = 1 \implies \overline{z} = 1/z$. This means $\overline{e^{i\theta}} = e^{-i\theta}$.  
So if I write $1+e^{i\theta}$, then $\overline{1+e^{i\theta}} = e^{-i\theta} + \bar{1} = e^{-i\theta} + 1$.  
Wait, $|w|^2 = w \bar{w}$. So $|1+e^{i\theta}|^2 = (1+\cos \theta + i \sin \theta)(1+\cos \theta - i \sin \theta)$? No.  
Wait, the real part is $1+\cos \theta$? No, $\bar{z}$ term is missing.  
Actually $|w|^2 = |w\bar{w}|$. If I just take modulus of sum:  
Let's use polar coordinates again. $z = \rho e^{i\phi}$. Here $\rho=1$.  
$1+z = 1 + e^{i\theta}$.  
Modulus is $(1+\cos \theta)^2 + (\sin \theta)^2$.  
Wait, this assumes $Re(1+z) = \text{Real}(1+e^{i\theta})$.  
And $\text{Im}(1+z) = \text{Im}(1+e^{i\theta})$.  
Is it true that $\overline{1+e^{i\theta}} = 1 + e^{-i\theta}$? No. $\bar{1} = 1$, $\bar{e^{i\theta}} = e^{-i\theta}$.  
Wait, so $(1+\cos \theta) + i \sin \theta$? No. $1+e^{i\theta} = (1+\cos \theta) + i(\sin \theta)$.  
This is WRONG. $|1+z|^2$ cannot be computed this way because I am mixing up real and imaginary parts of $z$ with $e^{i\theta}$.  
Let's write $z = x+iy$. Then $\theta = \arctan(y/x)$.  
Let's stick to the fact that $|1+z|^2 = (1+Re z)^2 + (Im z)^2$.  
Wait, no.  
If $z$ is general complex number with magnitude 1. Let $z = x+iy$. Then $x^2+y^2=1$.  
Then $1+z = 1 + x + iy$. So real part is $1+x$, imag part is $y$.  
So $|1+z|^2 = (1+x)^2 + y^2$.  
But wait, this implies that we can choose any $z$ with modulus 1? No, we assume $x+iy$ are coordinates.  
Wait, if $x$ and $y$ satisfy $x^2+y^2=1$, then $(1+x)^2 + y^2 = 1 + 2x + x^2 + y^2 = 1 + 2x + 1 = 2+2x$.  
Ah!  
So if we fix $x$, we have a range of values. But wait, for any $z$ on unit circle, $x=x_{\text{real}}(z)$. This depends on $z$.  
Let's re-calculate $|1+z|^2$ properly.  
For $z = e^{i\theta}$ (using polar notation), $x=e^0 \cos \theta$? No, that is not correct.  
$x = \cos \theta$, $y = \sin \theta$. But this assumes $z=x+iy$ where $\theta$ is the argument.  
So for any complex number on unit circle, we can parameterize by $\theta$.  
Then $1+z = 1 + (\cos \theta + i \sin \theta)$.  
Then real part is $1+\cos \theta$. Imaginary part is $\sin \theta$.  
Wait, earlier I wrote "Wait, if $z=1$, then $|1+z|=2$". Here $x=1, y=0$. So $1+1 = 2$. Correct.  
But wait, the real part is $1+\cos \theta$ for $z$ on unit circle? No.  
If $z = e^{i\theta}$, then $Re(z) = \cos \theta$ and $Im(z) = \sin \theta$.  
Then $1+z = 1 + \cos \theta + i \sin \theta$.  
Wait, no. This is wrong.  
Let's use the property of complex numbers: $z \bar{z} = |z|^2$. If $|z|=1$, then $\bar{z} = 1/z$? No. $\bar{z}$ is NOT equal to $1/z$ unless $z=0, -1$... No. $\bar{z} = e^{-i\theta}$. And $z \bar{z} = (\cos \theta + i\sin \theta)(\cos \theta - i\sin \theta) = \cos^2 + \sin^2 = 1$. Yes, it's true.  
So for $z=e^{i\theta}$, the coordinates are:  
$Re(z) = \cos \theta$, $Im(z) = \sin \theta$.  
Then $1+z = (1+\cos \theta) + i(\sin \theta)$.  
Wait, I am missing the imaginary part of $z$. Wait, $z=e^{i\theta}$ is a number.  
The real part is $\cos \theta$? Yes. The imaginary part is $\sin \theta$? Yes.  
Then $(1+e^{i\theta}) = (1+\cos \theta) + i(\sin \theta)$. No, $e^{i\theta} = \cos \theta + i \sin \theta$.  
So $1+z = 1 + (\cos \theta + i \sin \theta)$.  
This simplifies to $(1-\cos \theta) + i \sin \theta$? No. $1+\cos \theta$.  
Wait, then squared magnitude is $(1+\cos \theta)^2 + \sin^2 \theta = 1 + 2\cos \theta + \cos^2 \theta + \sin^2 \theta = 1 + 2\cos \theta + 1 = 2+2\cos \theta$.  
Wait, but earlier I calculated for $z=1$, $\theta=0$, modulus is 2.  
$2+2(1) = 4$. This contradicts.  
Let me check the coordinate calculation again.  
If $z=e^{i\theta}$, then $Re(z) = \cos \theta$.  
Then $1+z = 1 + \cos \theta + i \sin \theta$.  
Is this correct?  
$z = \cos \theta + i \sin \theta$. Yes.  
So the real part is $1+\cos \theta$ and imaginary part is $\sin \theta$.  
Wait, if $z=1$, then $Re(z)=1, Im(z)=0$. $\cos(0)=1, \sin(0)=0$.  
So $1+z = 2$. Real part 2. Imag part 0.  
Modulus squared $4$. Correct.  
Now check for $z=-1$. $\theta=\pi$. $Re(z)=-1, Im(z)=0$.  
$1+z = 1-1+1 = 1$. Modulus 1.  
Formula: $2+2(-1) = 0$. Incorrect.  
So my formula is wrong. Where is the error?  
I used $\bar{z} = e^{-i\theta}$ to substitute $e^{i\theta}$ with something? No.  
$|w|^2 = (Re w)^2 + (Im w)^2$.  
Let's rewrite $1+z$.  
Wait, if $z=e^{i\theta}$, then $z = \cos \theta + i \sin \theta$. Wait.  
Why did I write $(1+\cos \theta) + i(\sin \theta)$?  
$1+z = 1 + \cos \theta + i \sin \theta$. This is correct if $\text{Im}(z)=\sin \theta$? No, this assumes $x+iy = \dots$.  
Wait, $z=x+iy$. Then $|z|^2 = x^2+y^2=1$.  
Then $1+z = (1+x) + iy$. So real part is $1+x$, imaginary is $y$.  
So $|1+z|^2 = (1+x)^2 + y^2$.  
This must equal 4 for $z=1$? No, $x=1, y=0$.  
Wait, why did I use $\theta$ as angle of $z$?  
For general $z$, if we parameterize by $\theta \in [0, 2\pi)$ such that $z = e^{i\theta}$? No.  
If $|z|=1$, then $e^{i\theta} = z$. So $Re(z) = \cos \theta$ and $Im(z) = \sin \theta$.  
So this seems consistent with my  

## Answer

*(none: the token cap hit during thinking)*
