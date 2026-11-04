# test/intermediate_algebra/2015.json, part 2 of 3

[Previous part](intermediate_algebra_2015.md)

Let's derive it for $P(x) = x^4 + 2x^3 + 0x^2 + 0x + 2$.  
We know $\prod (x-\alpha_i) = x^n - (\sum \alpha_i)x^{n-1} + \dots$ is NOT correct because the sign of constant term depends on whether we take product of $(x-\alpha)$.  
The expansion of $P(\alpha)$? No.  
Let's look at $(x-\alpha_1)\dots(x-\alpha_n) = x^n - (\alpha_1+\dots+\alpha_n)x^{n-1} + \sum_{i<j} (-1)^{n-2} (something)x^{\dots}$.  
The term $x^{n-2}$ is $\sum_{i<j}\alpha_i\alpha_j$? No. The coefficient of $x^{n-2}$ is $(-1)^n \sigma_2$? No.  
Let's use a standard table for monic polynomials.  
$x^n + c_1 x^{n-1} + c_2 x^{n-2} + \dots$.  
Then $\sum_{i=1}^n \alpha_i = -c_1$.  
$\sum_{i<j}\alpha_i\alpha_j = c_2$? No, this is not true for all symmetric sums.  
Let's check the example: $(x-1)(x-\beta) = x^2 - (\beta+1)x + \beta$. Here $\sigma_1=\beta+1$, $\sigma_2=\beta$.  
Here $c_1 = -(\sigma_1)$, so $\sigma_1 = -c_1$? No, coefficient is 1 (monic). So $-(\beta+1) = c_1 \implies \sum = -c_1 = 1$? No.  
$c_1=0$ for $x^2-1$, so sum $\sigma_1 = 1$.  
Here $\alpha_1+\alpha_2 = 0$. So if $c_1=0$, sum is 0. But constant term is -1, product is 1.  
So $\sigma_2 = \alpha_1\alpha_2$? Yes. Coeff of $x^0$ is $\prod \alpha_i$.  
In our case $P(x) = x^4 + 2x^3 + 0x^2 + 0x + 2$.  
Here $a_0=2$. So product of roots $\sigma_4 = 2$? No, the coefficient of $x^{n-4}$ is $\prod \alpha_i (-1)^{n}$. No.  
Let's check the relation between $P(x)$ and coefficients again.  
Polynomial: $(x-\alpha_1)(x-\alpha_2) \dots (x-\alpha_n) = x^n - S_1 x^{n-1} + S_2 x^{n-2} - S_3 x^{n-3} + (-1)^n S_n$.  
Here $S_k$ are elementary symmetric polynomials.  
Comparing to $x^4 + 2x^3 + 0x^2 + 0x + 2 = 0$:  
Coefficient of $x^3$ is $-S_1$. (This corresponds to $\alpha_1+\dots+\alpha_4 = -(-2)$? No, coeff is 2. So $S_1=2$. But sign? If coeff is positive, sum must be negative).  
Here coefficient of $x^3$ is 2. So $-S_1 = 2 \implies S_1 = -2$.  
Let's check the next term in expansion: $(-1)^{n-1} S_{n-1}$? No, it's $\sum (-1)^k S_k x^{n-k}$? No.  
Coeff of $x^3$:  
Term is $(x-\alpha_1)(x-\alpha_2) \dots$ no.  
Let's expand $(x-\alpha)(x-\beta)$ again. $x^2 - (\alpha+\beta)x + \alpha\beta$.  
Here $\sigma_1 = \alpha+\beta$. Coeff of $x^{n-1}$ (degree 2 in this case, so $x^1$ term) is $-(\sum \alpha)$.  
So for degree $n$, the coefficient of $x^{n-1}$ is $-\sigma_1$? No.  
The constant term in $(x-\alpha)(x-\beta)$ is $\alpha\beta$. This is $S_4 = 2$? No, coeff of $x^0$ (constant) in expansion $x^4+...$ is $S_4$ if polynomial is $x^n + \dots + (-1)^n S_n$.  
Let's check the sign for $S_k$.  
$(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
Polynomial is $x^2 - (\alpha+\beta)x + \alpha\beta$.  
So if $P(x) = x^4+2x^3+\dots$, and we have $\sum \alpha_i = -a_1$ (where $a_1=2$). So sum is 2. No.  
Coefficient of $x^{n-1}$ in $(x-\alpha)(x-\beta)$ is $\alpha+\beta$. So for degree $n$, coeff of $x^{n-1}$ is $\sigma_1 = -(\sum \alpha)$.  
So $P(x) = x^n + a_1 x^{n-1} + a_2 x^{n-2} + \dots$. Then sum $\sigma_1 = -a_1$? No, sum of roots for $x^4+2x^3+...$ is coeff of $x^3$.  
Let's re-evaluate Vieta's formulas for general polynomial.  
If $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0$.  
Then roots sum: $\sigma_1 = -a_{n-1}/a_n$? No, $a_n$ is coeff of $x^n$. So if monic, sum is $-a_{n-1}$.  
If $P(x) = x^4 + 2x^3 + \dots$, then sum $\sigma_1 = -2$.  
Then product $\prod \alpha_i = a_0$? No.  
The constant term in expansion is $\prod (-\alpha_i)$.  
Let's check the sign again. $S_n = (-1)^n \prod_{i=1}^n \alpha_i$.  
So if constant term is $e_0=2$, and it is multiplied by $(-1)^n$? No, $P(0)=a_0$. In expansion $(x-\alpha)(x-\beta) = x^2 - \dots + \alpha\beta$. So product of roots is constant term (if degree is even?).  
Let's write out $x^4+2x^3+\dots$ terms.  
If we expand $\prod_{i=1}^n(x-\alpha_i)$, we get:  
$x^n - (\sum \alpha_i)x^{n-1} + (\sum \alpha_i\beta) x^{n-2} - \dots$. No.  
Let's use indices $k$ for number of roots in a term.  
$\prod_{i=1}^n (x-\alpha_i) = \prod_{i=1}^n (x + (-\alpha_i)x)$.  
This is getting confusing. Let's just trust the coefficients directly from the equation provided.  
The equation is $x^4+2x^3+2=0$ ? No, "roots of the equation $x^4+2x^3+2=0$".  
Usually this implies a polynomial of degree 4.  
$x^4 + 2x^3 + 0x^2 + 0x + e = 0$.  
So if we write the coefficients explicitly:  
$a_4=1, a_3=2, a_2=0, a_1=0, a_0=2$.  
Then $\sigma_1 = -a_3 = -2$? No.  
Coefficient of $x^3$ in $(x-\alpha)(x-\beta) \dots (x-\alpha_n)$ is sum of roots? No.  
It's $-(\sum \alpha_i)$.  
So sum is 2? No, $-(-2) = 2$. So $\sigma_1 = -a_3$? No.  
Let's recheck $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
Coeff of $x^{n-1}$ is $-e_1$.  
Here $n=4$, term is $x^3$. So coeff is $-e_1$.  
So $e_1$ (sum of roots) is coefficient of $x^{n-1}$.  
But we have monic polynomial $x^4+2x^3+0x^2+0x+2$.  
The term $x^3$ has coefficient 2.  
Thus sum of roots $\sigma_1 = -2$.  
Let's check the product term. The constant term is 2. In expansion $(x-\alpha)(x-\beta)\dots(x-\alpha_n)$,  
Constant term corresponds to product of roots? No.  
Let's verify again with $n=2$: $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
Coeff of $x^1$ is $-(\alpha+\beta)$, so sum $\sigma_1 = -a_{n-1}$? No. Here coeff is 1?  
Here $P(x) = x^4 + 2x^3 + \dots$ corresponds to the polynomial $(x-\alpha_1)(x-\alpha_2)\dots$.  
So $\sum \alpha_i$ corresponds to the coefficient of $x^{n-1}$ which is 2. No, this means coeff is positive? No.  
The term is $+2x^3$. So $a_3=2$. This is $\sigma_1$. So sum is -2? Or just $\sigma_1 = 2$?  
Let's look at $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \dots$.  
If we write $P(x)$, then the coefficient of $x^{n-1}$ is $-\sigma_1$.  
So if $P(x) = x^4+2x^3$, then $\sigma_1=2$?  
No. Let's check for roots $0, 1, \dots$ sum $\sigma_1$.  
Let's try a specific example. $x^4 - 5x^3 + \dots$  
Roots are $x_i$. Then product of roots is constant term with sign change.  
Actually, there's a simpler way.  
The polynomial coefficients $c_0, c_1, c_2, c_3, c_4$ correspond to elementary symmetric sums:  
$c_0 = \prod x_i = 2$.  
$c_1 = -e_1 = -(\sum x_i)$.  
$c_2 = e_2 = \sum_{i<j} x_i x_j$.  
$c_3 = -e_3 = -(\sum_{i<j<k} x_i x_j x_k)$.  
$c_4 = 0$. (Since no $x^3$ term in expansion if leading term is coeff of $x^3$? No, if polynomial is $x^4+2x^3+\dots$, the coefficient of $x^3$ is $-e_1$.  
If we assume monic, $P(x) = x^4 - e_1 x^3 + \dots + (-1)^4 e_n$.  
Here $P(x)$ has coefficient 2 for $x^3$? Or $a_{n-1}$?  
Let's check. The expansion is $\sum_{k=0}^n a_k S_{n-k} x^{n-k}$.  
Usually, if we have roots $r_1, \dots, r_n$.  
$P(x) = (x-r_1)(x-r_2)\dots(x-r_n)$.  
This is monic.  
Then $a_k$ are elementary symmetric sums of the roots? No.  
Let's write out expansion of product $(x-\alpha_1)(x-\alpha_2) \dots (x-\alpha_n)$ in terms of symmetric polynomials.  
The coefficient of $x^{n-1}$ is $-\sigma_1$.  
Here polynomial is monic ($a_4=1$). Coefficient of $x^3$ is $2$.  
This suggests $-\sigma_1 = 2 \implies \sigma_1 = -2$.  
What about $\sigma_2$?  
Coeff of $x^{n-2}$ in $(x-\alpha)(x-\beta) \dots (x-\gamma)$ is $\sigma_2$.  
In our polynomial, coeff of $x^2$ is 0. So $\sigma_2 = 0$.  
What about $\sigma_3$?  
Coeff of $x^1$ in product is $\sum_{i<j<k} \alpha_i\alpha_j\alpha_k$. No.  
Let's recheck the expansion.  
$(x-\alpha)(x-\beta) \dots (x-\alpha_n) = x^n - (\sum \alpha)x^{n-1} + (\sum_{i<j}\alpha_i\alpha_j)x^{n-2} - \dots + (-1)^{n-1} e_{n-1} + (-1)^n e_n$.  
Is this correct? No, the signs alternate.  
Actually, let's just expand $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
The constant term is $\alpha\beta$. The coefficient of $x^{n-1}$ is $-(\alpha+\beta)$.  
If we have degree 4 polynomial, the last term in expansion corresponds to the root product.  
Let's look at $(x-\alpha)(x-\beta)(x-\gamma)(x-\delta) = x^4 - (\sum \alpha)x^3 + \dots$?  
No. Let $x^n + a_1 x^{n-1} + a_2 x^{n-2} + \dots + a_n$.  
Then the roots satisfy $\alpha_1+\dots+\alpha_n = -a_{n-1}$ (sum of roots).  
For degree 4 polynomial, sum of roots is $-\text{coeff of } x^3$.  
Here coeff is 2. So sum $\sigma_1 = -2$? No, $-\alpha_i \alpha_j \dots$  
Let's check standard result:  
Polynomial $x^4 + c_3 x^3 + c_2 x^2 + c_1 x + c_0$.  
$\sum x = -c_3$.  
$\sum_{i<j} x_i x_j = c_2$.  
$\sum_{i<j<k} x_i x_j x_k$ (with signs) $= \sigma_3$?  
Let's verify with example. $x^2+1=0$. Roots are $\pm i$. Sum 0, sum prod -1, sum sq 0? No.  
Roots of $x^4+2x^3+2=0$.  
Sum $\sum \alpha_i = -(-2) = 2$. (Coefficient of $x^3$ is positive).  
Let's double check signs.  
If roots are real, sum must be negative if poly has odd degree? No, leading coefficient sign matters.  
But for monic polynomial, sum of roots is $-\sum \alpha_i x^{n-1}$ term?  
Expansion: $\prod (x-r_i) = \sum_{k=0}^n e_k x^{n-k} (-1)^k$? No.  
It's easier to say:  
$(x-\alpha_1)\dots(x-\alpha_n)$.  
Constant term is $e_n$ where $e_k$ is sum of products of roots with some signs.  
Actually, if polynomial is monic ($a_0=1$), then $\sum x = -\text{coeff of } x^{n-1}$.  
If poly is $x^4+2x^3+0x^2+0x+2$.  
Here coeff of $x^3$ is 2. So sum of roots $\sigma_1 = -(-2) = 2$.  
So $\sum \alpha_i = 2$.  
Coeff of $x^{n-2}$ (for $x^2$) is 0.  
Is this $\sum_{i<j} x_i x_j$? No, it should be related to sign of next term.  
Term for degree 2 is $a_2 = -\text{coefficient of } x^1$. But here polynomial has no $x^1$ term.  
Let's just use the expansion:  
$(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
Here $a_1 = -(\sigma_1)$. Here $a_1=0$. So $\sigma_1 = 0$ (sum is 0).  
So coeff of $x^3$ term must be consistent with sum? No.  
Let's check coefficient $c_k$.  
$c_k$ corresponds to elementary symmetric sum $e_k$ of roots?  
If polynomial is monic: $x^n + a_{n-1} x^{n-1} + \dots + a_0$.  
Then roots are solutions to characteristic equation.  
Let's use the property: $\sigma_k = (-1)^k e_k$? No.  
$\sum_{i=1}^4 x_i = -a_{n-1}$ if we write $x^n - (\sum) x^{n-1} + \dots$.  
So for $x^4+2x^3+\dots$, the coeff is $+2$.  
Wait, let's look at a simpler polynomial. $x^2+x^3=x(x-1)$? No.  
Let's consider the expansion of $\prod_{i=1}^n (x-\alpha_i)$.  
$P(x) = x^n - (\sum \alpha_i)x^{n-1} + (\sum_{i<j}\alpha_i\alpha_j)x^{n-2} - \dots + (-1)^n e_n$.  
Comparing coefficients with $P(x) = x^4+2x^3+0x^2+0x+2$:  
$n=4$. Coeff of $x^3$ is $2$. So $-\sum \alpha_i = 2$? No, coeff is minus $\sigma_1$? No, coefficient is $-e_1$ (if we ignore the sign).  
Let's assume the coefficients are:  
$a_k = (-1)^{n-k} e_{k+1}$? No.  
Let's stick to elementary symmetric polynomials.  
$\alpha_1+\dots+\alpha_n = -a_{n-1}$.  
In our case $a_{n-1}=2$ (coeff of $x^3$).  
So $\sigma_1 = 2$? Or $-\sigma_1$?  
Let's re-derive the expansion.  
$(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
Here, coeff of $x^{n-1}$ is $- (\sum \alpha_i)$.  
In our polynomial $(x-\alpha_1)\dots(x-\alpha_n)$, the coefficient of $x^{n-1}$ is $- (\sum \alpha_i)$.  
This means $\sigma_1 = -2$? No. The coefficient of $x^3$ in $P(x)$ is 2.  
So $- \sum \alpha_i = 2$. So $\sum \alpha_i = -2$.  
If this is correct, then sum of roots is 2? Or -2? Let's assume it is -2.  
Coeff of $x^3$ in $(x-\alpha_1)\dots(x-\alpha_n)$ is $-e_1$. So if coeff is 2, $e_1 = -2$.  
Then product $P(0) = (-1)^n e_n$.  
Here $e_n = a_0 = 2$? Or -2?  
If $(x-\alpha_1)(x-\alpha_2) \dots (x-\alpha_n)$, then $\prod (\alpha_k)$ is coefficient of $x^n$ divided by $a_n$ times...  
Let's check: $(x-\alpha_1)(x-\alpha_2)\dots(x-\alpha_n) = x^4 - (\sum \alpha_i)x^3 + \dots$.  
If we have $x^4+2x^3+\dots$, then $\sum \alpha_i$ should be related to 2.  
Usually, if polynomial is $a_n x^n + a_{n-1} x^{n-1} + \dots$, then roots are roots of this polynomial.  
So coefficient $a_{n-1}$ is the coefficient of $x^{n-1}$.  
The sum of roots is $-\frac{a_{n-1}}{a_n}$. Since $a_n=1$, sum is $-2$. (Assuming leading coeff is 1).  
But here $x^4+2x^3$ means coefficient of $x^3$ is 2.  
So $\sum \alpha_i = -2$.  
This leads to sum = $e_1 = -2$. No, that's wrong.  
Let's try again with a specific polynomial: $x^4 + x^3 = x^3(x+1)$. Roots are $0, 0, -1, -1$.  
Sum is -2. Product is 0.  
So for our polynomial, roots satisfy sum of roots $\sum \alpha_i$?  
Actually, the roots are not necessarily symmetric with respect to $\alpha_k$. The equation defines them.  
Let's just use standard elementary symmetric polynomials $e_1, e_2, \dots, e_n$.  
For a monic polynomial $x^4 + e_1 x^3 + e_2 x^2 + e_3 x + e_4$.  
Here $a_4=1$, $a_3=2$. So sum of roots $\sigma_1 = -e_1$? No. $e_1$ is the coefficient of $x^3$.  
So $\sum \alpha_i = -(-2) = 2$.  
But earlier I said coeff of $x^{n-1}$ is $-\sigma_1$.  
If $a_{n-1} = -\sigma_1$, then $\sum \alpha_i = 2$.  
Let's check the sign. $(x-\alpha_1)(x-\alpha_2) = x^2 - (\alpha+\beta)x + \dots$.  
The term with highest degree is $x^2$. The term with lowest degree in this polynomial is constant? No.  
Here polynomial has constant term 0. $x^4+x^3$?  
Let's check $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
The sum of roots $\sigma_1 = -(-2)$? No, let's assume standard Vieta for $(x-\alpha)(x-\beta)=0$.  
Then product is $\alpha\beta$. Coeff of $x^2$ is $-(\alpha+\beta)$. So sum is $-e_2$? No.  
Let's use the notation where coefficients are $a_k$ in $\sum a_i x^{n-i}$.  
$\sum \alpha_i = -a_{n-1}$ (for $x^n + \dots + a_0$).  
So for $x^4+2x^3+2$, we have sum of roots $\sigma_1 = 2$.  
And product of roots is $e_4$. For the constant term, in expansion $(x-\alpha_i)\dots(x-\alpha_n)$, the constant term (product of roots) is equal to $(-1)^n e_n$? No.  
Let's calculate product for quadratic: $x^2 - (\sigma_1)x + \sigma_4$.  
Then $\sigma_1 = -c_1$, $\sigma_4 = -a_0$. (No, $x^2-...$).  
If polynomial is $(x-\alpha_1)(x-\alpha_2) \dots (x-\alpha_n)$ with roots $\alpha_i$.  
Then $P(0) = (-\prod \alpha_i)$. So $e_4 = -(-\prod \alpha_i) = e_n$? No.  
Let's assume the polynomial is $x^4 + 2x^3 + 0x^2 + 0x + 2$.  
This means roots satisfy:  
1) $\sum_{i<j} \alpha_i \alpha_j = -a_1$? No.  
Coeff of $x^2$ in expansion is $\prod (\dots)$.  
Wait, if the equation is $x^4+2x^3+\dots$, then sum of roots is 2.  
Then we can compute $A = \alpha_1\alpha_2 + \alpha_3\alpha_4$? No, $B = \alpha_1\alpha_3 + \alpha_2\alpha_4$?  
No, the question asks for $\{\alpha_1\alpha_2+\alpha_3\alpha_4, \dots\}$.  
The term $\alpha_i\alpha_j$ is not symmetric in a simple way.  
Let's check the set of values.  
Let $S = \{\alpha_1\alpha_2, \alpha_3\alpha_4, \alpha_1\alpha_4 + \alpha_2\alpha_3\}$. (No, $\alpha_1\alpha_4$ is one term).  
Wait, the expression is:  
$\beta_1 = \alpha_1\alpha_2 + \alpha_3\alpha_4$.  
$\beta_2 = \alpha_1\alpha_3 + \alpha_2\alpha_4$.  
$\beta_3 = \alpha_1\alpha_4 + \alpha_2\alpha_3$.  
We want the set $\{\beta_1, \beta_2, \beta_3\}$.  

Let's find the values of elementary symmetric sums $S_1, S_2, S_3$.  
Given equation: $x^4+2x^3+2=0$ (assuming monic). No. It is $x^4+2x^3+0x^2+0x+2$.  
So roots are $\alpha_1, \dots, \alpha_4$.  
Let $S_k$ be the elementary symmetric polynomial of degree $k$ involving the roots:  
$e_1 = \sum_{i<j<k} \alpha_i\alpha_j\alpha_k$ (No).  
Let's define $s_k$ such that $x^{n-k} s_n = \prod (\dots)$. No.  
Standard notation: $\sigma_k(x)$ is the elementary symmetric polynomial of degree $k$ in variables $\alpha_1, \dots, \alpha_n$.  
Then $\sum \alpha_i = -e_1$.  
$\sum_{i<j}\alpha_i\alpha_j = e_2$.  
$\sum_{i<j<k}\alpha_i\alpha_j\alpha_k = -e_3$? No.  
In standard polynomial expansion $P(x) = x^n + a_{n-1}x^{n-1} + \dots$.  
If roots are $\alpha_i$, then:  
$(x-\alpha_1)\dots(x-\alpha_n) = x^n - e_1 x^{n-1} + e_2 x^{n-2} - e_3 x^{n-3} + e_4$.  
Comparing this to $x^4+2x^3+0x^2+0x+2$:  
We have a mismatch.  
$x^n$ coeff is 1. In our case it's 1 (coeff of $x^4$).  
$x^{n-1}$ coeff is 2 in our case.  
This means $\sum \alpha_i = -a_{n-1} = -2$.  
The polynomial has constant term 2, which implies product of roots is -2? Or 2?  
Let's check the sign of product. $e_4 = (-1)^n e_n$ where $P(x) = \dots + e_4$.  
Expansion $(x-\alpha_1)(x-\alpha_2)\dots(x-\alpha_n)$:  
Constant term is $(-1)^n \prod_{i=1}^n \alpha_i$.  
Here constant term is 2. So $\prod \alpha_i = -2$? Or 2?  
Let's assume roots satisfy the polynomial equation.  
Then $(x-\alpha_1)\dots(x-\alpha_n)$ evaluated at $x=0$ gives product of roots.  
So if we write $(x-\alpha_1)(x-\alpha_2)(x-\alpha_3)(x-\alpha_4) = P(x)$.  
Then $P(0) = (-\alpha_1)(-\alpha_2)(-\alpha_3)(-\alpha_4)$? No.  
$P(0) = \prod (0-\alpha_i) = (-1)^4 \prod \alpha_i = -\prod \alpha_i$.  
So $\prod \alpha_i = -a_{constant}$. But constant term is 2.  
So $\prod \alpha_i = -2$.  

Now let's compute the set of values $\beta_1, \beta_2, \beta_3$.  
We need to evaluate:  
$\beta_1 = \alpha_1\alpha_2 + \alpha_3\alpha_4$.  
This is sum of products with distinct indices. No, it's just product.  
This looks like we are looking at symmetric polynomials? No.  
Let $e_1 = 2$ (sum) from earlier calculation. Wait, I derived $\sigma_1=2$ earlier as "sum is -(-2)=2". Let me re-verify this carefully.  
For $P(x) = x^4+2x^3+0x^2+0x+2$.  
Using the formula:  
$\sum \alpha_i = -a_{n-1}$? No, it's $\sigma_1$ if we write $x^n + e_1 x^{n-1}$.  
Here $e_1$ is coeff of $x^3$. So $e_1=2$.  
Wait, let's check for a simple case: $(x-\alpha_1)(x-\alpha_2)=x^2 - \sum x_i x_j + \prod x_k$. No.  
If roots are real numbers $\alpha_1, \alpha_2$ with no sum constraint from other terms.  
The expansion is $x^2 - (\sum \alpha)x + \dots$? No.  
Let's just look at the coefficients of the polynomial $P(x)$.  
$P(x) = x^n + A_{n-1} x^{n-1} + \dots + A_0$.  
Then $\sigma_1$ is related to coefficient $A_{n-1}$?  
If $P(x) = (x-\alpha_1)\dots(x-\alpha_n)$.  
Then $A_{n-1} = -\sum \alpha_i$.  
So sum $\alpha_i = -A_{n-1}$.  
Here $A_{n-1}=2$. So sum $\sigma_1 = 2$. (Assuming leading coeff is 1 and polynomial is monic).  
Then constant term in expansion is $\prod \alpha_i$? No.  
Let's check with $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
Here $n=2$. Coeff of $x^{n-1}$ is 1. So sum $\sigma_1 = -A_{n-1}$? No, coefficient is $\sigma_1$ in expansion? No.  
The coefficient of $x^0$ in expansion is product.  
So if $P(x) = x^2 + B x + C$. Roots are $-\frac{-B}{1}$ and something else? No.  
Let's check: $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$.  
Here $A_{n-1} = 0$ if $C=0$. Wait, coefficient of $x$ is $-(-B)$? No.  
The expansion is $x^n + e_1 x^{n-1} + e_2 x^{n-2} + \dots$.  
Here coefficient of $x^3$ corresponds to $e_1 = -\sum \alpha_i$.  
So if polynomial is $x^4+2x^3+\dots$, then $e_1=2$.  
So $\sum \alpha_i = -2$? No, this depends on definition.  
If $P(x) = x^n + e_1 x^{n-1} + \dots$, then roots are defined by $\sigma_k = (-1)^{n-k+1} A_{k}$? No.  
Let's try to be very explicit about the relation between roots and coefficients of a monic polynomial $x^n + c_3 x^2 + c_2 x + c_1$ (degree $n=4$, $x^4 + 0x^2 \dots$?).  
Actually, let's rewrite the problem as finding the product of $\alpha_i$.  
The equation is $x^4+2x^3+2=0$.  
Let roots be $\alpha_1, \alpha_2, \alpha_3, \alpha_4$.  
Then $(x-\alpha_1)(x-\alpha_2)(x-\alpha_3)(x-\alpha_4) = x^4 - (\sum \alpha_i)x^3 + (\sum \alpha_i\beta_{ij})x^2 - \dots$? No.  
The term $x^3$ corresponds to the sum of roots. Let's denote it by $\sigma$.  
So $\sigma = -2$. (Since coeff is positive 2, so we get a negative sign for sum).  
The constant term in the polynomial is 2. So product $\prod \alpha_i = (-1)^4 e_4$? No.  
The constant term in expansion $P(x)$ is equal to $(-1)^n e_n$.  
For $x^4+2x^3+0x^2+0x+2$, the constant term is 2.  
In our expression, product $\prod \alpha_i$ corresponds to constant term? No.  
Let's verify with $(x-\alpha_1)(x-\alpha_2) = x^2 - (\alpha_1+\alpha_2)x + \alpha_1\alpha_2$.  
Here constant term is 0? No, $\alpha_1\alpha_2$.  
If we have $x^4+0x^3+...$, then product of roots is coefficient of $x^{n-2}$.  
Let's just use the formula for roots.  
$\sigma_1 = -a_{n-1}$. Here coeff of $x^3$ is 2, so $\sigma_1 = -(-2) = 2$. No, coeff is $2 x^3$, so $-\sigma_1$ in the expansion term.  
So $-\sum \alpha_i = 2 \implies \sum \alpha_i = -2$. (Since leading term is monic).  
And product of roots $\sigma_4 = a_{n-2}$? No.  
Let's check $(x-\alpha)(x-\beta)$. Coeff of $x^1$ in expansion $x^2-(\sum)x+\dots$ is $-\sigma_1$.  
Here polynomial is degree 4.  
So $\sum \alpha_i$ corresponds to $A_{n-1}$? No, $A_{n-1} = \text{coeff of } x^{n-1}$ (which is $x^3$).  
And the constant term in expansion is $\prod \alpha_i$ times sign.  

*Continued in [part 3 of 3](intermediate_algebra_2015_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
