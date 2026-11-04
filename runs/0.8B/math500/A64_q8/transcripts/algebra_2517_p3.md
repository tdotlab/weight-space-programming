# test/algebra/2517.json, part 3 of 3

[Previous part](algebra_2517_p2.md) · [Start](algebra_2517.md)

To maximize $u^2 - a^2$, we should minimize $|a|$? No. We want to subtract a small number from the large number $u^2$. But $u^2$ is max at $b=3$. And $|a|$ can be any value from $4$ (min abs) or larger? No, $|a|$ depends on range.  
Min value of $a^2$ is when $|a|$ is minimized. That means we should check $a$ values close to 0. But the problem fixes $a \in [-6, -2]$.  
So $a^2 \ge 4$.  
To maximize $u^2 - a^2$, we need to choose $b$ such that $u^2$ is maximized? No. We want to minimize $a^2$. The smallest value of $a^2$ possible in the domain is $4$ (since $a \ge -6$, so max $|a|$ is 0).  
But $|a|$ cannot be less than 4 because $a \le -6$? No, wait.  
Let's re-evaluate $a$'s range.  
$a \in [-6, -2]$. This is the set of values for $a$.  
If $a=-5$, $a^2 = 25$. If $a=-2$, $a^2 = 4$.  
Since the expression is $\frac{1}{b^2} - a^2$, we have $E(a,b) \le \max_u u^2 - (-\infty)$.  
But since $a^2$ is subtracted, to maximize $E$, we want $a^2$ as small as possible.  
The smallest possible value of $a^2$ occurs when $|a|$ is minimized. Since $a \ge -6$, min $|a| = 0$. But $a \in [-6, -2]$ implies $a$ cannot be 0.  
However, the set includes values close to 0? No, it's a negative interval.  
The range of $a^2$ for $a \in [-6, -2]$ is $[4, 36]$.  
So min $a^2 = 4$. Max $a^2 = 36$.  
To maximize $\frac{1}{b^2} - a^2$, we want to minimize $a^2$. This means choosing the most negative $a$? No.  
We need to choose $a$ such that $a$ is as far from 0 as possible (since $a^2$ increases with $|a|$).  
To maximize the result, we should minimize $a^2$. The minimum value of $a^2$ is 4 (at $a=-2$).  
And for $b$, to maximize $\frac{1}{b^2}$, we should choose smallest possible denominator squared. That means $b=3$, which gives max $1/9$.  
If we choose these values: $b=3 \implies 1/b^2 = 1/9 \approx 0.111$. $a=-2 \implies a^2 = 4$.  
Then expression value is $\frac{1}{9} - 4 = -3.888...$  
This result is quite negative.  
However, we are not maximizing the *absolute* value? No, just "greatest possible value".  
Since this result is negative, maybe I messed up signs or something fundamental about the expression?  
Let me check the problem statement again very carefully.  
$\displaystyle\left(a+\frac{1}{b}\right)\left(\frac{1}{b}-a\right)$ ?  
This looks correct.  
Is it possible that $\frac{1}{b}$ is negative? No, $3 \le b \le 5$.  
Is it possible the expression was $\left(a-\frac{1}{b}\right)\left(\frac{1}{b}+a\right)$?  
If I assume that, then expansion gives $a^2 - b^{-2}$. Since $-4 \approx 3.89$, max value might be different.  
But usually standard form is written correctly.  
Let me check if there's a typo in my manual calculation of the sign.  
$(a+1/b)(1/b-a) = (a + u)(u - a)$.  
If $a=-5, b=3.5$: $(-4.7)(-0.28)?$ No. $(1/b-a) \approx 5.28$ ? No.  
Let's re-calculate carefully with calculator-like precision.  
$a = -5, b = 3.5$.  
$1/b = 1/3.5 \approx 0.285714$.  
Factor 1: $a + 1/b = -5 + 0.285714 = -4.714286$.  
Factor 2: $1/b - a = 0.285714 - (-5) = 5.285714$.  
Product: $(-4.714286)(5.285714) \approx -25.0$. (Since $4.7 + 5.3 = 9.9$ and $9.9 \times ...$ no, it's $-25$ exactly?)  
Let's check exact fraction.  
$a=-5$, $b=7/2 = 3.5$.  
Term 1: $a+u = -5 + 2/7 = (-35+2)/7 = -33/7$.  
Term 2: $u-a = 2/7 - (-5) = 2/7 + 35/7 = 37/7$.  
Product: $(-33/7)(37/7) = -1221 / 49 \approx -24.85$.  
Now check $u^2 - a^2$ formula again.  
$u = 2/7 \approx 0.2857$.  
$a^2 = 25$.  
Formula $u^2 - a^2 = (2/7)^2 - 25 = 4/49 - 25 = (-1221)/49 \approx -24.85$.  
This matches exactly.  
So expression is indeed $\frac{1}{b^2} - a^2$.  

Wait, my previous calculation of signs was confusing because I used "minimize $a^2$" but the result was negative.  
Let me re-verify the sign of product $(a+u)(u-a)$.  
If I substitute $a=0$, then $(1/u)(u-0) = 1/b \cdot 1/b$ ? No, $1/b - 0 = 1/b$. So $(a+u)(u-a)$?  
Let's check $a=-2$ and $b=3.5$ (from previous example).  
$a=-2, b=3.5 \implies u = 2/7 \approx 0.2857$.  
Expression: $(-2 + 2/7)(2/7 - (-2)) = (-16/7)(39/7)$?  
$u-a = 2/7 + 14/7 = 16/7$.  
$a+u = -2 + 2/7 = -16/7$.  
Product: $(-16/7)(16/7) = -256/49 \approx -5.22$.  
Formula: $u^2 - a^2 = (2/7)^2 - (-2)^2 = 4/49 - 4 = -380/49$ ? No, $4 - 4/49 = 196/49$.  
So it's different.  
Let me calculate the product using expansion again for $a=-2, b=3.5$.  
$a+u = -2 + 2/7 = -16/7$ ? No.  
Wait, $a+u = a + 1/b$.  
If $b=3.5$, then $1/b = 0.2857...$  
$-2 + 0.2857 = -1.71428...$?  
$-16/7$ is $-2.28$? No.  
$16/7 \approx 2.28$. So $a+u = -16/7$? Yes, if $a=-2$, then $-2 + 2/7 = (-14+2)/7 = -12/7$.  
Let's redo the example calculation carefully.  
$a=-2, b=3.5$. $1/b = 2/7$.  
Term 1: $a+1/b = -2 + 2/7 = -16/7$? No.  
$-2 = -14/7$. $-14/7 + 2/7 = -12/7$.  
So $a+u = -12/7$.  
Term 2: $1/b - a = 2/7 - (-2) = 2/7 + 14/7 = 16/7$.  
Product: $(-12/7)(16/7) = -192 / 49 \approx -3.93$.  
Now check expansion of $(a+1/b)(1/b-a)$.  
Expansion: $(u+v)(v-u)$ where $u=a, v=b^{-1}$? No.  
Let's use the identity $(x+y)(y-x) = y^2 - x^2$ again.  
$x = a$, $y = 1/b$.  
Product should be $y^2 - x^2 = 1/b^2 - a^2$.  
Using these numbers:  
$1/3.5^2 - (-2)^2$.  
$3.5^2 = 12.25$.  
$1/12.25 \approx 0.0816$.  
$a^2 = 4$.  
$E = 0.0816 - 4 = -3.938$.  
Matches my direct calculation of $-3.93$.  
So the formula is correct.  

Now, back to maximizing $\frac{1}{b^2} - a^2$ subject  

## Answer

*(none: the token cap hit during thinking)*
