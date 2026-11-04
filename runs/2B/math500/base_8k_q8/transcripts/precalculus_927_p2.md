# test/precalculus/927.json, part 2 of 2

[Previous part](precalculus_927.md)

So $\mathbf{d}_2 = (2, -12, -3)$. Wait. $(2, -12, -3)$ seems to be derived from the vector approach.  
However, I should double check my vector simplification again.  
Vector components: $x = 1$, $y = -6$, $z = -3/2$.  
Is there a simpler integer vector?  
Maybe $(2, -12, -3)$ is correct but reducible? No, GCD of 2, 12, 3 is 1.  
Is it possible to simplify differently?  
What about $y$ vs $z$?  
From $6x = -y$, if $x=k$, $y=-6k$.  
From $-4z = 6x$, $z = -6/4 x = -3/2 x$.  
So vector is $(x, -6x, -3/2 x) \propto (2, -12, -3)$? No.  
Let $x=2$. Then $y=-12$. Then $z = -3$.  
Vector $(2, -12, -3)$.  

Wait, I had a calculation issue earlier with the cross product or something similar.  
Let's check for errors in my reasoning.  
Line 2: $\mathbf{d}_2 = (2, -12, -3)$? Or is it $(2, 0, 1)$? No.  

Is there another way to write this line?  
From $-y = -4z \implies y = 4z$.  
From $6x = -y \implies 6x = -(4z) = -4z \implies x = -2/3 z$.  
So $\mathbf{r} = (-2/3 t, 4t, t)$. Multiply by 3 to get integers.  
$(-2t, 12t, 3t)$. Direction vector $(-2, 12, 3)$.  
Wait. $( -2, 12, 3 )$ is the same direction as $(2, -12, -3)$? No, opposite signs.  
Is it $x=-2, y=12$ or $y=-6$?  
Let's re-calculate $x$ relation with $z$.  
$6x = 4z$ is WRONG.  
Eq: $6x = -y$.  
Eq: $-y = -4z \implies y = 4z$.  
Substitute $y=4z$ into first eq: $6x = -(4z) = -4z \implies x/z = -4/6 = -2/3$.  
So $x : z = -2 : 3$ or $x/z = -2/3$.  

## Answer

*(none: the token cap hit during thinking)*
