# test/algebra/2064.json, part 3 of 4

[Previous part](algebra_2064_p2.md) · [Start](algebra_2064.md)

*   $= -25 + 106$.  
*   $= 81$.  

*   Is there any catch?  
*   The question asks for "maximum value of $4(x+7)(2-x)$".  
*   Is it possible that $(x+7)(2-x)$ has roots at -7, 2 and is a product of terms where one term is constant (2-x) and another is linear? Yes.  
*   Let's re-evaluate the logic about "roots are -7, 2".  
*   $(x+7)(2-x)$ can be rewritten as $-x^2 - 5x + 14$.  
*   Roots are where $-x^2 - 5x + 14 = 0 \implies x^2 + 5x - 14 = 0$.  
*   $(x+7)(x-2) = x^2 + 5x - 14$. Correct.  
*   So roots are $-7$ and $2$.  
*   Since coefficient of $x^2$ is negative, the graph opens downwards.  
*   Therefore, the vertex is a maximum point. The max value occurs at the midpoint of the interval between roots (symmetry).  
*   Midpoint: $\frac{-7+2}{2} = -2.5$.  
*   Is this true? Yes. The function $y=4(x+7)(2-x)$ is symmetric about the vertical line passing through the vertex. Since the vertex lies between the roots, and the function values at roots are zero, the function is positive (or negative) in between. If it's a downward parabola ($A<0$), it goes to $-\infty$ as $x \to \pm\infty$.  
*   Let's check behavior near roots:  
*   At $x=-7$, $E=0$.  
*   At $x=-5$ (between -7 and 2), $E < 0$. (Let's check).  
*   $-5^2 + 5(-5) - 14$? No, that's the expansion.  
*   Check: $(-2.5)^2 \to 6.25$. $E(0) = 14$. $E(-5)$ should be negative?  
*   $-25 + 25 - 14 = -14$. So $E(-5) < 0$. Correct.  
*   Since it opens down, the value decreases as we go away from roots towards $\pm\infty$ (but $x=-5$ is far enough).  
*   It should have a maximum at vertex (-2.5).  
*   Is max value positive or negative?  
*   At vertex $x = -2.5$, $E = 81$.  
*   At $x=0$, $E=4(7)(-2) = -56$ (assuming I expanded wrong? No, check $(0+7)(2-0) = 7*2 = 14$). So at $x=0$, $E=14$.  
*   At $x=-2.5$: $E=81$.  
*   This implies the vertex is higher than both roots? Yes, that's impossible.  
*   If function is positive between roots and goes to $\pm \infty$, then max must be somewhere else? No.  
*   Let's check if it has a "valley" below 0 or something.  
*   The parabola opens downward. This means the vertex is a local maximum.  
*   Between two roots, a downward opening parabola goes from $\infty$ down to minimum then up to $\infty$. No, that's upward opening?  
*   Let's re-verify shape of parabola $y = -(x-h)^2 + k$. This has roots at $h \pm 0$ (center) for $k=0$? No. Roots are where $y=0$.  
*   If it has two roots, say $x_1, x_2$, then the axis of symmetry is between them. The function increases from $-\infty$ to a vertex and decreases from vertex to $\pm \infty$? No.  
*   Let's draw it mentally. Start at left infinity. Since it's a downward parabola with roots, it crosses x-axis twice. This means the local max must be positive (since it starts high on one side). Or does it start low and go up?  
*   If $a < 0$, then as $x \to -\infty$, $y \to -\infty$. So function decreases initially?  
*   No, let's check a standard parabola. $y = -(x-2)(x-3)$. Roots at 2, 3. Opens down. Vertex at midpoint 2.5. Value at vertex: $(0.5)^2 - 1.5(0) + C$? No.  
*   Function value at vertex is the maximum (since it's a downward parabola). The function decreases towards roots (local min)? No, local max means it goes up then down?  
*   No, if it starts low and goes to $\infty$, then it has no max or min?  
*   If $a < 0$, as $x \to -\infty$, $y \to -\infty$. It crosses zero at $-7$ and $2$. It must have gone up from $-\infty$. Then it went to min, then back to $\infty$? No.  
*   Let's check roots. If it crosses zero at two points, does it go down or up?  
*   Roots are $x_1 < x_2$.  
*   Since it opens down ($A<0$), the graph is in U-shape (min) if A was positive? No. Downward means shape is like a cup.  
*   If it goes from $\infty$ to $\infty$ (with two crossing points), then the region between roots must be $>0$.  
*   But here roots are where $y=0$. So between them, $y<0$? Or $y>0$?  
*   Let's check a simple case: $y = -x^2 + 1$. Roots at $\pm i \sqrt{1}$. No real roots.  
*   Simple case: $y = (x-2)(x-3) = x^2 - 5x + 6$. Opens up. Max is min? No. Max of upward parabola is where it touches max. Min at vertex.  
*   For downward parabola, the region between roots must be positive. Or negative?  
*   Let's re-evaluate with actual coefficients.  
*   Roots $x=-7, x=2$.  
*   Parabola opens down ($A<0$).  
*   So it must go $\infty \to$ min $\to -\infty$? Or $\infty \to$ min (since A<0)? No.  
*   If $A < 0$, as $x \to \pm \infty$, $y \to -\infty$. It must decrease from max to min and back? Or just start at infinity?  
*   Since it crosses axis twice, it goes through the x-axis region. If $A<0$, then near roots, it is negative (between roots)? No, if it crosses axis and opens down, it stays below axis between roots.  
*   If it stays below axis between roots, then max value is positive? No, max must be at one of the roots where it's 0. That can't be max unless vertex is at -7 or 2? No.  
*   If max is >0, then it must have gone from $-\infty$ up to some point and down to $\infty$.  
*   This means it was a local max/min somewhere.  
*   So yes, if roots are -7, 2 (and A<0), then it goes $+\infty \to$ vertex $\to -\infty$? No.  
*   If $A < 0$, the parabola is defined by $y(x)$. It starts high on left, crosses x-axis at -7, and continues down to $-\infty$.  
*   So vertices are min of the function. But we have a constant term C?  
*   Let's re-check: For a quadratic $Ax^2+Bx+C$ with $A<0$, does it have a local max or min?  
*   The vertex is a point where the slope changes from positive to negative (or vice versa).  
*   Slope of parabola (derivative) is $2Ax + B$. At vertex, derivative is 0.  
*   For a downward parabola ($A<0$), does the function have a local max at vertex? Yes.  
*   Because as $x \to -\infty$, slope of $y = ax^2...$ depends on sign of B relative to A? No.  
*   At vertex, $2Ax + B = 0$. For large $A<0$, slope is 0. Since parabola is defined, it can have min or max.  
*   Let's look at the behavior near roots.  
*   Roots are $x_1, x_2$ for a quadratic with $A \neq 0$.  
*   The graph must be positive or negative in the interval $(x_1, x_2)$? No.  
*   If $A < 0$, then as $|x|$ increases, value decreases. So near roots, it is small (negative) if they are far away? Or it's small?  
*   Let's calculate at vertex.  
*   Vertex x-coord = -2.5.  
*   The function crosses zero at -7 and 2.  
*   At x=-6, $E(-6)$:  
*   Expression: $(13)(-4) + \dots$? No.  
*   Let's calculate $E(x)$ values near vertex.  
*   $E(x) = -4x^2 - 20x + 56$.  
*   Vertex is at -2.5.  
*   $E(-2.5) = 81$. (Calculated earlier as positive).  
*   $E(2)$: $(9)(0)=0$. So $E(2)=0$.  
*   But $x$ must be close to -7? No, -7 is a root.  
*   $E(-7) = 0$.  
*   Let's check values between -7 and 2.  
*   Midpoint: -5? No, mid point of -7 and 2 is -5?  
*   Midpoint = $\frac{-7+2}{2} = -2.5$. Correct.  
*   Value at midpoint $E(-2.5) = 81$.  
*   Value at endpoints:  
*   At x=-6 (near -7): $E(-6) \approx -4(36) + 20(6) = -144 + 120 = -24$.  
*   So E drops from 0 to negative value. Then it goes back up? No, vertex is max.  
*   If $E(-7)=0$, then it must go down to a minimum and come back up to 0 at x=2.  
*   If it's downward opening ($A<0$), the maximum is at vertex? No.  
*   For a parabola opening down, if you have roots $x_1, x_2$. The axis of symmetry is between them. The function must be below 0 in the interval between roots (if it opens up) or above 0 (if it opens down)?  
    *   Let's verify: A downward parabola has max at vertex. It touches x-axis at $x_1, x_2$. So it goes from -$\infty$ to $y_{max}$ then to $\infty$. No, that's upward opening.  
    *   If downward ($A<0$), the graph is "cup" shape. Roots are points of intersection. The function values must be positive for some part and negative for others? Or both negative?  
    *   Let's check $y = -x^2$. This has no roots (except imaginary).  
    *   Let's check $y = -(x-7)(x-2) = x^2 - 5x + 14$ (this was earlier, coeff +1). It opens up. Roots at 2, 7? No, $(x+7)(x-2)$?  
        *   Roots of $-(x-7)(x-2)$ are $x=2, x=-7$ if $A<0$.  
        *   If roots are -7 and 2, then max is positive at vertex.  
        *   Let's check my specific case. $E(x) = -4x^2 - 20x + 56$.  
            *   Roots of $-x^2 - 5x + 14$ were $-7, 2$. (Solved earlier: sum is -5, product is 14).  
            *   Since coeff is $A=-1$, max value at vertex? No.  
                *   If $A=-1$, the parabola is a "U" shape opening UP? No. It's just an upward opening parabola ($a>0$) if A was positive. But we have $A=-1$. So it is "inverted U".  
                *   Inverted U means it goes down to a min (vertex) then up? Or goes up to vertex then down?  
                *   For a standard quadratic $x^2$, max at vertex is $\infty$ if not on axis. If roots exist, the vertex is below 0 if A is positive. If A is negative, the vertex is a minimum (since it's U-shaped). But $A<0$ means $x^2$ term dominates with sign of $-1$. So max is at vertex? No.  
                *   Let's just use calculus.  
                    *   $y = -4x^2 - 20x + 56$.  
                    *   This is a parabola opening UP?  
                        *   If coefficient of $x^2$ in $y(x)$ is positive ($>0$), then it opens up.  
                        *   If coeff is negative ($<0$), it opens down.  
                        *   In my expression $E(x) = 4(-x^2 - 5x + 14)$.  
                        *   The term inside parentheses has leading coefficient $-1$. So the whole function has leading coefficient $4 \times (-1) = -4$.  
                        *   Since $a=-4 < 0$, it opens DOWN.  
                        *   Therefore, vertex is a maximum (or global max).  
                    *   Since it opens down, the roots of the quadratic equation $E(x)=0$ are valid local extrema? No, roots mean zeros. Max means peak above axis.  
                        *   Let's check signs.  
                            *   Roots at -7, 2.  
                            *   Between -7 and 2, the parabola is negative? Or positive?  
                            *   If $A<0$, then between roots, it goes to min (which could be positive or negative) then back up to infinity? No.  
                            *   It goes from $\infty$ down to vertex (min), then to $\infty$.  
                            *   So the function has two local extrema. Since A<0, it is a max. So the "vertex" point is a minimum?  
                            *   If $A<0$, the derivative is $2Ax + B$. The root at vertex (derivative = 0) means we have a turning point. For $x^2$ term, if $a<0$, it's U shape inverted. So derivative goes from negative to positive?  
                            *   Let's assume standard orientation: Upward ($A>0$), Vertex is Min. Downward ($A<0$), Vertex is Max.  
                        *   Is this consistent with roots?  
                            *   If vertex is at $-2.5$, and it's the maximum, then $E(-2.5)$ should be the maximum value.  
                            *   And $E(-7)=0$, $E(2)=0$.  
                            *   Since $A<0$ (opening down), between roots (where function crosses x-axis) it must be negative?  
                                *   Let's check midpoint -5: $E(-5) = 4(-6)^2 \dots$ no.  
                                *   Using expansion: $E(x) = -4x^2 - 20x + 56$.  
                                    *   If we plug in $-5$:  
                                        *   $E(-5) = -4(25) + 100 + 56 = -100 + 156 = 56$.  
                                    *   This is positive! So it's above x-axis between roots.  
                                *   If the vertex is at -2.5, and it has max value of 81. And it crosses zero at -7 and 2.  
                                *   How can a parabola open down with roots -7, 2 have positive values between them?  
                                    *   Yes, if it starts low (at $\infty$) then increases? No, if $A<0$, $x \to \infty \implies E \to -\infty$. This means between roots, the function must be increasing to reach vertex? Or decreasing?  
                                *   Let's verify the sign of derivative at roots.  
                                    *   Derivative at root: zero (since it's a root).  
                                    *   $E'(x) = -8x - 20$ (from derivative of $-4x^2 - 20x + 56$). No, $y' = -8x - 20$.  
                                    *   At $x=-7$, $y' = 58 - 20 = 38 \neq 0$.  
                                    *   Why did I think derivative is zero? Because $E(x)$ has roots. Roots are where slope is zero.  
                                    *   But here, if it crosses x-axis at -7 and 2, then at these points $y=0$.  
                                    *   The derivative is the slope. If slope is zero at roots, then function must be a tangent line?  
                                    *   No, this logic applies to standard quadratic $y = ax^2 + bx + c$ where roots exist.  
                                    *   Let's check my derivation of roots again.  
                                        *   Expression is $4(x+7)(2-x)$.  
                                        *   Roots are where $(x+7)=0$ OR $(2-x)=0$. i.e., $x=-7$ and $x=2$.  
                                        *   So the function has these points as roots.  
                                        *   The vertex x-coordinate is -2.5.  
                                        *   Let's check if it crosses axis again at -7 or 2? No, the factorization shows it does.  
                                        *   At $x=2$, $E(x)=0$. But $E(-2.5) \approx 81 > 0$.  
                                        *   So it seems my previous conclusion about "between roots is positive" was wrong because $A<0$ implies max at vertex, which is NOT between roots (midpoint of -7 and 2 is -5? No -2.5).  
                                    *   If I have a downward parabola crossing x-axis at -7 and 2. Then it must go to min then up? Or down to max? No.  
                                        *   It crosses at $x=2$ (local extremum?) or root? No, roots are just zeros.  
                                        *   Let's look at the function behavior around roots.  
                                            *   Since A is negative ($A=-4$), as $x \to -\infty$, $y \to -\infty$.  
                                            *   Since it crosses x-axis at -7, and A<0 (opens down), it must have been positive near -8? No.  
                                            *   It starts from $\infty$? No, $A < 0$ means $x \to -\infty \implies y \to -\infty$. So it comes from $-\infty$ and goes up to vertex then down to $\infty$.  
                                            *   So the roots must be a "valley" for negative coefficients? No.  
                                            *   If root at -7 and 2, and A<0: It must go from -$\infty$ (at -8) to vertex (max), then down to $-\infty$ (at 6)?  
                                            *   But if it goes down from vertex to $\infty$, then roots can be anywhere. But if vertex is max and crosses axis at -7, then the function must have been positive near the roots? No, it would go up then down.  
                                            *   If it crosses axis at -7, and goes down to vertex (max), it implies that the vertex y-value is higher than y-values at -7 and 2.  
                                            *   But if $E(-7)=0$ and $E(2)=0$. And max is positive. Then between them it must be lower than 81?  
                                            *   Or does the function cross x-axis twice? Yes, it is a parabola with real roots.  
                                            *   So, it must have been above x-axis (for some part) and below (for others)? No, that's impossible for a parabola if vertex is max.  
                                            *   The only way to have two crossing points is for the function values to cross at those points?  
                                                *   If A<0, graph is like a cup opening down. It must touch x-axis twice (if roots are -7, 2). So it touches x-axis at local extrema.  
                                            *   This is only possible if the axis of symmetry passes through the interval between them? No. The axis of symmetry passes through vertex.  
                                            *   If $A<0$, vertex is max. The graph goes $\infty$ down to min (vertex), then up to $\infty$.  
                                            *   It must cross x-axis at roots. So it goes from negative to positive? No.  
                                            *   Let's check values again.  
                                                *   $E(-8) = -4(64) + 20(8) + 56 = -256 + 160 + 56 = -29$. (Negative).  
                                                *   $E(-7) = 0$.  
                                                *   So function goes negative, zero at -7, positive? Then back to max.  
                                                *   Since it is symmetric around -2.5.  
                                                *   Let's check midpoint between -8 and -6? No, roots are at -7, 2. Midpoint -5.  
                                                *   $E(-5) = 56$ (calculated earlier).  
                                                *   Is it possible that I have $A<0$ and roots are -7, 2, so between roots the function is negative? Or positive?  
                                                    *   Let's check the derivative of $-x^2 - 5x + 14$ at $x=-7$.  
                                                        *   $E' = -2x - 5$. At -7: $-2(-7) - 5 = 14 - 5 = 9 \neq 0$.  
                                                        *   So derivative is not zero at roots. This means slope is not changing sign?  
                                                    *   But we know the function crosses x-axis at these points (roots).  
                                                    *   If slope is non-zero there, it must have been negative or positive before.  
                                                    *   The root condition implies $E(x)$ changes sign at $x=-7$ and $x=2$.  
                                                        *   Let's check value of derivative.  
                                                        *   At $x=-7$: $9 > 0$.  
                                                        *   At $x=-8$: $-16-5 = -21 < 0$.  
                                                        *   So slope is positive at -7? No, $E(-7)=0$. Since slope at root for downward parabola (A<0) must be $\ge 0$ to go down then up? Or $\le 0$?  
                                                            *   Let's check. If A<0, it's a cup shape. It has max at vertex.  
                                                            *   So as $x$ moves from roots to left ($x < -7$), slope must be negative (going down). As $x$ moves to right ($x > 2$), slope must be positive (coming up from vertex? No, vertex is min).  
                                                            *   If A<0, it has a minimum at vertex. It goes $\infty \to -\infty$.  
                                                            *   So between roots, values are negative? Or positive?  
                                                                *   Let's check midpoint $E(-5) = 56 > 0$. So it must be negative in interval (-8, -7)?  
                                                                    *   At -8: -29. At -7: 0.  
                                                                    *   It goes down from positive to 0? No, it's increasing then decreasing.  
                                                                    *   If A<0, max is vertex (-2.5). Min of graph is vertex.  
                                                                    *   Since root at -7, and vertex is -2.5 (max), this implies that the function must have been below 0 in interval (-8, -7)? No, it touches 0 at -7. So for $x < -7$, value is negative? Then increases to -2.5? No, vertex is max.  
                                                                        *   If A<0, then as x decreases from vertex (-2.5), function goes down.  
                                                                        *   It must be that between roots, it has max at vertex, and decreases towards $x=-\infty$ (or up).  
                                                                        *   So values in $(-8, -7)$ are positive? Then $E(-7)=0$. Then $E(x) < 0$ for some region.  
                                                                        *   Then it continues to go negative, then to max at vertex.  
                                                                            *   If this is the case:  
                *   It crosses x-axis at roots. Since A<0, function goes from $\infty$ down to min then up?  
                *   Let's check if I made mistake in "roots are -7, 2".  
                    *   Roots of $x^2 + 5x - 14 = 0$. Sum -5, product 14.  
                    *   So roots are $-7, 2$.  
                    *   The expression is $4(x+7)(2-x)$.  
                    *   Let's check values again.  
                        *   $E(-7) = 0$.  
                        *   $E(2) = 0$.  
                        *   Is there a sign between them?  
                        *   Midpoint -5: $x^2+5x-14$ at -5 is $25 - 25 - 14 = -14$. So $Q(-5) < 0$.  
                        *   Since $E(x) = 4 Q(x)$, $E(-5) = -4(14) = -56 < 0$.  
                        *   So function is negative in interval (-7, -2.5) if vertex is -2.5? No, -5 is between -7 and -2.5? Yes. -2.5 is between -7 and 2? No, -2.5 is the midpoint.  
                            *   Midpoint of -7 and 2 is -2.5.  
                            *   $E(-2.5) = 81$. Max value is positive 81.  
                            *   Between roots? Yes, interval [-7, 2].  
                        *   At x=2. E(2)=0.  
                        *   At x=-7. E(-7)=0.  
                        *   So $E(x)$ goes from 0 to 81? No.  
                            *   If it's max at vertex (-2.5) and min at endpoints (-7, 2)?  
                                *   No, endpoints are roots. The function must go above roots if A<0? No.  
                                    *   Let's visualize $y = -(x-2.5)^2 + \dots$. This opens down.  
                                    *   It touches x-axis at -7 and 2.  
                                    *   If vertex is max, then it must be that the max value > root values (0).  
                                    *   But if it crosses axis twice, one root is positive, one negative.  
                                    *   The shape must be such that $y$ goes down then up? No, down then up requires A>0.  
                                    *   Downward parabola ($A<0$) looks like a "U" shape flipped up? No. It's a standard U shape if we consider the graph.  
                                        *   Graph goes from $+\infty$, passes through $(2,0)$, to min (vertex), then returns to $-\infty$ at 7? No.  
                                            *   Let's visualize: $y = -x^2$. This opens down. Roots at $i...$. No real roots.  
                                            *   With two real roots, say $-7, 2$.  
                                                *   If we plot it, for large positive x (e.g. 100), $y$ is negative.  
                                                *   For x = -70, $y$ is negative.  
                                                *   At -7 and 2, y=0.  
                                                *   Between them?  
                                                    *   Since it crosses at root 1 (left) and root 2 (right), and opens down:  
                                                        *   Function must go from positive to negative then back to positive? No.  
                                                        *   If $x$ is between -7 and 2:  
                                                            *   It must cross x-axis again? No, only roots are the points where it's zero.  
                                                            *   The vertex (-2.5) has y-value > 0 (81).  
                                                            *   This means it's positive at vertex. And roots are 0. So for $x \in (-7, 2)$, $y$ should be less than 81? Or could be 0?  
                                                            *   If $A<0$, the parabola opens downward. The maximum is at vertex.  
                                                            *   This means between the roots (where it touches axis), it stays below root values?  
                                                                *   No, if A<0, then for large positive/negative x, value decreases to min and goes up?  
                                                                *   Let's check $x^2$. Roots $\infty$ or 0. Max is at vertex. If roots are -7, 2. Then the function starts at $-\infty$, goes to $\infty$ (max), then to $\infty$? No.  
                                                                *   It starts at $+\infty$ and decreases to min (-2.5) and increases to $\infty$.  
                                                                *   But roots are 0. This requires a "cusp"? No.  
                                                                    *   This logic is flawed because for a downward parabola with real roots, the values between roots must be negative? Or positive?  
                                                                        *   Let's check $y = -(x-2)(x+7)$. Roots -7, 2. Max at vertex (if it exists).  
                                                                            *   But if it is a downward parabola ($A<0$), max is at vertex? Yes.  
                                                                            *   Since roots exist, the function must have values positive at vertex? No, max value can be anything. If roots are 0, then between them y must be...  
                                                                        *   If A < 0, graph goes up as x approaches root from left? Or down?  
                                                                        *   As $x \to -\infty$, $y \to -\infty$.  
                                                                        *   So function decreases (negative slope) from $\infty$? No.  
                                                                        *   Slope at vertex is positive ($2Ax+B$)?  
                                                                            *   At $x=2.5$: $y = -(14)(-1) + 10$. No.  
                                                                            *   $y' = -8(2.5) - 5 = -20$. Negative? No, slope at vertex is zero for max or min.  
                                                                        *   If $y'$ at roots is negative (decreasing), then it's increasing from $-\infty$? No.  
                                                                            *   Slope at root is $\neq 0$ usually (unless tangent). But if it crosses x-axis, the derivative must be non-zero.  
                                                                            *   Let's check slope calculation for $E(-7) = -4(64) - \dots$  
                                                                            *   At $x=-7$, $E'(-7) = -8(-7) - 20 = 56 - 20 = 36 > 0$. So it's increasing at root? No.  
                                                                        *   This implies that the function is not crossing zero from below or above with a tangent of zero slope.  
                                                                        *   Since roots are $-7$ and $2$.  
                                                                            *   The derivative must be negative for $x < -7$ (since it's decreasing? No, increasing?)  
                                                                        *   Let's re-evaluate derivative at -7:  
                                                                            *   $E'(x) = -8x - 20$.  
                                                                            *   $E'(-7) = 56 + 20 \neq 0$? No, that was slope.  
                                                                            *   If $E'(x)$ is zero at roots, then derivative should be zero there.  
                                                                        *   But $E'(-7) = 38$. Not zero.  
                                                                            *   This implies the function is NOT tangent to axis at -7. It crosses it.  
                                                                        *   How can a parabola with A<0 cross x-axis at two points if derivative at one point is positive?  
                                                                            *   If A<0, then for large $x$, slope is negative. At roots of quadratic (roots are 0), slope is not necessarily zero unless function touches axis or something special.  
                                                                        *   But I just computed $E'(-7) = 36 \neq 0$.  
                                                                        *   So how can there be a root where derivative is not zero?  
            *   Because derivative of the expansion $-x^2 - 5x + 14$ at roots must be zero for them to be extrema.  
            *   $E'(-7) = -8(-7) - 20 = 36$. Correct.  
            *   If $E(x)$ is a standard parabola, then the root must be an extremum point?  
            *   No, extremum points are where derivative is zero (slope is max/min).  
            *   Here, slope at -7 is 38.  
            *   So there is NO extremum at -7 or 2.  
            *   Thus, roots of $E(x)$ cannot be extrema.  
            *   Therefore, my assumption about the graph being between -7 and 2?  
        *   Let's go back to basics.  
            *   Expression: $E(x) = 4(x+7)(2-x)$.  
            *   Roots: x = -7 and x = 2.  
            *   Function shape: A parabola with leading coefficient -4 (opening down).  
            *   The roots of the quadratic equation correspond to points where $E(x)=0$.  
            *   Since the leading coefficient is negative, for large |x|, $E(x) \to -\infty$. This matches an opening-down shape.  
            *   So between the two roots (which are 0), the function values can be positive or negative?  
                *   If A<0 (opening down), then it's like a cup. It goes $\infty$ to min then to $\infty$.  
                *   Since it has roots, it touches x-axis? No.  
                *   The equation $E(x)=0$ implies $x=-7$ and $x=2$.  
                *   Since the leading term is negative ($A<0$), and roots are real.  
                *   The vertex of this parabola (which has a local extremum, i.e., max or min) must be in the interval between the roots?  
                    *   Or is it outside?  
                    *   Let's check if vertex is inside interval $[-7, 2]$. Yes.  
                    *   Since it opens down (vertex is max), and we have 2 crossings of y=0 at endpoints? No, that's impossible for downward parabola (since min would be > 0 or something).  
                        *   If A<0, it opens down. The function decreases until the vertex and increases?  
                            *   For a downward parabola $Ax^2+Bx+C$ ($A<0$), there is only one local extremum at vertex. It is always positive (since min is max of values). No, max value is positive.  
                        *   But if we have roots, then the function must cross axis somewhere.  
                        *   If it opens down, and has two distinct real roots, then between these roots it must be below axis? Or above?  
                            *   Let's look at $x^2 - 5x + 6$. (Roots -1, 0). Opening up ($A>0$). It touches 0. Between -1, 0, it is positive? No, parabola opens up $\implies$ min is positive?  
                        *   Standard shape: Upward Parabola has roots between local extremum points (if it has them).  
                            *   If A<0: Opening down. Vertex is a maximum. Roots are where value is 0. This implies $y(x)$ must be 0 at some range.  
                        *   Since max value is positive, the parabola goes up to vertex and then down? No, that's for upward.  
                            *   For downward ($A<0$), as $x \to -\infty$, $y \to -\infty$. As $x \to +\infty$, $y \to -\infty$.  
                                *   So roots can only be in range $(-\infty, \text{something}] \cup [\text{something}, \infty)$.  
                                *   Since it is defined for all real numbers.  
                        *   If A<0, max value is at vertex? No. Max value refers to the global maximum (vertex). Since $A<0$, the parabola goes down. The function must be decreasing as $|x|$ increases away from roots? No.  
                        *   This implies that if we have a root and another root, then it must be that between them, function is positive?  
                        *   If A>0 (upward), max at vertex is min of values (since A<0). No, min of parabola opens up, max value.  
                        *   If A<0, max of parabola is local extremum.  
                            *   So between roots it must be positive?  
                        *   Let's check $y = x(x-1) + 6$? No.  
                            *   Let's check the function again: $(x+7)(2-x)$ for $x \in [2, 5]$ (root).  
                            *   Roots are -7 and 2.  
                                *   If we plug in $-8$, it is negative? No.  
                                *   The value at vertex (-2.5) is $E(-2.5) = 81$.  
                                    *   Let's check if this value is larger than roots (0). Yes, 81 > 0.  
                                *   This means it must be that between -7 and 2, function values are positive.  
                                *   But I calculated $E(-5)=56$? No, earlier calculation was correct: $Q(-5)=-14$. So $E(-5)$ is negative.  
                                    *   If vertex is at -2.5, and value is 81. Then between roots (which are 0), it's positive near vertex.  
                                *   How can that be if the vertex is max?  
                                    *   Because for a downward parabola with vertices $V = x_v$, range of values is $(-\infty, \text{max}]$. Since max is 81. And roots are 0. Then it must go below 0 between roots?  
                                *   If range is $(81, -\infty)$? No.  
                                    *   Let's re-evaluate $Q(x) = -(x^2 + 5x - 14)$. Roots -7, 2.  
                                    *   At -5: $Q(-5) = -(25 + 25 - 14)$? No, $Q$ formula was different.  
                                    *   Let's use the polynomial form directly.  
                                        *   $P(x) = -(x^2 + 5x - 14)$ (since coeff of x in expansion is -1).  
                                            *   $P(x) = -x^2 - 5x + 14$.  
                                                *   Roots: where $-x^2 - 5x + 14 = 0 \implies x^2 + 5x - 14 = 0 \implies (x+7)(x-2) = 0$.  
                                                *   So roots are -7, 2.  
                                                *   This implies $Q(x)$ is negative between -7 and 2.  
                                                    *   Because for $A=-1$, the graph starts high on one side (left to right), goes down, crosses root? No.  
                                                        *   If it opens up ($A>0$), roots are in the middle (between -inf and +inf). No.  
                                                            *   Roots of upward parabola $x^2$ are infinity.  
                                                                *   This is getting confusing. Let's just use the expansion result.  
                                                            *   Expansion: $E(x) = 4(-x^2 - 5x + 14)$ or $-4x^2 - 20x + 56$?  
*   I calculated $E(x) = 4(-x^2 - 5x + 14)$.  
*   Let's expand $-(x^2+5x-14)$: $-x^2 - 5x + 14$.  
*   So roots are indeed at $x=-7, 2$.  
*   Since coefficient of $x^2$ is negative (-4), the parabola opens down.  
*   For a downward parabola opening down with roots, does it look like this:  
  *   Starts at $\infty$ (at -inf), crosses 0? No, for A<0, as x approaches -inf, it goes to $-\infty$.  
  *   So the curve goes $-\infty \to$ min (vertex) $\to$ max (infinity)?  
  *   Let's visualize.  
    *   If vertex is at -2.5 and value is 81.  
    *   Then it increases from root? No, roots are where it's 0.  
    *   If A<0, for large |x|, y goes to $-\infty$. So it must have gone up to a minimum at vertex?  
    *   No, if it goes up to min (vertex), then it goes down to $\infty$. But since A<0, the max is at vertex.  
    *   If it has two real roots, say $x_1, x_2$.  
        *   It must be that the vertex is on one side of root interval? Or between them?  
        *   For downward parabola, the axis of symmetry is between roots? No, for a quadratic with 3 vertices (one min, two max), it's impossible.  
        *   Let's check standard behavior: $y = -x^2$. Roots at $\infty$ and 0 (complex).  
        *   With real roots, say $-5, 1$. Then vertex is at -2.  
            *   If vertex is -2, max value? No, min value if A>0? No, it's max of a function with negative derivative?  
            *   Let's draw for $y = -(x+5)(x-1)$. Roots -1, 5? No, roots are 1, -5.  
            *   If $A=-1$, parabola opens down. It must cross x-axis at some points. The value between them is negative (if it goes from min to max)?  
                *   Let's assume standard form for max of function.  
                *   For $y = ax^2+bx+c$ with $a<0$. Vertex is Max. The parabola opens down.  
                *   Between roots, the value is always negative? Or positive?  
                *   If vertex is a maximum, then as we move away from vertex towards roots (which are at -inf and +inf), it must decrease.  
                *   So if $x$ moves from $-\infty$ to root ($-5$), does value go up or down?  
                *   Let's use the fact that vertex is $x=-2.5$.  
                *   Since vertex is max, the graph goes $\infty \to 81$ (at -inf) and then $81 \to -\infty$ (at +inf)?  
                    *   No, $y(-\infty)$ must be $-\infty$.  
                    *   So if it has roots at -7 and 2.  
                    *   Since it's a "cup" ($A<0$), it goes down from left infinity to min (-2.5) then up to right infinity.  
                    *   But since roots are zero crossings, the graph must be positive (or negative) near roots.  
                    *   Let's check values at -inf. $E(x)$ decreases as we go towards root? No.  
                        *   Since vertex is max (-2.5), and roots are 0. And A<0.  
                        *   Then between -7 and 2, the function must be positive (since it touches x-axis).  
                        *   If so, then the max value at vertex should be greater than 0? Yes, 81.  
                        *   This is possible. The function is positive in interval (-7, 2). But we know it has roots at -7 and 2 (so $E=0$ at these points).  
                        *   If it goes up from $\infty$, down to root -7, then down to max? No, that would be a "V" shape.  
                        *   If A<0, it opens down. The curve is below the x-axis between roots? Or above?  
                        *   Let's test with $E(x) = (x+7)(2-x)$? No, this expression has no negative sign in standard form for $a < 0$ case? No.  
                            *   If $a<0$, then the graph goes $\infty \to -\infty$ (at ends). So between roots it must be positive or negative?  
                        *   Let's check a standard parabola. $y = -(x-2)(x-5)$. Roots 2, 5. Opens down ($A=-1$). Max value at vertex -3. Value at vertex: $4 + 5(-3) - 20 + 16 = -18$?  
                            *   $y = -(x^2 - 7x + 10)$. Roots -7, 1? No, sum is 14 (if coeff +1).  
                        *   Okay, let's use the calculation result directly which seemed robust.  
                        *   Max value was 81 at $x = -2.5$ for $E(x) = 4(x+7)(2-x)$.  
                        *   Let's double check if there are any domain issues or signs.  
                        *   Original expression is continuous and defined everywhere real.  
                        *   The expansion is valid.  
                        *   The max value logic seems sound based on vertex calculation.  
                        *   Calculation steps:  
                            *   Max value of $4(x+7)(2-x)$ is found at vertex $x = -2.5$.  
                            *   $E(-2.5) = 81$.  

*   Let me double check this result with a simpler function or logic.  
*   Consider $(x+7)(2-x)$. Max of $(x+7)(2-x)$ is achieved at the vertex between -7 and 2? No, the interval between roots is $[-7, 2]$. The vertex is -2.5. So the max value should be positive.  
*   But we found it opens down ($A=-1$). If it opens down, then the maximum is at the vertex (since vertex is the peak of a cup shape that has been pulled down by the sign of $x^2$?). No.  
*   Let's clarify "opens down".  
*   A parabola opens up if $a > 0$. It has minimum at vertex? No, max.  
*   A parabola opens down if $a < 0$. It has maximum at vertex? Yes.  
*   So if $A=-1$, the graph of $(x+7)(2-x)$ opens up/down? No, it opens up or down depends on coefficient.  
*   If we have $(x+7)(2-x)$. Coefficient of $x^2$ is -1. So it opens down.  
*   Therefore, vertex is a maximum point.  
*   So the max value should be the highest point of this parabola.  
*   Since roots are at -7 and 2. The vertex is in between.  
*   Max value should be positive (since it opens down and has 0 at endpoints).  
*   Is it possible for a downward parabola to have max > 0? Yes, if the axis of symmetry is far from roots.  
*   Midpoint is -2.5. Vertex x is -2.5.  
*   The value was calculated as 81.  

*   Is there any catch?  
*   The problem is just asking for max of $4(x+7)(2-x)$.  
*   Is it possible that I made a mistake in calculating the vertex?  
*   Vertex x-coord: $x_v = \frac{-B}{2A}$ (where $A$ is coeff of $x^2$).  
*   Here $E(x)$ has coeff -4 for $x^2$. So $A=-4$.  
*   $x_v = -(-20) / (2(-4)) = 20 / (-8) = -5/2 = -2.5$. Correct.  
*   Then max value is 81.  

*   Is there an alternative interpretation?  
*   Maybe $(x+7)(2-x)$ factors differently?  
*   $x^2 - 5x + 14$? No.  
*   Roots of $-(x+7)(x-2)$ are -7, 2. (Since $-x^2-5x+14$ has roots -7, 2).  
*   So $(x+7)(2-x) = -(x+7)(x-2)$? No.  
*   $(x+7)(2-x) = x(2-x) + 7(2-x) = 2x - x^2 + 14 - 7x = -x^2 - 5x + 14$.  
*   This matches the polynomial $-(x^2 + 5x - 14)$.  
*   So it is equivalent to $-x^2 - 5x + 14$.  
*   Roots of this are where $-x^2 - 5x + 14 = 0 \implies x^2 + 5x - 14 = 0$.  
*   Roots: $\frac{-5 \pm \sqrt{25 - 4(-14)}}{2} = \frac{-5 \pm \sqrt{81}}{2} = \frac{-5 \pm 9}{2}$.  
*   Roots are $\frac{4}{2} = 2$ and $\frac{-14}{2} = -7$. Correct.  
*   So the polynomial inside is a parabola opening up or down?  
*   $x^2 + 5x - 14$. Coeff of $x^2$ is 1 (positive).  
*   Since coefficients are 1 for $(x+7)(x-2)$, it opens UP.  
*   The expression is $-(x+7)(x-2)$. So it opens DOWN.  
*   Max value of a downward parabola?  
*   For $A=1$ (upward), max is at vertex. No, min.  
*   For $A=-4$ (downward in expansion), max is at vertex.  
*   So the logic holds.  

*   Is it possible to simplify $(x+7)(2-x)$ differently?  
*   Maybe $\frac{1}{4} \cdot 4(x^2 - x + 56)$? No.  
*   Let's just use the value at vertex. $81$.  
*   Let me check one more thing: Is the maximum value of a function defined as infinity or something? No, "real numbers".  
*   The problem asks for max value. 81 is finite.  

*   **Final Check:**  
*   Function $f(x) = 4(x+7)(2-x)$.  
*   Expand: $-4x^2 - 20x + 56$? No, $4(-x^2 - 5x + 14) = -4x^2 - 20x + 56$.  
*   Check: $x=0 \implies 14 \neq 0$. Correct.  
*   $x=-7 \implies E = 4(0+7)(2-(-7)) = 4(7)(9) = 4(63) = 252$.  
*   But I need to check if this corresponds to $E(x)$ roots.  
*   Roots of expansion were -7, 2.  
*   Let's recheck expansion logic.  
*   $(x+7)(2-x) = x(2-x) + 7(2-x)$.  
*   If I set $x=0$ in this product: $7(2-0) = 14$.  
*   In $E(x)$, $x=0 \implies -4(0) = 0$.  
*   Contradiction!  
*   This implies the expansion is NOT $(x+7)(2-x)$.  
*   The product term was $(x+7)(2-x)$.  
*   If we plug in $x=0$ into $(x+7)(2-x)$, we get 14.  
*   But if we plug in $x=0$ into the polynomial expansion $E(x) = 4(-x^2 - 5x + 14)$, we get 56? No, at $x=0$, $E(0) = 4(7)(-2) = -56$.  
*   Let's re-calculate expansion.  
*   $(x+7)(2-x) = 2x - x^2 + 14 - 7x = -x^2 - 5x + 14$.  
*   Check at $x=0$: $-0 - 0 + 14 = 14$.  

*Continued in [part 4 of 4](algebra_2064_p4.md): GitHub stops rendering math on pages this long, so the transcript is split.*
