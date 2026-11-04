# test/intermediate_algebra/1405.json, part 3 of 3

[Previous part](intermediate_algebra_1405_p2.md) · [Start](intermediate_algebra_1405.md)

If vertices are $(0,0), B, C$, then side length $s = \text{dist}(A,B)$. But $\text{dist}(A,B) = s$ means $B$ must be distance $s$ from origin.  
Since $B$ lies on parabola $y=x^2/8$, its coordinates are determined by intersection of circle and parabola.  
However, if we fix side length $s$, we can find possible points $B$ and $C$.  
Then we need to ensure that $\triangle ABC$ is equilateral (i.e., $AC=s$).  
So for a given $s$, there must exist two distinct points on parabola at distance $s$ from origin? No.  
If vertices are $A(0,0), B(x_2, y_2)$ and $C(x_3, y_3)$.  
Then we need $\text{dist}(P_1, P_2)^2 = \text{dist}(P_1, P_3)^2$? No.  
We need $\triangle ABC$ equilateral. So $\text{dist}(B,C)^2 = \text{dist}(A,B)^2$.  
Also $A=(0,0)$. So we need $P_1, P_2, P_3$ to lie on a circle? No, vertices on parabola must form equilateral triangle.  
If one vertex is at origin $(0,0)$, let its distance from other vertices be $s$.  
Since $A=(0,0)$, we need $|AB|=s$. This means $B$ is on a circle of radius $s$ centered at $A$? No.  
$A$ is the origin. So $B$ must be on a circle centered at origin with radius $s$.  
And $C$ must satisfy $BC=s$, so $C$ must be on circle centered at $B$ with radius $s$.  
Also $AC=s$, so $C$ must be on circle centered at $A$ with radius $s$.  
This implies that all vertices lie on a circle of radius $s$? No. $A(0,0)$ is on the circle of radius 0. So $AC=s$ means distance between $A$ and $C$ is $s$.  
But $C$ must be on parabola. And $B$ must be on parabola.  
We also need $\text{dist}(B,C) = s$.  
So we have points $B, C$ on parabola such that distance to origin (distance between $A$ and other vertex) is $s$, and distance between $B$ and $C$ is $s$.  
This implies $\triangle ABC$ is equilateral with vertices $(0,0), B, C$.  
We need to find a point $B$ on the parabola such that there exists a point $C$ on the parabola such that triangle $ABC$ is equilateral.  
Is it possible? Yes.  
Let's set up equations.  
Let $A=(0,0)$. Then $B = (x_B, x_B^2/8)$ for some $x_B$.  
We need $\text{dist}(A,B)^2 = s^2 \implies x_B^2 + x_B^4/64 = s^2$? No.  
Wait. If $A=(0,0)$ is a vertex, and vertices are on parabola.  
The distance from origin to the curve $y=x^2/8$ varies with $x$.  
Let $f(x) = \sqrt{x^2 + x^4/64}$ be the distance from origin to point $(x,y)$ where $y=x^2/8$.  
We need to choose two points on parabola, say $B$ and $C$, such that their distances to origin are equal? No.  
Let's denote vertices as $P_1(0,0), P_2(x_B, y_B), P_3(x_C, y_C)$.  
Then $\text{dist}(P_2, P_1)^2 = s^2$. Since $P_1=(0,0)$ is distance 0 from origin? No, vertices are $(0,0)$ and $B$ and $C$.  
The distance from vertex to any other vertex must be equal.  
Since vertex is at origin, and vertices are on parabola.  
Then $\text{dist}(P_1, P_2)^2 = \text{dist}(P_1, P_3)^  

## Answer

*(none: the token cap hit during thinking)*
