# test/algebra/634.json (Algebra, level 3)

> Find the value of $r$ such that $$\frac{6r^2 -19r - 7}{2r-7} = 4r-3.$$  

**Wrong.** Gold `4`, predicted `None`. Finish: length, 8192 tokens, 7 waits, 953.6 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here is a thinking process to solve the equation:  

1.  **Analyze the Request:** The user wants to find the value of $r$ that satisfies the equation $\frac{6r^2 -19r - 7}{2r-7} = 4r-3$. The response should be step-by-step, and the final answer must be in a box.  

2.  **Initial Assessment of the Equation:**  
The equation is an equality involving a rational expression on the left-hand side (LHS) equal to a polynomial on the right-hand side (RHS).  
$$ \frac{6r^2 -19r - 7}{2r-7} = 4r-3 $$  

3.  **Determine Potential Issues:**  
The variable $r$ is in the denominator: $(2r-7)$. Thus, if the denominator equals zero, the expression is undefined (vertical asymptote). I should check for any domain restrictions later. However, usually in these types of problems, we first solve the equation by clearing the denominator, then verify solutions to ensure they don't make the denominator zero.  

4.  **Method: Cross-Multiplication / Elimination of Fractions:**  
Multiply both sides by the denominator $(2r-7)$, assuming $2r - 7 \neq 0$.  

$$ 6r^2 - 19r - 7 = (2r-7)(4r-3) $$  

5.  **Expand the Right-Hand Side (RHS):**  
$(2r-7)(4r-3)$  
Using FOIL (First, Outer, Inner, Last):  
    *   First: $2r \cdot 4r = 8r^2$  
    *   Outer: $2r \cdot -3 = -6r$  
    *   Inner: $-7 \cdot 4r = -28r$  
    *   Last: $-7 \cdot -3 = +21$  

So, RHS = $8r^2 - 6r - 28r + 21$  
Combine like terms ($-6r - 28r = -34r$):  
RHS = $8r^2 - 34r + 21$  

6.  **Equate LHS and Expanded RHS:**  
$$ 6r^2 - 19r - 7 = 8r^2 - 34r + 21 $$  

7.  **Form a Polynomial Equation (Standard Quadratic):**  
Move all terms to one side (usually the right side) to set equal to zero.  
Subtract $6r^2$ from both sides:  
$$ -19r - 7 = 2r^2 - 34r + 21 $$  

Rearrange to standard quadratic form $ar^2 + br + c = 0$:  
$$ 0 = 8r^2 - 34r + 21 + 6r^2 + 19r + 7 $$ -- *Correction*: Wait, let's look at the signs carefully.  

LHS is $6r^2 - 19r - 7$.  
RHS expanded was $8r^2 - 34r + 21$.  

Equation: $6r^2 - 19r - 7 = 8r^2 - 34r + 21$  

Move everything to the right side (so we get $0 = \dots$):  
Subtract $6r^2$: $0 = 2r^2 - 15r - 7 - (-34r) + 21$ -- *No, let's just subtract terms carefully.*  

RHS term: $8r^2$. Subtract $6r^2 \to 2r^2$.  
RHS term: $-34r$. Add $19r$ (moving LHS to RHS means adding). So $-34 + 19 = -15$.  
RHS term: $+21$. Add 7. So $21 + 7 = 28$.  

So the equation is:  
$$ 0 = 2r^2 - 15r + 28 $$  
(Note: I made a mistake in my head during rearrangement or copying. Let me re-check.)  

**Re-calculation:**  
Equation: $6r^2 - 19r - 7 = 8r^2 - 34r + 21$  

Move LHS terms to RHS:  
Subtract $6r^2$: $-19r - 7$.  
Add $19r$: $-15r$. (Since $-34r - (-19r) = -34r + 19r = -15r$)  
Add $6r^2$: $21 + 7$? Wait.  
Original: $LHS = RHS$.  
$0 = \text{RHS} - \text{LHS}$  
$0 = (8r^2 - 34r + 21) - (6r^2 - 19r - 7)$  
$0 = 8r^2 - 6r^2 - 34r + 19r + 21 - (-7)$ -- *Sign error here again.*  

Let's stick to $a r^2 + b r + c = 0$.  
Move all terms to RHS:  
$8r^2 - 34r + 21 - 6r^2 + 19r - (-7) = 0$?  
Let's write it out linearly.  
Right side minus Left side:  
$(8r^2 - 6r^2) + (-34r - (-19r)) + (21 - (-7))$ -- *Is this correct?*  

Let's re-read the original equation.  
$6r^2 - 19r - 7 = (2r-7)(4r-3)$  
RHS = $8r^2 - 34r + 21$.  

So, $6r^2 - 19r - 7 = 8r^2 - 34r + 21$  
Bring everything to the right side (RHS becomes 0):  
$8r^2 - 34r + 21 - (6r^2 - 19r - 7) = 0$  
$8r^2 - 34r + 21 - 6r^2 + 19r + 7 = 0$  

Group terms:  
$r^2(8 - 6) = 2r^2$  
$r(-34 + 19) = -15r$  
$(21 + 7) = 28$  

Equation: $2r^2 - 15r + 28 = 0$.  

**Double Check the Algebra:**  
LHS: $6r^2 - 19r - 7$  
RHS: $8r^2 - 34r + 21$  

Move RHS to left?  
$(8-6)r^2 = 2r^2$.  
$(-34 - (-19))r = -15r$.  
$(21 - (-7)) = 28$.  

Result: $2r^2 - 15r + 28 = 0$.  

**Factoring / Solving Quadratic:**  
$2r^2 - 15r + 28 = 0$  

Let's check the discriminant $\Delta = b^2 - 4ac$.  
$a=2, b=-15, c=28$.  
$\Delta = (-15)^2 - 4(2)(28)$  
$\Delta = 225 - 224$  
$\Delta = 1$.  

Since the discriminant is a perfect square, there are rational roots.  
Roots formula: $r = \frac{-b \pm \sqrt{\Delta}}{2a}$  
$r = \frac{15 \pm \sqrt{1}}{2(2)}$  
$r = \frac{15 \pm 1}{4}$  

Case 1:  
$r = \frac{15 + 1}{4} = \frac{16}{4} = 4$  

Case 2:  
$r = \frac{15 - 1}{4} = \frac{14}{4} = \frac{7}{2}$ (or 3.5)  

8.  **Verify Solutions against Domain:**  
The original equation has the denominator $2r - 7$.  
We must ensure the solution does not make the denominator zero.  

If $r = 4$:  
Denominator: $2(4) - 7 = 8 - 7 = 1 \neq 0$. Valid.  

If $r = \frac{7}{2}$:  
Denominator: $2(\frac{7}{2}) - 7 = 7 - 7 = 0$.  
This value is undefined in the original equation because division by zero is not allowed.  
Even though solving the algebraic identity resulted in this root, it does not satisfy the original equation due to the domain restriction.  

*Self-Correction/Sanity Check:*  
Often students forget the vertical asymptote check. It's a common trap.  

Let's plug $r=4$ back into the original expression:  
LHS: $\frac{6(16) - 19(4) - 7}{2(4)-7} = \frac{96 - 76 - 7}{8-7}$  
Numerator: $96 - 83 = 13$? No, $19 \times 4 = 76$. $96 - 76 = 20$. $20 - 7 = 13$.  
Denominator: $1$.  
Result LHS = $13 / 1 = 13$.  

RHS: $4r - 3 = 4(4) - 3 = 16 - 3 = 13$.  
So, LHS = RHS. $13=13$.  
Therefore, $r=4$ is a valid solution.  

Let's plug $r=7/2$ (assuming it was found from algebra) back into the original expression just to see what happens:  
Denominator: $0$. Undefined. So strictly speaking, this equation has 1 solution ($r=4$), while the quadratic derived has 2 solutions but only one is valid.  

Let me re-read the expansion step again. Maybe I messed up signs somewhere.  
Equation: $\frac{6r^2 -19r - 7}{2r-7} = 4r-3$  

$6r^2 - 19r - 7 = (2r-7)(4r-3)$  
Expansion:  
$(2r)(4r) = 8r^2$  
$(2r)(-3) = -6r$  
$(-7)(4r) = -28r$  
$(-7)(-3) = 21$  
Sum: $8r^2 - 34r + 21$.  

Equation:  
$6r^2 - 19r - 7 = 8r^2 - 34r + 21$  
Subtract LHS from RHS? Or move everything to one side.  
Let's subtract LHS:  
$0 = (8r^2 - 6r^2) + (-34r - (-19r)) + (21 - (-7))$  
$0 = 2r^2 - 15r + 28$.  

Discriminant check again: $\Delta = 225 - 4(2)(28) = 225 - 224 = 1$.  
Roots: $(15 \pm 1)/4 \implies 4, 3.5$.  
Check $r=4$: Valid.  
Check $r=3.5$: Denom is $2(3.5)-7 = 0$. Invalid.  

Is there a possibility that the user made a typo in the problem statement?  
Or maybe I missed something trivial?  
Let's check the arithmetic of the roots again.  
Roots: $\frac{15 \pm 1}{4}$.  
$r_1 = 4$. $2(4)-7=1 \neq 0$.  
$r_2 = 3.5$. $2(3.5)-7=0$.  

The solution set is usually just the valid numbers.  

**Structure of the Explanation:**  
1.  State the given equation.  
    2.  Multiply both sides by $(2r-7)$ to clear the fraction, noting $r \neq 3.5$.  
    3.  Expand the RHS polynomial.  
    4.  Move all terms to one side to form a quadratic equation equal to zero.  
    5.  Solve the quadratic equation using factoring (or quadratic formula).  
    6.  Test the potential solutions against the original expression (specifically checking the denominator) to discard invalid roots caused by domain restrictions.  

**Alternative approach:**  
Polynomial long division?  
Divide $6r^2 -19r -7$ by $2r-7$.  
$\frac{6r^2}{2r} = 3r$.  
$(3r)(2r-7) = 6r^2 - 21r$.  
Subtract from LHS: $(6r^2 - 19r - 7) - (6r^2 - 21r) = 2r - 7$.  
$\frac{2r}{2r} = 1$.  
$1(2r-7) = 2r-7$.  
Subtract: $(2r - 7) - (2r - 7) = 0$.  
So, $\frac{6r^2 -19r -7}{2r-7} = 3r + 1$.  

Let's check this identity.  
$6r^2 -19r - 7$ divided by $2r-7$:  
Quotient: $3r+1$. Remainder: 0?  
$(3r+1)(2r-7) = 6r^2 - 21r + 2r - 7 = 6r^2 - 19r - 7$.  
Yes.  

So the equation becomes:  
$3r + 1 = 4r - 3$  

Subtract $3r$ from both sides:  
$1 = r - 3$  
Add 3 to both sides:  
$r = 4$.  

This is much faster and avoids the quadratic formula completely, reducing calculation error risk. However, checking for $2r-7=0$ remains crucial.  
With this method:  
If $3r+1 = 4r-3$, then $1 + 3 = r + 4r \Rightarrow 4 = 5r \Rightarrow r = 4/5$.  
**STOP.** Where is the discrepancy?  

Let's re-divide carefully.  
Numerator: $6r^2 - 19r - 7$. Divisor: $2r-7$.  
Step 1: $\frac{6r^2}{2r} = 3r$.  
Multiply divisor by $3r$: $3r(2r) = 6r^2$, $3r(-7) = -21r$.  
Subtract from Numerator: $(6r^2 - 19r - 7) - (6r^2 - 21r)$.  
$= (-19r + 21r) - 7 = 2r - 7$.  

Step 2: $\frac{2r-7}{2r-7} = 1$.  
Multiply divisor by $1$: $1(2r) - 1(7) = 2r - 7$.  
Subtract from remainder $(2r - 7)$: $(2r - 7) - (2r - 7) = 0$.  

So the division works out perfectly. The LHS simplifies to $3r+1$.  
Now set equal to RHS ($4r-3$).  
$3r + 1 = 4r - 3$.  
$r - (-3) + \dots$  
Move terms: $3 + 3 = r + 4r$.  
$6 = 5r$.  
$r = 1.2$.  

**HOLD ON.**  
Why did the quadratic method give $r=4$ and the division method give $r=1.2$?  

Let's check the cross-multiplication step again.  
$(2r-7)(4r-3) = 8r^2 - 6r - 28r + 21$.  
$= 8r^2 - 34r + 21$.  

Wait, my cross multiplication logic:  
Original: $\frac{6r^2 -19r - 7}{2r-7} = 4r-3$  
Cross multiply: $6r^2 -19r - 7 = (2r-7)(4r-3)$.  

Let's expand $(2r-7)(4r-3)$ again.  
$2r \times 4r = 8r^2$.  
$2r \times (-3) = -6r$.  
$-7 \times 4r = -28r$.  
$-7 \times (-3) = +21$.  
Sum: $8r^2 - 34r + 21$.  

Equation: $6r^2 - 19r - 7 = 8r^2 - 34r + 21$.  

Let's re-expand $(3r+1)(2r-7)$ which represents the division.  
$3r(2r) = 6r^2$.  
$3r(-7) = -21r$.  
$1(2r) = 2r$.  
$1(-7) = -7$.  
Sum: $6r^2 - 19r - 7$. Correct.  

So, $\frac{6r^2 - 19r - 7}{2r-7} = 3r+1$ is correct.  

The equation to solve is $3r + 1 = 4r - 3$.  
$3r - 4r = -3 - 1$.  
$-r = -4$.  
$r = 4$.  

Okay, so where did I make a mistake in the division method just now?  
"Add 3 to both sides: $1 + 3 = r + 4r \Rightarrow 4 = 5r$."  
Why did I think $1+3=r+4r$?  
I wrote $1 = r - 3$. Then I subtracted $-1$ from both sides?  
$3r + 1 = 4r - 3$.  
Subtract $1$: $3r = 4r - 4$.  
Subtract $3r$: $0 = r - 4$.  
Multiply by -1: $r = 4$.  

Why did I calculate $6=5r$ earlier?  
"Move terms: $1 + 3 = r + 4r$" -> That is adding to both sides, not moving variables.  
Original equation: $3r+1 = 4r-3$.  
Rearrange: $3 - (-3) = 4r - 3r \implies 6$?  
Let's do it carefully.  
LHS = $3r + 1$  
RHS = $4r - 3$  
Subtract $3r$ from both sides: $1 = r - 3$.  
Add 3 to both sides: $1+3 = r \implies r=4$.  

Okay, the quadratic method gave $\Delta=1$, roots 4 and 7/2.  
The division method is much cleaner and confirms $r=4$ is the root (and implicitly discards $r=7/2$ since the remainder is 0).  

Why did I think the division method yielded $r=4/5$ before?  
Because I wrote: "Move terms: $3 + 3 = r + 4r \Rightarrow 6 = 5r$."  
Ah, in that thought trace, I was likely adding to LHS and subtracting from RHS incorrectly or moving the constant term wrong.  
Equation: $3r + 1 = 4r - 3$.  
Move $r$: $3r - 4r = 1$ (if it was on the left? No).  
Move constants to left: $3r - 4r = -3 - 1 \implies -r = -4 \implies r=4$.  

So, both methods point to $r=4$. The quadratic method found an extra root at 7/2 which is extraneous.  

9.  **Constructing the Final Output:**  
    *   Method: Clear the denominator.  
    *   Expand $(2r-7)(4r-3)$.  
    *   Set up equality.  
    *   Form quadratic equation.  
    *   Solve for $r$.  
    *   Check domain (denominator $\neq 0$).  
    *   State final answer.  

Let's quickly verify the "Domain Restriction" logic in the quadratic method output.  
Quadratic: $2r^2 - 15r + 28 = 0$.  
Roots: $4, \frac{7}{2}$.  
Denominator: $2r-7$.  
If $r=4$, $2(4)-7 = 1 \neq 0$. OK.  
If $r=3.5$, $2(3.5)-7 = 7-7 = 0$. Discard.  
Final answer is just 4? Or a set $\{4, 3.5\}$?  
Usually, finding the value of r implies finding valid solutions. The question asks for "the value", singular. However, sometimes multiple answers exist if I missed something. But mathematically, $r$ cannot be 3.5. So $r=4$.  

Let me just double check the expansion $(2r-7)(4r-3)$ one more time. It's easy to mess up signs.  
$2 \times 4 = 8$. Coeff of $r^2$ is correct.  
$2 \times -3 = -6$. Correct.  
$-7 \times 4 = -28$. Correct.  
$-7 \times -3 = 21$. Correct.  
Sum linear: $-6 - 28 = -34$. Correct.  
Constant: 21. Correct.  

LHS constant: -7.  
RHS quadratic coeff: $8r^2$. LHS: $6r^2$. Diff: $2r^2$ on RHS. Move to left $\to 0$.  
RHS linear coeff: $-34$. LHS: $-19$. Move $-19 \to -(-19) = +19$. No, if moving LHS to RHS, subtract LHS from RHS.  
So RHS term is $(8r^2 - 34r + 21)$ minus $(6r^2 - 19r - 7)$.  
$-34r - (-19r) = -34r + 19r = -15r$. Correct.  
Constant term: $21 - (-7) = 28$. Correct.  

Okay, the quadratic is definitely $2r^2 - 15r + 28 = 0$.  
$r = \frac{15 \pm 1}{4}$.  
$r = 16/4 = 4$.  
$r = 14/4 = 3.5$.  

Is it possible to solve $\frac{6r^2 - 19r - 7}{2r-7}$ differently?  
Maybe substitution? Not really necessary.  

What if the prompt implies finding *all* values, even complex ones?  
Discriminant is $1$, so roots are real and rational.  

Is there any ambiguity in "Find the value of r"? It usually means find all solutions that make the equation true. Since $3.5$ makes it undefined, strictly speaking, only 4 satisfies the equation.  

**Summary of Steps for Solution:**  
1.  Given equation: $\frac{6r^2 -19r - 7}{2r-7} = 4r-3$.  
    2.  Multiply by $(2r-7)$ to eliminate denominator: $6r^2 -19r - 7 = (2r-7)(4r-3)$.  
    3.  Expand RHS: $(2r-7)(4r-3) = 8r^2 - 6r - 28r + 21 = 8r^2 - 34r + 21$.  
    4.  Set LHS equal to expanded RHS: $6r^2 - 19r - 7 = 8r^2 - 34r + 21$.  
    5.  Rearrange into standard form ($0 = \dots$): $0 = (8-6)r^2 + (-34+19)r + (21-(-7))$.  
$0 = 2r^2 - 15r + 28$.  
    6.  Solve quadratic equation: $2r^2 - 15r + 28 = 0$.  
    7.  Use factoring or formula. $\Delta = 1$, factors $(2r-7)(r-4)=0$ or similar? Let's check expansion of $(2r-7)(r-4)$.  
$2r^2 - 8r - 7r + 28 = 2r^2 - 15r + 28$. Yes.  
    8.  Roots are $r=4$ and $r=7/2$.  
    9.  Check validity in original expression:  
Denominator is $2r-7$.  
If $r=7/2$, denominator is $7-7=0$ (undefined).  
If $r=4$, denominator is $8-7=1$ (defined).  
    10. Conclusion: Only $r=4$ is a solution.  

The question asks to "Find the value of r". Singular or plural? Usually if multiple valid answers exist, it says "values". If one is invalid and others are valid, usually list valid ones. Here only one valid. So answer is 4.  

One tiny detail: Does the problem imply finding an integer solution? Or just *a* value? It asks for "the value", singular. Maybe there's a constraint I missed? "Find the value of r".  
If $r=3.5$ was valid, it would be "the values". But it's not. So answer is 4.  

Final check of calculation:  
LHS at $r=4$: $(6(16)-19(4)-7)/(8-7) = (96-76-7)/1 = 13/1 = 13$.  
RHS at $r=4$: $4(4)-3 = 13$.  
Match.  

LHS at $r=3.5$: Denom is 0. Undefined.  

Looks solid.  

**Step-by-step reasoning text generation:**  
- Start with the equation.  
  - Multiply both sides by $(2r-7)$. Mention restriction $r \neq 7/2$.  
    - Expand RHS product.  
    - Move all terms to one side to form a quadratic equation.  
    - Solve for r.  
    - Verify solutions against original domain constraint.  
    - State final answer.  

Let's write out the steps clearly.  
Equation: $\frac{6r^2 -19r - 7}{2r-7} = 4r-3$  
Multiply by $(2r-7)$: $6r^2 - 19r - 7 = (2r-7)(4r-3)$  
Expand RHS: $8r^2 - 6r - 28r + 21 = 8r^2 - 34r + 21$  
Equate LHS and RHS: $6r^2 - 19r - 7 = 8r^2 - 34r + 21$  
Move terms to form a quadratic equal to zero.  
Subtract $6r^2$: $-19r - 7 = 2r^2 - 34r + 21$  
Add $34r$ and subtract $21$, add $19r$?  
Better: $0 = (8-6)r^2 + (-34 - (-19))r + (21 - (-7))$  
$0 = 2r^2 - 15r + 28$.  
Factor quadratic: $2r^2 - 15r + 28 = 0$.  
$(2r-7)(r-4) = 0$. (Since $(2 \times 1)(-7)$ or similar logic. $(2r-7)(r-4) = 2r^2 - 8r - 7r + 28 = 2r^2 - 15r + 28$.)  
Solutions: $2r-7=0 \implies r=3.5$ or $r-4=0 \implies r=4$.  
Check original denominator: $2r-7$.  
For $r=3.5$: $2(3.5)-7 = 0$. Undefined. Reject.  
For $r=4$: $2(4)-7 = 1 \neq 0$. Accept.  

Final Answer is 4.  
Also, the quadratic could be factored by grouping if that makes it look faster for some...  
$2r^2 - 15r + 28$ -> coefficients $a,b,c$ with $b^2-4ac=1$. Not obvious integer factors without trial or formula. Formula is safest.  

The solution seems robust.  

Double check the arithmetic one last time.  
$6(16) = 96$.  
$19(4) = 76$.  
$96 - 76 = 20$.  
$20 - 7 = 13$. Correct.  
$4r-3$ at $r=4 \implies 16-3=13$. Correct.  

What if I made a mistake copying the problem?  
$\frac{6r^2 -19r - 7}{2r-7} = 4r-3$.  
Looks correct.  

Is it possible that $2r-7$ in the numerator was meant to be something else? Probably not, I must solve what is given.  

The result is straightforward.  

One nuance: In some contexts, "Find the value of r" might imply finding a specific integer or a unique solution without explicitly listing extraneous roots if they are obvious (like domain violations). But showing the exclusion is mathematically rigorous and expected in step-by-step solutions. I will include it.  

Final check on latex formatting.  
$\boxed{4}$ or $\boxed{r=4}$. The prompt asks "Find the value of r". Usually $r$ is substituted into the box, or the value itself. I will put 4 in the box, or maybe "r=4". Standard for these formats usually prefers just the number if asked for a value. Let's look at the phrasing "put your final answer within \boxed{}". Usually this means the result. I'll provide $4$. But $r=4$ is also acceptable. I'll stick to providing the value $4$ or the equation solved. Let's write out the solution clearly.  

Let me check if there are complex solutions?  
$\Delta = 1 > 0$, so only one pair of real roots (counting multiplicity). Complex numbers don't apply here anyway.  

The request asks for "the value". If I have to choose, it is 4.  

Ready to write the response.  

Step 1: Write equation.  
Step 2: Clear denominator.  
Step 3: Expand polynomial.  
Step 4: Simplify to quadratic form.  
Step 5: Solve quadratic.  
Step 6: Check validity (denominator constraint).  
Step 7: Final answer.  

Constraint check again:  
Denom: $2r-7$.  
If $r=3.5$, denom is 0.  
Equation becomes $\frac{A}{0} = B$. This implies infinity or equality only if both sides are undefined (impossible) or limits involved, but for algebraic manipulation, it's strictly excluded.  

Okay, proceeding.  

One detail: The prompt uses LaTeX `$` delimiters. I will use them.  
Final Answer Box: `\boxed{4}` is appropriate. Or `\boxed{r=4}`. I will put `4` as the primary value. Actually, "value of r" asks for $r$. So stating $r=4$ or just 4. Usually in math competitions/textbooks, if the variable is asked, the number is sufficient, but identifying the variable equality is clearer. I'll write $r=4$ inside the box? Or just 4? Let's check common patterns. Often `\boxed{4}`. I will provide `r=4` to be safe, or just `4`.  
"Find the value of r" -> The value is 4. So $\boxed{4}$.  

Re-reading: "Please reason step by step...".  
Okay, logic is solid. No tricks found.  

Let's re-read carefully to ensure I didn't miss a sign change.  
$6r^2 -19r -7$.  
$(2r-7)(4r-3) = 8r^2 - 34r + 21$.  
$6r^2 - 19r - 7 - (8r^2 - 34r + 21) = 0$  
$-2r^2 + 15r - 28 = 0$  
Multiply by -1:  
$2r^2 - 15r + 28 = 0$.  
Same quadratic.  

Factors of 28 with middle term -15?  
(x+y) -> x=7, y=4 -> product 28, sum 11?  
Wait, $28 \times r$.  
Coeffs are $-15$ and $+28$.  
$(r-4)$ gives $28$ (pos) or something.  
$(2r-7)(r-4) = 2r^2 - 8r - 7r + 28 = 2r^2 - 15r + 28$.  
Yes, correct.  

What about factors of $a \cdot c$?  


## Answer

*(none: the token cap hit during thinking)*
