# test/algebra/2064.json (Algebra, level 5)

> What is the maximum value of $4(x + 7)(2 - x)$, over all real numbers $x$?  

**Correct.** Gold `81`, predicted `81`. Finish: stop, 6226 tokens, 2 waits, 646.1 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's a thinking process that leads to the solution:  

1.  **Analyze the Problem:**  
    The goal is to find the maximum value of the function $f(x) = 4(x + 7)(2 - x)$ for all real numbers $x$.  

2.  **Expand and Rewrite (Optional but helpful method):**  
    Let's expand the expression inside first to understand its structure, although direct application of algebraic techniques might be faster.  
    $f(x) = 4(x^2 - 5x - 14)$  
    $f(x) = 4x^2 - 20x - 56$  

3.  **Identify the Type of Function:**  
    The expression involves a quadratic term with a positive coefficient ($4x^2$). This means the graph is an upside-down parabola (a concave down function).  
    Therefore, the maximum value occurs at the vertex of the parabola.  

4.  **Find the Vertex:**  
    For a general quadratic equation $ax^2 + bx + c$, the x-coordinate of the vertex is given by $x = -\frac{b}{2a}$.  
    Here, $a = 4$ and $b = -20$.  

    $x = -\frac{-20}{2(4)} = \frac{20}{8} = \frac{5}{2} = 2.5$.  

5.  **Calculate the Maximum Value:**  
    Now substitute $x = 2.5$ back into the original function to find the maximum value (or use the vertex formula $f(x) = c - \frac{b^2}{4a}$).  

    Method A: Direct Substitution  
    $f(2.5) = 4(2.5 + 7)(2 - 2.5)$  
    $f(2.5) = 4(9.5)(-0.5)$  
    $f(2.5) = 4 \cdot (-4.75)$  
    Calculation: $4 \times -4.75$.  
    $4 \times 4 = 16$.  
    $4 \times 0.75 = 3$.  
    So $16+3 = 19$. Negative sign? Let's check the logic.  
    The term is $(x+7)$ (positive) and $(2-x)$ (negative). The product is negative. Then multiplied by 4, it stays negative.  

    Let me re-evaluate the factorization to ensure no arithmetic error.  
    $f(x) = 4(x^2 - 5x - 14)$? No, $(x+7)(2-x) = x(2) + 7(2) - x(x) - 7x$ ? No.  
    Let's do FOIL carefully.  
    $(A+B)(C-D)$. Here $(x+7)(- (x-2))$. Or just multiply directly.  
    $= 4 [ (x \cdot 2) + (x \cdot -x) + (7 \cdot 2) + (7 \cdot -x) ]$ ... No that's not grouping right.  
    Let's use the standard expansion:  
    $(x + 7)(2 - x)$  
    $= x(2) + x(-x) + 7(2) + 7(-x)$  
    $= 2x - x^2 + 14 - 7x$  
    $= -x^2 - 5x + 14$.  

    **Wait, I made a mistake in Step 2.**  
    Let's re-check Step 2.  
    $f(x) = 4(x+7)(2-x)$  
    Expansion: $4(-x^2 + 2x - 7x + 14) = 4(-x^2 - 5x + 14) = -4x^2 - 20x + 56$.  
    Okay, so the coefficient of $x^2$ is negative. This means it is an upside-down parabola? No, upside down is positive $a$. If $a < 0$, the graph opens downwards. So the vertex represents a maximum.  

    Let's double check my mental expansion in Step 1.  
    Step 1 had $f(x) = 4x^2 - 20x - 56$. This was wrong.  
    Let's re-expand:  
    $(x+7)(2-x)$  
    $= x(2-x) + 7(2-x)$  
    $= 2x - x^2 + 14 - 7x$  
    $= -x^2 - 5x + 14$.  
    Multiply by 4:  
    $-4x^2 - 20x + 56$.  

    Okay, let's verify the vertex calculation with these coefficients.  
    $a = -4$, $b = -20$, $c = 56$.  
    $x_{vertex} = \frac{-b}{2a} = \frac{-(-20)}{2(-4)} = \frac{20}{-8} = -\frac{5}{2} = -2.5$.  

    Now find the value at $x = -2.5$.  
    $f(-2.5) = 4(-2.5 + 7)(2 - (-2.5))$  
    $= 4(4.5)(2 + 2.5)$  
    $= 4(4.5)(4.5)$  
    $= 4 \cdot (4.5)^2$  
    $= 4 \cdot 20.25$  

    Calculation:  
    $4 \times 20 = 80$.  
    $4 \times 0.25 = 1$.  
    Total = 81.  

    Let's try Method B (Completing the square) to verify.  
    Expression: $-4x^2 - 20x + 56$  
    Factor out -4: $-4(x^2 + 5x - 14)$? No, $(5)(-1) = -5$. Here we have $-5x$. So inside bracket is $x^2 + 5x$. Correct.  
    Complete the square for $x^2 + 5x$: Add $(5/2)^2 = 6.25$.  
    $-4 [ (x^2 + 5x) - 14 ]$ -- this doesn't look right immediately with the constant shift inside the bracket if we factor out differently.  

    Let's stick to completing the square on the original polynomial expression first: $-4x^2 - 20x + 56$.  
    $-4(x^2 + 5x) + 56$  
    $-4( (x^2 + 5x + \frac{25}{4}) - \frac{25}{4} ) + 56$  
    $-4( (x + \frac{5}{2})^2 - \frac{25}{4} ) + 56$  
    $-4(x + \frac{5}{2})^2 + (-4)(-\frac{25}{4}) + 56$  
    $-4(x + \frac{5}{2})^2 + 25 + 56$  
    $-4(x + \frac{5}{2})^2 + 81$.  

    The maximum value is the constant term if the squared term coefficient is negative. Since $-4 < 0$, the parabola opens down and 81 is the global maximum.  

    Let's verify with AM-GM inequality or just simple logic to be absolutely sure.  
    $(x+7)(2-x)$. This looks like part of a geometric mean setup?  
    Or simply, let $u = x+7$ and $v = 2-x$. Note that $u-v = (x+7) - (2-x) = 2x + 5$, not helpful.  
    Let's express $(x+7)$ in terms of the other factor?  
    Let $y = (x+7)(2-x)$.  
    The function is $4y$. We need to maximize $4y$. So we maximize $y$.  
    $y = -x^2 + 2x + 14 - x(-5)$... no.  
    $y = -x^2 - 5x + 14$. (This matches my previous derivation).  

    Let's use the property of maximizing $-x^2 + bx + c$.  
    Max value is at $x = b/2$ for $-x^2$? No.  
    Vertex x-coord: $-b/(2(-1)) = -(-5)/(-2)$?  
    Formula for vertex x in $ax^2+bx+c$ is $-b/2a$.  
    Here $a=-1, b=-5$.  
    $x = -(-5)/(2(-1)) = 5/-2 = -2.5$.  
    Max value is $y_{max} = c - b^2/4a$ (vertex formula for y).  
    $c=14, a=-1, b=-5$.  
    $y_{max} = 14 - (-5)^2 / (4(-1))$  
    $y_{max} = 14 - 25 / (-4)$  
    $y_{max} = 14 + 6.25$  
    $y_{max} = 20.25$.  
    Max value of original function is $4 \times y_{max} = 4 \times 20.25 = 81$.  

    Alternative approach: Inequality using AM-GM.  
    We have $-(x+7)(x-2)$. The product $(x+7)(x-2)$ would be easier, but we have a minus sign.  
    Let's look at the function again: $f(x) = 4(7+x)(2-x)$.  
    To use AM-GM directly on two terms like $(x+k)(l-k)$ usually requires the linear factors to sum to zero. Here we have $(x+7)$ and $(2-x)$. The product is $-1$. This suggests a trick involving splitting the term or using a parameter.  

    Let's try to substitute variables to make them conjugate or something?  
    We want to maximize $(x+7)(2-x)$.  
    Rewrite: $(2-x)^2$ doesn't help much.  
    Let's rewrite as $-(x^2 - 5x - 14)$ ? No, earlier I found it is $-x^2 - 5x + 14$.  
    So we want to maximize $- (x^2 + 5x - 14)$.  
    Completing square on inside: $x^2 + 5x - 14 = (x+2.5)^2 - 6.25 - 14 = (x+2.5)^2 - 20.25$.  
    So we want to maximize $- [ (x+2.5)^2 - 20.25 ] = 20.25 - (x+2.5)^2$.  
    This is clearly maximized when $(x+2.5)^2$ is minimized, i.e., equal to 0.  
    At $x = -2.5$, the max value is $20.25$.  
    The function is $4 \times 20.25 = 81$.  

    Is there any constraint on $x$? "over all real numbers x". So no domain restrictions.  

    Let me double check the arithmetic expansion one more time to be paranoid.  
    Original expression: $(x + 7)(2 - x)$  
    Term 1: $x \cdot 2 = 2x$.  
    Term 2: $x \cdot (-x) = -x^2$.  
    Term 3: $7 \cdot 2 = 14$.  
    Term 4: $7 \cdot (-x) = -7x$.  
    Sum: $-x^2 + (2x - 7x) + 14 = -x^2 - 5x + 14$.  
    Multiplied by 4: $-4x^2 - 20x + 56$.  

    Calculations for vertex of $-4x^2 - 20x + 56$:  
    Max at $x = \frac{-(-20)}{2(-4)} = \frac{20}{-8} = -2.5$. Correct.  
    Value at vertex: $y = -4(-2.5)^2 - 20(-2.5) + 56$  
    $(-2.5)^2 = 6.25$  
    $-4(6.25) = -25$  
    $-20(-2.5) = +50$  
    $56 + 50 - 25$  
    $106 - 25 = 81$.  

    Another check:  
    Let $x = -3$: $4(-3+7)(2-(-3)) = 4(4)(5) = 80$.  
    Let $x = -2.5$: $4(-2.5+7)(2-(-2.5)) = 4(4.5)(4.5) = 4 \times 20.25 = 81$.  
    Let $x = 0$: $4(7)(2) = 56$. (Wait, earlier calculation for x=0 gave 56? Yes).  
    Let $x = 3$: $4(3+7)(2-3) = 4(10)(-1) = -40$.  

    The logic holds.  
    The maximum value is 81.  

    **Structure of the step-by-step reasoning:**  
    1. Define the function $f(x) = 4(x + 7)(2 - x)$.  
    2. Expand the polynomial to identify it as a quadratic function $ax^2 + bx + c$.  
       $(x+7)(2-x) = -x^2 - 5x + 14$.  
       So $f(x) = -4x^2 - 20x + 56$.  
    3. Note that since the coefficient of $x^2$ is negative ($-4$), the parabola opens downwards, and the vertex represents the maximum point.  
    4. Calculate the x-coordinate of the vertex using the formula $x = -b / (2a)$.  
       $x = -(-20) / (2 \cdot (-4)) = 20 / (-8) = -2.5$.  
    5. Substitute $x = -2.5$ back into the function to find the maximum value.  
       Alternatively, use vertex formula $f(x_{vertex}) = c - b^2 / (4a)$? No, for vertex y-value directly.  
       Or simpler: $y = a(x-h)^2 + k$. Here we derived it was $-4(x+2.5)^2 + 81$.  
    6. State the maximum value clearly.  

    Is there an alternative method? AM-GM on specific terms.  
    We need to maximize $(x+7)(2-x)$.  
    Let $u = x+7$ and $v = -(x-2)$ ? No.  
    Look at $(x+7)(2-x) = (x+7)(2-x)$.  
    Notice that the terms add up to 0?  
    $(x+7) + (2-x) = 9 \neq 0$.  
    So direct AM-GM isn't applicable simply on these factors.  
    However, we can try:  
    $4(x+7)(2-x) = -4(x^2 - 5x + 14)$ -- no that was wrong sign in my head.  
    Let's re-verify expansion sign again.  
    $(x+7)(2-x)$.  
    If I group $(x+7)(2) - (x+7)x = 2x + 14 - x^2 - 7x = -x^2 - 5x + 14$. Correct.  

    What if we substitute $u = -x$? No need.  
    Let's stick to the algebraic expansion method as it is robust and easy to follow.  

    **Step-by-step derivation for final output:**  
    1.  Let $f(x) = 4(x + 7)(2 - x)$.  
    2.  First, expand the factors $(x + 7)$ and $(2 - x)$.  
        $$ (x + 7)(2 - x) = x(2) + x(-x) + 7(2) + 7(-x) $$  
        $$ = 2x - x^2 + 14 - 7x $$  
        $$ = -x^2 - 5x + 14 $$  
    3.  Substitute this back into the function definition:  
        $$ f(x) = 4(-x^2 - 5x + 14) $$  
        $$ f(x) = -4x^2 - 20x + 56 $$  
    4.  We have a quadratic function $f(x)$ with the form $ax^2 + bx + c$, where $a = -4$, $b = -20$, and $c = 56$. Since $a < 0$, the graph of $f(x)$ is an inverted parabola opening downwards. Therefore, the vertex corresponds to the global maximum value.  
    5.  Find the x-coordinate of the vertex ($x_v$) using the formula $x_v = -\frac{b}{2a}$.  
        $$ x_v = \frac{-(-20)}{2(-4)} $$  
        $$ x_v = \frac{20}{-8} $$  
        $$ x_v = -\frac{5}{2} = -2.5 $$  
    6.  Calculate the maximum value $y_v$ by substituting $x_v$ into the function. It's often helpful to factor out -4 first or just plug in.  
        Using factored form: $f(x) = -4(x^2 + 5x - 14)$ is not quite right...  
        Let's use vertex y-formula directly on $ax^2+bx+c$ with signs handled, or substitute values.  
        $$ f(-2.5) = -4(-2.5)^2 - 20(-2.5) + 56 $$  
        $$ (-2.5)^2 = 6.25 $$  
        $$ -4(6.25) = -25 $$  
        $$ -20(-2.5) = 50 $$  
        $$ f(-2.5) = -25 + 50 + 56 $$  
        $$ f(-2.5) = 25 + 56 $$  
        $$ f(-2.5) = 81 $$  
    7. The maximum value is 81.  

    Let's double check if I missed any subtleties. "Maximum value" vs "Max value of x". No, just the function value.  
    Is there a trick with inequalities?  
    Maybe $f(x) = -4(x^2 - 5x + 14)$?  
    $f(x) = -4(x - \frac{5}{2})^2 + C$?  
    $f(x) = -4 [ x^2 - 5x + 6.25 ] - 4[ 6.25 - 14 ]$ ?  
    Inside: $(x-2.5)^2$.  
    $x^2 - 5x + 6.25 = (x-2.5)^2$.  
    So $f(x) = -4 (x-2.5)^2 + ...$  
    We need to find the constant term.  
    From earlier: $f(x) = -4x^2 - 20x + 56$.  
    Completing square on $-4x^2 - 20x$:  
    $-4(x^2 + 5x)$  
    $= -4( (x+2.5)^2 - 6.25 )$  
    $= -4(x+2.5)^2 + 25$.  
    Add the constant from original function: $+ 56$.  
    Total max term: $25 + 56 = 81$.  
    So $f(x) = -4(x+2.5)^2 + 81$.  
    The maximum is indeed 81.  

    Just to be absolutely sure, let's look at the expression $(x+7)(2-x)$ again.  
    This looks like it might be related to maximizing a quadratic with roots $x=-7$ and $x=2$? No, that would be $a(x+7)(x-2)$.  
    Here we have $(x+7)(2-x) = -(x+7)(x-2)$.  
    So we are maximizing the negative of a quadratic with roots at -7 and 2.  
    The quadratic is $Q(x) = (x+7)(x-2) = x^2 + 5x - 14$.  
    Roots are $-7$ and $2$. The vertex x-coord for this parabola would be midpoint of roots? No, for $a=1$, yes.  
    Midpoint: $(-7+2)/2 = -2.5$.  
    Since the original expression is $4 \times [ -(x^2 + 5x - 14) ]$ ?  
    Let's check sign.  
    Original term: $(x+7)(2-x)$. This is $(x+7)[-(x-2)] = - (x+7)(x-2)$.  
    So $f(x) = 4 \times [ -Q(x) ]$ where $Q(x) = x^2 + 5x - 14$.  
    We know $Q(x)$ has a minimum at its vertex and goes to $+\infty$. So $-Q(x)$ goes to $-\infty$ and has a maximum.  
    The vertex of $Q(x) = x^2 + 5x - 14$ occurs at $x_v = \frac{-b}{2a} = \frac{-5}{2} = -2.5$.  
    The value of $Q(-2.5)$ is:  
    $(-2.5)^2 + 5(-2.5) - 14 = 6.25 - 12.5 - 14 = -8 - 8 = -14$? No.  
    $6.25 - 12.5 = -6.25$.  
    $-6.25 - 14 = -20.25$.  
    So $Q(-2.5) = -20.25$.  
    Then $f(-2.5) = 4 \times (-(-20.25)) = 4 \times (20.25) = 81$.  

    Calculation check:  
    $x^2 + 5x - 14$  
    Vertex x: -2.5.  
    $(x+2.5)^2 - 6.25 - 14 = (x+2.5)^2 - 20.25$.  
    Multiply by -4.  
    $-4 [ (x+2.5)^2 - 20.25 ]$  
    $= -4(x+2.5)^2 + 81$.  
    Yes, math is consistent across multiple derivations.  

    The question asks for the "maximum value".  
    Result: 81.  

    One final check on the question wording.  
    "over all real numbers x" -> defined everywhere. No domain restrictions (like $x < -5$). If it were restricted, I'd have to check boundaries. Since no restriction, the vertex is the answer.  


## Answer

To find the maximum value of the function $f(x) = 4(x + 7)(2 - x)$, we can follow these steps:  

**Step 1: Expand the polynomial expression.**  
First, multiply the factors $(x + 7)$ and $(2 - x)$.  
$$ (x + 7)(2 - x) = x(2) + x(-x) + 7(2) + 7(-x) $$  
$$ = 2x - x^2 + 14 - 7x $$  
Combine like terms:  
$$ = -x^2 + (2x - 7x) + 14 $$  
$$ = -x^2 - 5x + 14 $$  

**Step 2: Formulate the quadratic function.**  
Now, substitute this result back into the expression multiplied by 4 to get the full function $f(x)$ in the standard form $ax^2 + bx + c$:  
$$ f(x) = 4(-x^2 - 5x + 14) $$  
$$ f(x) = -4x^2 - 20x + 56 $$  

This is a quadratic function of the form $ax^2 + bx + c$, where:  
*   $a = -4$  
*   $b = -20$  
*   $c = 56$  

**Step 3: Determine if it opens up or down.**  
Since the coefficient $a = -4$ is negative, the parabola opens downwards. This means the vertex of the parabola corresponds to the maximum value on the real number line (assuming the function is defined for all real numbers, which it is).  

**Step 4: Find the vertex x-coordinate.**  
The x-coordinate of the vertex is given by $x = -\frac{b}{2a}$.  
$$ x = \frac{-(-20)}{2(-4)} $$  
$$ x = \frac{20}{-8} $$  
$$ x = -2.5 \quad \text{or} \quad -\frac{5}{2} $$  

**Step 5: Calculate the maximum value.**  
Substitute $x = -2.5$ back into the function to find the y-coordinate (the maximum value). It is also possible to use the vertex formula for a quadratic, which gives $\frac{c - b^2 / (4a)}$.  

Using substitution:  
$$ f(-2.5) = 4(-2.5 + 7)(2 - (-2.5)) $$  
$$ f(-2.5) = 4(4.5)(4.5) $$  
$$ f(-2.5) = 4(20.25) $$  
$$ f(-2.5) = 81 $$  

Alternatively, using the vertex formula directly for $f(x) = ax^2 + bx + c$:  
$$ \text{Max Value} = a x_{vertex}^2 + b x_{vertex} + c = c - \frac{b^2}{4a} \times (-4a)? $$ No, simpler to just calculate.  
$$ f(-\frac{5}{2}) = 56 - \frac{-20^2}{4(-4)} $$  
$$ = 56 - \frac{400}{-16} $$  
$$ = 56 + 25 $$  
$$ = 81 $$  

The maximum value is 81.  

\boxed{81}  
