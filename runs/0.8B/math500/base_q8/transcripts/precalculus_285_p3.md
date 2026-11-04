# test/precalculus/285.json, part 3 of 3

[Previous part](precalculus_285_p2.md) · [Start](precalculus_285.md)

Wait, no. $x^4+x^2+1$.  
Let's factorize: $(z^2-1)(z^2+1)$? No.  
Let's check if roots of unity exist.  
The question asks for "smallest positive integer $n$ such that all the roots of $z^4+z^2+1=0$ are $n$-th roots of unity".  
This phrasing is extremely specific. It suggests the set of roots has modulus 1 and forms a subset of roots of unity? Or rather, all elements of this set satisfy $\alpha^n=1$? No.  
If all roots are roots of unity, then all roots $z_k$ must satisfy $|z_k|=1$.  
And they must be distinct.  
But wait, if the modulus is not 1, then it's impossible for them to be "roots of unity" (which have modulus 1).  
Wait, "are roots of unity" means that the elements are in $\{z^n = \omega \mid z \in \text{Roots}\}$. No.  
Usually "all the roots ... are $n$-th roots of unity" means that the set of roots is equal to a subset of $\{ e^{i 2\pi k/n} \}$? Or just that they belong to this group.  
Wait, maybe it means they are roots of unity.  
So I need to find $n$ such that all roots satisfy $z^4+z^2+1=0$.  
But let's check if my substitution is correct.  
If $z^4+z^2+1=0$, then $z^2 = \pm \sqrt{...}$.  
Let's solve for $z$ properly.  
$z^4+z^2+1=0$. This is a quartic equation.  
Let's check if it factors over $\mathbb{Q}$ or $\mathbb{C}$. It seems irreducible over $\mathbb{Z}$.  
Wait, the roots are solutions to $w^2+w+1=0$? No.  
Wait, let me double check the "substitute" step.  
Let $y = z^2$.  
Then $z^4+z^2+1 = (z^2)^2 + z^2 + 1$.  
If this is $w^2+w+1$, then $w=z^2$ leads to a contradiction? No, if I have an equation in $z$, I don't substitute variables freely into the polynomial.  
Wait, I am substituting $y=z^2$. The resulting expression is $(y)^2+y+1 = y^2+y+1$.  
Does this equal 0? Yes.  
So, does it mean that if $z$ is a root, then $w=y=z^2$ must be a solution to $y^2+y+1=0$?  
No, wait. If $z$ satisfies the equation, then substituting $y=z^2$ into $(y)^2+y+1$ yields 0.  
This means that $z^4+z^2+1$ evaluated at any root is zero.  
Wait, this implies that $w=y=z^2$ satisfies $w^2+w+1=0$.  
This means that all roots satisfy $w^2+w+1=0$.  
So if $z^4+z^2+1=0$, then $z^2$ must be a root of $x^2+x+1=0$?  
Wait, no. $y=z^2$. The condition is $(z^2)^2 + z^2 + 1 = 0$.  
This means $w^2+w+1=0$ where $w=z^2$ is not true.  
Wait, why did I think $w=z^2 \implies w^2+w+1$?  
Because $x^4+x^2+1 = (x^2)^2 + x^2 + 1$.  
But the polynomial in $z$ is $(x)^2 +  

## Answer

*(none: the token cap hit during thinking)*
