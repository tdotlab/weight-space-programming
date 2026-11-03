# test/algebra/2064.json (Algebra, level 5)

> What is the maximum value of $4(x + 7)(2 - x)$, over all real numbers $x$?  

**Wrong.** Gold `81`, predicted `1`. Finish: length, 8192 tokens, 37 waits, 675.2 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's a thinking process that leads to the solution:  

1.  **Analyze the Problem:**  
The goal is to find the maximum value of the function $f(x) = 4(x + 7)(2 - x)$ for all real numbers $x$.  

2.  **Expand the Function (Optional but helpful):**  
Let's expand the term inside the parenthesis first or just look at the product form.  
The expression is a product of two linear terms: $(x+7)$ and $(2-x)$.  
$f(x) = 4 \cdot (x + 7)(2 - x)$  

3.  **Identify the Structure:**  
This looks like a difference of squares structure or simply expanding to a quadratic polynomial.  
Let's expand $(x + 7)(2 - x)$.  
Using FOIL: $x(2) - x(x) + 7(2) - 7(x)$  
$= 2x - x^2 + 14 - 7x$  
$= -x^2 - 5x + 14$  

So, the function is:  
$f(x) = 4(-x^2 - 5x + 14)$  
$f(x) = -4x^2 - 20x + 56$  

4.  **Recognize it as a Quadratic Function:**  
The expression $y = ax^2 + bx + c$ is a parabola.  
Here, $a = -4$, $b = -20$, and $c = 56$.  

5.  **Determine the Nature of the Parabola:**  
Since the coefficient of $x^2$ ($a = -4$) is negative ($a < 0$), the parabola opens downwards.  
Therefore, the vertex represents the maximum point of the function.  

6.  **Find the Vertex:**  
There are a few ways to find the x-coordinate of the vertex:  
    *   Formula: $x_v = -\frac{b}{2a}$  
    *   Completing the square / Vertex form ($y = a(x-h)^2 + k$)  

Using the formula:  
$x = -\frac{-20}{2(-4)}$  
$x = \frac{-20}{-8}$ ... wait, let's double check signs.  
$b = -20$.  
$a = -4$.  
Numerator: $-(-20) = 20$.  
Denominator: $2(-4) = -8$.  
Result: $x = \frac{20}{-8} = -\frac{5}{2}$ or $x = -2.5$.  

7.  **Calculate the Maximum Value:**  
Now plug $x = -2.5$ back into the original function or the expanded form to find the y-value ($k$).  

*Method A: Using Expansions*  
$f(-2.5) = -4(-2.5)^2 - 20(-2.5) + 56$  
$(-2.5)^2 = 6.25$  
$-4(6.25) = -25$  
$-20(-2.5) = +50$  
$f(x) = -25 + 50 + 56$  
$f(x) = 25 + 56$  
$f(x) = 81$  

*Method B: Using Original Form*  
$f(x) = 4(-2.5 + 7)(2 - (-2.5))$  
Inside first bracket: $-2.5 + 7 = 4.5$  
Inside second bracket: $2 + 2.5 = 4.5$  
$f(x) = 4(4.5)(4.5)$  
$f(x) = 4(4.5)^2$  
$4.5 = \frac{9}{2}$  
$f(x) = 4(\frac{81}{4})$  
$f(x) = 81$  

8.  **Alternative Method (Difference of Squares / AM-GM logic):**  
The expression is $4(x+7)(2-x)$.  
Let $u = x + 7$ and $v = 2 - x$.  
Then $u + v = (x + 7) + (2 - x) = 9$.  
Since the sum of factors $(x+7)$ and $(2-x)$ is constant ($9$), we can use algebraic properties.  
We want to maximize $4uv$ subject to $u+v=9$.  
The product of two numbers with a fixed sum is maximized when they are equal.  
So, set $x+7 = 2-x \Rightarrow 2x = -5 \Rightarrow x = -2.5$.  
Then $(x+7)(2-x) = (2.5)^2$ or rather the factors become $4.5$.  
Max value = $4 \times (4.5) \times (4.5)$ or $4 \times 4.5^2$.  
Wait, checking the expansion logic again:  
Let $P(x) = -x^2 - 5x + 14$. Vertex is at $-b/2a = 20/8$ ... no wait signs again.  
Coefficients of quadratic:  
Original: $(x+7)(2-x) = -x^2 + 2x - x + 14$? No.  
Wait, re-calculate expansion.  
$(x+7)(2-x) = x(2) + 7(2) - x(x) - x(7)$ ...  
$= 2x + 14 - x^2 - 7x$  
$= -x^2 - 5x + 14$.  
Correct.  
Max of $-x^2 - 5x + 14$ occurs at vertex.  
$a=-1$, $b=-5$, $c=14$.  
Vertex x = $-(-5) / (2*-1) = 5 / -2 = -2.5$. Correct.  
Max y-value:  
$y(-2.5) = -( (-2.5)^2 ) - 5(-2.5) + 14$  
$= -6.25 + 12.5 + 14$  
$= 6.25 + 14 = 20.25$. Correct (Wait, earlier I got 81).  
Where is the error?  
Ah, there was a factor of 4 in front.  
Original problem: $4(x+7)(2-x)$.  
So Max Value = $4 \times (\text{Max of quadratic})$.  
My previous calculation for Method A:  
$-4(6.25) = -25$ (This was from the expanded form with the 4).  
$f(x) = -4x^2 - 20x + 56$.  
$a=-4, b=-20$. Vertex x = $-(-20)/(2*-4) = 20/-8 = -2.5$.  
Value at vertex: $c + \frac{-b^2}{4a}$ ... formula is $y_{max} = c - \frac{b^2}{4a}$. Wait, usually it's $\frac{4ac - b^2}{4a}$. Or just plug in.  
Let's check the sign of vertex term again.  
$f(x) = 4(1 - 5x + (-x^2))$? No.  
Let's stick to Method B (AM-GM / Factor equalization). It was faster and less prone to arithmetic errors on expansion if done correctly.  

**Re-verification with Factor Equalization:**  
Maximize $4 \cdot u \cdot v$ where $u+v=9$.  
Max occurs when $u=v$.  
$u = 2 - x$ and $v = x + 7$.  
$2 - x = x + 7 \Rightarrow 2x = -5 \Rightarrow x = -2.5$.  
Then $u = 2 - (-2.5) = 4.5$.  
Then $v = -2.5 + 7 = 4.5$.  
So the expression becomes $4(4.5)(4.5) = 4(20.25) = 81$.  

Let's re-verify expansion calculation to ensure no sign errors.  
$(x+7)(2-x)$  
Expand: $x(-x)$ is wrong? No, terms are multiplied.  
$(x)(2) + (x)(-x) + (7)(2) + (7)(-x)$  
Wait.  
The first term in the first bracket is $x$. Second in second bracket is $-x$. Product is $-x^2$.  
The first term of $f(x)$ has to be multiplied by 4.  
So we have $-4x^2$.  
Next terms: $(x)(-7) = -7x$? No, look at the bracket $(2-x)$. It's $2-x$.  
So $x(-x)$ is $-x^2$ ? No, that's if you take $x \cdot x$ in a term.  
Let's write it out clearly:  
Expression inside: $A = (x+7)(2-x)$  
$A = x \cdot 2 + x \cdot (-x) + 7 \cdot 2 + 7 \cdot (-x)$ -- This is incorrect grouping in my head.  
Let's list terms:  
$x$ comes from first factor, times... ? No.  
Use FOIL carefully.  
First: $(x)(2) = 2x$  
Outer: $(x)(-x) = -x^2$  
Inner: $(7)(2) = 14$  
Last: $(7)(-x) = -7x$  
Sum: $-x^2 + 50 + 14 - ...$ No.  
Wait, $2x - x^2 - 7x = -x^2 - 5x$.  
Then add 14.  
So $-x^2 - 5x + 14$.  
Multiply by 4: $-4x^2 - 20x + 56$.  
Vertex of $ax^2+bx+c$: $x = -b/2a$.  
$x = -(-20) / (2 \cdot -4) = 20 / -8 = -2.5$.  
Max value = $-4(-2.5)^2 - 20(-2.5) + 56$  
$= -4(6.25) + 50 + 56$  
$= -25 + 106$  
$= 81$.  

Why did I think 81 was correct in the first attempt and doubted it?  
Wait, Method B calculation: $4(4.5)^2 = 4(20.25) = 81$. Correct.  
Method A calculation (in doubt earlier):  
$y(-2.5)$ using expansion form $-x^2 - 5x + 14$.  
$y(-2.5) = -6.25 - 5(-2.5) + 14$  
$= -6.25 + 12.5 + 14$  
$= 5.75 + 14$? No, $-6.25+12.5 = 6.25$.  
$6.25 + 14 = 20.25$.  
Ah, so the max value of $(x+7)(2-x)$ is $20.25$.  
Then multiplying by 4 gives $81$.  
Everything seems consistent.  

9.  **Consider Domain:**  
The problem states "over all real numbers x". So domain is $\mathbb{R}$.  
Function is continuous everywhere, differentiable everywhere.  
Parabola opens down (coefficient of $x^2$ is -4), so vertex is a global maximum.  

10. **Alternative perspective (Discriminant):**  
Max value is related to the discriminant if we were looking for roots? Not really useful here.  
Roots are where $(x+7)(2-x) = 0$.  
$x = -7$ and $x = 2$.  
The function crosses zero at these points.  
At vertex $x = -2.5$, we have a maximum positive value.  

11. **Structure the Step-by-Step Reasoning:**  
    *   State the function: $f(x) = 4(x + 7)(2 - x)$.  
    *   Goal: Maximize this product.  
    *   Observe that it's a quadratic in $x$ or can be viewed as maximizing the product of two numbers whose sum is constant.  
    *   **Approach 1: Algebraic Expansion.**  
        *   Expand $(x+7)(2-x)$.  
        *   Calculate coefficients for $f(x)$.  
        *   Identify $a = -4$, $b = -20$, $c = 56$.  
        *   Calculate the axis of symmetry (vertex x-coordinate).  
        *   Calculate $f$ at that vertex.  
    *   **Approach 2: AM-GM Inequality (for the product).**  
        *   Rewrite as $4(x+7)(2-x)$.  
        *   Let $A = x+7$ and $B = 2-x$.  
        *   Note that $A + B = x + 7 + 2 - x = 9$.  
        *   We want to maximize $4AB$ given $A+B=9$.  
        *   For positive numbers with a fixed sum, product is maximized when numbers are equal.  
        *   Check if the domain for AM-GM allows this (numbers can be negative, product can be larger? No, AM-GM works on real numbers where we know the behavior).  
Wait, $(x+7)$ and $(2-x)$. Their sum is 9.  
Can both be negative? If $x > -7$ but $x < 2$, no, that doesn't make them both negative if $x$ varies.  
Actually, AM-GM holds for positive numbers or specific signs. Here we have a max value problem. Since the function is a downward opening parabola with vertex at -2.5, and roots at -7 and 2.  
Between -7 and 2, $(x+7)$ is positive and $(2-x)$ is positive.  
Outside this range (e.g., $x < -7$ or $x > 2$), one factor is negative, the other is positive?  
Wait. If $x < -7$, $x+7 < 0$. If $x > 2$, $2-x < 0$.  
So if $x \in (-\infty, -7)$, one term is pos, one neg. Product negative. Function is neg?  
Let's check sign of original function $f(x) = 4(x+7)(2-x)$.  
            *   If $x > 2$: $(x+7) > 0$, $(2-x) < 0$. Product is negative. Max value must be positive (assuming global max exists).  
            *   If $-7 < x < 2$: Both terms positive. Product positive. Vertex here is max? Yes, for $a=-4$ parabola, vertex gives max.  
Wait, the domain of AM-GM (maximize product) usually assumes numbers are non-negative. Since sum is positive ($9$), they must be $\ge 0$. If both were negative, sum would be negative (sum=9). So we can safely apply the logic that factors should be equal to maximize magnitude, provided they are same sign or check boundary conditions. Actually, for $y = -ax^2+bx+c$, vertex is max regardless of signs.  
Let's stick to the AM-GM intuition: To maximize product $xy$ given sum $x+y=C$, set $x=y$. Here we have $4(x+7)(2-x)$. Sum of factors is 9. Max value = $4 \times (\text{product of terms equal})^2 / 1$? No, just $4 \times (9/2)^2$.  
Is it possible for $(x+7)$ and $(2-x)$ to be such that their product is higher?  
The quadratic has roots -7 and 2. Vertex is between them. The function is positive between the roots. Outside, it's negative. Since we are looking for max value, we only care about the region where it can't go up (which is the peak). So checking $x=-2.5$ is sufficient.  

    *   **Calculation:**  
$4 \times 4.5 \times 4.5 = 81$.  

12. **Final check of the steps.**  
Expression: $4(x+7)(2-x)$  
Let's double check the question isn't asking for "maximum *integer* value" or something. It just says "real numbers x".  
The logic holds up.  

Step 1: Define function.  
Step 2: Notice it is a quadratic $-4x^2 ...$  
Step 3: Vertex formula or completing the square to find max.  
Let's try completing the square just to be absolutely certain about arithmetic.  
$y = -4(x^2 + 5x) + 56$ -- wait, $(x+7)(2-x) = -x^2 - 5x + 14$.  
Wait, $(x+7)(2-x) = (x+7)(-(x-2)) = -(x+7)(x-2) = -(x^2 - 5x - 14)$? No.  
$-(x^2 - 5x - 14)$ would be $-x^2 + 5x + 14$. My expansion was $-x^2 - 5x + 14$.  
Let's re-expand $(x+7)(2-x)$.  
$(x+7)(2) = 2x + 14$  
$(x+7)(-x) = -x^2 - 7x$  
Sum: $2x + 14 - x^2 - 7x = -x^2 - 5x + 14$.  
Yes, coefficient of $x$ is negative (-5).  
Wait, earlier in AM-GM I assumed sum is constant. Let's check the quadratic vertex again.  
Sum of factors: $(x+7) + (2-x) = x-7 - x + 7 = 0$? No.  
$x + 7 + 2 - x = 9$. Correct.  
So if sum is constant 9, product is maximized when terms are equal ($4.5$).  
Max value is $4(4.5)(4.5) = 81$.  

Wait, why did I have a doubt about $-5x$ vs $+5x$ earlier?  
Let's re-evaluate $(x+7)(2-x)$ expansion carefully one last time.  
Let $x=0$. Product should be $7 \cdot 2 = 14$. Formula $-0^2 - 5(0) + 14 = 14$. Correct.  
Let $x=-2$. Terms: $(-2+7)(2-(-2)) = (5)(4) = 20$.  
Formula: $-(-2)^2 - 5(-2) + 14 = -4 + 10 + 14 = 20$. Correct.  
Let $x=-2.5$. Terms: $4.5 \cdot 4.5 = 20.25$.  
Formula: $-6.25 - 5(-2.5) + 14 = -6.25 + 12.5 + 14 = 20.25$. Correct.  

Okay, everything is consistent. The max value of $(x+7)(2-x)$ is $20.25$.  
Then multiply by 4 to get 81.  

Wait... I just noticed the expansion $(x+7)(2-x)$.  
Usually, a sum $a+b = k$ implies max product for positive numbers.  
Here we are maximizing $(x+7)(2-x)$.  
Let's check if $x$ can be anything such that terms are both positive.  
For $x+7 > 0 \implies x > -7$.  
For $2-x > 0 \implies x < 2$.  
So for any $x \in (-7, 2)$, the product is positive.  
The vertex $x = -2.5$ lies inside this interval.  
What about outside? If $x > 2$, one term negative, product negative.  
If $x < -7$, one term negative, product negative.  
So the global maximum must occur in the interval where the function is positive (and is a parabola opening down), which confirms finding the vertex is correct for the *global* maximum as well.  

Wait, I see "maximum value" vs "minimum value". Since coefficient of $x^2$ is negative (-4), it opens downward, so vertex is indeed the global maximum.  

**Final check:**  
Function: $f(x) = 4(x+7)(2-x)$  
Vertex x-coordinate: $x = -\frac{b}{2a}$.  
Expanded form: $-4x^2 - 20x + 56$ (after expanding $4(-x^2-5x+14)$).  
Wait, in step 3 I wrote:  
$f(x) = -4x^2 - 20x + 56$.  
Let's re-expand the constant term. $4(14) = 56$. Correct.  
Linear term coefficient:  
From expansion of $(x+7)(2-x)$, coeff was $-5x$. Multiplied by 4 gives $-20x$. Correct.  
Quadratic term: $4(-x^2)$ is $-4x^2$. Correct.  

Vertex calculation check:  
$x = -(-20)/(2*-4) = 20 / -8 = -5/2$.  
Value check check check again.  
$f(-5/2) = 4( (-5/2) + 7 )( 2 - (-5/2) )$  
$= 4( ( -5/2 + 14/2 )( 4/2 + 5/2 ) )$  
$= 4( (9/2)( 9/2 ) )$  
$= 4( 81 / 4 )$  
$= 81$.  

Wait, did I mess up the linear term coefficient sign in my manual check just now?  
$(x+7)(2-x) = -x^2 - 5x + 14$.  
Let's re-verify signs of coefficients.  
$x(-x)$ gives $-x^2$ (quad term, negative).  
$x(-7x)$ wait...  
Expansion: $(x+7)(2-x) = 2x - x^2 + 14 - 7x$.  
Group $x$: $2x - 7x = -5x$. Correct.  
So the coefficient of $x$ in $f(x)$ is $-4 \times (-5) = +20$? No.  
Let's write down $f(x) = 4(-x^2 - 5x + 14)$.  
$= -4x^2 - 20x + 56$.  
Vertex formula is $-b/(2a)$ for $ax^2+bx+c$.  
Here $a=-4$, $b=-20$.  
$x = -(-20)/(2*-4) = 20 / -8 = -2.5$.  
Wait, previously I calculated vertex as:  
For $-x^2 - 5x + 14$, vertex is $-(-5)/ (2*-1) = 5/-2 = -2.5$.  
So for the expanded form with a factor of 4, we must use the coefficients of that expanded form directly or just scale? No, vertex scales linearly.  
Wait, scaling does not shift the vertex horizontally if you think about "shifting" by factor of 4. But wait...  
Max of $y = c \cdot (quadratic)$. The maximum of $c \cdot q(x)$ occurs where $q(x)$ is max. Since max of $q(x)$ happens at a specific x, the max of scaled version happens at same x.  
So finding x for $f(x) = -4x^2 + ...$ leads to $x=-2.5$.  
But let's check the calculation $f(-2.5)$ again.  
$f(-2.5) = 4( (-2.5+7)(2-(-2.5)) )$.  
$= 4( (4.5)(4.5) )$.  
Wait, why did I think linear coeff was positive before?  
In previous check: "Let's try completing the square... $y = -4(x^2 + 5x) + 56$ ... Wait, $(x+7)(2-x)$ expansion... $= -x^2 - 5x + 14$."  
Wait.  
$(-x^2 - 5x + 14) = -(x^2 + 5x - 14)$.  
$-( (x+2.5)^2 - 6.25 - 14 )$? No.  
$x^2 + 5x = (x+2.5)^2 - 6.25$.  
So inside parenthesis is $-( (x+2.5)^2 - 6.25 + 14)$... no, constant is +14.  
Inside: $(x+7)(2-x) = 14 + x(2) + 7(2) - x^2 - 7x$ ...  
Wait. $x \cdot (-x)$ is $-x^2$.  
$x(2) = 2x$.  
$x(-7) = -7x$.  
$7(2) = 14$.  
Sum: $-x^2 - 5x + 14$.  
Yes.  
So vertex x for this quadratic is at $-b/(2a) = -(-5)/(2*-1)$ (with a= -1, b=-5).  
$= 5 / (-2) = -2.5$.  
Correct.  

Wait, earlier I calculated value using coefficients of expanded form with $4$.  
$f(x) = 4(-x^2 - 5x + 14) = -4x^2 - 20x + 56$.  
Vertex x: $-b/(2a) = -(-20)/(2*-4) = 20 / (-8) = -2.5$.  
Both methods yield $x=-2.5$.  

Let me re-read the "linear coeff" confusion in step 12 thought process just now to ensure clarity.  
In my head: "$f(x) = 4(-x^2 - 5x + 14)$".  
Linear term is $4 \times (-5x) = -20x$.  
Quadratic term is $4 \times (-x^2) = -4x^2$.  
Constant term is $4 \times 14 = 56$.  
So $f(x) = -4x^2 - 20x + 56$.  
Vertex formula: $-(-20)/(2*-4) = 20/-8 = -2.5$.  
This seems correct.  

Is there any trap? "Maximum value".  
Since $a=-4 < 0$, vertex is max.  
The calculation $4(4.5)(4.5)$ is robust.  

Final check of the question text: "What is the maximum value... over all real numbers x?"  
No tricks found.  

Let's quickly write out the solution steps clearly.  
1. Define function.  
   2. Recognize form $4(u)(v)$ where $u+v = 9$.  
    3. Apply logic that product is max when $u=v=4.5$.  
    4. Compute $4(4.5)^2 = 81$.  
    5. Verify with expansion to confirm no calculation errors in thinking process.  

Double check: $(x+7)(2-x)$.  
If $x = -6$: $(-6+7)(2-(-6)) = (1)(8) = 8$. $4(8)=32$.  
If $x = -3$: $(-3+7)(2-(-3)) = (4)(5) = 20$. $4(20)=80$.  
If $x = -4$: $(3)(6) = 18$. $4(18)=72$.  
If $x = -2.5$: $4.5 \times 4.5 = 20.25$. $4 \times 20.25 = 81$.  
Max value is indeed at the vertex.  

The solution is solid.  

Wait, I should double check the sign of $x^2$ term in $(x+7)(2-x)$.  
Is it possible to write $(x+7)(2-x)$ as something else? No, multiplication is commutative.  
$-x(x) + ...$  
It's definitely negative $x^2$. So the parabola opens down.  

What if I made a mistake in "sum of factors"?  
$(x+7) + (2-x) = x - x + 7 + 2 = 9$.  
Yes, sum is constant.  
Product of two numbers with fixed sum is maximized when they are equal.  
This is the core algebraic insight. It's faster than expanding quadratics for mental math or checking signs (though here signs aren't tricky).  
$4 \times (9/2) \times (9/2) = 81$.  

Wait, does AM-GM require non-negative numbers?  
$A+B=9$. Maximize $AB$.  
We found max is at $A=4.5$. Then $B=4.5$. Both are positive.  
What if sum was negative? e.g. sum = -10. Max product would be at $-5, -5$, giving 25. But then we have a factor of 4 and it's $4(-5)(-5) = 100$.  
However, here the range of valid x is where product is potentially maximized.  
Wait, if we consider function values:  
$f(x)$ goes to infinity? No, coefficient of highest power ($x^2$) is negative, so it goes to $-\infty$ as $|x| \to \infty$.  
So global max must be at vertex.  
Since vertex occurs inside the region where $u, v > 0$, AM-GM holds perfectly without caveats.  

Final answer seems to be 81.  

Let's write down the response based on this thought process.  
Step 1: Expand or substitute to find quadratic form or use properties of product with constant sum. I will use the expansion method as primary, maybe mention the symmetry property. Expansion is usually standard for these questions.  

Expansion:  
$f(x) = 4(x + 7)(2 - x)$  
$= 4 [ x(2 - x) + 7(2 - x) ]$ -- No, that's messy.  
Standard FOIL:  
$= 4 [ 2x - x^2 + 14 - 7x ]$  
$= 4 [ -x^2 - 5x + 14 ]$  
$= -4x^2 - 20x + 56$.  

Find vertex of $-4x^2 - 20x + 56$:  
Axis of symmetry: $x = -b / (2a)$  
$a = -4, b = -20$.  
$x = -(-20) / (2 \cdot -4) = 20 / -8 = -2.5$.  

Evaluate function at vertex:  
Substitute $x = -2.5$ into $f(x)$ or the expanded form.  
Using expanded form: $-4(-2.5)^2 - 20(-2.5) + 56$  
$= -4(6.25) + 50 + 56$  
$= -25 + 50 + 56$  
$= 81$.  

Alternative check using vertex form of $-x^2 - 5x + 14$:  
$y = a(x-h)^2 + k$ where $h = -b/2a$.  
Here $a=-1, b=-5 \implies h = -(-5)/(-2) = 5/-2 = -2.5$.  
Wait, $a$ in vertex formula is just coefficient of x^2? No, usually standard form.  
If $y = -x^2$, vertex is $(0,0)$. If $y=-(x-h)^2+k$, vertex is $(h,k)$.  
$-x^2 - 5x + 14 = -(x^2 + 5x) + 14$ ... completing square requires adding/subtracting $(5/2)^2 = 6.25$.  
$-(x^2 + 5x + 6.25) + 6.25 + 14$  
$= -(x + 2.5)^2 + 20.25$.  
Max value is the constant term when squared part is zero (which happens at vertex).  
So max y-value is $20.25$.  
Then multiply by 4: $4 \times 20.25 = 81$.  

This second calculation ($f(x)$) is cleaner because it isolates the term immediately before multiplying by 4.  
$(x+7)(2-x) = -x^2 - 5x + 14 = -(x + 2.5)^2 + (6.25 + 14)$.  
Wait, $-(x^2 + 5x)$ needs to complete square correctly.  
$x^2+5x$ becomes $(x+2.5)^2 - 6.25$.  
So $-[(x+2.5)^2 - 6.25] + 14 = -(x+2.5)^2 + 6.25 + 14 = -(x+2.5)^2 + 20.25$.  
Multiply by 4: $4[-(x+2.5)^2 + 20.25] = -4(x+2.5)^2 + 81$.  
Clearly max is 81.  

The reasoning holds up perfectly.  

Final Answer seems to be 81.  


## Answer

To find the maximum value of the expression $f(x) = 4(x + 7)(2 - x)$, we can follow these steps:  

**Step 1: Expand the quadratic polynomial.**  
First, let's expand the product inside the parentheses by applying the distributive property (FOIL method):  

