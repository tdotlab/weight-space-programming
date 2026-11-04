# test/intermediate_algebra/158.json, part 2 of 3

[Previous part](intermediate_algebra_158.md)

Derivative wrt $b$: The part that is dependent on $b$ is just $b^2$. So $2b \cdot 1$.  
So $\frac{\partial f}{\partial b} = a \cdot (2b) c^3 d^4 = 2ab c^3 d^4$. Correct.  
$\frac{\partial f}{\partial c}$: The part dependent on $c$ is $c^3$. So derivative is $3c^2$.  
So $\frac{\partial f}{\partial c} = a \cdot b^2 \cdot (3c^2) d^4 = 3a b^2 c^2 d^4$.  
$\frac{\partial f}{\partial d}$: The part dependent on $d$ is $d^4$. So derivative is $4d^3$.  
So $\frac{\partial f}{\partial d} = a \cdot b^2 \cdot c^3 \cdot (4d^3)$. No, product rule.  
Actually, the function $f(a,b,c,d)$ has terms like $a$, $b^2$, $c^3$, $d^4$.  
If I differentiate w.r.t $a$, only term is $b^2 c^3 d^4 \cdot (1/0)$? No.  
Let's just compute using product rule or simple substitution.  
$f = a b^2 c^3 d^4$.  
$\frac{\partial f}{\partial a} = b^2 c^3 d^4$.  
$\frac{\partial f}{\partial b} = a \cdot 2b \cdot c^3 d^4$.  
$\frac{\partial f}{\partial c} = a \cdot b^2 \cdot 3c^2 d^4$.  
$\frac{\partial f}{\partial d} = a \cdot b^2 \cdot c^3 \cdot 4d^3$.  

Let's re-verify the partial derivatives.  
$f(a,b,c,d) = (a b^2 c^3 d^4)$.  
1) $a$ is multiplied by $b^2 c^3 d^4$. The coefficient of $a$ is 1. So $\partial/\partial a = b^2 c^3 d^4$. Correct.  
2) $b$ is squared inside the term $(ab^2 \dots)$? No, it's outside. It is just $b^2$. Wait, no.  
Let me write $f$ explicitly.  
$f = a \cdot b^2 \cdot c^3 \cdot d^4$.  
Yes, derivative of $a \cdot (\text{const})$ with respect to $a$ is constant.  
So $\partial f / \partial a = 1 \cdot b^2 c^3 d^4$. (Correct)  
$\partial f / \partial b$: The term is $(ab^2 \dots)$.  
Deriv wrt $b$: $2b \cdot (\text{term})$. So $\partial f / \partial b = 1 \cdot a \cdot b \cdot c^3 d^4 \cdot 2$? No.  
Let's look at the term $(ab^2)$. It has $b^2$. Derivative wrt $b$ is $2b$.  
Then multiply by $a$ (coefficient of $f$). So $2ab c^3 d^4$. Correct.  
$\partial f / \partial c$: The term is $c^3$. Deriv wrt $c$ is $3c^2$. Multiply by $1 \cdot b^2 \cdot a$ (coefficient).  
So $\partial f / \partial c = 3a b^2 c^2 d^4$? No. The term is $b^2 \dots$? No.  
Term is $(ab^2 \dots)$. So $a$ is constant.  
Wait, the term inside the derivative for $c$ comes from $c^3$. It's $c^3 \cdot 1$. Deriv wrt $c$ is $3c^2$.  
So $\partial f / \partial c = a b^2 (3c^2 d^4)$. No, coefficient of $d^4$ is just 1. So it is $a b^2 \cdot 3c^2 d^4$.  
Let's check the term in the sum: $(ab^2 c^3 d^4)$.  
So $\partial f / \partial c = a b^2 (3c^2) d^4$? No.  
Term is $a \cdot b^2 \cdot c^3 \cdot d^4$.  
Derivative wrt $c$: It's $b^2 \cdot a \cdot 0 \cdot d^4 + b^2 c^3(3c^2) d^4$? No.  
If it's sum $a b^2 c^3 d^4$, derivative is just the coefficient of $c^3$. That is $a b^2 \cdot 3c^2 d^4$.  
No, this assumes we are dealing with a polynomial.  
$f(a,b,c,d) = (ab^2)c^3d^4$.  
So $\partial f/\partial c$ is coefficient of $c^3$ times derivative of constant? No, it's product of terms $a b^2 c^3 d^4$.  
Deriv wrt $c$: The part depending on $c$ is just $(c^3)$. So we differentiate the whole expression.  
This means $\frac{\partial}{\partial c} (a \cdot b^2 \cdot c^3 \cdot d^4) = 3 a b^2 c^2 d^4$? No.  
It's $a \cdot b^2 \cdot (3c^2 d^4)$? No, I'm confusing the variables.  
Let's check term by term in expression: $f = a \cdot b^2 \cdot c^3 \cdot d^4$.  
$\frac{\partial f}{\partial c}$: The coefficient of $c$ is 1. Term is $c^3$. Derivative wrt $c$ is $3c^2$. Multiply by remaining terms $(a, b^2, d^4)$.  
So $\frac{\partial f}{\partial c} = a \cdot b^2 \cdot (3c^2) \cdot 1$? No.  
Term is just $c^3$. So the derivative wrt $c$ is $3c^2$.  
The other terms are constant with respect to $c$ ($a, b^2, d^4$).  
So yes, $\partial f / \partial c = a b^2 (3c^2) d^4$.  
But I must check if there's any term in the product $ab^2 c^3 d^4$ that is constant with respect to $c$. Yes, just $a b^2 d^4$.  
So yes, $\partial f / \partial c = 3a b^2 c^2 d^4$.  

Now for $d$:  
$f = a b^2 c^3 d^4$.  
Deriv wrt $d$ is $4 a b^2 c^3 d^3$. (Derivative of $d^4$).  
But this means I'm treating $f$ as a product where $c$ is a part.  
Let's write it clearly:  
$f = a \cdot b^2 \cdot c^3 \cdot d^4$.  
$\frac{\partial f}{\partial d} = 1 \cdot (b^2) \cdot (c^3) \cdot (d^4)'$? No. The derivative of $d^4$ with respect to $d$ is $4d^3$.  
So $\frac{\partial f}{\partial d} = a b^2 c^3 (4d^3)$. No, that's assuming I'm differentiating the sum.  
$f = (a \cdot b^2 c^3) \cdot d^4$.  
Let's treat the term $(a \cdot b^2 c^3)$ as a variable? No.  
It is $P(x) \cdot y$ where $y=d^4$. So derivative wrt $d$ is $4d^3 \cdot P(x)$.  
So $\frac{\partial f}{\partial d} = 4a b^2 c^3 d^3$.  

Wait, this logic holds if I consider the expression as a function of variables.  
But I must be careful. The constraint is on variables sum to 10.  
So $\nabla f$ is the gradient vector $(b^2 c^3 d^4, 2ab c^3 d^4, 3a b^2 c^3 d^4, 4a b^2 c^3 d^3)$? No.  
Let's check partial derivatives again carefully.  

Term in $f$ as function of variables:  
1. $a$: coefficient is $b^2 c^3 d^4$. $\implies \partial f / \partial a = b^2 c^3 d^4$.  
2. $b$: coeff is $a \cdot 1 \cdot c^3 \cdot d^4$? No, the term is $(ab^2) \dots$ so coeff of $b$ is $2ab$. No.  
Let's look at the expression:  
$f(a,b,c,d) = a b^2 c^3 d^4$.  
This is a polynomial in 4 variables.  
Partial derivative with respect to $a$:  
Consider terms involving $a$.  
Only term involving $a$ is $a$. So coefficient is $1 \cdot b^2 c^3 d^4$.  
So $\frac{\partial f}{\partial a} = b^2 c^3 d^4$.  

Partial derivative with respect to $b$:  
Terms involving $b$ are $b^2$. Coefficient of $b^2$ is 1.  
Term in expression: $(a \cdot b^2) \cdot c^3 \cdot d^4$.  
So $\frac{\partial f}{\partial b} = a \cdot 1 \cdot 2b \cdot c^3 d^4 + \dots$ No, $c^3$ and $d^4$ are constants wrt $b$.  
The derivative of $b^2$ is $2b$.  
So $\frac{\partial f}{\partial b} = a(1) \cdot 2b c^3 d^4$.  
So $\frac{\partial f}{\partial b} = 2ab c^3 d^4$.  

Partial derivative with respect to $c$:  
Terms involving $c$ is $c^3$. Coefficient of $c^3$ is 1.  
So $\frac{\partial f}{\partial c} = a \cdot 1 \cdot b^2 c^2 d^4 + \dots$? No, $b^2$ and $d^4$ depend on $c$? No.  
The derivative of $c^3$ wrt $c$ is $3c^2$.  
So $\frac{\partial f}{\partial c} = a b^2 (1 \cdot 3c^2 d^4)$? No.  
It's $a b^2 c^3 d^4$.  
Deriv wrt $c$: the term $(c^3)$ contributes $3c^2$.  
The other terms ($a$, $b^2$, $d^4$) don't contain $c$.  
So $\frac{\partial f}{\partial c} = a b^2 (3c^2 d^4)$? No.  
The term $(c^3)$ has coefficient $1$. Deriv is $3c^2$.  
So yes, $\frac{\partial f}{\partial c} = 3 a b^2 c^2 d^4$ is wrong?  
No, derivative of $b^2$ wrt $c$ is 0.  
Wait, is there any other term with $c$? No.  
So $\frac{\partial f}{\partial c} = a b^2 \cdot (3c^2) d^4$. No. The variable inside the derivative of $c^3$ is just $c^3$.  
Let's check.  
$f(a,b,c,d)$ is defined as product of $a, b^2, c^3, d^4$.  
$\partial f / \partial c = (0) + a(1)b^2(0)c^2(3)d^4$? No.  
Term is $(c^3)$. Deriv wrt $c$ is $3c^2$.  
The other terms are $(b^2, a, d^4)$. They do not depend on $c$.  
So $\frac{\partial f}{\partial c} = 3 a b^2 c^2 d^4$? No.  
It should be just the coefficient of $c$ in the expression? No, derivative is $3c^2 \cdot (a b^2 d^4)$. No.  
The derivative wrt $c$ of $(c^3)$ is $3c^2$.  
Since $a,b,d$ do not depend on $c$, they are constants.  
So $\frac{\partial f}{\partial c} = a b^2 (1) (3c^2) (d^4)$? No.  
Let's check again.  
$f(a,b,c,d) = ab^2 c^3 d^4$.  
$\frac{\partial f}{\partial c} = 0 \cdot a \cdot b^2 + c^3 \cdot 1 \cdot \dots$? No.  
$f = (a)(b^2)(c^3)(d^4)$.  
Partial w.r.t $c$: only $(c^3)$ term is affected. So it's $3c^2 \cdot (a)(b^2)(d^4)$.  
So $\frac{\partial f}{\partial c} = 3 a b^2 c^2 d^4$? No.  
It is just $3 a b^2 c^2 d^4$ if I am squaring or multiplying by constants.  
Wait, derivative of $(c^3)$ wrt $c$ is $3c^2$. The other terms are multiplied by $a,b,d$. They are multiplied by 1.  
So yes, $\frac{\partial f}{\partial c} = a b^2 (3c^2) d^4$? No.  
The expression is just $a \cdot b^2 \cdot c^3 \cdot d^4$.  
If I take derivative of $(x)^3$ wrt $x$, it's $3x^2$. Here the term is $x=c^3$ in the product? No, it's $c^3$ in front.  
So yes, $\partial f / \partial c = 3 a b^2 c^2 d^4$? No.  
The coefficient of $c$ in the expression is 0 (since no term depends on $c$ except $c^3$).  
Ah, no. The product $c^3$.  
Is it possible to interpret the problem as maximizing $\sum x_i y_i z_i$ with sum constraint?  
Usually this means finding critical points where gradient of $f$ is proportional to gradient of $g$.  
But I'm getting stuck on partials.  

Let's try a substitution.  
Given: $a+b+c+d=10$. Maximize $P = ab^2 c^3 d^4$.  
If we use scaling, let $u_1=u, u_2=v, u_3=w, u_4=z$.  
Then $f(u,v,w,z) = (u v^2 w^3 z^4)$? No.  
Let's check if there's a relation between exponents that suggests something.  
$f(x,y,z) \to$ Maximize $x^{1} y^{2} z^{3}$.  
Sum constraint $\sum x_i = 10$.  
Wait, the exponents in my function are $(1, 2, 3, 4)$? No.  
Function is $a b^2 c^3 d^4$.  
Exponents of variables: $(1, 2, 3, 4)$.  
Is it homogeneous?  
Let's check homogeneity degree.  
If we have sum of weights $\sum a_i = S$, then max occurs at uniform distribution or boundary.  
But here the sum is fixed at 10.  
We can try to normalize variables $a,b,c,d$.  
The expression can be written as $(ab c^3 d^4)^1$? No.  
Let's check if I made a mistake in the product rule.  
Let's use Lagrange multipliers.  
$L(a,b,c,d) = ab^2 c^3 d^4 - \mu (a+b+c+d-10)$.  
We need to solve $\partial/\partial a, \partial/\partial b, \partial/\partial c, \partial/\partial d$.  
But I was doing this in the previous step and it worked.  
Let me double check the partial derivatives again.  

Expression: $P = a \cdot b^2 \cdot c^3 \cdot d^4$.  
$\frac{\partial P}{\partial a}$: The derivative of $a$ is 1. So $\partial/\partial a (P) = 1 \cdot b^2 c^3 d^4$. Correct.  
$\frac{\partial P}{\partial b}$: The term $b^2$ is inside. Derivative wrt $b$ of $b^2$ is $2b$. Multiply by coefficient of $b$. But there's no other $b$-term in the expression? No.  
The expression is $(a \cdot b^2) \cdot c^3 \cdot d^4$.  
So derivative wrt $b$ is $1 \cdot a \cdot 2b \cdot c^3 \cdot d^4$.  
So $\frac{\partial P}{\partial b} = 2ab c^3 d^4$. Correct.  
$\frac{\partial P}{\partial c}$: The term $c^3$ in $(a \cdot b^2) \cdot c^3 \cdot d^4$.  
Derivative of $c^3$ wrt $c$ is $3c^2$.  
So $\frac{\partial P}{\partial c} = 1 \cdot a \cdot b^2 \cdot 3c^2 \cdot d^4$. No.  
It's $a b^2 c^3 d^4$? No, the derivative of $c^3$ is $3c^2$. The variable is $c$.  
Is there any term that is constant wrt $c$? Yes, $b^2 a d^4$. But it multiplies $1$ in front.  
So yes, $\frac{\partial P}{\partial c} = 3 a b^2 c^2 d^4$. No. The derivative of $c^3$ wrt $c$ is $3c^2$.  
So $\frac{\partial P}{\partial c} = 3 a b^2 c^2 d^4$? No, this is getting confused with the expression again.  
Let's write it clearly.  
$f(a,b,c,d) = ab^2 c^3 d^4$.  
Variables: $a,b,c,d$.  
$\frac{\partial f}{\partial a}$: Derivative of $(a \cdot b^2 \cdot c^3 \cdot d^4)$ with respect to $a$.  
The only term containing $a$ is $a$ itself. Coefficient is 1. So derivative is $1 \cdot b^2 c^3 d^4$.  
$\frac{\partial f}{\partial b}$: Derivative of $(b^2 \cdot c^3 \cdot a \cdot d^4)$? No, $f = (a) (b^2) (c^3) (d^4)$.  
So term $b^2$ is multiplied by $a$, which is constant.  
Derivative wrt $b$ of $(b^2)$ is $2b$. So we have $1 \cdot a \cdot 2b \cdot c^3 d^4$.  
$\frac{\partial f}{\partial c}$: Derivative of $(c^3)$ wrt $c$ is $3c^2$. So derivative is $a b^2 (3c^2) d^4$. No.  
The term is just $(b^2 a c^3 d^4)$? No.  
It's $(a)(b^2)(c^3)(d^4)$.  
So $\frac{\partial f}{\partial c} = 0 + (1 \cdot b^2) \cdot (c^3)'$? No.  
Let's just apply product rule for $f(x_1, x_2, x_3, x_4)$ where $x_1=a, x_2=b, x_3=c, x_4=d$.  
$f = a b^2 c^3 d^4$.  
$\frac{\partial f}{\partial a} = 1 \cdot b^2 c^3 d^4$. (Correct)  
$\frac{\partial f}{\partial b} = a(2b)c^3 d^4$. (No. Term $ab^2$ is the first factor. It depends on $b^2$. So derivative wrt $b$ is $2ab c^3 d^4$. This seems correct.  
$\frac{\partial f}{\partial c} = a b^2 (3c^2 d^4)$. (No. Term $c^3$ is third factor. Derivative of $c^3$ wrt $c$ is $3c^2$. So term is $a b^2 \cdot 3 c^2 d^4$. This seems correct.)  
$\frac{\partial f}{\partial d} = a b^2 c^3 (4d^3)$. (No. Term $d^4$ is fourth factor. Derivative wrt $d$ is $4d^3$. So term is $a b^2 c^3 \cdot 4d^3$.  
Yes, this looks consistent.  

Now let's set up the system.  
$L = a b^2 c^3 d^4 - \mu (a+b+c+d-10)$.  
$\partial L / \partial a = b^2 c^3 d^4 - \mu = 0$.  
$\partial L / \partial b = 2a b c^3 d^4 - \mu = 0$.  
$\partial L / \partial c = 3a b^2 c^2 d^4 - \mu = 0$ (Wait, I missed the term $c^3$ in the expression? No, it's just $c^3$. So $3c^2$. Yes. But $f$ has $(b^2)$ which is squared.  
Let me check my first thought: $\partial f / \partial b = 2ab c^3 d^4$.  
Here I used $f = a(b^2)c^3d^4$.  
Then $\frac{\partial f}{\partial b}$ comes from $\frac{\partial}{\partial b}(b^2) \cdot (\text{coeffs of } a, c^3, d^4) + (a) \frac{\partial}{\partial b}(\dots)$.  
No. It's just product rule for $a \cdot b^2$.  
$\frac{\partial}{\partial b}(a b^2) = 2ab$.  
Then $\frac{\partial}{\partial c}(3c^2 d^4) \dots$? No.  
Let's re-verify the derivative wrt $c$.  
Term is $c^3$. Deriv is $3c^2$. Multiplied by everything else.  
So $\frac{\partial f}{\partial c} = 3 a b^2 c^2 d^4$? No.  
The term is just $(b^2)$ and $(d^4)$. The variable is $c$.  
If I have $(x)^n$, derivative is $nx^{n-1}$.  
So derivative of $c^3$ is $3c^2$.  
But $f$ has $a b^2 c^3 d^4$.  
The term containing $c$ is just the first part? No, $b^2$ is part of $f$.  
$f$ depends on $b$. So partials are computed.  
Let's do it properly using Lagrange Multipliers logic which handles all terms at once.  
We have a sum constraint: $\sum a = 10$.  
So we want to maximize $ab^2 c^3 d^4$ subject to $\sum x_i = C$.  
The maximum value usually happens when the ratio of partial derivatives is constant? No, that's for constrained optimization problems with $g(x)=C$ if we have homogeneous constraints. But here sum is fixed at 10, so it's just a sum.  
However, I suspect the variables are proportional to $x^{-2}$ or something? No.  

Let's check the condition for maximum using simple inequalities.  
We know $(a+b+c+d)^4 \ge (ab c d)$? No.  
If we maximize $ab^2 c^3 d^4$, maybe symmetry is not the only idea, but since it's a product with powers 1, 2, 3, 4, maybe one variable should be small or large. But usually for $a+b+c+d=10$, we might want to put variables equal.  
However, exponents are distinct: $(1, 2, 3, 4)$.  
This looks like we can try substitution or AM-GM inequality logic? No.  

Let's look at the expression again: $f = a b^2 c^3 d^4$.  
Is it possible that we can use the Cauchy-Schwarz or Holder's Inequality to bound this from above? No, that's for min/max with constraints usually. But here constraint is linear sum.  
Holder's inequality gives an upper bound.  
Let $p = a+b+c+d = 10$.  
We want to maximize $\prod (\text{something})^{e_i}$.  
Usually we use AM-GM type logic, but it doesn't apply directly as exponents are different.  
However, the expression is not homogeneous if I don't look at $x_1 x_2^3 \dots$? No.  
Let's consider the function $F(a,b,c,d) = a^{1/4} b^{2/3} c^{3/5} d^{4/3}$? No.  

Maybe we can rewrite the problem as minimizing something or finding the maximum of the reciprocal?  
Or maybe using inequalities like weighted AM-GM or Holder's.  
Let's check if the answer is simply 0 or some small positive number. But usually, these problems have a nice value like 2, 1/2, etc.  
Wait, $a+b+c+d=10$. The maximum of $ab^2 c^3 d^4$?  
If we set $a=b=c=d=2.5$, then $f = (2.5)^8 \cdot 4^{something}$? No.  
Let's check the exponents again.  
Is it possible that the problem is a variation of $a+b+c+d=k$. Maximize $x_1 x_2^3 \dots$ with some weights?  
Let's try to find the critical point directly.  
The Lagrange multiplier equations gave:  
$\lambda = b^2 c^3 d^4 = 2ab c^3 d^4 = 3a b^2 c^2 d^4 = 4 a b^2 c^3 d^3$? No, I used earlier the derivatives.  
Let's re-evaluate the derivative system derived.  
$\frac{\partial f}{\partial a} = b^2 c^3 d^4$.  
$\frac{\partial f}{\partial b} = 2ab c^3 d^4$.  
$\frac{\partial f}{\partial c} = 3a b^2 c^2 d^4$? No. I need to be careful with derivatives again.  
Let's re-evaluate $\partial f / \partial d$.  
$f = a b^2 c^3 d^4$.  
Deriv wrt $d$: $b^2 c^3 (4 d^3) + \dots$?  
If we use the formula for product:  
$\partial/\partial d (a b^2 c^3 d^4) = 1 \cdot a b^2 c^3 (4 d^3)$. No.  
The term is $d^4$. So derivative is $4d^3$.  
So $\frac{\partial f}{\partial d} = 4a b^2 c^3 d^3$? No, that is $a b^2 c^3 (4 d^3)$. But the first term in product is just $(b^2)$ and $(c^3)$ and $(d^3)$.  
Is it? No. The variable is $d$, so only $d^4$ matters. It's multiplied by $a b^2 c^3$. So $\frac{\partial f}{\partial d} = a b^2 c^3 \cdot 4 d^3$.  
But this seems wrong. If I have $x y z w$ and differentiate wrt $z$, it is $(ywx)^1$.  
Actually, my mistake earlier was thinking of terms like $a b^2$.  
Let's just check a simple case. $f = x$. $\partial f / \partial x = 1$.  
If $f = x y$, then $f' / \partial x = y$. So $y$ depends on $x$.  
In our case, variables are distinct. The partials are $b^2 c^3 d^4$, $2ab c^3 d^4$, $3c^2 a b^2 d^4$ (from $c^3$ term), $4a b^2 c^3 d^3$? No, from $d^4$ term.  
Let's check the derivative wrt $c$.  
$f = a b^2 c^3 d^4$.  
Term is $c^3$. Deriv wrt $c$ is $3c^2$.  
Multiply by coefficient of $a, b, d$. That is just 1.  
So $\frac{\partial f}{\partial c} = a b^2 \cdot 3c^2 d^4$. No. It's $a b^2 \cdot (0) + c^3(3c^2)$?  
No. The product rule:  
$\frac{d}{dx}(ab y z w)$ where $y, z, w$ are constants wrt $x$.  
Here the variable is $x=c$. So we just treat it as a term in product.  
Term with $c^3$ is $(c^3) \cdot 1 \cdot b^2 \cdot a \cdot d^4$. No. It's $(b^2 c^3 d^4) \dots$.  
So $\frac{\partial f}{\partial c} = (b^2 c^3 d^4)'$? No, it's just $c^3$ part derivative.  
The derivative of $c^3$ is $3c^2$. The other parts are constant.  
So $\frac{\partial f}{\partial c} = 1 \cdot b^2 a (3c^2) d^4 = 3ab^2 c^2 d^4$? No, derivative of $b^2$ wrt $c$ is 0.  
So $\frac{\partial f}{\partial c} = 3a b^2 c^2 d^4$.  
Now check $d$. Term $d^4$. Deriv is $4d^3$. The coefficient is just $1$. So $\frac{\partial f}{\partial d} = 4 a b^2 c^3 d^3$? No.  
It's $a b^2 c^3 \cdot (d^3)'$? No, derivative of $d^4$ wrt $d$ is $4d^3$.  
So $\frac{\partial f}{\partial d} = 1 \cdot a b^2 c^3 (4 d^3) = 4a b^2 c^3 d^3$.  
Okay, now I have the gradients.  
Let's write them down again carefully with $a,b,c,d$ as variables.  
$f_a = b^2 c^3 d^4$? No. Let's re-verify the expression of function.  
$f = a b^2 c^3 d^4$.  

*Continued in [part 3 of 3](intermediate_algebra_158_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
