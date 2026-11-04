# test/algebra/2064.json (Algebra, level 5)

> What is the maximum value of $4(x + 7)(2 - x)$, over all real numbers $x$?  

**Correct.** Gold `81`, predicted `81`. Finish: stop, 4725 tokens, 5 waits, 380.0 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's a thinking process that leads to the solution:  

1.  **Analyze the Problem:**  
The goal is to find the maximum value of the function $f(x) = 4(x + 7)(2 - x)$ for all real numbers $x$.  

2.  **Expand and Rewrite (Optional but helpful method):**  
    *   Let $y = 4(x + 7)(2 - x)$.  
    *   Expand the term $(x + 7)(2 - x)$:  
$$ (x + 7)(2 - x) = 2x - x^2 + 14 - 7x = -x^2 - 5x + 14 $$  
    *   Multiply by 4:  
$$ y = 4(-x^2 - 5x + 14) = -4x^2 - 20x + 56 $$  

3.  **Identify the Function Type:**  
The function is a quadratic of the form $ax^2 + bx + c$.  
    *   Here, $a = -4$, $b = -20$, and $c = 56$.  
    *   Since $a < 0$ ($-4$), this is a downward-opening parabola. Therefore, the vertex represents the global maximum (maximum value).  

4.  **Determine the Vertex Formula:**  
For a quadratic $ax^2 + bx + c$, the x-coordinate of the vertex is given by $x = \frac{-b}{2a}$.  
    *   $a = -4$  
    *   $b = -20$  
    *   $x_{vertex} = \frac{-(-20)}{2(-4)}$  
    *   $x_{vertex} = \frac{20}{-8}$  
    *   $x_{vertex} = -\frac{5}{2} = -2.5$  

*Self-Correction/Check:* This method works well if the function doesn't involve fractions, or if I use algebraic manipulation to avoid the vertex formula if I prefer. Let's try completing the square first, just to be sure.  

5.  **Alternative Method: Completing the Square (Vertex Form):**  
    *   Recall $f(x) = -4x^2 - 20x + 56$.  
    *   Factor out -4 from the quadratic terms:  
$$ f(x) = -4(x^2 + 5x - 14) $$ -- Wait, $56/-4 = 14$, not $-14$. Let's recheck.  
$$ -4x^2 - 20x + 56 = -4(x^2 + 5x - 14) $$ ... $4 \times (-14) = -56$. I have $+56$. So:  
$$ -4(x^2 + 5x - 14) \rightarrow -4(x^2 + 5x - 14) = -4x^2 - 20x + 56 $.  
        *   Let's check signs again. $-4( -14 ) = +56$. Correct.  
    *   Now complete the square inside the parenthesis.  
$$ x^2 + 5x $$ -> Take half of 5, which is $5/2$, square it to get $25/4$.  
So add and subtract $(25/4)$.  
    *   $$ -4 \left[ (x^2 + 5x + \frac{25}{4}) - \frac{25}{4} - 14 \right] $$  
    *   $$ -4 \left[ \left(x + \frac{5}{2}\right)^2 - \frac{25}{4} - \frac{56}{4} \right] $$  
$$ -4 \left[ \left(x + \frac{5}{2}\right)^2 - \frac{81}{4} \right] $$  
    *   Distribute the $-4$:  
$$ -4\left(x + \frac{5}{2}\right)^2 - 4\left(-\frac{81}{4}\right) $$  
    *   $$ -4\left(x + \frac{5}{2}\right)^2 + 81 $$  

6.  **Analyze the Resulting Expression:**  
The maximum value occurs when the squared term is zero (since it's multiplied by $-4$, which makes the graph peak).  
    *   Set $\left(x + \frac{5}{2}\right)^2 = 0$ -> $x = -2.5$.  
    *   Substitute back into the expression:  
$$ f(-2.5) = 81 $$  

7.  **Alternative Method: Algebraic Identity (AM-GM/Half-Area approach? Not directly applicable to one side without constraints). Let's try simply factoring.**  
Actually, looking at $4(x+7)(2-x)$ is a product of terms $(A+B)$ and $(C-D)$.  
This looks like finding the maximum value of a quadratic.  
Consider $f(x) = 4[(x+7)(2-x)]$ or just maximize the inner term first?  
The function is defined as $y = k \cdot u \cdot v$ where $k=4$.  
$u = x + 7$, $v = -(x - 2)$.  
Maximize $(x+7)(-x+2)$.  

Let's go back to the vertex formula for the product form directly:  
$(x+a)(c-x)$ is not quite it. It is $ax^2 + b$. Let's check standard max of product type $A(x-h_1)(k-x-h_2)$.  
The roots are at $x=-7$ (multiplicity 1? Wait, the expression is $4(x+7)(2-x)$).  
Roots are $-7$ and $2$.  
Since it's a parabola opening down, the maximum value occurs exactly halfway between the roots.  

*   Root 1: $x_1 = -7$  
    *   Root 2: $x_2 = 2$  
    *   Midpoint: $\frac{x_1 + x_2}{2} = \frac{-7 + 2}{2} = \frac{-5}{2}$ or $-2.5$.  

Let's check the max value calculation with this midpoint result.  
Substitute $x = -2.5$ into $4(x + 7)(2 - x)$.  
$f(-2.5) = 4(-2.5 + 7)(2 - (-2.5))$  
$f(-2.5) = 4(4.5)(2 + 2.5)$  
$f(-2.5) = 4(4.5)(4.5)$  
$f(-2.5) = 4 \times (4.5^2)$  
$4.5^2 = (9/2)^2 = 81/4 = 20.25$  
$f(-2.5) = 4 \times 20.25 = 81$.  

This seems consistent and robust. The "product of roots midpoint" trick is the most elegant for quadratic forms like $a(x-r_1)(x-r_2)$. But let's double check that logic.  
Is $(x+7)(2-x)$ a difference of terms $(A+B)(C-D)$?  
Let $u = x + 7$ and $v = -(x - 2)$. Then $v = -x + 2$.  
$uv = (x+7)(-x+2)$.  
The roots are $-7$ and $2$.  
Symmetry axis is indeed the midpoint.  

8.  **Final Verification:**  
Function: $f(x) = -4x^2 - 20x + 56$  
Vertex y-coordinate (max):  
Substitute $x = \frac{-b}{2a} = \frac{20}{-8} = -\frac{5}{2}$.  
$y = -4(\frac{-5}{2})^2 - 20(\frac{-5}{2}) + 56$  
$y = -4(\frac{25}{4}) + 100/1 + ...$? No.  
$-4(6.25) = -25$.  
$-20(-2.5) = +50$.  
Sum: $-25 + 50 + 56 = 25 + 56 = 81$.  

Calculation steps again to ensure arithmetic error:  
$x = -2.5$  
$(x+7) = 4.5$  
$(2-x) = 4.5$  
$4 \times 4.5 \times 4.5 = 4 \times 20.25$  
$4 \times 20 = 80$  
$4 \times 0.25 = 1$  
$80 + 1 = 81$.  

Is there any constraint? "over all real numbers x". So domain is $\mathbb{R}$. Parabola opens down, so max exists.  

9.  **Structuring the Output:**  
    *   State the function clearly.  
    *   Identify it as a quadratic function (in vertex form).  
    *   Determine the axis of symmetry or the roots to find the peak.  
    *   Calculate the coordinates using the formula $\frac{-b}{2a}$ for x-coordinate, and substitute back for y-value. Or complete the square. I will use completing the square as it is rigorous and easy to follow without relying on the "roots" intuition (though both are correct). Actually, identifying roots is faster here.  
    *   Method: Expand -> Identify $a$ vs $\Delta$.  
$(x+7)(2-x) = 2x - x^2 + 14 - 7x = -x^2 - 5x + 14$.  
Function = $-4x^2 - 20x + 56$.  
Vertex x = $\frac{-(-20)}{2(-4)} = -\frac{5}{2}$.  
Vertex y = $-4(-\frac{5}{2})^2 - 20(-\frac{5}{2}) + 56$  
$= -4(\frac{25}{4}) + 50 + 56$  
$= -25 + 106 = 81$.  

Let's double check the arithmetic $-4(25/4) + 50 + 56$.  
$-25 + 106$. No, $-4(-5)$?  
Let's re-evaluate term by term carefully.  
Term 1: $-4x^2$ at $x=-2.5 \rightarrow -4(6.25) = -25$.  
Term 2: $-20x$ at $x=-2.5 \rightarrow -20(-2.5) = +50$.  
Term 3: $+56$.  
Sum: $-25 + 50 + 56 = 81$.  

Calculation:  
$\frac{-b}{2a} = \frac{20}{-8} = -2.5$. Correct.  
$f(-2.5) = 4(-2.5 + 7)(2 - (-2.5))$  
$= 4(4.5)(4.5)$  
$= 4 \times 20.25$  
$= 81$.  

The question asks for the maximum value.  
Result is 81.  

Let's just quickly check boundaries or behavior. As $x \to \pm \infty$, $f(x) \to -\infty$ because of the negative coefficient of $x^2$. So the max is indeed the vertex.  

Steps for final response:  
1. Define function.  
   2. Expand to quadratic form.  
    3. Complete the square or use axis of symmetry formula.  
    4. Calculate value.  

Let's write out the steps clearly.  

Step 1: Simplify expression.  
$y = 4(x + 7)(2 - x)$  
Step 2: Expand the product part.  
$(x + 7)(2 - x) = 2x - x^2 + 14 - 7x = -x^2 - 5x + 14$.  
Multiply by 4:  
$y = -4x^2 - 20x + 56$.  
Step 3: Use the formula for the vertex of a parabola $ax^2 + bx + c$ to find $y_{max}$.  
The x-coordinate of the maximum is at $x = \frac{-b}{2a}$.  
Here, $a = -4$, $b = -20$.  
$x = \frac{-(-20)}{2(-4)} = \frac{20}{-8} = -\frac{5}{2} = -2.5$.  
Substitute $x = -2.5$ into the equation to find the maximum value.  
$y = -4(-2.5)^2 - 20(-2.5) + 56$  
$y = -4(6.25) + 50 + 56$  
$y = -25 + 106$  
$y = 81$.  

Alternatively, completing the square as shown in step 5:  
$-4(x^2 + 5x - 14)$ is incorrect... let me check that again.  
Wait. $f(x) = -4x^2 - 20x + 56$.  
Factor out -4: $-4(x^2 + 5x - 14)$.  
Inside the brackets, $(x + 5/2)^2 - (25/4)$.  
So $-4((x + 5/2)^2 - 25/4 - 14)$.  
$-4((x + 5/2)^2 - (25/4 + 56/4))$.  
$-4((x + 5/2)^2 - (81/4))$.  
$-4(x + 5/2)^2 + 4(81/4)$.  
$-4(x + 5/2)^2 + 81$.  
The max value is 81. This matches perfectly.  

I will write down the expansion and vertex method as it's standard and easy to follow. I will also mention the symmetry argument (midpoint of roots) for clarity. Roots are $-7$ and $2$, midpoint is $(-5)/2 = -2.5$.  
Max value is simply 81.  

One small detail: Is there any trick with absolute values? "Maximum value".  
If the function was just $(x+7)(2-x)$, max would be $81/4 = 20.25$. With the 4 multiplier, it's 81.  
Just a sanity check on the prompt. $4(x + 7)(2 - x)$. Real numbers. Done.  

Let's check if there is an AM-GM approach that yields this quickly.  
We want to maximize $P = (x+7)(2-x)$.  
This is product of two linear terms with different roots.  
Not a standard AM-GM form unless rewritten as difference of squares or something else?  
Usually, for sum-product problems with no constraints on sum/product, but here we have fixed numbers.  
Let $x+7 = A$, $2-x = B$. Then $A+B = -3$ is not true because $A+B = x+7 + 2-x = 9$.  
Ah! $A = x+7$ and $B = 2-x$. Sum is constant?  
$(x+7) + (2-x) = 9$. Yes.  
So we want to maximize the product of two numbers that sum to a constant (and are constrained by being real).  
However, they aren't independent. For example, $x=0 \implies A=7, B=2$, sum=9. Product=14.  
$(x+7)(2-x)$ is not bounded by AM-GM directly because AM-GM applies to non-negative numbers.  
Here we are finding max of $AB$ subject to $A+B = 9$.  
We know that for product of two numbers with a fixed sum, the product is maximized when the two numbers are equal (i.e., if we treat them as symmetric).  
So $x+7 = 2-x \implies 2x = -5 \implies x = -2.5$.  
Then product is $(4.5)(4.5) = 20.25$.  
Then multiply by the factor 4 to get $4(20.25) = 81$.  
This confirms the result without even explicitly calculating coefficients for quadratic, just using algebraic substitution properties. This is a nice confirmation.  

I will present the algebraic solution:  
1. Expand/Analyze as quadratic.  
   2. Find vertex.  
    3. Calculate max.  


## Answer

To find the maximum value of the function $f(x) = 4(x + 7)(2 - x)$ for all real numbers $x$, we can treat it as a quadratic equation and analyze its properties.  

**Step 1: Expand the expression**  
First, expand the product inside the parentheses:  
$$ (x + 7)(2 - x) $$  
Using the FOIL method or distribution:  
$$ = x(2) + x(-x) + 7(2) + 7(-x) $$  
$$ = 2x - x^2 + 14 - 7x $$  
$$ = -x^2 - 5x + 14 $$  

Now, multiply this result by the coefficient 4:  
$$ f(x) = 4(-x^2 - 5x + 14) $$  
$$ f(x) = -4x^2 - 20x + 56 $$  

**Step 2: Identify the properties of the parabola**  
The function is a quadratic of the form $f(x) = ax^2 + bx + c$, where:  
*   $a = -4$  
*   $b = -20$  
*   $c = 56$  

Since the coefficient of $x^2$ is negative ($a = -4 < 0$), the graph of this parabola opens downwards. This means the vertex represents the maximum point of the function.  

**Step 3: Find the coordinates of the vertex**  
The x-coordinate of the vertex, denoted as $x_{vertex}$, is given by the formula $\frac{-b}{2a}$.  
$$ x_{vertex} = \frac{-(-20)}{2(-4)} = \frac{20}{-8} = -\frac{5}{2} = -2.5 $$  

**Step 4: Calculate the maximum value**  
Substitute $x = -2.5$ back into the original equation to find the corresponding y-value (the maximum).  
Using the expanded form $f(x) = -4x^2 - 20x + 56$:  
$$ f(-2.5) = -4(-2.5)^2 - 20(-2.5) + 56 $$  

Calculate each term:  
1.  $(-2.5)^2 = 6.25$  
2.  $-4 \times 6.25 = -25$  
3.  $-20 \times (-2.5) = +50$  
4.  The constant is $56$.  

Combine them:  
$$ f(-2.5) = -25 + 50 + 56 $$  
$$ f(-2.5) = 25 + 56 $$  
$$ f(-2.5) = 81 $$  

Alternatively, you can use the sum-product property. We are maximizing $(x+7)(2-x)$. Let $u = x+7$ and $v = 2-x$. Then $u+v = (x+7)+(2-x) = 9$. For a product of two numbers with a constant sum to be maximized, the numbers must be equal.  
$x + 7 = 2 - x \Rightarrow 2x = -5 \Rightarrow x = -2.5$.  
Then $f(-2.5) = 4(4.5)(4.5) = 4(20.25) = 81$.  

\boxed{81}  
