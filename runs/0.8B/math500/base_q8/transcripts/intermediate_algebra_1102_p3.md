# test/intermediate_algebra/1102.json, part 3 of 3

[Previous part](intermediate_algebra_1102_p2.md) · [Start](intermediate_algebra_1102.md)

Wait. If I write $x^4 + 5x^3 + 9x^2 - x - 14$, this means $P(x) = 1x^4 + 5x^3 + 9x^2 - 1x - 14$.  
So coefficient of $x$ is $-1$.  
Coefficient of constant term is $-14$.  

Okay. So my substitution at $x=-2$:  
Term "- x" becomes $-(-2) = 2$.  
Sum: $16 + (-40) + 36 - 2 - 14$? No, I need to add/subtract properly.  
$16 - 40 + 36 - 2 - 14$.  
Wait. Is the term "- x" or is the term "minus x"?  
If it's just a term $-x$, then substituting $x=-2$, we get a value of $+2$? No, wait.  
Let me re-read my thought process.  
If I plug in -2 into $-x$. The result is $-(-2) = 2$. Yes.  
Wait, but if I look at the polynomial $P(x)$ where coefficients are $1, 5, 9, -1$.  
Then value at $x=-2$ is:  
$16 - 40 + 36 - (-2)?$ Wait.  
If term is "- x", then it is $-(-2) = +2$. No wait, this means if the expression is written as "minus times x".  
If the equation was $x^4 + \dots - x$, then substituting $x=-2$ yields:  
$16 + (-40) + 36 + (-(-2)) - 14$? No.  
Term "- x" means $- \times x$. So value is $+2$.  
If the user wrote "$- x$", they meant $-x$.  
So at $x=-2$, it's $-(-2) = +2$.  
So let's sum: $16 - 40 + 36 + 2 - 14$.  
Wait. Is $-14$ subtracted or added? It is "- 14". So it is minus 14.  
So Sum = $16 - 40 + 36 + 2 - 14$.  
Wait, I have "Summing up: $16 - 40 + 36 + 2 - 14 = (16-40) + (36+2) - 14$."  
Let's sum these groups.  
$16-40 = -24$.  
$36+2 = 38$.  
$-24 + 38 = 14$.  
$14 - 14 = 0$.  
So $x=-2$ is indeed a root.  

Let me check $P(1)$ again.  
$1 + 5 + 9 - 1 - 14$.  
Wait, the term is "- x". At $x=1$, this is $-1$.  
Wait, why did I think $x^4 + 5x^3 + 9x^2 - x - 14$?  
Let me re-read.  
$x^4 + 5x^3 + 9x^2 - x - 14$.  
Okay, let's check the signs of coefficients.  
$c_0 = -14$.  
$c_1 = -1$.  
$c_2 = 9$.  
$c_3 = 5$.  
$c_4 = 1$.  
Wait, I missed something crucial.  
Is $c_1$ the coefficient of $x$ or is there a typo?  
Usually if someone writes "x^4 + 5x^3 + 9x^2 - x - 14", they mean:  
$x^4 + 5x^3 + 9x^2 + (-1)x - 14$.  
But wait. In the original text, there is a "$- x$" and " $- 14$ ".  
Okay, so at $x=-2$:  
$x^4 \to 16$.  
$5x^3 \to -40$.  
$9x^2 \to 36$.  
$-x \to 2$. (Since $-(-2)=+2$).  
Constant $\to -14$.  
Sum: $16 - 40 + 36 + 2 - 14 = 0$.  

Let me check the other candidate, $x=7$.  
Wait. Is there any chance I made an arithmetic error in my mental addition?  
Let's re-evaluate $P(-2)$.  
$16 - 40 = -24$.  
$-24 + 36 = 12$.  
$12 + 2 = 14$.  
$14 - 14 = 0$.  

Let me re-evaluate $P(7)$ again.  
$x^4 \to 2401$.  
$5x^3 \to 5(343) = 1715$.  
$9x^2 \to 9(49) = 441$.  
$-x \to -7$.  
Sum: $2401 + 1715 + 441 - 7 - 14$.  
Wait. The term is "- x". If I evaluate the last term at $x=7$, it's $-7$.  
So sum is positive large number. No way to find zero.  

Okay, so let's look for other integer roots.  
Maybe I missed a simpler factorization?  
Let's divide $P(x)$ by $(x+2)$.  
$1, 5, 9, -1, -14$.  
Divide by $x+2$.  
Synthetic division with -2:  
Coeffs: $1, 5, 9, -1, -14$.  
Shift:  
Bring down 1.  
Multiply by -2: $-2$. Add to 5 $\to$ 3.  
Multiply by -2: $-6$. Add to 9 $\to$ 3.  
Multiply by -2: $-6$. Add to -1 $\to$ -7.  
Multiply by -2: $14$. Add to -14 $\to$ $-10$. Wait.  
Let's re-calculate this step.  
Polynomial division: $(x+2)(Ax^3 + Bx^2 + Cx + D) = x^4 + (A+B)x^3 + (B+C)ix^2 + (C+D)x + BD$?  
Wait, no. $(x+2)$ multiplies $ax^3 + bx^2 + cx + d$.  
Result is $Ax^4 + Bx^3 + Cx^2 + Dx + 2A$. Wait.  
Let's do the division properly.  
Polynomial: $1x^4 + 5x^3 + 9x^2 - x - 14$.  
Divisor: $x+2$.  
$x^4$: coeff 1. Remainder is 0? No, we subtract.  
Wait, I'll perform polynomial long division.  
$P(x) = 1 \cdot (x+2)(x^3 + ax^2 + bx + c)$?  
Let's check if $x=-2$ divides it.  
If $x=-2$, then terms are:  
$x^4 - 5 \cdot 8 + 9 \cdot 4 - (-2) - 14$. Wait, the term for $-x$ is positive.  
$16 - 40 + 36 + 2 - 14 = 0$.  
Wait, why did I doubt?  
Let's check the coefficients of the new quotient polynomial.  
If $x^4+5x^3+9x^2-x-14$ has factor $(x+2)$, then:  
$x^4 - 8 + \dots$ No, wait.  
Let's perform division:  
$(1)x^4 = x^4$. Divisor is $x+2$. So $x^4/(x+2)$ is quotient $x^3 + ax^2 + bx + c$.  
Multiply $(x+2)(x^3 + ax^2 + bx + c)$.  
$x^5 + \dots$  
No, it's $(x^4+ax^3+bx^2+cx+d)(x+2)$.  
Wait, I'll multiply:  
$(1)x^4 = x^4$.  
$(1)(-2)$? No.  
We want to write $P(x) = (x+2)(Ax^3 + Bx^2 + Cx + D)$.  
$Ax^4 + (A+B)x^3 + (B+C)x^2 + (C+D)x + 2D$. Wait, this is only if constant term is 0? No.  
Constant term of $P(x)$ is $-14$. So $(x+2)$ must multiply by a constant factor $k$? No.  
The remainder would be $R(-2) = P(-2) - (-2)^3 \times (\dots)$.  
Let's just use the fact that if $x=-2$, then $P(x) = 0$.  
Since $P(-2) = 0$, we can factor out $(x+2)$ from the polynomial.  
So there exists a quadratic factor: $(x^2 + ax + b)$. No, $x=-2$ is integer root.  
But wait, $P(x)$ is degree 4.  
If it factors as $(x+2)(Quadratic)$, then the product must be integer coefficients.  
The other factor will have integer coefficients if $x=-2$ is an integer root.  
Wait, I don't need to do synthetic division manually, I can check the roots using divisors of -14.  
Divisors of -14: $\pm 1, \pm 2, \pm 7, \pm 14$.  
Since we found $x=-2$ is a root (via $P(-2)=0$), and I checked the rest.  

Wait, did I check all divisors?  
$x=1$:  
$1 + 5 + 9 - 1 - 14 = 0$. Correct.  
$x=2$:  
$16 + 40 + 36 - 2 - 14 = 76 \neq 0$.  
$x=-1$:  
$1 - 5 + 9 - (-1) - 14$? No, $P(-1)$ is value.  
$x^4 - 5 + 9 - x - 14$?  
Wait, term at $x=-1$ for $-x$ is $+1$.  
Sum: $1 - 5 + 9 + 1 - 14 = -8 \neq 0$.  
$x=7$:  
$x^4 + 5(343) + 9(49) - x - 14$.  
If term is $-x$, then for $x=7$, term is $-7$.  
$2401 + 1715 + 441 - 7 - 14$. Positive large.  
$x=-7$:  
$x^4 = 2401$.  
Wait, $(-7)^4$? No, $(-2)^4=16$. Wait, $x^4$ is always positive for even x.  
So $P(7)$ is definitely not 0 (as we checked).  

## Answer

*(none: the token cap hit during thinking)*
