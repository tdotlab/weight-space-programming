# test/algebra/2064.json (Algebra, level 5)

> What is the maximum value of $4(x + 7)(2 - x)$, over all real numbers $x$?  

**Correct.** Gold `81`, predicted `81`. Finish: stop, 2545 tokens, 0 waits, 201.5 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's a thinking process that leads to the solution:  

1.  **Analyze the Problem:**  
The goal is to find the maximum value of the function $f(x) = 4(x + 7)(2 - x)$ for all real numbers $x$.  

2.  **Expand the Function (Optional but helpful):**  
Let's expand the term inside the parenthesis first or just keep it factored as a quadratic in form.  
$f(x) = 4(x + 7)(2 - x)$  

Let's expand $(x+7)(2-x)$:  
$(x+7)(2-x) = x(2) + x(-x) + 7(2) + 7(-x)$  
$= 2x - x^2 + 14 - 7x$  
$= -x^2 - 5x + 14$  

So, $f(x) = 4(-x^2 - 5x + 14)$  
$f(x) = -4x^2 - 20x + 56$  

3.  **Identify the Type of Function:**  
The expression $-4x^2 - 20x + 56$ is a quadratic function in the form $ax^2 + bx + c$.  
Here, $a = -4$, $b = -20$, and $c = 56$.  

Since $a < 0$ (specifically $-4$), the parabola opens *downwards*. This means the function has a global maximum.  

4.  **Find the Vertex of the Parabola:**  
The $x$-coordinate of the vertex of a parabola $y = ax^2 + bx + c$ is given by $x = \frac{-b}{2a}$.  

Substitute the values:  
$x = \frac{-(-20)}{2(-4)}$  
$x = \frac{20}{-8}$  
$x = -\frac{20}{8}$  
$x = -\frac{5}{2}$ or $-2.5$  

5.  **Calculate the Maximum Value:**  
Now that we have the $x$-value, plug it back into the original function (or the expanded version) to find the maximum value ($f(-2.5)$).  

*Method 1: Using the original factored form*  
$f(x) = 4(x + 7)(2 - x)$  
$x = -2.5$  
$x + 7 = -2.5 + 7 = 4.5 = \frac{9}{2}$  
$2 - x = 2 - (-2.5) = 2 + 2.5 = 4.5 = \frac{9}{2}$  
$f(-2.5) = 4 \cdot (4.5) \cdot (4.5)$  
$f(-2.5) = 4 \cdot \left(\frac{9}{2}\right) \cdot \left(\frac{9}{2}\right)$  
$f(-2.5) = 4 \cdot \frac{81}{4}$  
$f(-2.5) = 81$  

*Method 2: Using the expanded form*  
$f(x) = -4x^2 - 20x + 56$  
Substitute $x = -\frac{5}{2}$:  
$x^2 = \left(-\frac{5}{2}\right)^2 = \frac{25}{4}$  
$-4x^2 = -4 \cdot \frac{25}{4} = -25$  
$-20x = -20 \cdot \left(-\frac{5}{2}\right) = 10 \cdot 5 = 50$  
Constant term: $56$  
Sum: $-25 + 50 + 56$  
$f(x) = 25 + 56$  
$f(x) = 81$  

6.  **Verify the logic:**  
    - Function is a product of linear terms, so it behaves like a quadratic with one positive factor in parentheses and one negative. $(x+7)$ goes up then down, $(2-x)$ goes down then up. They meet at $x=-7$ and $x=2$. The max should be between these points. $x = \frac{(-7) + 2}{-1} = \dots$ No, standard vertex formula check.  
    - Let's look at the factors: $4 \cdot (x+7)(2-x)$.  
    - This is $4(-(x^2 - 5x - 14))$. Max occurs when terms are balanced in magnitude but opposite signs? No.  
    - Look at the shape again. It's an inverted "U". The vertex is between $x = -7$ and $x = 2$ because the roots (zeros) of the expression $(x+7)(2-x)=0$ are $-7$ and $2$. Since it opens down, the maximum must be strictly inside $(-7, 2)$.  
    - Distance from center to vertex is determined by vertex formula. The "center" logic works like finding the max of a distance problem where one term increases linearly and the other decreases linearly.  
    - Vertex calculation: $\frac{a+b+c}{...}$ No, just use algebraic formulas. It's robust.  

7.  **Final Formatting:**  
    - State the function clearly.  
    - Expand (optional but shows understanding).  
    - Determine it's a quadratic opening downwards.  
    - Find vertex $x$.  
    - Calculate max value.  
    - Box the final answer.  

8.  **Alternative Geometric/Completing Square approach:**  
$f(x) = -4(x^2 + 5x) + 56$  
$f(x) = -4(x^2 + 5x + \frac{25}{4} - \frac{25}{4}) + 56$  
$f(x) = -4((x + \frac{5}{2})^2 - \frac{25}{4}) + 56$  
$f(x) = -4(x + \frac{5}{2})^2 + (-4)(-\frac{25}{4}) + 56$  
$f(x) = -4(x + \frac{5}{2})^2 + 25 + 56$  
$f(x) = -4(x + \frac{5}{2})^2 + 81$  
Max value occurs when squared term is 0.  
Result: $81$.  

This confirms the previous calculation perfectly.  

9.  **Construct the final response.**  
    *   Step 1: Write function $f(x) = 4(x+7)(2-x)$.  
    *   Step 2: Expand to see it's a quadratic. $f(x) = -4x^2 - 20x + 56$.  
    *   Step 3: Identify $a=-4$ (opens down), so max exists.  
    *   Step 4: Find vertex x-coordinate $x = -(-20)/(2*-4) = -20/-8$? No, $2*(-4) = -8$. $x = 20 / (-8) = -2.5$.  
    *   Step 5: Substitute back to find max. $4(4.5)(4.5) = 81$.  

Let's recheck the sign in step 5 logic.  
Vertex formula check again: $x = \frac{-b}{2a}$.  
Here $f(x) = -4x^2 - 20x + 56$.  
$a = -4, b = -20$.  
$x = -(-20)/(2*-4) = 20/(-8) = -5/2$. Correct.  
Calculation: $f(-5/2) = -4(25/4) - 20(-5/2) + 56 = -25 + 50 + 56 = 81$. Correct.  

Double check the question text: "maximum value". Yes. "over all real numbers x". Yes.  

Ready to write output.  


## Answer

To find the maximum value of the function $f(x) = 4(x + 7)(2 - x)$ over all real numbers $x$, we can follow these steps:  

**Step 1: Expand the expression.**  
The given expression is a product of two linear terms. Let's first expand the binomials inside the parentheses.  
$$ (x + 7)(2 - x) = x(2 - x) + 7(2 - x) $$  
$$ = 2x - x^2 + 14 - 7x $$  
$$ = -x^2 - 5x + 14 $$  

Now, multiply this result by the constant factor of 4:  
$$ f(x) = 4(-x^2 - 5x + 14) $$  
$$ f(x) = -4x^2 - 20x + 56 $$  

**Step 2: Identify the nature of the function.**  
The function $f(x)$ is a quadratic equation in the form $ax^2 + bx + c$, where $a = -4$, $b = -20$, and $c = 56$. Since the coefficient of $x^2$ ($a$) is negative (-4), the parabola opens downwards. This means the function has a maximum value at its vertex.  

**Step 3: Find the x-coordinate of the vertex.**  
The x-coordinate of the vertex for a quadratic equation $ax^2 + bx + c$ is given by the formula:  
$$ x = \frac{-b}{2a} $$  
Substitute the values of $a$ and $b$:  
$$ x = \frac{-(-20)}{2(-4)} $$  
$$ x = \frac{20}{-8} $$  
$$ x = -\frac{5}{2} $$ (or -2.5)  

**Step 4: Calculate the maximum value.**  
Substitute $x = -2.5$ back into the function to find the maximum value:  
$$ f(-2.5) = 4(-2.5 + 7)(2 - (-2.5)) $$  
$$ f(-2.5) = 4(4.5)(4.5) $$  
$$ f(-2.5) = 4 \times (4.5)^2 $$  
$$ f(-2.5) = 4 \times 20.25 $$  
$$ f(-2.5) = 81 $$  

Alternatively, using the expanded form:  
$$ f(-\frac{5}{2}) = -4\left(-\frac{5}{2}\right)^2 - 20\left(-\frac{5}{2}\right) + 56 $$  
$$ = -4\left(\frac{25}{4}\right) + 50 + 56 $$  
$$ = -25 + 50 + 56 $$  
$$ = 81 $$  

The maximum value is 81.  

\boxed{81}  
