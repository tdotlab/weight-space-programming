# test/algebra/2064.json (Algebra, level 5)

> What is the maximum value of $4(x + 7)(2 - x)$, over all real numbers $x$?  

**Correct.** Gold `81`, predicted `81`. Finish: stop, 6564 tokens, 5 waits, 679.4 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's a thinking process that leads to the solution:  

1.  **Analyze the Problem:**  
The goal is to find the maximum value of the function $f(x) = 4(x + 7)(2 - x)$ for all real numbers $x$.  

2.  **Expand the Function (Optional but helpful):**  
Let's expand the term inside the parenthesis first or just keep it factored as a quadratic form.  
$f(x) = 4(2x - x^2 + 14 - 7x)$  
$f(x) = 4(-x^2 - 5x + 14)$  
$f(x) = -4x^2 - 20x + 56$  

3.  **Identify the Type of Function:**  
This is a quadratic function in the form $ax^2 + bx + c$.  
Here, $a = -4$, $b = -20$, and $c = 56$.  
Since the coefficient of $x^2$ ($a$) is negative ($-4 < 0$), the parabola opens *downwards*.  
This means the function has a global maximum.  

4.  **Find the Vertex (Coordinate Form):**  
The vertex of a parabola $y = ax^2 + bx + c$ occurs at $x = -\frac{b}{2a}$.  

    *   Substitute values:  
$x = -\frac{-20}{2(-4)}$  
$x = \frac{20}{-8}$  
$x = -\frac{5}{2}$ or $-2.5$  

    *   Now, substitute this $x$ value back into the original function to find the $y$ (value of $f(x)$).  
Method A: Using the expanded form $f(x) = -4x^2 - 20x + 56$  
$f(-2.5) = -4(-2.5)^2 - 20(-2.5) + 56$  
$(-2.5)^2 = 6.25$  
$-4(6.25) = -25$  
$-20(-2.5) = 50$  
$f(x) = -25 + 50 + 56$  
$f(x) = 25 + 56$  
$f(x) = 81$  

Method B: Using the factored form $f(x) = 4(x+7)(2-x)$ (using algebraic manipulation)  
We want to maximize $(x+7)(2-x)$. Let's use a product-sum identity or check if there are integer roots for a substitution.  
Actually, let's expand $(x+7)(2-x)$ first again: $-x^2 - 5x + 14$.  
Complete the square?  
Multiply out: $-(x+7)(x-2) = -(x^2 + 5x - 14) = -x^2 - 5x + 14$... this is confusing.  
Let's stick to $(x+7)(2-x) = (x+7)(-(x-2)) = -(x+7)(x-2)$.  
Expand: $-(x^2 - 2x + 7x - 14) = -(x^2 + 5x - 14) = -x^2 - 5x + 14$.  

Let's rewrite the expression $y = (x+7)(2-x)$ in terms of $(x+3.5)^2$ or similar to see the vertex directly.  
$x = -2.5 = \frac{-5}{2}$.  
Term is $\left(x + 3.5\right)$ and $\left(2 - x\right)$.  
Note that $x + 7 = (x+3.5) + 3.5$ and $2-x = -(x-2)$. This doesn't look symmetric in the simplest way around the vertex unless we center it right there.  

Let's use a simpler geometric or algebraic approach to double-check.  
We want to maximize $(x+7)(2-x)$. This looks like finding the area of a rectangle with width $d$ or something? No.  
It is of the form $-(x^2 + 5x - 14)$. The maximum value of $-(x-a)(x+b)$ is when $x = -(a+b)/2$.  
Here, the product inside is $(x+7)(2-x)$. Let's call it $P$.  
To maximize $P$, we need to find the peak.  
The critical point calculation gave $x = -5/2$.  
So, substitute back:  
Value = $4(-5/2 + 7)(2 - (-5/2))$  
$= 4(3/2)(9/2)$  
$= 4 \cdot (1.5) \cdot (4.5)$  
$= 6 \cdot 4.5$  
$= 27$.  

**Wait**, let me re-calculate Method A vs Method B.  
Method A calculation: $f(-2.5) = -4(-2.5)^2 - 20(-2.5) + 56$  
$-4(6.25) = -25$.  
$+50$.  
$+56$.  
$-25 + 50 = 25$. $25 + 56 = 81$.  

Method B calculation: $x=-2.5$.  
Term inside: $(x+7)(2-x)$.  
$(-2.5 + 7) = 4.5$.  
$(2 - (-2.5)) = 4.5$.  
Product: $4.5 \times 4.5 = (9/2)^2 = 81/4 = 20.25$.  
Then multiply by 4 outside.  
$4 \times 20.25 = 81$.  

Why did I think Method B calculation was "6 * 4.5"? Ah, $27$ came from somewhere or I misread the step where I wrote 27 vs 81.  
Let's re-read method B line in thought process above: "$f(x) = 4 \cdot (1.5) \cdot (4.5)$ ... $= 27$".  
$1.5 \times 4.5$:  
$1 \times 10/8$ no... $3/2 \times 9/2 = 27/4$.  
Then multiply by 4: $4 \times (27/4) = 27$.  

**ERROR CHECK:**  
Let's re-calculate the expansion carefully.  
Expression: $(x+7)(2-x)$  
Let's check values at vertex. Vertex is where derivative is zero.  
$f(x) = 4(x^2 + 5x - 14)$ (Sign error in previous step).  
$(x+7)(2-x) = 2x - x^2 + 14 - 7x = -x^2 - 5x + 14$. Correct.  
So $f(x) = 4(-x^2 - 5x + 14) = -4x^2 - 20x + 56$. Correct.  
Vertex x-coordinate: $-b/(2a)$ for $y=-4x^2-20x+56$. $a=-4, b=-20$.  
$x = -(-20)/(2*-4) = 20 / -8 = -2.5$. Correct.  
Value: $f(-2.5) = -4(6.25) - 20(-2.5) + 56 = -25 + 50 + 56 = 81$. Correct.  

**Wait, let me re-evaluate the "Method B" check where I got confused.**  
$x = -2.5$.  
Term $(x+7) = 4.5$.  
Term $(2-x) = 4.5$.  
Product is $4.5 \times 4.5 = 20.25$.  
Multiply by 4: $4 \times 20.25 = 81$.  

Where did "6 * 4.5" come from?  
Ah, I calculated the product term $(x+7)(2-x)$ as $-x^2 - 5x + 14$.  
Maybe I confused coefficients in a quick mental check?  
Let's re-expand $(x+7)(2-x)$.  
First: $x \cdot 2 = 2x$.  
Second: $x \cdot (-x) = -x^2$.  
Third: $7 \cdot 2 = 14$.  
Fourth: $7 \cdot (-x) = -7x$.  
Sum: $-x^2 + (2x - 7x) + 14 = -x^2 - 5x + 14$.  

Let's check the substitution in Method A again.  
$f(x) = 4(-x^2 - 5x + 14)$.  
$a=-4, b=0$ (inside), c=14? No, the function is $-4(x+7)(x-2)$.  
The roots of $(x+7)(x-2)$ are $-7$ and $2$.  
The parabola passing through these with a vertical axis.  
Let's try to use AM-GM inequality or just standard quadratic properties directly without expanding if possible, though expansion is safest.  

**Method A re-check:**  
Maximize $(x+7)(2-x)$? No, maximize $4(x+7)(2-x)$.  
Let's treat $u = x + 7$. Then $x = u - 7$.  
Substitute into second part: $2 - (u-7) = 2 - u + 7 = 9 - u$.  
We want to maximize $4(u)(9-u) = 36u - 4u^2$.  
Vertex of parabola $36u - 4u^2$ occurs at $u = -b / (2a)$.  
$b=36, a=-4$.  
$u = -36 / (2*-4) = 36/8 = 4.5$.  
This corresponds to $x+7 = 4.5 \implies x = -2.5$.  
Now calculate the value of the function using $u$:  
Value $= 4(4.5)(9-4.5) = 4(4.5)(4.5)$.  
$4.5 \times 4.5 = 20.25$.  
$20.25 \times 4 = 81$.  

**Method A (Alternative calculation check):**  
Let's calculate using the vertex formula on the expanded polynomial again just to be absolutely sure I didn't mess up signs in the previous thought block.  
$f(x) = -4x^2 - 20x + 56$.  
$a = -4, b = -20$.  
Vertex $x = -(-20)/(2*-4) = 20/-8 = -2.5$.  
$f(-2.5) = -4( (-2.5)^2 ) - 20(-2.5) + 56$  
$= -4(6.25) + 50 + 56$  
$= -25 + 106$  
$= 81$.  

Is the question asking for *maximum* or minimum? "maximum value".  
The coefficient of $x^2$ is negative, so the parabola opens down, and there is a maximum.  
My calculations consistently give 81.  

5.  **Alternative Verification: AM-GM (or Cauchy-Schwarz)**  
We have $\max f(x) = 4 \cdot [(x+7)(2-x)]$.  
Let's try to express $(x+7)(2-x)$ as a difference of squares or sum.  
Notice $-(x^2 + 5x - 14) = -( (x+7)(x-2) )$. This is not helpful for AM-GM directly unless we shift variables.  
Let's rewrite the factor terms to look like sums of constants.  
We have $(x+7)$ and $(2-x)$. Note that $x+7 + 2 - x = 9$. The sum is constant (9).  
We want to maximize the product given a fixed sum of factors?  
Let $A = x+7$ and $B = 2-x$. Then $A+B = 9$.  
This looks like maximizing $4AB$ where $A+B=9$.  
For the product of two numbers with a constant sum to be maximized, the numbers must be equal.  
So set $A = B$.  
$x + 7 = 2 - x$  
$2x = -5$  
$x = -2.5$ (which matches our previous result).  
If $x = -2.5$, then:  
$A = -2.5 + 7 = 4.5$  
$B = 2 - (-2.5) = 4.5$  
Product $AB = 4.5 \times 4.5 = (9/2)^2 = 81/4$.  
The original expression is $4(AB)$.  
Value $= 4 \times (81/4) = 81$.  

This method (AM-GM applied to $(x+7)(2-x)$ where sum is constant) is much faster and confirms the result.  

6.  **Step-by-Step Formatting:**  
    *   State the function clearly.  
    *   Identify it as a quadratic (or apply AM-GM). Since the user asked for reasoning, showing the expansion or substitution leads to a quadratic vertex is standard. The substitution $A=B$ method is elegant but needs justification that max occurs when terms are equal (AM-GM). If I use just algebraic manipulation, expanding and finding the vertex of the parabola is more "step-by-step" without assuming knowledge of AM-GM conditions on general quadratics, though those apply to real numbers here.  
    *   Let's stick to the substitution method (A=B) or expansion method. The expansion method is less prone to "magic" logic if the user doesn't remember AM-GM for this specific structure immediately, but finding the vertex of $-4x^2$ is standard calculus/algebra.  
    *   Actually, looking at $f(x) = 4(x+7)(2-x)$:  
This is $-4(x - (-7))(x - 2)$.  
This is in the form $a(x-r_1)(x-r_2)$.  
The vertex of this parabola (with respect to $x$) is midway between roots $r_1$ and $r_2$.  
Midpoint of $-7$ and $2$ is $( -7 + 2 ) / 2 = -5/2 = -2.5$.  
The value at this midpoint:  
We need the y-value, which can be found by plugging in or completing the square.  
Completing the square on $f(x) = -4(x+7)(x-2)$? No, $(x+7)(x-2)$ is already there.  
Maximize $-(x^2 + 5x - 14)$.  
Vertex of $g(x) = x^2 + 5x$ is at $x = -5/2$.  
The max value of $g(x+7)(x-2)$? No.  
Let's look at $(x+7)(2-x) = -(x^2 + 5x - 14)$.  
Maximize $-( (x+3.5)^2 - (9/2)^2 - 14 )$?  
Expand: $- [ x^2 + 5x + 12.25 - \text{shifted term} ]$.  
Let's just use the vertex form directly on the expression inside the parenthesis to avoid sign errors, but we already did that.  

**Let's write out the steps for the final response:**  
1.  Define $y = 4(x+7)(2-x)$.  
    2.  Identify the quadratic structure or set up the vertex formula.  
    3.  Using vertex formula: The quadratic function is $y = -4x^2 - 20x + 56$ (after expansion).  
    4.  Find axis of symmetry ($x = -b/2a$).  
    5.  Calculate the maximum value by substituting the x-value back into the equation.  
    6.  Alternatively, note that $-(x^2 + 5x - 14)$ is maximized when $|x^2 + 5x - 14|$ is minimized (if looking for min/max). Since leading coeff is negative, it's a downward opening parabola, max is at the peak.  
    7.  Use AM-GM on the product $(x+7)(2-x)$. The sum is constant ($9$). Max product occurs when factors are equal ($x+7 = 2-x$).  
    8.  Solve for $x$, find $y$.  

I will provide the substitution/vertex method as it's more universally understood, perhaps mentioning the sum of factors trick as a nice observation or just doing the vertex calculation cleanly. Vertex calculation is robust.  

Calculation check:  
$f(x) = -4x^2 - 20x + 56$  
$x = -5/2 = -2.5$  
$f(-2.5) = -4(6.25) - 20(-2.5) + 56$  
$= -25 + 50 + 56$  
$= 81$.  

Is there any domain constraint? "over all real numbers x". No constraints.  
So, max value is 81.  

Double check for silly arithmetic errors.  
$2^2 = 4$.  
$-4 \times 6.25$:  
$6.25 = 25/4$.  
$-4 \times (25/4) = -25$. Correct.  
$-20 \times (-2.5)$:  
$= 20 \times 2.5 = 50$. Correct.  
$56$ is constant term.  
$-25 + 50 + 56 = 81$. Correct.  

Final Answer seems solid.  

One more check on the prompt: "What is the maximum value of $4(x + 7)(2 - x)$".  
Does it imply an algebraic expression or a specific number? "maximum value" implies a number.  
If $x$ was restricted to integers, it would be different, but it says "real numbers". So continuous max exists and is found at the vertex.  

Let's re-read the term $(2-x)$.  
$4(x+7)(2-x)$.  
Let $a = x+7 \implies x = a-7$.  
Expression: $4(a)(2-(a-7)) = 4a(2-a+7) = 4a(9-a) = 36a - 4a^2$.  
Maximize $P(a) = -4a^2 + 36a$.  
Vertex at $a = -36 / (2*-4) = 4.5$.  
Value $= 36(4.5) - 4(4.5)^2$  
$= 4(9)(4.5) - 4(4.5)^2$  
$= 4(4.5)(4.5) = 81$.  

The logic holds up from multiple angles.  

**Structure of the explanation:**  
1. Expand the expression to get a quadratic function in terms of $x$.  
   2. Identify coefficients ($a, b, c$).  
    3. Determine the vertex coordinate (for real max) using $-b/2a$.  
    4. Calculate the value of the function at that $x$.  
    5. Alternatively (optional for brevity), use the property that a product $xy$ is maximized when $y=x$ given $x+y=K$ (AM-GM). This yields $(x+7)(2-x)$ sum is $9$, so max when $x+7 = 2-x$.  
    6. Both methods yield 81. I'll write down the AM-GM method or the vertex method? Vertex method is standard "Algebra" way, AM-GM is "Calculus-lite". I will provide the vertex method as primary since it requires fewer "insights" and more direct substitution logic.  

Let's draft the steps clearly.  
$f(x) = 4(x + 7)(2 - x)$  
Expand:  
$f(x) = 4(2x - x^2 + 14 - 7x)$  
$f(x) = 4(-x^2 - 5x + 14)$  
$f(x) = -4x^2 - 20x + 56$  

Quadratic form: $ax^2 + bx + c$ with $a=-4, b=-20$.  
Vertex $x = -b/2a = 20 / -8 = -5/2 = -2.5$.  
Substitute $x = -2.5$:  
$f(-2.5) = 4(-2.5 + 7)(2 - (-2.5))$  
$f(-2.5) = 4(4.5)(4.5)$  
$= 4 \times 20.25$  
$= 81$.  

Looks good.  

One tiny detail:  
The term inside the parenthesis is $(x+7)(2-x)$.  
Can we write it as $(x + (7-2)) (x - (-7))? No.  
Can we write as $(x - (-7)) (-(x - 2))$? Yes.  
$= -(x^2 + 5x - 14)$.  
Completing square for $x^2+5x-14$:  
$x^2+5x = (x+5/2)^2 - 25/4$.  
So expression is $-( [ (x+5/2)^2 - 25/4 - 14 ] )$  
$= - (x+5/2)^2 + 6.25 + 14$ -- wait.  
Let's check the constant again.  
$-14 = -56/4$.  
$+25/4 - (-56/4) = 25/4 + 112/4$? No.  
Constant term in $(x+7)(2-x)$ is $-(7 \times 2) - (2(-7)+(-7)(-2))?$ No, that's for product of differences from roots.  
Let's just trust the constant calculation: $-(x^2 + 5x - 14)$.  
If we complete square on $x^2+5x$:  
Add $5/2$, subtract $(5/2)^2 = 25/4$.  
So $x^2+5x = (x+2.5)^2 - 6.25$.  
Substitute back: $-( (x+2.5)^2 - 6.25 - 14 )$  
$= -(x+2.5)^2 + 6.25 + 14$  
$= -(x+2.5)^2 + 20.25$.  
Now multiply by the outer factor 4:  
$f(x) = 4 [ - (x+2.5)^2 + 20.25 ]$  
$f(x) = -4(x+2.5)^2 + 4(20.25)$  
$f(x) = -4(x+2.5)^2 + 81$.  
The maximum value is clearly when the squared term is 0 (since coefficient is negative).  
Max = 81.  

This confirms the result again with a slightly different arithmetic path.  

Final check of the question text: "maximum value". "real numbers x".  
Everything seems aligned.  

The thinking process is complete. I will structure the answer based on expanding the expression to form a standard quadratic function, finding its vertex, and substituting back to find the maximum y-value. This is the most robust method for explaining it. I'll also briefly mention the AM-GM logic as an elegant alternative.  

Step 1: Expand.  
Step 2: Identify parabola type ($a<0$, opens down -> max).  
Step 3: Calculate vertex $x$ and value $y$.  
Step 4: Conclude answer.  

Result is 81.  


## Answer

To find the maximum value of the function $f(x) = 4(x + 7)(2 - x)$ for all real numbers $x$, we can expand the expression into a quadratic equation and analyze its properties, or use algebraic manipulation to simplify it.  

**Method 1: Algebraic Expansion and Quadratic Vertex**  

1.  **Expand the term:**  
First, multiply the binomials inside the parentheses:  
$$ (x + 7)(2 - x) = x(2 - x) + 7(2 - x) $$  
$$ = 2x - x^2 + 14 - 7x $$  
Combine like terms ($2x$ and $-7x$, and the constant term):  
$$ = -x^2 - 5x + 14 $$  

2.  **Form the function:**  
Multiply by the coefficient $4$:  
$$ f(x) = 4(-x^2 - 5x + 14) $$  
$$ f(x) = -4x^2 - 20x + 56 $$  
This is a quadratic function in the standard form $ax^2 + bx + c$.  

3.  **Analyze the graph:**  
The coefficient of $x^2$ is $a = -4$, which is negative. Therefore, the parabola opens downwards, meaning it has a global maximum at its vertex.  

4.  **Find the x-coordinate of the vertex:**  
The x-coordinate of the vertex for a quadratic $ax^2 + bx + c$ is given by the formula $x = -\frac{b}{2a}$.  
Here, $a = -4$ and $b = -20$.  
$$ x = -\frac{-20}{2(-4)} = \frac{20}{-8} = -\frac{5}{2} = -2.5 $$  

5.  **Find the maximum value:**  
Substitute $x = -2.5$ back into the expanded function (or the original factored form) to find the maximum value.  

Using the expanded form:  
$$ f(-2.5) = -4(-2.5)^2 - 20(-2.5) + 56 $$  
$$ f(-2.5) = -4(6.25) + 50 + 56 $$  
$$ f(-2.5) = -25 + 50 + 56 $$  
$$ f(-2.5) = 25 + 56 $$  
$$ f(-2.5) = 81 $$  

**Method 2: Using the AM-GM Inequality**  
We want to maximize $4(x+7)(2-x)$. Let's focus on maximizing the product $(x+7)(2-x)$.  
Notice that the sum of these two factors is constant:  
$$ (x+7) + (2-x) = 9 $$  
For a product of two numbers with a fixed positive sum to be maximized, the numbers must be equal.  
So, set $x+7 = 2-x$. Solving for $x$:  
$$ 2x = -5 \implies x = -2.5 $$  
The maximum value of the product is $(4.5)(4.5) = 20.25$.  
Multiply by the coefficient 4:  
$$ 4 \times 20.25 = 81 $$  

Both methods yield the same result.  

\boxed{81}  
