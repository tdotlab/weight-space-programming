# test/intermediate_algebra/1797.json (Intermediate Algebra, level 4)

> The asymptotes of a hyperbola are $y = 2x - 3$ and $y = 17 - 2x.$  Also, the hyperbola passes through the point $(4,7).$  Find the distance between the foci of the hyperbola.  

**Wrong.** Gold `2 \sqrt{5}`, predicted `None`. Finish: length, 8192 tokens, 4 waits, 659.2 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here is my thought process for solving this problem:  

1.  **Analyze the Request:**  
    *   **Given:** An asymptote equation ($y = 2x - 3$) and its slope-intercept form. Another asymptote ($y = 17 - 2x$). Also, a point $(4, 7)$ lies on the hyperbola.  
    *   **Goal:** Find the distance between the foci of the hyperbola.  

2.  **Identify the Key Features of a Hyperbola with Asymptotes:**  
    *   The equations of the asymptotes are linear equations: $y = mx - c$ and $y = m'x + d'$ or more generally, two parallel lines? Or diagonals?  
    *   The product of slopes of asymptotes is usually $+1$ or $-1$, but here I have explicit equations. Let's look at the structure.  
    *   The equations are:  
        1.  $y = 2x - 3 \implies 2x - y - 3 = 0$. Slope $m_1 = 2$.  
        2.  $y = 17 - 2x \implies y + 2x - 17 = 0$. Slope $m_2 = -2$.  
    *   The slopes are opposites ($2$ and $-2$) and magnitudes are equal (absolute value 2). This suggests the hyperbola is of the form $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ or $\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1$. No, that's standard. If asymptotes are perpendicular?  
        *   Slopes $m_1 = 2$, $m_2 = -2$. Product is $-4$. Not $-1$.  
    *   However, for a hyperbola, the product of slopes of perpendicular asymptotes is $-1$. The equation of asymptotes is determined by the lines passing through the center. Let's find the intersection point first to find the center.  

3.  **Find the Center $(h, k)$:**  
    *   The intersection of asymptotes gives the center.  
    *   System of equations:  
$y = 2x - 3$  
$y = -2x + 17$  
    *   Set them equal:  
$2x - 3 = -2x + 17$  
$4x = 20$  
$x = 5$  
    *   Find $y$:  
$y = 2(5) - 3 = 10 - 3 = 7$  
    *   So, the center is $C(5, 7)$.  

4.  **Use the Point on the Hyperbola:**  
    *   The hyperbola passes through $(4, 7)$.  
    *   Let's check if this point relates to the asymptotes.  
Is $(4,7)$ one of the points where asymptotes meet? Wait, $(4,7)$ has $y=7$ and $x=4$.  
At $x=4$, $y = 2(4) - 3 = 5 \neq 7$. So it's not on the first asymptote.  
At $x=4$, $y = -2(4) + 17 = 9 \neq 7$. So it's not on the second asymptote either.  
    *   This seems straightforward, but there's a specific property about points $(h, k)$ being the center? The point is $(4,7)$, which is NOT the center $(5,7)$. It is close to it.  
    *   Let's verify if $(4,7)$ satisfies the condition for an ellipse or hyperbola equation form relative to the asymptotes.  

5.  **Analyze the Asymptote Equations and Center:**  
    *   The center is $C(5,7)$.  
    *   The lines can be written as $L_1: 2x - y - 3 = 0$ and $L_2: 2x + y - 17 = 0$.  
    *   Let the standard form of the hyperbola be $\frac{(x-h)^2}{a^2} \pm \frac{(y-k)^2}{b^2} = 1$. Here $(h,k)=(5,7)$.  
    *   The asymptotes are given by $y - k = m(x-h)$.  
Let's check.  
Line 1: $y - 7 = 2(x - 5) \implies y - 7 = 2x - 10 \implies y = 2x - 3$. Correct.  
Line 2: $y - 7 = -2(x - 5)$? Let's check. $y - 7 = -2x + 10 \implies y = -2x + 17$. Correct.  
    *   The equation of the asymptotes is $\frac{y-k}{m_1} = \pm \frac{x-h}{c}$, so $y = m_1(x-h) + k$ and $y = -\frac{1}{m_1}(x-h) + k$.  
    *   This means the slope of asymptotes are $\pm 2$ and they intersect at $(5,7)$.  
    *   The general equation of a hyperbola is:  
$\frac{(x-5)^2}{A} - \frac{(y-7)^2}{B} = 1$ or $\frac{(x-5)^2}{A} + \frac{(y-7)^2}{B} = 1$ (ellipse). Since it's a hyperbola, it is the minus.  
So the equation of the hyperbola can be written as:  
$(y - 7)^2 / B^2 - (x - 5)^2 / A^2 = 1$ OR $(x - 5)^2 / A^2 - (y - 7)^2 / B^2 = 1$.  

6.  **Identify the Relationship between Asymptotes and Coefficients:**  
    *   The asymptotes are $2x - y - 3 = 0$ and $2x + y - 17 = 0$.  
    *   Let's rewrite the general equation for a hyperbola centered at $(h,k)$ with slopes $\pm m$:  
$\frac{(y-k)^2}{a^2} \mp \frac{(x-h)^2}{b^2} = 1$ is not quite right. The lines passing through $(h,k)$ and having slopes $m$ are $y-k = m(x-h)$.  
    *   Let the hyperbola be $\frac{x^2}{A^2} - \frac{y^2}{B^2} = 1$ (centered at origin). Asymptotes are $y = \pm \frac{B}{A} x$.  
    *   In general, the asymptotes of $\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$ are $y-k = \pm \frac{b}{a}(x-h)$. Or if it's the other orientation: $(y-k) = \mp \frac{a}{b}(x-h)$.  
    *   Here we have slopes $\pm 2$. This means $a/b = 1/2$ or $b/a = 2$. Let's assume the form $(x-5)^2 / a^2 - (y-7)^2 / b^2 = 1$. Then asymptotes are $y = \pm 2(x-5) + 7$.  
    *   The slopes match.  
    *   So, we have a hyperbola of the form $\frac{(x-5)^2}{a^2} - \frac{(y-7)^2}{b^2} = 1$ OR $\frac{(x-5)^2}{b^2} - \frac{(y-7)^2}{a^2} = 1$. The slopes are $m_1, m_2$.  
    *   If it is $\frac{(x-h)^2}{A^2} - \frac{(y-k)^2}{B^2} = 1$, the asymptotes are $y=k \pm \sqrt{B/A}(x-h)$. The slopes would be $\pm B/A$.  
Here slopes are $2$ and $-2$. So either $B/A = 2$ or $A/B = 2$. Let's call $a^2 = a_{h}^2$ and $b^2 = b_{h}^2$.  
    *   Let the hyperbola equation be $(x-h)^2 / A - (y-k)^2 / B = 1$ or similar.  
    *   The standard form is $\frac{(x-5)^2}{u^2} - \frac{(y-7)^2}{v^2} = 1$. The asymptotes are $(x-5) = \pm \frac{u}{v}(y-7)$? Wait, that's not right.  
    *   Let's stick to the line equations directly.  
    *   Asymptote 1: $y - 7 = 2(x - 5)$. So $\sqrt{\dots} = 2 \sqrt{\dots}$ or something similar.  
The equation of the hyperbola is $(y-7)^2/B^2 \pm (x-5)^2/A^2 = 1$?  
Let's just use the intercept form logic for asymptotes.  
For a hyperbola $\frac{x^2}{A^2} - \frac{y^2}{B^2} = 1$, asymptotes are $y = \pm \frac{B}{A} x$.  
This means the product of slopes is not determined by just the equation but related to coefficients.  
    *   General Equation: $Ax^2 + By^2 + Dx + Ey + F = 0$ with different signs for terms corresponding to hyperbola? Or better, just substitute the center and simplify.  
Since we know the center is $(5,7)$, let's shift coordinates to the center. Let $X = x - 5$ and $Y = y - 7$.  
The asymptotes in $(X,Y)$ are $y - k = \pm \lambda (x - h)$ where $\lambda = 2$ is one slope and $-2$ is the other. No, these are the same magnitude.  
So in $(X,Y)$ coordinates, the lines passing through origin are $Y = 2X$ and $Y = -2X$.  
Thus, $\frac{Y}{X} = \pm 2$. Or rather, the asymptote equations in original coords correspond to $Y = m X$ with $m=2$.  
    *   This implies the hyperbola equation (centered at origin) is of form $X^2/A^2 - Y^2/B^2 = 1$ or $Y^2/A^2 - X^2/B^2 = 1$.  
If it's $X^2/a^2 - Y^2/b^2 = 1$, asymptotes are $Y = \pm (b/a) X$. Here $Y/X = \pm b/a$. We have slopes $\pm 2$. So $b/a = 2$ (assuming positive slope for a branch, but hyperbola has both).  
    *   Let's look at the given equations in terms of $(x-5)$ and $(y-7)$.  
Equation 1: $y = 2x - 3 \implies y - 7 = 2(x - 5) - 3$?  
$2(5)-3 = 7$. So $2x-3-7 = 2x-10 = 2(x-5)$.  
Equation 1 becomes: $y - 7 = 2(x - 5) \implies Y = 2X$.  
Equation 2: $y = 17 - 2x \implies y - 7 = -2(x - 5)$.  
Check: $17-7 = 10$. $-2(5) + 7 = -3 \neq 7$... Let's redo.  
Center is $(5,7)$.  
For line 2: $y = -2x + 17 \implies y - 7 = -2x + 10 = -2(x-5)$. Yes, so $Y = -2X$.  
    *   So the asymptotes in the shifted coordinate system $(X,Y)$ centered at $(5,7)$ are simply $Y = 2X$ and $Y = -2X$.  
    *   The hyperbola passes through a point $P(4,7)$. In $(X,Y)$ coords, $x=4, y=7 \implies X = 4-5 = -1$, $Y = 7-7 = 0$. So the point is $(-1, 0)$ in the shifted frame.  
    *   Let the equation of the hyperbola in $(X,Y)$ be $\frac{X^2}{a^2} \pm \frac{Y^2}{b^2} = 1$ (since asymptotes have slopes $\pm b/a$, or $a/b$).  
Since the asymptotes are $Y = \pm 2X$, this means one branch goes to infinity in direction $(1, 2)$ and other goes to infinity in direction $(-1, -2)$. This is for rectangular hyperbola if slopes were infinite, but here finite.  
The slopes of asymptotes correspond to $\pm \sqrt{b^2/a^2}$ or something?  
Let's assume the equation is $\frac{X^2}{A^2} - \frac{Y^2}{B^2} = 1$ with $m_{asymptote} = \pm B/A$. Here $\pm B/A = \pm 2$. This implies $B/A = 2$, so $B = 2A$.  
The other possibility is the equation is $\frac{Y^2}{A^2} - \frac{X^2}{B^2} = 1$. Then asymptotes are $Y^2/B^2 = X^2/A^2 \implies Y = \pm (B/A)X$ ?  
Let's derive carefully.  
Standard hyperbola $\frac{x^2}{A^2} - \frac{y^2}{B^2} = 1$. Asymptotes are $y = \pm \frac{B}{A} x$. The slopes are $\frac{B}{A}$ and $-\frac{B}{A}$.  
In our case, the slopes are $\pm 2$. So either $\frac{B}{A} = 2$ or $\frac{B}{A} = -2$ (but A, B are lengths so positive).  
This implies one slope is $-2$, which is consistent.  
Thus, the equation of the hyperbola can be written in terms of shifted coordinates $(X,Y)$ centered at $(5,7)$.  
The asymptotes are $Y = \pm 2X$.  
Let's check the point $P(4,7)$ which corresponds to $(-1,0)$ in $(X,Y)$.  
Substitute $x=4, y=7$ into equation. Or simply find $X=-1, Y=0$.  
The equation must pass through $(-1, 0)$.  
If form is $\frac{X^2}{A^2} - \frac{Y^2}{B^2} = 1$:  
$(-1)^2 / A^2 - 0 / B^2 = 1 \implies 1/A^2 = 1 \implies A^2 = 1$. So $A=1$ (or any $\pm$). But let's call it $a^2$.  
Then $B/A = 2 \implies B^2 = 4a^2$.  
The equation is $\frac{X^2}{a^2} - \frac{Y^2}{4a^2} = 1$ with $a=1$. $\frac{X^2}{1} - \frac{Y^2}{4} = 1$.  
Does this make sense?  
Asymptotes: $Y = \pm 2X$. Yes.  
Passes through $(0,7)$? Center is $(5,7)$. Point is $(4,7)$. In shifted coords: $(x-5)^2 / a^2 - (y-7)^2 / b^2 = 1$.  
At point $(4,7)$, $X=-1$, $Y=0$.  
$\frac{(-1)^2}{a^2} - \frac{0}{b^2} = 1 \implies a^{-2} = 1 \implies a=1$ (assuming $a>0$).  
Then hyperbola equation: $\frac{(x-5)^2}{1} - \frac{(y-7)^2}{4} = 1$.  

    *   What if the form is $\frac{Y^2}{A^2} - \frac{X^2}{B^2} = 1$?  
This corresponds to a hyperbola opening vertically.  
Asymptotes are $Y = \pm \frac{B}{A} X$. Here slopes $\pm 2$. So $B/A = 2$.  
Passes through $(-1, 0)$ (since $(4,7) \to (-1,0)$).  
$0 / A^2 - (-1)^2 / B^2 = 1 \implies -1/B^2 = 1$, impossible for real $B$. Or $Y=0$ is a point on the hyperbola. For $Y^2/A^2 - X^2/B^2 = 1$, if $Y=0$, then $X^2 = B^2$, $X = \pm B$. So $(-1, 0)$ means $X=-1, Y=0$.  
Then $0^2/A^2 - (-1)^2/B^2 = 1 \implies -1/B^2 = 1$, which has no solution for real $B$.  
Thus, the hyperbola cannot open vertically in this shifted frame. It must open horizontally (in terms of X).  
So the form is $\frac{X^2}{a^2} - \frac{Y^2}{b^2} = 1$ with $a, b > 0$.  
We found earlier:  
Point $(-1, 0)$ implies $1/a^2 - 0 = 1$, so $a=1$.  
Slopes are $\pm 2$, which means $b/a = 2 \implies b = 2a = 2$.  
So equation is $(x-5)^2/1 - (y-7)^2/4 = 1$.  

    *   Let's double check.  
Equation: $(x-5)^2 - (y-7)^2/4 = 1$.  
Asymptotes: $(x-5) / \sqrt{1} = \pm (y-7)/\sqrt{4}$?  
From $\frac{(x-5)^2}{1} - \frac{(y-7)^2}{4} = 0$, we get $\frac{x-5}{1} = \pm \frac{y-7}{2}$. No.  
Let's re-derive asymptote from equation $\frac{x^2}{A^2} - \frac{y^2}{B^2} = 1$.  
$x^2/B^2 \dots$ Multiply by $A^2 B^2$: $B^2 x^2 - A^2 y^2 = A^2 B^2$.  
Asymptotes: $B^2 x^2 - A^2 y^2 = 0 \implies y = \pm (B/A) x$.  
Slopes are $\pm B/A$.  
Here slopes are $\pm 2$. So $B/A = 2$.  
The hyperbola equation must be $\frac{(x-5)^2}{a^2} - \frac{(y-7)^2}{b^2} = 1$?  
Let's check the slope calculation again.  
Equation: $\frac{X^2}{A^2} - \frac{Y^2}{B^2} = 1$.  
Asymptotes: $Y^2/B^2 = X^2/A^2$ (since RHS must be non-zero? Or rather if we move 1 to RHS).  
Actually, asymptote is defined by $L^2 = C$. So $\frac{(x-h)^2}{a^2} \pm \frac{(y-k)^2}{b^2} = 0$.  
If term 1 is positive and term 2 negative: $(x-h)^2/a^2 - (y-k)^2/b^2 = 0 \implies \frac{x-h}{a} = \pm \frac{y-k}{b} \implies y-k = \mp \frac{b}{a}(x-h)$.  
Slope $m = \mp b/a$. Here slopes are $\pm 2$. So $b/a = 2$ (assuming we pick positive slope).  
Or is it possible that term 2 is positive? $(y-k)^2/b^2 - (x-h)^2/a^2 = 0$. Slope would be $\pm b/a$ for $y-k = \pm a/b (x-h)$.  
Since slopes are $\pm 2$, we have two options.  
Case 1: $b/a = 2$ implies $Y/X = \pm 2$. If hyperbola is $X^2 - Y^2 = C$, asymptotes are $Y = \pm X$. (Slope 1). Here slope is 2. So this works.  
In this case, for the point $(x,y)$ which corresponds to $(-1,0)$ to work on hyperbola, we must have $\frac{X^2}{A^2} - \frac{Y^2}{B^2} = 1$?  
Or maybe $\frac{Y^2}{A^2} - \frac{X^2}{B^2} = 1$ gives vertical asymptotes $y=k$ if B is infinite?  
If it's the horizontal hyperbola ($\pm X^2 \mp Y^2$), the asymptotes pass through origin with slope $\pm b/a$.  
Since slopes are $\pm 2$, and $b,a$ positive, we have $b/a = 2 \implies b=2a$.  
Then point $(-1,0)$ on hyperbola $\frac{x^2}{A^2} - \frac{y^2}{B^2} = 1$:  
$(-1)^2/A^2 - 0/B^2 = 1 \implies 1/A^2 = 1 \implies A^2 = 1$.  
Then $B = 2A = 2 \implies B^2 = 4$.  
So $\frac{(x-5)^2}{1} - \frac{(y-7)^2}{4} = 1$.  
Distance between foci: For hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$, $c^2 = a^2 + b^2$.  
Here $c_{centered}^2 = 1 + 4 = 5$. So $c_{centered} = \sqrt{5}$.  
The foci are shifted back by $(h,k) = (5,7)$ to $(5-\sqrt{5}, 7+\text{shift})$?  
Center is at $(5,7)$. Foci are at $(5 \pm c, 7)$ or something.  
For horizontal hyperbola ($a^2 < b^2$ usually, $X^2/A^2 - Y^2/B^2 = 1$), foci are on X-axis in centered frame. $c = \sqrt{a^2+b^2}$. So foci at $(h\pm c, k)$.  
Distance between foci is $2c$.  
Here distance is $2\sqrt{5}$.  

    *   Let's check if the other orientation works.  
Suppose the hyperbola is $\frac{(y-7)^2}{a^2} - \frac{(x-5)^2}{b^2} = 1$ (vertical opening).  
Then asymptotes are $Y = \pm a/b X$. Slopes are $\pm a/b$.  
We are given slopes $\pm 2$. So $a/b = 2 \implies b = a/2$.  
The point $(4,7)$ corresponds to $(-1,0)$ in the shifted frame. Substitute into equation:  
$\frac{(-1)^2}{?} - \dots$  
Equation becomes $Y^2/a^2 - X^2/b^2 = 1 \implies Y^2/a^2 - X^2/(4a^2) = 1$.  
Substitute $(-1,0)$: $0 - (-1)^2/(4a^2) = 1 \implies -1/(4a^2) = 1$. Impossible for real $a,b$.  
Therefore, the hyperbola must be the horizontal type $\frac{(x-5)^2}{A^2} - \frac{(y-7)^2}{B^2} = 1$ or rotated?  
If it's rotated by some angle, say the slope is not constant $m$. But asymptotes are given as linear equations. The center is fixed.  
If the asymptotes are $L_1$ and $L_2$, then the hyperbola is defined by being between these lines in a certain region (if it's a rectangular hyperbola) or simply passing through specific point.  
But for general hyperbola, $\frac{u^2}{A} - \frac{v^2}{B} = 1$ with asymptotes $uv = 0$. The slopes are determined by the coefficients of the equation in the rotated frame if not aligned with axes.  
However, given two lines passing through a center with slopes $\pm 2$, they form a rectangular coordinate system for that center?  
The angle between them is $\arccos(\frac{m_1 - m_2}{\sqrt{(1+m_1^2)(1+m_2^2)}})$ ?  
No, the lines are not perpendicular ($4$ vs $-1$). So we don't have an implicit rectangular grid.  
The hyperbola axes must be aligned with the principal axes of the asymptotes or something?  
Let's formalize:  
The asymptotes of a central conic section $\frac{x^2}{A^2} + \frac{y^2}{B^2} = 1$ are $y = \pm (B/A)x$.  
If we shift coordinates to center $(5,7)$, we get $Y = \pm kX$ where $k = B/A$.  
Here the slopes are $\pm 2$, so one is 2, other -2. This matches exactly with the form $\frac{(x-5)^2}{A^2} - \frac{(y-7)^2}{B^2} = 1$ (or swapped).  
We already showed that for the point $(4,7)$ to lie on it, we need:  
Case 1: Horizontal orientation $\frac{(x-5)^2}{A^2} - \frac{(y-7)^2}{B^2} = 1$.  
Shifted coords $(-1,0)$.  
$(-1)^2/A^2 - 0 = 1 \implies A=1$ (or $\pm 1$, but length is positive).  
Then $B/A = 2 \implies B=2$.  
So hyperbola: $\frac{(x-5)^2}{1} - \frac{(y-7)^2}{4} = 1$.  

Case 2: Vertical orientation $\frac{(y-7)^2}{A^2} - \frac{(x-5)^2}{B^2} = 1$.  
Shifted coords $(-1,0)$.  
$0 - (-1)^2/B^2 = 1 \implies -1/B^2 = 1$, impossible.  
So Case 2 is invalid for real hyperbola.  

*   Is there any other interpretation?  
What if the asymptotes are not aligned with the axes of the hyperbola (rotated)?  
"Asymptotes are $y=2x-3$ and $y=-2x+17$."  
The center is $(5,7)$.  
These lines are fixed.  
If a hyperbola has these asymptotes, its equation can be written in the form:  
$\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$ or similar?  
The general second degree equation with equal coefficients for $x^2$ and $y^2$ terms but different signs, centered at $(h,k)$, is $\frac{X^2}{a^2} \pm \frac{Y^2}{b^2} = 1$.  
If we rotate the hyperbola axes, it becomes a rotated conic.  
But asymptotes of a rotated hyperbola are lines passing through center with slopes $m_1, m_2$ satisfying specific product?  
Let's check.  
General equation $\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1$ is ellipse.  
Hyperbola: $\frac{(x-h)^2}{A} - \frac{(y-k)^2}{B} = 1$. Asymptotes are $(y-k) = \pm \sqrt{B/A}(x-h)$? Or $y-k = \pm (a/b)(x-h)$?  
From $\frac{X^2}{A} - \frac{Y^2}{B} = 0$, we get $X/A = Y/B \implies Y/X = B/A$. No.  
$\frac{X^2}{A} = \frac{Y^2}{B} \implies X/Y = A/B$ or $Y/X = \sqrt{B/A}$?  
If $x^2/a^2 - y^2/b^2 = 0$, then $y = \pm (b/a)x$.  
So the slopes are $\pm b/a$.  
Here slopes are $\pm 2$.  
This implies the hyperbola axes *in the local frame* $(X,Y)$ relative to the asymptotes...  
The slopes of asymptotes are simply defined by the coefficients of $x,y$ in the linear equations.  
So, if the asymptotes are $y = m x + c_1$ and $y = m' x + c_2$, the hyperbola (when shifted) will be such that its principal axes are aligned with the directions perpendicular to these slopes?  
Let's look at it algebraically.  
The equation of a conic is $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$.  
Since asymptotes intersect at center, we can set $(x,y) = (X+5, Y+7)$ to get center shifted to origin.  
Equation: $a X^2 + b XY + c Y^2 + d X + e Y + f = 0$.  
The lines are given as $Y-7 = \pm 2(X-5) \implies (y-7)^2 - 4(x-5)^2$?  
The asymptotes of $ax^2 + \dots = 1$ or something.  
Actually, for a conic with asymptotes, the equation can be written as:  
$(Ax+By+C)(Ax'+By'+C') + \dots = 0$.  
If asymptotes are lines passing through origin of new coords, then the terms containing $X^2$ and $Y^2$ must cancel each other out or be proportional to something?  
The hyperbola equation in standard form is $x^2/a^2 - y^2/b^2 = 1$. Asymptotes are $y = \pm b/a x$.  
So the slopes are fixed by the ratio of coefficients.  
Here, we know the slopes are $\pm 2$.  
This implies $b/a = 2$ in some sense.  
But which axis is horizontal?  
The hyperbola could be "vertical" (opening up/down) with respect to the $x,y$ axes, or "horizontal" (opening left/right).  
If it's vertical, asymptotes slopes $\pm b/a$ means $b/a = 2$. The hyperbola opens in $y$ direction. Equation: $Y^2/A^2 - X^2/B^2 = 1$. But we found this leads to contradiction for point $(4,7)$ (which is at $X=-1, Y=0$).  
So the hyperbola must open horizontally with respect to the center frame.  
Thus, it is of the form $X^2/A^2 - Y^2/B^2 = 1$.  
The slopes of asymptotes for this form are $\pm B/A$.  
We have slopes $\pm 2$. So $B/A = 2 \implies B=2A$.  
The hyperbola passes through $(4,7)$.  
Shifted to center: point is $(-1, 0)$ in $X,Y$ coordinates? Let's check again.  
$x-5 = -1$, $y-7 = 0$. Yes.  
Substitute into $\frac{X^2}{A^2} - \frac{Y^2}{B^2} = 1$:  
$\frac{(-1)^2}{A^2} - \frac{0^2}{B^2} = 1 \implies \frac{1}{A^2} = 1 \implies A=1$.  
Then $B/A = 2 \implies B=2$.  
So $\frac{(x-5)^2}{1} - \frac{(y-7)^2}{4} = 1$.  

    *   Let's check if there is any ambiguity.  
Are the asymptotes perpendicular?  
Slopes $2$ and $-2$. Product $-4$. Not perpendicular.  
If they were $\pm 1$, we would have a rectangular hyperbola? Or axes are at 45 degrees to asymptotes.  
Here axes are along the line connecting vertices $(h \pm c, k)$?  
For $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$, the axes of symmetry (focal axis) is the x-axis in the $x,y$ frame.  
The asymptotes have slopes $\pm b/a$.  
So, given that the slopes are $\pm 2$, we identify this as a standard hyperbola with semi-major axis $a$ and semi-minor axis $b$? Or rather $a$ and $b$.  
In this notation, slope is $b/a$. So $b/a = 2$.  
This implies the hyperbola opens along the x-axis (in local frame).  
This corresponds to $\frac{(x-5)^2}{a^2} - \frac{(y-7)^2}{b^2} = 1$.  
We solved this: $a=1, b=2$. Focal distance calculation depends on $c = \sqrt{a^2+b^2} = \sqrt{1+4} = \sqrt{5}$.  
Distance between foci = $2c = 2\sqrt{5}$.  

    *   Is there any chance the hyperbola is of the form $\frac{(x-5)^2}{a^2} - \frac{(y-7)^2}{b^2} = 1$ but rotated?  
If the asymptotes are $y=2x+7$ and $y=-2x+17$.  
The center is $(5,7)$.  
Any hyperbola  

## Answer

*(none: the token cap hit during thinking)*
