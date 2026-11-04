# test/precalculus/580.json (Precalculus, level 3)

> Let $A = (1,-11,2),$ $B = (3,-4,1),$ and $C = (-2,1,-1).$  Compute $\angle ABC,$ in degrees.  

**Correct.** Gold `120^\circ`, predicted `120^\circ`. Finish: stop, 14070 tokens, 5 waits, 1281.6 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

The user wants me to compute the angle between two lines or vectors? No, the order of letters suggests the vertices $A$, $B$, and $C$. The notation $\angle ABC$ refers to the angle formed at vertex $B$ by the points $A$, $B$, and $C$. This means we need to find the angles that are formed by the segments from $B$ to $A$ and $B$ to $C$, but actually, it's the angle between vectors $\vec{BA}$ and $\vec{BC}$? Or is it the angle in the plane of triangle $ABC$? The notation $\angle ABC$ usually means the angle between the vectors $\vec{BA}$ and $\vec{BC}$ (or $\vec{CB}$ and something else). Let's clarify. In $\triangle ABC$, $\angle B$ is the angle at vertex $B$. However, since these points define a triangle, we can treat $A$, $B$, $C$ as coordinates in 3D space. But the problem states to compute $\angle ABC$. Usually, this implies finding the angle at vertex $B$.  

Let's check if $A, B, C$ form a plane or are coplanar. The problem doesn't state that they lie on a flat surface, but usually coordinates like this imply they define an angle in 3D space between lines connecting $A$ and $B$, and $C$ and $B$. However, the question likely asks for the angle $\theta$ such that $\vec{BA} \cdot \vec{BC} = |\vec{BA}| |\vec{BC}| \cos(\theta)$ or something similar? Or is it just a vector angle between two vectors originating from $B$? No, vectors from $A$ to $B$, $C$ to $A$?  

Let's consider the standard convention: In $\triangle ABC$, $\angle B$ is the angle at vertex $B$. The rays are $BA$ and $BC$. So it's the angle between the vectors $\vec{AB}$ and $\vec{BC}$. Let's verify the notation. $\angle XYZ$ usually denotes the angle at vertex $X$ formed by segments $XY$ and $YZ$.  
If the problem meant the angle of a triangle, it would likely specify coordinates.  
Let's interpret "Compute $\angle ABC$" as the angle subtended at point $B$? No, that is not how notation works.  
Actually, looking at standard geometry problems of this type (often found in math competitions or homework), $A$, $B$, $C$ usually form a triangle in the plane. Or maybe in 3D. If it's just a coordinate calculation, I should calculate the angle between vectors $\vec{AB}$ and $\vec{BC}$. But "angle at B" means the angle formed by lines connecting $B$ to $A$ and $B$ to $C$.  

Let's re-read carefully: $A=(1,-11,2)$, $B=(3,-4,1)$, $C=(-2,1,-1)$.  
Compute $\angle ABC$.  
Usually, for a triangle in 3D space with vertices $A, B, C$, the angle at vertex $B$ is defined by vectors $\vec{BA}$ and $\vec{BC}$. However, if they are just points in space, we can consider the coordinates. But the question asks for degrees.  
Let's calculate the coordinates:  
$A = (1, -11, 2)$  
$B = (3, -4, 1)$  
$C = (-2, 1, -1)$  

First, check if they are coplanar. A vector $\vec{BC} = C - B$. Let's calculate the dot product of vectors from vertex $B$ to $A$ and $B$ to $C$, or perhaps between vectors $\vec{BA}$ and $\vec{BC}$ (where $A, B, C$ form a triangle). The notation $\angle ABC$ implies the angle at point $B$. So we need to find the angle between vector $\vec{BA}$ and vector $\vec{BC}$.  
Let's verify this is standard convention. If points are $P_1, P_2, P_3$, the angle at $P_2$ is usually denoted as $\angle P_1 P_2 P_3$. So $\angle ABC$ would correspond to vertices $A, B, C$.  
However, there is a slight ambiguity. In many contexts (like calculating the "angle" of a triangle plane), $\angle ABC$ refers to the angle between vectors $\vec{BA}$ and $\vec{BC}$. Let's proceed with this assumption but be careful if the result is weird or if it implies a plane angle vs 3D angle. Given no mention of projection or orthogonality, I'll assume it's a standard triangle angle in 3D space (or planar).  

First, calculate vectors:  
$\vec{BA} = A - B = (1-3, -11 - (-4), 2 - 1) = (-2, -7, 1)$  
$\vec{BC} = C - B = (-2-3, 1 - (-4), -1 - 1) = (-5, 5, -2)$  

Let's compute the dot product of $\vec{BA}$ and $\vec{BC}$:  
$u = (-2, -7, 1)$  
$v = (-5, 5, -2)$  
$u \cdot v = (-2)(-5) + (-7)(5) + (1)(-2)$  
$= 10 - 35 - 2 = -27$  

Now we need the magnitudes of $u$ and $v$.  
$|u|^2 = (-2)^2 + (-7)^2 + (1)^2 = 4 + 49 + 1 = 54$  
$|u| = \sqrt{54} = \sqrt{9 \cdot 6} = 3\sqrt{6}$  

$|v|^2 = (-5)^2 + (5)^2 + (-2)^2 = 25 + 25 + 4 = 54$  
$|v| = \sqrt{54} = 3\sqrt{6}$  

$\cos(\theta) = \frac{u \cdot v}{|u||v|} = \frac{-27}{(3\sqrt{6})(3\sqrt{6})} = \frac{-27}{9 \cdot 6} = \frac{-27}{54}$  
$\cos(\theta) = \frac{-1}{2}$  

So $\theta = \arccos(-0.5)$.  
We need to find the angle in degrees.  
The answer would be $120^\circ$ or $240^\circ$? Usually angles between vectors are considered positive and in $(0, \pi]$. So it should be $120^\circ$.  
Let's double check the question phrasing. "Compute $\angle ABC$, in degrees." It is an angle between two rays originating from B.  
Is there any possibility that $\angle ABC$ means something else? Could it be the angle between vectors $\vec{BA}$ and $\vec{BC}$ but oriented differently?  
Usually, if $A=(1,-11,2)$, $B=(3,-4,1)$, then $\vec{BA} = A-B$. If we consider triangle $ABC$, the interior angle at $B$ is between vectors $\vec{BA}$ and $\vec{BC}$. That seems correct.  

However, there might be an interpretation where coordinates are in a specific plane? Let's check if the points form a 3D angle.  
If the question implies finding the angle of the triangle in terms of planar geometry, we just need to find the dot product. If it's just about the triangle plane, it would be $\arccos(\dots)$. The result $-1/2$ is quite clean.  

Let me double check coordinates calculation.  
$A = (1, -11, 2)$  
$B = (3, -4, 1)$  
$C = (-2, 1, -1)$  

$A-B$: $x: 1-3=-2$, $y: -11 - (-4) = -7$, $z: 2 - 1 = 1$. Correct.  
$B-C$: $x: -5$, $y: 1-(-4)=5$, $z:-1-1=-2$.  
Vector $\vec{BC} = (-5, 5, -2)$.  

Dot product $\vec{BA} \cdot \vec{BC}$:  
$(-2)(-5) + (-7)(5) + (1)(-2)$  
$= 10 - 35 - 2 = -27$. Correct.  

Magnitudes squared:  
$\vec{BA}^2 = 4 + 49 + 1 = 54$. $\sqrt{54}$.  
$\vec{BC}^2 = 25 + 25 + 4 = 54$. $\sqrt{54}$.  

Cosine: $\frac{-27}{54} = -0.5$. Correct.  
Arccos(-0.5) = $120^\circ$ (since cosine is negative in second quadrant). Or maybe $360-120$, but angle between two vectors is usually in $[0, 180]$. So $120^\circ$.  

Let's consider the possibility of "angle at B" meaning something else. If the vertices were coplanar, say on a plane, the angle could be calculated using sine or cosine relative to the normal? No, if they form a triangle in space (which is what the coordinates usually imply unless stated otherwise), then we just use the vectors. If $A,B,C$ are points in 3D space, the angle is defined by the dot product formula derived above.  

Is it possible that $\angle ABC$ refers to something else? Sometimes notation is $\vec{AB} \cdot \vec{BC}$. That would be $(B-A) \cdot (C-B)$? Or $A-B$? If angle at B, then usually vectors starting at B. So $\vec{BA}$ and $\vec{BC}$.  
Could it be the plane of triangle? If $A, B, C$ form a triangle in space (non-collinear), the angle at B inside the triangle is between vectors $\vec{BA}$ and $\vec{BC}$. This seems to be the most likely interpretation.  

Let's re-verify if any other interpretation is possible.  
Maybe coordinates are $(x_1, y_1, z_1) = (1, -11, 2)$ etc.  
Is it a 2D plane? No, no x,y,z relation given that would reduce to 2D. The calculation yields $-0.5$, which is an angle of $120$ or $240$. Since it's an angle between lines/segments in space, we must be careful about conventions. In standard Euclidean geometry problems involving vectors:  
If we want $\vec{v} = \dots$, the angle between $\vec{u}$ and $\vec{v}$ is $\arccos(\frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|})$.  
However, sometimes "angle" in a triangle refers to the interior angle. If we have $A, B, C$ forming a triangle. We can compute the dot product of vectors $\vec{AB}$ and $\vec{AC}$? No, that's not right for $\angle ABC$.  
The vertices are points. The edges connecting them are segments $AB$, $BC$, $CA$. The angles at these vertices are internal angles.  
$\angle ABC$ is the angle between segment $BA$ and segment $BC$. This means we are looking for the angle between vectors $\vec{BA}$ (vector from B to A) and $\vec{BC}$ (vector from B to C).  

Let me double check my vector calculation again.  
$A - B$: $(1-3, -11+4, 2-1) = (-2, -7, 1)$? No, $y$ is $-11 - (-4) = -11 + 4 = -7$. Correct.  
$\vec{BA} = (-2, -7, 1)$.  
$\vec{BC} = (-2-3, 1-(-4), -1-1) = (-5, 5, -2)$. Correct.  

Dot product:  
$x_1 x_2 + y_1 y_2 + z_1 z_2$  
$= (-2)(-5) + (-7)(5) + (1)(-2)$  
$= 10 - 35 - 2 = -27$.  

Magnitude squared:  
$|A-B|^2 = (-2)^2 + (-7)^2 + (1)^2 = 4+49+1=54$.  
$|C-B|^2 = (-5)^2 + (5)^2 + (-2)^2 = 25+25+4=54$.  

Result: $\cos(\theta) = \frac{-27}{(3\sqrt{6})(3\sqrt{6})} = \frac{-27}{9(6)} = -0.5$.  
The angle is $120^\circ$ or $2\pi/3$ rad? No, degrees are requested.  
Is there any nuance I'm missing? "Compute $\angle ABC$". In a triangle problem in 3D, usually coordinates are just points on the surface of the sphere (or plane). If they were all on a plane, we would have vectors lying in that plane. The angle is determined by the dot product. If it's not coplanar, it's a general vector calculation in space, which gives a unique value (180 degrees if collinear, or something else). Here the vectors form a cosine of -1/2, so $120^\circ$.  

Let me pause and think: Is there any chance this is an angle between two vectors $\vec{AB}$ and $\vec{AC}$? That would be $\angle A$ (or $\angle CAB$). The question asks for $\angle B$.  
Is it possible the answer is not $120^\circ$ but something else due to coordinate errors? No, I'm fairly certain about arithmetic.  
Let's check the subtraction again.  
$A = (1, -11, 2)$  
$B = (3, -4, 1)$  
$C = (-2, 1, -1)$  

Vector $\vec{BA} = (1-3, -11-(-4), 2-1) = (-2, -7, 1)$.  
Vector $\vec{BC} = (-2-3, 1-(-4), -1-1) = (-5, 5, -2)$.  
Dot product: $-2(-5) + (-7)(5) + 1(-2) = 10 - 35 - 2 = -27$.  
$|\vec{BA}| = \sqrt{4+49+1} = \sqrt{54}$.  
$|\vec{BC}| = \sqrt{25+25+4} = \sqrt{54}$.  
$\cos(\theta) = -0.5$.  
$\theta = 120^\circ$.  

Let's double check if there is any interpretation where the angle refers to the exterior angle? No, "angle $\angle ABC$" is standard for the interior angle at vertex B in a triangle. But sometimes it might mean something else? Or maybe it is asking for the supplement? The cosine rule gives the side length relationships.  
Is there any possibility that the question meant $AB \perp BC$ or $AB^2 + BC^2 = AC^2$? No, "angle" implies finding the measure.  

What if the problem is from a specific context where coordinates are in some rotated frame? No, just 3D space.  
Is it possible that $\angle ABC$ means angle between vectors $\vec{BA}$ and $\vec{CB}$? No, usually angle at B refers to rays $BA$ and $BC$. If we consider vector directions $BA$ and $CB$, the angle is the supplement of interior angle.  
Let's check if vectors $\vec{BA}$ and $\vec{CB}$ give a different answer.  
$\vec{CB} = B - C = (3 - (-2), -4 - 1, 1 - (-1)) = (5, -5, 2)$.  
Dot product $u \cdot v$ with $u=(-2,-7,1)$ and $v=(5,-5,2)$:  
$-2(5) + (-7)(-5) + 1(2) = -10 + 35 + 2 = 27$.  
$\cos(\phi) = \frac{27}{\sqrt{54}\sqrt{54}} = \frac{27}{54} = \frac{1}{2}$.  
So $\phi = 60^\circ$.  
The question is ambiguous in standard geometry notation without specific definition of "angle at B" being the interior angle vs external angle. However, typically "Angle between vectors" or "Triangle angle" implies the smaller (convex) angle usually measured as positive.  
Usually, in a triangle, $\angle ABC$ is the angle inside the triangle. If the points $A, B, C$ form a triangle where we compute angles using cosine law or dot product, they are interior angles.  
Let's check if the vector $\vec{CB}$ corresponds to direction $B \to C$. That is not "ray BC" but ray from C to B. But angle is always defined by two rays originating from common point. The common point for rays $BA$ and $BC$ is $B$. So we are looking for angle between vector $\vec{BA}$ and vector $\vec{BC}$.  

In some contexts (e.g. vector spaces), $\angle ABC$ can be interpreted as $\cos^{-1}(\frac{\vec{BA} \cdot \vec{BC}}{|BA||BC|})$. This is the standard interpretation.  
Also, note that if points are in a triangle, the angle at vertex B could be acute or obtuse. Here it's obtuse.  

One more check: Is $A$ collinear with something? No.  
Is $A, B, C$ coplanar? Yes, vectors lie in 3D space, which implies they define a plane. The calculation holds.  
Is there any other interpretation of $\angle ABC$?  
In geometry problems where points are on the surface of a sphere, the angle is usually defined using spherical coordinates or similar. But here they are given as Cartesian coordinates.  
If it's just "Compute the angle", and it says $\angle ABC$, it means at $B$.  

Let's double check calculation $y = -7$?  
$A_y = -11$. $B_y = -4$.  
$-11 - (-4) = -11 + 4 = -7$. Yes.  
$z = 2 - 1 = 1$. Yes.  
$x = 1 - 3 = -2$. Yes.  

$\vec{BA} = (-2, -7, 1)$.  
Check magnitude: $4+49+1=54$. $\sqrt{54}=3\sqrt{6}$. Correct.  

$\vec{BC} = C - B = (-2-3, 1-(-4), -1-1) = (-5, 5, -2)$.  
Check magnitude: $25 + 25 + 4 = 54$. $\sqrt{54}=3\sqrt{6}$. Correct.  

Dot product: $-2(-5) + (-7)(5) + 1(-2) = 10 - 35 - 2 = -27$.  
Cosine: $-27 / (54 \times 3\sqrt{6})$? No, just divide by squares.  
Denominator is $|\vec{BA}||\vec{BC}| = 54$. Numerator is $-27$.  
So $\cos \theta = -27/54 = -1/2$.  

This seems very straightforward. Is there any catch?  
Let's consider the possibility of error in coordinate calculation of C.  
$C=(-2,1,-1)$. $B=(3,-4,1)$.  
$x_C - x_B = -2-3 = -5$. Correct.  
$y_C - y_B = 1-(-4) = 5$. Correct.  
$z_C - z_B = -1-1 = -2$. Correct.  
So $\vec{BC} = (-5, 5, -2)$. Correct.  

Let's check $A=(1,-11,2)$. $B=(3,-4,1)$.  
$x_A - x_B = 1-3 = -2$. Correct.  
$y_A - y_B = -11 - (-4) = -7$. Correct.  
$z_A - z_B = 2 - 1 = 1$. Correct.  
So $\vec{BA} = (-2, -7, 1)$. Correct.  

Let's check the vector cross product just in case (orthogonality? no).  
Is there any hidden interpretation where angle is defined differently?  
Maybe $A$ and $B$ are points on a surface? No.  

What if the notation $\angle ABC$ refers to the angle of rotation from one line to another? That's what it means here.  
Could there be a typo in my calculation of coordinates?  
Let me re-read the problem statement provided by user.  
"A = (1,-11,2), B = (3,-4,1), and C = (-2,1,-1)."  
Looks fine.  

Let's do a sanity check on $-27/54$. $-1/2$. Angle 120 degrees.  
Let's visualize the vectors.  
$\vec{BA} = (-2, -7, 1)$.  
$\vec{BC} = (-5, 5, -2)$.  
Plot them in a grid.  
From B:  
$A$ is at distance $\approx \sqrt{54} \approx 7.3$ from origin? No. $B$ is origin for calculation relative to vectors.  
The angle between vector with length $\sqrt{54}$ and vector with length $\sqrt{54}$. The dot product is $-27$, which is large negative (magnitude 27, half of sum). So the angle should be obtuse. $60+90=150$? No.  
With vectors $\vec{u}$ and $\vec{v}$ of equal length $L$. Angle is $\arccos(-0.5) = 120^\circ$. This is clearly not acute ($<90^\circ$). It's obtuse.  

Could there be any reason to compute the angle of the triangle using the plane normal?  
Since the question asks for a degree, and no mention of 3D vectors in plane calculation (like finding a distance), it likely just asks for the geometric angle between vectors at vertex B. The phrase "angle between vectors $\vec{AB}$ and $\vec{BC}$" is often interpreted as interior angle. Sometimes it's $\vec{BA}$ and $\vec{BC}$. This doesn't change the angle, except if one uses vectors starting at origin but here they start from $B$.  
If we used $\vec{AB}$ and $\vec{AC}$, the angle would be $\angle A$, not $\angle B$.  
So it is indeed between $\vec{BA}$ and $\vec{BC}$.  

Is there any nuance about $\vec{BC}$? If the question asks for the angle of triangle $ABC$ at vertex B, usually it refers to the plane geometry. But if the points are in 3D space, we need to know which vector is the "edge" or side direction.  
The edges are lines connecting B to A and B to C. The vectors defining them are $\vec{BA}$ and $\vec{BC}$. The angle between them is $120^\circ$.  

Let's verify if there's any tricky wording I missed.  
"Let $A = (1,-11,2), B = (3,-4,1),$ and $C = (-2,1,-1).$ Compute $\angle ABC,$ in degrees."  
Standard math notation for a vector is $\vec{u}$ pointing from origin to A, but here vectors start at B.  
Usually, if it's a triangle in the plane, vertices are collinear? No. The points form a triangle.  
Maybe I should check the "angles" of the triangle using law of cosines or dot products?  
Yes, $\cos \angle B = \frac{AB^2 + BC^2 - AC^2}{2 AB \cdot BC}$? No. $\cos B = \frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|}$.  
This is what I did.  

Could it be that we need to compute the angle between two vectors given as coordinates in some other space? No, standard context.  

Let's double check arithmetic one more time.  
$x_1 x_2$: $(1-3) = -2$, $(-2)$. Correct.  
$y_1 y_2$: $(-11+4) = -7$. $x=1, y=4$? No, $A_y+B_x$? No. $-11-(-4)=-7$. Correct.  
$z_1 z_2$: $(2-1)=1$. Correct.  
Sum squares: $4+49+1=54$. Correct.  

$x'_c = -5$. $x'_y = 5$. $z'_c = -2$. Sum squares: $25+25+4=54$. Correct.  
Dot product: $(-2)(-5) + (-7)(5) + (1)(-2)$.  
$10 + (-35) + (-2)$? No. $(1)(-2) = -2$. So sum is $-27$.  
Is the dot product $10 - 35 - 2 = -27$? Yes.  

Could the vectors be defined as $\vec{AB}$ and $\vec{CB}$?  
Then angle would be same if we just flip signs of vectors? No, $\cos \phi = \frac{\vec{AB} \cdot \vec{CB}}{|AB| |CB|}$.  
$\vec{AB} = (2, 7, -1)$.  
$\vec{CB} = (5, -5, 2)$? No. $B=(3,-4,1), C=(-2,1,-1)$. $\vec{CB} = (-3, 3, -2)$.  
Dot product: $(2)(-3) + (7)(3) + (-1)(-2) = -6 + 21 + 2 = 17$.  
Magnitudes: $|AB|=\sqrt{54}$? No $\vec{AB}^2 = (2)^2+7^2+(-1)^2=4+49+1=54$. Same magnitude.  
$|CB|^2 = (-3)^2 + 3^2 + (-2)^2 = 9+9+4=22$. Not same as $\sqrt{54}$.  
So this is not the case.  

The question asks for "angle ABC". Standard notation implies angle at vertex B. The vectors forming this angle start at B and end at A and C. So $\vec{BA}$ and $\vec{BC}$ are candidates.  

However, there is a catch with coordinate geometry problems sometimes involving orthographic projections. But here no projection matrix or similar is given.  
Is it possible the points are on a sphere? No, coordinates given.  
Let's check if there's any ambiguity in "Compute $\angle ABC$".  
If it was a 2D plane problem, the coordinates would be such that they lie on a plane and we could find the angle between them using cross product magnitude? Or just $\arccos(\dots)$. But since no other info is given (like points being coplanar), I assume general position in 3D space. The calculation is robust to this assumption.  

Let's think about potential pitfalls.  
Did I copy coordinates correctly?  
A: 1, -11, 2. Correct.  
B: 3, -4, 1. Correct.  
C: -2, 1, -1. Correct.  

Is it possible that the question asks for the angle between $AB$ and $BC$? i.e. $\angle ABC$ is the angle *between* vectors from A to B and C to B? No, standard notation is rays from vertex.  
Or maybe $\angle ABC$ refers to the angle between the lines containing the sides AB and BC.  
In a triangle in 3D space, these are just lines passing through B. The angle of intersection at B is well-defined as the angle formed by the vectors along these lines.  
Usually, this is what we compute.  
Is there any ambiguity about the notation $\angle ABC$? Some textbooks might denote it $\angle CBA$ or something to avoid confusion with orientation. But standard convention is interior angle at vertex $B$.  

Let's check if the magnitude of dot product is zero? No.  
Magnitude of vector products:  
$|\vec{BA}| = \sqrt{54}$.  
$|\vec{BC}| = \sqrt{54}$.  
So $\cos B = -1/2$. $B = 120^\circ$.  

Let's check the problem source or similar problems online. "Compute angle ABC given coordinates". This looks like a standard vector geometry question often found in math competitions (e.g., AMC 12, AIME).  
If it was an exercise asking for something else, like lengths, I would calculate side lengths. But angle is asked.  
Is there any chance the answer is simply $\arccos(-0.5)$? Yes.  
Could it be $360 - 120$? Or just degrees in $(0, 180)$ usually implies acute/obtuse range $[0, 180]$. So $120^\circ$.  

Let's do a quick check on the vector components again.  
$A = (1, -11, 2)$.  
$B = (3, -4, 1)$.  
$C = (-2, 1, -1)$.  
Vector $\vec{BA} = A - B = (-2, -7, 1)$.  
Vector $\vec{BC} = C - B = (-5, 5, -2)$.  

Let's calculate cross product $\vec{AB} \times \vec{BC}$ to find normal vector? No, we need the angle between them.  
Dot product: $(-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$.  
Correct.  
Magnitudes: $\sqrt{4+49+1} = \sqrt{54}$. Correct.  
Result: $-27 / 54 = -1/2$.  
Result: $180^\circ$? No, arccos(-0.5) is $120^\circ$.  

The only potential issue is if the points are collinear? No, $\vec{BA} \cdot \vec{BC} = 10 - 35 - 2 \neq 0$.  
Collinear means $y=z$? $(-7,-2)=0$? No.  
If it were in 3D space with points forming a flat triangle (e.g. on a plane), the angle would be $\arccos(\dots)$. But even if they were coplanar, we need to know which vectors are relevant. If they form a closed triangle, the vectors at B should point from vertex B to vertices A and C. So this is correct.  
What if the notation $\angle ABC$ meant angle between line $AB$ and line $BC$? That is exactly the angle between the lines passing through B containing the segments $AB$ and $BC$. Since they are just rays or infinite lines in 3D, the angle is either acute or obtuse. The calculation gives 120 degrees which fits standard definition for intersection of two lines originating at B.  

Let's check if there is an alternative interpretation of coordinates that might change the result.  
Maybe $A=(1,-11,2)$ means something different? Unlikely. Standard cartesian notation.  
If it was a trick question and meant $\cos^{-1}(x) = y$? No.  
The problem asks to "compute". Usually, this implies finding the exact value or an integer. $-0.5$ leads to exactly 120 degrees.  

Let's double check calculation of sum of squares:  
$1^2 + (-7)^2 + 1^2 = 1 + 49 + 1 = 51$. No, 4+49+1 is 54. $2^2=4, 3^2=9, 1^2=1$. Yes, $4+49+1=54$.  
Sum of squares for other:  
$(-5)^2 + (5)^2 + (-2)^2 = 25 + 25 + 4 = 54$.  
Dot product is sum of terms where $u_i v_j$:  
$-2(-5) = 10$.  
$-7(5) = -35$.  
$1(-2) = -2$.  
Sum: $10 - 35 - 2 = -27$.  

Everything seems solid.  

Is there any chance the question implies finding $\angle B$ in the plane spanned by vectors?  
The vectors lie in some plane passing through B (the vector space). If they lie in a 2D subspace defined by $B$, then we can compute the angle using just the dot product, which is invariant regardless of coordinate origin. Since I calculated $\angle ABC$ using only coordinates in 3D space and no constraint on "plane" or "projection", this must be sufficient. The question doesn't specify that A, B, C lie in a specific plane, so I assume general coordinates. If they were all coplanar, the result would be the same because dot product depends only on differences between points (which is independent of reference frame), and magnitude depends on distance to origin? No, magnitude depends on coordinates relative to B. $\vec{AB} = A-B$, etc. Magnitudes $|\vec{BA}|$ are constant regardless of coordinate system if we use $B$ as origin. Since the angle $\theta$ is defined by the dot product formula $u \cdot v / (|u||v|)$, and that involves only relative vectors from B to A and C, it works regardless of whether B is considered in a plane or not? No.  
Let's re-read: "Compute $\angle ABC$". This defines the geometry of the triangle formed by points $A,B,C$.  
The angle at vertex B is the angle between the two lines segments connecting B to A and B to C.  
In 3D space, we treat vectors as elements of a vector space. The angle between these vectors in Euclidean space (standard) gives the result directly.  

One edge case: "angle ABC" could mean the angle subtended by the arc AB and BC? No, vertices usually mean segments.  

What if the coordinates were 2D but mixed up with 3D?  
$y=-4$. $z=1$. $x=3$. All integers.  
If it was planar points in 3D, we are done.  

The result is an integer (or a rational number leading to integer degrees). $120^\circ$ fits perfectly.  

Let's check if I made a sign error.  
Vector $\vec{BA} = (-2, -7, 1)$.  
Vector $\vec{BC} = (-5, 5, -2)$.  
Dot product: $(-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$.  
Magnitudes: $\sqrt{54} \approx 7.348$.  
$\cos(\theta) = -27 / (54 \times \dots)$?  
$|\vec{BA}| \approx 7.348$.  
$|\vec{BC}| \approx 7.348$.  
Product of magnitudes $\approx 54$.  
Ratio is $-27/54 = -0.5$.  
Correct.  

Let's verify if the angle could be $60^\circ$?  
If we took $\vec{CB}$ instead of $\vec{BC}$, dot product was positive, cosine would be positive.  
$\cos(60) = 1/2$. So angle would be $60^\circ$.  
Does "angle ABC" imply the interior angle of a triangle? Or just the angle between segments $BA$ and $BC$?  
Usually, in geometry, $\angle ABC$ refers to the interior angle of the triangle. If the points are arranged in counterclockwise order around B (looking from perspective of observer), or rather just looking at the segment lengths. The orientation doesn't affect the magnitude unless it asks for the oriented angle, which is usually $[0, 180]$.  
However, sometimes "angle ABC" might mean $\angle (\vec{BA}, \vec{BC})$? No, vectors originate at B.  
If the question was to find $\angle A$, we would compute dot product of $\vec{BA}$ and $\vec{CA}$.  
Here it is $\angle B$.  
So it should be $120^\circ$.  

I will formulate the final response based on this calculation.  
Steps:  
1. Identify vertices $A, B, C$ with coordinates.  
2. Form vectors starting from $B$: $\vec{BA} = A - B$, $\vec{BC} = C - B$.  
3. Compute dot product and magnitudes of these vectors.  
4. Calculate $\cos(\theta) = \frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|}$.  
5. Determine the angle $\theta$ in degrees.  

Calculations:  
$\vec{BA} = (-2, -7, 1)$  

*Continued in [part 2 of 2](precalculus_580_p2.md): GitHub stops rendering math on pages this long, so the transcript is split.*
