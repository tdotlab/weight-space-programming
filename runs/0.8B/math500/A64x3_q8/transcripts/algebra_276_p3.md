# test/algebra/276.json, part 3 of 3

[Previous part](algebra_276_p2.md) · [Start](algebra_276.md)

$A=5, B=2$.  
$AB = 10$.  
$B = 2$.  
Sum $= 12$.  

I am confident.  

One edge case: "integers A and B". Could they be complex?  
"Can be written as... where A and B are integers." - implies real integers or integer coefficients. Usually integers means $\mathbb{Z}$.  
If non-integers were allowed, there would be infinite solutions for $3A-8B=-1$ with $AB=10$.  
For example, let $B = \lambda^2 \cdot 10$? No, $AB=10$.  
If $B$ was not integer, $B=1$, then $A=5/3$? No, $3(5) - 8(1) = 1$.  
If we need $3A - 8B = -1$ with $AB=10$, then $B(3-8/A) = -1$ ?  
From $3A = 8B-1 \implies A = (8/3)B - 1/3$.  
Substitute into $AB=10$: $(\frac{8}{3}B - \frac{1}{3})B = 10$.  
$\frac{8}{3}B^2 - \frac{1}{3}B = 10$.  
Multiply by 3: $8B^2 - B - 30 = 0$.  
Discriminant $\Delta_B = (-1)^2 - 4(8)(-30) = 1 + 960 = 961$.  
$\sqrt{961} = 31$.  
$B = \frac{1 \pm 31}{16}$.  
$B_1 = (32)/16 = 2$.  
$B_2 = (-30)/16 = -15/8$. Not integer.  
So $B=2$ is the unique positive rational solution? No, $A$ must be integer too.  
Let's check if A comes out integer for these B's.  
If $B=1$, then $A = 8(1)-1/3$ no. $A=2.5$.  
If $B=-1$, then $-30$. $A = (-1)(10)$? No, equation was derived from $AB=10$.  
If $B$ is the factor, we need to satisfy all constraints.  
The constraint on A being integer means $8/3 B - 1/3 \in \mathbb{Z}$.  
$B$ must be such that $8B - 1  

## Answer

*(none: the token cap hit during thinking)*
