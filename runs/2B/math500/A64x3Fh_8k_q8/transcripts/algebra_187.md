# test/algebra/187.json (Algebra, level 4)

> Suppose that $f$ is a polynomial such that \[(x-1)\cdot f(x)=3x^4+x^3 - 25x^2 +38x -17.\]What is the degree of $f$?  

**Correct.** Gold `3`, predicted `3`. Finish: stop, 7486 tokens, 0 waits, 1055.2 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's my thought process for solving this problem:  

1.  **Analyze the Request:** The user wants to find the degree of a polynomial $f(x)$ given an equation involving a product $(x-1)f(x)$ equal to another polynomial $3x^4 + x^3 - 25x^2 + 38x - 17$.  

2.  **Identify the Given Equation:**  
Let $P(x) = 3x^4 + x^3 - 25x^2 + 38x - 17$.  
The equation is $(x-1)f(x) = P(x)$.  

3.  **Define the Goal:** Find the degree of $f(x)$, denoted as $\deg(f)$.  

4.  **Recall Properties of Polynomials:**  
    *   If $g(x)$ is a polynomial and $c$ is a non-zero constant, then $a(x-1)^n g(x)$ is not applicable here directly unless it's factoring.  
    *   The leading coefficient of $(x-a)h(x)$ depends on the leading terms.  
    *   If $\deg(f) = n$, then $f(x) \approx a_n x^n + \dots$ where $a_n \neq 0$.  
    *   Let's analyze the term $(x-1)f(x)$.  
$(x-1)f(x) = (x)(f(x)) - 1(f(x))$.  
The degree of the product of a polynomial $A(x)$ and another polynomial $B(x)$ is generally $\deg(A) + \deg(B)$, unless there's a common factor that cancels out or reduces the degree (which happens if the roots match, i.e., $(x-x_0)^2$ factor).  
    *   Specifically, $\deg((x-1)f(x)) = \deg(f(x)) + 1$, provided $f(x)$ is non-zero.  

5.  **Determine $\deg(P(x))$:**  
Looking at the term $3x^4$, the polynomial $P(x)$ has degree 4 (since the coefficient of $x^4$ is 3, which is not zero). So, $\deg(P) = 4$.  

6.  **Relate Degrees:**  
We know that $(x-1)f(x) = P(x)$.  
Assuming $f(x)$ is a polynomial (which the problem states), we can compare the degrees.  
Let $n = \deg(f)$.  
The leading term of $(x-1)f(x)$ depends on the leading term of $f(x)$.  
If $\deg(f) = n$, let the leading coefficient be $a_n$. Then $f(x) = a_n x^n + (\dots)$.  
Then $(x-1)f(x) = (x)(a_n x^n + \dots) - 1(a_n x^n + \dots)$  
$= a_n x^{n+1} + \dots - a_n x^n - \dots$  
The leading term is $a_n x^{n+1}$ (assuming $a_n \neq 0$).  

7.  **Identify Constraints/Assumptions:**  
Is it possible that $\deg(f) < n+1$?  
If $\deg(f) = k$, then the product $(x-1)f(x)$ has degree $k+1$.  
Since we are given an explicit polynomial on the right-hand side, we know its degree is 4.  
Therefore, $k+1 = 4$, which implies $k=3$ (assuming no cancellation or leading coefficient vanishing).  

Let's double check for edge cases.  
*   Could $\deg(f)$ be negative? No, $f$ is a polynomial.  
    *   Could the equation imply $f(x) = 0$? If $P(x) = 3x^4 + \dots$, it's not the zero polynomial. So $f(x)$ cannot be the zero polynomial.  
    *   Is there any scenario where the product $(x-1)f(x)$ has a lower degree than $k+1$?  
Only if the leading coefficient of $P(x)$ were 0, but here it's 3 (for $x^4$). Or if $\deg(f)$ was such that cancellations occurred.  
Let $f(x) = c_k x^k + \dots$. $(x-1)f(x) = c_k x^{k+1} - c_k x^k + \dots$. The term $c_k x^{k+1}$ will definitely be present unless $c_k=0$. Since the RHS polynomial is non-zero and degree 4, $c_k$ cannot be zero for all $x$ in that sense.  

So, $\deg((x-1)f(x)) = \deg(f) + 1$.  
We found $\deg(P) = 4$.  
Therefore, $\deg(f) + 1 = 4$.  
$\deg(f) = 3$.  

8.  **Verification Step (Optional but recommended):**  
If $\deg(f) = 3$, let $f(x) = ax^3 + bx^2 + cx + d$ ($a \neq 0$).  
Then $(x-1)(ax^3 + bx^2 + cx + d) = a x^4 - b x^3 + c x^3 + d x - a x^2 + b x - c x - d$.  
$= ax^4 + (c-b)x^3 + (-a+d)x^2 + (-c-d)x$? No, let's just multiply carefully.  
$(x-1)(ax^3 + bx^2 + cx + d)$  
$= a x(x^3) - 1(x^3) + \dots$ -- no, that's wrong.  
Let's expand:  
$(x-1)f(x) = a x^4 + b x^3 + c x^2 + d x - (a x^3 + b x^2 + c x + d)$  
$= a x^4 + (b-a)x^3 + (c-b)x^2 + (d-c)x - d$?  
Let's check the expansion of $(x-1)P(x)$ where $P(x) = ax^3$.  
$(x-1)(ax^3) = a x^4 - a x^3$. Correct.  

Now we look at the given equation:  
$(x-1)f(x) = 3x^4 + x^3 - 25x^2 + 38x - 17$.  

Let's look at the highest degree term on the RHS. It is $3x^4$.  
On the LHS, $(x-1)f(x) = (x)(f_0 x^3) \dots$ No, let's assume $\deg(f)=n$.  
$(x-1)f(x) = (x)f(x) - f(x)$.  
The degree of $xf(x)$ is $n+1$.  
The degree of $f(x)$ is $n$.  
So the LHS has degree $n+1$ and leading coefficient equal to the leading coefficient of $f(x)$.  

Comparing degrees on both sides:  
LHS degree = $\deg(f) + 1$.  
RHS degree = $\deg(3x^4 + x^3 - 25x^2 + 38x - 17) = 4$.  

Therefore, $\deg(f) + 1 = 4$, so $\deg(f) = 3$.  

9.  **Potential Pitfall Check:**  
Is it possible that $f(x)$ is not a polynomial? No, the problem states "Suppose that f is a polynomial".  
Could $f(x)$ be such that $(x-1)f(x)$ does not have degree $\deg(f)+1$?  
This happens if the leading coefficient of $f(x)$ is 0, meaning lower terms cancel out? No, that would imply $f(x)=0$ eventually or $a_n=0$, contradicting polynomial degree definition. Or if the roots are shared.  
Suppose $f(x) = k$. Constant term. $(x-1)k = kx - k$. Degree 1.  
RHS is degree 4. So $\deg(f)=3$ seems robust.  

Let's try to solve for $f(x)$ explicitly just to be absolutely sure about the leading coefficient and constant terms (not strictly required, but good for sanity check).  
$(x-1)f(x) = P(x)$.  
So $f(x) = \frac{3x^4 + x^3 - 25x^2 + 38x - 17}{x-1}$.  
Since $f(x)$ must be a polynomial, the division by $(x-1)$ must result in an exact remainder of 0.  
Let's perform synthetic division or long division to divide $P(x)$ by $x-1$ and check if the remainder is indeed 0.  

Polynomial: $3x^4 + 1x^3 - 25x^2 + 38x - 17$.  
Divisor: $x-1$.  

Using synthetic division:  
Coefficients: 3, 1, -25, 38, -17.  
Root: 1.  

Row calculation:  
1 | 3   1  -25   38  -17  
|     3    4  -21   17 (or just check values at x=1)  
-------------------------------\-  
3, 4, -21...? No, I need to calculate carefully.  

Let's evaluate $P(1)$:  
$P(1) = 3(1)^4 + (1)^3 - 25(1)^2 + 38(1) - 17$  
$P(1) = 3 + 1 - 25 + 38 - 17$  
$P(1) = 4 - 25 + 38 - 17$  
$P(1) = -21 + 38 - 17$  
$P(1) = 17 - 17$  
$P(1) = 0$.  

Good. Since $P(1)=0$, $(x-1)$ is a factor of $P(x)$. Thus $f(x)$ exists and has degree $\deg(P)-1$.  

Degree of $f(x) = \deg(P(x)) - 1$ ?  
Let's check the division logic.  
If $f(x)(x-1) = P(x)$, then $\deg((x-1)f(x)) = \deg(f) + 1$ (since leading coeff is non-zero).  
LHS degree is $\deg(P)$.  
So $\deg(f) + 1 = \deg(P)$.  
Therefore $\deg(f) = \deg(P) - 1$.  

Let's double check the value of $P(1)$ again.  
$3x^4 \to 3$  
$+ x^3 \to 1$  
$- 25x^2 \to -25$  
$+ 38x \to 38$  
$- 17 \to -17$  
Sum: $3 + 1 = 4$.  
$4 - 25 = -21$.  
$-21 + 38 = 17$.  
$17 - 17 = 0$.  
The remainder is 0. This confirms that $f(x)$ is indeed a polynomial (not rational with a remainder).  

So, the calculation holds up.  
$\deg(P) = 4$.  
$\deg(f) = 4 - 1 = 3$.  

Is there any trick? "degree of f".  
Could $f(x)$ be identically zero? No, degree is undefined or considered $-\infty$ or just 0 depending on convention, but usually for polynomial equation with non-zero RHS, it's not zero. If $P(x)$ was 0, then degree would be anything (or infinite). Here $P(x) \neq 0$.  

Is the degree defined as the lowest power of x with non-zero coeff?  
Yes. Leading coefficient is 3 (non-zero).  

Let's try to construct a simple example to verify logic.  
If $(x-1)f(x) = 2x^3$.  
$f(x) = \frac{2x^3}{x-1}$. Not polynomial.  
So, for $f(x)$ to be a polynomial, the RHS must have zero remainder upon division by LHS factor? No, $(x-1)f(x)$ is on the LHS.  
If $f(x) = x^2$, then $(x-1)x^2 = x^3 - x^2$. Degree 3.  
So if RHS was degree 3, and we want to find $\deg(f)$, it must be 2.  

General case:  
Let $P(x) = c_k x^k + \dots$ with $c_k \neq 0$.  
$(x-1)f(x) = P(x)$.  
Leading term of $(x-1)f(x)$ is $\text{coeff}_f \cdot x^{n+1}$.  
Leading term of RHS is $c_k x^k$.  
Equating degrees: $n+1 = k \implies n = k-1$.  

Is it possible that $n > 0$ and the leading term coefficient changes? No, polynomial multiplication preserves degree unless cancellation occurs (requires factors with matching terms). Here, we are multiplying by $(x-1)$ which has distinct roots. It cannot cancel any term in the highest degree of $f(x)$ (which is at power $n$) because it shifts to $n+1$ but doesn't touch $n+2$.  
The only risk is if $\deg(f) < k-1$, meaning $(x-1)f(x)$ would have degree less than $k$. Then RHS would be lower degree, contradiction.  
Or if $\deg(f) \ge k$, then LHS has degree $\ge k+1$, which contradicts RHS degree $k$.  

So the logic is sound. The answer is 3.  

Just to be pedantic, what if the user meant "degree of f(x)" as a variable name for something else? No, standard polynomial problem.  
What if $f(x)$ has negative terms? Doesn't matter, leading term determines degree.  

Let's quickly check the remainder calculation again using synthetic division or polynomial algebra.  
$f(x) = ax^3 + bx^2 + cx + d$.  
$(x-1)(ax^3 + bx^2 + cx + d) = ax^4 - ax^3 + b x^3 - b x^2 + c x^2 - c x + d x - d$?  
Expansion:  
$= a x^4 + (b-a)x^3 + (c-b)x^2 + (d-c)x - d$ -- No, check the signs carefully.  
$(x-1)(ax^3) = ax^4 - ax^3$. Correct.  
$(x-1)(bx^2) = bx^3 - bx^2$. Correct.  
$(x-1)(cx) = cx^2 - cx$ -- no, this is $cx \cdot x - 1 \cdot cx$? No. $c \cdot x \cdot x$ ...  
Let's multiply terms:  
Term $x^3$: from $ax^4$ and $-ax^3$.  
Term $x^2$: from $bx^3$, $-bx^2$ (from $-1 \cdot bx^2$), $+cx^2$ (from $c \cdot x \cdot x$). So coeff is $b+c$.  
Let's restart the multiplication to avoid brain fog.  

$f(x) = ax^3 + bx^2 + cx + d$.  
$(x-1)f(x) = x f(x) - f(x)$.  
$x(ax^3 + bx^2 + cx + d) - (ax^3 + bx^2 + cx + d)$  
$= (ax^4 + bx^3 + cx^2 + dx) - (ax^3 + bx^2 + cx + d)$  
$= ax^4 + (b-a)x^3 + (c-b)x^2 + (d-c)x - d$.  

We need to match this with $3x^4 + x^3 - 25x^2 + 38x - 17$.  

Coefficient of $x^4$: LHS has $a$, RHS has 3. $\implies a=3$.  
Degree check:  
LHS highest power is $x^4$ (from $ax^4$).  
RHS highest power is $x^4$.  
So $\deg(f)$ can be at most 4-1 = 3?  
Let's look at the equation for $a$:  
The coefficient of $x^4$ in $(x-1)f(x)$ is exactly the coefficient of $x^4$ in $f(x)$.  
Why? Let $f(x) = \dots + a_n x^n + \dots$. Then $x f(x) = \dots + a_n x^{n+1} + \dots$.  
The term $a_n x^{n+1}$ is the leading term.  
Since $(x-1)$ does not affect the degree of the product, and $\deg(f)+1 \neq n$? No.  
Leading term of $P(x)$ is determined by the coefficient of $f(x)$.  
LHS: $(x-1)(a_n x^n + \dots) = a_n x^{n+1} - a_n x^n + \dots$  
RHS: $3x^4 + \dots$  

Comparing leading terms:  
Coeff of $x^{n+1}$ in LHS is $a_n$.  
Coeff of $x^4$ in RHS is 3.  
So $a_n = 3$.  
Thus, the degree of $f(x)$ must be $n$. The degree of $P(x)$ is 4.  
Since the leading term of $(x-1)f(x)$ is $a_n x^{n+1}$, and this must match the $3x^4$ in RHS?  
No, there could be terms like $2x^{n+1} - 5x^n$.  
But we equate polynomials.  
LHS: $a_1 x^{n+1} + \dots$ where $a_1 = a_n$ (leading coeff of $f$).  
RHS: $3x^4 + x^3 + \dots$  

If $\deg(f) > 0$, then the term of degree $n+1$ in LHS is $a_n x^{n+1}$. This term must equal the leading term of RHS, which is $3x^4$.  
Therefore, $a_n = 3$ and $n+1 = 4 \implies n=3$.  
Is it possible that $a_n=0$? If $\deg(f)$ was defined by non-zero coefficients.  
But $f(x)$ is a polynomial. The problem asks for the degree of $f$, implying $\deg(f) > -\infty$ and not negative. Since we found $n+1=4$, the degree must be 3.  

Let's check if there are other possibilities.  
What if $\deg(f) < 4$? No, that was the assumption in finding $a_n$. If $\deg(f) = k$, then leading term of LHS is $k+1$ power $x$. This must match RHS leading term which is degree 4. So $k+1=4 \implies k=3$.  

Are there any edge cases where $(x-1)f(x)$ can be equal to a polynomial of lower degree but $f$ has higher degree?  
No, that would mean the leading coefficient of $(x-1)f(x)$ is zero. The leading coefficient is just the leading coefficient of $f$. If it's non-zero, degree is preserved plus 1. Since RHS is degree 4 and coefficient is 3 (non-zero), $\deg(f) = 3$ is necessary.  

Is it possible that $(x-1)f(x)$ reduces to degree less than 4 due to cancellations between $x f(x)$ and $f(x)$?  
Let's check: $P(x) = x \cdot f(x) - f(x)$.  
If $\deg(f)=n$, LHS leading term is $a_n x^{n+1}$. RHS leading term is 3x^4.  
So $n+1=4$ and $a_n=3$.  
This logic does not depend on cancellation in lower degrees. It just compares the highest degree terms.  

Is there any ambiguity? No.  
The answer seems solid.  

Let's write down the steps clearly for the final output.  
1.  Identify the given equation: $(x-1)f(x) = 3x^4 + x^3 - 25x^2 + 38x - 17$.  
    2.  Observe that the right side is a polynomial of degree 4 with leading coefficient 3. Let $RHS = P(x)$. $\deg(P) = 4$.  
    3.  Consider the degree of the product on the left side, LHS = $(x-1)f(x)$.  
    4.  The leading term of $f(x)$ contributes to the highest power of $x$ in the product. If $\deg(f) = k$, let the leading coefficient be $c_k \neq 0$. Then the highest degree term of $(x-1)f(x)$ is $c_k x^{k+1} - c_k x^k$.  
    5.  Since $\deg((x-1)f(x)) = \max(k+1, \deg(f)) = k+1$ (assuming leading coeff non-zero and no cancellation, which isn't possible here because degrees shift), we have $k+1 = \deg(P) = 4$.  
    6.  Thus, $\deg(f) + 1 = 4$, so $\deg(f) = 3$.  

The question asks for "the degree of $f$". It does not ask to find $f(x)$ itself or verify it.  

Final check.  
Suppose $f(x) = 3x^3 + x^2 - 17x + c$.  
$(x-1)(3x^3 + x^2 - 17x + c) = 3x^4 + x^2x - 3x + xc - x^3 - x^2 + 17x - c$?  
$= 3x^4 + (1-3)x^3 + (-1+0?)x^2$... no.  
$(x-1)(3x^3) = 3x^4 - 3x^3$.  
RHS has $+x^3$. So need $-3x^3$ to match with existing?  
Let's check the constant term of the expansion again to ensure consistency if needed.  
If $f(x)$ exists, its degree must be 3.  
Is it possible that $(x-1)f(x)$ has degree 4 but $\deg(f)=3$? Yes, as derived.  
Could $\deg(f) > 4$? No, LHS degree would be $\ge 5$, RHS degree is 4.  
Could $\deg(f) < 3$?  
If $\deg(f)=2$, then $(x-1)f(x)$ has degree $2+1=3$. The leading term of RHS is $x^4$, so this is a contradiction (degree mismatch).  
Therefore, $\deg(f)$ must be 3.  

Final Answer seems to be 3.  

Just thinking if there's any tricky interpretation where $f(x)$ might have complex coefficients or something? No, "polynomial" usually implies real/complex coefficients, degrees are integers.  
If it were a rational function, degree wouldn't make sense the same way (would be defined by $\deg N - \deg D$). But it says polynomial $f$.  

Let's double check if I misread the question.  
"Suppose that f is a polynomial such that [(x-1) . f(x)] = 3x^4 + x^3 - 25x^2 +38x - 17."  
The dot implies multiplication.  
Is it possible $f(x)$ contains a negative sign? Doesn't matter.  
Is it possible that the polynomial on the right is zero? No, it's clearly given.  

Step-by-step derivation for the response:  
1. Let $\deg(f) = n$.  
   2. Since $f$ is a polynomial of degree $n$ ($n \ge 0$), and assuming $f(x) \neq 0$, its leading term dominates $(x-1)f(x)$ except at the highest power? No.  
Let $f(x) = a_n x^n + \dots$.  
Then $(x-1)f(x) = (x)(a_n x^n + \dots) - (a_n x^n + \dots) = a_n x^{n+1} + (-a_n x^n + \text{others})$.  
The degree of the polynomial on the left is $n+1$ provided $a_n \neq 0$.  
From the given equation, we have $(x-1)f(x) = P(x)$ where $P(x) = 3x^4 + x^3 - 25x^2 + 38x - 17$.  
The degree of the right-hand side polynomial is clearly 4. So $\deg(P)=4$.  
Since polynomials with equal degrees are not necessarily equal (they differ by lower order terms), but here we have an exact equality, the degree of the product must match the degree on the RHS.  
Thus, $\deg((x-1)f(x)) = 4$.  
This implies $n+1 = 4$ or $n+1$ is reduced?  
Is it possible for leading term to cancel out? No, because we're subtracting a lower order term from an upper order term. The coefficient of $x^{n+1}$ is $a_n$. Since $P(x)$ has leading term $3x^4$, the coefficient of $x^4$ in LHS must match 3?  
Yes, leading term is dominant for large $x$. As $|x| \to \infty$, $(x-1)f(x) \approx a_n x^{n+1}$. But $P(x) \approx 3x^4$.  
So $a_n x^{n+1} = 3x^4 + \dots$ implies $n+1=4$ and $a_n=3$.  
Thus $\deg(f) = 3$.  

Seems completely straightforward. Why did I overthink "cancellation"?  
Because $(x-1)$ has a root at 1. If we were dividing, the remainder must be zero.  
This implies $(x-1)$ is not just a factor but $P(1) = 0$. Which it was ($3+1-25+38-17=0$).  
So division is valid.  
Degree of quotient is degree of dividend - degree of divisor.  
$\deg(f) = \deg(P(x)) - \deg(x-1) = 4 - 1 = 3$.  
This confirms the result perfectly.  

The question asks to "reason step by step". I will write the solution based on the leading term argument and/or division rule. The leading term argument is simpler and less prone to arithmetic errors if one understands algebraic manipulation well. But the division rule is also very standard for these problems.  

Let's write out the steps.  
1. Identify $f(x)$ as a polynomial of degree $d$.  
   2. The leading term of $f(x)$ is $a d x^d$ where $a \neq 0$.  
    3. Multiply by $(x-1)$. This shifts the highest power to $d+1$.  
    4. Compare degrees on both sides of the equation. LHS degree is $\max(d+1, d) = d+1$ (assuming $a \neq 0$). RHS degree is 4.  
    5. Equate: $d+1 = 4 \implies d=3$.  

Just a small sanity check on the term "degree of f". If $f$ were the zero polynomial, degree is undefined or -infinity. But $(x-1) \cdot 0 = 0 \neq P(x)$. So $f$ is not zero.  

Final answer is 3.  

One tiny detail: What if $P(x)$ was a constant? Then $\deg(f) = -1$ impossible. What if $P(x)$ was degree 0? $\deg(f)=0-1$ impossible? No, $d+1=0 \implies d=-1$. So we must ensure RHS is not zero or has positive degree. Here it has positive degree.  

The reasoning holds up.  


## Answer

Let the polynomial be denoted by $f(x)$. We are given the equation:  
\[ (x-1)f(x) = 3x^4 + x^3 - 25x^2 + 38x - 17 \]  

Let $\deg(f)$ denote the degree of the polynomial $f(x)$. Since $f(x)$ is a polynomial, let us assume it has a leading term of the form $a x^n$, where $n$ is the degree and $a \neq 0$.  

Consider the left-hand side of the equation: $(x-1)f(x)$.  
Let's multiply the leading term of $f(x)$ by $x$:  
\[ (x)(ax^n + \dots) = ax^{n+1} + \dots \]  
Then, subtracting $f(x)$:  
\[ (x-1)f(x) = (ax^{n+1} + \dots) - (ax^n + \dots) = ax^{n+1} - ax^n + \dots \]  
The degree of the product $(x-1)f(x)$ is generally $\deg(f) + 1$, provided that $a \neq 0$. This is because the highest power term, $a x^{n+1}$, cannot be cancelled out by any other term in the polynomial expansion.  

Now, let's look at the right-hand side of the given equation:  
\[ P(x) = 3x^4 + x^3 - 25x^2 + 38x - 17 \]  
The degree of this polynomial is 4, because the coefficient of $x^4$ is non-zero (it is 3).  

Equating the degrees from both sides:  
Since $(x-1)f(x)$ and $P(x)$ are equal for all $x$, they must have the same leading term structure. Since $\deg(P(x)) = 4$, we have:  
\[ \deg((x-1)f(x)) = 4 \]  
From our analysis above, $\deg((x-1)f(x)) = \deg(f) + 1$.  
Therefore:  
\[ \deg(f) + 1 = 4 \]  
\[ \deg(f) = 3 \]  

To verify this, we can divide the polynomial $3x^4 + x^3 - 25x^2 + 38x - 17$ by $(x-1)$:  
Using synthetic division with root 1:  
Row values: $3, 1, -25, 38, -17$.  
$1 \to 1$:  
$1 \cdot 3 = 3$  
$1+3=4$ (coeff of $x^3$)  
$4 \cdot 1 = 4$: coeff for $x^2$ is $1-4=-3$. No, let's do it carefully.  

Let $f(x) = a_0 x^n + \dots$ where $n=3$.  
$(x-1)(ax^3 + bx^2 + cx + d) = ax^4 + (b-a)x^3 + (c-b)x^2 + (d-c)x - d$.  
We need to match this with $3x^4 + x^3 - 25x^2 + 38x - 17$.  
Comparing coefficients for $x^4$: $a = 3$.  
Comparing highest terms, the degree of LHS is $n+1 = 3+1 = 4$, which matches the degree of RHS.  
This confirms that $\deg(f)=3$ is consistent with the leading term of the given polynomial.  

Another way to see this: If $\deg(f) = n$, then $\deg((x-1)f(x)) = n+1$. The degree of the right side polynomial is 4. Thus $n+1=4 \Rightarrow n=3$.  

\boxed{3}  
