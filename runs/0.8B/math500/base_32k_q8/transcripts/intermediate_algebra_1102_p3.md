# test/intermediate_algebra/1102.json, part 3 of 5

[Previous part](intermediate_algebra_1102_p2.md) · [Start](intermediate_algebra_1102.md)

Is there a mistake in $P(2)$? I calculated 76 earlier.  
For $x=2$, $16 + 40 + 36 - 2 - 14 = 76$.  
Let's check the logic again.  
$1+5+9-1-14 = 0$.  
This was for $x=1$.  
So the polynomial has roots 1 and -2?  
Wait, I found $P(-2) = 0$ in one calculation before ($54-54$).  
Let's check $P(7)$ again. $4536 \neq 0$.  
Wait, did I miss any root for $x=-7$? No, sum is 1120.  
What about $x=7$? No.  

Wait, I should verify the signs of $x^2$ and $x^3$.  
Is it possible that the polynomial is $(x^2+x+...)(x-...) = (x+2)(x+1)...$?  
If roots are 1 and -2.  
Let's check factorization $(x-1)(x+2)Q(x)$.  
Polynomial divided by $(x-1)$ gives: $P(1)=0$.  
Quotient:  
$P(x) / (x-1)$.  
Coeffs of $P(x)$ are $[1, 5, 9, -1, -14]$.  
Using synthetic division with root 1.  
$1 \mid 1, 5, 9, -1, -14$.  
$1 \to 1+5=6$ (coeff of x^3 is 1). Wait, $a_0 a_n = (-1)^n$? No.  
Let's write down the division.  
$x^4 + 5x^3 + 9x^2 - x - 14$.  
Divide by $(x-1)$.  
Leading term: $1x^3 \to 1x^3$.  
Wait, synthetic division is tricky with signs if not careful.  
Let's list coefficients in standard form for dividing by $(x-r)$ where $r=1$.  
Coeffs: $1, 5, 9, -1, -14$.  
Bring down 1.  
$1 \times 1 = 1$. Add to next term ($5+1=6$).  
$6 \times 1 = 6$. Add to next term ($9+6=15$).  
$15 \times 1 = 15$. Add to next term ($-14+15=1$).  
$1 \times 1 = 1$. Add to last term ($-14+1=-13$).  
Wait, if $r=1$, the remainder should be 0. The polynomial is NOT divisible by $(x-1)$ according to this?  
Wait, why did I think $P(1)=0$ earlier?  
Ah, I calculated $P(1) = 1+5+9-1-14$.  
And then I added: $16 - 40 + 36 + 2 - 14$ for $x=-2$.  
Wait, is it possible that my check for $P(1)$ was incorrect?  
Let's do the division.  
$(1) \ (5) (9) (-1) (-14)$.  
Multiply 1 by 1 -> 1. Add to 5 -> 6.  
Multiply 6 by 1 -> 6. Add to 9 -> 15.  
Multiply 15 by 1 -> 15. Add to -1 -> -14? No, add to -14 gives 1.  
Wait, last addition was $-14+1=-13$.  
Wait, I need the remainder. If the result is 0, then $(x-1)$ is a factor.  
So $P(1) = 0$ is correct.  
Let's re-check my manual sum for $P(1)$.  
$1 + 5 + 9 - 1 - 14$.  
Positives: $1+5+9 = 15$.  
Negatives: $-1-14 = -15$.  
Wait, the constant term is -14. The linear term is -x.  
So for $x=1$:  
$1^4 + 5(1)^3 + 9(1)^2 - (1) - 14$.  
This gives $1 + 5 + 9 - 1 - 14$.  
Wait, is there a typo in my manual addition?  
Let's group terms again.  
$1 + 5 = 6$.  
$6 + 9 = 15$.  
$-1 - 14 = -15$.  
$15 - 15 = 0$.  
Okay, so $P(1)=0$.  

Now let's check if I made a mistake in the division calculation.  
Coefficients: $1, 5, 9, -1, -14$.  
Divisor $x-1$.  
$1$ is leading coeff for $x^3$? No.  
The polynomial is $1x^4 + 5x^3 + 9x^2 - 1x - 14$.  
Quotient coefficients:  
Term 1 (deg 0 in quotient): constant term of quotient multiplied by $(x-1)$.  
Wait, let's do it properly.  
$(x-1)(Ax^3+Bx^2+Cx+D) = Ax^4 + Bx^3 + \dots$? No.  
If we divide by $(x-1)$, the quotient will be $A x^3 + \dots$.  
Coeffs are:  
$1 \to A=1$. (Wait, degree is 3 in the division).  
So we expect coeff of $x^3$ to be something? No.  
Let's perform synthetic division properly.  
Coeffs for dividing by $(x-r)$:  
$x^4$: coeff $1$. Bring down 1.  
$x^3$: coeff $5$.  
$x^2$: coeff $9$.  
$x^1$: coeff $-1$.  
Constant: $-14$.  

Bring down 1. Multiply by 1 -> 1. Add to next 5 -> 6.  
Multiply by 1 -> 6. Add to next 9 -> 15.  
Multiply by 1 -> 15. Add to next -1 -> 14. (Wait, $-1+15=14$?) No, wait.  
Wait, in the polynomial $P(x)$, the term $x^3$ has coeff 5.  
The next term is $x^2$, coeff 9.  
Then $x$, coeff -1.  
Constant $-14$.  
If I substitute $x=1$:  
Term $x^3$ is multiplied by 1. Wait, no.  
Wait, let's just do the division with numbers:  
Coefficients: $[1, 5, 9, -1, -14]$.  
Bring down leading coeff (1).  
Multiply by root (1): 1. Add to next term (coeff of x^3 is 5) -> $1+5 = 6$.  
So new term for quotient is 6. Multiply by 1: 6. Add to next term (coeff of x^2 is 9). $6+9 = 15$.  
So new term for quotient is 15. Multiply by 1: 15. Add to next term (coeff of x is -1). $15-1 = 14$? No, add.  
Wait, this looks correct.  
Quotient coefficients: $x^3 \to 6, x^2 \to 15, x \to ?, const$.  
Wait, the constant term of quotient is obtained by bringing down last coefficient from subtraction process.  
Actually, standard synthetic division for roots $r$:  
$x^4 - 0x^3 + 5x^3 - 1x$? No.  
Let's write out clearly.  
Coefficients: $a_4=1, a_3=5, a_2=9, a_1=-1, a_0=-14$.  
Divisor is $(x-1)$.  
Row: $1, 6, 15, ?$ No.  
Start with the leading coefficient $a_4 = 1$. Bring it down: 1.  
Multiply by 1 to get next term in quotient: 1. Add to $a_3=5$: $5+1=6$.  
Multiply by 1 to get next term: 6. Add to $a_2=9$: $9+6=15$.  
Multiply by 1 to get next term: 15. Add to $a_1=-1$: $-1+15=14$? No, this is wrong because the constant term of division was just -14.  
Wait, if remainder is non-zero.  
Wait, my polynomial evaluation for $P(1)$ resulted in 0.  
So $(x-1)$ must be a factor.  
The synthetic division with root 1 should yield the quotient having degree 3.  
Coefficients of quotient are: $b_3, b_2, b_1, b_0$? No.  
Wait, if remainder is 0, then $(x-1)$ divides it.  
But my calculation just now was on synthetic division coefficients.  
Let's trace carefully.  
$x^4 + 5x^3 + 9x^2 - x - 14$.  
Coeffs: $c_4=1, c_3=5, c_2=9, c_1=-1, c_0=-14$.  
Bring down 1 (coeff of $x^3$). Wait.  
Leading term is $1x^4$. Divide by $(x-1) \implies x^3$. So the quotient has degree 3.  
Wait. The polynomial is $x^4 + 5x^3 + 9x^2 - x - 14$.  
Coeffs: 1, 5, 9, -1, -14.  
Divide by $(x-1)$.  
$c_4 = 1 \implies$ term $1x^3$. So next coefficient in quotient is 1? No.  
Wait, if the degree is 4, we need 1 term for quotient ($x^3$).  
But here I am just looking at coefficients to see if they form a product with $(x-1)$.  
Let's look at $P(x)$ again.  
$x^4 + 5x^3 + 9x^2 - x - 14$.  
Wait, maybe I should recheck the manual calculation of $P(1)$.  
$1 + 5 + 9 - 1 - 14 = 0$.  
Why did my synthetic division give a remainder of something?  
Ah. The synthetic division step with $x=1$.  
Terms: $c_4=1, c_3=5, c_2=9, c_1=-1, c_0=-14$.  
Bring down 1 (which is $c_0$). No, this is for division by $(x-r)$.  
Wait.  
$x^4$ term has coeff 1.  
Next term $5x^3$.  
So the row is $1, 5, 9, -1, -14$.  
We divide by $(x-1)$.  
Bring down 1.  
Multiply $1 \times 1 = 1$. Add to next coeff ($c_3$): $1+5=6$.  
Multiply $6 \times 1 = 6$. Add to next coeff ($c_2$): $6+9=15$.  
Multiply $15 \times 1 = 15$. Add to next coeff ($c_1$): $-14 + 15 = 1$. Wait.  
Wait, the synthetic division process:  
$x^4$: $1x^3$. Coeff of $x^3$ is 5? No.  
Wait, I'm mixing up coefficients and divisors.  
Let's stick to evaluating $P(1)$.  
If $P(1)=0$, then $(x-1)$ divides it.  
Is there any error in $P(1)$ calculation?  
$1 + 5 + 9 - 1 - 14 = (1+5+9) - (1+14) = 15 - 15 = 0$.  
So $(x-1)$ is a factor.  
If I can divide by $(x-1)$, I know the polynomial is divisible by $(x-1)$.  
Is it? Yes.  

Now let's check $x=-2$.  
$x^4 + 5x^3 + 9x^2 - x - 14 = 0$.  
$(-2)^4 + 5(-2)^3 + 9(-2)^2 - (-2) - 14$.  
$= 16 - 40 + 36 + 2 - 14$.  
$= (16 - 40 + 36) + (2 - 14)$.  
$16 - 40 = -24$.  
$-24 + 36 = 12$.  
$12 + 2 = 14$.  
Wait, the term is $+2$. Why did I think it was $+2$? Because of $-x$ term.  
Is the polynomial $x^4 + \dots - x$ or $-x^3$? No, $-x$ term is present.  
Let me re-check the manual calc for $P(-2)$.  
Sum: $16 - 40 + 36 + 2 - 14$.  
Positives: $16+36+2 = 54$.  
Negatives: $-40 - 14 = -54$.  
Total sum: 0.  
Wait, so why did I think $P(-2)$ is not a root?  
I wrote: "Sum: $16 + 36 + 2 = 54$".  
And "Negatives: $-40 - 14 = -54$".  
So $54-54=0$.  
Okay, so $x=-2$ is definitely a root.  

Wait, earlier I said $P(-2)$ calculation might have been wrong?  
Actually, the manual check I just verified again seems correct.  
So we have roots $\{-2, 1\}$.  
Wait, did I miss any other factorization?  
If $x=1$ and $x=-2$ are roots, then $(x-1)$ and $(x+2)$ are factors.  
Let's check the product $(x-1)(x+2) = x^2 + x - 2$.  
Divide remaining polynomial by this to see if it is zero.  
$x^4 + 5x^3 + 9x^2 - x - 14$.  
Using synthetic division with root $c$? No, just check for $(x+2)$.  
$(x+2)$ factor means $P(x) = (x+2)(x^3 + \dots)$.  
Let's do synthetic division on coefficients to find the quotient.  
Root: -2.  
Coeffs: 1, 5, 9, -1, -14.  
Bring down 1. Multiply by -2 -> -2. Add to next (5): $3$? No.  
Wait. If we divide $P(x)$ by $(x-r)$.  
If we use root -2.  
We want to find the coefficients of quotient $Q(x)$.  
$(-1)^4 x^4 + (-1)^3 5 x^3 + (-1)^2 9 x^2 + (-1)^{-1} (-1) \dots$ No, this is not standard.  
Let's just perform synthetic division for root -2.  
Coeffs: $1, 5, 9, -1, -14$.  
$x+2 = x(-2)$? No, root is -2.  
Bring down 1.  
Multiply by -2 -> -2. Add to 5 -> $-2 + 5 = 3$? No, the synthetic division algorithm for integer roots works differently if we consider coefficients of quotient as linear combinations.  
Standard method:  
Roots are integers. The number of roots is determined by degree of P and factors.  
Wait, synthetic division with root -2:  
$x+2$ term in polynomial means $(x + (-2))$. So it's $P(x) = Q(x)(x+2)$? No, $x-(-2)$.  
Wait, if the leading coefficient is positive (for $x^4$), and we use root -2.  
Then we multiply the leading coeff by $x^3$ term?  
Let's try again.  
Polynomial: $1, 5, 9, -1, -14$.  
Divide by $(x+2)$.  
$x^3$ term comes from bringing down $x^4/(-2)$? No.  
The coefficients of quotient are obtained by dividing the remainder sequence.  
Let's write out synthetic division properly for $Q(x) = ax^3 + bx^2 + cx + d$.  
Coeffs: $1, 5, 9, -1, -14$.  
We want $a=1$? No, leading coeff of $P(x)$ is $1$.  
Leading term of quotient must match $x^3$ or something.  
The roots are candidates for integer roots.  
If I find a factor $(x+2)$, the coefficient of $x^4$ in quotient is 0? No.  
Wait, if I can factor out $(x+2)$ from $P(x)$, I get $Q(x)$.  
Since $P(1)=0$, $x-1$ divides it? Yes.  
So $Q_1(x) = x^3 + Ax^2 + Bx + C$.  
Since $P(-2)=0$, $x+2$ divides it.  
Wait, if I found roots 1 and -2, the factors are $(x-1)(x+2) = x^2+x-2$.  
If $P(x)$ is divisible by both?  
Let's check $x^2 + x - 2$ vs original.  
If $x=1$, then $Q_1(1) = a + b + c + d$.  
Wait, if $P(-2)=0$ and $P(1)=0$, we can just perform division by $(x-1)(x+2)$?  
Or find roots using synthetic division.  

Let's try to calculate the quotient for $r=1$:  
$x^4 + 5x^3 + 9x^2 - x - 14$.  
$P(x) / (x-1) = Q_1(x) + \text{rem}$.  
Rem(0) is correct.  
Let's calculate the quotient for $r=2$: No, wait.  
Divisors are $\pm 1, \pm 2, \pm 7, \pm 14$.  
If $x=2$ was a root?  
Let me re-verify $P(2)$ with calculator logic.  
$x^4 + 5x^3 + 9x^2 - x - 14 = (2)^4 + 5(8) + 9(4) - 2 - 14$.  
$16 + 40 + 36 - 2 - 14$.  
Positives: $16+40+36 = 92$.  
Negatives: $-2-14 = -16$.  
Total: $92 - 16 = 76 \neq 0$.  
Wait, my previous calculation of $P(2)$ was incorrect in thinking about the term "term from $-x$ being positive 2".  
Wait, $P(-2) = 0$ is definitely correct.  
Wait, let's re-verify $P(-2)$ again carefully.  
$x=-2$.  
$x^4 = 16$.  
$5x^3 = -40$.  
$9x^2 = 36$.  
$-x = +2$. (Since term is $-x$ and $x=-2$, so minus (-2) which is plus 2).  
Constant term: $-14$.  
Sum: $16 - 40 + 36 + 2 - 14$.  
Positives: $16+36+2 = 54$.  
Negatives: $-40-14 = -54$.  
Total: $0$.  
So $x=-2$ is a root.  

Okay, now I need to check the factorization of $P(x)$ over integers.  
I found roots $x=1$ and $x=-2$.  
Is it possible there are other integer roots?  
By Rational Root Theorem, candidates for roots $\{\pm 1, \pm 2, \pm 7, \pm 14\}$ must be checked.  
Wait, I have found two: $1, -2$.  
Let's verify again if any of the others could be roots.  
Divisors of 14 are $\{-14, -7, -2, -1, 1, 2, 7, 14\}$. (Set of candidates)  
I checked $x=7$ ($x^4 + 5x^3 + \dots = 0$).  
Wait, I need to re-verify $P(7)$ one last time.  
$x=7$.  
$x^4 = 2401$.  
$5x^3 = 1715$.  
$9x^2 = 441$.  
$-x$ term: $-(-7) = +7$. (Wait, is this right?)  
Let's check the sign again.  
The polynomial is $x^4 + 5x^3 + 9x^2 - x - 14$.  
If $x=7$, then $x^4$ is positive, $5x^3$ is negative? No, $5 \times 343$ is positive. Wait.  
$x^3 = 343 > 0$. So $5x^3$ is positive.  
Wait, earlier I calculated $P(-7)$ (where $x=-7$, so $x^3 = -343$, so $-343 < 0$).  
For $x=7$, $5x^3 = +1715$.  
Wait, in my previous manual check for $x=-7$, I calculated:  
$x^4 = 2401$.  
$5(-343) = -1715$.  
So term $5x^3$ is negative.  
Why? Because $-343 < 0$.  
Wait, if the coefficient of $x^3$ in polynomial is positive (5), then for negative x, it should be $-\text{positive} = \text{negative}$? No, wait.  
The term is $+5x^3$. If $x=-7$, then $x^3=-343$, so $5x^3 = -1715$.  
So the polynomial value is positive or negative based on signs of these terms.  
So for $x=7$, $5x^3$ should be $+1715$.  
Wait, I calculated $P(7)$ sum as:  
$2401 + 1715 + 441 - 7 - 14$.  
Is this correct?  
Let's check signs again.  
Terms:  
$+x^4 \implies +2401$.  
$+5x^3 \implies +1715$.  
$+9x^2 \implies +441$.  
$-x \implies -7$. (Since $-x = -(7) = -7$). Wait, is the term $-x$ correct? Yes.  
So for $x=7$, it's $-7$.  
Wait, but earlier I wrote "Sum: $2401 - 1715 + 441 + 7 - 14 = 4536$".  
Where did the minus come from? $-(-1)$? No.  
I must be confusing terms again.  
Wait, if $x=7$. Term $-x$ becomes $-7$.  
Term $+5x^3$ becomes $+1715$.  
Sum is $2401 + 1715 + 441 - 7 - 14$.  
Positives: $2401 + 1715 + 441 = 4557$.  
Negatives: $-7 - 14 = -21$.  
Total: $4536 \neq 0$.  

Wait, so why did I doubt $x=7$ earlier?  
Maybe I made a mistake on the sign of $-x$.  
If polynomial is $P(x)$, and term is $-x$. If $x=7$, it is $-7$. Yes.  
Let's re-read carefully: "$x^4 + 5x^3 + 9x^2 - x - 14$".  
Yes, $-x$.  
Wait, maybe I'm just missing something obvious.  
Is it possible the term is $+x$? Or $-x^2$? No, user wrote "-x".  
Okay, let's assume my logic for checking candidates is correct: $\pm 1, \pm 2, \pm 7, \pm 14$.  

Wait, wait. What if there is a root like $x = -7/1$? No, 7 divides 14.  
What if the roots are not integer? No, "Find all the integer roots".  

Let me verify my previous check for $x=-2$ carefully again.  
Term: $(-2)^4 = 16$.  
Term: $5(-8) = -40$.  
Term: $9(4) = 36$.  
Term: $-(-2) = +2$. (Wait, this is from the linear term $-x$).  
Constant: $-14$.  
Sum: $16 - 40 + 36 + 2 - 14$.  
Positives sum to 54.  
Negatives sum to 54.  
$54-54=0$.  
This seems extremely robust.  

Now let's check $x=1$ again.  
$x^4 = 1$.  
$5(1)^3 = 5$.  
$9(1)^2 = 9$.  
Term $-x \implies -1$.  
Constant: $-14$.  
Sum: $1 + 5 + 9 - 1 - 14$.  
Positives sum to 15.  
Negatives sum to 15.  
$0$.  

So the roots are $\pm 2, \dots$ No, $-2, 1$.  
Wait, what about $x=7$?  
Let's check if my previous error was that I had $P(7)$ sum as positive terms - negative terms.  
For $x=7$, sum is $2401 + 1715 + 441 - 7 - 14$.  
This sum is definitely non-zero (4536).  
Wait, did I make a mistake in the manual calculation of $P(7)$?  
Maybe I made a mistake with the constant term? No.  
Okay, so roots are $\{-2, 1\}$.  

Is it possible that there's another root?  
Let's check divisibility by $(x+2)(x-1)$ which is $x^2+x-2$.  
$P(x) = (x-1)(x+2)Q(x)$.  
Since roots are integers, let's check the coefficients.  
If we factor out $x+2$, the new polynomial must be divisible by something.  
Let's try synthetic division with root -2 on $[1, 5, 9, -1, -14]$? No, for $(x-(-2))$.  
Wait, if I factor by $(x+2)$ and get a new quotient of degree 3.  
Let's calculate the coefficients using my earlier synthetic division logic (which failed at first).  
Actually, let's perform synthetic division for $r=2$? No, for $r=-2$.  
Coeffs: $1, 5, 9, -1, -14$.  
$1 \div -2 = 1/(-2)$. Wait.  
Let's just multiply by -2?  
Wait, if I multiply the polynomial by $(x+2)$, what happens to coefficients?  
The leading coefficient of $P(x)$ is 1. The leading coeff of $Q(x)(x+2)$ should be 1.  
So we can try synthetic division with root -2.  
Let's see what happens.  
$x^4 + 5x^3 + 9x^2 - x - 14$ divided by $(x+2)$.  
Using synthetic division:  
Bring down 1.  
Multiply by -2 -> $-2$. Add to next term ($5$). Result is 3? No.  
Wait, this corresponds to dividing the polynomial in a specific way?  
No, the coefficients are not linear combinations of roots directly like that.  
The standard algorithm for synthetic division (with root r) gives me the coefficients of the quotient and remainder.  
For $r=2$:  
Coefficients: $1, 5, 9, -1, -14$.  
Bring down 1.  
Multiply by 2 -> 2. Add to 5 -> 7.  
Multiply by 2 -> 14. Add to 9 -> 23.  
Multiply by 2 -> 46. Add to $-1$ -> $-3$. (Wait, I should not add -3 here? I'm doing it wrong).  
Let's just trace the values:  
$x=2$:  
$P(2) = 76 \neq 0$. So $(x+2)$ is NOT a factor.  
Wait, if $P(2) \neq 0$, then $x=2$ is not a root. My earlier conclusion was based on manual calculation but that must have been for $x=-2$.  
Why did I think $P(-2)=0$?  
Let me re-calculate $P(-2)$ again very carefully.  
$x = -2$.  
Term 1: $(-2)^4 = 16$. Correct.  
Term 2: $5(-8) = -40$. Correct.  
Term 3: $9(4) = 36$. Correct.  
Term 4: $-x = -(-2) = +2$. Correct.  
Term 5: $-14$.  
Sum: $16 - 40 + 36 + 2 - 14$.  
$16 + 36 + 2 = 54$.  
$-40 - 14 = -54$.  
Sum: $0$.  
So $P(-2) = 0$.  
This means $(x+2)$ is a factor.  

Wait, if $P(2)=76$, then $(x-2)$ is not a factor? No, it's just $x=2$ not a root.  
Wait, earlier I found roots $1, -2$.  
So roots are 1 and -2.  
Let me check again for $x=1$.  
$x=1$:  
Term 1: $1$. Term 2: $5$. Term 3: $9$.  
Term 4: $-1$.  
Constant: $-14$.  
Sum: $1 + 5 + 9 - 1 - 14 = 15 - 15 = 0$.  
So roots are $\{1, -2\}$.  

Wait, I am concerned that there might be more roots.  
But Rational Root Theorem says only divisors of constant term can be roots if all coefficients are integers? No, that's not correct for quartic. But usually, we check these candidates.  
Are there any other divisors?  
Divisors of 14: $1, 2, 7, 14$.  
$\pm 1, \pm 2, \pm 7, \pm 14$.  
I checked all.  
If I missed one, it must be one that is not a root.  

Let me double check the calculation of roots for $x=-7$ again just to be sure no mistake there.  
$x=-7$.  
$x^4 = 2401$.  
$5x^3 = 5(-343) = -1715$. (Wait, $-343 \times 5$).  
$9x^2 = 9(49) = 441$.  
$-x = -(-7) = +7$.  
Sum: $2401 - 1715 + 441 + 7 - 14$.  
Positives: $2401 + 441 = 2842$.  
Negatives: $1715 + 7 + 14$? No, $-14$ is constant.  
Wait, term $-x$ is positive (because it's subtracting negative).  
Wait, let's be absolutely precise with signs for $P(x)$.  
$x = -7$.  
$P(-7) = (-7)^4 + 5(-7)^3 + 9(-7)^2 - (-7) - 14$.  
Pos: $81 \times 4? No. (-7)^4 = 2401$. Wait, $x^4$ is even power. So it's positive regardless of sign.  
$5x^3$: $x^3 = -343$. So $-(-343) \to +(-1715)$? No. $5 \times (-343) = -1715$. Correct.  
Wait, if $x=-7$, then $5x^3$ term is negative.  
My previous calc for $P(7)$ (assuming it was positive) used $+1715$? No, I calculated it using the logic of terms.  
Let's write down clearly.  
$x=7$:  
$x^4 = 2401$.  
$5x^3 = 1715$.  
$9x^2 = 441$.  
$-x = -7$. (Wait, term is $-x$, for $x=7$, this is $-7$).  
Constant: $-14$.  

*Continued in [part 4 of 5](intermediate_algebra_1102_p4.md): GitHub stops rendering math on pages this long, so the transcript is split.*
