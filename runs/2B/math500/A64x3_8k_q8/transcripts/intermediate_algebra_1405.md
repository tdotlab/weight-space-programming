# test/intermediate_algebra/1405.json (Intermediate Algebra, level 4)

> An equilateral triangle is inscribed in the parabola $x^2 = 8y,$ such that one of the vertices of the triangle coincides with the vertex of the parabola.  Find the side length of this equilateral triangle.  

**Wrong.** Gold `16 \sqrt{3}`, predicted `None`. Finish: length, 8192 tokens, 2 waits, 661.2 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Let the equation of the parabola be $x^2 = 8y$. This can be written as $y = \frac{1}{8}x^2$.  
The vertex of the parabola is at $(0,0)$.  
The problem states that an equilateral triangle is inscribed in this parabola.  
"An equilateral triangle is inscribed in the parabola." This usually means all three vertices lie on the curve. However, there are two common interpretations:  
1. Vertices are points of tangency and intersections? No, "inscribed" for a polygon usually implies vertices are on the boundary (in this case, the parabola).  
2. Since it's an equilateral triangle, if one vertex is fixed at the vertex of the parabola $(0,0)$, we need to find the other two vertices $(x_1, y_1)$ and $(x_2, y_2)$ that lie on the parabola and form an equilateral triangle with $(0,0)$.  

Let $V = (0,0)$. Let the other two vertices be $A$ and $B$.  
The condition is that $AB = AC = BC$? No, it's an equilateral triangle. The vertices are $P$, $Q$, $R$. One vertex is at $V(0,0)$.  
So, we need to find points $A(x_A, y_A)$ and $B(x_B, y_B)$ on the parabola such that $\triangle VAB$ is equilateral.  
The coordinates of $V$ are $(0,0)$.  
The coordinates of $A$ are $(x_1, x_1^2/8)$.  
The coordinates of $B$ are $(x_2, x_2^2/8)$.  

First, calculate the distance $|VA|$ and $|VB|$.  
Let's use complex numbers or rotation. Or simple geometry.  
Since it's an equilateral triangle, the angle $\angle AVB = 60^\circ$.  
Or we can rotate $VAB$ by 60 degrees around one of the vertices? No.  
The coordinates are on the parabola $x^2=8y$.  
Let's parameterize the points. Since it's a function $y=ax^2$, let $x = k t^2$, $y=k t^4$. No, simpler.  
$x = 4u$, $y = u^2$ is not quite right.  
The vertex is at $(0,0)$. The tangent is the y-axis? No, tangent is horizontal there? No, at $(0,0)$, slope is undefined (vertical tangent).  
Let's check the tangent equation: $x dx - 8 dy = 0 \implies x^2/8$ derivative is $\frac{1}{4}$.  
At vertex $(0,0)$, tangent is vertical $x=0$. The latus rectum passes through $(0, 1/8(2)) = (0, 1)$. No.  
Equation of parabola: $x^2 = 8y$. Latus rectum length is 4a? No. $x^2 = 4ay$. So $4a = 8$, so $a=2$. Focus is at $(0,2)$.  

Let the vertices be $V(0,0)$, $A(x_A, y_A)$, $B(x_B, y_B)$.  
$y_A = x_A^2/8$. $y_B = x_B^2/8$.  
Since triangle is equilateral, all sides have equal length.  
Side 1: $c = |VA|$. Side 2: $b = |VB|$. Side 3: $a = |AB|$.  
We need $c=b=a$ and $\angle AVB = 60^\circ$.  

Let's use the rotation idea.  
Rotate vector $\vec{VA}$ by $+90^\circ$ to get a direction perpendicular to $VA$. No, that doesn't help directly with finding B on parabola unless we know something about symmetry.  
Let's find the coordinates of A and B.  
The distance between A and B is $c$, and the angle at V is 60 degrees? No.  
If $\triangle VAB$ is equilateral, then the length $|AB| = |VA| = |VB|$.  
So we need a triangle with vertices on the parabola such that it's equilateral with one vertex at $(0,0)$.  
Let the vertices be $V(0,0)$, $A$, $B$.  
The condition is $A, B \in P$ and $|VA|=|VB|=|AB|=L$.  
This means $\angle A V B = 60^\circ$.  
Also $\triangle OAB$ (where O is origin) is equilateral. This implies the coordinates of $A$ and $B$ must satisfy certain relationships.  

Let's use polar coordinates or just rotation.  
Let $V$ be the vertex $(0,0)$.  
The points $A(x_1, x_1^2/8)$ and $B(x_2, x_2^2/8)$ are on the parabola.  
The angle subtended by chord AB at V must be 60 degrees? No, the angle $\angle AVB = 60^\circ$.  
Let's denote coordinates in terms of $x$.  
$x^2 = 8y \implies y = x^2/8$.  
$|VA|^2 = x_1^2 + (x_1^2/8)^2 = x_1^2 + x_1^4/64 = x_1^2(1 + x_1^2/64)$.  
For the equilateral triangle condition:  
$|VA| = |VB|$ is not required to hold, but $|AB|=|VA|$ and $|AB|=|VB|$.  
So $|VA| = |VB|$ implies $|VA|^2 = |VB|^2$.  
This means $x_1^2(1+x_1^2/64) = x_2^2(1+x_2^2/64)$.  
Since the points are distinct, this usually implies $|VA| = |VB|$ leads to symmetric points if they have the same distance from vertex. But we don't know which one is "up" or "down". However, since the parabola is symmetric about x-axis? No, it's symmetric about y-axis (which is vertical), but the vertices are usually $A$ and $B$.  
Since the parabola opens upwards with vertex at origin, points $(x, y)$ and $(-x, y)$ have same distance from origin if we consider distance on parabola? No.  
Let's check symmetry. If $A=(x_1, x_1^2/8)$ is a solution for some parameter $x_1$, then the symmetric point would be related. But here one vertex is $(0,0)$.  
Since $\angle AVB = 60^\circ$, points A and B are at distance $L$ from origin.  
Let's rotate the vector to make it easier.  
Consider a coordinate system where one axis aligns with the symmetry of the triangle. But the parabola is not centrally symmetric in a way that allows easy rotation of vertices unless we use parametric form.  

Actually, let's look at the property of equilateral triangles inscribed in parabolas. There is a known formula for this.  
Or solve it directly.  
Let's assume coordinates $A=(x_1, y_1)$ and $B=(x_2, y_2)$.  
Condition 1: $x_1^2 = 8y_1$, $x_2^2 = 8y_2$.  
Condition 2: $|VA|^2 = x_1^2 + y_1^2 = L^2$. (Note $L$ is the side length).  
Condition 3: $|VB|^2 = x_2^2 + y_2^2 = L^2$.  
Condition 4: $|AB|^2 = (x_1-x_2)^2 + (y_1-y_2)^2 = L^2$.  
Since we need a triangle with one vertex at $(0,0)$ and others on the curve, is there a specific configuration?  
Usually "inscribed" means vertices lie on the boundary. Here all 3 vertices are required to be on the parabola. One vertex is fixed as $V(0,0)$.  
So we need to find two points on $x^2=8y$ that form an equilateral triangle with $(0,0)$.  

Let's assume $L = \sqrt{r}$. $A$ and $B$ have distance $\sqrt{8}$ from origin in the rotated frame? No.  
The coordinates of A can be written as $(a, b)$ on parabola.  
Since $\triangle VAB$ is equilateral, the vector $\vec{BA}$ is obtained by rotating $\vec{VA}$ by $90+30$ degrees?  
Let's visualize. $V$ is at $(0,0)$. $A$ is some point. $B$ is another point.  
If we construct an equilateral triangle on the segment $AB$, one vertex could be $V$. But here the vertex is fixed at origin. So $V$ is a vertex of the triangle with other vertices on parabola.  
So $\angle AVB = 60^\circ$ and $|VA|=|VB|$.  

Let's parameterize points by $t$. For $x^2=4ay$, parameter $t=x/2\sqrt{a}$. Here $4a=8 \implies a=2$. So $x = 2\sqrt{2} t$.  
This gives $y = (2\sqrt{2}t)^2 / 4 = 8t^2/4 = 2t^2$? No. $y = x^2/8$.  
If $x=4t$, $y=16t^2/8=2t^2$. Let's use $x = k t, y = m t^2$.  
$x^2=4ay \implies x^2/a = 4y$. Or $x = 2\sqrt{a} \sin \theta, y = 2\sqrt{a}(1-\cos \theta)$?  
Let's just use $x$ coordinate as variable.  
Since triangle is equilateral, the angle of the chord AB with respect to x-axis... no.  

Let's rotate the parabola around $(0,0)$. Or simpler:  
The vertices are $V(0,0)$ and $A(x_1, y_1)$ and $B(x_2, y_2)$.  
For $V$ to be vertex of equilateral triangle with $A,B$, we must have $\angle AVB = 60^\circ$.  
Also distance $|VA|^2 = |VB|^2 = (x_1^2 + x_1^4/64)$.  
Distance squared from origin is not sufficient, we need equal lengths.  
$y_A = \frac{1}{8} x_A^2$, so $|VA|^2 = x_A^2 + (\frac{x_A^2}{8})^2 = x_A^2 (1 + \frac{x_A^2}{64})$.  
Let's denote $u = x_A, v = x_B$.  
$u^2 + u^4/64 = L^2$.  
$v^2 + v^4/64 = L^2$.  
So $u^2 (1 + u^2/64) = v^2 (1 + v^2/64)$.  
This simplifies to $u^2 - v^2 + \frac{u^4-v^4}{64} = 0$ or $(u^2-v^2)(1 - \dots)$? No.  
$u^2 (1 + u^2/64) = v^2 (1 + v^2/64)$  
If $|VA| \neq |VB|$, then $L^2$ is different. But triangle equilateral requires equal sides. So $|VA|=|VB|=L$.  
So we must have the same value for the expression.  

Let's look at geometry. $V(0,0)$.  
Consider complex numbers. The parabola is not symmetric in a standard way around 0 unless origin is center. Here it is vertex.  
Let the two other vertices be points $A$ and $B$.  
Since $\angle A V B = 60^\circ$, let's rotate $V(0,0)$ to $B(x_B, y_B)$.  
Maybe use a property of "equilateral triangle inscribed in a parabola".  
The equation of a parabola $x^2=4ay$ can be parameterized as $(at^2, 2at)$ or similar. Here $a=2$, so points $(2t^2 \cdot 4?, no)$.  
Let's stick to $x^2 = 8y$.  
Points are $(x_1, x_1^2/8)$ and $(x_2, x_2^2/8)$.  
Also $x_A = x_B$ gives a line parallel to axis? No.  

Let's use the rotation method.  
We can think of rotating $V(0,0)$ to form equilateral triangle on base $AB$. This is not right. $V$ is one vertex. So we have an equilateral triangle with vertices $(0,0), A, B$.  
This means the chord $AB$ subtends a $60^\circ$ angle at the origin? No, $\angle AVB = 60^\circ$.  
Let's consider the polar coordinates of A and B.  
But the relation between x-coordinates of points on parabola and distance from vertex is fixed by geometry.  

Let's find specific example.  
If $A$ is $(x_1, y_1)$ and $B$ is $(x_2, y_2)$.  
Since $\triangle VAB$ is equilateral, the vector $\vec{V A}$ can be rotated by $\pm 60^\circ$ relative to some bisector? No.  
$\vec{VA}$ and $\vec{VB}$ have length $L$. The angle between them is $60^\circ$.  
So we can write $\vec{BA} = \vec{VA} - \vec{VB}$.  
Length $|\vec{BA}| = |\vec{VA}| = L$.  
Also angle between $\vec{VA}$ and $\vec{VB}$ is $60^\circ$ or $120^\circ$? It is vertex angle.  
Let's check orientation. A, B on parabola opening up. Origin at bottom.  
Usually the triangle would be "above" the vertex if it opens up. But here vertex is $(0,0)$.  
Points with $x > 0$: $A(1, 2/8?) = (1, 0.125)$.  
Points with $x < 0$: symmetric.  

Let's use coordinates of the rotated points.  
Let $\theta$ be the angle $\angle AVB$.  
Since triangle is equilateral, angle between radii to vertices is $60^\circ$ ? No, A and B are not on circle centered at origin necessarily. But we found $|VA|=|VB|$ implies they are symmetric w.r.t some axis? Not necessarily.  
But $\angle AVB = 60^\circ$.  
Let's rotate the coordinate system so that $\vec{VA}$ lies along some angle.  
Actually, let's use a known property or solve algebraically.  

Algebraic setup:  
Let $u = x_A^2 + (x_A^2/8)^2$ be the square of side length? No.  
Equation for point on parabola to distance L from origin.  
$y = \frac{x^2}{8}$.  
Distance squared is $d^2 = x^2 + y^2 = x^2 + \frac{x^4}{64}$.  
Let this be $L^2$. So $x^2 (1 + x^2/64) = L^2$.  
This can be written as $L^2 x^2 - x^4/8 = 0$? No.  
$L^2 \approx x^2$ for small $x$.  
Let's define a variable $z$ representing the complex position or just use coordinates $(x,y)$.  
Since it's an equilateral triangle with vertices on parabola and one vertex at origin, we need to find $x_A, y_A, x_B, y_B$ such that:  
1. $y = x^2/8$  
2. $|VA|^2 = |VB|^2$  
3. $\vec{V A} \cdot \vec{V B} = L^2 \cos(60^\circ)$ or something? No, dot product is magnitude squared times cosine. So $\vec{VA} \cdot \vec{VB} = L^2 (1/2)$.  
Let's write out the vector products.  
$A = (x_A, x_A^2/8)$. $B = (x_B, x_B^2/8)$.  
$|VA|^2 = x_A^2 + x_A^4/64$.  
$|VB|^2 = x_B^2 + x_B^4/64$.  
For equilateral triangle, we need $|VA| = |VB| = L$.  
So $x_A^2(1+x_A^2/64) = x_B^2(1+x_B^2/64)$.  
Also the dot product condition:  
$\vec{VA} \cdot \vec{VB} = x_A x_B + y_A y_B = x_A x_B + \frac{x_A^2}{8} \frac{x_B^2}{8} = x_A x_B (1 + \frac{x_A^2 x_B^2}{64})$.  
Since angle is $60^\circ$, $\vec{VA} \cdot \vec{VB} = L^2 \cos 60^\circ = L^2/2$.  
So $x_A x_B (1 + \frac{x_A^2 x_B^2}{64}) = \frac{1}{2} (x_A^2 + x_A^4/64) (x_B^2 + x_B^4/64)$? No, that would be if $|VA|=L$ and we use dot product formula.  
Let's just say $|\vec{VA}| = |\vec{VB}| \implies |VA|^2 = |VB|^2$.  
Let this value be $S$.  
$S = x_A^2 + \frac{x_A^4}{64}$.  
We also have $|AB|^2 = S$.  
$|AB|^2 = (x_A - x_B)^2 + (y_A - y_B)^2 = (x_A - x_B)^2 + (\frac{x_A^2}{8} - \frac{x_B^2}{8})^2$.  
$= (x_A - x_B)^2 + \frac{(x_A^2 - x_B^2)^2}{64} = (x_A - x_B)^2 [1 + (\frac{x_A^2 - x_B^2}{8(x_A-x_B)})^2]$? No.  
$|AB|^2 = \frac{1}{64} (64(x_A-x_B)^2 + (x_A^2 - x_B^2)^2)$.  
Also $\vec{V A} \cdot \vec{V B} = x_A x_B + \frac{x_A^2 x_B^2}{64}$.  
For equilateral triangle, the angle between $VA$ and $VB$ is 60 degrees.  
So $\vec{VA} \cdot \vec{VB} = |\vec{VA}| |\vec{VB}| \cos(60^\circ) = S/2$.  
Thus:  
$x_A x_B + \frac{x_A^2 x_B^2}{64} = \frac{1}{2} (x_A^2 + \frac{x_A^4}{64})$? No.  
The condition $|VA|=S$ and $|VB|=S$ means $|VA|^2 = |VB|^2$.  
So $\vec{VA} \cdot \vec{VB} = \frac{1}{2} |VA|^2$.  
This implies $x_A x_B + \frac{x_A^2 x_B^2}{64} = \frac{1}{2} (x_A^2 + \frac{x_A^4}{64})$.  
Let's analyze this equation. Let $u = x_A, v = x_B$.  
$uv + \frac{u^2 v^2}{64} = \frac{1}{2}(u^2 + u^4/64)$.  
Also we need $|AB|^2 = S = |VA|^2$.  
$\frac{1}{64} [ 64(u-v)^2 + (u^2-v^2)^2 ] = u^2 + \frac{u^4}{64}$.  
Multiply by 64:  
$64(u-v)^2 + (u^2-v^2)^2 = 64(u^2 + \frac{u^4}{64})$.  
$64(u^2 - 2uv + v^2) + u^4 - 2u^2v^2 + v^4 = 64u^2 + u^4$.  
Simplify:  
$64u^2 - 128uv + 64v^2 + u^4 - 2u^2v^2 + v^4 = 64u^2 + u^4$.  
Subtract $64u^2 + u^4$ from both sides:  
$- 128uv + 64v^2 - 2u^2v^2 + v^4 = 0$.  
This is one equation relating x-coordinates. It doesn't use the angle condition fully?  
We have $|AB|=S$.  
Also we used $\angle AVB=60^\circ$ which implied dot product equals S/2.  
Is that sufficient? Yes, $|VA|=S$, $|VB|=S$, $|\vec{VA} \times \vec{VB}| = S^2 \sin(60)$. Or simpler, $\angle = 60$ is angle between vectors.  

Let's look at the equation derived from $\frac{1}{2} (u^2 + u^4/64)$ on the RHS of dot product eq? No.  
The dot product condition was: $uv + \frac{u^2 v^2}{64} = S/2$.  
Substitute $S$:  
$uv + \frac{u^2 v^2}{64} = \frac{1}{2} (u^2 + \frac{u^4}{64})$. This assumes $\vec{VB} = \vec{VA}$? No.  
$|\vec{VB}|$ is same $S$, so it works for B.  

Let's solve for relations.  
$u v (1 + u v / 64) = \frac{1}{2} S$.  
This doesn't help much with solving directly.  

Let's consider a special case where triangle might be "symmetric" or simple.  
If $A, B$ are symmetric w.r.t y-axis, i.e., $x_A = x_B > 0$, then $A, B$ have different distances from origin? No.  
If symmetric, $x_A = -x_B$. Then $|VA|=|VB|$ automatically since parabola is not symmetric wrt vertical axis at $(0,0)$ in terms of shape? Parabola $x^2=8y$ is symmetric about y-axis (x -> -x).  
Let's check: If $A(x, y)$ on parabola, then $(-x, y)$ is also on parabola.  
Then $|VA|^2 = x^2 + y^2$. So $|-x|^2 + y^2 = x^2+y^2$. Same length.  
But if we need angle $60^\circ$, can we have an equilateral triangle symmetric w.r.t y-axis?  
If vertices are $(0,0), (x_1, y_1), (-x_1, y_1)$.  
This triangle is degenerate? No, if $(0,0), A, B$ are collinear with origin. But A and B have $y > 0$ and distinct x.  
The points are not collinear unless on the x-axis (which is not parabola).  
If vertices are $(0,0)$, $A(x_1, y_1)$, $B(-x_1, y_1)$.  
Then $\triangle OAB$ has base AB parallel to x-axis? No.  
Vertices $(0,0), (x_1, y_1), (-x_1, y_1)$.  
Length $OA = L$, $OB = L$. Base $AB$ length is $2x_1$.  
Sides $OA=L, OB=L, AB=2x_1$.  
For equilateral, $L = 2x_1$.  
So side length is $2x_1$.  
Distance from origin to chord AB must be perpendicular bisector? Yes.  
This means $\angle A V B$ would be angle subtended by a point on circle of radius L. But V is vertex of triangle, not center.  
Here V is $(0,0)$.  
So we need $A, B$ such that $\triangle OAB$ is equilateral.  
Then coordinates must satisfy:  
1. A on parabola.  
2. $B$ on parabola (and symmetric to A implies B also on parabola).  
3. $L = 2 x_A$.  
4. $OA^2 = L^2 = 4x_A^2$.  
Let's check if this holds for parabola.  
$A(x, y)$. $B(-x, y)$.  
Condition: $x^2 + y^2 = (2x)^2 \implies x^2 + y^2 = 4x^2 \implies y^2 = 3x^2 \implies y = \pm \sqrt{3} x$.  
Since points are on parabola, $y = x^2/8$.  
So we need $x^2/8 = \pm \sqrt{3} x$.  
If $x > 0$, $x/8 = \sqrt{3} \implies x = 8\sqrt{3}$.  
Then $y = (64 \cdot 3)/8 = 24$.  
Let's check side length.  
$A = (8\sqrt{3}, 24)$.  
$B = (-8\sqrt{3}, 24)$.  
$V = (0,0)$.  
$|VA|^2 = 64(3) + 576 = 192 + 576 = 768$. $|VA| = \sqrt{768} = 8\sqrt{12} = 16\sqrt{3}$? No. $\sqrt{192} \approx 13.8$.  
$AB = 16\sqrt{3}$.  
So side length is $16\sqrt{3}$.  
Is this equilateral? Yes, base on x-axis? No. Vertices are $(0,0), (x,y), (-x,y)$.  
Distance between A and B is $2x$. Distance from V to A is $\sqrt{x^2+y^2}$.  
If $y = \sqrt{3}x$, then $2x$ vs $\sqrt{x^2+3x^2} = 2x$. So it works.  
However, the triangle must be inscribed in the parabola.  
Vertices are $(0,0)$ and two points on parabola.  
If $y = \sqrt{3}x$, then $x$ is real? Yes. $x^2/8 = \sqrt{3} x \implies x = 8\sqrt{3}$ (since $x>0$ for symmetry).  
So vertices are $(0,0), (8\sqrt{3}, 24), (-8\sqrt{3}, 24)$.  
Does this form a triangle? Yes.  
Is it equilateral? Yes.  
But is it "inscribed"? All vertices lie on the parabola?  
The vertex of the triangle is $(0,0)$ which lies on the parabola.  
So we found one solution with side length $16\sqrt{3}$?  
Let's check if there are other solutions. The question says "Find the side length". It implies a unique value or I might be missing something.  
However, is this triangle valid?  
Vertices: $(0,0)$ on parabola.  
$(8\sqrt{3}, 24)$ on parabola?  
$x^2 = (8\sqrt{3})^2 = 64 \cdot 3 = 192$.  
$8y = 8(24) = 192$. Yes.  
So this is a valid inscribed equilateral triangle.  

But usually, "inscribed in parabola" might imply vertices are distinct and non-degenerate. This solution works.  
Is there another one?  
Maybe $A$ and $B$ are not symmetric w.r.t y-axis.  
Let's revisit the general case.  
We established:  
1. $|VA|^2 = |VB|^2 = L^2$.  
2. $|AB|^2 = L^2$.  
3. $\angle AVB = 60^\circ$ (implied by equilateral).  

Consider the coordinate transformation to align with the chord AB? No.  
The equation for points on parabola in terms of $x$:  
$y = x^2/8$.  
We found a solution where A and B are symmetric w.r.t y-axis.  
Let's check if this is unique or generalizable.  
Consider the case where triangle is not oriented that way.  
However, for $x^2=4ay$, the locus of points $P$ such that $\angle APB = \theta$? No.  
Let's use a coordinate transformation.  
Rotate by 90 degrees around origin? No.  
Consider a rotated parabola.  
But simply, maybe this is the only one.  
However, in general for ellipse/hyperbola/circle, there are two such triangles.  
For parabola $y=x^2$, we found $x_A = x_B$ or $x_A = -x_B$?  
If $x_A = -x_B$, we have symmetric triangle. But this requires the vertex angle $\angle A V B$ to be $60^\circ$.  
With points $(x, y)$ and $(-x, y)$, the angle at origin is determined by vector product.  
$\vec{V A} = (x, x^2/8)$, $\vec{V B} = (-x, x^2/8)$.  
Cross product magnitude: $|x(x^2/8) - (-x)(x^2/8)|$? No.  
Area is $0.5 \times 2x \times y_{\text{mid}} = x \cdot y/2$? No.  
Vertices $(0,0), (x,y), (-x,y)$.  
Base $AB$ lies on line $y=y_A$. So distance is $2|x|$. Height from origin to chord $y=y_A$ is $0$?? No.  
Distance from origin to line $y=x^2/8$? Origin is at vertex, line passes through $(x,y)$.  
The chord is horizontal segment from $(-x, y)$ to $(x, y)$.  
Height of triangle from V to AB is the perpendicular distance between $(0,0)$ and $y=y_A$.  
This is simply $y = x^2/8$. But this line is at distance 0? No.  
The vertices are not collinear with origin unless y=0.  
Distance from origin to line AB: The line containing A and B is $y = x_A^2/8$.  
The vertex V is $(0,0)$. The perpendicular distance is $y / \sqrt{...}$? No.  
Line equation: $X - x_X + y - y_Y$ ? No.  
Line passes through $(x,y)$ and $(-x,y)$. Equation is $Y = y$. No. This is horizontal.  
So the height is just $y$. But distance to origin (vertex) from line $y=k$?  
The point $(0,0)$ has coordinates. Distance to line $X - x + Y = 0$? No.  
Distance from origin to line connecting A and B:  
Line AB is $y_A = \text{const}$? No. A is $(x_A, y_A)$. B is $(-x_A, y_A)$.  
Yes, they have same y-coordinate. So the segment AB is horizontal.  
The perpendicular distance from origin to the line segment AB (which lies on $Y=y_A$) is NOT simply $y_A$.  
Distance from $(0,0)$ to line $Y=Y_A$? No, line equation is $Y = Y_A$.  
This means X varies. The distance from $(0,0)$ to line $Y-Y_A=0$? No, it's just the y-coordinate.  
But for an equilateral triangle with base on horizontal line at height $h$, the vertex must lie on the perpendicular bisector of the base.  
The perpendicular bisector is the vertical line through the midpoint of AB (which is x=0).  
So V(0,0) lies on this bisector. This works perfectly for our symmetric solution.  

But does an equilateral triangle inscribed in parabola necessarily have to be symmetric?  
Consider $y = x^2$. We can rotate.  
Let's check if there are other solutions where A and B are not symmetric w.r.t y-axis.  
Let $\alpha$ be angle of A with vertical axis. Let $\beta$ be angle of B with vertical axis.  
Or simply let's try a coordinate approach without symmetry assumption.  

Let $u, v$ be the parameters $x$. We have $f(u) = u^2 + u^4/64$ and $g(v) = v^2 + v^4/64$.  
We need $|VA| = |VB| \implies f(u) = f(v)$. Since $u,v$ are x-coords of vertices on parabola, and $f(x)$ is monotonic for $x \ge 0$, we likely have either $u=v$ (degenerate) or $u=-v$.  
If $u=v$, then A=B. Not a triangle.  
So if $|VA|=|VB|$ for non-degenerate A,B, must be that $A$ and B are not necessarily symmetric in x, but could be different?  
Let's check. $f(x) = x^2 (1 + x^2/64)$. This is strictly increasing for $x \ge 0$.  
If we require $|VA| = |VB|$, then either $x_A^2 = x_B^2$ or $x_A^2+x_B^2$ etc? No.  
$x_A^2(1 + x_A^2/64) = x_B^2(1 + x_B^2/64)$ implies either $|x_A| = |x_B|$ OR other relation?  
Let's analyze the function $f(t)$. It increases for $t \ge 0$.  
$f(t) = t^2 + (t^4)/64$.  
If $f(u) = f(v)$ and $u,v$ are real.  
Is it possible to have two different positive $u,v$ such that $u \neq v$?  
Suppose $u=1, v=0.5$? No. $f(t)$ is monotonic increasing for $t>0$.  
So if $u^2 > 0$ and $v^2 > 0$, then $f(u)=f(v) \implies u^2 = v^2 \implies u^2=v^2 \implies u=\pm v$.  
Since we assumed non-degenerate triangle, $A \ne B$, so if one is positive, other must be negative or same sign with different value. But value of function depends on $x^2$. So it implies $u^2 = v^2$.  
This means either $x_A = x_B$ (impossible if distinct) or $x_A = -x_B$.  
So the vertices A and B must be symmetric w.r.t y-axis.  

Is this true? Let's double check.  
The condition $|VA|=|VB|$ means distance from origin is equal.  
Distance squared  

## Answer

*(none: the token cap hit during thinking)*
