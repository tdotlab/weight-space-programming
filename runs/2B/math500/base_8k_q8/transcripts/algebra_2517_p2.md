# test/algebra/2517.json, part 2 of 2

[Previous part](algebra_2517.md)

Is it possible to make $a$ such that $-a^2$ is large positive? No, $a^2 \ge 0$.  
So $\frac{1}{b^2} - a^2$ is maximized when $a^2$ is minimized and $b^2$ is minimized.  
Wait, if I choose $a=-2$, $E = -35/9 \approx -4$.  
But wait.  
If the problem was $(\frac{1}{b}-a)^2 + a^2$... No.  
Maybe I am misreading the expression entirely.  
$\left(a+\frac{1}{b}\right)\left(\frac{1}{b}-a\right)$.  
Wait, is it possible that $a$ is in numerator of second fraction?  
No, standard notation.  
Is it possible that $a+1/b$ means $a^{1/2}$? No.  

Let's consider if I should look at the expression as $\frac{1}{b^2} - a^2$.  
Wait. The question asks for "greatest possible value". If the function is negative, maybe there is a constraint I missed or misread.  
What if $a$ was positive? If $-6 \leq a \leq 0$, then range for $|a|$ would be up to 6. Still negative.  
If the expression was $(\frac{1}{b}-a)(a+\frac{1}{b})$.  
Let's check if there is a sign error in my simplification.  
$(a + 1/b)(1/b - a)$.  
Let $u = 1/b$, $v = -a$.  
Expression: $(v+u)(u-v)$? No.  
$1/b - a = u - (-v) = u+v$. Wait. $v=-a$.  
First factor $a+1/b = v + u$.  
Wait.  
$a = -v$. So $a+1/b = -v+u$.  
Expression is $(u-v)(u+v)$?  
Let's trace back.  
$E = (a + \frac{1}{b})(\frac{1}{b} - a)$.  
Let $X = \frac{1}{b}$ and $Y = a$.  
Then expression is $(Y+X)(X-Y)$.  
Wait, $Y+X = a+1/b$. $X-Y = 1/b-a$.  
So it is indeed $(X+Y)(X-Y) = X^2 - Y^2 = (1/b)^2 - a^2$.  

Okay, so the expression IS $\frac{1}{b^2} - a^2$.  
Is there any other way to read the prompt?  
"greatest possible value of $(a+1/b)(1/b-a)$".  
Constraints: $-6 \le a \le -2$ and $3 \le b \le 5$.  

If the expression is $\frac{1}{b^2} - a^2$, then to maximize it, we need:  
Maximize $\frac{1}{b^2}$: min $b=3$. Max value $1/9$.  
Minimize $a^2$: max $a = 0$ (not in range) or min  

## Answer

*(none: the token cap hit during thinking)*
