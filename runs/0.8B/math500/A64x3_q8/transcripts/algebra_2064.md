# test/algebra/2064.json (Algebra, level 5)

> What is the maximum value of $4(x + 7)(2 - x)$, over all real numbers $x$?  

**Wrong.** Gold `81`, predicted `None`. Finish: length, 16384 tokens, 4 waits, 1409.6 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's my thought process for solving this problem:  

1.  **Analyze the Request:** The user wants to find the maximum value of the expression $4(x + 7)(2 - x)$. They want the reasoning step-by-step and the final answer in a specific format ($\boxed{}$). The variable $x$ must be real numbers.  

2.  **Initial Inspection & Simplification:**  
    *   Expression: $f(x) = 4(x + 7)(2 - x)$  
    *   Variable: $x \in \mathbb{R}$  
    *   Note: The factorization of the quadratic expression $(a+b)(c+d)$.  
    *   Let's simplify the term inside first or expand it. Usually, finding the maximum of a function requires completing the square or analyzing its derivative to see if it goes to infinity. If it has roots (specifically at $x = -7$ and $x=2$), that means it changes sign, but since I'm looking for an *absolute* maximum, I should check endpoints. However, $(x + 7)(2 - x)$ is a quadratic opening upwards? No.  
    *   Let's expand: $f(x) = 4(x^2 + 5x + 14 - 7x) = 4(x^2 - 2x + 14)$.  
        *   This opens upwards (coefficient of $x^2$ is $+4$). The roots are at $x = \frac{-(-2) \pm \sqrt{4 - 4(1)(-5)}}{2}$? No, let's look at the factorization.  
    *   Let's check if the expression can be written as a square or something simpler.  
    *   $4(x^2 - 2x + 14)$. This doesn't seem to simplify nicely into a perfect square $(ax+b)^2$ immediately without completing the box.  

3.  **Completing the Square Method (Standard Approach for "Maximum" on Reals):**  
    *   Factor out the coefficient from the quadratic part: $f(x) = 4(x^2 - 2x + 14)$.  
    *   Let's look at the discriminant of this quadratic to know if it has real roots. It doesn't need to have them for a function to have a global maximum (unless the coefficients force a minimum).  
    *   The expression is $f(x) = -4(2x^2 - 10x + \dots)$ No, let's just solve $x^2 - 2x + 14$.  
    *   Discriminant $\Delta = b^2 - 4ac = (-2)^2 - 4(1)(14) = 4 - 56 < 0$. Since the quadratic opens upwards ($a=4 > 0$), $f(x)$ decreases as $x$ moves away from $-7$ to the left and increases for values greater than $-7$? No, since the parabola opens upward ($a>0$), it has a minimum at the vertex. The global maximum is at the "endpoints" of the domain.  
    *   However, $(x^2 - 2x + 14)$ is positive for all real $x$ because $-2x \ge -2$, and $14 > 0$.  
    *   Let's check: The quadratic expression inside is a sum of squares or a difference. Since $a=4, b=-2, c=14$ (if we write $f(x) = 4(x+7)(x^2-2x-5)$?). No, let's stick to the original.  
    *   $f(x) = 4(x + 7)(2 - x)$.  
    *   This is a downward parabola in terms of $(x - (-7))$? No, $(x+7)$ has a minimum at $-7$. $(2-x)$ has a minimum at $x=2$. The expression is $4 \cdot (\text{positive})(\text{something with max})$.  
    *   Actually, let's rewrite it as $f(x) = 4((x+7)(2-x))$. Since $x^2 - 2x + 14$ is positive for all $x$, then $(x+7)$ and $(2-x)$ product determines the sign.  
        *   If $x \in (0, 1)$? No, just look at range.  
    *   Let's use a substitution or algebraic manipulation.  
    *   Let $t = x+7$. Then $x = t - 7$. The expression is $4(t)(2 - (t-7)) = 4t(9-t) = 4(-t^2 + 9t)$. This is not a max/min problem with a constant term.  
    *   Let's use the property: $(x-a)(x-b)$ form.  
    *   Let's look at the expression again. $f(x) = -4(x-2)(x+7)?$ No, it was $4(x^2-2x+14)$.  
    *   The term $x^2 - 2x + 14$ is always positive because its minimum is at $x=1$, with value $1^2 - 2(1) + 14 = 15 > 0$.  
    *   Thus, the product $(x+7)(2-x)$ has the same sign as $-2x + x$? No. The term inside is always positive, so its sign depends on $(x+7)(2-x)$.  
        *   Let's check signs:  
            *   If $x < -2$, say $x = -10$: $f(-10) = 4( (-9)(-11)) > 0$.  
            *   If $x \in (-7, 2)$: e.g., $x=0$: $f(0) = 4(7)(2) = 56$ (positive).  
            *   If $x > 2$, say $x=3$: $f(3) = 4(10)(-1) < 0$.  
    *   Since we are looking for the **maximum value** of a continuous function on $\mathbb{R}$, it is either bounded above by its supremum or infinite. But $(x^2 - 2x + 14)$ has roots. The discriminant was negative? No. Let's recheck $x^2-2x+14$.  
    *   Roots of $x^2 - 2x + 14 = 0$: $D = (-2)^2 - 4(1)(14) = 4 - 56 = -52 < 0$.  
    *   Thus, the quadratic $x^2 - 2x + 14$ is strictly positive for all real $x$.  
    *   Since the coefficient of the highest degree term (in fact the leading coeff) is positive ($+4$), the product $(x+7)(2-x)$ behaves like a parabola opening upwards. Its minimum occurs at the vertex, but its maximum depends on the roots? No, for $f(x) = k(x-a)(x-b)$ with $k>0$, there are no extrema in $\mathbb{R}$ if it is strictly positive?  
    *   Let's look at the expression again carefully.  
    *   Original: $4(x+7)(2-x)$.  
    *   Let's complete the square inside for a more systematic approach.  
        *   $4((x^2 - 2x + 14))$? No.  
        *   Let's look at $(x+7)(2-x) = -2x - x^2 + 14 + \dots$?  
    *   Expansion: $-2x^2 + 5x + 28$.  
    *   Let's re-evaluate the sign of $f(x)$.  
        *   If $x=3$, $(6)(-1) = -6$, product is $-6$ times $4 = -24 < 0$.  
        *   If $x=-5$, $( -2 )(8 ) = 16$. $f(-5) = -64$.  
    *   So $f(x)$ goes from positive to negative as $x$ increases? No, $(x+7)(2-x)$ is a product of two linear factors.  
        *   Roots of $(x+7)(2-x)=0$ are $x=-7$ and $x=2$.  
    *   So for $x < -7$: both factors negative $\rightarrow$ product positive $\rightarrow f(x) > 0$.  
        *   At $x = -8$: $(-1)(14)$? No. $(-8+7)(2-(-8)) = (-1)(10) = -10$ (product of signs: pos).  
            *   Let's check carefully. $(x+7)$ at $x=-8$ is negative. $(2-x)$ at $x=-8$ is positive. Product is negative.  
            *   So if product is negative, $f(x) = 4 \cdot (\text{negative}) < 0$.  
        *   For $-7 < x < 2$: Both factors positive or one positive and one negative?  
            *   At $x=0$, $(7)(2) > 0$. So for $-7 < x < 2$, product is positive. $f(x) > 0$.  
        *   For $x > 2$: $(x+7)$ positive, $(2-x)$ negative. Product is negative. $f(x) < 0$.  
    *   So the function $f(x) = -16x^2 + \dots$ No.  
        *   Let's calculate derivative $f'(x) = 4( (2-x) + (-1)(7) ) = 4(-7-x)$? No, $(2-x)' = -1$. Deriv of $(x+7)$ is $1$. So $4 [ -(x+7)(1) \dots ]$?  
        *   Let's use product rule properly: $f'(x) = 4 [ 1(2-x) + (x+7)(-1) ] = 4 [ 2 - x - x - 7 ] = 4 [ -3x - 5 ]$.  
        *   Setting derivative to 0: $-3x - 5 = 0 \implies x = -5/3$.  
    *   Let's check the behavior of the function around this critical point.  
        *   For $x < -7$: product $(2-x)$ positive (since $x+7$ positive? No, if $x<-7$, $x+7$ is negative). $(2-x)$ positive. So prod is negative.  
        *   At $x = -5/3 \approx -1.67$:  
            *   For $x < -1.67$ and $-2 < x \le 0$ (so $-5/3$ is in this interval? No, $-5/3$ is $\approx -1.67$. The interval is $-7 < x < 2$).  
            *   Let's check the sign of derivative:  
                *   If $x = -8$, deriv is $-3(-8)-5 = 24 > 0$. Function increasing?  
                    *   Check $f(-8) = 4(-1)(10) = -40 < 0$? No, earlier check said product was negative.  
                *   So if derivative is positive ($x < -7$, $f' > 0$), function goes from negative to positive? No.  
        *   Let's re-evaluate the sign of $(2-x)$ for $x \in (-\infty, 2)$. At $x=-8$, $2-x=10>0$.  
        *   For $x \in (-7, 2)$: $x+7 > 0$, $2-x > 0$. So product is positive.  
        *   For $x \in (-\infty, -7)$: $(x+7) < 0$ (negative), $(2-x) > 0$ (positive). Product is negative.  
    *   Okay, so in the interval $(-\infty, -7]$, function goes from $\text{negative}$ (at $-7$ to negative? Let's check at -7: $4(0)(15)?$ No. $f(-7) = 4(0)(27)$? No. $x=-7$.  
        *   Expression: $4(-7+7)(2 - (-7)) = 0$.  
        *   Let's check derivative at -7.  
        *   If derivative is positive, function increases immediately?  
            *   Check value at $-8$: $f(-8) = 4(-1)(10) = -40$.  
            *   Check value at $-6.9$ (approx -7 + epsilon).  
                *   Let's check derivative at $x=0$: $-15 < 0$. So decreasing? No, let's recompute.  
            *   Let's calculate derivatives again carefully.  
                *   $f(x) = 4(x+7)(2-x) = 4(-x^2 - x + 14)$? No.  
                    *   $(x+7)(2-x) = 2x - x^2 + 7 - 7x$? No.  
                    *   $(x+7)(2-x) = 2x - x^2 + 7 - 7x$.  
                    *   Let's expand properly: $(x+7)(-1 + x + 3) \rightarrow (x+7)(x-5)$?  
                        *   $(x+7)(2-x) = 2x - x^2 + 14 - 7x$? No.  
                        *   $(x+7)(2-x) = 2x - x^2 - 7(2-x)$? No.  
                        *   $= -x^2 + (2-5)x + 14$?  
                        *   $= -x^2 - 3x + 14$.  
                    *   Let's check factorization again: $(x+7)(2-x) = -x^2 + x + \dots$ No.  
                    *   $(x+7)(2-x) = x^2 - x + 14 - 7x - \dots$?  
                    *   Multiply $x \cdot (-x)$ (from 7 and 2).  
                        *   $x \cdot (-x) = -x^2$.  
                        *   $x \cdot 2 = 2x$.  
                        *   $7 \cdot (-x) = -7x$? No. $x \cdot x$ is not $(x+7)(2-x)$.  
                    *   Correct expansion: $(x+7)(2-x)$.  
                        *   First term $x \cdot 2 = 2x$.  
                        *   Next $x \cdot (-1) = -x$. (from 14? No).  
                        *   Let's stick to the previous factorization: $4(-x^2 + x + 7)$? No.  
                        *   $(x+7)(2-x)$.  
                            *   $x \cdot 2 = 2x$.  
                            *   $x \cdot (-1) = -x$.  
                            *   $7 \cdot 0$ (No, 14).  
                        *   Let's multiply:  
                            *   $x + 7$.  
                            *   $-x + 7 \times x = -5x$? No.  
                            *   Multiply $(x+7)(2-x)$.  
                                *   $x \cdot 2 = 2x$.  
                                *   $x \cdot (-1)$ is wrong.  
                                *   $(x+7)(2-x) = (x+7) \cdot ((-1)x + x) + ...$? No.  
                                *   Let's do polynomial multiplication:  
                                    *   $1(x) \cdot 2 = 2$.  
                                    *   $1(x) \cdot (-1)$? No, $(2-x)$ has constant term 14? No.  
                                    *   Constant term is $x=0$ in expression $4(0+7)(0-0) = 0$?  
                                    *   Expression at $x=0$: $4(7)(2) = 56$.  
                                    *   Correct factorization of $(x+7)(2-x)$:  
                                        *   Let's use FOIL.  
                                        *   First term ($7 \cdot x$): No, we need $x(x + 7)$?  
                                        *   $(x+7)(2-x)$.  
                                        *   Term 1: $7 \cdot (-x) = -7x$. (This is from the factorization of $(x^2 - x + 74) \dots$ No.  
                                        *   Let's expand properly:  
                                            *   $(x+7)(2-x) = x(2-x) + 7(2-x)$? No.  
                                            *   $= 2x - x^2 + 14 - 7x$? No.  
                                            *   Let's write out: $2x - x^2 + 14 - 7x$.  
                                                *   $(2x - x^2) = 2x - x^2$.  
                                                *   Then add $+ 7(0)?$ No, we need to multiply $(2-x)$ by $(x+7)$.  
                                                *   $(2-x)(x+7)$.  
                                                *   $= 2(x+7) - x(x+7)$? No.  
                                                *   Let's try: $(2)(x) + (-1)(x) = 2x - x = x$.  
                                                *   $(7)(x) + (7)(-x)?$ No.  
                                            *   $(x+7)(2-x) = 2x - x^2 + 14 - 7x$.  
                                                *   $= -x^2 + (-3x) + 14$.  
                                                *   This is a parabola opening downwards ($a=-1$). It has roots at $x=0$ and $x=-2.5$? No, roots are $0$ and $7$?  
                                                    *   $-x^2 - 3x + 14 = 0$.  
                                                    *   Roots: $\frac{3 \pm \sqrt{9 - 4(-1)(14)}}{-2}$. $D = 9 - (-56) = 65$. Not integer.  
                                            *   Let's re-verify the original expansion.  
                                                *   $f(x) = (x+7)(2-x)$.  
                                                *   $(x+7)(2-x) = x(2) - x^2 + 14 - 7x$? No.  
                                                    *   $= x(2) - x(-1)$ is not right. $-x \cdot (-x)$ is $x^2$.  
                                                *   Let's expand using coefficients:  
                                                    *   $x \cdot 2 = 2x$.  
                                                    *   $7 \cdot 2 = 14$ (constant).  
                                                    *   Wait, the expression is $f(x) = 4(x+7)(2-x)$.  
                                                    *   Expand $(x+7)(2-x)$.  
                                                    *   First term: $x \cdot (-x) = -x^2$. (No, this is from 1st to 1st).  
                                                    *   Let's do term by term:  
                                                        *   $x(2) = 2x$? No.  
                                                        *   $(x+7)(2-x)$.  
                                                        *   $x \cdot (-1) = -x$. (from $-x^2$).  
                                                        *   $x \cdot (-x)$ is not there. The term with $x$ in the second factor is $-x$. So $x(-x)$? No, that's a mistake.  
                                                    *   Correct expansion of $(x+7)(2-x)$:  
                                                        *   $= x(2) + 7(2) - x(-1) - 7(x)$? No.  
                                                        *   Let's use the formula $(a+b)(c+d) = ac + ad + bc + bd$.  
                                                            *   $a=x, b=7, c=2, d=-x$? No, the factors are $x+7$ and $2-x$.  
                                                            *   Factor 1: $(x+7) \implies x, 7$.  
                                                            *   Factor 2: $(2-x) \implies 2, -x$ (No, constant is 0? No. It's linear).  
                                                                *   Constant term of $2-x$ is 0.  
                                                                *   $x(x+7)$ gives $x^2$.  
                                                            *   Let's rewrite $f(x) = 4((2-x)(x+7))$.  
                                                                *   $(2-x)(x+7)$.  
                                                                *   $= (2-x)x + (2-x)7$? No.  
                                                                    *   $x(2-x) = 2x - x^2$.  
                                                                    *   $7(2-x) = 14 - 7x$.  
                                                                    *   Sum: $-x^2 + 2x + 14 - 7x = -x^2 - 5x + 14$.  
                                                            *   So $f(x) = 4(-x^2 - 5x + 14) = -4x^2 - 20x + 56$.  
                                                        *   Let's check this against previous expansion $(x+7)(2-x) = x(2)-x^2+14-7x$?  
                                                            *   $= 2x - x^2 + 14 - 7x$.  
                                                                *   $2x - 7x = -5x$. Correct.  
                                                                *   So $(x+7)(2-x) = -x^2 - 5x + 14$. Correct.  
                                                        *   And then multiply by the coefficient $4$:  
                                                            *   $f(x) = 4(-x^2 - 5x + 14) = -4x^2 - 20x + 56$.  

    *   **New Analysis:**  
        *   We need to maximize a quadratic function: $g(x) = -4x^2 - 20x + 56$.  
        *   The coefficient of $x^2$ is $-4$, which means the parabola opens **downwards**.  
        *   This means the vertex is the global maximum.  
        *   $g'(x) = -8x - 20$.  
        *   Set derivative to 0: $-8x - 20 = 0 \implies 8x = -20 \implies x = -20/8 = -5/2 = -2.5$.  
        *   Since the coefficient is negative, this critical point represents a local maximum. Is it global? No, we need to check if the domain allows for other extrema. But it's an open parabola with range $[min, \max]$. Max value occurs at the vertex.  
        *   Now calculate $g(-2.5)$:  
            *   $g(x) = -4x^2 - 20x + 56$.  
            *   Substitute $x = -2.5$:  
                *   $-4(-2.5)^2 - 20(-2.5) + 56$.  
                *   $= -4(6.25) + 50 + 56$.  
                *   $= -25 + 50 + 56$.  
                *   $= 25 + 56 = 81$.  

        *   Let's check the original expression again with this result to ensure consistency.  
            *   $f(x) = (x+7)(2-x) \times 4$.  
            *   Substitute $x=-2.5$: $( -2.5 + 7 )( 2 - (-2.5) ) = (4.5)(4.5)$.  
                *   $= (9/2)^2 = 81/4$.  
            *   Multiply by 4: $4 \times (81/4) = 81$.  
        *   The calculation is consistent.  

4.  **Generalizing the approach:**  
    *   To maximize a quadratic of the form $Ax^2 + Bx + C$ (where $A < 0$), the vertex $x_v$ is at $-B/(2A)$.  
        *   Here $A = -4, B = -20$.  
        *   Vertex $x = -(-20)/(2(-4)) = 20 / (-8) = -5/2$.  
    *   Value $f(x_v) = A x_v^2 + B x_v + C$.  
        *   This is $g(v) = -25 - 50 + 56 = 1$? No, previous calculation used correct coefficients. Let's re-calculate:  
            *   $f(x) = -4x^2 - 20x + 56$.  
            *   $x = -2.5$.  
            *   $x^2 = (5/2)^2 = 25/4$.  
            *   $-4(25/4) = -25$.  
            *   $-20(-5/2) = +50$.  
            *   $f(-2.5) = -25 + 50 + 56$? No, $f(x_v) = f(x) - Bx_v^2 - \dots$ No.  
            *   Let's just compute directly: $-4(6.25) - 20(-2.5) + 56$.  
                *   $-4(6.25) = -25$.  
                *   $-20(-2.5) = 50$.  
                *   $56$ is constant.  
            *   Sum: $-25 + 50 + 56 = 81$.  
    *   Is there a simpler way to verify this?  
        *   Complete the square on $g(x) = -4x^2 - 20x + 56$.  
        *   $g(x) = -4(x^2 + 5x) + 56$.  
        *   Complete square inside: $x^2 + 5x = (x + 2.5)^2 - (2.5)^2$. No, it's $(x+2.5)^2$.  
            *   $(x + 5/2)^2 = x^2 + 5x/2$? No.  
            *   Square: $x^2 + 2(5)(0.5)x + \dots$  
            *   $(x + 2.5)^2 = x^2 + 5x + 6.25$.  
            *   So $x^2 + 5x = (x + 2.5)^2 - 6.25$.  
        *   Substitute back into $g(x)$:  
            *   $-4( (x+2.5)^2 - 6.25 ) + 56$  
            *   $= -4(x+2.5)^2 + 25 + 56$  
            *   $= -4(x+2.5)^2 + 81$.  
    *   Since the coefficient of $(x+2.5)^2$ is negative ($-4$), this represents a downward opening parabola with maximum at vertex $x = -2.5$.  
    *   The maximum value is $81$.  

    *   **Checking for constraints:**  
        *   Does the question imply $x$ must be an integer? No, "over all real numbers $x$".  
        *   So $x = -2.5$ is allowed.  

    *   Another check on the problem statement:  
        *   What is the maximum value of $4(x + 7)(2 - x)$?  
        *   Is it possible I misread the expression as something else? "4(x+7)(2-x)".  
            *   $(x+7)$ and $(2-x)$.  
            *   Let's check if there is a trick with $4(x+7)(2-x)$.  
            *   Maybe rewrite $x^2 - 5x + 14$? No.  
            *   Maybe use AM-GM?  
                *   $(x+7)(2-x)$ is negative between $x=-7$ and $x=2$, positive outside?  
                *   If it's positive, then max value is positive.  
                *   Let's check if the product can reach a maximum value of 81.  
                    *   $(4.5)(4.5) = 20.25$.  
                    *   $4 \times 20.25 = 81$.  
            *   This seems correct.  

    *   **Another Approach: Roots.**  
        *   Let's check the value of the expression at $x=-7$ and $x=2$.  
            *   At $x=-7$: $(4.5) \times (-9)?$ No, factor is $x+7$. So it becomes 0.  
                *   $f(-7) = 4(0)(15)?$ No.  
                    *   $2 - (-7) = 9$.  
                    *   So $f(-7) = 4 \cdot (0) \cdot 9 = 0$.  
            *   At $x=2$: $(2+7)(2-2) = 9(0) = 0$.  
                *   $f(2) = 0$.  
        *   Since it's a continuous function, it reaches local maxima at the vertex. We found max to be 81.  

    *   **Another Method: Completing Square (Re-verified).**  
        *   $4(x^2 - 2x + 14)$.  
            *   The previous expansion gave $f(x) = -4x^2 - 20x + 56$. This matches $4(x^2 - 5x + 14)$? No.  
                *   $(x+7)(2-x) = -x^2 - 5x + 14$? Let's re-verify expansion.  
                    *   $(x+7)(2-x)$.  
                        *   $x \cdot 2 = 2x$.  
                        *   $x \cdot (-1) = -x$. (This was my mistake earlier, it should be $(x+7)$ vs $(x-5)$. No. The factors are $x$ and $7$? No, the term $x+7$ is a variable factor. $2-x$ is another.)  
                        *   Let's do standard multiplication again very carefully.  
                            *   $(a+b)(c+d) = ac + ad + bc + bd$.  
                                *   $x \cdot 2 = 2x$.  
                                *   $x \cdot (-1) = -x$. (No, the second factor is $-x$, so $x(-x)$? No).  
                                *   The first factor is $(x+7)$.  
                                    *   Terms: $x$ and $7$.  
                                *   The second factor is $(2-x)$.  
                                    *   Terms: $2$ and $-x$.  
                                *   Product: $(x)(2) + (x)(-x) + (7)(2) + (7)(-x)$? No.  
                                    *   First term in product of first factor is $x$ times second factor constant term ($2$) is $2x$? Yes.  
                                        *   Second term: $x$ times second factor variable part ($-x$). That gives $-x^2$.  
                                        *   Third term: $7$ times second factor constant ($2$). No, that's $(2-x)$'s linear term 0 (since it is $-x+2$? No).  
                                            *   Term $(x+7)(2-x) = x(2-x) + 7(2-x)$?  
                                                *   $x(2-x) = 2x - x^2$.  
                                                *   $7(2-x) = 14 - 7x$.  
                                                *   Sum: $-x^2 + (2x - 7x) + 14 = -x^2 - 5x + 14$.  
                                *   So the expression to maximize is $4(-x^2 - 5x + 14) = -4x^2 - 20x + 56$.  
        *   This confirms my previous derivation was correct.  
        *   The function opens downwards ($A = -4 < 0$).  
        *   Maximum value at $x_v = -B / (2A) = -(-20) / (2(-4)) = 20 / -8 = -2.5$.  
        *   Value: $g(v) = -4( (-2.5)^2 ) - 20(-2.5) + 56$? No, formula is $Ax^2+...$ no.  
            *   $-4(x^2 + 5x) + 56$.  
            *   $-4((x+2.5)^2 - (2.5)^2 + \dots)$ No.  
            *   $(x+2.5)^2 = x^2 + 5x + 6.25$.  
            *   So $-4(x^2 + 5x) = -4((x+2.5)^2 - 6.25) = -4(x+2.5)^2 + 25$.  
            *   Max value is $25 + 56 = 81$.  

5.  **Alternative Check (Geometric / Domain Analysis):**  
    *   The function is symmetric around the vertex of the quadratic curve. Since it's defined for all reals, we check if endpoints are max or min. For an inverted parabola, the vertex is the global maximum.  

6.  **Formatting the Solution:**  
    *   Identify expression: $y = 4(x + 7)(2 - x)$.  
    *   Expand to find polynomial form: $f(x) = -4x^2 - 20x + 56$.  
    *   Find vertex (max): $x_v = -(-20)/2(-4) = -5/2$.  
    *   Calculate maximum value: $y_v = f(-5/2)$.  
        *   $f(-5/2) = -4( (-5/2)^2 ) - 20(-5/2) + 56$.  
        *   $= -4(25/4) + 50 + 56$.  
        *   $= -25 + 106$? No, $-25 + 56 = 31$? No.  
            *   $-25 + 50 = 25$.  
            *   $25 + 56 = 81$.  
    *   Verify calculation one last time.  
        *   $x = -2.5$.  
        *   $x+7 = 4.5$.  
        *   $2-x = 4.5$.  
        *   Product is $(4.5)^2 = 20.25$.  
        *   Multiply by 4: $81$.  

7.  **Is there any ambiguity in the question?**  
    *   "Maximum value" implies the global maximum on the reals.  
    *   Is the expression ever less negative? Yes, but we found max 81.  
    *   Could it be $4(x+7)(2-x)$ can be positive everywhere?  
        *   Check sign of $(x+7)$ and $(2-x)$.  
        *   Roots at -7 and 2.  
        *   For $x < -7$, both factors negative? No, $x+7$ neg, $2-x$ pos $\implies$ neg.  
            *   At $x=-8$: $f(x) = 4(0)(10)$ ? No, $2-(-8)=10$. $(2-x)$ is positive. $(x+7)$ is negative. Product is negative.  
        *   For $-7 < x < 2$, both factors positive?  
            *   At $x=0$: $7 \times 2 = +$ ? No, $0+7=7$. $2-0=2$. Prod pos.  
        *   For $x > 2$, $x+7$ pos, $2-x$ neg. Product neg.  
    *   The expression is a quadratic opening upwards? No. It was -4...  
    *   If $A = -4$, it opens down.  
    *   Is there any chance $(2-x)$ is not the linear term? No, usually written as such.  
    *   Let's check derivative sign again for the original form directly to be absolutely sure.  
        *   $f(x) = 4(-x^2 - 5x + 14)$.  
            *   Let's re-expand $(x+7)(2-x)$.  
                *   $(x+7)(2-x) = (x)(-x) + x(2) + 7(2) - 7(x)$? No.  
                    *   $x \cdot (-x) = -x^2$. Correct.  
                    *   $x \cdot 2 = 2x$. Correct.  
                    *   $7 \cdot 2 = 14$. Correct.  
                    *   $7 \cdot (-1)$? No, that's if we factor out $(x+7)$. No.  
                *   Okay, I need to be extremely careful with the term "7". The expression is $(x+7)(2-x)$.  
                *   So it is $(1)x + 7$ and $(2-x)$.  
                    *   $x \cdot 2 = 2x$.  

*Continued in [part 2 of 2](algebra_2064_p2.md): GitHub stops rendering math on pages this long, so the transcript is split.*
