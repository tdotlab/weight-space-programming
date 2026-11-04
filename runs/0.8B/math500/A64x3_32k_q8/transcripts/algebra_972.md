# test/algebra/972.json (Algebra, level 4)

> If $|x+5|-|3x-6|=0$, find the largest possible value of $x$. Express your answer as an improper fraction.  

**Correct.** Gold `\frac{11}{2}`, predicted `\frac{11}{2}`. Finish: stop, 30802 tokens, 11 waits, 2126.4 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here is my thought process for solving this problem:  

1.  **Analyze the given equation:**  
The equation is $|x+5|-|3x-6|=0$.  

2.  **Understand the meaning of absolute value inequalities/equations:**  
An equation involving absolute values of two terms with the form $|A| - |B| = 0$ implies that their difference must be zero, which means $A = B$.  
So, $|x+5| = |3x-6|$.  

3.  **Explore the properties of absolute value:**  
The property of absolute values is $|x| \ge 0$. Also, $|x-a|$ represents the distance from point $x$ to point $a$.  
For equation: $|x+5| = |3x-6|$, both sides must be equal (non-negative).  

4.  **Consider cases for $3x-6$:**  
There are a few ways to interpret the equation, but usually, we should check the conditions for equality or inequality to ensure validity. Since we have an equation with absolute values, let's solve it by considering cases based on the sign of expressions inside the absolute value bars.  

**Case 1:** $x+5 = 3x-6$.  
**Case 2:** $-(x+5) = -(3x-6)$ (which is same as $|x+5|=|3x-6|$).  
Actually, the standard way to handle this:  
If $a > b$, then $|a|=a$ and $|b|=b$. But here we are comparing two expressions.  
Let's break down by cases for $3x-6$ (or $x$ relative to a point). Let's just analyze where each term inside absolute value is positive or negative.  

The equation is $|x+5| = |3x-6|$.  
This implies $|x+5|$ and $|3x-6|$ have the same distance from 0. They are equal if:  
-   They are both on the same side of 0, OR  
    -   One is negative and one is positive (so magnitudes match).  

Let's analyze the roots of the expressions inside to find $x$ where they switch sign or are not zero? No.  
The condition is just $|A| = |B|$. This happens when $A=B$ or $A=-B$.  

**Case A: Both positive.**  
$x+5 \ge 0$ AND $3x-6 \ge 0$.  
Then $x+5 = 3x-6$.  
Subtract $x$: $5 = -2x + 6$. (This is wrong algebra).  
Move terms to one side: $3x-6 - x - 5 = 0 \implies 2x - 11 = 0$.  
Let's re-write carefully.  
$x+5 = 3x-6$  
$5 + 6 = 3x - x$  
$11 = 2x$  
$x = \frac{11}{2}$.  

**Case B: Both negative.**  
$-(x+5) = -(3x-6)$  
This implies $|x+5| = |3x-6|$ but signs are the same?  
No. Let's rephrase.  
If we consider the graph of $f(t) = |t|$, the points $(0,0)$ is intersection.  
Here $x$ and $3x-6$.  
$x+5 > 0 \implies x > -5$.  
$3x-6 > 0 \implies x > 2$.  
Since $x > 2$, then $|x+5| = x+5$, so $x+5=3x-6$ holds.  

**Case C: One positive, one negative.**  
The equation is $|A| = |B|$. This means $A=B$ OR $A=-B$.  
Subcase C1: $x+5 = 3x-6$ (Already solved).  
Subcase C2: $x+5 = -(3x-6) \implies x+5 = -3x + 6 \implies 4x = 1 \implies x = 1/4$.  

**Case D: One negative, one positive.**  
This means $|A|$ and $|B|$ have the same absolute value.  
If $x+5$ is negative (or non-positive) and $3x-6$ is positive (or non-negative).  
We need $|x+5| = |3x-6|$.  
Let's use the condition: $|x+5| \ge 0$.  
Let's look at the structure again.  
Let $g(x) = |x+5|$ and $h(x) = |3x-6|$. We want $g(x) = h(x)$.  
Consider $x$ as a function of time, but let's solve algebraically.  

**Analyzing the signs:**  
The absolute value bars denote that we look at points $x+5$ and $3x-6$.  
If $x \in (-\infty, -5]$, then $x+5 \le 0$ and $3x-6 \le 2(-1.4) < 0$. No, check.  
Let's look at regions:  
1.  $x \ge -5$: $x+5 \ge 0$.  
The equation is $(x+5) = |3x-6|$.  
If $3x-6 \le 0$, then $|3x-6| = -(3x-6) = 6-3x$. So $(x+5) = 6-3x \implies 4x = 11 \implies x = 11/4$.  
If $x < -5$: $x+5 < 0$, so $|x+5| = -(x+5)$. $|3x-6|$. We have a negative on both sides.  
Equation: $-(x+5) = -(3x-6) \implies x+5=3x-6$ again? No.  
This is getting confused. Let's stick to $|A|=|B|$.  
The set of solutions must satisfy two conditions:  
    1.  $(x+5)^2 = (3x-6)^2$ (Always true) OR  
        2.  $(x+5)^2 = -(3x-6)^2 + (x+5)$? No.  
Let's step back. The condition $|A|=|B|$ is equivalent to:  
$A^2 - B^2 = 0 \implies (A-B)(A+B)=0$.  
Here $A=x+5, B=3x-6$.  
So $(x+5)-(3x-6) = 0$ or $(x+5)+(3x-6) = 0$.  

Let's solve the quadratic equation derived from $A^2-B^2=0$:  
$(x+5)^2 - (3x-6)^2 = 0 \implies ((x+5)-(3x-6))((x+5)+(3x-6)) = 0$.  

**Root 1:** $x+5 = -(3x-6)$  
$x+5 = -3x + 6$  
$4x = 1 \implies x = 1/4$.  
Let's check if this solution satisfies the original equation.  
LHS: $|1/4 + 5| = |21/4| = 21/4$.  
RHS: $|3(1/4) - 6| = |12/4 - 24/4| = |-12/4| = |-3| = 3 = 30/10$? No, 3.  
LHS/RHS ratio check. Is LHS=RHS? $21/4 \neq 3$. So $x=1/4$ is a solution to the equation $|A|=|B|$ only if it satisfies the original form.  
Let's re-evaluate the derivation from $(A-B)(A+B)=0$.  
If we expand: $(x+5)^2 = (3x-6)^2$? No, we need $|A| = |B|$.  
This means $|x+5| = |3x-6|$.  
Squaring gives $(x+5)^2 = (3x-6)^2$.  
Expanding: $x^2 + 10x + 25 = 9x^2 - 36x + 36$.  
$8x^2 - 46x + 11 = 0$? No.  
Let's check carefully.  
If $(x+5)^2 = (3x-6)^2$, then $(x+5) = \pm(3x-6)$.  
Since this implies $|A|=|B|$, both signs are valid if we allow for the condition that $A$ and $B$ can be equal or opposite? No.  
If $|A|=|B|$ holds, then $(x+5)^2 = (3x-6)^2$.  
The solutions to $(x+5)^2 = (3x-6)^2$ are simply $x+5 = 3x-6$ or $-(x+5) = -(3x-6)$? No.  
Squaring both sides removes sign information, but we are looking for the set of values $x$.  
However, usually, we check cases.  

**Case A: The two expressions have the same sign.**  
This means $(x+5)^2 = (3x-6)^2$ holds for all cases where signs are positive or negative.  
This implies $(x+5)(3x-6) - x^2 - 10x - 25 + 9x^2 - 36x + 36 = 0$? No.  
Let's go back to basics. $|A|=|B|$. This is equivalent to $(A+B)(A-B)=0$.  
So, we need to solve either:  
(I) $x+5 - (3x-6) = 0 \implies x+5-3x+6=0 \implies -2x + 11 = 0 \implies 2x = 11 \implies x = 11/2$.  
(II) $x+5 + (3x-6) = 0 \implies 4x - 11 = 0 \implies x = 11/4$.  

Now, which of these are actually valid solutions?  
We must have satisfied the original equation $|A|=|B|$ for that specific $x$.  
Let's check my logic.  
The condition $(x+5)(3x-6) - x^2 + 10x + 25 = 0$?  
No, this was derived from squaring: $(x+5)^2 = (3x-6)^2$.  
If $|A|=|B|$, then $(A+B)(A-B)$ is not necessarily valid.  
The correct condition is that the sign of $A$ is equal to the sign of $B$ OR they are opposite? No, just $A^2=B^2$ or something else.  
Let's re-verify my cases.  
Equation: $|x+5| = |3x-6|$.  
Squaring: $(x+5)^2 = (3x-6)^2 \implies x^2 + 10x + 25 = 9x^2 - 36x + 36$.  
$8x^2 - 46x + 11 = 0$. This gives us the set of values for $x$ where signs might match? No, this is for $(A)^2 = (B)^2$.  
We need to check if $|x+5|=|3x-6|$ or not.  
If $(A-B)(A+B)=0$, then either $A=B$ or $A=-B$.  
Since $|A|=|B|$, does this mean $A$ and $B$ can be different signs?  
No. $|A|=|B|$ means $|x+5| = |3x-6|$. This implies $|x+5|$ and $|3x-6|$ are equal distances from the origin.  
The condition $|A|=|B|$ is satisfied by $A=B$ or $A=-B$.  
So, $(x+5) - (3x-6) = 0$ or $(x+5) + (3x-6) = 0$.  

Let's re-evaluate the first case: $x+5 = -(3x-6)$? No, this means $|A|=|B|$ implies $A=-(B)$ if both negative? No.  
Let's just use the algebraic condition $(A-B)(A+B)=0$ to solve for $A,B$.  
Case 1: $x+5 = -(3x-6) \implies x+5 = -3x + 6 \implies 4x = 1 \implies x = 1/4$.  
Let's check the original equation.  
If $x=1/4$, $|1/4+5| = |21/4| = 21/4$.  
$|3(1/4)-6| = |-12/4 - 24/4| = |-36/4| = |-9| = 9$?  
Let me calculate again.  
If $x=1/4$:  
LHS: $|21/4| = 21/4$.  
RHS: $|3(0.25)-6| = |0.75 - 6| = |-5.25| = 5.25 = 21/4$.  
So $21/4 = 21/4$.  
The equation holds for $x=1/4$ when both sides are positive?  
Let me re-read the algebra.  
Original: $|x+5| - |3x-6| = 0 \implies |x+5| = |3x-6|$.  
Condition $(x+5)-(3x-6)=0$ gives $A=B$.  
Condition $(x+5)+(3x-6)=0$ gives $A=-B$.  
Are these two distinct cases? Yes.  
If $A=0$, then $|A|=0$.  
But the expression inside is $x+5$ and $3x-6$. They are non-zero if we are looking for real values.  
The condition $(A-B)(A+B)=0$ means that either:  
1. $x+5 = -(3x-6)$ (implies $|x+5|=|-B|$ where $B=3x-6$) -> No, this means $|x+5|=|-(3x-6)|$ is true for all cases? No.  
It implies the equality $|A|=|B|$ holds if either $A=B$ or $A+B=0$ (if we square both sides).  
If $(x+5) - (3x-6) = 0 \implies 2x+11=0 \implies x=-5.5$.  
If $(x+5) + (3x-6) = 0 \implies 4x+9=0 \implies x=-9/4 = -2.25$.  

Let's try to verify which of these cases is actually valid.  
Case 1: $A=B \implies x+5 = 3x-6 \implies 2x=11 \implies x=5.5$.  
Let's check validity.  
LHS: $|5.5+5| = |10.5| = 10.5$.  
RHS: $|17.4 - 6| = |11.4| = 11.4$.  
These are not equal. So Case 1 is incorrect?  
Why did I think they were?  
Ah, I used the logic that $(x+5) = -(3x-6)$ was the condition derived from $A-B=0$ in the squared equation? No.  
Let's be very systematic.  

We have two sides: $y_1(x) = |x+5|$ and $y_2(x) = |3x-6|$.  
We want $y_1(x) = y_2(x)$.  
Squaring both sides gives $(y_1)^2 = (y_2)^2$ if $y_1, y_2 \ge 0$.  
If we allow negative values?  
$|A|=|B|$ means $A=B$ or $A=-B$ is FALSE. $A^2=B^2$ is true.  
It means $\sqrt{A^2} = |A|$ is always equal to $A$ if $A \ge 0$, and $\sqrt{A^2} = -A$ if $A < 0$.  
So, for $|x+5| = |3x-6|$, we are looking for points where the absolute values of the functions intersect.  

We can define regions:  
Region 1: $x+5 \ge 0$ and $3x-6 \ge 0$.  
Here, both are positive. Then $x+5 = 3x-6$.  
Region 2: $x+5 \le 0$ and $3x-6 \ge 0$ (one negative, one non-negative or both). No, if one is negative it can't be positive?  
If we have $|A|=|B|$, then either ($A=B$) or ($A=-B$)? No.  
If $A$ is positive and $B$ is negative:  
Example: $A=5, B=-3$. $|5|=| -3 |$ is false.  
Example: $A=5, B=5$. $|5|=|5|$ is true.  
Example: $A=5, B=4$. No.  
Example: $A=2, B=1$. Yes? No, $|2| \neq |1|$.  
Example: $A=-2, B=-3$. $|-2|=|-3|$ is false (if $-2 \neq -3$).  
But if $x$ satisfies the equation.  
The condition $(x+5)^2 = (3x-6)^2$ ensures that $|x+5| = |3x-6|$ for a given x? No.  
It implies that $\sqrt{x^2 + 10x + 25} = \sqrt{9x^2 - 36x + 36}$ assuming both are non-negative.  
So $(x+5)^2 = (3x-6)^2$ is equivalent to the equation $|x+5|=|3x-6|$.  
Therefore, any solution to the squared equation must satisfy the absolute value equality provided that $|x+5| \ge 0$.  
Since absolute value is always non-negative, this holds.  

However, we must also check if the sign condition was valid?  
If $x$ satisfies $(x+5)^2 = (3x-6)^2$, then either $x+5=3x-6$ or $-(x+5) = -(3x-6)$ is not necessarily true.  
Let's re-derive the condition properly.  
The equation $|A|=|B|$ means $(A \cdot B^*) \ge 0$.  
Let's just solve it by checking the two branches of absolute value.  

**Case 1: Both inside terms are positive.**  
This is true if $x+5 > 0$ and $3x-6 > 0$.  
If $x > -5$, then $|x+5| = x+5$.  
If $x > 2$, then $|3x-6| = 3x-6$.  
The equation is $x+5 = 3x-6 \implies 2x = 11 \implies x = 5.5$.  
Check: At $x=5.5$, $x>2$ holds, so both inside positive? No, $3(5.5)-6 = 16.5-6 = 10.5 > 0$.  
So at $x=5.5$:  
LHS: $|5.5+5| = |10.5| = 10.5$.  
RHS: $|3(5.5)-6| = |16.5-6| = |10.5| = 10.5$.  
So $x=5.5$ is a solution.  

**Case 2: Both inside terms are negative.**  
This means $x+5 < 0$ and $3x-6 < 0$.  
Since $x+5 < 0 \implies x < -5$.  
If $x < -5$, then $|x+5| = -(x+5) = -x-5$.  
For $|3x-6|$: if $x < -6$, then $3x-6 < -12$, so positive value is negative.  
So $3x-6 < 0 \implies 3x < 6 \implies x < 2$.  
Since $x < -5$ implies $x < 2$, the condition holds.  
The equation is $-(x+5) = -(3x-6) \implies -(x+5) = 6-3x \implies x+5 = 3x-6$.  
This simplifies to $4x = 11$ which is not possible as derived before?  
Let me recheck the algebra.  
If $A < 0$, then $|A| = -A$. If $B < 0$, then $|B| = -B$.  
Then equation becomes $-(-x-5) = -(-3x+6)$ ? No.  
Let's write out terms:  
LHS of original equation is $|-2|$.  
RHS of original equation is $|9|$.  
No, the problem is to find values where $|A| = |B|$.  
Case 2: $x < -5$ and $3x-6 < 0$.  
LHS term is $|x+5| = -(x+5) = -x-5$.  
RHS term is $|3x-6|$. Since $x < -5$, $3x < -15$, so $3x-6 < -21$, so $|3x-6| = -3x+6$.  
Equation: $-(x+5) = -(-3x+6)$? No.  
The equation is $(|x+5|) - (|3x-6|) = 0 \implies |x+5| = |3x-6|$.  
Let's use the logic from my scratchpad.  
I need $x$ such that $|-x-5| = |-2x-14|$? No.  
Let's look at terms:  
Term 1: $A = x+5$. Term 2: $B = 3x-6$.  
If we consider signs.  
Condition: $x \in (-\infty, -5]$ (since for this region $x+5 \le 0$).  
For the second term, if $3x-6 \le 0 \implies x \le 2$. Since $x \le -5$, condition holds.  
So we are looking for intersections of regions where both terms are positive or negative?  
The equation is $|A| = |B|$.  
This implies that the set $\{y : y = |A|\}$ and $\{y : y = |B|\}$ intersect at the point(s).  
Since $|y| \ge 0$, we are looking for intersection of graph of $y=|x+5|$ with graph of $y=|3x-6|$.  

However, I should be careful. My algebraic deduction was based on $(A-B)(A+B) = (A^2-B^2)$? No.  
The logic is: if the equation holds, then $A=B$ or $A+B=0$ OR $A=-B$ AND $A,B$ are consistent with original signs? No.  

Let's re-evaluate my Case 1 ($x+5 \ge 0, 3x-6 \ge 0$).  
The intersection of regions where both expressions have the same sign is not sufficient.  
For example, if $A=2, B=4$, then $|2|=|4|$ fails because signs are opposite? No, absolute value is non-negative.  
If $A=3x-6$, and $B=x+5$, we need $x+5 \ge 0$ and $3x-6 \ge 0$. This gives us the case where both are positive, leading to $21/4 = 5.5$ or something.  
But what if $A=3, B=3$? Then $|3|=|3|$ is valid.  
What if $A=-2, B=3$? Then $|-2|=|3|$ is false (since $-2 \ne 3$).  
The condition is that the set of values for which $|x+5|=|3x-6|$ includes all real numbers in the intersection? No.  

Let's restart with a clear method.  
We need to find $x$ such that:  
$x+5 = 3x-6$ OR $-(x+5) = -(3x-6)$  
AND ensure $|A|=|B|$.  
But absolute value is defined for real numbers, so it's always non-negative.  
$|A|=|B|$ implies that they are both $\ge 0$ (since if one is negative and the other positive, say $-5 = 5$, impossible).  
However, there's another possibility: what if both are negatives? Then $|-x|=|-2|$ means $|x+5| = |-17/4|$. No.  
Let's check the logic:  
If we have $A^2=B^2$, then $A= \pm B$ is not necessarily true, but $\sqrt{A^2} = |A| = |B|$.  
The condition $|x+5|=|3x-6|$ holds for all $x$ such that $(x+5)^2 - (3x-6)^2 = 0$? No.  
Because $|u| \ge 0$ and $|v| \ge 0$. The set of valid $x$ is determined by $\sqrt{(x+5)^2} = \sqrt{(3x-6)^2}$?  
Yes, but this is only true if $x+5$ and $3x-6$ are the arguments.  
Since we have real numbers, $|A|=|B|$ means $A^2=B^2$.  
So $|x+5|^2 = |3x-6|^2 \implies (x+5)^2 = (3x-6)^2$.  
So the valid $x$ must satisfy $(x+5)^2 = (3x-6)^2$.  

Let's expand:  
$x^2 + 10x + 25 = 9x^2 - 36x + 36$.  
$8x^2 - 46x + 11 = 0$.  
Roots for this quadratic are solutions to the squared equation. But we must check which of these roots satisfy the original condition $|x+5|=|3x-6|$?  
Squaring both sides is an equivalence relation only if we consider $y^2=z^2$ and $z=y$. No.  
The squaring operation introduces extraneous solutions where one side is negative but the other is not? No, squares are always non-negative.  
So for any $x$ satisfying $(x+5)^2 = (3x-6)^2$, we automatically have $|x+5|^2 = |3x-6|^2$.  
Does this mean $|x+5|=|3x-6|$? Yes, because both are non-negative by definition of square root.  
However, we need to ensure that the signs match? No.  
If $A=B$ and $|A|=|B|$, then $A=|A|=|B|$.  
But if $A=-B$, then $|A|=|B|$ implies $-|A|=|B|$ which means $|A|=|-B|=|B|$.  
So both cases cover all possibilities for $|A|=|B|$.  

So the question reduces to solving $(x+5)^2 = (3x-6)^2$ and checking consistency?  
But I already did this:  
Case 1: $x+5 = 3x-6 \implies x=5.5$.  
Case 2: $-(x+5) = -(3x-6) \implies x=-5.5$? No.  
Let's check my algebra for Case 2 again.  
$(x+5)+(3x-6)=0 \implies 4x=1 \implies x=1/4$.  
But $|A|=|B|$ condition requires that the expressions are non-negative?  
No, just $|x+5| = |3x-6|$.  
If $x=-2.25$, then $x+5 = 2.75$ (positive), $3x-6 = -9(0.4)$? No.  
Let's calculate values for Case 1 ($x=5.5$):  
LHS: $|10.5|=10.5$. RHS: $|16.5-6|=10.5$. It works.  

Let's check my algebraic derivation of the quadratic again.  
$x^2 + 10x + 25 = 9x^2 - 36x + 36$  
$0 = 8x^2 - 46x + 11$.  
Is this correct?  
Let's re-derive:  
$(x+5)^2 = (3x-6)^2 \implies x^2 + 10x + 25 = 9x^2 - 36x + 36$  
$8x^2 - 46x + 11 = 0$.  

Let's check if $x=5.5$ satisfies this quadratic.  
$8(5.5)^2 - 46(5.5) + 11$.  
$5.5^2 = (11/2)^2 = 121/4$.  
$8 \times 121/4 = 2 \times 121 = 242$.  
$46 \times 11/2 = 23 \times 11 = 253$.  
$242 - 253 + 11 = 81 / ?$  
$242 + 11 = 253$.  
$253 - 253 = 0$.  
So $x=5.5$ IS a root of this quadratic.  

Let's check if $x=1/4$ is a root.  
$8(1/4)^2 - 46(1/4) + 11 = 8/16 - 23/4 + 11$.  
$0.5 - 5.75 + 11 = 0$.  
$11 - 5.75 + 0.5 = 5.75 \neq 0$.  
So $x=1/4$ is NOT a solution to $(x+5)^2 = (3x-6)^2$.  
Why? Because if $x=1/4$, then:  
$(x+5) = 21/4$. Square is $441/16 \approx 27.56$.  
$(3x-6) = 12/4 - 6 = -36/4 = -9$. Square is $81/16 = 5.06$.  
$441/16 \neq 81/16$. So the squared equation gives different solutions.  

The condition $|A|=|B|$ implies $|A|^2 = |B|^2$, which means $(x+5)^2 = (3x-6)^2$.  
However, this must be consistent with the equality of signs? No.  
If we square both sides of $|x+5| = |3x-6|$, we obtain $(x+5)^2 = (3x-6)^2$ IF $|A|=|B|$ was an assumption? No.  
We are solving the system:  
1) $(x+5)^2 = (3x-6)^2$  
   2) $|x+5| = |3x-6|$.  
The first equation is necessary and sufficient.  
So, if I solve for $x$ in terms of roots, I must check if they satisfy the condition $A^2=B^2$?  
Since $A^2=B^2 \iff A=\pm B$ implies $|A|=|B|$ IF AND ONLY IF $\{x+5\} = \{3x-6\}$ is false.  
Let's check: if $(x+5) = (3x-6)$, then LHS=$|A|$, RHS=$|B|$. Since $LHS^2=RHS^2$, this implies $(A)^2=(B)^2$? Yes.  
Does it imply $|A|=|B|$? No. It implies $|A|= \pm B$. If $A=B$ then $|A|=|B|$. If $A=-B$ then $|A|=|-B|=|B|$.  
So if $(x+5) = -(3x-6)$ (meaning $A^2=B^2$ implies $x=5.5$ and $x=1/4$), we need to check if $|A|$ matches the magnitude.  

Let's analyze the roots of $8x^2 - 46x + 11 = 0$.  
Discriminant $\Delta = (-46)^2 - 4(8)(11) = 2116 - 352 = 1764$.  
$\sqrt{1764} = 42$.  
So $x = \frac{46 \pm 42}{16}$.  
Case A: $x_1 = (46 + 42)/16 = 88/16 = 11/2 = 5.5$.  
Case B: $x_2 = (46 - 42)/16 = 4/16 = 0.25 = 1/4$.  

Let's verify both roots.  
**Check x=5.5:**  
LHS: $|x+5| = |10.5| = 10.5$.  
RHS: $|3x-6| = |16.5 - 6| = |10.5| = 10.5$.  
So $|A|=|B|$ is satisfied. This gives a valid solution.  

**Check x=0.25:**  
LHS: $|x+5| = |21/4| = 21/4 = 5.25$.  
RHS: $|3x-6| = |3(1/4) - 6| = |-12/4 + 24/4| = |-9| / 10 = -1.8$? No.  
$|0.75 - 6| = |-5.25| = 5.25$.  
So $LHS=RHS$.  
Let's re-evaluate my manual check of x=1/4.  
My algebra calculation for $(x+5)^2$:  
$(1/4 + 5)^2 = (21/4)^2 = 441/16$.  
$(3(1/4) - 6)^2 = (-36/4)^2 = 36^2 / 16 = 1296/16$? No.  
$3(0.25) = 0.75 = 3/4$. $6 = 24/4$. So $3x-6 = -18/4 = -9/2$.  
Square is $(9/2)^2 = 81/4$.  
$81/4 = 1600/64$? No. $81/4 = 2025/16$? No.  
$16 \times 3 = 48$.  
Let's use exact fractions.  
LHS sq: $(21/4)^2 = 441/16$.  
RHS sq: $(9/2)^2 = 81/4$.  

*Continued in [part 2 of 4](algebra_972_p2.md): GitHub stops rendering math on pages this long, so the transcript is split.*
