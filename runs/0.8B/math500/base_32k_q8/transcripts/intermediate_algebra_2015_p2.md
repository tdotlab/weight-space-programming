# test/intermediate_algebra/2015.json, part 2 of 4

[Previous part](intermediate_algebra_2015.md)

Let's check with $P(x) = (x-1)(x-2) = x^2 - 3x + 2$. Constant term is 2.  
Wait, in this polynomial, the roots are 1 and 2. $\prod \alpha_i = 2$.  
So for $x^4+2x^3+2$, constant term is 2. This implies $\prod \alpha_i = 2$?  
But wait, I said sum is $-c_1/c_n$ earlier.  
Let's stick to the standard expansion:  
$\prod (x-\alpha_i) = x^n - e_1 x^{n-1} + e_2 x^{n-2} - \dots$.  
Here, constant term is 2. This means $\prod \alpha_i = 2$? Wait. The term $c_k$ in the polynomial corresponds to a coefficient.  
Wait, if I write $x^4+2x^3+2$, then coeff of $x^0$ is 2. So product of roots is $-2$. No.  
Wait, $\prod (x-\alpha_i) = (-1)^n \prod \alpha_i + \sum (\dots) x + \dots$?  
Let's check $(x-1)(x-2) = x^2 - 3x + 2$. Constant term is $+2$.  
This means the constant term of polynomial with roots $1, 2$ is $\prod (-\alpha_i)$? No.  
$\prod (x-\alpha_i) = x^4 - (\sum \alpha_i)x^3 + (\sum_{i<j} \alpha_i \alpha_j)x^2 - (\dots)x + (\prod \alpha_i)$.  
Wait, this is for monic polynomial. The term in $x$ expansion corresponds to $\sum (-1)^k e_k$. No.  
It is $e_4 = \prod \alpha_i$.  
But wait, if constant term is 2, then $\prod \alpha_i = 2$? Or something like that.  
Let's check again the sign rule.  
$x^3 - (\sum) x^2 + \dots + (-1)^n \prod$.  
If $P(x) = x^4+2x^3+2$, then coefficient of $x^0$ is 2. This means $\prod \alpha_i = 2$.  
Wait, if I have roots $r_1, r_2$. Then product of roots is $r_1 r_2$.  
If the equation is $(x-r_1)(x-r_2) = x^2 - (r_1+r_2)x + r_1 r_2$, then constant term is $r_1 r_2$.  
But this is for a quadratic. For degree 4, I must have $\prod \alpha_i$ multiplied by something? No, just product.  
So if equation is $(x-\alpha_1)(x-\alpha_2) = x^2 - (\sum \alpha_i)x + \alpha_1\alpha_2$, then constant term is $\alpha_1\alpha_2$.  
But this assumes the polynomial has only 2 terms of type $x^k$? No, that's for a specific degree.  
Wait, $P(x)$ is degree 4. So the expansion gives 4 terms: $x^4 - e_1 x^3 + e_2 x^2 - e_3 x + e_4$.  
Wait, I am mixing up coefficients in the polynomial and roots.  
Let's go with Vieta directly on the equation given in the problem.  
$x^4+2x^3+0x^2+0x+2=0$.  
This is a polynomial $P(x)$ of degree 4.  
The coefficient of $x^3$ is 2.  
So $\sum \alpha_i = -(-2) = 2$. Wait, let me recheck the sign convention again.  
The standard identity is $\prod (x-\alpha_i) = x^n - e_1 x^{n-1} + \dots$ where $e_k$ are elementary symmetric sums of roots $\alpha_i$ in some order.  
Specifically, $\sum_{i<j<k} \alpha_i \alpha_j \alpha_k = -\frac{a_n}{a_1}$? No.  
Let's use the property that the coefficient of $x^{n-1}$ is the negative sum of roots if the polynomial is monic? No, that's for $(x-\alpha_1)...(x-\alpha_n)$.  
Yes, this is true: coeff of $x^{n-1}$ is $\sum \alpha_i$? No. It is $-\sum \alpha_i$.  
Wait, let's check with the example $(x-1)(x-2) = x^2 - 3x + 2$. Coeff of $x^0$ is 2. Coeff of $x^1$ is $-3$. Sum of roots is $1+2=3$.  
So if coeff of $x^{n-1}$ in monic expansion is $c_{n-1}$, then sum of roots is $-c_{n-1}$. Wait, this contradicts my example. In $(x-1)(x-2)$, the polynomial is $x^2 - 3x + \dots$ or is it?  
Wait, $(x-a)(x-b) = x^2 - (a+b)x + ab$.  
Here coeff of $x^2$ is 1. Coeff of $x^1$ is $-(a+b)$. Coeff of $x^0$ is $ab$.  
So if $x^4+2x^3+2$, the coefficients are: $c_1=1, c_2=2$. No wait. $x^4 + 2x^3 + \dots$ means coeff of $x^3$ is 2?  
If this equation has roots $\alpha_i$, then substituting these into the polynomial should give zero.  
Let's re-evaluate Vieta signs.  
For $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
So if we want $c_3 = 2$ in the expansion of $\prod (x-\alpha_i)$, then $-\sum \alpha_i = c_3$? No.  
Wait, I said sum is $-c_{n-1}$. For monic, this formula holds if $P(x) = x^n - (\sum \alpha_i) x^{n-1} + \dots$.  
Let's check the example $(x-1)(x-2)$. This corresponds to equation $x^2-x+1$? No.  
$x^2 - (1+2)x + 1(2) = x^2 - 3x + 2$. Coeff of $x^1$ is $-3$. Sum of roots $1+2=3$.  
So sum of roots $\alpha_i$ corresponds to $c_{n-1}$ coefficient (coefficient of $x^{n-1}$ in expansion). Wait, in $x^2-3x+2$, the term $x$ has coeff -3. Sum is 3. So it's not directly $-\sum$.  
Wait, the coefficient of $x$ in the polynomial expansion $(x-a)...(x-b)$ is $-(a+b)$. But the sum of roots is $\alpha + \beta = a+b$. No, that's wrong. It's minus the sum? Wait, I said $-(\alpha+\beta)$ so it's $-3$ which is $-(1+2)$. So yes, coeff of $x^{n-1}$ is $-\sum_{i=1}^n \alpha_i$.  
Wait, for $(x-1)(x-2)$, the coefficient of $x^1$ is $-(1+2) = -3$.  
For $x^4+2x^3$, the coeff of $x^0$ is 2? No.  
Let's write down the full expansion formula again.  
$(x-\alpha_1)(x-\alpha_2)(x-\alpha_3) = x^3 - (\alpha_1+\alpha_2+\alpha_3)x^2 + \dots$.  
This implies that if we have a polynomial of degree 4, $P(x)$ with roots $\alpha_i$, the coeff of $x^{n-1}$ is $-\sum_{i=1}^n \alpha_i$.  
Wait, I am getting confused. Let's just look at coefficients.  
For $P(x) = \prod (x-\alpha_i)$,  
$P(0) = (-\prod \alpha_i)$? No, $(0- \dots)(0- \dots)(0- \dots)$?  
Wait, the product of terms in expansion is $(-1)^n e_n + e_1 x + \dots$. No.  
The term with $x^0$ is $\prod (-\alpha_i) = (-1)^4 (\prod \alpha_i) = \prod \alpha_i$.  
But wait, for $P(x)$ to be degree 4, I need to check signs of coefficients.  
Let's just use the formula for roots directly from Vieta's relations.  
For monic polynomial: $\sum \alpha_i = -a_{n-1}$. Wait, let me verify again.  
Consider $(x-2)(x+2) = x^2-4$. Roots are 2 and -2. Sum is $2-2=0$. Formula gives $a_{n-1}$?  
If I write $P(x) = (x-\alpha_1)...(x-\alpha_n)$, then $P(0) = (-\alpha_1...-\alpha_n)$. Wait.  
Let's just evaluate $x^4+2x^3+2$. This polynomial equation is not satisfied by any number in the roots? No, it IS satisfied.  
The roots $\alpha_1, \dots$ satisfy $x^4+2x^3+2=0$.  
This means the roots are solutions to this equation.  
Vieta's formulas relate coefficients to elementary symmetric sums.  
Let $s_1 = \sum_{i=1}^n \alpha_i$, $s_2 = \sum_{i<j} \alpha_i \alpha_j$? No, usually it is $\prod (\alpha_i + \dots)$.  
For $x^n - e_1 x^{n-1} + e_2 x^{n-2} - \dots + (-1)^n e_n = 0$.  
Here roots are $\alpha_i$. So the coefficient of $x^3$ is $-s_1$. The coefficient of $x^2$ is $e_2$? No, it's something else.  
Wait, for $(x-\alpha)(x-\beta) = x^2 - (a+b)x + ab$.  
If we multiply these 4 terms, we get:  
$(x-\alpha_1)(x-\alpha_2)(x-\alpha_3)(x-\alpha_4)$  
$= x^4 - (\sum \alpha_i) x^3 + \dots$  
Let's re-verify this. $(x-a)x(b-c)?$ No, this is the product.  
Wait. Let me check with a small example.  
$x^2-x+1$. Roots $0.5, 0.5$. Wait. Sum of roots for $x^2-x+1$? No. $P(x)=x^4-3x+...$ no.  
Let's take $(x-1)(x-2) = x^2-3x+2$.  
Roots are $a,b$. $\alpha+\beta=-3$. $ab=2$.  
So in this case, the coefficient of $x^0$ is 2. The coefficient of $x^1$ is -3.  
For a degree 4 polynomial $P(x) = x^4 + c_1 x^3 + c_2 x^2 + \dots$, where roots are $\alpha_i$.  
If the equation is $x^4+2x^3+0x^2+0x+2$, then we have:  
$c_1 = 2$ (coeff of $x^3$). Wait, $x^3$ coefficient.  
Wait, if I write $(x-1)(x-\alpha)(x-\beta)(x-\gamma)$. No, just one factor.  
Let's assume the polynomial is written in form:  
$x^4 + a x^3 + b x^2 + c x + d = 0$.  
Then Vieta's relations (for roots $\alpha_i$):  
$\sum_{i} \alpha_i = -a$? Wait, $x^3$ term.  
Wait, $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \dots$  
Wait, if I multiply 4 of these to get a product of degree 4:  
$x^4 - s_1 x^3 + s_2 x^2 - s_3 x + s_4$.  
But wait. $(x-\alpha_1)(x-\alpha_2) = x^2 - (\sum \alpha_i) x + \dots$? No.  
Wait, $\prod_{i=1}^n (x-\alpha_i)$ is a polynomial in $x$. Let its coefficient of $x^{n-1}$ be $c_3$. Then $c_3 = -\sum_{i<j} \alpha_i \alpha_j$? No.  
Let's check $(x-a)(x-b)$. It is $x^2 - (a+b)x + ab$. Coeff of $x^{n-1}$ is 0 for degree 2. Wait.  
Wait, I am making an error in my memory of the sign relation between coeffs and roots.  
The correct relation is:  
If $P(x) = \prod_{i=1}^n (x-\alpha_i)$, then the coefficient of $x^{n-1}$ in $P(x)$ is $-\sum \alpha_i$.  
Wait, let's check $(x-1)(x-2) = x^2 - 3x + 2$. Coeff of $x$ is $-3$. $\sum \alpha_i = 3$. Wait. This matches the sign rule.  
So coeff of $x^{n-1}$ in expansion is minus sum of roots? No, plus?  
Wait. $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
If I write this as $x^2 - s_1 x + e_1$ where $s_1$ is the coeff of $x$. No, that's wrong.  
Wait. If I expand $(x-\alpha)(x-\beta) = (x-\alpha_x)(x-\alpha_x)$?  
$(x-a)(x-b) = x^2 - (a+b)x + ab$.  
If we write this in terms of sums, the coefficient of $x$ is $-(\alpha+\beta)$. So it's minus sum.  
Then multiplying by another degree 4 polynomial?  
Wait, let's assume roots are $\alpha_1, \dots, \alpha_n$.  
Then $(x-\alpha_1)...(x-\alpha_n)$ expanded as $c_k x^k + \dots$.  
The coefficient of $x^{n-1}$ in the expansion is $- \sum_{i<j} \alpha_i \alpha_j$? No.  
Wait, the relation between sum and coeff of $x$?  
$(x-a)(x-b) = x^2 - (a+b)x + ab$.  
If I want to write this as a polynomial with roots $\alpha_i$, then it must match the structure.  
But wait. The expansion $(x-\alpha_1)...(x-\alpha_n)$ is a specific polynomial.  
Its constant term is $(-1)^n \prod \alpha_i$.  
If this polynomial has a root $c_k$, what happens?  
Let's just look at Vieta again.  
$x^4 - e_1 x^3 + e_2 x^2 - e_3 x + e_4 = 0$.  
Here roots are $\alpha_1, \dots, \alpha_n$.  
Then $e_1 = \sum \alpha_i$? No. The coefficient of $x^1$ in $x^3-x+...$ is $-(a+b)$ where roots are $\alpha_i$? No.  
$(x-a)(x-b) = x^2 - (a+b)x + ab$. This has no $x^3$ term.  
Wait, if I write the polynomial as $(x-\alpha_1)...(x-\alpha_n)$.  
Expansion: $x^4 - (\sum \alpha_i)x^3 + (\sum_{i<j} \alpha_i \alpha_j)x^2 - (\sum_{i<j<k} \alpha_i \alpha_j \alpha_k)x + \prod \alpha_i$.  
This is correct.  
Let's check this formula against the example $(x-1)(x-2) = x^2 - 3x + 2$.  
Here $\sum \alpha_i = 3$ (coefficient of $x$). $\sum_{i<j} \dots = 0$.  
Wait, $\sum_{i<j} \alpha_i \alpha_j$ is for pairs? No, sum over all pairs. There are no other terms.  
So coefficient of $x^1$ is $-3$. The pair $\{1,2\}$ gives 1.  
Is there a pair $(a,b)$ such that $a+b=3$? Yes, if roots are $0.5$ and $-0.5$, sum is $0$. No.  
Wait, coefficients: $x^4 - \sum x^3 + \sum_{i<j} x^2 \dots$.  
Let's check $(x-1)(x-2) = x^2 - 3x + 2$.  
Is it possible that the coefficient of $x$ is $\sum \alpha_i$?  
If roots are $\alpha_1, \alpha_2$, then coeff of $x^0$ in expansion of $(x-\alpha_1)(x-\alpha_2)$ is $\prod \alpha_i$.  
And coeff of $x$ is $-\sum \alpha_i$.  
Wait. I am seeing a sign confusion.  
For example, $(x-1)(x-2) = x^2 - 3x + 2$.  
So if $P(x) = (x-\alpha_1)(x-\alpha_2)$, then coeff of $x$ is $-(\alpha_1+\alpha_2)$.  
And coeff of $x^0$ is $\alpha_1 \alpha_2$.  
If I multiply such a polynomial by $(x-3)$ and $(x+3)$? No.  
Actually, let's use the relation:  
$\prod (x-\alpha_i) = x^n + c_{n-1} x^{n-1} + c_{n-2} x^{n-2} + \dots + c_0$.  
The coefficient $c_{n-1}$ is $-\sum_{i=1}^n \alpha_i$? No.  
Wait, if $\alpha_i$ are roots of $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \dots$, then $P(x)$ should have coefficient $-(\alpha+\beta)$.  
So if the equation is $x^n - e_1 x^{n-1} + e_2 x^{n-2} - \dots + e_n = 0$, then $\sum \alpha_i = c_{n-1}$? No.  
Wait, let's check Vieta again carefully.  
For a polynomial $a_n x^n + a_{n-1} x^{n-1} + \dots + a_0$.  
If roots are $\alpha_i$, then:  
$\sum \alpha_i = -\frac{a_{n-1}}{a_n}$? No. Wait, this gives $\sum \alpha_i$ if $a_{n-1}$ is coeff of $x^{n-1}$.  
Wait, $(x-\alpha_1)...(x-\alpha_n)$ expansion:  
$x^4 - (\sum \alpha_i) x^3 + \dots$  
So coefficient of $x^3$ is $-\sum \alpha_i$.  
In our case $c_3 = 2$. So $\sum \alpha_i = -2$.  
Wait, but earlier I said sum is $-c_{n-1}$ which is $-c_3$.  
Let's recheck.  
$(x-1)(x-2) = x^2 - 3x + 2$.  
Roots are $1, 2$. Sum is $3$. Coefficient of $x$ is $-3$.  
So $\sum \alpha_i = -c_3$. Wait. The constant term in the example was 2.  
My formula gives coeff of $x$ as $-\sum \alpha_i$.  
Wait, if I multiply by $(x-\dots)$? No.  
Okay, let's check the product $(x-1)(x-2)(x-3)(x-4)$. This is a degree 4 polynomial.  
Expansion terms:  
$x^4$ coeff is 1.  
$x^3$ term comes from $-(\sum \alpha_i)$? No.  
Wait, I am getting confused with signs again.  
Let's write it out explicitly.  
$(x-\alpha_1)(x-\alpha_2) = x^2 - (\alpha_1+\alpha_2)x + \alpha_1\alpha_2$.  
$(x-\alpha_3)$? No, wait.  
I want the product of 4 such polynomials.  
$P(x) = \prod_{i=1}^n (x-\alpha_i)$.  
The terms are $x^k e_1 + \dots + e_k$.  
So $c_{-1} x^{-1}$? No.  
Let's just use the coefficients of $x^n, x^{n-1}, x^{n-2} \dots$  
If I define symmetric sums $\sigma_1, \dots, \sigma_n$.  
$\sum_{i=1}^n \alpha_i = \sigma_1$.  
$\sum_{i<j} \alpha_i \alpha_j = e_2$.  
Wait. This is not what Vieta says.  
The polynomial is $x^n + c_{n-1} x^{n-1} + \dots$.  
This means the coefficient of $x^k$ in $\prod (x-\alpha_i)$ is related to symmetric sums? No.  
Let's check example $(x-1)(x-2) = x^2 - 3x + 2$.  
Coefficients are 1, -3, 2.  
This means $n=2$. Coeff of $x$ is $-e_1 = -3$. $\sum \alpha_i = 3$. So $\sigma_1$ matches coeff of $x^{n-1}$? No.  
The term with highest degree in $(x-\alpha)(x-\beta)$ is $x^2$.  
If I write it as $x^k + c_{k-1} x^{k-1} + \dots$, then the coefficient $c_k$ is $(-1)^{n-k} \sigma_1$? No.  
Okay, let's look at the polynomial $(x-\alpha_1)...(x-\alpha_n)$ and its expansion.  
If $P(x) = x^4 - e_1 x^3 + e_2 x^2 - e_3 x + e_4$.  
Wait, is this correct? No. The term is $\sum (-\alpha_i) x^{n-1}$.  
Wait, let's verify with $(x-1)(x-2) = x^2 - 3x + 2$.  
This has degree 2. So $n=2$? No, the roots are not single terms.  
I mean $\alpha_1, \alpha_2, \dots, \alpha_n$ are roots.  
So let's assume I have roots $\alpha_i$.  
Then $(x-\alpha_1)...(x-\alpha_n)$ is a polynomial in $x$ of degree $n$.  
Its coefficient of $x^{n-1}$ is $-\sum_{i=1}^n \alpha_i$.  
So if equation is $x^4 + 2x^3 + 2 = 0$, then:  
Coefficient of $x^3$ is $2$. Wait, this means coeff of $x^{n-1}$ is 2?  
Wait. Let's check the sign again.  
For $(x-\alpha_1)...(x-\alpha_n)$, coefficient of $x^{n-1}$ is $-e_1$.  
So if equation is $x^4 + c_3 x^3 + \dots$, then $c_3 = -e_1$. So $e_1 = -2$? No.  
Wait, usually Vieta says $\sigma_k = (-1)^{k-1} \text{coeff of } x^{n-k}$ in expansion? No.  
Let's check $(x-1)(x-2)$. $P(x) = x^2 - 3x + 2$.  
$c_0 = 2$, $c_1 = -3$, $c_2 = 1$ (coeff of $x^2$). Wait.  
Let's rewrite $P(x)$ as $\sum a_k x^k$.  
$a_1 = \sigma_1$. No, $a_2 = \sum \dots$ No, let's stick to coefficients.  
$c_0$: $\prod \alpha_i$. In example $(x-1)(x-2) = x^2 - 3x + 2$, $c_0 = 2$. Wait.  
Wait, I'm mixing up roots and coefficients again.  
Let's use the explicit formula for $\prod_{i<j} \alpha_k$ or similar.  
Actually, let's just compute the set of values requested using Vieta's relations directly?  
Let $S_1 = \sum \alpha_i$. Let $S_2 = \sum_{i<j} \alpha_i \alpha_j$. Wait, is this $\sum \alpha_i \alpha_j$ or something else? No.  
Actually, for the equation $x^4 + 2x^3 + 2$, let's find the roots.  
Wait, I found earlier that it has no rational roots.  
Maybe I can factor it if it was reducible. But coefficients are integers.  
Let's try to factorize.  
$x^4+2x^3+2$.  
Is there a substitution $x = y + 1/2$? Or something similar?  
$(y+1)^4 - \dots$ no.  
Let's look at $x^4+2x^3+2$ in terms of $\alpha_i$.  
We know $e_1 = \sum \alpha_i = -2$. (Assuming standard sign convention: $(x-a)...(x-b) = x^n - e_1 x^{n-1} + e_2 x^{n-2} \dots$).  
Wait, for $P(x)=x^4+2x^3+2$, we have roots.  
If I write $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
This is not the full polynomial unless $\alpha_1 \dots \alpha_4$ are roots of a quartic.  
Wait, if $P(x)$ has roots $\alpha_i$, then $c_{n-1}$ (coeff of $x^{n-1}$ in expansion of product of $n-1$ factors) is related to sums.  
Let's restart with clear notation.  
Let $S_k$ be elementary symmetric polynomials of degree $k$.  
$e_1 = \sum \alpha_i = -2$? No, sign depends on convention.  
The equation is $x^4+2x^3+2=0$.  
Multiply by 0 to make coefficients integers? No.  
Wait, I should check if roots are real or not. If they are complex conjugate pairs, maybe there's a trick.  
Let's substitute $x = -1/2 y$ in some form?  
Maybe try $(x+1)^2 + \dots$.  
$x^4+2x^3+2$. Roots $\alpha_i$ satisfy this.  
Is it possible that $\alpha_1 = 1$, etc.  
Let's check for rational roots again. Divisors of 2: $\pm 1, \pm 2$.  
$(-1)^4 + 2(-1)^3 + 2 = 1 - 2 + 2 = 1 \neq 0$.  
$(+1)^4 + 2(1) + 2 = 5 \neq 0$.  
So no integer roots.  
But roots are complex.  
Since roots of $x^4+2x^3+2$ are likely not real, maybe I should just look for the set product values.  

Let's consider the expression $\alpha_1 \alpha_2 + \alpha_3 \alpha_4$.  
Is it related to something like $(\alpha_1+\alpha_2)(\alpha_3+\alpha_4)$? No.  
Maybe it is simpler:  
$\alpha_1 \alpha_2 + \alpha_3 \alpha_4 = (\sum \alpha_i)^2 - \sum_{i<j} \alpha_i \alpha_j$? No.  
Wait, $\sum \alpha_i \alpha_j$ involves pairs. $\alpha_1 \alpha_2 + \alpha_3 \alpha_4$ is a specific subset of products.  
If we can write the polynomial $P(x)$ in terms of these sums.  
Let's check if the roots are $\alpha_i$.  
Wait, is it possible that $\sum \alpha_i = 0$?  
No. Coefficient of $x^3$ is 2, so sum is -2 (or 2 depending on sign).  
Actually, I will use standard Vieta:  
If $P(x) = a_n x^n + c_{n-1} x^{n-1} + \dots$, then $\sum \alpha_i = -c_{n-1}/a_n$? No. Wait.  
Let's check $(x-1)(x-2)$. Coeff of $x^0$ is 2, coefficient of $x$ is -3. Sum of roots is 3.  
So $\sum \alpha_i = c_1$ where $c_1=-2$ for $x^4+2x^3$. Wait.  
Wait. $(x-1)(x-2) = x^2 - 3x + 2$.  
If I write this as product of roots $\{a,b\}$: $P(x) = (x-a)(x-b) = x^2 - (\sum a)x + \prod a$.  
In $x^4+2x^3$, the coefficient of $x^1$ is 2? Wait.  
My polynomial in equation is $x^4 + 2x^3 + 2$.  
Wait. This implies $c_1 = 2$.  
So $\sum \alpha_i = -2$.  
Wait, let's check if the sign rule is consistent with this.  
If roots are $\alpha_i$, then $(x-\alpha_1)...(x-\alpha_n) = x^n - (\sum \alpha_i) x^{n-1} + \dots$? No.  
$(x-1)(x-2) = x^2 - 3x + 2$. Coeff of $x^0$ is 2, coeff of $x$ is -3.  
Wait, this matches if $\sum \alpha_i = 3$. Wait. The coefficient of $x^3$ in expansion is zero? No.  
The term is $x^4 - (\sum \alpha_i) x^3 + \dots$  
Wait, for degree 2 polynomial:  
$x^2 - (\sum \alpha_1) x + \dots$.  
Here coeff of $x^0$ is $\prod \alpha_1$.  
In my equation, coeff of $x^0$ is 2.  
So $\prod \alpha_i = 2$.  
Also coeff of $x$ is $-(\sum \alpha_i)$? No, it's $-(\alpha_1+\alpha_2)$.  
But in $(x-1)(x-2)$, the term with coeff $x^0$ is $2$.  
So if I have degree 4 polynomial:  
$x^4 + 2x^3 + 2 = 0$.  
Coeff of $x^3$: 2.  
This means $\sum \alpha_i = -(-2)$? No. Wait, for a monic polynomial $P(x) = x^4 - e_1 x^3 + e_2 x^2 - e_3 x + e_4$.  
Then coefficient of $x^3$ is $-e_1$.  
Here we have $x^4+2x^3+2$.  
So $e_1 = 2$.  
Wait, if this holds, then sum of roots $\alpha_i = -2$.  
Let's check example: $(x-1)(x-2)$. Sum is 3. Coeff of $x$ is -3. Here $e_1=3$. Matches.  
Wait, I am assuming the polynomial in standard form has constant term $+a$.  
For equation $x^4+2x^3+2$, the coefficients are $1, 2, 0, 0, 2$? No.  
$x^4+2x^3+2$ means:  
$a_4 = 1$.  
$a_3 = 2$.  
$a_2 = 0$.  
$a_1 = 0$.  
$a_0 = 2$.  
Wait, in standard Vieta form $x^n + c_{n-1} x^{n-1} + \dots$, the sign is minus.  
So $x^4 - (a_3) x^3 + e_2 x^2 - e_3 x + e_4$. No.  
Let's check again.  
$x^4+2x^3+...$ implies coeff of $x^3$ is 2? Or maybe the sum of roots is 2?  
Wait, I need to be very careful about signs.  
Let's verify with $(x-1)(x-2) = x^2 - 3x + 2$.  
Roots are $\alpha_1, \alpha_2$. $\sum \alpha_i = 1+2=3$.  
Polynomial is $x^2 - (\sum \alpha_i)x + \prod \alpha_i$. No. $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
So coefficient of $x$ is $-(\alpha+\beta)$ and constant term $\alpha\beta$.  
Wait, the expansion $(x-\alpha_1)...(x-\alpha_n)$ has:  
Term $x^{n-1}$ (coefficient of $x^3$ in $x^2-x...$): $-\sum \alpha_i$.  
Here coeff is 0? No.  

*Continued in [part 3 of 4](intermediate_algebra_2015_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
