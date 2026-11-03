# test/intermediate_algebra/1797.json (Intermediate Algebra, level 4)

> The asymptotes of a hyperbola are $y = 2x - 3$ and $y = 17 - 2x.$  Also, the hyperbola passes through the point $(4,7).$  Find the distance between the foci of the hyperbola.  

**Wrong.** Gold `2 \sqrt{5}`, predicted `None`. Finish: length, 8192 tokens, 1 waits, 659.7 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here is my thought process for solving this problem:  

1.  **Analyze the Request:**  
    *   **Given:** An asymptote equation ($y = 2x - 3$), another asymptote equation ($y = -2x + 17$), and a point on the hyperbola $(4, 7)$.  
    *   **Goal:** Find the distance between the foci.  
    *   **Format:** Step-by-step reasoning, final answer in `\boxed{}`.  

2.  **Recall Properties of Hyperbolas:**  
    *   A hyperbola is defined by two perpendicular asymptotes (for a general rectangular hyperbola) or just asymptotes that intersect at the center.  
    *   The equations of asymptotes for a hyperbola with horizontal/vertical transverse axis are $y = mx + c$ and $y = -\frac{b}{a}x \pm 2c$? No, let's use the standard forms.  
    *   Standard equation: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$. Asymptotes are $y = \pm \frac{b}{a}x$.  
    *   Center of hyperbola $(h, k)$. The equations of asymptotes can be found as: $A x + B y + C = 0$ (where $\frac{B}{A}$ is related to slope). Here the slopes are $2$ and $-2$. This implies a rectangular hyperbola because the product of slopes is $-4 \neq -1$.  
    *   Let's check if it's a general hyperbola. The asymptotes intersect at the center.  
    *   Equation 1: $y = 2x - 3 \Rightarrow 2x - y - 3 = 0$.  
    *   Equation 2: $y = -2x + 17 \Rightarrow 2x + y - 17 = 0$.  
    *   Intersection of asymptotes (which is the Center, denoted as $(h,k)$):  
        *   From Eq 1: $y = 2(4) - 3$? No, solve for intersection.  
        *   $2x - y - 3 = 0 \Rightarrow 2x = y + 3$.  
        *   $2x + y - 17 = 0 \Rightarrow 2x = 17 - y$.  
        *   Set equal: $y + 3 = 17 - y \Rightarrow 2y = 14 \Rightarrow y = 7$.  
        *   Then $x = (7+3)/2 = 5$. Or $x = (17-7)/2 = 5$.  
    *   So the center is $(h, k) = (5, 7)$.  

3.  **Determine the Orientation of the Hyperbola:**  
    *   The center is $(5,7)$.  
    *   We need to find $a$ and $b$ or just $c^2 = a^2 + b^2$.  
    *   Let's use the asymptote equation form with shifted center coordinates.  
    *   Let $X = x - 5$ and $Y = y - 7$.  
    *   The center is $(0,0)$ in the new coordinate system.  
    *   The original equations are: $y = 2x - 3$ and $y = -2x + 17$.  
    *   Substitute $y = Y+7$ and $x = X+5$:  
        *   First Asymptote: $Y + 7 = 2(X + 5) - 3 \Rightarrow Y + 7 = 2X + 10 - 3 \Rightarrow Y + 7 = 2X + 7 \Rightarrow Y = 2X$.  
        *   Second Asymptote: $Y + 7 = -(2X + 5) + 17$? No, let's just rearrange second one.  
            *   $y = -2x + 17 \Rightarrow (y-7) = -2(x-5) - 14 + 17 = -2(x-5) + 3$? No, simpler: $(-2)(x-5)$. Let's check.  
            *   $-2(x-5) = -2x + 10$. The asymptote is $y+7 = -2x + 17$ (using original eq). So $(Y+7) = -2(X+5) + 17 \Rightarrow Y+7 = -2X - 10 + 17 \Rightarrow Y+7 = -2X + 7 \Rightarrow Y = -2X$.  
    *   This confirms the asymptotes in the centered coordinates are $Y = 2X$ and $Y = -2X$.  
    *   Since the equation of the hyperbola is $\frac{X^2}{a^2} - \frac{Y^2}{b^2} = 1$ (horizontal transverse axis) or $\frac{Y^2}{a^2} - \frac{X^2}{b^2} = 1$ (vertical), and the asymptotes are $Y = \pm m X$, where $m = b/a$.  
    *   Here $Y/X = \pm 2$. So $\frac{b}{a} = 2$ or $\frac{b}{a} = -2$. Since slope magnitude is taken, $|b|/|a| = 2$. Thus $b = 2a$.  

4.  **Analyze the Point (4,7):**  
    *   The point given is $P(4,7)$.  
    *   Does this point lie on the hyperbola? Yes, stated in the problem.  
    *   Let's translate $P$ back to centered coordinates $(X, Y)$:  
        *   $x = 4 \Rightarrow X = x - h = 4 - 5 = -1$.  
        *   $y = 7 \Rightarrow Y = y - k = 7 - 7 = 0$.  
    *   So the point corresponds to $(-1, 0)$.  

5.  **Check if this makes sense:**  
    *   We have a hyperbola centered at $(5,7)$ with asymptotes slope $\pm 2$ through origin in centered coords.  
    *   The equation is $\frac{X^2}{a^2} - \frac{Y^2}{b^2} = 1$ OR $\frac{Y^2}{a^2} - \frac{X^2}{b^2} = 1$.  
    *   Since the slope $m=2$ is related to $b/a$, it's not clear which form, but let's look at the asymptotes equations.  
    *   Asymptote: $Y = \pm 2X$. This means the slopes are $\pm 2$. So $b/a = 2$ in both cases? No.  
        *   If eq is $X^2/a^2 - Y^2/b^2 = 1$, asymptotes are $Y = \pm (b/a) X$. Here slope $\pm 2$. So $b/a = 2$. Thus $b = 2a$.  
        *   If eq is $Y^2/a^2 - X^2/b^2 = 1$, asymptotes are $Y = \pm (a/b) X$? No. The equation of asymptotes for vertical axis hyperbola is $Y = \pm (a/b) X$ where $b$ is under the other term. Let's re-derive.  
            *   Equation: $\frac{X^2}{A} - \frac{Y^2}{B} = 1$. Asymptotes $Y^2/B = X^2/A \Rightarrow Y = \pm \sqrt{B/A} X$. So slope is $\pm \sqrt{B/A}$.  
            *   Here slopes are $\pm 2$. So $\sqrt{b_{term}/a_{term}} = 2$. Let's call the denominators $A, B$ for generic terms $u^2/A - v^2/B = 1$.  
            *   For $X^2/a^2 - Y^2/b^2 = 1$, slope is $\pm b/a$. We have $\pm 2$. So $b/a = 2 \Rightarrow b = 2a$. Then $b_{term} = 4a^2$? No.  
            *   Let's stick to the notation: $\frac{X^2}{h} - \frac{Y^2}{k} = 1$. Asymptotes are $y = \pm \sqrt{k/h} x$ (where Y is new). So slope is $\sqrt{k/h}$. We have slope $= 2$.  
            *   Let's check the other axis. Is it vertical or horizontal?  
            *   Point $P(-1, 0)$ corresponds to center $(5,7)$. The point lies on the "X-axis" ($Y=0$) in the centered coordinate system.  
            *   In a hyperbola $\frac{X^2}{a^2} - \frac{Y^2}{b^2} = 1$, points with $Y=0$ have $X^2/a^2 = 1 \Rightarrow X = \pm a$. So the vertices are at $(-1,0)$?  
            *   If the vertex is at $(-1,0)$ in $(X,Y)$ coordinates relative to center, then the distance from the center to the vertex is 1.  
            *   In standard form $\frac{u^2}{A} - \frac{v^2}{B} = 1$, vertices are at $(\pm \sqrt{A}, 0)$.  
            *   Here our point is $(-1,0)$ relative to center. So we must have $\sqrt{A} = 1$ (assuming A is associated with the positive term if X-term is positive).  
            *   So the term for $X$ is likely squared over $a^2$ or $b^2$?  
    *   Let's re-evaluate. We have asymptotes slopes $\pm 2$. This means the slope of lines passing through center tangent to the hyperbola at infinity? No, just the asymptote slopes.  
    *   In equation form $\frac{X^2}{A} - \frac{Y^2}{B} = 1$, slopes of asymptotes are $\pm \sqrt{B/A}$. Given slopes $\pm 2$, we have $B/A = 4$. So $B = 4A$.  
        *   Case 1: $X^2/A - Y^2/(4A) = 1$. This opens along X-axis. Vertex at $(\pm \sqrt{A}, 0)$. The point $(-1, 0)$ must satisfy this.  
        *   $(-1)^2/A - (0)^2/(4A) = 1 \Rightarrow 1/A = 1 \Rightarrow A = 1$.  
            *   If $A=1$, then $B=4$. Equation: $X^2 - Y^2/4 = 1$. Vertices at $(\pm 1, 0)$? No.  
            *   Let's check standard form again. $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$. Asymptotes $y = \pm (b/a)x$. Slope is $b/a$. Here slope $= 2$, so $b/a = 2 \Rightarrow b=2a$.  
            *   Then vertices are at $(\pm a, 0)$. The point $(-1,0)$ must be the vertex. So $a=1$.  
            *   Then $b=2$.  
        *   Case 2: $X^2/A + Y^2/B = 1$? No, that's an ellipse.  
        *   So we assume hyperbola opens horizontally in X (centered coords). Equation $\frac{X^2}{a^2} - \frac{Y^2}{b^2} = 1$. Asymptotes $Y = \pm \frac{b}{a} X$. We found $\frac{b}{a} = 2$. The point is $(-1,0)$. Plugging into equation: $\frac{(-1)^2}{a^2} - 0 = 1 \Rightarrow a=1$. So $b=2$.  
    *   Is it possible the hyperbola opens vertically?  
        *   If vertical, eq: $\frac{Y^2}{a^2} - \frac{X^2}{b^2} = 1$. Asymptotes $Y = \pm (a/b) X$. This implies slope is $a/b = 2 \Rightarrow a=2b$.  
        *   Point $(-1,0)$ gives $\frac{(-1)^2}{4a_{new}} - 0$? No. If it opens vertically, vertices are at $(0, \pm c)$. The point $(-1,0)$ would not be on the hyperbola unless...  
        *   Let's check vertex coordinates again. For vertical transverse axis $\frac{Y^2}{a^2} - \frac{X^2}{b^2} = 1$, vertices are $(0, a)$. If $Y=0$ in original centered coords, we have a point on the curve?  
        *   Let's look at the asymptotes again. Asymptotes for vertical hyperbola: $y = \pm (a/b) x$. The slopes $\pm 2$ mean $a/b = 2$ or $b/a=1$? No, slope is $m = a/b$ only if the denominator is under Y?  
        *   Let's verify. $\frac{Y^2}{a^2} - \frac{X^2}{b^2} = 1$. Asymptotes are obtained by setting LHS=0: $Y^2/a^2 = X^2/b^2 \Rightarrow Y = \pm (a/b) X$. So if slopes are $\pm 2$, then $a/b = 2$ or $b/a = 2$? No.  
        *   Let's be precise. $\frac{y^2}{A} - \frac{x^2}{B} = 1$. Asymptotes $y = x\sqrt{A/B}$. Slope is $\pm \sqrt{A/B}$.  
            *   Here slopes are $\pm 2$. So $\sqrt{A/B} = 2 \Rightarrow A/B = 4$. Let's say $A=b^2, B=a^2$ in some notation. Let's call denominator of Y term as $a^2$. Then $Y$-denom over $X$-denom is $4$.  
            *   If this is the case (vertical hyperbola), vertices are at $(0, \pm a)$. The point given is $(4,7) \to (-1, 0)$ in centered coords. It must satisfy $Y=0$?  
            *   Equation: $\frac{Y^2}{a_{vert}^2} - \frac{X^2}{b_{vert}^2} = 1$. If point is on curve and Y-coordinate is $-1$, then $(-1)^2/b_{vert}^2$ term?  
            *   Substitute $X=-1, Y=0$ into equation: $0/a - 1/b^2 = 1 \Rightarrow -1/b^2 = 1$. Impossible for real $a,b$.  
            *   Thus, a vertical hyperbola centered at $(5,7)$ cannot pass through $(-1, 0)$ in the local coordinates. It would require $X$ to be imaginary or the term to be negative? No.  
            *   For $\frac{Y^2}{A} - \frac{X^2}{B} = 1$, at $Y=0$, we must have $-X^2/B = 1$, impossible. So no points with $Y=0$ exist on this curve. Since the point $(-1,0)$ has $Y=0$ (in local coords), the hyperbola MUST open horizontally.  
            *   So, it is definitely a horizontal hyperbola in $(X,Y)$ coordinates centered at origin.  
    *   So we have established:  
        *   Center $(h,k) = (5,7)$.  
        *   Equation in centered coords: $\frac{X^2}{a^2} - \frac{Y^2}{b^2} = 1$.  
        *   Asymptotes slopes $\pm b/a = \pm 2$. So $b/a = 2$.  
        *   Point $(-1,0)$ lies on the hyperbola.  

6.  **Solve for parameters:**  
    *   Equation: $\frac{X^2}{a^2} - \frac{Y^2}{b^2} = 1$.  
    *   Sub-point $(-1, 0)$: $\frac{(-1)^2}{a^2} - 0 = 1 \Rightarrow \frac{1}{a^2} = 1 \Rightarrow a^2 = 1$.  
    *   Relation to asymptotes: $b/a = 2$. Since $a=1$, then $b=2$. So $b^2 = 4$.  
    *   Hyperbola equation: $\frac{X^2}{1} - \frac{Y^2}{4} = 1$.  
    *   Center $(5,7)$ is correct.  

7.  **Calculate Distance between Foci:**  
    *   The standard formula for distance $c$ from center to focus is $c^2 = a^2 + b^2$ for hyperbolas?  
        *   Usually defined as $b^2 + c^2$? No, $a^2 - b^2$. Let's stick to definitions.  
        *   For $\frac{X^2}{a^2} - \frac{Y^2}{b^2} = 1$, foci are at $(h \pm c_x, k)$ with $c$ satisfying $c^2 = a^2 + b^2$? No.  
        *   Let's derive or recall properly.  
        *   Ellipse: $x^2/a^2 + y^2/b^2 = 1$. $c^2 = a^2 - b^2$.  
        *   Hyperbola: $x^2/a^2 - y^2/b^2 = 1$. Foci are at $\pm c$ along transverse axis ($x$). The semi-major axis length is usually defined as 'a' in this case. The focal distance $c$ satisfies $c^2 = a^2 + b^2$. Let's verify.  
        *   If $y=0$, then $x^2/a^2 = 1 \to x = \pm a$. Vertex is at distance $a$ from center. Foci are at $\pm c$.  
        *   By definition, eccentricity $e = c/a$. For hyperbola, $c^2 = a^2 + b^2$ and $e > 1$. Also $b^2 = a^2(e^2-1)$? No.  
        *   Relationship: $\frac{y}{k} \propto \sqrt{\lambda^2 - 1}$? Let's just use the standard property. The asymptotes pass through $(\pm b, \pm a)$ for $x/a = y/b$? No, asymptote slope $b/a$.  
        *   If asymptote equation is $x/a = \pm y/b \implies by = ax \implies y = (a/b)x$? No.  
            *   Standard form: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$.  
            *   Asymptote: $x^2/a^2 - y^2/b^2 = 0 \implies x^2/a^2 = y^2/b^2 \implies x/\sqrt{a^2} = \pm y/\sqrt{b^2}$.  
            *   So asymptotes are $y = \pm (b/a) x$. This matches our slopes $\pm 2$.  
            *   We have established $a^2 = 1$ and $b^2 = 4$.  
        *   Foci distance formula: $c^2 = a^2 + b^2$.  
            *   Is it $c^2 = a^2 - b^2$ or $a^2 + b^2$?  
            *   For $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$, the foci are on the x-axis. $c^2 = a^2 + b^2$. Let's check.  
            *   If $x=0, y= \pm ia/b$? No. At vertex $x=a, y=0$. Focus is at $(\pm c)$. Distance from origin is $c$.  
            *   Consider the intersection of hyperbola branches.  
            *   Let's test with $e = c/a$.  
            *   $y^2/b^2 + x^2/a^2 = 1$ (ellipse). $c^2 = a^2 - b^2$? No, usually $c^2 = a^2 - b^2$.  
            *   Hyperbola: $y^2/b^2 - x^2/a^2 = 1$. Asymptotes are $\pm (a/b) x$. Slope $a/b$.  
            *   Standard text says $c^2 = a^2 + b^2$ for hyperbola.  
            *   Let's check the slope relation. For $\frac{x^2}{A} - \frac{y^2}{B} = 1$, asymptotes have equation $x^2/A - y^2/B = 0$. So $x/ \sqrt{A} = \pm y/\sqrt{B} \implies y = \mp (1/\sqrt{B})\sqrt{A} x$? No.  
                *   $\frac{x}{\sqrt{A}} - \frac{y}{\sqrt{B}} = 0$. $y/x = \sqrt{B/A}$? No, that would be $y^2/B = x^2/A \implies y/x = \pm \sqrt{A/B}$.  
                *   Let's restart the algebra on asymptotes for $\frac{X^2}{a^2} - \frac{Y^2}{b^2} = 1$.  
                *   $X^2/a^2 - Y^2/b^2 = 0 \implies X^2/b^2 = a^2/b^2 ...$ No.  
                *   $X^2/A - Y^2/B = 0 \implies (Y/X)^2 = B/A$. Slopes are $\pm \sqrt{B/A}$.  
                *   In our case, asymptote slope is $b/a$ or something? Let's look at the given equation: $y=2x-3$ and $y=-2x+17$.  
                *   Center $(5,7)$. Transformed coordinates $X=x-5, Y=y-7$.  
                *   Slope of asymptotes in original coords is same as slope in local coords.  
                *   So slopes are $\pm 2$. This means $Y/X = \pm 2$.  
                *   So the equation for hyperbola must be such that $\sqrt{b_{denom}/a_{denom}} = 2$? Or $\sqrt{A/B} = 2$?  
                    *   If form is $\frac{X^2}{a^2} - \frac{Y^2}{b^2} = 1$, asymptotes are $y = \pm (b/a) x$. So $b/a = 2$. Thus $b=2a, b^2=4a^2$.  
                    *   If form is $\frac{Y^2}{a^2} - \frac{X^2}{b^2} = 1$, asymptotes are $y = \pm (a/b) x$ (no, let's verify).  
                        *   $Y^2/a^2 - X^2/b^2 = 0 \implies Y^2/b^2 = X^2/a^2 \implies Y = \pm (b/a) X$.  
                        *   So the slope is always $\sqrt{A/B}$ where A is the denominator under the minus term? No.  
                        *   If eq is $x^2/A - y^2/B = 1$, asymptotes are $y = \pm \sqrt{B/A} x$.  
                            *   Let's verify this again. At infinity, $x^2/A - y^2/B \approx 0 \implies (y/\sqrt{B}) = \pm (x/\sqrt{A})$. So slope $m = \sqrt{B/A}$? No, it's $\sqrt{B/A} x$ so $y/x = \pm \sqrt{B/A}$? No, this is wrong.  
                            *   If $y^2/b^2 - x^2/a^2 = 1$, asymptotes are $y^2/b^2 = x^2/a^2 \implies y/x = \pm (b/a)$. So slope is $\pm b/a$.  
                            *   So let's call denominators $A, B$ for terms $x^2/A - y^2/B = 1$. Asymptotes: $y/x = \pm \sqrt{B/A}$. No, this implies slope is $\sqrt{B/A}$.  
                            *   Let's do a simple test. $x^2 - y^2 = 1$. Slopes are $\pm 1$. $A=1, B=1$. $\sqrt{1/1} = 1$. Correct.  
                            *   Test: $x^2/4 - y^2/9 = 1$. Slopes are $\pm 3/4$? No, $y/x = \pm \sqrt{9/4} = \pm 3/4$. Correct. So slope is $\sqrt{B/A}$.  
                            *   In our problem, slopes are $\pm 2$.  
                            *   This means $\sqrt{B/A} = 2 \implies B/A = 4$.  
                            *   Let's check my previous deduction about horizontal vs vertical.  
                                *   If hyperbola is $X^2/a^2 - Y^2/b^2 = 1$ (horizontal opening). Asymptote equation derived earlier was $Y = \pm (b/a) X$. So slope is $\pm b/a$.  
                                    *   Here $B_{term}$ under X term? No. $X$ has coeff $a^2$, $Y$ has coeff $b^2$. Equation $\frac{X^2}{A} - \frac{Y^2}{B} = 1$.  
                                    *   Asymptotes: $y/x = \pm \sqrt{B/A}$. So slope is $\sqrt{B/A}$.  
                                    *   If this is the case, then $b/a$ corresponds to $\sqrt{A_{denom}/B_{denom}}$? No. Let's write it clearly.  
                                    *   Equation: $\frac{x^2}{h^2} - \frac{y^2}{k^2} = 1$. (Horizontal opening). Asymptote slope $m = \pm k/h$. Here we have slopes $\pm 2$. So $k/h = 2$. Thus $k=2h, k^2=4h^2$.  
                                    *   In this case, point $(-1,0)$ is on curve: $(-1)^2/h^2 - 0 = 1 \implies h^2 = 1 \implies h=1$.  
                                    *   So $k=2$.  
                                    *   Parameters are $h_{hyperbola\_param} = 1$ and $k_{hyperbola\_param} = 2$.  
                                    *   Distance between foci: For $\frac{x^2}{h^2} - \frac{y^2}{k^2} = 1$, foci are at $(\pm c, 0)$ where $c^2 = h^2 + k^2$ (using standard notation where $a=h, b=k$).  
                                        *   So $c^2 = 1^2 + 2^2 = 5$. Distance is $\sqrt{5}$.  
                                *   What if hyperbola is vertical opening?  
                                    *   Equation: $\frac{x^2}{k^2} - \frac{y^2}{h^2} = 1$? No, that's horizontal. Vertical: $\frac{y^2}{h^2} - \frac{x^2}{k^2} = 1$.  
                                    *   Here $a=h, b=k$. Asymptotes slopes: $y/x = \pm h/k$. (Since $y^2/h^2 = x^2/k^2$). So slope is $\pm h/k$.  
                                    *   We have slopes $\pm 2$. So $h/k = 2$.  
                                    *   Point on curve: $(4,7) \to (-1, 0)$ in centered coords.  
                                    *   Substitute into equation $\frac{y^2}{h^2} - \frac{x^2}{k^2} = 1$. Note that Y is y-coordinate relative to center? Yes. $Y=y-7$.  
                                    *   At point $(-1,0)$, $Y=0$.  
                                    *   Equation: $\frac{0}{h^2} - \frac{(-1)^2}{k^2} = 1 \implies -1/k^2 = 1 \implies k^2 = -1$. Impossible.  
                                    *   So the hyperbola cannot be vertical (in centered coords). It must be horizontal.  

    *   **Re-evaluating "Slopes" vs "Standard Form".**  
        *   Hyperbola asymptotes: $y-7 = m(x-5)$.  
        *   $m^2 = 4$? No, product of slopes for orthogonal hyperbola is -1. Here product is $-4$. So not rectangular.  
        *   Let's use the general property: The distance between foci is determined by the center $(h,k)$ and one of the parameters related to asymptotes passing through it.  
        *   Since the point $(-1,0)$ lies on the hyperbola, we have a "vertex" at $x=-1$?  
            *   Let's look at the form $\frac{(x-5)^2}{a^2} - \frac{(y-7)^2}{b^2} = 1$.  
            *   We found slopes are $\pm b/a$. We have slopes $\pm 2$. So $b/a = 2 \implies a=1, b=2$ (or vice versa depending on orientation).  
            *   If horizontal: $\frac{(x-5)^2}{a^2} - \frac{(y-7)^2}{b^2} = 1$. The term $x$ must be positive to get slope. Yes, $(x-5)$ is linear in denom? No. Denom is squared.  
            *   Slope comes from $\sqrt{B/A} = b/a$. So if slopes are $\pm 2$, then $b/a = 2$.  
            *   Since point is on curve and has $y$-coordinate same as center (in shifted coords), the term with $(y-k)$ must be zero? Yes, in my derivation I used Y as shift. $Y = y-7$. At point $(4,7) \to (-1, 0)$, $Y=0$.  
            *   Equation at $Y=0$: $\frac{(-1)^2}{a^2} - 0 = 1 \implies a^2 = 1$.  
            *   We know $b/a = 2$. Since $a^2=1$, $b^2 = 4$.  
            *   So equation is $\frac{(x-5)^2}{1} - \frac{(y-7)^2}{4} = 1$.  
        *   Now, distance between foci $c$.  
            *   For this form (horizontal), $c^2 = a^2 + b^2$ is NOT correct. Let's check definitions carefully.  
            *   Hyperbola: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$. Foci at $(\pm c, 0)$ where $c = \sqrt{a^2 + b^2}$?  
                *   Let's check this property.  
                *   Standard ellipse: $c^2 = a^2 - b^2$.  
                *   Standard hyperbola: $c^2 = a^2 + b^2$. (This is the definition where vertices are at distance $a$ and asymptotes make angle $\theta$ such that $\tan(2\alpha) = ...$).  
                *   Let's derive $e$. For hyperbola, $b/a = \cot(\beta)$? No.  
                *   Asymptote makes angle $\phi$ with x-axis. $\tan(\phi) = b/a$. Then $\cos^2 \phi = a^2/(a^2+b^2)$ and $\sin^2 \phi = b^2/(a^2+b^2)$.  
                *   Foci are at $c$ along the x-axis. $c = ae$.  
                *   If asymptote slope is $m$, then $e \tan \alpha = m$. No, $e = \sqrt{1 + 1/(b/a)^2}$? No.  
                *   $b^2/a^2 = e^2 - 1$.  
                *   Let's check relation to $c$.  
                *   For $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$, the foci are at $(\pm c, 0)$ with $c = \sqrt{a^2 + b^2}$.  
                *   Let's verify this. Intersection of hyperbola and asymptote? No.  
                *   Check point on curve. Vertex at $(a,0)$. Asymptote passes through origin. Angle $\alpha$ between tangent and x-axis?  
                *   Consider $x = \cosh t \cdot a$. $y = \sinh t \cdot b$. (Hyperbolic param).  
                *   Focal distance: $2c$. Distance from center to focus is $c$.  
                *   Formula is definitely $c^2 = a^2 + b^2$? No, that's not right for all cases.  
                *   Let's check the ellipse case. $a=5, b=3, c= \sqrt{16} = 4$. $a > c$. Correct.  
                *   For hyperbola, $a$ and $b$ are usually defined such that $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$. Here the term "transverse axis" corresponds to $x$, length $2a$. Wait.  
                    *   Let's check Wikipedia or similar mental reference.  
                    *   Equation: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$. Foci are at $(\pm c, 0)$.  
                    *   Relationship is $c^2 = a^2 + b^2$? No.  
                    *   Let's calculate for a specific example: $x^2/4 - y^2/3 = 1$.  
                        *   $a^2 = 4, b^2 = 3$.  
                        *   Vertex at $(\pm 2, 0)$. Focus is at $(c,0)$?  
                        *   If formula $c = \sqrt{a^2+b^2}$ holds, then $c = \sqrt{7}$.  
                        *   Is it correct?  
                        *   The definition of hyperbola: distance to focus minus distance to directrix. Directrix is $x = a/e$ where $e = c/a$.  
                            *   If $c = \sqrt{a^2+b^2}$, then $e = \sqrt{a^2/b^2 + 1}$.  

## Answer

*(none: the token cap hit during thinking)*
