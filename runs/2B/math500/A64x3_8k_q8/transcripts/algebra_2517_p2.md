# test/algebra/2517.json, part 2 of 2

[Previous part](algebra_2517.md)

If $a=-3, |a|=3 > 0.33$.  
If $a=0$ was allowed, max is $1/9$. But not allowed.  

Is there a typo in the question provided by user?  
"what is the greatest possible value of $(a+\frac{1}{b})(\frac{1}{b}-a)$"  
Usually, these problems come from contexts where you want to maximize positive results or find max/min of expressions like $(a-b)^2$.  
If it were $(a+1/b)(a-1/b)$, then max is at boundary.  
But with what is given, it's straightforward.  

Let me think if there is a way $a$ and $b$ are related? No "if ... and ...". They are independent variables constrained by their own intervals.  

Is there any ambiguity in the order of operations?  
$(a+1/b)$ then $(1/b-a)$. Yes, that's how it is written.  
What if $a+\frac{1}{b}$ is a single term and $\frac{1}{b}-a$ is another? Yes.  
Is it possible that I should write the value as $35/9$? No, value must be consistent with signs. The product is negative.  

Let's assume there might be a misinterpretation of "common fraction".  
Maybe the answer is supposed to be positive and I'm missing something fundamental.  
Could the question be $(\frac{1}{b}+a)(\frac{1}{b}-a)$? Same as above.  
Could it be $|(\dots)|$? No, usually explicit.  

Let's assume the standard interpretation.  
Function: $f(a,b) = \frac{1}{b^2} - a^2$.  
Maximize over domain.  
The domain is disconnected into 4 quadrants in terms of signs if we consider $a,b$ independent. But here both are fixed intervals.  
We need to find argmax of $f$.  
Since the function is strictly decreasing with respect to $|a|$ and decreasing with respect to $b$ (increasing $b \to$ decreasing term),  
Max occurs at smallest possible values for $|a|$ and largest possible value for term $\frac{1}{b^2}$?  
No, let's trace the monotonicity carefully.  
$f(a,b) = \frac{1}{b^2} - a^2$.  
Term $g(b) = 1/b^2$ is strictly decreasing on $(0, \infty)$. So to MAXIMIZE it, we need MINIMUM $b$. Constraint: $b \geq 3$. Min $b=3$.  
Term $h(a) = -a^2$. This is an inverted parabola opening downwards. It is maximized at $a=0$. However, domain is $[-6, -2]$, which is a subset of negative numbers. The function $-x^2$ decreases as $|x|$ increases.  
On interval $[-6, -2]$, $x^2$ increases from 4 to 36 (for non-0 values).  
So $-a^2$ increases from 4 to -36? No.  
If $a=-2, a^2=4 \implies -a^2 = -4$.  
If $a=-6, a^2=36 \implies -a^2 = -36$.  
So on the domain of $a$, $-a^2$ is maximized at the point where $a^2$ is minimized. That is $a=-2$.  
So both terms are individually maximized (one term increasing, one term decreasing? No.)  
We want to Maximize $X - Y$ where $X = 1/b^2 > 0$ and $Y = a^2 \geq 0$.  
To maximize $X-Y$, we need large $X$ and small $Y$.  
Large $X$: Max possible value of $X$. $b=3 \implies X_{max} = 1/9$.  
Small $Y$: Min possible value of $Y$. Min possible value of $a^2$ on domain. $|a|$ min is 2 (at $a=-2$). So $Y_{min} = 4$.  
So Max value = $1/9 - 4 = -35/9$.  

Is there any case where this logic fails?  
What if the  

## Answer

*(none: the token cap hit during thinking)*
