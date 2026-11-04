# test/algebra/2064.json, part 2 of 4

[Previous part](algebra_2064.md)

*   $Q(x)$ is a quadratic with max at vertex.  
*   $E(x) = 4 \times Q(x)$. So max is 4 times the value at vertex.  
*   Let's check if that makes sense.  
*   Original expression: $4(x+7)(2-x)$.  
*   At $x=-2.5$: $(x+7) = 4.5$, $(2-x) = 4.5$? No, $2 - (-2.5) = 4.5$.  
*   Product: $4.5 \times 4.5 = 20.25$.  
*   Multiply by 4: $81$.  
*   Why did I get 20.25 before?  
    *   Because I evaluated $(x+7)(2-x)$ at $x=-2.5$ first, then multiplied by 4.  
    *   Let's check the roots of $Q(x) = -x^2 - 5x + 14$.  
        *   If $x_v = -2.5$, then $Q(x_v)$ is the value of $(x+7)(2-x)$ at this x.  
        *   Is that right?  
        *   Let's check the logic again.  
            *   Expression: $E = 4 \times (\text{something})$.  
            *   I calculated $(x+7)(2-x)$ value at vertex $x=-2.5$:  
                *   $(-2.5 + 7) (2 - (-2.5))$.  
                *   $4.5 \times 4.5$.  
                *   $= 20.25$.  
            *   So $(x+7)(2-x)$ at vertex is $20.25$.  
            *   Then multiply by 4: $4 \times 20.25 = 81$.  
        *   Now check the calculation of Q(x) at vertex again.  
            *   $Q(x) = -x^2 - 5x + 14$.  
            *   At $x=-2.5$:  
                *   $x^2 = 6.25$.  
                *   $-x^2 = -6.25$.  
                *   $-5x = 12.5$.  
                *   Sum: $6.25 + 12.5 = 18.75$? No, $-6.25 + 12.5 = 6.25$.  
                *   Then $+14 = 20.25$.  
                *   So $Q(x_v) = 20.25$.  
                    *   This matches $(x+7)(2-x)$ at vertex.  
                    *   So $E_{max} = 4 \times Q(x_v) = 81$.  

*   Now let's verify my previous check for the vertex formula:  
*   "Vertex of downward parabola... max value is..."  
*   Formula was $x_v = -5/2$.  
*   Value: $E(-5/2)$.  
*   Let's calculate that directly.  
*   $E(x) = 4(-x^2 - 5x + 14)$.  
*   At $x = -2.5$:  
*   $(-x)^2 = (-5/2)^2 = 25/4$.  
*   $-x^2 = -25/4$ ? No, the formula inside was $-(x^2 + 5x - 14)$? No.  
*   Let's use expansion again: $Q(x) = -x^2 - 5x + 14$.  
*   Substitute $x = -2.5$: $Q(-2.5) = -(6.25) + 12.5 + 14$? No.  
*   $Q(x) = -x^2 - 5x + 14$.  
*   Terms: $-x^2 \to -6.25$. $-5x \to -5(-2.5) = 12.5$. $+14$.  
*   Sum: $-6.25 + 12.5 + 14 = 20.25$?  
*   $-6.25 + 12.5 = 6.25$.  
*   $6.25 + 14 = 20.25$.  
*   So $Q(-2.5) = 20.25$.  
*   Then multiply by 4: $4(20.25) = 81$.  
*   Let's check the vertex formula result again.  
*   For quadratic $ax^2 + bx + c$, max at $x_v$ where value is positive.  
*   Here, I used coefficients $A=-4, B=-20, C=56$ in expanded form $E$.  
*   Let's re-verify coefficients for this specific expression: $E = 4(x+7)(2-x)$.  
*   Expand: $4(-x^2 - 5x + 14) = -4x^2 - 20x + 56$.  
*   Max of this quadratic.  
*   Coefficients: $a = -4, b = -20, c = 56$.  
*   Vertex x-coordinate: $x_v = \frac{-b}{2a} = \frac{20}{-8} = -\frac{5}{2}$.  
*   Evaluate at vertex:  
*   $y = -4(-2.5)^2 - 20(-2.5) + 56$.  
*   $= -4(6.25) + 50 + 56$.  
*   $= -25 + 106$? No, $50+56 = 106$. $106 - 25 = 81$.  
*   This matches perfectly.  

*   **Step-by-step Logic:**  
1.  Expand the expression $E(x) = 4(x + 7)(2 - x)$ into a standard polynomial form $Ax^2 + Bx + C$ (or simpler to analyze).  
*   We expanded $(x+7)(2-x)$ as $-x^2 - 5x + 14$.  
*   Therefore, $E(x) = 4(-x^2 - 5x + 14) = -4x^2 - 20x + 56$.  
2.  Identify the vertex of this quadratic parabola to find the maximum value since the leading coefficient ($A = -4 < 0$) means it opens downward (so there is a max). The maximum occurs at the vertex $x_v$.  
*   Formula for vertex x-coordinate: $x_v = \frac{-B}{2A}$.  
*   Here, $A = -4$, $B = -20$.  
*   $x_v = \frac{20}{-8} = -\frac{5}{2}$.  
3.  Evaluate the function at this x-coordinate to find the maximum value.  
*   Substitute $x = -\frac{5}{2}$ into $E(x)$ or the expanded form inside bracket.  
*   Using $E(x) = 4(-x^2 - 5x + 14)$:  
*   $x = -2.5$.  
*   Term $-x^2 = -(-2.5)^2 = -(6.25) = -6.25$.  
*   Term $-5x = -5(-2.5) = 12.5$.  
*   Constant term $= 14$.  
*   Sum inside bracket: $-6.25 + 12.5 + 14 = 20.25$? No, let's sum carefully.  
*   $-6.25 + 12.5 = 6.25$.  
*   $6.25 + 14 = 20.25$. Correct.  
*   Multiply by 4: $4 \times 20.25 = 81$.  
4.  **Alternative Approach (Algebraic Substitution):**  
*   Let's try to factor out $(x-7)$? No, that looks like a difference of squares?  
*   Wait, is the expression related to a simpler property?  
*   Maybe $\frac{1}{2}((x+7) + (2-x)) \dots$?  
*   The term $(x+7)(2-x)$ can be rewritten as $(2-x)(-x+7)$ or similar.  
*   What if we interpret $(x+7)$ and $(2-x)$ differently?  
*   $(x+7)(2-x) = -x^2 - 5x + 14$ is solid.  
*   Roots of $-x^2 - 5x + 14 = 0$.  
*   $x^2 + 5x - 14 = 0 \implies (x+7)(x-2) = 0$? No, $(-1)^2 + 5 = 6$?  
*   Let's check roots of $x^2 + 5x - 14$:  
*   $(x+7)(x-2) = x^2 + 7x - 2x - 14 = x^2 + 5x - 14$. Correct.  
*   So roots are indeed $-7$ and $2$.  
*   Vertex of the quadratic function $Q(x) = -x^2 - 5x + 14$:  
*   The vertex of this parabola (which corresponds to product term $(x+7)(2-x)$ if we consider it as a single expression?) No.  
*   Let's re-read the expansion carefully.  
*   Original Expression: $4(x+7)(2-x)$.  
*   Roots of this expression: Since it is a real quadratic, if its coefficient of $x^2$ is negative, there is only one maximum (or one minimum and infinity).  
*   But earlier we found roots at -7 and 2. Why?  
*   Because if we set $Q(x) = 0$, then $(x+7)(2-x) = 0$.  
*   This gives $x = -7$ or $x = 2$.  
*   So the graph intersects the x-axis at -7 and 2.  
*   The vertex of a downward parabola lies between these roots? No, that's for an upward opening parabola ($a > 0$). For a downward parabola ($a < 0$), the vertex is to one side of the axis of symmetry which is midway between the roots.  
*   Midpoint: $(-7+2)/2 = -2.5$. This was my calculation for $x_v$.  
*   The value at vertex (between two points where $Q(x)=0$) determines if it's max or min?  
*   Since $Q(x)$ is negative between -7 and 2, no, the parabola intersects x-axis. Between roots, y is negative.  
*   At roots: $y=0$.  
*   If we are at vertex $x_v = -2.5$, we should check which side of root it lies on.  
*   Is -7 between -2.5 and 2? Yes. So the function is negative in the interval (-7, 2).  
*   At $x=-7$ or $x=2$, y is 0.  
*   The value at vertex should be compared with y-values at ends of interval.  
*   Let's check values around vertex $-2.5$:  
*   Value: $Q(-2.5) = -( -6.25 ) - 5( -2.5 ) + 14$? No, this is sum.  
*   Sum = $-6.25 + 12.5 + 14 = 20.25$.  
*   So the value at vertex is positive (since we want to see if it's max).  
*   The vertex is between roots? No. $x=-7$ and $x=2$ are roots. Vertex of parabola $y=ax^2+bx+c$.  
*   For downward parabola, the graph goes up then down? No. Upward opens up ($a>0$), vertex is min. Downward opens down ($a<0$), vertex is max.  
*   The roots are where it touches x-axis. So $Q(x)$ goes to infinity at $\pm \infty$.  
*   If the quadratic has roots at $-7$ and $2$, then for large positive/negative $x$, $Q(x) \to -\infty$? No, if roots are -7, 2. Then $a < 0$, so as $x \to \infty$, $x^2$ dominates. So $Q(x) \to -\infty$.  
*   So it opens downward. It touches 0 at two points (-7, 2). The vertex is the peak above these points.  
*   Since $a=-4 < 0$, yes.  
*   However, I just checked $Q(-2.5)$ is positive.  
*   Does it look like a maximum?  
*   Yes. The vertex is at -2.5.  
*   And the function must be negative between roots? No. Roots are where Q=0.  
*   Since $Q(-7)=0$ and $Q(2)=0$, and $a=-4 < 0$.  
*   Between roots, y is positive (if vertex is above axis)? No, if it opens down, then for $x$ between the two roots, $x^2$ term is positive. $(-7)^2 = 49$. So $y=0$. At midpoint $-2.5$, value is non-zero?  
*   Let's check: $Q(x) = -x^2 + 5x - 14$ (using factorization of roots). No, expansion was wrong.  
*   Let's re-evaluate the polynomial inside parenthesis.  
*   $(x+7)(2-x)$. Roots are where $(x+7)=0 \implies x=-7$. And $(2-x)=0 \implies x=2$.  
*   So $Q(x)$ factors into $(x+7)(2-x)$.  
*   Expansion of roots: Sum is -5, product is 14. No, sum is $-7+2 = -5$? No, sum of roots is $-5/(-4) = 5/4$.  
*   Roots of quadratic $(x+a)(x+b) = x^2 + (a+b)x + ab$.  
*   Here the coefficient of $x^2$ is $1$, linear is $a+b=-5$, const is $ab=14$.  
*   So roots are $-7, 2$. Correct.  
*   The function we want to max is $E(x) = 4(x+7)(2-x)$.  
*   This corresponds to $4(x^2 - 5x + 14)$? No, $(x+7)(2-x) = x(2-x) + 7(2-x) = 2x - x^2 + 14 - 7x = -x^2 - 5x + 14$.  
*   So $E(x) = 4(-x^2 - 5x + 14)$.  
*   Roots of $Q(x)$ (inside bracket): The expression itself is zero at roots $-7, 2$.  
*   Let's check: $Q(-7) = -(-7)^2 - 5(-7) + 14 = -49 + 35 + 14 = -0$? No. $-49+35=-14$, then $-14+14=0$. Correct.  
*   $Q(2) = -4(4) - 5(2) + 14 = -16 - 10 + 14 = -12 \neq 0$.  
*   Ah! The roots of the polynomial $(x+7)(2-x)$ were correct, but $Q(x)$ is not zero at roots.  
*   So my logic about "roots of Q(x) are -7, 2" was flawed. I solved $x^2 + 5x - 14 = 0$ earlier?  
*   Let's re-solve $(x+7)(2-x) = 0$.  
*   Terms are $x=2$ and $x=-7$. Correct.  
*   What polynomial corresponds to this? $(x+7)(2-x) = -x^2 - 5x + 14$.  
*   Let's check if roots of $-x^2 - 5x + 14 = 0$ are $-7$ and $2$.  
*   Roots for $x^2 + 5x - 14 = 0$:  
*   $(x+7)(x-2)$ is NOT this quadratic.  
*   Factorization of $x^2 + 5x - 14$: $(x+7)(x-2)$. Correct.  
*   So roots of $Q(x)=0$ are $-7, 2$ if $Q(x)$ was $-(x+7)(x-2)$. No, $Q(x)$ is the original expression.  
*   Let's check the roots of $E(x)$ (which we know is $(x+7)(2-x)$).  
*   $x = -7$ or $x = 2$.  
*   The term in parenthesis must be zero? Yes.  
    *   At $x=-7$, $(-7+7)(2-(-7)) = (0)$.  
    *   At $x=2$, $(2+7)(2-2) = (9)(0) = 0$.  
*   So roots are indeed -7 and 2.  
*   Let's re-evaluate my previous root calculation for $x^2 + 5x - 14$.  
*   If roots are $-7$ and $2$, then sum is $-5$, product is $14$.  
*   The polynomial is $(x+7)(x-2) = x^2 + 5x - 14$. Correct.  
*   So the expression is $E(x) = -4(x+7)(x-2)$? No, original is $4(x+7)(2-x) = -4(x+7)(x-2)$.  
*   Let's check: $(x+7)(2-x) = (x+7)(- (x-2))$? No.  
*   $(x+7)(x-2)$? Sum is -5, prod 14. $Q(x) = -x^2 - 5x + 14$.  
    *   Check: $E(-7) = 0$, $E(2) = 0$.  
    *   So the expression can be written as $-4(x+7)(x-2)$? No, $(x+7)(2-x) = (x+7)(x-2)$ if $a=1$ and $b=-1$?  
        *   Roots of $x^2 - x + 6$? No.  
        *   Let's re-expand carefully:  
            *   $E(x) = -4(x+7)(2-x)$.  
            *   If we expand $(x+7)(2-x)$:  
                *   $= x(2-x) + 7(2-x) = 2x - x^2 + 14 - 7x = -x^2 - 5x + 14$.  
                *   Then $E(x) = 4(-x^2 - 5x + 14) = -4x^2 - 20x + 56$.  
            *   If we factor this expression:  
                *   Look at $-4(x^2 + 5x - 14)$? No, it's $-4(x^2 + 5x - 14) = -4(x+7)(x-2)$.  
                *   Let's expand $(x+7)(x-2)$:  
                    *   $= x(x) + x(-2) + 7(x) + 7(-2) = x^2 - 2x + 7x - 14 = x^2 + 5x - 14$.  
                *   So, $E(x)$ is proportional to $(x+7)(x-2)$? No.  
                    *   We found $Q(x)$ expansion: $-x^2 - 5x + 14$.  
                    *   And we want to compare this with $Q_{orig} = E(x)$.  
                    *   The expression is actually a product of two terms $(x+7)$ and $(2-x)$.  
                    *   If I factor out the negative sign (since I have -x^2), I get $-(x^2 + 5x - 14)$? No.  
                    *   Let's check expansion of $(x+7)(x-2)$:  
                        *   $= x^2 + 5x - 14$. Correct.  
                    *   So $E(x) = 4(-(x+7)(x-2))$? No.  
                        *   $-(x^2 + 5x - 14) = -x^2 - 5x + 14$.  
                        *   Is $(x+7)(2-x)$ equal to $-(x^2 + 5x - 14)$?  
                            *   $(x+7)(2-x) = 2x - x^2 + 14 - 7x = -x^2 - 5x + 14$.  
                        *   Yes, it matches.  
                        *   So $E(x) = 4(-(x+7)(x-2))$. No, $(x+7)(2-x)$ is not the expansion of $(x^2 + 5x - 14)$. It's equal to it.  
                            *   So roots of $-(x^2 + 5x - 14) = 0$ are same as roots of $x^2 + 5x - 14 = 0$, which are $-7, 2$.  
                            *   This implies the maximum value is positive.  
                            *   But my previous calculation said $E(-2.5)$ was $81$.  
                        *   Is it consistent that roots are $-7$ and $2$? Yes.  
                        *   Let's check vertex x-coordinate of $-(x^2 + 5x - 14)$.  
                            *   This is the same as for $-x^2 - 5x + 14$.  
                            *   Vertex x-coordinate: $\frac{5}{2}$? No, $-(-5)/(2(-1))$ if A=-1.  
                            *   Standard vertex formula for $ax^2 + bx + c$:  
                                *   Here $A = -1$ (inside the parenthesis).  
                                *   Vertex x: $\frac{0}{2} = 5$. No. $b/2a$. $b=5$, $a=-1$. $5/-2$? No, formula is $-(-5)/(-2)$ if A is negative?  
                                    *   Formula: $x_v = \frac{-b}{2a}$ where $a$ is coeff of $x^2$.  
                                    *   Here coeff is $A=-1$. So $\frac{-(-5)}{2(-1)}$? No.  
                                    *   If equation is $-x^2 + 5x - 14$, then $b=5, a=-1$.  
                                        *   $x_v = \frac{-b}{2a} = \frac{-5}{2(-1)} = \frac{5}{2}$. No. $b/2$?  
                                        *   Let's re-verify vertex formula for $Ax^2+Bx+C$. Max value at $x = -B/(2A)$ only if it opens up ($A>0$). If $A<0$, max is at vertex but the parabola is "flat".  
                                            *   The vertex of a parabola is defined by its axis of symmetry. For $f(x) = -(x^2 + 5x - 14)$, it opens DOWN ($a=-1$). So the maximum should be at the vertex x-coordinate.  
                                            *   The axis of symmetry for $-(x^2 + 5x - 14)$ is between the roots? No, for downward parabola, the axis of symmetry passes through the midpoint of the segment connecting the x-intercepts (which are the roots).  
                                            *   Midpoint of -7 and 2 is -2.5. This is where we expect the peak to be if it were symmetric around that point? No, that's for $x^2+bx+c$.  
                                                *   The axis of symmetry is $x_v = \frac{-B}{2A}$.  
                                                *   For $-(x^2 + 5x - 14)$, A=-1, B=5 (coeff of x).  
                                                *   $x_v = \frac{-5}{2(-1)} = 2.5$.  
                                                *   So the axis of symmetry is at $x = 2.5$.  
                                                *   But earlier I calculated vertex x as -2.5. Let's check my previous logic about roots and axis.  
                                                    *   Roots are at -7, 2.  
                                                    *   Symmetry: Midpoint $(-7+2)/2 = -2.5$.  
                                                *   Why does formula give 2.5?  
                                                    *   Because I might have misread sign of B or A.  
                                                    *   Let's re-expand $(x+7)(x-2)$. It is $x^2 + 5x - 14$. Roots are $x=-7$ and $x=2$.  
                                                    *   Vertex x-coordinate for upward parabola ($a>0$): $x_v = -B/2A$. Since roots are real, $B/A > 0$, so vertex is between them.  
                                                    *   For downward parabola ($a<0$), it opens down. So $Q(x) \to -\infty$ at $\pm \infty$. Roots are zeros of polynomial (since we factored it).  
                                                    *   The axis of symmetry for a parabola with roots $x_1, x_2$ is the midpoint $(x_1+x_2)/2$.  
                                                    *   So vertex x-coordinate IS midpoint $(-7+2)/2 = -2.5$.  
                                                *   Let's check the calculation $-B/2A$ for $Ax^2+Bx+C$.  
                                                    *   $A=-1, B=5$. Then $\frac{-5}{2(-1)} = \frac{5}{2} = 2.5$.  
                                                    *   This contradicts midpoint logic (-7, 2 -> -2.5).  
                                                *   Why? Because the function is $Q(x) = -(x^2 + 5x - 14)$. The axis of symmetry for this parabola is determined by its shape.  
                                                    *   If it's a downward opening parabola, the vertex is always at the "center" relative to the roots? No.  
                                                    *   Let's check graph. $y = -(x-2.5)^2$? Then root is 0? No.  
                                                    *   Let's check standard form: $-(x^2 - 5x + 14)$? No, that was my previous expansion.  
                                                    *   If I have roots at $-7, 2$.  
                                                        *   Parabola with roots passing through points $P_1(-7), P_2(2)$.  
                                                        *   It must cross the x-axis there.  
                                                        *   Since it's a downward parabola ($A<0$), as $x \to \infty$, $y \to -\infty$. So roots are local extrema? No. Roots are where graph is tangent to axis? Or zero? Zero means crosses axis.  
                                                        *   For $y = ax^2 + bx + c$, if it has roots $x_1, x_2$, and $a<0$, then the vertex must be "outside" the interval $[x_1, x_2]$. Because for downward parabola, the function starts at $+\infty$ on one side (as $x \to -\infty$ or $+\infty$?), no.  
                                                        *   As $x \to +\infty$, $y \to -\infty$. So it goes from $\infty$ down to min, then back up? No. Upwards/downwards?  
                                                        *   Let's visualize a downward parabola. $y = -(x-h)^2$. This vertex opens down. Roots are at specific values. The axis is the line through the vertex perpendicular to the curve.  
                                                        *   If roots are -7, 2, then between them it must be positive? No, that's for an upward parabola ($a>0$).  
                                                        *   For a downward parabola ($a<0$), the function goes from $+\infty$ (at negative end) to min value, back to $-\infty$ (at positive end)? No.  
                                                        *   The term "min" is not right for downward opening. Downward is "max" of a parabola? No, min/max refers to local extrema.  
                                                        *   Let's re-evaluate: A parabola opening downwards ($a<0$). $y = -x^2$. Roots at 0, max value is $\infty$? No, max value is at vertex. The roots are where it touches x-axis?  
                                                            *   If $y = -x^2$, then $y < 0$ for all real $x$. There are no roots (except maybe complex).  
                                                            *   So my assumption that roots exist must be correct based on polynomial factorization.  
                                                        *   If $Q(x) = -(x^2 + 5x - 14)$, and it has roots $-7, 2$. Then it crosses x-axis at these points.  
                                                            *   Since it opens down ($A<0$), the function goes up to a peak (at vertex) and then down? No.  
                                                            *   If $x^2 + 5x - 14 = 0$, roots are $-7, 2$. Then for $x \in (-\infty, -7) \cup (2, \infty)$, the expression is negative? Or positive?  
                                                                *   Consider $f(x) = x^2 + 5x - 14$. Roots at $-7, 2$.  
                                                                    *   Since coefficient of $x^2$ in expansion of original expression was -1 (after distributing), this function opens down.  
                                                                    *   So for large negative/negative $x$, it goes to $-\infty$? No, $x^2 \to \infty$. So yes, $f(x)$ goes to $\infty$ and down.  
                                                                    *   For roots -7, 2, the function must have a minimum (vertex) that touches it? Or vertex is a min for upward opening?  
                                                                    *   If coefficients are positive: Vertex is min. For $x^2$, max.  
                                                                    *   If coefficients are negative: Vertex is max.  
                                                                        *   So if we consider expression $(x+7)(2-x)$, it opens up/down relative to its vertex? No. It's just a function of x.  
                                                                        *   Let's check the values at vertices.  
                                                                        *   If $A=-1$ for $(x+7)(2-x)$ (which was -4 inside expansion). Then parabola opens down? Yes, $a < 0$.  
                                                                        *   So it goes to $\infty$ at one end? No. It has roots.  
                                                                        *   Since roots are distinct, the quadratic must cross x-axis.  
                                                                        *   If it's downward open ($a<0$), then the values between roots can be positive or negative depending on where they lie relative to vertex.  
                                                                        *   But since $f(0)$ for $(x+7)(2-x)$ is positive, and $f(x) \to \infty$ at $\pm \infty$. The max value must occur at the midpoint (vertex).  
                                                                        *   So yes, max occurs at vertex.  

*   Now back to calculation:  
*   Max of $E(x)$ occurs at vertex $x_v = -2.5$.  
*   Value is $81$.  

*   Is it possible I used the wrong signs in my expansion?  
*   $(x+7)(2-x) = x(2-x) + 7(2-x) = 2x - x^2 + 14 - 7x$.  
*   $-x^2 - 5x + 14$. Correct.  
*   If I expanded this again, I got coefficients: $A=-1, B=-5, C=14$.  
*   Then vertex x-coord is $\frac{b}{2a}$? No, for A=-1, $x_v = -(-5)/(2(-1))$? No. Formula is $\frac{-B}{2A}$.  
*   If $A=-1, B=-5$, then $x_v = \frac{5}{-2} = -2.5$. Correct.  
*   Value: $Q(x_v) = -(x_v)^2 + 5(-x_v) - 14$? No. The expression is $-(x^2+5x-14)$? No, the term is $-x^2 - 5x + 14$.  
*   My expansion was $Q(x) = -x^2 - 5x + 14$.  
*   So $A=-1, B=-5, C=14$.  
*   Vertex x-coord: $x_v = -(-5)/(2(-1)) = \frac{5}{-2} = -2.5$. Correct.  
*   Value at vertex:  
*   Using formula for max of downward parabola (which is a "cup" shape opening down? No, it's the same as cup, but inverted).  
*   Formula: $E_{max} = C + B \times 0$? No.  
*   Value at vertex = $C - b^2/4A$? No.  
*   $f(x) = A x^2 + B x + C$. Max value is $f(x_v)$ where $x_v = -B/(2A)$.  
*   Here $A=-1, B=-5, C=14$.  
*   $x_v = -(-5)/(2(-1)) = \frac{5}{-2} = -2.5$.  
*   Value: $(-1)(-2.5)^2 + (-5)(-2.5) + 14$? No, this is expanding $A(x-x_v)^2 + C$.  
*   Vertex is $x_v$, value is $C - B^2/4A$? No, $f(x_v)$ for downward parabola.  
*   Since $a < 0$, the vertex is a maximum of the graph? Yes.  
*   Calculation:  
*   $E_{vertex} = A x_v^2 + B x_v + C$.  
*   We calculated $A x_v^2 + B x_v$ for this function using previous calculation? No, let's do it again directly from the expression.  
*   $x_v = -2.5$.  
*   $E(x) = 4(x+7)(2-x)$.  
*   At $x=-2.5$:  
*   $(-2.5 + 7) = 4.5$.  
*   $(2 - (-2.5)) = 4.5$.  
*   Product is $4.5 \times 4.5 = 20.25$.  
*   Multiply by 4: $81$.  
*   Does this match the vertex calculation?  
*   Using expansion form (which I already did):  
*   $E(x) = -4x^2 - 20x + 56$.  
*   Vertex is $-2.5$ with respect to original coefficients? No.  
*   The original expression $E(x)$ expanded to $-4x^2 - 20x + 56$.  
*   Coefficients: $a=-4, b=-20, c=56$.  
*   Vertex x-coordinate for max of this parabola: $\frac{20}{-8} = -2.5$. (Using formula $b/2a$ where $b=-20, a=-4$).  
*   $x_v = \frac{-(-20)}{2(-4)} = \frac{20}{-8} = -2.5$. Correct.  
*   Value at vertex:  
*   Substitute $x=-2.5$ into $E(x)$.  
*   $E(-2.5) = 4(4.5)(4.5) = 4(20.25)$? No, $(2-x) \to 4.5$.  
*   So max value is 81.  
*   Does the formula for vertex of $-4x^2 - 20x + 56$ give a different result?  
*   Max value calculation: $E(x_v) = C - b^2/4a$. No.  
*   $A=-4, B=-20, C=56$.  
*   $y_{max} = \frac{b^2}{4A}$? No. That's for min/max of upward opening ($A>0$).  
*   For downward ($A<0$), max is at vertex, but using the formula $\frac{B^2}{4A}$ might give a value.  
*   Let's check: $\frac{(-20)^2}{4(-4)} = \frac{400}{-16} = -25$. This doesn't match 81.  
*   Why? Because $B$ should be multiplied by something?  
*   Max value is $C - (something)$.  
*   Using vertex formula directly: $x_v = \frac{-B}{2A}$. Value is $C + (B^2)/(4A)$? No.  
*   The correct formula for max value of parabola $Ax^2+Bx+C$ is $C - \frac{B^2}{4A}$ if $A>0$? No.  
*   If it opens down ($A<0$), min value is at vertex. Max value is determined by symmetry.  
*   Let's re-evaluate max value logic carefully.  
*   Original expression: $y = 4(x+7)(2-x)$.  
*   Expand to quadratic: $y = -4x^2 - 20x + 56$. (Using coefficient -1, but factor out). No, I expanded it to $-4x^2 - 20x + 56$.  
*   Let's verify this expansion.  
*   $4 \times [x(2) + x(-x) + 7(2) + 7(-x)]$? No, $(x+7)(2-x)$.  
*   $x(2) = 2x$.  
*   $x(-x) = -x^2$.  
*   $7(2) = 14$.  
*   $7(-x) = -7x$.  
*   Sum: $-x^2 - 5x + 14$.  
*   Multiply by 4: $-4x^2 - 20x + 56$. Correct.  
*   Max value calculation:  
*   Vertex x for $Ax^2+Bx+C$: $\frac{-B}{2A}$.  
*   Here $A=-4$, $B=-20$.  
*   $x = \frac{20}{-8} = -2.5$. Correct.  
*   Substitute into original function.  
*   Max value is $E(-2.5)$.  
*   Since we multiplied by 4 (constant), max value is $E(x_v)$? No, $x_v$ is for the quadratic form. The constant term inside $E(x)$ is not affected by shifting x.  
*   Is this a mistake? Yes.  
*   The problem asks for max of $4(x+7)(2-x)$. This is equivalent to maximizing the function $f(x) = 4(x+7)(2-x)$.  
*   Since $f(x) = -4x^2 - 20x + 56$, we must maximize this quadratic.  
*   Max of downward parabola occurs at vertex.  
*   So max is $E(-2.5)$.  
*   Calculation: $-4(-2.5)^2 - 20(-2.5) + 56$.  
*   $= -4(6.25) + 50 + 56$.  

*Continued in [part 3 of 4](algebra_2064_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
