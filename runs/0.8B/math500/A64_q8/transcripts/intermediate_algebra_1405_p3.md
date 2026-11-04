# test/intermediate_algebra/1405.json, part 3 of 3

[Previous part](intermediate_algebra_1405_p2.md) · [Start](intermediate_algebra_1405.md)

*   If $C$ is $(-a,-b)$ and on parabola, then $x_C = -a$. So $y_C = a^2/8$.  
*   But $B$ has $y_B=b$. And $C$ has $y_C=a^2/8$. They must be equal?  
*   This means $y_B=y_C$, so the triangle is degenerate if it's symmetric? No.  
*   If vertices are $(0,0), (x,y), (-x,y)$.  
*   Distance between $(x,y)$ and $(-x,y)$ is $\sqrt{(2x)^2 + (y-y^2/8)^2}$? No.  
*   Wait, $P_2$ has coordinates $(x,y)$ on parabola means $y=x^2/8$.  
*   If $C=(-x,-y')$, then for it to be on the curve, $(-x)^2 = 8(-y') \implies x^2 = -8y'$. This is impossible since $x^2 \ge 0$ and $y' \le 0$ (wait parabola opens up).  
*   Let's go back to standard interpretation. The vertices of an equilateral triangle inscribed in a parabola usually refers to the fact that if you have a vertex at $(0,0)$, then the other two are determined by the geometry.  
*   Let $s$ be the side length.  
*   We can set up equations.  
*   One vertex is at $(0,0)$. The triangle has sides of length $L$.  
*   So vertices must be distance $L$ from origin? Or just form equilateral triangle with one vertex at origin?  
*   This means we need a point $P_1(0,0)$ and points $P_2(x_2,y_2), P_3(x_3,y_3)$ such that they form equilateral triangle.  
*   Since the parabola is symmetric with respect to y-axis? No.  
*   Let's re-evaluate the "vertex" at $(0,0)$.  
*   If the vertices are on the curve, then we have a triangle inscribed in the parabola.  
*   Let's check if $P_1$ can be $(0,0)$ and $P_2, P_3$ are $(-a,a)$ and $(a,-a)$. No.  
*   Let's try to find if there is a triangle with side length 3 or something? Or maybe related to $x=3a$?  
*   Let's consider the equation of the parabola: $y = x^2/8$.  
*   We want an equilateral triangle inscribed in this curve.  
*   The vertices are $(0,0)$ and points on the curve.  
*   If we assume symmetry w.r.t y-axis, then vertices could be $(-a,a)$? No, that's symmetric about y-axis (so x = -x). But for parabola $y=x^2/8$. So points must satisfy $y=b, b \ge 0$.  
*   If we want a triangle with vertex at $(0,0)$.  
*   Vertices are $P_1(0,0)$ and $P_2(x_2,y_2), P_3(x_3,y_3)$.  
*   Since it's equilateral, the sum of side lengths is 3 times something? No.  
*   Let's assume coordinates of vertices are $A(0,0)$. Then $B$ and $C$ must be such that $s$ is determined by their position.  
*   Let $s^2 = (x_2)^2 + (y_2)^2 = (x_3-x_2)^2 + (y_3-y_2)^2$.  
*   Also since vertices lie on the parabola, we have $y_2=x_2^2/8$ and $y_3=x_3^2/8$.  
*   Let's denote $s = L$.  
*   Case 1: The triangle is equilateral and one vertex is $(0,0)$. This means the other two vertices $P_2, P_3$ lie on parabola such that distance between them is equal to distance from origin. But we need distances from origin to $P_2$ and $P_3$ to be related to sides? No, side lengths are equal.  
*   So $s^2 = (x_2)^2 + y_2^2$. Also $s^2 = (x_2-x_3)^2 + (y_2-y_3)^2$? No, distance between two points on parabola is not a side of triangle if vertices are $A, B, C$.  
*   If vertices are $A(0,0)$ and $B, C$ are on the curve. Then side length $s = |AB| = |AC| = |BC|$.  
*   This implies $\triangle ABC$ is equilateral.  
*   Let's check if there exists a solution with vertices $(0,0), (x,y), (x',y')$.  
*   This seems unlikely to give a unique side length unless there's an implicit constraint.  
*   Is it possible that the question implies vertices lie on parabola such that sides are tangent or something? No.  
*   Let's go back to the idea of symmetry. If $A=(0,0)$ is vertex.  
*   The triangle has an axis of symmetry through $A$? Yes. So the third side must be perpendicular to the bisector of $\angle A$. Or the vertices $B, C$ are symmetric with respect to y-axis (bisector).  
*   If so, $B=(x,y)$ and $C=(-x,y)$. But $B$ on curve means $y=x^2/8$. This implies $x^2 = 8y$. And $C(-x,y)$ is on curve if $x^2=8y$.  
*   Then the vertices are $(0,0), (a, a^2/8)$ and $(-a, a^2/8)$.  
*   Let's check distances for this case.  
*   $AB = \sqrt{a^2 + y^2}$. No, distance is $\sqrt{x^2+y^2} = \sqrt{y^2+a^2}$? No, if $x=a$, then $y=a^2/8$.  
*   Then $AB^2 = a^2 + y^2$.  
*   Also we need to find the coordinates of $C(-a,y)$. Is it on curve? Yes.  
*   So vertices are $P_1(0,0)$, $P_2(a,a^2/8)$, $P_3(-a,a^2/8)$.  
*   This defines a triangle. We need to calculate its side length $L = AB$.  
*   $L = \sqrt{a^2 + y^2}$.  
*   Here we have two vertices $A$ and $B$. But wait, the problem asks for "the" side length. This implies it's unique.  
*   Let's check if there's a third vertex  

## Answer

*(none: the token cap hit during thinking)*
