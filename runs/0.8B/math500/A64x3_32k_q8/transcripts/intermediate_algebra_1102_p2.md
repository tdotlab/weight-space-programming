# test/intermediate_algebra/1102.json, part 2 of 2

[Previous part](intermediate_algebra_1102.md)

Let me re-verify $f(-2)$.  
$(-2)^4 = 16$.  
$5(-2)^3 = -40$.  
$9(-2)^2 = 36$.  
$-x = -(-2) = 2$.  
$-14$.  
Sum: $16 - 40 + 36 + 2 - 14$.  
$16 - 40 = -24$.  
$36 - 24 = 12$.  
$12 + 2 = 14$.  
$14 - 14 = 0$.  

It seems my manual calculations are consistent.  

However, I should check if the polynomial is actually factorable into simple quadratics or lower degree polynomials, which would confirm the roots.  
$(x-2)$ isn't a factor.  
Let's divide $P(x)$ by $(x^2 + ax + b)$.  
If it has real roots, maybe $a=0$ is not required for integer factors to be integers? No, integer roots are rational if coefficients are integers (Rational Root Theorem).  

Is there a possibility that the constant term is different in my transcription?  
Prompt: "x^4 + 5x^3 + 9x^2 - x - 14 = 0"  
Let me look at the example outputs if available? No examples.  
Let's check for potential typos in my thought process (mental arithmetic).  
Is $x^4 + 5x^3 + 9x^2 - x - 14$ divisible by something simple?  
If $x=1$, then $P(1)=0$. So $(x-1)$ divides it.  
If I divide $P(x)$ by $x-1$:  
Coeffs: 1, 5, 9, -1, -14  
Synthetic division with root 1:  

```text
      1 | 1   5   9   0  -14
         +-----+---+-----+--+-------
         2   6   8  -14  -3
```


Let's re-do this carefully.  
Polynomial: $x^4 + 5x^3 + 9x^2 - x - 14$.  
Synthetic Divisor: 1.  
Coeffs: 1, 5, 9, 0, -14 (since term is $-x$? No, constant term is -14).  
The terms are $x^4$, $5x^3$, $9x^2$, $-x$, $-14$.  
So coeffs are $[1, 5, 9, -1, -14]$.  
Let's check my manual division logic.  
I used "coeffs of terms" but forgot to include the linear and constant?  
Yes, I need to be careful with the sign for $x^0$ term.  
So coeffs are: 1, 5, 9, -1, -14.  
Let's do division:  
1 | 1   5   9   0  -14 (Assuming constant is 0? No. The problem has -x-14).  
I should align $P(x)$ as $1x^4 + 5x^3 + 9x^2 + 0x - 14$.  
So coefficients are $\{1, 5, 9, 0, -14\}$.  

Using synthetic division with root 1:  
Row 0: 1 (coeff for $x^4$)  
Summing rows? No.  

Let's re-calculate using standard row operations.  

```text
      1 | 5   9   0  -14
       +---+
```

| 1  2   13  -13 | (sums are tricky).  

Let's do it properly:  
$x^4 + 5x^3 + 9x^2 - x - 14$  
$(x-1)(?)$? No, let's divide by $(x-1)$ if possible.  

If I divide by $(x-1)$:  
Wait, why did I think $f(1)=0$ means $(x-1)$ is a factor? It implies that if $x=1$ is a root, $x^4 + 5x^3 + \dots$ evaluated at 1 should be 0.  
Yes, that's what I calculated earlier: $P(1) = 0$.  

If I use synthetic division with root 1 on $[1, 5, 9, -1, -14]$? No, the order is wrong if coefficients are $x^4$ to $x^0$.  
The sequence of coefficients for the polynomial $c_k x^k + \dots + c_0 = 0$:  
$c_4=1, c_3=5, c_2=9, c_1=-1, c_0=-14$.  

Let's re-do the division for synthetic root 1:  
$x^4 + 5x^3 + 9x^2 - x - 14$  
| 1     5     9       0   ? (No, coeff is -14, not -1).  
Sum the coefficients?  
Let's just perform division.  
Divide $(x-1)$.  
$1 \times (-2)?$ No.  

Let's try dividing by $x+1$ or something?  
If $f(x)$ was a root, synthetic division works with integer coefficients if leading coefficient is 1.  
Synthetic Divisor for $x=1$:  
Coeffs: 1, 5, 9, -1, -14 (since coeff of $x$ is -1).  

$1+5+9-1-14 = 0$. Correct.  

So the division process would be:  
Start with 1.  
Next digit: 5?  
Or just check coefficients.  
If I divide $(x-1)$, it should result in a remainder of $-2$ or something? No.  
Since the constant term is -14 and leading coeff is 1, there are many possibilities for quotient degree.  

The product of $(x-r_1)(x-r_2)...$ would be $P(x)$.  

If I assume the problem has integer roots, then $x=1$ must be a factor.  
Then $x^4 + 5x^3 + 9x^2 - x - 14$ is divisible by $(x-1)$.  

Let's check if the quotient is a polynomial of degree 3 with integer coefficients.  
$Q(x) = x^3 + 6x^2 + \dots$? No, let's do actual division.  
$P(x) / (x-1)$  
Coeffs: 1, 5, 9, -1, -14.  
Leading digit is $x$.  

Row operation:  
Multiply term by term? No.  
Just write down coeffs.  
1 | 1   5   9   0  -14  

(Actually, standard synthetic division works on coefficients if you align terms).  
If the coefficient for $x^3$ is 5, then we multiply it by 1 to get $5$. Then add to next coeff.  
Let's do this properly.  

Row: 1, 5, 9, -1, -14  
Divide by $(x-1)$.  
Quotient has degree 3, roots are 1?  
If root is $r=1$, then we are doing synthetic division.  
Coeffs for quotient are: $c_0 / (-1)$ ? No.  

Let's write down the coefficients of $P(x)$.  
Term 0: -14.  
Term 1: -1.  
Term 2: 9.  
Term 3: 5.  
Term 4: 1.  

Division by $(x-1)$? No, let's use the value $r=1$ as root for division.  
So we check if $P(1)=0$. If so, quotient is determined by dividing coefficients.  

Let's perform synthetic division with $r=1$.  
Coeffs: 1 (for $x^4$), 5 ($x^3$), 9 ($x^2$), -1 ($x$), -14 (const).  
Row:  
Start with leading coeff of divisor (1)? No, I need to multiply it.  
Let's write down the division steps.  

We want to compute $P(x) / (x-1)$.  
Synthetic Division steps for polynomial $(c_k x^k + \dots)$ and root $r$:  
Write coefficients: $c_4, c_3, c_2, c_1, c_0$.  
Replace $c_4$ with 1.  
Move to next term: multiply $r=1$, add to $c_k$.  
Actually, just list:  
1.  Coeff of $x^4$: 1  
    2.  Multiply by root (1): $1 \times 1 = 1$. Add to previous coeff? No, the standard algorithm is:  
        - Write $r=1$ in a row.  
          - Move $c_3=5$. Add to result of division for next term.  
          - No, standard synthetic division:  
            - Multiply leading coefficient (c4) by r?  
              - Usually just "add".  

Let's use the values from my thought trace where I got stuck on signs and logic.  

$P(x) = x^4 + 5x^3 + 9x^2 - x - 14$  
Substitute $x=1$: $1+5+9-1-14=0$.  
So $(x-1)$ is a factor? Or is it $(x-1)$?  
Since the constant term was 0, $(x-1)$ divides it.  
Let's perform synthetic division:  
| x^4 |  5  9   -1   -14  
|    1     |   6   8  -34 | (add r=1 to coefficients)  
|  100? No.  

Let's be very careful about synthetic division signs.  
Coefficients: $1, 5, 9, -1, -14$.  
If dividing by $(x+2)$ is the root (since we found $-2$ as a root):  
$P(-2) = 0$.  
Divisor: $x+2$? Or $x-(-2)$ which is $x+2$.  
Synthetic division with -2.  
| 1 5   9   0  -14 (if coeff of x^3 was missing or something)  
But the polynomial ends at $-x$.  
The sequence of coefficients for $x^4 + 5x^3 + 9x^2 - x - 14$ is:  
$c_4=1, c_3=5, c_2=9, c_1=-1, c_0=-14$.  

Let's calculate remainder by $(x+2)$? No, I checked $(x+2)$ earlier for the constant term.  
If it is divisible by $(x-(-2))$ i.e., $x+2$, the quotient coefficients would be determined.  

**Check if polynomial factors with integer roots.**  
Since we found roots -2 and 1, maybe I should check for other rational roots (candidates).  
The divisors of -14 are $\pm 1, \pm 2, \pm 7, \pm 14$.  
We checked all. So likely these are the only integer roots.  

**Re-calculation of $f(-2)$ to be absolutely sure.**  
Term: $x^4$: 16  
Term: $5x^3$: 5 * (-8) = -40  
Term: $9x^2$: 9 * (4) = 36  
Term: $-x$: -(-2) = +2. (Note: user has "- x" term in the equation, so it's minus x. If I substitute x=-2, it is -(-2) = 2).  
Term: -14.  
Sum: 16 - 40 + 36 + 2 - 14.  
(Positives): 16+36+2 = 54  
(Negatives): 40+14 = 54  
Result: 0.  

**Re-calculation of $f(1)$ to be absolutely sure.**  
Term: $x^4$: 1  
Term: $5x^3$: 5 * 1 = 5  
Term: $9x^2$: 9 * 1 = 9  
Term: $-x$: -(-?) No, term is "- x". If x=1, it is -1.  
Term: -14.  
Sum: 1 + 5 + 9 - 1 - 14.  
Positives: 1+5+9 = 15.  
Negatives: 1+14 = 15.  
Result: 0.  

Both are integer roots. The question asks for "all the integer roots".  
So I should list them separated by commas.  
Roots: -2, 1.  
Order: Ascending? Usually not specified but helpful to present clearly.  

Are there any other possibilities?  
Could the polynomial have irrational or complex roots that I don't care about? The question asks for integer roots specifically.  
Is it possible there's a typo in my transcription of the question?  
"x^4 \+ 5x^3 + 9x^2 - x - 14 = 0"  
If it were $x^4 + 5x^3 + 9x^2 - 5x - 14 = 0$ or something, maybe.  
But with $-x$, it's fine.  

Double check if there are other factors of 14?  
-14 is prime to integers (except divisors).  
Factors: $\pm 1, \pm 2, \pm 7, \pm 14$.  
Checked them all. Only $-2$ and $1$ yield integer results.  

**Let's assume the question implies a polynomial with integer coefficients.** Yes.  

Let me check if I misinterpreted "integer roots". Does it mean $r_i \in \mathbb{Z}$? Yes.  
Does it ask for solutions to the equation $x^4 + 5x^3 + 9x^2 - x - 14 = 0$? Yes.  

So, I should provide $\{-2, 1\}$.  
Usually formatted as `1, -2` or `{-2, 1}` or similar. The user said "Enter all the integer roots".  
Common format for such answers is comma-separated integers.  

Let me check one more time for $x=-1$ and $x=-7$ again.  
$x=-1$: $1 - 5 + 9 + 1 - 14 = -8$. Not zero.  
$x=-2$: $16 - 40 + 36 + 2 - 14 = 0$. Zero.  
$x=7$: $2401 + 1715 + 441 - 7 - 14 \neq 0$.  
$x=-7$: $2401 - 1715 + 441 + 7 - 14 = 1106$. Not zero.  
$x=14$: $34^4$ approx? No. $19^2 \times 5^4$?  
Just to be sure, no other factor.  

Let's do a quick check on the coefficients to see if they are factors of 68? No relation.  

One potential pitfall: Did I calculate $5x^3$ correctly for $x=-2$?  
$5(-8) = -40$. Correct.  
Did I calculate $9x^2$ correctly? $9(4) = 36$. Correct.  
Did I calculate $-x$ correctly for $x=-2$?  
$-(-2) = +2$. Correct.  

What if the user meant: $x^4 + 5x^3 + 9x^2 - x - 14 = 0$.  
And the question is from a source where maybe the constant term was different? No, I must solve for what is written.  

Let me check if there's any subtle reason why $x=1$ and $x=-2$ are the only ones.  
Since we checked all rational root candidates (factors of -14), and found only these two integer roots, I am confident in this result unless I missed a candidate or miscalculated one.  
Wait. The Rational Root Theorem states that any rational root $p/q$ (in lowest terms) has $p|a_0$ and $q|a_n$. Here $a_n = 1$, so $p \in \{-14, \dots\}$. If roots are integers, they must be factors. I checked all.  
There is no other root that is rational with denominator not dividing the constant term? No, if it's a rational root, the denominator must divide the leading coefficient (which is 1). So denominator must be $\pm 1$. Thus roots must be integer divisors of constant term.  

I should write down the solution clearly.  
Steps:  
1. State Rational Root Theorem. Candidates are factors of -14: $\pm 1, \pm 2, \pm 7, \pm 14$.  
   2. Test each candidate.  
    3. Find $x=-2$ and $x=1$.  

I will output the result based on these two candidates.  

Final check of the question phrasing "Enter all the integer roots".  
If it's -2, 1, that's it.  
Is there any ambiguity? No.  

Let me re-verify $f(-2)$ one last time manually with a calculator simulation in my head.  
$(x^4 + 5x^3) = x^2(x+5)$? No.  
$(x^4 + 9x^2) + \dots$ No obvious factorization.  

Let's check $f(1)$ again.  
$1^4 + 5(1)^3 + 9(1)^2 - 1 - 14 = 1 + 5 + 9 - 1 - 14$.  
$6+9-1-14$? No.  
$1+5+9 = 15$.  
$-1-14 = -15$.  
$15-15=0$. Correct.  

Let's check if I made a mistake in the question transcription.  
Maybe the signs are different? "x^4 + 5x^3 + 9x^2 - x - 14".  
If it was $+x$ instead of $-x$, then for $x=1$, term is $+1$.  
Then $P(1) = 1+5+9-1-14 = -6 \neq 0$.  
If it was $-9x^2$...  
I'll assume the text is exactly as provided.  

The roots are -2 and 1.  

Double check if any term in the problem might be a typo for something like "x^4 + 5x^3 + 9x^2 + x - 14"?  
If $+x$ was present: $f(1) = 6 \neq 0$.  
Then roots are different.  

But I should strictly stick to the provided text.  

Final Answer seems to be $\{-2, 1\}$.  

One more check.  
Could there be a mistake in $f(-7)$?  
$f(-7) = 2401 - 5(343) + \dots$ No.  
Let's just compute the value of $\frac{x(x+2)(x+7) ...}{\dots}$  

There are no obvious tricks or missing factors I can spot easily without doing more work.  
The manual check is robust.  

**Final Result Construction:**  
Roots found: -2 and 1.  
Output format: "1, -2" or similar? Standard math problem format often puts them in order or set notation. The user said "Enter all the integer roots". I will list them separated by a comma.  
Since it is a set, maybe sort them. $\{-2, 1\}$ or $-2, 1$.  

Let me write out the argument clearly.  
Rational root theorem implies roots are divisors of constant term -14.  
Divisors: $\pm 1, \pm 2, \pm 7, \pm 14$.  
Checking each:  
$x=-2$: $(−2)^4 + 5(−2)^3 + 9(−2)^2 − (−2) − 14 = 16 − 40 + 36 + 2 − 14 = 0$.  
$x=1$: $1^4 + 5(1)^3 + 9(1)^2 − 1 − 14 = 1 + 5 + 9 − 1 − 14 = 0$.  
All other values checked:  
-1: $1−5+9+1−14 = -8$  
7: $2401 + \dots \neq 0$  
14: ... $\neq 0$  

So the integer roots are -2 and 1.  


## Answer

To find all the integer roots of the polynomial equation  
\[x^4 + 5x^3 + 9x^2 - x - 14 = 0,\]  
we can use the Rational Root Theorem. This theorem states that any rational root $p/q$ of a polynomial with integer coefficients must be a factor of the constant term divided by a factor of the leading coefficient.  

Here, the polynomial is $x^4 + 5x^3 + 9x^2 - x - 14 = 0$, where:  
- The leading coefficient $a_4$ is $1$.  
- The constant term $a_0$ is $-14$.  

Thus, any integer root must be a factor of $-14$. The factors of $-14$ are $\pm 1, \pm 2, \pm 7, \pm 14$.  

We will test each candidate to see if it is a root ($f(x) = 0$).  

**Test $x = 1$:**  
\[ f(1) = (1)^4 + 5(1)^3 + 9(1)^2 - (1) - 14 \]  
Substitute the value:  
\[ f(1) = 1 + 5 + 9 - 1 - 14 \]  
\[ f(1) = 15 - 15 = 0 \]  
Since $f(1) = 0$, **x = 1** is an integer root.  

**Test $x = -2$:**  
Substitute the value into the equation:  
\[ f(-2) = (-2)^4 + 5(-2)^3 + 9(-2)^2 - (-2) - 14 \]  
Calculate each term:  
- $( -2 )^4 = 16 $  
- $ 5(-2)^3 = 5(-8) = -40 $  
- $ 9(-2)^2 = 9(4) = 36 $  
- $ -(-2) = +2 $ (note the coefficient is minus, so $-x$ becomes $+x$ when substituting negative)  
- Constant term $-14$  

Summing these values:  
\[ f(-2) = 16 - 40 + 36 + 2 - 14 \]  
\[ f(-2) = (16 + 36 + 2) - 40 - 14 \]  
\[ f(-2) = 54 - 54 \]  
\[ f(-2) = 0 \]  
Since $f(-2) = 0$, **x = -2** is an integer root.  

**Check other potential integer roots (like $x = -1, 7, -7, 14$):**  
For example, checking $x = -1$:  
\[ f(-1) = (-1)^4 + 5(-1)^3 + 9(-1)^2 - (-1) - 14 \]  
\[ f(-1) = 1 - 5 + 9 + 1 - 14 = -8 \neq 0 \]  
Checking $x = -7$:  
\[ f(-7) \approx 2401 - 1715 + 441 + 7 - 14 = 1106 \neq 0 \]  
Checking $x = 7$:  
\[ f(7) \approx 4036 \neq 0 \]  
The other integers were checked and found to be non-zero.  

Since the Rational Root Theorem guarantees that integer roots must be among the factors of -14, we have found all integer roots.  

The integer roots are: 1, -2.  

\boxed{1, -2}  
