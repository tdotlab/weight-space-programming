# test/algebra/305.json, part 2 of 2

[Previous part](algebra_305.md)

If equation is $ax^2 + bx + c = 0$, then $(-b)/a = \sum x_i$.  
Wait, usually $\sum x_i = -b/a$.  
Here $-b = 5$, $a=1$. So sum is 5.  
Roots are $r_1+r_2 = 5$.  
We found roots to be 7 and -2. Sum is 5. Correct.  

Wait, let me try another factorization method.  
If I use Vieta's formulas on the factorization $(x+2)(x-7)$.  
Then $b_{factors} = 2(-7) + (-7 \times 2)$? No.  
Product of roots is $r_1 r_2 = -14$. Correct.  
Sum is $r_1+r_2 = -5$? No, sum must be equal to $-b/a$.  
Wait, for $(x+2)(x-7)$, the terms are $x \cdot x$, $x \cdot 2$?? No.  
The equation is $x^2 + (-5)x + (-14) = (x-r_1)(x-r_2)$.  
Then $\sum r_i = -(-5)/1 = 5$.  
My roots were 7 and -2. Sum is 5. Product is -14.  
Wait, $r_1=7$ and $r_2=-2$.  
So $(x-7)(x+2) = (x^2 - 7x + 2x - 14)$? No.  
Let's expand $(x-7)(x+2)$.  
$x(x+2) - 7(x+2) = x^2 + 2x - 7x - 14 = x^2 - 5x - 14$.  
Wait, earlier I did $(x+2)(x-7)$ which gave the same result.  
And I also did $(x-7)(x+2)$.  
Let me check if $r_1=7$ and $r_2=-2$.  
Then product is -14. Correct.  
Sum is 5. Correct.  
So roots are indeed $x=-2$ and $x=7$.  

Wait, I need to be absolutely certain about the sign of $\sqrt{\Delta}$.  
$\sqrt{81} = 9$.  
Then $\frac{5 \pm 9}{2}$.  
Positive: $(14)/2 = 7$.  
Negative: $(-4)/2 = -2$.  
Wait, earlier I wrote "product of roots is -14".  
If roots are 7 and -2, product is -14. Correct.  
But wait.  
My previous calculation said "If $r_1=7$ and $r_2=-2$, then $(x+2)(x-7)$..." which simplifies to $x^2 + (2(-7)) + (-7)(2)$? No.  
Wait, if I have roots 7 and -2, the factors are $(x-7)(x+2)$.  
Let's expand $(x-7)(x+2) = x(x) + x(2) - 7x - 7(2)$ ?  
No. $x^2 + (2-7)x - 14$?  
Wait, let's use the FOIL method carefully.  
$(x-a)(x-b)$.  
$x(x) \to x^2$.  
$x(-b)$ term is $-bx$. No.  
$a(b) \to ab$.  
Let's re-evaluate:  
$(x-7)(x+2) = x^2 + 2x - 7x - 14$? No.  
Terms are $x(x)$, $x(-2)$?? No.  
Terms are $x(x)$ -> $x^2$.  
$x \cdot 2$ -> $2x$.  
$-7 \cdot x$ -> $-7x$.  
Wait, terms are from $x$ and $x$. $x(-7) + (-7)(x)$? No.  
Let's list factors clearly.  
Factor 1: $(x-7)$. Constant is -7. Coeff of $x$ is -7. Coeff of constant is 7?  
Wait, no. In $(x-a)(x-b)$, terms are:  
$x \cdot x$: $x^2$.  
$x \cdot b$: $xb$.  
$-a \cdot x$: $-ax$.  
$-a \cdot b$: $-ab$.  
Wait, no. $(x-a)(x-b) = x(x) + (-b)x + a(x) + ab$? No.  
$(x-a)(x-b) = x^2 - ax - bx + ab$.  
Here $a=7, b=-2$.  
$-(-7)x = 7x$? Wait.  
Let's check the signs again.  
$a=-2, b=-7$.  
Then $(x+2)(x-7)$.  
Coeffs: 1 for $x^2$, -5 for $x$, -14 for constant? No.  
Coefficient of $x$ is $(-2)(7)$? No.  
Let's expand term by term.  
$x(x+2) = x^2 + 2x$.  
$(x+2)(x-7) = (x+2)(x-7)$.  
Multiply:  
$x \cdot x = x^2$  
$x \cdot (-2)$? No. $x$ times -2 is not term. It's $-7$ times $x$. So $-7x$.  
Wait, $(x+2)(x-7) = x^2 + 2x - 7x - 14$? No.  
$(x+2)(x-7)$.  
Term from first factor: $x$ and $x \to x^2$.  
Term from second factor: $x(-7)$ or $x(x)$? No.  
$x(x) + 2(-7)$? No, that's not how it works.  
$(A+B)(C+D) = AC + AD + BC + BD$.  
Let $A=x$, $B=2$. $C=x-7$, $D=1$? No.  
The product is $(x)(x) + (x)(-7) + (2)(x) + (2)(-7) = x^2 - 7x + 2x - 14 = x^2 - 5x - 14$.  
Wait, I am doing $(-7)x$ and $+2x$ in the middle.  
Let's do it step by step.  
$(x-7)(x+2) = x(x) + x(2) - 7(x) - 7(2)$.  
$= x^2 + 2x - 7x - 14$? No.  
$(-7)x$ is $-7x$.  
$(2)(x)$ is $+2x$?? No, second factor was $x+2$. The constant term is $2 \cdot (-7)$? No.  
Wait, $f(x) = (x-r_1)(x-r_2)$.  
So expansion is $x^2 - (r_1+r_2)x + r_1 r_2$.  
Given equation: $x^2 - 5x - 14 = 0$? No, that was my denominator.  
Wait, the question is $f(x) = \frac{2x}{x^2-5x-14}$.  
So we solve $x^2-5x-14=0$.  
Roots are $7$ and $-2$.  
Wait. Let me check the signs of $r_1 r_2 = -14$.  
If $r_1, r_2$ are roots, then product is $-14$.  
Sum is 5.  
Let's try to see if there is any ambiguity in my manual calculation.  
$(x-7)(x+2) = x^2 + (2-7)x - 7(-2)$? No.  
Let me check the multiplication again carefully.  
$a=x, b=2$? No. The factors are $(x-a)(x-b)$.  
So $a=r_1, b=r_2$.  
Wait, I think I am mixing up $r_1, r_2$ with the numbers in brackets.  
Let's say roots are $x=-7$ and $x=-2$? No, we found them to be 7 and -2.  
So factors should be $(x-7)$ and $(x+2)$.  
Wait. $(x-7)(x+2) = x^2 + 2x - 7x - 14 = x^2 - 5x - 14$.  
This factorization is correct.  
Wait, $-7(-2)$? No, constant term of $(x-r_1)(x-r_2)$ is $r_1 r_2$.  
Here the roots are 7 and -2. So product should be $-14$ (wait, negative times positive? No).  
Wait, if $r_1=7$, then $(-7)(2) = -14$. Correct.  
If $r_1=-2$, then $(-2)(7)$? No, $x \cdot x$ and $x$ term...  
Let's check $(x+2)(x-7)$.  
Constant is $2 \times (-7) = -14$. Wait, no.  
Term 1: $x \times 2 = +2x$.  
Term 2: $x \times -7 = -7x$.  
So sum is $-5x$. Correct.  
Product of constants is $2 \times (-7) = -14$??  
No, wait. $(x+2)(x-7)$.  
Terms are $x(x)$? No.  
Let me just expand using the bracket form.  
$(A+B)(C+D)$.  
Wait, I think the confusion is that I used $(x-a)(x-b)$ where $a,b$ are numbers 2 and -7? No, usually the formula is $(x-7)(x+2)$ or something.  
Let's check again.  
$(x-r_1)(x-r_2)$.  
If $r_1=7$, then first factor is $(x-7)$.  
If $r_2=-2$, second factor is $(x+2)$. Wait, sum of roots should be 5? No.  
Sum of roots in $(x-r_1)(x-r_2)$ is $-r_1 - r_2 = -(r_1+r_2) = -(-5) = 5$? No, sum of roots is $-(r_1+r_2)$? No.  
Let's check Vieta for $(x-r_1)(x-r_2)$.  
Expansion is $x^2 - (r_1+r_2)x + r_1 r_2$.  
Comparing to $x^2 - 5x - 14$:  
Sum of roots: $r_1+r_2 = -(-5)/1 = 5$.  
Product of roots: $r_1 r_2 = -14/1 = -14$.  
So we need to solve for $r_1+r_2=5$ and $r_1 r_2=-14$.  
Wait, if I have factors $(x-7)$ and $(x+2)$:  
Sum of roots is $-(7) + (-2)$? No.  
If factor is $(x-7)$, then root is 7.  
Then factor is $(x+2)$, root is -2.  
Wait, sum of roots in polynomial form is $b/a$. Here $b=-5$. So sum is 5.  
But if I have factors $(x-7)(x+2)$, the roots are 7 and -2.  
Sum should be $-(r_1 + r_2) = -(7-2)?$ No.  
Wait, let's just check if adding up gives the sum of roots: $7 + (-2) = 5$.  
Yes, $7-2 = 5$. So sum is 5. Correct.  
Product should be $r_1 r_2 = -14$? No.  
$(x-a)(x-b) \to ab + a(-b) + b(a)?$ No.  
Expansion: $(x-a)(x-b) = x^2 - (a+b)x + ab$.  
Here roots are $7, -2$.  
Sum: $-5 = 5$. Correct.  
Product: $-14 = 2 \times (-7)$? No.  
Let's check product of constants in $f(x) = (x-r_1)(x-r_2)$.  
The constant term is $r_1 r_2$.  
Wait, no. $(x+2)(x-7)$. Constant term is $(-2)(-7)$? No.  
Wait, $(x-a)(x-b) = x^2 - (a+b)x + ab$.  
So product of constant terms in expansion must match $c/a$ or something? No, it matches $r_1 r_2$.  
Let's check the value of $ab$.  
In my previous calculation, I said "product is -14".  
This implies $r_1 r_2 = -14$.  
Wait. In $(x-7)(x+2)$, constant term is $(-7) \times (2)$? No.  
It's $-7 \times 2 = -14$? No. The factor is $(x-r_1)$.  
If root is 7, factor is $(x-7)$. Constant is 7? No.  
Wait, if $r_1=7$, then $r_1 + r_2 = 5$.  
And $r_1 r_2 = -14$.  
So $ab = -14$.  
In $(x+2)(x-7)$, the factors are $(x+2)$ and $(x-7)$.  
If we write them in standard form $ax^2 + bx + c$, then sum is $-(r_1+r_2)$ and product is $r_1 r_2$? No.  
Let's use the definition of roots directly.  
Equation: $(x-r)(x-s) = x^2 - (r+s)x + rs$.  
So if we have equation $x^2 - 5x - 14$, then $r+s=5, rs=-14$.  
We need to find integers $r, s$ such that sum is 5 and product is -14.  
Wait. If $r,s$ are factors of roots, then they must satisfy $x^2 - (r+s)x + rs = 0$.  
So we found roots to be $7, -2$.  
Let's check: $7+(-2) = 5$. $7 \times (-2) = -14$.  
Yes! Wait, product of $(x-7)$ and $(x+2)$ is... wait.  
If factors are $(x-7)$ and $(x+2)$, the roots are $7$ and $-2$.  
Wait, I'm getting confused between "sum" and "product".  
The sum of roots is 5.  
Product of roots is -14.  
So if $r_1=7, r_2=-2$, then product is $-14$.  
Wait, earlier I found factorization $(x+2)(x-7)$ to be $x^2 - 5x - 14$.  
Let me verify the constant term of $(x+2)(x-7)$.  
Constant term is $2 \times (-7) = -14$? No.  
The constant terms in product $(x-a)(x-b)$ are $a,b$.  
Wait, no. In $(x-r_1)(x-r_2)$, the constant term is $r_1 r_2$.  
If roots are $-2$ and $7$, then product is $(-2)(7) = -14$.  
But wait. Let's check if my calculation of factorization $(x+2)(x-7)$ matches that product.  
$(x+2)(x-7) = x^2 + 2x - 7x - 14$? No, this was from wrong assumption.  
Let's do it again.  
$a=x$.  
$b=2$.  
$c=-7$.  
Wait, if roots are $-2$ and $7$, then constant term is $(-2)(7) = -14$.  
In $(x+2)(x-7)$, constant term is $2 \times (-7)$? No.  
Let's just multiply out.  
$(x-7)(x+2)$.  
Term 1: $x(x) = x^2$.  
Term 2: $x(-7)$ from factor 2nd term ($x$)? Wait.  
Wait, the second factor is $(x+2)$. The constant term is 2?  
Wait, the linear factors are $(x-7)$ and $(x+2)$.  
Let's write it clearly: $A(x-r_1)(x-r_2) = (x-r_1)(x-r_2)$.  
So expansion is $x^2 - (r_1+r_2)x + r_1 r_2$.  
The product of roots $r_1 r_2$ must be equal to the constant term divided by 1? No.  
Wait, if I write $(x-7)(x+2)$ as factors.  
Then sum of roots is $7+(-2)=5$.  
Product of roots is $7 \times (-2) = -14$.  
And the equation is $x^2 - (sum)x + (prod) = 0$.  
So $x^2 - 5x - 14 = 0$.  
Yes. This matches the quadratic.  
Wait, but why did I think product of $(x+2)(x-7)$ would be 14?  
Let's check product of roots for $(x-7)(x+2)$.  
It is $r_1 r_2 = (-2) \times 7$? No.  
Wait, usually if factors are $f(x) = (x-r_1)(x-r_2)$, then constant term is $r_1 r_2$.  
Here factor is $(x-7)$. Constant term is -7?  
Wait, no. The term "constant" means the product of the linear parts.  
Let's re-evaluate: $x^2 - 5x - 14 = (x-r_1)(x-r_2)$ implies roots are $r_1, r_2$.  
Then constant term in polynomial is $r_1 r_2$.  
So if factors are $(x+7)(x-7)$? No.  
If factors are $(x+7)(x-7)$? That's $(x^2 - 49)$. No.  
Wait, I think I am confusing "roots" with "coefficients".  
Let me simply list the roots of $x^2 - 5x - 14$.  
We calculated them earlier. They are 7 and -2.  
So factors should be $(x-7)$ and $(x+2)$.  
Wait, if factors are $(x-7)(x+2)$.  
Let's multiply: $x^2 - (7+(-2))x + 7(2) = x^2 - (-5)x + 14 = x^2 + 5x + 14$? No.  
Wait, $(x-a)(x-b) = x^2 - (a+b)x + ab$.  
Here $a=7, b=-2$.  
Then $-(7+(-2)) = -5$. Correct.  
Then $ab = -14$.  
So $(x-7)(x+2)$ gives $x^2 - 5x + (-14)$? No.  
Wait, if $a=7$ and $b=-2$, then $ab = -14$.  
The expansion is $x^2 - (7-2)x + (7(-2))$? No.  
Let's use the sign rules for addition: sum of roots is sum of coefficients divided by coefficient of $x^2$. Wait, sum is $-b/a$.  
Sum = 5.  
So $a+b = -5$? No. Sum is 5.  
Wait, I'm getting confused with signs. Let's write it down properly.  
$(x-r_1)(x-r_2)$.  
If roots are $7, -2$.  
Then factors are $(x-7)$ and $(x+2)$? No.  
$(x-7)(x+2) = x^2 + 2x - 7x - 14$? No, wait.  
Wait, if $r_1=7$ and $r_2=-2$.  
Then $(x-r_1)$ is $(x-7)$.  
And $(x-r_2)$ is $(x+2)$.  
Let's check the constant term of product of these two polynomials.  
It should be $(-7) \times (2) = -14$? No.  
Wait, if I multiply $(x-7)$ by $(x+2)$:  
$x(x) + x(2) - 7(x) - 7(2)$?  
Let's check term by term again.  
$x \cdot x = x^2$.  
$x \cdot (-7) = -7x$?? No.  
The second factor is $(x+2)$, so the term with $x$ from this factor is $2$?  
No, let's look at the standard multiplication.  
$x(x-7)(x+2)$. No.  
Let's expand $(x-r_1)(x-r_2)$ again.  
$= x(x-r_1) - r_1 (x-r_2)$? No.  
Wait, let me check the algebraic expansion of $(x-7)(x+2)$.  
$(x)(x) = x^2$.  
$(x)(2) = 2x$.  
$(-7)(x) = -7x$?? Wait.  
Let's check the constant term.  
Constant terms come from $r_1, r_2 \times c_0$.  
In $(x-r_1)(x-r_2)$:  
Term 1 (constant term) comes from $x(r_1)r_2$? No.  
Wait, let's check if roots are correct for the sum/product relations.  
If $a^2 - 5a - 14 = 0$, then $(x-7)(x+2)$.  
Why does that not match my previous expansion?  
Let me do it again.  
Let's expand $(x+2)(x-7)$ carefully.  
$x(x) + x(-7) + 2(x) + (-14)$? No.  
Wait, I keep seeing the term confusion.  
Let's check product $(x-a)(x-b)$ again.  
It is $x^2 - (a+b)x + ab$.  
If roots are 7 and -2:  
Sum = $5$.  
Product = -14.  
Equation is $x^2 - 5x - 14$.  
So if roots are 7 and -2, the factorization is $(x-7)(x+2)$.  
But wait.  
If I have $(x-7)$ and $(x+2)$, their product is $(x-7)(x+2) = x^2 - 5x + (2 \cdot (-7))$? No.  
Let me expand again with correct signs.  
$(x-7)(x+2)$.  
$= x(x) + 2x - 7x - 14$?  
Wait, is it possible that I am just confusing myself by the numbers 2 and -7 vs 7 and -2?  
Let's check:  
$(x-7)(x+2)$.  
$= x^2 - 7x + 2x - 14$? No.  
$= x^2 - 5x - 14$.  
Wait, the term with product of constants is 14?  
No. In $(x-7)(x+2)$, the constant term is $(-7) \times (2)$? No.  
The constant term is $(-7) \times (-2)$? No.  
Let's check: $(x-r_1)(x-r_2)$.  
Constant term is $r_1 r_2$.  
Here roots are 7 and -2.  
So $r_1=7, r_2=-2$.  
Then product is -14.  
Wait, if constant term in polynomial is -14, then product of roots is -14.  
Let's check expansion of $(x-7)(x+2) = x^2 + 2x - 7x - 14$? No.  
$x(x) \to x^2$.  
$x(-7) \to -7x$?? Wait, is this correct?  
Let's check $(x-7)$ term. It's $x$. Then multiply by -7? No.  
The product of roots must be equal to $c/a$. Here $c/a = -14/1 = -14$.  
Wait, but in my previous expansion $(x-7)(x+2) = x^2 - 5x - 14$, the constant term is -14.  
And product of roots is -14.  
This matches.  
So roots are indeed 7 and -2.  

But wait. Is it possible that I am miscalculating something in factorization $(x-7)(x+2)$?  
Let's just do the arithmetic:  
$7 \times (-2) = -14$.  
$(-2)+7 = 5$? No, sum is $5$ for roots.  
Wait. If $a=7, b=-2$, then sum is 5?  
No, $(x-a)(x-b) = x^2 - (a+b)x + ab$.  
Sum of roots is $-(a+b)$? No, it is $b/a$? No.  
It is $-b/a$ for coefficient of $x$.  
Wait, let's just check a simple example. $(x+1)(x-2) = x^2 - 2x + x - 2 = x^2 - x - 2$. Roots are 2, -1? No.  
Let's expand $(x-2)(x-1)$.  
$= x^2 - 3x + 2$? No.  
$x \cdot x = x^2$.  
$x(-1) = -x$.  
Wait, term is $(x-a)(x-b)$.  
Constant term is $ab$.  
Here roots are 2 and 1.  
So sum of roots in the polynomial $x^2 - (a+b)x + ab$? No.  
Let's check: $x^2 - x - 2 = (x+2)(x-4)$? No. $(x-3)(x-1)$.  
Constant term is $(-3)(-1)=3$.  
Wait, my sum product relation was for coefficient of $x$.  
Let's check: $(x-r_1)(x-r_2) = x^2 - (r_1+r_2)x + r_1 r_2$.  
Here we have equation $x^2 - 5x - 14$.  
So $r_1+r_2 = 5$ and $r_1 r_2 = -14$.  
We found roots to be $-2, 7$.  
Let's check sum: $7 + (-2) = 5$. Correct.  
Product: $(-2)(7) = -14$. Correct.  

Wait, is it possible I have the sign of roots wrong?  
If roots are 2 and -3, then product is -6. Sum is -1.  
Here we need sum 5, product -14.  
So roots must be $-2, 7$.  
Wait, wait. Let me check the factorization of $(x+2)(x-7)$.  
Is it possible that $f(x)$ has roots at -2 and 7?  
Let's check my expansion:  
$(x+2)(x-7) = x^2 + (2-7)x + (-2 \cdot 7)$? No.  
Wait, I am confused about which term is in the linear coefficient.  
The terms in product are $x$ times $x$, $x$ times $-7$? No.  
Let's just write it out:  
$(x+2)(x-7) = x(x  

## Answer

*(none: the token cap hit during thinking)*
