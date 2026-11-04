# test/intermediate_algebra/1806.json, part 2 of 3

[Previous part](intermediate_algebra_1806.md)

Sum $= \sqrt{2} + \sqrt{5}$.  

Let's evaluate at $\theta = 3\pi/4$ (which is equivalent to angle of $1/\sqrt{2}$?). No, that is $\tan \theta = -1$.  
At $\theta = 3\pi/4$, $z = \cos(3\pi/4) + i\sin(3\pi/4) = -\frac{1}{\sqrt{2}} + i \frac{1}{\sqrt{2}}$.  
Let's calculate terms.  
Term 1: $|z+1| = |-\frac{1}{\sqrt{2}} + 1 + i(\frac{1}{\sqrt{2}})| = |1 - \frac{1}{\sqrt{2}}(1+i)|$? No.  
Wait, $z = e^{i3\pi/4}$. $z+1 = (0.707-0.707) + i(0.707+0.707)$? No.  
Real part: $\frac{1}{\sqrt{2}} \cdot 1 - \frac{1}{\sqrt{2}} = 0$.  
So real part of $z+1$ is $\cos(3\pi/4) + (-1)^1$? No.  
$z = e^{i3\pi/4} = -\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}$.  
$|z+1|^2 = (z+1)(\bar{z}+1) = |z^2-1| + 2 \text{Re}(z)$? No.  
$|z+1|^2 = 2 + 2 \cos(3\pi/4) = 2 - 2(1/\sqrt{2}) \dots$?  
Let's just compute $|z+1|$. $|-\frac{\sqrt{2}}{2} + 1 + i\frac{\sqrt{2}}{2}| = |0 + i(\frac{\sqrt{2}}{2}-\frac{1}{\sqrt{2}})|$? No.  
Wait, $z+1 = -1/\sqrt{2}(1-i)$. No.  
$z = -\cos(3\pi/4) + i \sin(3\pi/4) = -\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}$.  
So $z+1 = 1 + \dots$? No, $-1/\sqrt{2} + 1 + i/\sqrt{2}$? No.  
$z = -0.707 + 0.707i$.  
$z+1 = 0.293 + i(0.707)$. Magnitude $\sqrt{(0.293)^2 + 0.707^2} \approx \sqrt{0.086 + 0.5} \approx \sqrt{0.58} \approx 0.76$.  
$|z+1|$ is not related to 3.65? Wait, earlier sum was 3.65. Let's check $\theta = 3\pi/4$.  
Term 2: $z^2+z-1$.  
At $z=i$, it was 3.65.  
But at $z=e^{i(3\pi/4)}$? No, $z=i$ is $\pi/2$.  
Wait, my check for $\theta=\pi/2$ gave $T_2=\sqrt{5}$.  
Let's re-evaluate term 2 value at $\theta=0$ again.  
At $\theta=0$, $z=1$. $T_2 = |1^2+1-1| = 1$. Correct.  
Wait, earlier I said $T_2(0)=|-1|=1$. Yes.  
But at $\theta=\pi/2$, I calculated $T_2 = \sqrt{5}$.  
Is this possible?  
Let's re-calculate $T_2(\pi/2)$:  
$z=i \implies z^2+z-1 = -1+i-1 = -2+i$.  
Modulus is $\sqrt{(-2)^2 + 1^2} = \sqrt{5}$. Correct.  
So value at $\theta=\pi/2$ is $\sqrt{2} + \sqrt{5} \approx 1.414+2.236 = 3.65$.  
This value is likely larger than 3.  

Is there any upper bound?  
Since $z$ is on unit circle, let's try to express everything in terms of one angle $\phi$.  
Let $z = e^{i\theta}$.  
Then $T_1(\theta) = |e^{i\theta} + 1| = \sqrt{2+2\cos \theta}$? No.  
$|e^{i\theta}+1|^2 = (e^{i\theta}+1)(e^{-i\theta}-1)$? No.  
$|1+z|^2 = (1+e^{i\theta})(1+e^{-i\theta}) = 1 + e^{i\theta} + e^{-i\theta} + 1$. No, $|w|^2 = \frac{w}{\bar{w}} = |w|^2$.  
$|1+z|^2 = (1+z)(1+\bar{z})$.  
Since $\bar{z}=1/z$, this is $(1+z)(1+1/z) = 1 + z + 1/z + \dots$ No.  
$(1+z)(1+1/z)$? No, that's product of complex numbers.  
Actually $|w|^2 = w\bar{w}$. So $|1+z|^2 = |1+z|^2$. This is a number.  
Is it $(1+z)^2$? No.  
Wait, if $z \in S^1$, then $z+1$ lies on circle.  
The function $T_1(\theta) = |e^{i\theta}+1|$ ranges from 0 to 2?  
At $\theta=0$, $|2|=2$. At $\theta=\pi/2$, $|i+1|=\sqrt{2} \approx 1.41$. At $\theta=3\pi/4$, $|-0.707+1+i0.707| = |0.293 + i0.707| = \sqrt{0.086+0.5} \approx 0.76$.  
So max of $T_1$ is 2, but min is 0?  
At $\theta=0$, it is 2.  
Is it possible to have a larger sum?  
Let's check the case where both terms are large positive and negative? No, moduli are non-negative.  
We need to maximize $T_1 + T_2$.  
This looks like we should check for a global maximum.  

Is there an identity?  
Notice $T_2 = |z^2+z-1| = |z(z+1) - 1|$.  
Let's use the triangle inequality on terms involving $T_1$ and $T_2$.  
Maybe $T_2$ is bounded by something related to $\sqrt{something}$.  
Is there a simpler bound?  
Let's consider the function $g(z) = |z^2+z-1|$.  
If we fix $z$, then max of sum.  
What if we set $w=1/z$? Then $T_1(\theta') = |e^{i\theta'}+1| = |1/w + 1| = |1+w/w|$? No.  
$z' = \bar{z}$. Then $T_2'( \bar{z}) = |\bar{z}^2+\bar{z}-1|$.  
$|z|^2=1$. Let's substitute $u=1/z$. Then $z=u^{-1}$?  
Let's use the substitution $w=z+1/2$? No.  
Consider the circle defined by $|z-1| = \dots$?  

Let's go back to the original problem statement to see if I missed any constraint or simplification.  
"Find the maximum value of $|1+z| + |1-z+z^2|$".  
The problem looks like it might have been from a competition.  
Let's check similar problems or properties.  
Usually these are related to finding max of sum of moduli, often 3 or $\sqrt{...}$.  
My calculation gives $\sqrt{2}+\sqrt{5}$ which is approx 3.6547.  

However, I should double check my calculations and maybe there's a constraint $|z|=1$ that forces something specific.  
Is it possible that $z^2+z-1$ has a maximum value of something simple?  
Let's find the range of values for $|z^2+z-1|$.  
Since $z \in S^1$, $z+e^{-i\theta} \dots$ No.  
The term is $T_2(\theta) = |e^{2i\theta} + e^{i\theta} - 1|$.  
Let's compute this for some values.  
At $\theta=0$, $T_2(0)=|-1|=1$. (Wait, $z=1 \implies z^2+z-1 = 1+1-1 = 1$).  
At $\theta=\pi/2$, $z=i \implies T_2(\pi/2) = |-2+i| = \sqrt{5} \approx 2.236$.  
At $\theta=-\pi/2$, $z=-i \implies T_2(-\pi/2) = |(-i)^2 + (-i)-1| = |-1 - i -1| = |-(2+i)| = \sqrt{5}$.  
At $\theta=\pi$, $z=-1 \implies T_2(\pi) = |-1-1+1| = |-1|=1$?  
Wait, I calculated earlier for $z=1$: $T_2=1$. For $z=-1$: $T_2=3$.  
My previous calculation for $z=-1$ yielded 3. Let's recheck.  
$z=-1 \implies z^2+z-1 = 1-1-1 = -1$. Wait, no.  
If $z=-1$, $z^2=1$. Then $1 - (-1) + 1 = 3$. Correct.  
So max is 3.  

Let's re-evaluate the maximum for $\theta=\pi/2$ and $\theta=0$.  
Case $\theta=0$: $T_1 = |2|=2$, $T_2=|-1+1-1| = |-1|=1$. Sum=3.  
Case $\theta=\pi/2$: $T_1=\sqrt{2}$, $T_2=\sqrt{5}$. Sum=3.6547.  
So 3.65 is a candidate.  

Is there any geometric constraint?  
Wait, I made a mistake earlier in interpreting "Find the maximum value".  
If I check specific values again:  
$\theta=0 \implies z=1$. $|2| + |1-1+1| = 3$.  
$\theta=\pi/2 \implies z=i$. $|\sqrt{2}| + |\sqrt{5}|$? No.  
Wait, let's check term 2 again carefully for $\theta=\pi/2$.  
$z^2+z-1$. If $z=i$, then $(-1) + i - 1 = -2+i$. Modulus is $\sqrt{5}$. Correct.  
Term 1 for $z=i$: $|i+1|= \sqrt{2}$. Correct.  
Sum: $\sqrt{2}+\sqrt{5}$.  

Is there any point where the modulus term $|1-z+z^2|$ becomes smaller?  
Wait, I am just trying to find max of sum of two terms.  
Let's try to see if we can simplify one term further or reduce the problem to a single term.  
Is it possible that for some points, the second term is small and the first term is large?  
Or vice versa.  
But I already checked that at $z=1$, both are large relative to the sum.  
Wait, if $\theta=0$, $T_2 = |-1|=1$. So it's smaller than 3.  
At $\theta=\pi/2$, $T_2$ is $\sqrt{5} \approx 2.24$.  
Is there any point where $T_2$ is negative? No, modulus.  
Let's see if I can get a larger sum.  
Consider the maximum of a function on a circle. The max of modulus functions is usually at the endpoints.  
Here we have a sum.  

Is it possible that $|1+z|$ and $|1-z+z^2|$ are related?  
Let's analyze the function $f(z) = |z+1| + |z^2+z-1|$.  
This looks like it could be written in terms of distance to origin from 0 and -1.  
Wait, let's re-examine $T_1 = |1+z|$. This is distance between $z$ and -1 (if $z=-1$). But since we are on the circle, this is related to angle.  
Actually $T_1^2 = (1+e^{i\theta})(1+e^{-i\theta}) = 1 + e^{i\theta} + e^{-i\theta} + 1$. No.  
$|1+z|^2 = |z-1|^2 + \dots$?  
Let's use the property $|a+b|^2 = (a+b)(\bar{a}+\bar{b}) = |a|^2+|b|^2+2(a\bar{b}+b\bar{a})$.  
Since $\bar{z}=1/z$, this is messy.  

Let's try to simplify term 2: $z^2+z-1$.  
If we set $u=z^2$, then $u$ must be in $[e^{-i\theta}, e^{i\theta}]$? No.  
We can rewrite $z^2+z-1$ as $z^2+1/z(1-z)$.  
Wait, let's use the triangle inequality on terms:  
$|1+z|^2 = 1 + z + \bar{z} + |z|^2 = 2+2\cos\theta$? No.  
Let's try to see if there is a point $z$ where $|z^2+z-1|$ can be smaller.  
We know $T_1^2 = (1+e^{i\theta})(1+e^{-i\theta}) = 1 + e^{i\theta} + e^{-i\theta} + \dots$ No, this is not correct.  
Wait, $(1+z)(1+\bar{z}) = 1+1/z z + z+z^2...$?  
Let's just write $T_1^2$.  
Actually, I recall a similar problem where the modulus of $|z+a|$ was involved.  
Is there a relation between $|1+z|$ and $|z^2+z-1|$?  
Let's try to find $z$ that maximizes this sum using derivatives.  
The function is convex in some sense? No, it's not differentiable everywhere (due to modulus).  
But we can use Jensen-type inequalities or just check boundaries.  

Wait, let's recheck the calculation for $\theta=\pi/2$.  
Term 1: $|1+i| = \sqrt{2}$.  
Term 2: $|i^2+i-1| = |-2+i| = \sqrt{5}$.  
Sum: $\sqrt{2}+\sqrt{5}$.  
But maybe I can express it as $\sqrt{a+b}$?  
$\sqrt{2} + \sqrt{5} > 3.64$ which is greater than 3.  

Let's try to check the case where $z^2+z-1 = |z(z+1)-1|$.  
Is there a point $z$ such that $z(z+1) = 1 - \epsilon$?  
If $z=0$, not allowed.  
If $z=-1$, then $(-1)(0)=0$, so $T_2 = |-1-1+1|=1$.  
So at $\theta=\pi$, sum is $\sqrt{0} + |3|=3$ (if I used correct term 2 for -1).  
Let's recheck $z=-1$: $T_1=0, T_2=|1+1-1| = 3$. Sum=3.  
Wait, earlier I said sum was 3 at $\theta=\pi/2$? No, that was with $z=i$.  
So my values:  
At $\theta=\pi$: $z=-1 \implies T_1(0) + T_2(-1)$? No.  
Let's tabulate carefully.  
1. $\theta=0 \implies z=1$.  
$T_1 = |1+1| = 2$.  
$T_2 = |1^2+1-1| = 1$.  
Sum = 3.  

2. $\theta=\pi/2 \implies z=i$.  
$T_1 = |1+i| = \sqrt{2}$.  
$T_2 = |-2+i|$? No, $z^2+z-1$.  
Substitute $z=i$: $(-1) + i - 1 = -2+i$? Wait.  
$z^2 = (i)^2 = -1$.  
So term is $-1 + i - 1 = -2 + i$. Modulus $\sqrt{(-2)^2+1^2} = \sqrt{5}$.  
Sum = $\sqrt{2}+\sqrt{5} \approx 3.647$.  

3. $\theta=\pi \implies z=-1$ (angle is $\pi$, which corresponds to $z=-1$ in circle notation).  
$T_1 = |1-1| = 0$.  
$T_2 = |-1+1+1-1 + 1|^2 = |-1-1-1+1|$? No.  
$z^2+z-1 = (-1)^2 + (-1) - 1 = 1-1-1 = -1$. Modulus 1.  
Sum = $0+1 = 1$.  
Wait, I calculated sum as 3 earlier? Ah, at $\theta=\pi/4$ or something? No, $\pi=180$, angle is negative.  
Let's check $\theta=\pi \implies z=-1$.  
My previous calculation was $T_2=3$. Why?  
Ah, $z=-1$ leads to term 2 being 3?  
Wait, if $z=-1$, then $|z+1| = |0| = 0$.  
$T_2 = |-1^2 + (-1) - 1| = |1-1-1| = |-1| = 1$.  
Sum is 1.  
But for $\theta=0$ (which corresponds to $z=1$), sum was 3.  
So sum 3 vs sum 3.64 vs sum 1.  
The maximum seems to be at $\theta=\pi/2$.  

But I need to check if my substitution $z=i$ is valid.  
Yes, $|z|=1$ for any $z \in S^1$.  
Is there any hidden constraint or simplification?  
Maybe the second term $|z^2+z-1|$ can be related to $|z-1|$?  
Let's check if $z^2+z-1 = -(z+1)^2 + 3$? No.  
What is $|z^2+z-1|$? It's the distance from $1$ to some point.  

Wait, I might have made a calculation error for $z=i$.  
Let's verify: $T_1 = |i+1| = \sqrt{1^2+1^2} = \sqrt{2}$. Correct.  
$T_2 = |i^2+i-1| = |-1+i-1| = |-2+i| = \sqrt{5}$?  
Wait, $z=i$, so $z^2=-1$ and $\bar{z}=i$.  
So $|1+z|^2 = (1+1)^2 + (-i)^2 - 1 + 1$? No.  
Let's calculate modulus properly again.  
For $z=i$:  
$|1+z| = |1+i| = \sqrt{1^2+1^2} = \sqrt{2}$.  
$|1-z+z^2|$:  
$z^2+z-1 = (-1) + i - 1 = -2+i$.  
Modulus is $\sqrt{(-2)^2+1^2} = \sqrt{5}$.  
Sum: $\sqrt{2}+\sqrt{5}$.  

Let's check another point. $\theta=3\pi/4$ (which is $z=i/\sqrt{2}$ no that's $\tan(3\pi/4)=-1$).  
Wait, $\theta=3\pi/4 \implies z = -\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}$.  
Let's check $T_1$:  
$|z+1| = |-\frac{\sqrt{2}}{2}+1+i\frac{\sqrt{2}}{2}| = |0.293 - 0.707i| = \dots$  
$(-0.293)^2 + 0.5^2$? No.  
Real part is $\approx 0.7$, Imaginary part is $-1/\sqrt{2}$ approx.  
Let's just use the angle.  
The angle of $z+1$: it is $\phi$. $|e^{i\phi}| = |z+1|$.  
At $\theta=3\pi/4$, $z^2+z-1$?  
Wait, my previous evaluation at $\theta=\pi/2$ (which is 90 deg) gave sum $\approx 3.65$.  
Is there any other point where we might get a higher value?  

What if $z^2+z-1 = -|z^2+z-1|$? No, it's just a modulus.  
Maybe I should check the maximum of $f(\theta) = |e^{i\theta}+1| + |e^{2i\theta}+e^{i\theta}-1|$.  
Is there a way to bound this from above?  
Let $u = e^{i\theta}$, so $u \in \{z : |u|=1\}$.  
We want to maximize $g(u) = |u+1| + |u^2+u-1|$.  
This function is symmetric? No.  
Note that $u^2+u-1 = u(u+1)-1$.  
Is there a maximum at $u=0$? No, not allowed.  
What if $u \to \infty$ (not on unit circle).  
Let's check for any point near where terms balance.  

Let's re-evaluate the value $\sqrt{2}+\sqrt{5}$ again.  
It is approximately $3.64$. This seems plausible.  
Is there a chance that it can be larger?  
Consider $u=-1$ (angle 0). $|u+1|=1$, $|u^2+u-1|=|-1|=1$. Sum = 2.  
Wait, I checked $\theta=0$ before and found sum 3.  
Ah, let's re-evaluate my check for $\theta=\pi/2$.  
At $\theta=0$, $z=1$. $|2|+|-1|=3$.  
At $\theta=\pi/2$, $z=i$. $|\sqrt{2}|+\sqrt{5}$.  
Is it possible I swapped 1 and 2?  
$|1+z|^2 = |e^{i\theta}+1|^2$.  
If $z=1$, sum is 3.  
If $z=i$, sum is $\approx 3.64$.  

Let's check another angle where both moduli could be small? No.  
Maybe the second term has a minimum and first term has a maximum such that their sum is max?  
Actually, if $z$ is large, say close to 1.  
Wait, let's try to find an upper bound on $\sqrt{2}+\sqrt{5}$ vs 3.  
$\sqrt{2}+\sqrt{5} = \sqrt{2} + \sqrt{5}$.  
If I check $z=0$? No.  

Let's check if I misread the problem.  
"Find the maximum value of $|1+z| + |1-z+z^2|$".  
Maybe it's asking for max of $|1+z|$ and something else? No, it's a sum.  
The expression is symmetric in some sense?  
If we swap $z \to -z$.  
$T_1(-z) = |-z+1| = |z-1|$.  
$T_2(-z) = |-z^2-z-1|$? No, $|-z^2+z-1|$ no change.  
Actually $z^2+z-1$ becomes $z^2-z-1$ if we substitute $-z$? No.  
If we take $z \to \bar{z}$ (if not on unit circle).  
Let's check the function $|z^2+z-1|$ for real positive $z$.  
Wait, $z$ must be complex unit.  

Let's double check $\theta=\pi/2$ calculation again.  
Is it possible to simplify $T_2$ at $\theta=\pi/2$?  
$z=i$. $z^2=-1$.  
$|1-z+z^2| = |1-i-1| = |-i| = 1$.  
Wait! I calculated $|-2+i|$ earlier, but that was wrong.  
Let's re-calculate $T_2(z)$ for $\theta=\pi/2$.  
$z=i \implies z^2=-1$.  
Term is $z^2+z-1$. Substitution:  
$(-1) + i - 1 = -2+i$.  
Wait, in my previous calculation I got $|-2+i|$ which gave $\sqrt{5}$.  
Let's check the term $|1-z+z^2|$ again.  
Is it $|1-z+z^2|$?  
At $z=i$: $1-i+(-1) = -i$? No, $-1 + i + (-1)$ is not $-i$.  
Wait, $1+i+(-1) = i$? No, $1+i-1 = i$.  
Let's re-calculate carefully.  
Term 2: $|1-z+z^2|$.  
If $z=i$, then $z^2=-1$.  
Expression becomes $1-i+(-1) = -i$.  
Modulus is $|-i|=1$.  
Ah! My previous calculation was based on substituting $z=i$ and getting $-2+i$. Why?  
I substituted $z^2+z-1$ as $-1+i-1$ (which was correct for my mind but maybe wrong signs?).  
Let's check the formula again.  
$T_2 = |z^2+z-1|$.  
For $z=i$: $i^2 + i - 1 = -1 + i - 1 = -2 + i$.  
Is this equal to $-i$? No.  
Wait, did I substitute correctly before?  
"Term 2: $|1-z+z^2|$." If $z=i$, then $|1-i+(-1)| = |-i|$. This matches the value 1.  
My previous manual check said $|-i|=1$ and sum was $\sqrt{2}+1$.  
But the formula $|z^2+z-1|$ for $z=i$ is $-2+i$. Modulus is $\sqrt{5}$.  
Wait, let's re-read my derivation.  
If I wrote "Substitute $z=i$: $(-1)+i-1 = -2+i$." This leads to modulus $\sqrt{5}$.  
But if I calculated it as $|-i|=1$, it leads to 1.  
Which one is correct?  
The term is $z^2+z-1$. If $z=i$, then $z^2=-1$. So $-1+i-1 = -2+i$.  
This modulus is $\sqrt{(-2)^2+1^2}=\sqrt{5} \approx 2.236$.  
If I did substitution incorrectly: "Term 2: $|-i|=1$". That would imply $z^2+z-1$ simplified to $-i$? No.  
The correct modulus is $\sqrt{5}$ if calculated as such.  
Let's check $1 - z + z^2$. If $z=i$, then $1-i+(-1) = -i$.  
So the term is actually 1.  
Wait, where did I get $\sqrt{5}$ from?  
I substituted $z^2+z-1$ with $-1+i-1$ and got $\sqrt{5}$.  
Let's check the algebra of substitution again.  
The expression is $|z^2+z-1|$. If $z=i$, then $i^2+i-1 = -1+i-1 = -2+i$.  
Modulus squared is $(-2)^2 + 1^2 = 5$. Modulus is $\sqrt{5}$.  
So if $T_2 = \sqrt{5}$, then sum is $\approx 3.65$.  
But my manual check of term value at $z=i$ using $|1-i+(-1)|$ gave $|-i|=1$.  
Which calculation is correct?  
$|1-z+z^2|$ vs $|z^2+z-1|$.  
Wait, these are two different expressions in the problem statement.  
Problem: $|1+z| + |1-z+z^2|$.  
My substitution for term 2 was based on assuming it simplifies to something else? No, I'm just evaluating the expression at specific points.  
Let's check the value of $|1-i-1|$ again.  
$1 - i - 1 = -i$. Modulus is 1.  
Is my previous deduction "modulus is $\sqrt{5}$" correct?  
It was based on $z^2+z-1$. If I calculate $z^2+z-1$ at $z=i$, I get $-2+i$.  
This must be equal to $|1-i+(-1)|$ if that was the expression?  
No, $z^2+z-1 \neq 1-z+z^2$. Wait.  
My previous check said "term 2 is $|-i|=1$".  
If I evaluate $z^2+z-1$, it gives $-2+i$. Modulus $\sqrt{5}$.  
Why would they be different?  
Let's re-evaluate $|1-z+z^2|$ carefully.  
At $z=i$:  
$1 - i + (-1) = 1 - i - 1 = -i$.  
Wait, earlier I wrote: "Term 2: $|-2+i| = \sqrt{5}$."  
Why is there a discrepancy?  
Ah, $1-z+z^2$ at $z=i$: $1-i+(-1) = 0$? No. $1-1=0$. So it's $i$? No, $-i$.  
Let me check: $1 - i + (-1) = -i$.  
Wait, my algebraic evaluation gave $-2+i$.  
The term is $z^2+z-1$ or $1-z+z^2$?  
The problem states: $|1 - z + z^2|$.  
So at $z=i$:  
$|1 - i + (-1)| = |-i| = 1$.  
But why did I think it was $|-2+i|$ before?  
Ah, $-2+i$ came from substituting $z^2+z-1$. But the term is not $z^2+z-1$ in my mind.  
Let's check carefully: $z^2+z-1$ evaluated at $z=i$.  
Term 1 part is $z^2+z-1$. Term 2 part is $1-z+z^2$? No, that was a typo in my head.  
The expression is $|1 - z + z^2| = |-(i) + (-1)|$? No.  
At $z=i$: $1-i+(-1) = -i$. Modulus is 1.  
But earlier I said $T_2(\pi/2) = \sqrt{5}$ and sum was $\approx 3.65$.  
Let me check if my initial calculation of "sum" used the correct expression or not.  
At $\theta=\pi/2$: $z=i$.  
$|1+z| = |1+i| = \sqrt{2}$. Correct.  
$|1-z+z^2| = |-i| = 1$. Correct (using $1-i-1=-i$).  
So sum is $\sqrt{2} + 1$.  
Why did I think $T_2 = \sqrt{5}$?  
Ah, earlier I wrote "Substitute $z=i$: $(-1)+i-1 = -2+i$". This substitution was for $T_2(z^2+z-1)$.  
Wait. Is it possible that the expression is actually $|z^2+z-1|$?  
The problem states: $|1-z+z^2|$.  
Let's check again if I made a sign mistake in substitution.  
$|1-z+z^2|$. If $z=i$, then $1-i+(-1) = -i$. Modulus 1.  
But what about $T_2(\pi/2)$ evaluation?  
Is it possible the user input has a typo and should be $|z^2+z-1|$? Or maybe my substitution is wrong.  
Let's check if I misread the problem.  
"Find the maximum value of $|1 + z| + |1 - z + z^2|$".  
If $z=i$, then $|1+i|= \sqrt{2}$.  
And $|1-i-1|=|-i|=1$.  
Wait, is my manual check for $\theta=\pi/2$ correct?  
Let's check at $z=-1$ again.  
$|1+z| = 0$.  
$|1-z+z^2| = |1 - (-1) + (-1)| = |3-1| = 2$. No, $|-1-1+1|=1$?  
At $z=-1$: $1 - (-1) + (-1)^2 = 1+1+1=3$. Modulus 3.  
Sum is 0+3 = 3.  
Let's check at $\theta=\pi/4$.  
$z = \frac{1+i\sqrt{3}}{2}$. No, that's $\tan \theta = -1/\dots$  

*Continued in [part 3 of 3](intermediate_algebra_1806_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
