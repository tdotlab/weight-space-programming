# test/intermediate_algebra/1806.json, part 3 of 3

[Previous part](intermediate_algebra_1806_p2.md) · [Start](intermediate_algebra_1806.md)

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
