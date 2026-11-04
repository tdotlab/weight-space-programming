# test/intermediate_algebra/1806.json, part 2 of 3

[Previous part](intermediate_algebra_1806.md)

$T_2^2 = |1 - z + z^2|^2 = |(-z)(1-z) + 1|^2$? No.  
Let's use polar coordinates in the expression term.  
Let $u = 1$.  
Then we are maximizing $|u+z|$ subject to $|z|=1$ and minimizing/maximizing something related?  
No, $T_2 = |u - v z^2 + \dots|$ ? No.  
Let's factor out the constant term from the second modulus.  
We can think of this as a geometric optimization problem on the unit circle in 2D.  
We want to maximize $\sqrt{(1+x)^2+y^2} + |1-x+iyz^2 - \dots|$? No.  
Let's use coordinates $(x,y)$. The constraints are $x^2+y^2=1$ for both points.  
So we have the sum of distances from 0 to $w_1$ and 0 to $w_2$ where $w_1 = 1+z$ and $w_2 = z^2-z+1$ ? No.  

Let's rewrite $B = |z^3-1| / \dots$? No.  
Let's try to express $T_2$ as the distance of some points.  
Notice that $1 - z + z^2$ is related to the polynomial with roots $\omega, \bar{\omega}$.  
Let's look at the expression for $z=e^{i\theta}$ in terms of vectors on unit circle.  
We want to maximize $\sqrt{(1+\cos\theta)^2 + \sin^2\theta} + |1 - z + z^2|$.  
This is equivalent to maximizing $A+B$ where $A, B$ are magnitudes of complex numbers formed by $z$ itself.  
The modulus of the second term is $\le 1+z+z^2$? No.  

Let's check the maximum possible value for a single term.  
We know that on the unit circle, we can have terms as far from each other?  
Actually, look at the geometry in the complex plane.  
We are considering points $P_1 = z$, $P_2 = 1-z+z^2$ ? No, $P_2 = 1 - z + z^2$.  
Let's re-examine $|1-z+z^2|$.  
The expression inside is $1 - (z-z) + \dots$  
Maybe factor out $z$? $1 - z(1+z)$. No.  
Is it possible to write $|1-z+z^2|$ in terms of $\sqrt{...}$?  
Let's try substituting specific angles.  
We want to maximize $f(\theta) = \sqrt{2+2\cos\theta} + |1 - e^{i\theta} + e^{i2\theta}|$.  
We already tested a few angles:  
$\theta=0 \implies z=1$, sum=3. (Here $\cos \theta = 1$)  
$\theta=\pi/6 \implies z=e^{i\pi/6}$, $x=1/2, y=\sqrt{3}/2$.  
Then $A = \sqrt{(1+1/2)^2 + (\sqrt{3}/2)^2} = \sqrt{9/4 + 3/4} = \sqrt{12/4} = \sqrt{3} \approx 1.732$?  
Let's recalculate $A^2$.  
$(1+1/2)^2 + (\sqrt{3}/2)^2 = (3/2)^2 + 3/4 = 9/4 + 3/4 = 12/4 = 3$. So $A = \sqrt{3}$.  
For $B$, $z=e^{i\pi/6}$.  
$z^2 = e^{i\pi/3} = 1/2 + i\sqrt{3}/2$.  
$1 - z + z^2 = 1 - (1/2 + i\sqrt{3}/2) + (-1/2 + i\sqrt{3}/2) = 1 - 1 - i\sqrt{3} = -i\sqrt{3}$?  
No, $-z$ term. $1 - e^{i\pi/6}$. $e^{i\pi/6} = \frac{1+i}{\sqrt{3}}$. No.  
$e^{i\pi/6} = \cos(\pi/6) + i\sin(\pi/6) = \frac{\sqrt{3}}{2} + \frac{i}{2}$.  
So $1-z+z^2 = 1 - (\frac{\sqrt{3}}{2} + \frac{i}{2}) + (-\frac{\sqrt{3}}{2} - \frac{i}{2})$? No, $z^2 = e^{i\pi/3} = \frac{1+\sqrt{3}i}{2}$?  
$e^{i\pi/3} = \cos(\pi/3) + i\sin(\pi/3) = 1/2 + i\sqrt{3}/2$.  
So $z^2 - z + 1$ is $0$ at $\theta=\dots$ no.  
Let's recalculate $B$ for $\theta=\pi/6$.  
$1-z+z^2 = 1 - (\frac{\sqrt{3}}{2} + \frac{i}{2}) + (-\frac{\sqrt{3}}{2} + \frac{i\sqrt{3}}{2})$? No.  
Wait, $z = e^{i\pi/6}$. So $\cos(\pi/6) = \frac{\sqrt{3}}{2}$, $\sin(\pi/6)=1/2$.  
Then $z^2 = e^{i2\pi/3} = -1/2 + i\sqrt{3}/2$? No.  
$2\pi/3$ is $e^{i(2\pi/3)}$.  
So $z=e^{i\theta}$, $z^2=e^{i2\theta}$.  
So for $\theta=\pi/6$, $z^2 = e^{i\pi/3} = \frac{1}{2} + i\frac{\sqrt{3}}{2}$.  
Then $1-z+z^2 = 1 - (\frac{\sqrt{3}}{2} + \frac{i}{2}) + (\frac{1}{2} + i\frac{\sqrt{3}}{2}) = 1 - \frac{\sqrt{3}}{2} - \frac{i}{2} + \frac{1}{2} + i\frac{\sqrt{3}}{2}$.  
Real part: $1-1/2 - \frac{\sqrt{3}}{2} + \frac{\sqrt{3}}{2}$? No.  
$1 - \frac{\sqrt{3}}{2} + \frac{1}{2} = 1 - 0.5\sqrt{3}$. Imaginary part: $-1/2 + \sqrt{3}/2 = (\sqrt{3}-1)/2$.  
This term is not necessarily real or zero.  
Let's calculate modulus.  
Modulus squared: $(1 - \frac{\sqrt{3}}{2})^2 + ((\sqrt{3}-1)/2)^2$? No, $(-z)$ and ($z^2$) have same imaginary part sign?  
$-z = -\frac{\sqrt{3}}{2} - i/2$.  
$z^2 = \frac{1}{2} + i\frac{\sqrt{3}}{2}$.  
Sum real: $1 - \frac{\sqrt{3}}{2} + 1/2 = 3/2 - \frac{\sqrt{3}}{2} = \frac{3-\sqrt{3}}{2}$.  
Sum imag: $-1/2 + \frac{\sqrt{3}}{2} = \frac{\sqrt{3}-1}{2}$.  
So magnitude squared is $\frac{1}{4}( (3-\sqrt{3})^2 + (\sqrt{3}-1)^2 ) = \frac{1}{4} (9 - 6\sqrt{3} + 3 + 3 - 2\sqrt{3} + 1)$.  
$= \frac{1}{4} (16 - 8\sqrt{3}) = 4 - 2\sqrt{3}$.  
This is approx $4 - 3.46 = 0.54$.  
So $|B| = \sqrt{4-2\sqrt{3}}$. This is small.  

Let's re-evaluate the value for $\theta$ near 1 radian? No, let's try a general approach.  
We are maximizing $f(z) = |1+z| + |z^2-z+1|$.  
Let's consider the geometric interpretation of this.  
The term $T_2 = z^2-z+1 = (z-1/2)^2 - 3/4$? No.  
Roots are $\frac{1 \pm i\sqrt{3}}{2}$. The value is related to these roots.  
If we consider the triangle formed by $0$, $1+z$, and $1-z-z^2$? No.  

Let's rewrite the second term in terms of polar angles.  
We have $\theta$.  
$T_2 = |1 - z(1+z)|$. Let's see if we can bound it.  
Since $|z|=1$, we can write $|z| \le 1$.  
So $T_2 \le |1| + |-z+z^2| = 1+|-i\sqrt{3}|$? No, let's use the triangle inequality:  
$|A+B| \le |A|+|B|$. Here $A=1, B=z(1-z)$?  
So $|z^2-z+1| = |z^2-z+z(z-1)| + |-z+z|$? No.  
Let's just use the triangle inequality properly:  
$|1 - z + z^2| \le 1 + |-z + z^2|$.  
We want to bound $|-z + z^2| = |z(1-z)|$? No, $|z^2| = 1$.  
So $|1 - z + z^2| \le 1 + |z(z-1)|$? No.  
Actually $|A+B| \le |A|+|B|$. So we need to find the best lower bound for $|z-z^2|$ or similar.  
However, note that $1 - z + z^2 = 1 - z(1-z)$.  
We know that for any unit vector $z$, the quantity $1 - \cos\theta + i\sin\theta$ has modulus.  
Let's use the polar form of the roots again.  
The maximum value of $|w|$ on the circle $|w-1|=1$? No, we have the circle $|z|=1$.  
The expression is $|1+z| + |z^2-z+1|$.  
Let's define vectors $\mathbf{u} = 1+z$, $\mathbf{v} = z^2 - z + 1$.  
This doesn't simplify to standard unit circle.  

Let's go back to basic algebraic inequality on $T_2$.  
$T_2^2 = (1-z+z^2)(\overline{1-z+z^2}) = |1-z+z^2|^2$.  
We can expand this as $(1-\bar{z}+z^2)\dots$? No.  
Consider the function $g(\theta) = \sqrt{2+2\cos\theta} + |1 - e^{i\theta} + e^{i2\theta}|$.  
Is it possible that the maximum is attained at $\theta = \pi/3$?  
Let's check $\theta=\pi/3$ again.  
$\cos(\pi/3) = 1/2$. $z=e^{i\pi/3}$.  
$T_1^2 = (1+1/2)^2 + (\sqrt{3}/2)^2 = 9/4 + 3/4 = 3$. So $|T_1|= \sqrt{3}$.  
$T_2$: $z=e^{i\pi/3}$, $\cos=1/2, \sin=\sqrt{3}/2$.  
$z^2 = e^{i2\pi/3} = \cos(120^\circ) + i\sin(120^\circ) = -1/2 + i\sqrt{3}/2$.  
$T_2 = 1 - z + z^2 = 1 - (\frac{\sqrt{3}}{2} + i\frac{1}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})$.  
Real part: $1 - 0.5(\sqrt{3}) + 0.5 = 1.5 - \frac{\sqrt{3}}{2}$? No, this is wrong.  
$1 - (\frac{\sqrt{3}}{2} + i\frac{1}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})$.  
Real parts: $1 - \frac{\sqrt{3}}{2} - \frac{1}{2} = \frac{1-\sqrt{3}}{2}$. No. $1 - 0.5(\sqrt{3}) + 0.5$?  
Let's check: $\text{Re}(1) = 1$. $\text{Re}(z^2)$ is real part of $-1/2 + i\sqrt{3}/2$.  
So Real(T2) = $1 - \cos\theta + \sin(2\theta)$? No, that's not true.  
$1 - z + z^2$. $\text{Re}(1-z+z^2) = 1 - x + \cos(2\theta)$.  
$\cos(\theta) = 1/2$. $x = 1/2$. So Real part = $1 - 0.5 + (-1/2)$? No.  
$z^2$ has real part $\cos(2\theta) = \cos(\pi/3) = 1/2$.  
So Real(T2) is $1 - x + (1/2)$ if we are using polar form. But $x$ is the real part of $z$.  
If $z=e^{i\pi/3}$, then $x = \cos(\pi/3) = 1/2$, $y = \sin(\pi/3) = \sqrt{3}/2$.  
Then $1 - z + z^2 = (1 - x + y)$? No.  
Let's just use complex arithmetic.  
$z = \frac{1}{2} + i\frac{\sqrt{3}}{2}$.  
$z^2 = \cos(\pi/3) + i\sin(\pi/3)$?  
No. $z = e^{i2\pi/6} = e^{i\pi/3}$. Wait, $\theta=\pi/6$.  
Then $z=e^{i\pi/6}$. Real part $\frac{\sqrt{3}}{2}$. Imaginary part $\frac{1}{2}$.  
$z^2 = e^{i\pi/3} = \cos(\pi/3) + i\sin(\pi/3) = 1/2 + i\frac{\sqrt{3}}{2}$.  
So $1 - z + z^2 = 1 - (\frac{\sqrt{3}}{2}) + (-i\frac{\sqrt{3}}{2})$? No.  
Real part: $1 - \frac{\sqrt{3}}{2} + 0.5$. So $\frac{3-\sqrt{3}}{2}$?  
No, wait. I think the previous calculation of magnitude was wrong because I assumed signs.  
Let's re-calculate carefully.  
$z = e^{i\pi/6}$. Then $x=\cos(\pi/6)=\frac{\sqrt{3}}{2}$, $y=\sin(\pi/6)=\frac{1}{2}$.  
Then $T_2 = 1 - z + z^2 = 1 - (\frac{\sqrt{3}}{2} + i\frac{1}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})$? No, this is incorrect.  
$z^2$ has $\cos(2\pi/6) = \cos(\pi/3)=1/2$ and $\sin(2\pi/6)=\sin(\pi/3)=\sqrt{3}/2$.  
So $T_2 = (1 - 1/2) + (-i/2 + i\sqrt{3}/2)$? No.  
The coefficients are:  
Real part of $T_2$: $1 - (\frac{\sqrt{3}}{2}) - \frac{1}{2}$. This is $\frac{3-\sqrt{3}}{2}$.  
Imaginary part of $T_2$: $-0 + \frac{\sqrt{3}}{2}$? No.  
$-z = -(\frac{\sqrt{3}}{2} + i\frac{1}{2})$. Imaginary part is $-\frac{1}{2}$.  
$+z^2 = (\frac{1}{2} + i\frac{\sqrt{3}}{2})$. Imaginary part is $\frac{\sqrt{3}}{2}$.  
Sum of imaginary parts: $-0.5 + 0.866 = 0.366 > 0$.  
Sum of real parts: $1 - 0.866 - 0.5 = 0.5(1-2) + \dots$? No.  
Real part sum: $1 - 0.866 - 0.5$. This is $\frac{3-\sqrt{3}}{2} \approx 0.16$.  
So $T_2 \approx 0.16 + i0.37$.  
The magnitude of $T_2$ seems small (maybe less than 2).  

Wait, did I calculate the imaginary part correctly?  
$-z = -\frac{\sqrt{3}}{2} - i\frac{1}{2}$. Imaginary part is $-0.5$. Correct.  
$z^2 = \cos(2\pi/6) + i\sin(2\pi/6)$? No, wait. $z=e^{i\theta}$ where $\theta=\pi/6$. So $z^2=e^{i\pi}e^{i2\pi/3}$? No.  
$z = e^{i\pi/6}$. Then $z^2 = e^{i2\pi/6} = e^{i\pi/3} = \frac{1}{2} + i\frac{\sqrt{3}}{2}$. Correct.  
Then the imaginary part of $z^2$ is $\sqrt{3}/2 \approx 0.866$.  
The real part of $z^2$ is $0.5$.  
Imaginary part of $-z$ is $-1/2 = -0.5$. Real part is $\frac{\sqrt{3}}{2} \approx 0.866$. No, imag of $-z$ is $-y$ if we just take vector subtraction.  
So imaginary part is $-y + z_{y}$.  
$T_2$ has real part: $(1+x) + y^2 - (x + y) = 1+x+y^2-x-y$? No.  
Let's use the expansion for $|1-z+z^2|$:  
If we assume it is small, then maybe my assumption about magnitude is too big.  
However, the maximum value of a sum involves checking the boundaries.  

Let's try to maximize numerically.  
Consider $\theta$ such that $T_1$ and $T_2$ align or something?  
Maybe max occurs at $\theta = \pi$. Then $z=-1$.  
Then $A=0$ (since $|1-1|=0$, but it's $\sqrt{(1+(-1))^2} = 0$).  
$B = |1 - (-1) + (-1)^2| = |3| = \sqrt{9} = 3$.  
Sum = 3.  
Is this a local maximum? No, if $A$ is large (2), and $B$ is small, sum can be large.  
At $\theta = \pi/2$, $z=i$. $A=\sqrt{2}$.  
$T_2 = |1-i+(-1)| = |-i| = 1$. Sum $\approx 2.414$.  
If we try to increase, maybe at $\theta = -\pi/2$? Same as $\pi/2$.  
What if $z=i$, sum is $\sqrt{2}+1 \approx 2.414$.  
Let's check $z=0$? No $|z|=1$.  
Is there any point where $T_2$ is very large, or $A$ is small?  
We found at $z=-1$, sum is 3. At $\theta=\pi/2$, sum is $\approx 2.41$. At $\theta=0$, sum is 3.  
At $\theta=\pi/6$, we got something smaller.  

Let's re-evaluate the function for $z=e^{i\theta}$.  
We are looking for $M = \max_z (|1+z| + |z^2-z+1|)$.  
Let's express everything using polar coordinates $\phi$ such that $1+z = R_1 e^{i\alpha}$? No.  
Let $T_1(\theta) = |1+z|$ and $T_2(\theta) = |1-z+z^2|$.  
We need to maximize $f(\theta)$.  
$f(0) = 2+1 = 3$. (Since $\cos(0)=1$).  
$f(\pi/2) = \sqrt{2} + 1 \approx 2.414$.  
$f(\pi/3)$? $z=e^{i\pi/3}$, $x=1/2, y=\sqrt{3}/2$.  
$A = \sqrt{(3/2)^2 + (\sqrt{3}/2)^2} = \sqrt{9/4+3/4} = \sqrt{3} \approx 1.732$.  
$B = |1 - e^{i\pi/3} + e^{i2\pi/3}|$? No, $z^2=z^2$ is just $e^{i\theta}$.  
Let's recompute $B(\pi/3)$. $T_2(0.5) = |1 - (\frac{\sqrt{3}}{2}) + (-\frac{1}{2} + i\frac{\sqrt{3}}{2})|$. No, this was for $\theta=\pi/6$.  
Let's do it properly.  
$z = \cos(\pi/6) + i\sin(\pi/6)$ (No, angle $\pi/6$).  
Then $B(0) = 1 - e^{i\pi/6} + e^{i\pi/3}$? No, this is $\theta$.  
If $z=e^{i\theta}$:  
$A(\theta) = \sqrt{1+2\cos\theta}$.  
$B(\theta) = |1 - z(1+z)|$? No.  
The term is $|1-z+z^2|$.  
Let's check if there is an identity for this.  
Notice that $\text{Re}(1-z+z^2)$ and $\text{Im}(1-z+z^2)$ might be involved.  
Is it possible to relate this to a geometric problem?  
Consider points $P_1 = 1$, $P_2 = z$, $P_3 = z^2$. We are measuring distances from origin? No.  
Actually, let's try to use the property that on the unit circle $|1+z|^2 + |1-z+z^2|^2$ might be minimized/maximized?  
Or maybe $T_1 + T_2 \le 3\sqrt{...}$.  

Let's try substituting specific values from the options (like angles).  
We found $\theta=0 \implies z=1$, sum = 3.  
$\theta=\pi/2 \implies z=i$, sum $\approx 2.414$.  
$\theta=\pi \implies z=-1$, sum = 3.  
What if we take a value where the modulus is small but real part is large?  
For $A$ to be small, we need $\cos\theta$ close to $-1$ (so $z \approx -1$) or close to 0 ($z=0$ not allowed).  
If $z \to -1$, $T_1 \to 0$. But $T_2 \to 3$. Sum $\to 3$.  
So sum is 3.  
At $z=i$, sum is 2.414? Let's check this again.  
$A = |1+i| = \sqrt{1^2+1^2} = \sqrt{2}$.  
$B = |-i| = 1$.  
Sum $\approx 2.414$.  
Is it possible to get a larger value?  
Let's check if $z$ can be such that $\cos\theta$ is maximized for $T_1$, i.e., $\theta \to 0$ ($z=1$), sum = 3.  
At $\theta=0$, sum=3.  
What about at $\theta=-\pi/2$? Same as $\pi/2$.  
Is there any $\theta$ where $A$ is small? No, min A is 0 (at $z=-1$).  
At $z=-1$, sum = 3.  
So we have a range of values between 3 and $\approx 2.41$.  
Maybe the maximum is 3.  

Let's double check my arithmetic at $\theta=0$ and $\pi/2$.  
$\theta=0 \implies z=1$. $|1+z| = |2|=2$. $|1-z+z^2| = |1-1+1|=1$. Sum=3.  
$\theta=\pi/2 \implies z=i$. $|1+z| = |1+i| = \sqrt{2}$. $|1-z+z^2| = |-i| = 1$. Sum $\approx 2.414$.  
Is there any other critical point?  
Let's check the function values for different angles.  
At $\theta=\pi/3$:  
$z=e^{i\pi/3} = 1/2 + i\sqrt{3}/2$.  
$A^2 = (1+0.5)^2 + (\sqrt{3}/2)^2 = 2.25 + 0.75 = 3$. $A=\sqrt{3} \approx 1.732$.  
$B^2$: Real part is $1 - x + x_2$. Imaginary part is $y_2 - y_1$.  
Let's calculate $B$ again properly.  
$z = \frac{1+i\sqrt{3}}{2}$.  
$z^2 = e^{i2\pi/3} = \frac{-1 + i\sqrt{3}}{2}$.  
Then $1-z+z^2 = 1 - \frac{\sqrt{3}+i}{2} - \frac{1-i\sqrt{3}}{2} = 1 - \frac{\sqrt{3}+1}{2} - i\frac{\sqrt{3}-1}{2}$?  
Real part: $1 - \frac{\sqrt{3}+1}{2}$. Imaginary part: $\frac{-\sqrt{3} + \sqrt{3}}{2} = 0$?  
No, imaginary part of $z^2$ is $\sqrt{3}/2$.  
So Real(T) = $1 - (\frac{\sqrt{3}+1}{2}) + 0$? No.  
Let's just calculate using the values: $x=1/2$, $y=\sqrt{3}/2$.  
$T_2 = (1-x+y^2-xy)$? No.  
The imaginary part of the expression is determined by $\sin(\theta) + \sin(2\theta)$ or something.  
Let's recalculate $B$ for $\theta=0$ again to be sure.  
If $\theta=0$, $x=\cos 0 = 1$, $y=0$.  
Then $1 - z + z^2 = 1 - 1 + 1 = 1$. So $|B|=1$. Correct.  

What about if we consider $\theta$ very large? No, unit circle is finite.  
So let's check the derivative or geometry condition for maximum.  
We have a function of $x,y$.  
$f(x,y) = \sqrt{(1+x)^2+y^2} + |1 - x+iyz^2|$.  
Since we maximize $f$, we want to see if $A+B$ can be greater than 3.  
We found 3 and $\approx 2.41$. Let's check for any possibility of larger values.  
Maybe I should calculate the maximum of the sum algebraically.  
Consider vectors $\mathbf{u} = z-1$, $\mathbf{v} = z+1$? No.  
We want to maximize $|1+z|$ and $|z^2-z+1|$.  
The second term is related to a geometric mean?  
Let's look at the term $B$. Is it possible that for some $z$, $|1-z+z^2| = |z^2-z+1| = \sqrt{3}$?  
At $\theta=0$, $B=1$. Max of $B$ is 1? No, let's check.  
Roots of $z^2-z+1$: $\omega, \bar{\omega}$. Magnitude is 1.  
We want to maximize $|1 - z + z^2|$.  
Let's rewrite $|1-z+z^2| = |z^2-z+1|$.  
The roots of this are $\frac{1 \pm i\sqrt{3}}{2}$. These correspond to $e^{i2\pi/6}$ and $e^{-i2\pi/6}$.  
Let's check the angle of these points. They are $e^{\pm i 2\pi/3}$.  
These are points on the unit circle?  
$|z^2-z+1|$ is the distance between origin, $z$ and $z^2$ shifted by something?  
No, it's a complex number.  
Actually, let's look at the triangle formed by $1$, $z$, $z^2$.  
If we plot points in the complex plane: $P_1=1$, $P_2=z$, $P_3=z^2$.  
The value of $B$ is the length of the vector connecting $1, P_3, P_2$? No.  
It's just the modulus of a linear combination of points.  
The function $z \mapsto |z^2-z+1|$ is convex/monotonic on circle?  
Wait, let's look at the maximum value of $|z^2-z+1|$.  
Let $f(z) = z^2-z+1$. Then $f(e^{i\theta}) = e^{i2\theta} - e^{i\theta} + 1$.  
We want to maximize this modulus.  
The roots of $z^2-z+1$ are $\omega, \bar{\omega}$ where $\omega = e^{i 2\pi/3}$?  
No, roots of $x^2-x+1=0$ are $\frac{1 \pm i\sqrt{3}}{2}$.  
The modulus is 1.  
So $B$ is on the unit circle? No.  
Actually $B(\theta)$ takes values such that $|B| \le 1 + |z^2-z|$? No.  
If we take $\theta = \pi$, $z=-1$. Then $B = |1 - (-1) + 1| = |3| = 3$. This contradicts my previous calculation of $B$ being small or constant.  
Let's re-check $B$ for $z=-1$.  
$z=-1$. $z^2=1$.  
$1 - z + z^2 = 1 - (-1) + 1 = 3$. Modulus is 3.  
This was based on calculation error earlier? Wait, in $\theta=\pi$, $\cos\pi=-1$, $\sin\pi=0$.  
If $z=-1$, then $x=-1$, $y=0$.  
Then $A^2 = (1-1)^2 + 0^2 = 0$. $|A|=0$.  
$B^2 = (1-(-1)+(-1))^2 = 3^2 = 9$. $|B|=3$.  
So at $\theta=\pi$, sum is 3.  
At $\theta=0$, sum is 3.  
At $\theta=\pi/2$, sum is $\approx 2.414$.  

What if we maximize using the triangle inequality?  
$|A+B| \le A + B$. We know $B$ can be up to 3 (if $z=-1$). But at that point, $A=0$. So sum is small.  
To get large sum, we need both terms to be non-zero and close to each other? No, to maximize sum, usually we want them to not interfere much, but if they have same phase they cancel or add?  
Let's consider $z$ such that $\theta$ is small.  
If $A \approx 2$, $B \approx 1$. Sum $\approx 3$.  
Is it possible that one of the terms is large, say $|A|=1$, and $|B|$ is close to 2?  
Let's check if $|A|$ can be 1. $|1+z|=1 \implies |z+1|=1$. This implies $z=-1$ or something else.  
If $z=-1$, sum=3. If $z=i$, sum $\approx 2.41$. If $z=\sqrt{-1}$, $z^2=0$. Then $B = |-i - i| = |-2i| = 2$? No.  
Let's check other points.  
If $z$ is real number on circle (so $z \in [-1,1]$). $z \in \mathbb{R}$ implies $y=0$, so $z=x$. Then $x^2=1 \implies x=\pm 1$. So $A = |1 \pm 1| = 2$ or $0$. If $z=-1$, $A=0$, sum=3.  
If $z$ is purely imaginary, $A=|1 \pm i|$. Max is $\sqrt{2}$. Then $B=|-i|=1$. Sum $\approx 2.414$.  

Is there any point with higher values?  
Let's try to express $B$ as $|e^{i\alpha} - z(1+z)|$? No.  
Let's check the maximum of $A+B$ subject to $z \in \text{unit circle}$.  
If we fix $\theta$, let's just evaluate for a grid or similar.  
$\theta = 0 \implies A=2, B=1 \implies \sum = 3$.  
$\theta = \pi/2 \implies A=\sqrt{2}, B=1 \implies \sum = \sqrt{2}+1 \approx 2.41$.  
$\theta = \pi/6 \implies A=\sqrt{3}, B \approx 0.54$ (calculated earlier? Let's recheck).  
Re-evaluate $B(\pi/6)$.  
$z = e^{i\pi/6} = \frac{1+i}{2}$? No, $\cos=1/2, \sin=\sqrt{3}/2$.  

*Continued in [part 3 of 3](intermediate_algebra_1806_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
