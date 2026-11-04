# test/algebra/2064.json (Algebra, level 5)

> What is the maximum value of $4(x + 7)(2 - x)$, over all real numbers $x$?  

**Correct.** Gold `81`, predicted `81`. Finish: stop, 4543 tokens, 0 waits, 367.5 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's a thinking process that leads to the solution:  

1.  **Analyze the Problem:**  
    *   The goal is to find the maximum value of the function $f(x) = 4(x + 7)(2 - x)$.  
    *   The domain of $x$ is all real numbers ($\mathbb{R}$).  

2.  **Recognize the Structure:**  
    *   The expression looks like a product of two linear terms: $(x + 7)$ and $(2 - x)$.  
    *   This form $a(x - c_1)(c_2 - b)x$ suggests that it can be rewritten as a constant times a quadratic polynomial.  

3.  **Expand the Polynomial:**  
    *   Let's expand $f(x) = 4(x + 7)(2 - x)$.  
    *   First, ignore the coefficient 4 for a moment.  
    *   Multiply the terms inside the parentheses: $(x + 7)(2 - x)$.  
    *   Use the FOIL method (First, Outer, Inner, Last).  
        *   First: $x \cdot 2 = 2x$  
        *   Outer: $x \cdot (-x) = -x^2$  
        *   Inner: $7 \cdot 2 = 14$  
        *   Last: $7 \cdot (-x) = -7x$ (or $-x \cdot 7$)  
    *   Combine like terms: $2x - x^2 + 14 - 7x$.  
    *   Rearrange by powers of $x$: $-x^2 - 5x + 14$.  
    *   Now, apply the coefficient 4 that was outside the parentheses.  
    *   $f(x) = 4(-x^2 - 5x + 14)$  
    *   $f(x) = -4x^2 - 20x + 56$.  

4.  **Identify the Type of Quadratic:**  
    *   The function is a quadratic equation in terms of $x$: $y = ax^2 + bx + c$.  
    *   Here, $a = -4$, $b = -20$, and $c = 56$.  

5.  **Find the Nature of the Quadratic:**  
    *   Since the coefficient of $x^2$ is negative ($a = -4$), the parabola opens downwards.  
    *   Therefore, the vertex represents a maximum value.  
    *   (Note: If $a > 0$, it would be a minimum).  

6.  **Find the Vertex:**  
    *   The x-coordinate of the vertex for a quadratic $y = ax^2 + bx + c$ is given by the formula $x = \frac{-b}{2a}$.  
    *   Substitute the values:  
        *   $x = -(-20) / (2 \cdot -4)$  
        *   $x = 20 / (-8)$  
        *   $x = -5/2$ or $-2.5$.  

7.  **Calculate the y-value at the Vertex:**  
    *   Now substitute $x = -5/2$ back into the function $f(x) = -4x^2 - 20x + 56$.  
    *   Method A: Direct substitution.  
        *   $f(-5/2) = -4(-5/2)^2 - 20(-5/2) + 56$  
        *   Calculate the square term: $(-5/2)^2 = 25/4$.  
        *   Term 1: $-4(25/4) = -25$.  
        *   Term 2: $-20(-5/2) = +10 \cdot 5 = 50$.  
        *   Constant term: $56$.  
        *   Sum: $-25 + 50 + 56$.  
    *   Calculation:  
        *   $50 - 25 = 25$.  
        *   $25 + 56 = 81$.  

    *   Method B: Completing the square.  
        *   $f(x) = 4(x^2 + 5x)$ ... No, factor out the negative from inside to make vertex easier? Or stick to expanding.  
        *   Original: $4(x+7)(2-x)$.  
        *   Vertex form of $(x+a)(x+b) = x^2 + (a+b)x + ab$.  
        *   Here we have $(x-(-5/2))$ and $(x-2)$. This is getting complicated. Let's stick to the vertex formula on $f(x)$.  

    *   Method C: Completing the square for $4x^2+...$ inside.  
        *   $-4x^2 - 20x + 56$.  
        *   Factor out -4? No, let's factor out 4 from outside first to keep vertex simple?  
        *   $f(x) = 4 [ (x+7)(2-x) ]$.  
        *   Focus on $(x+7)(-x+2)$ or similar.  
        *   Let's use the standard vertex formula again but simpler numbers.  
        *   Parabola: $y = -4(x^2 + 5x - \dots)$.  
        *   $f(x) = -4(x^2 + x(-5/2?) + \dots)$. No, let's just use the completed square form directly from $-4x^2 - 20x$.  
        *   $-4 (x^2 + 5x)$ ? No.  
        *   Let's look at $(x+7)(2-x) = -(x+7)(x-2)$.  
        *   Roots are $x=-7$ and $x=2$. The axis of symmetry is midway between roots.  
        *   Midpoint: $\frac{-7 + 2}{2} = \frac{-5}{2} = -2.5$. This matches Method A calculation for x.  
        *   Calculate the value at midpoint relative to the roots' product?  
        *   At $x = -2.5$, $x+7 = 4.5$ and $2-x = 2 - (-2.5) = 4.5$.  
        *   So $(x+7)(2-x) = (4.5)(4.5) = (9/2)^2 = 81/4$.  
        *   Multiply by 4: $4 \cdot (81/4) = 81$.  

    *   Method D (Visual check):  
        *   Roots of $(x+7)(2-x)=0$ are $x=-7$ and $x=2$.  
        *   Between these roots, the quadratic opens downwards. The maximum must be at the vertex.  
        *   Vertex is halfway between -7 and 2: $\frac{-7+2}{2} = \frac{-5}{2}$.  
        *   Value: $4 \cdot (\frac{9}{2})^2 = 4 \cdot \frac{81}{4} = 81$.  

8.  **Alternative Approach: AM-GM Inequality?**  
    *   The problem asks for the maximum of $(x+7)(2-x) \times 4$. Since it's a product, maybe we can interpret it as area or something?  
    *   For $ax > 0$ and $bx > 0$, $a+b$. But here one term is positive, one is negative in the interval. The product $(x+7)(2-x)$ is positive only if $-7 < x < 2$. Since we want the maximum value of the function (which is positive), the sign doesn't matter yet, but let's check.  
    *   Let $u = x+7$ and $v = -(x-2) = -x+2$. Then product is $(x+7)(-(x-2)) = -4u^2 + ...$ no.  
    *   Consider the expression $(A-x)(C+x) = (x-A)(x+C)$.  
    *   This looks like $(c_1 - x)(c_2 - x)$ where $c_1=7$ and $c_2=2$.  
    *   Let's try substitution to get product.  
    *   The term is $(4.5)(4.5) = 20.25$. Multiply by 4 gives 81.  
    *   This relies on $x=-2.5$ giving max value for the square part.  

9.  **Verification:**  
    *   Expression: $g(x) = (x+7)(2-x)$.  
    *   We want max of $4 \cdot g(x)$.  
    *   Max occurs at midpoint of roots $-7, 2$.  
    *   Midpoint: $\frac{-7 + 2}{2} = -2.5$.  
    *   Calculate $g(-2.5) = (-2.5 + 7)(2 - (-2.5)) = (4.5)(4.5) = \frac{90}{16} \cdot \dots$ No, $4.5^2 = 20.25$.  
    *   $4 \cdot 20.25 = 81$.  
    *   Calculation check: $4.5 \times 4.5$:  
        *   $4 \times 4 = 16$  
        *   $0.5 \times 4 = 2$  
        *   $16 + 2(4) + 0.25 = 16 + 8 + 0.25$? No.  
        *   $(a+b)^2 = a^2 + 2ab + b^2$. Let $a=4, b=0.5$.  
        *   $16 + 4 + 0.25 = 20.25$. Correct.  
    *   Multiply by 4: $20.25 \times 4$.  
        *   $20 \times 4 = 80$.  
        *   $0.25 \times 4 = 1$.  
        *   $80 + 1 = 81$.  

10. **Final Conclusion Formulation:**  
    *   State the function clearly.  
    *   Expand the polynomial.  
    *   Identify it as a downward opening parabola ($a < 0$).  
    *   Calculate vertex x-coordinate (axis of symmetry).  
    *   Substitute back to find max value.  
    *   Alternatively, use the midpoint property of roots for $(x-a)(c-x)$.  

Let's write down the steps clearly.  
Function: $y = 4(x+7)(2-x)$  
Expand inside: $(x+7)(-x+2)$? No, standard FOIL is better written as $(x+7)(-(x-2))$.  
$(x+7)(-(x-2)) = -(x^2 + 5x - 14)$.  
So $y = -4(x^2 + 5x - 14)$?  
Let's check expansion again.  
$(x+7)(2-x) = x(2) - x(x) + 7(2) - 7(x) = 2x - x^2 + 14 - 7x = -x^2 - 5x + 14$.  
Multiply by 4: $-4x^2 - 20x + 56$. Correct.  
Max value occurs at vertex $x = \frac{-b}{2a}$.  
$a = -4, b = -20$.  
$x = \frac{20}{-8} = -\frac{5}{2}$.  
Substitute into quadratic:  
$y = 4(-(-5/2) + 7)(2 - (-5/2))$?  
Let's re-evaluate vertex calculation on the original factors.  
$x+7 = 4.5$.  
$2-x = 2 - (-2.5) = 4.5$.  
Product = $4.5 \times 4.5 = 20.25$.  
Multiply by 4 = $81$.  

The logic holds up completely.  

Double check arithmetic.  
$x = -2.5$  
Term 1: $x+7 = -2.5 + 7 = 4.5$  
Term 2: $2-x = 2 - (-2.5) = 4.5$  
Product: $(9/2) \cdot (9/2) = 81/4$.  
Multiply by 4: $81/4 \cdot 4 = 81$.  

Does it make sense? The roots of the original polynomial expression are -7 and 2.  
Is 81 > value at infinity? Yes, as $x \to \infty$, $-x^2$ dominates, goes to $-\infty$. As $x \to -\infty$, same. So it's bounded.  
The peak is at the vertex.  

Final check of the question phrasing: "maximum value". Yes. "real numbers x". Yes.  
Everything seems correct.  

Let's quickly check if there are any trick constraints hidden in "over all real numbers". None, standard quadratic problem.  

Is there any ambiguity with the order? $4(x+7)(2-x)$.  
Maybe $4 \cdot (x+7)$ first, then times $(2-x)$? No, multiplication is commutative and associative. Order doesn't matter.  
Just ensuring I didn't misread signs.  
$2-x$ means $-(x-2)$. Correct.  
Roots are -7 and 2. Correct.  

Step-by-step derivation for the final output:  
1. Define the function $f(x) = 4(x+7)(2-x)$.  
   2. Expand the polynomial to identify the structure (quadratic).  
$(x+7)(2-x) = -x^2 + 5x$? No.  
Let's redo expansion one more time carefully.  
$(x+7)(2-x) = x(2-x) + 7(2-x)$  
$= (2x - x^2) + (14 - 7x)$  
$= -x^2 - 5x + 14$.  
    3. Multiply by 4: $f(x) = -4x^2 - 20x + 56$.  
    4. Identify vertex. Since $a = -4 < 0$, max exists.  
x-coordinate is $\frac{-b}{2a}$.  
$x = \frac{-(-20)}{2(-4)} = \frac{20}{-8} = -\frac{5}{2} = -2.5$.  
    5. Calculate maximum value $f(-2.5)$.  
Method 1:  
$f(-2.5) = 4((-2.5) + 7)(2 - (-2.5))$  
$= 4(4.5)(4.5)$  
$= 4(20.25)$  
$= 81$.  

Method 2 (Completing square):  
$f(x) = -4(x^2 + 5x - \dots)$  
$= -4(x^2 + 5x - 14 + \dots)$  
Complete square for $-4x^2 - 20x$.  
Factor out -4: $-4(x^2 + 5x)$.  
Add and subtract $(5/2)^2 = 6.25$ inside parenthesis? No, just add term to make perfect square.  
To get $(x+3.25)^2$ from $x^2+5x$. No.  
Standard formula: $\frac{4ac}{a}$ or similar logic?  
Using $(y-k)$ form on the expression $(x+7)(2-x)$.  
The max of $(A+x)(B-x)$ where $A=7, B=2$ (so roots are -A and B) is $A^2/4$? No.  
Let's stick to the arithmetic verification which was cleanest.  
$x=-2.5 \implies x+7 = 4.5$.  
$2-x = 4.5$.  
Product is $4.5 \times 4.5 = 20.25$.  
Multiply by 4 -> 81.  

The solution seems robust.  


## Answer

To find the maximum value of the function $f(x) = 4(x + 7)(2 - x)$ over all real numbers $x$, we can proceed with the following steps:  

**Step 1: Expand the polynomial.**  
First, let's expand the expression $(x + 7)(2 - x)$. We use the FOIL method (First, Outer, Inner, Last):  
$$
\begin{aligned}
(x + 7)(2 - x) &= x \cdot 2 + x(-x) + 7 \cdot 2 + 7(-x) \\
&= 2x - x^2 + 14 - 7x
\end{aligned}
$$
Combine like terms ($2x - 7x = -5x$):  
$$
(x + 7)(2 - x) = -x^2 - 5x + 14
$$

**Step 2: Multiply by the coefficient.**  
Now, substitute this back into the original function multiplied by 4:  
$$
f(x) = 4(-x^2 - 5x + 14)
$$
Distribute the 4:  
$$
f(x) = -4x^2 - 20x + 56
$$

**Step 3: Identify the vertex of the parabola.**  
The function $f(x)$ is a quadratic equation of the form $ax^2 + bx + c$, where $a = -4$, $b = -20$, and $c = 56$. Since the coefficient of the $x^2$ term ($a$) is negative ($-4 < 0$), the parabola opens downwards, meaning the vertex represents a maximum value.  

The x-coordinate of the vertex is given by the formula:  
$$ x = \frac{-b}{2a} $$  
Substitute the values:  
$$ x = \frac{-(-20)}{2(-4)} = \frac{20}{-8} = -\frac{5}{2} = -2.5 $$  

**Step 4: Calculate the maximum value.**  
Substitute $x = -2.5$ (or $\frac{-5}{2}$) back into the function $f(x)$ to find the y-coordinate of the vertex.  

Method A: Using the expanded form  
$$
\begin{aligned}
f(-2.5) &= -4(-2.5)^2 - 20(-2.5) + 56 \\
&= -4(6.25) + 50 + 56 \\
&= -25 + 50 + 56 \\
&= 81
\end{aligned}
$$

Method B: Using the factored form (faster for checking)  
Note that the roots of the expression $(x+7)(2-x)=0$ are $x=-7$ and $x=2$. The axis of symmetry is halfway between these roots.  
$$ \text{Axis of Symmetry } x = \frac{-7 + 2}{2} = -2.5 $$  
Evaluate $(x+7)(2-x)$ at $x=-2.5$:  
$$
(-2.5 + 7)(2 - (-2.5)) = (4.5)(4.5) = 20.25
$$
Multiply by the coefficient 4:  
$$
4(20.25) = 81
$$

Both methods yield the same result.  

\boxed{81}  
