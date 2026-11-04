# test/algebra/1339.json, part 3 of 3

[Previous part](algebra_1339_p2.md) · [Start](algebra_1339.md)

If we have a constant $k$, then for a given $y$, $x$ is determined by $y = k x^{-1/2}$.  
$\implies x^{1/2} = k/y \implies x = (k/y)^2$.  
So $x = (15\sqrt{24} / 3)^2$.  
Let's evaluate this expression.  
$15\sqrt{24} / 3 = 5\sqrt{24} = 5 \cdot 2\sqrt{6} = 10\sqrt{6}$.  
Square it: $(10\sqrt{6})^2 = 100 \cdot 6 = 600$.  

Okay, I need to resolve why I got $x=25/24$ in the previous step.  
Step " $\sqrt{x} = k/3 $":  
$k/3 = (15\sqrt{24}) / 3 = 5\sqrt{24}$.  
My previous calculation was: $\sqrt{x} = k/3 = 5/\sqrt{24}$. Why the difference?  
Ah. In my "check step" I wrote $k/3$ in terms of $y=15$.  
Let's re-evaluate $x^{0.5} = k/y$.  
Wait, the equation is $y = k x^{-1/2}$.  
If $y=3$, then $3 = k x^{-1/2} \implies k/x^{1/2} = 3$? No.  
Let's solve for $\sqrt{x}$.  
$\frac{1}{\sqrt{x}} = \frac{3}{k}$.  
$\sqrt{x} = \frac{k}{3}$.  
$x = (k/3)^2$.  
If $k = 15\sqrt{24}$, then $x = (15\sqrt{24}/3)^2 = (5\sqrt{24})^2 = 600$.  


## Answer

*(none: the token cap hit during thinking)*
