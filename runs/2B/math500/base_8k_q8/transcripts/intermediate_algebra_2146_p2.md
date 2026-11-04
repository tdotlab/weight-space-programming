# test/intermediate_algebra/2146.json, part 2 of 2

[Previous part](intermediate_algebra_2146.md)

Wait, the bounds depend on $x$ (or $y$) quadratically? No, $Q_1(y+1) = (x-1)^2 + 1$. This is a function of $x$.  
So for any $x$, $x^2 - 2x + 2 \le P(x)$ and $P(x) \le 2x^2 - 4x + 3$.  
Let's look at the coefficient of $x^2$ in the difference.  
Let $\Delta_1(x) = Q_1(x) - P(x)$. This must be $\ge 0$.  
$\Delta_2(x) = P(x) - Q_2(x)$. This must be $\le 0$. Wait, $P(x) \le Q_2(x)$ implies $\Delta_2(x) \le 0$. No.  
$Q_1 \le P \le Q_2$.  
So we are given that for all $x$, $f(x) \le P(x) \le g(x)$ where $g(x) - f(x) = (x-1)^2$.  
Let's consider the function $h(x) = P(x) - x^2$? No.  
Consider $P(x)$ relative to the quadratic $(x-1)^2$.  
Notice that for any real number $k$, if we have a polynomial $Q$ such that $f(x) \le Q(x) \le g(x)$, then maybe $Q(x) = k f(x)$? No.  

Let's look at this:  
$(x-1)^2 + 1 \le ax^2 + bx + c \le 2(x-1)^2 + 1$.  
Since $(x-1)^2 \ge 0$, the term on LHS is positive.  
The vertex of $g$ is at $(1, 1)$ and coeff is 2. The vertex of $f$ is at $(1, 1)$ and coeff is 1.  
This suggests that for large $|x|$, $P(x) \approx ax^2$.  
And $f(x) \approx x^2$, $g(x) \approx 2x^2$.  
So we must have $1 \le a \le 2$.  

Let's check if there is  

## Answer

*(none: the token cap hit during thinking)*
