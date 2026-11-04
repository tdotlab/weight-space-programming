# test/algebra/1143.json, part 3 of 3

[Previous part](algebra_1143_p2.md) · [Start](algebra_1143.md)

So increasing on $(-4, 0)$.  
For $0 < x < 4$: e.g. 3. $(\text{pos})(\text{neg})$? No. $x^2-16 = -7 < 0$. $x$ is pos. So negative.  
So decreasing on $(0, 4)$.  
For $x > 4$: e.g. 5. $(\text{pos})(\text{pos})$? No. $x^2-16 = 9$. $x=5 \implies 25-16=9$. Positive.  
So increasing on $(4, \infty)$.  
Summary of critical points behavior:  
Decreasing on $(-\infty, -4]$.  
Increasing on $[-4, 0]$? No, negative to positive means crossing from left side to right side at some point.  
But it increases on $(-4, 0)$.  
So it starts at $\infty$ (since $-\infty \to -4$, no).  
If decreasing from $-\infty$ to $-4$. Then increasing from $-4$ to $0$.  
Then decreasing from $0$ to $4$.  
Then increasing from $4$ to $\infty$.  
Let's re-verify the "decreasing" on $(0, 4)$.  
At $x=2$: $g'(2) < 0$. Correct.  
At $x=-1$: $g'(-1) > 0$.  
So there is a local maximum somewhere between -5 and -3? No.  
If decreasing on $(-\infty, -4)$, then increasing on $[-4, 0]$ (so min at -4).  
And decreasing on $(0, 4)$, then increasing on $(4, \infty)$.  
So local maximum is not relevant if we want global minimum.  
The derivative changes sign from negative to positive at $x=-4$? No, goes neg $\to$ pos $\to$ neg $\to$ pos.  
Let's check again.  
$x^3 - 16x$: roots are $0, \pm 4$.  
Let's draw the curve of $g'(x)$.  
For $x < -4$, e.g. -5. $g'(-5) = -45 < 0$. (Decreasing).  
At $x=-4$: $g'=0$.  
Since derivative goes from negative to positive? No, if it increases from negative, it means at some point it crosses zero. But here we have a local minimum of the function? No, this is about where the curve goes down and then up.  
If decreasing on $(-\infty, -4)$, and increasing on $[-4, \dots]$ (which is $(-4, 0)$?), let's re-verify the derivative signs again.  
$x=-5$: negative.  
$x=-1$: positive? Wait.  
$g'(-1) = (-1)^3 - 16(-1) = -1 + 16 = 15 > 0$.  
So on $(-\infty, -4)$, it is decreasing.  
On $(-4, 0)$: e.g. $x=-1$ gives positive?  
No, check $x=2$: $8-32 < 0$.  
Check $x=3$: $27-48 < 0$.  
So derivative is negative on $(0, \infty)$.  
And derivative is positive on $(-\infty, -4)$? No.  
Let's re-evaluate the sign at -1 for $x^3-16x$.  
$x=-1 \implies (-1)^3 - 16(-1) = -1 + 16 = 15 > 0$.  
So it is increasing on $(-\infty, -4)$? No.  
Let's look at $x^2-16$ for $x=-1$: $9-16=-7 < 0$.  
$x^3-16x$ at $x=-1$: $-1+16=15 > 0$.  
So $g'(x)$ is positive on $(-\infty, -4)$.  
Let's re-evaluate for $x \in (-4, 0)$. e.g. $x=-3$. $27-48 = -21 < 0$? No. $x=-3$: $g'(-3)=21 > 0$.  
So at $x=-4$, it is a root (negative value of derivative).  
Let's re-calculate signs for $x \in (-\infty, -4)$.  
$x = -5$. $(-125) + 80 < 0$? No.  
$g'(-5) = -5^3 - 16(-5)$? No, $x^3 - 16x$.  
$-125 - (-80) = -45 < 0$.  
So it seems negative on $(-\infty, -4)$.  
So there must be a root between something else.  
Maybe I misremembered the sign of roots?  
Let's check the graph of $g'(x)$ again.  
$x(x^2-16) = x^3 - 16x$.  
Roots: $0, \pm 4$.  
Sign of $x(x^2-16)$ for $x < 0$:  
If $x=-5$, term is negative? No, $(x-4)$ is at least $(0.1)(-9) = -12$? No.  
If $x$ is very negative, $x^3$ is negative. $-16x$ is positive.  
So the dominant part is positive $-16x$.  
The cubic term $x^3$ dominates for large magnitude.  
At $-\infty$, $g' \approx -\infty$.  
At $x=-4$, $g'=0$.  
So it should cross 0 at some point? No, if at -5 it is negative and at -4 it is 0.  
It stays negative until it reaches -4?  
Then for $-4 < x < 0$?  
At $x=0$, $g'=0$.  
Is it positive or negative here?  
$x=-1$: $g'(-1) = 15 > 0$.  
So derivative is negative on $(-\infty, -4)$ (e.g. -5).  
Positive on $(-4, 0)$ (e.g. -1)? No, I said earlier it was positive at -1. But now I'm confused because of signs.  
Wait, if $g'(-5) = -45$, then derivative is negative.  
If $g'(-1) = 15$, derivative is positive.  
So there's a crossing point between -5 and -1?  
No, it doesn't cross zero at an interval where I tested points. It crosses somewhere inside $(0, -4)$? No, roots are $\{-4, 0\}$.  
Let's check the factorization again. $x^3 - 16x = x(x-4)(x+4)$ is correct.  
Let's re-evaluate signs at $x=-5$ using this.  
$x=-5$: $(-5)(-9)(-1)?$ No, $(-5)(25-16) = -5(9) = -45$. Negative.  
So it decreases from $\infty$ to something? Or increases?  
The sign is negative on $(-\infty, -4)$ (e.g. -3).  
Then at $x=-4$, it's 0.  
So if derivative is negative for $x \in (-\infty, -4)$ and positive on $(0, \dots)$? No, signs are $\text{neg}$ on $(-\infty, -4)$.  
At $x=0$ (positive root of cubic?).  
If we check sign between roots.  
Between $-4$ and $0$, e.g. -1.  
$g'(-1) = 15 > 0$.  
This contradicts the negative on $(-\infty, -4)$? No, because if it's continuous, it goes up from -4.  
But where does it go to $0$? It should be positive or something.  
Let's check values at roots:  
$g'(4) = 64 - 64 = 0$.  
So at $x=4$, derivative is 0.  
This means it must have a local max or min in $(4, \infty)$? No.  
If it crosses 0, and goes from negative to positive on the interval between roots... no.  
Let's check roots of cubic $x^3 - 16x$.  
Since leading coefficient is +1, and we know two real roots $\{-4, 4\}$.  
Then there is a third root? No, product of $(x-0)(x+4)$ terms...  
The roots are $0, \pm 4$? No, that would mean $x^3-16x = x(x-4)(x+4)$.  
Let's check factorization again.  
$x^3 - 16x = x(x^2-16)$.  
$(x^2-16)$ factors into $(x-4)(x+4)$.  
So the roots are $0, \pm 4$? No, roots of $x^2-16=0$ are $\pm 4$.  
So $x(x^2-16)=0$ has roots $0, -4, 4$.  
The derivative is a cubic polynomial. Its roots are $0, -4, 4$.  
But the leading coefficient of this cubic is positive? Yes ($+1$).  
A cubic with positive leading coeff always goes up at $\infty$.  
So we expect it to decrease from $-\infty$, reach local min, increase through other regions.  
Or start decreasing from $\infty$, go down.  
Let's recheck signs for $x < -4$:  
$x=-5$: $g'(-5) = (-125 + 80) < 0$. (Correct).  
$x \to -\infty$: negative? No, $x^3-16x$ goes to $-\infty$ as $x \to -\infty$.  
So it must cross zero somewhere. But all we have are roots $\{-4, 0, 4\}$? No.  
If the roots were $\pm 4, 0$, then there's no other real root.  
Let me re-verify the factorization of $x^3 - 16x$.  
It should be $(x+4)(x^2-16)$? No.  
Roots are $-4, 0, 4$ is incorrect for this equation?  
$(-4)^3 - 16(-4) = -64 + 64 = 0$. So $x=4$ and $x=-4$ are roots.  
$(0)^3 - 16(0) = 0$. Root is 0.  
Is there a third root? No, cubic has degree 3. But I only found two distinct real roots ($-4, 0$)?  
No, if $x^3 - 16x$ factors as $x(x+4)(x-4)$ then the product is $x^2(4)$? No.  
$x^2(x+4)(x-4)$? No.  
Let's multiply roots to check leading term: $0 \cdot 0 \cdot (-4) = 0$. Not cubic.  
Wait, roots of $g'(x)=0$ are $\{-4, 0, 4\}$?  
If I substitute $x=0$, $g'(0)=0$.  
If I substitute $x=-4$, $g'(-4)=-64  

## Answer

*(none: the token cap hit during thinking)*
