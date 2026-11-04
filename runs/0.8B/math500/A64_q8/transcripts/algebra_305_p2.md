# test/algebra/305.json, part 2 of 2

[Previous part](algebra_305.md)

Step 2: Identify $a$ and $b$.  
Step 3: Identify $c$ from horizontal asymptote.  
Step 4: Sum them.  

Roots of $x^2 - 5x - 14$:  
$x = \frac{5 \pm \sqrt{25+56}}{2} = \frac{5 \pm 9}{2}$.  
$x_1 = 7, x_2 = -2$.  
$a=7, b=-2$ (or vice versa). Sum $a+b=5$.  
Degree of numerator is 1. Degree of denominator is 2. $\lim_{x\to\infty} f(x) = 0$. So $c=0$.  
Sum $a+b+c = 5+0 = 5$.  

Double check the wording "graph ... has vertical asymptotes x=a and x=b".  
Sometimes problems have phrasing like "The graph of ... has asymptotes $y=ax+b$". No, usually just lines.  
If the graph had a horizontal asymptote, it means the line $y=c$ is the top/bottom behavior. Here, since $c=0$, the horizontal asymptote is the x-axis.  
So we have asymptotes $x=-2$ and $x=7$.  
The sum of coordinates of these points on the y-axis or whatever? No, x-coordinate.  

If there was any ambiguity about "horizontal asymptote" meaning slope or something, it would be trivial ($c=0$).  
If vertical asymptote means root location, then yes.  

I will write down the solution clearly.  

One edge case: what if $x^2-5x-14 = (x+6)(x-7)$? No, check roots of $(x+6)(x-7)$. $x^2 - 5x - 39 \neq x^2-5x-14$.  
So the factorization is correct.  
What about $x=2$? $2^2-10-14 < 0$. $x=-2$ is asymptote.  

Okay, I'm done thinking. The answer is 5.  
But just to ensure no other interpretation: what if "graph" refers to something like a specific graph where coordinates are defined differently? No.  

Is there any possibility that the roots of denominator were wrong?  
$x^2 - 5x - 14$.  
Try $x=7$: $49-35-14 = 0$. Yes.  
Try $x=-2$: $4-(-10)-14 = 4+10-14 = 0$. Yes.  
So roots are indeed $\pm 2$ relative to the coefficients? No, roots are $\pm 7/2$ and... no.  
Roots are $\frac{5 \pm \sqrt{81}}{2} = \frac{5 \pm 9}{2}$.  
$x_1 = 7, x_2 = -2$.  
So sum is $5$.  

Final Answer: 5.  
The values are $a=7$ and $b=-2$ (or vice versa). The sum of their coordinates is 5.  

I will just write out the reasoning clearly in the final response.  

One thought: "Find a+b+c" might mean $a+b+c = (\text{something}) + c$. If I am missing something, I can't see it.  
Given the phrasing, this looks like a straightforward application of properties of rational functions.  

Let's assume the question is from a context where $x=a$ implies specific values derived from the problem.  
Could "a" and "b" be something related to coefficients? No.  
I'll stick with 5.  

One weird possibility: The function might not be defined at asymptotes? Yes, it's undefined.  
Are vertical asymptotes always lines?  
If $f(x) = \frac{x}{x-1}$, as $x \to 1$, $f(x) \to \infty$. Vertical asymptote is $x=1$.  
Is there any "horizontal asymptote" that would be different? No.  
Just check if the denominator is reducible. It's $(x+2)(x-7)$.  
So vertical asymptotes at $x=-2, x=7$.  
Limit is 0.  
Sum is 5.  

I am ready.  

One last check: Is it possible that "vertical asymptote" means the line passing through a point where function goes to infinity? Yes, these are the lines $x=-2$ and $x=7$.  
So "a+b+c" sums up to 5.  

If the question meant $a,b,c$ as coordinates on the axes? No, usually they denote asymptotes as equations.  
If $f(x) = \dots$ has asymptotes at $x=a$, then $a=-2$ or $7$.  
Is it possible that $a+b+c$ refers to roots of something else?  
No, context implies graph properties.  

I will formulate the response now.  
The steps are:  
1.  Find vertical asymptotes by solving $x^2 - 5x - 14 = 0$. This yields roots $x=-2$ and $x=7$. Thus $a,b$ correspond to $\{-2, 7\}$.  
2.  Find horizontal asymptote as $x \to \infty$: degree of numerator (1) < degree of denominator (2). Ratio goes to 0. So $c=0$.  
3.  Sum: $-2 + 7 + 0 = 5$.  

If the question asked for $a+b$, the answer would be 5. Since it asks for $a+b+c$, and $c$ is a value, it's likely $c \neq -b+a$.  
If I assume order $a=7, b=-2$, sum is 5. If $a,b$ are just labels for roots, sum is invariant.  

I'll provide the reasoning based on these steps.  

What if $f(x)$ is not defined everywhere? The graph has asymptotes $x=a$. This implies vertical lines.  
So yes.  

Okay, done.  


## Answer

To find the values of $a$, $b$, and $c$ for the function $f(x) = \frac{2x}{x^2-5x-14}$, we analyze its asymptotic behavior step by step.  

**1. Vertical Asymptotes:**  
Vertical asymptotes occur where the denominator of the rational function is zero (assuming the numerator and denominator do not have common factors that cancel out to form a removable discontinuity, which isn't the case here since $\gcd(2x, x^2-5x-14) \neq 0$).  
The function can be rewritten as:  
$$ f(x) = \frac{2x}{(x-7)(x+2)} $$  
We find the roots of the denominator by setting the polynomial equal to zero:  
$$ x^2 - 5x - 14 = 0 $$  
Using factoring or the quadratic formula, we solve for $x$:  
$$ x = \frac{(-b) \pm \sqrt{b^2 - 4ac}}{2a} $$  
Substituting $a=1, b=-5, c=-14$:  
$$ x = \frac{-(-5) \pm \sqrt{(-5)^2 - 4(1)(-14)}}{2(1)} = \frac{5 \pm \sqrt{25 + 56}}{2} = \frac{5 \pm \sqrt{81}}{2} = \frac{5 \pm 9}{2} $$  
This gives two solutions:  
$$ x_1 = \frac{5+9}{2} = 7 $$  
$$ x_2 = \frac{5-9}{2} = -2 $$  
Thus, the vertical asymptotes are at $x=-2$ and $x=7$. Let's denote these as $a$ and $b$, so $\{a, b\} = \{-2, 7\}$ or simply $a=7, b=-2$ (order doesn't matter for sum). The problem asks for $a+b+c$.  

**2. Horizontal Asymptote:**  
The horizontal asymptote is determined by the ratio of the leading terms as $x \to \pm \infty$.  
$$ f(x) = \frac{2x}{x^2-5x-14} = \frac{2}{x + 5 - 14/x} $$  
As $x \to \infty$, the term $x$ in the denominator dominates, so:  
$$ \lim_{x \to \infty} f(x) = \lim_{x \to \infty} \frac{2}{x} = 0 $$  
Thus, the horizontal asymptote is $y=0$. This implies $c=0$.  

**3. Sum of Asymptotes:**  
Now we sum the values of $a$, $b$, and $c$:  
$$ a+b+c = -2 + 7 + 0 = 5 $$  
Or if $a$ represents the negative root $-2$ and $b$ represents the positive root $7$:  
$$ a+b = -2+7 = 5 $$  
In either case, the sum is 5.  

\boxed{5}  
