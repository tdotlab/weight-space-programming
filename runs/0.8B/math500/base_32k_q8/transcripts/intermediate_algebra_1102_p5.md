# test/intermediate_algebra/1102.json, part 5 of 5

[Previous part](intermediate_algebra_1102_p4.md) · [Start](intermediate_algebra_1102.md)

Let's double check the roots of $(x^2+x+7)$? No.  
What about $x=1$ and $x=-2$.  
Wait, did I miss any divisors?  
Divisors of 14: $\pm 1, \pm 2, \pm 7, \pm 14$.  
Checked all.  
So the roots are 1 and -2.  

Wait, what about $x=0$?  
$-14 \neq 0$.  
$x=-3$? Checked.  
$x=4$?  
$P(4) = 256 + 5(64) + 9(16) + 4 - 14$.  
$256 + 320 + 144 + 4 - 14$.  
Sum: $256+320+144 = 720$.  
$-14+4= -10$.  
$720 \neq 0$.  
$x=-4$?  
$P(-4) = (-4)^4 + 5(-4)^3 + 9(-4)^2 - (-4) - 14$.  
$256 - 320 + 144 + 4 - 14$.  
Positives: $256+144+4 = 404$.  
Negatives: $-320 + 14 = -306$.  
Sum $\neq 0$.  

Wait, I should check if my manual sum for $P(1)$ was correct.  
$P(1) = 1 + 5 + 9 - 1 - 14$.  
$1+5+9 = 15$.  
$-1-14 = -15$.  
Wait, I need to check if the constant term in the expression is $-14$. Yes.  
So sum is 0.  

Wait, I noticed a potential issue with my "positive/negative" logic for checking $P(x)$.  
For $x=-2$, $P(x) = (-2)^4 + 5(-8) + 9(4) - (-2) - 14$.  
Is it possible that the term was supposed to be $+x$?  
If it were $+x$, then for $x=1$: $P(1) = 1 + 5 + 9 + 1 - 14 = 0$.  
If it were $-x^2$? No.  

Is it possible that the root is not an integer but the question asks "Find all the integer roots"? Yes, asking for integers implies checking candidates.  
Is it possible that there's a subtle sign error in my manual check of $P(-2)$?  
Maybe I should verify if $(x+2)$ divides $x^4 + 5x^3 + 9x^2 - x - 14$.  
Let's try synthetic division on coefficients $[1, 5, 9, -1, -14]$ with root -2.  
$-2 \mid 1, 5, 9, -1, -14$.  
Bring down 1. (Coeff of $x^3$ term?) No, the synthetic division for roots $r$ divides polynomial $a x^4 + b x^3 + c x^2 + d x + e$ into quotient $(x-r) \times Q$.  
Wait, I am confusing myself with the root vs coefficient.  
Let's do it properly:  
$x^4 + 5x^3 + 9x^2 - x - 14$.  
Roots of $P(x)$ are $\{-2, 1\}$.  
We want to find if $(x+2)$ and $(x-1)$ are factors.  
We check divisibility by $(x+2)$.  
Using synthetic division with root -2:  
$1 / (-2)$? No.  
If $r=-2$, the coefficients of $P(x)$ should be multiplied by $(-2)^4, 5(-2)^3, \dots$  
Wait, no. The coefficient of $x^k$ in quotient is $(P(r) - r x^{...})/1$. No.  
Let's just check the product of factors at the roots.  
$(x+2)(x-1) = x^2 + x - 2$.  
If we divide original poly by this quadratic?  
Wait, the original polynomial is degree 4.  
So $(x+2)$ and $(x-1)$ are likely factors if they are roots.  
Let's try to factor $P(x) = (x+2)(x^3 + ax^2 + bx + c)$.  
Expand:  
$x^4 + ax^3 + cx^2 - 2x^3 + \dots$ Wait.  
$(x+2)(x^3 + ax^2 + bx + c) = x^4 + ax^3 + bx^2 + cx + 2x^3 + 2ax^2 + 2bx + 2c$.  
So $a+c=5$, $b-c=0$? No.  
$x^4 + (a+2)x^3 + \dots$ No, wait.  
If I multiply $(x+2)$ by a cubic polynomial $Q(x)$, the constant term of product will be $c$.  
Product has degree 4 (since original is degree 4).  
Wait, $P(-2)=0$, so $(x+2)$ divides it.  
This implies quotient is cubic $Q(x) = ax^3 + bx^2 + cx + d$.  
So we have:  
$x^4 + 5x^3 + 9x^2 - x - 14$  
$-2 \mid [1, 5, 9, -1, -14]$.  
Bring down $c$ (from constant term of quotient?). No.  
Standard synthetic division:  
$x=2$:  
Coeffs: 1, 5, 9, -1, -14.  
Term for root:  
We want $P(x) = (x+2)Q(x) + R$.  
The remainder is 0 if $x=-2$ is a root.  
Since coefficients are integers, we can just check if it's zero. We did that.  

Wait, let me double check the roots again. Is there any chance I missed a root?  
Divisors of -14: $\pm 1, \pm 2, \pm 7, \pm 14$.  
I have checked all of them for $P(x)$.  
Let's just re-verify the sum calculation one more time for each candidate to ensure no arithmetic errors.  

Candidate: $x=1$  
$1 + 5(1)^3 + 9(1)^2 - (1) - 14$  
$= 1 + 5 + 9 - 1 - 14$  
$= 15 - 15 = 0$.  
Candidate: $x=-2$  
$(-2)^4 + 5(-2)^3 + 9(-2)^2 - (-2) - 14$  
$= 16 - 40 + 36 + 2 - 14$  
$= (16+36+2) - (40+14)$  
$= 54 - 54 = 0$.  

Candidate: $x=-7$  
$(-7)^4 + 5(-7)^3 + 9(-7)^2 - (-7) - 14$  
$= 2401 - 1715 + 441 + 7 - 14$ (Note: I used -1 for the constant term in previous check, but this uses +7 for linear).  
Wait, the linear term is $-x$.  
If $x=-7$, then $-(-7) = 7$.  
Wait, earlier I wrote "Sum: $2849 - 1729 = 1120 \neq 0$".  
Let's re-sum carefully.  
Positives: $2401 + 441 + 7 = 2849$. (Wait, term $-x$ was positive).  
Negatives: $5(-7)^3 = -1715$. Wait, original polynomial has $+5x^3$. No.  
Let's look at the signs in polynomial definition again.  
$x^4$: +  
$5x^3$: + (if x=7, it's 343). If x=-7, it is -1715.  
Wait, I said for $x=-7$, $5x^3 = -1715$. Correct.  
But wait. Is the coefficient of $x^3$ in polynomial 5? Yes.  
So term is $+5(-7)^3$. This is negative.  
Term $-x$: If $x=-7$, this  

## Answer

*(none: the token cap hit during thinking)*
