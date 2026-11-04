# test/precalculus/580.json, part 2 of 2

[Previous part](precalculus_580.md)

$\vec{BC} = (-5, 5, -2)$  
$\vec{BA} \cdot \vec{BC} = (-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$.  
$|\vec{BA}| = \sqrt{(-2)^2 + (-7)^2 + 1^2} = \sqrt{4 + 49 + 1} = \sqrt{54} = 3\sqrt{6}$.  
$|\vec{BC}| = \sqrt{(-5)^2 + (5)^2 + (-2)^2} = \sqrt{25 + 25 + 4} = \sqrt{54} = 3\sqrt{6}$.  
$\cos(\theta) = \frac{-27}{(3\sqrt{6})(3\sqrt{6})} = \frac{-27}{9 \cdot 6} = \frac{-27}{54} = -0.5$.  
$\theta = \arccos(-0.5) = 120^\circ$.  

The problem asks to compute $\angle ABC$ in degrees. The result is $120$.  

Is there any possibility that the notation $\angle ABC$ implies angle between lines $AB$ and $BC$ but maybe signed? Unlikely.  
Also, usually angles are positive by definition (unless specified otherwise).  
Also, sometimes the dot product might be zero if collinear.  
Here it's not zero.  

Is there any ambiguity with vector subtraction?  
$\vec{BA} = A - B$. Correct.  
If I used $B - A$, $\cos$ would change sign but magnitude of cosine is absolute value? No, cosine function for angle is defined on range $[0, \pi]$. So signs matter for the value. But the dot product formula gives unique angle between two vectors regardless of direction.  
$\cos(180) = -1$. Here $\cos = -0.5$.  

Is there a simpler way to write this?  
Maybe just use dot product and cosines?  
No, I should provide the reasoning clearly.  

One last check: The problem statement "Compute $\angle ABC$, in degrees." suggests an answer like 120, 30, 45, etc. Since -0.5 is not exact (but $-1/2$), the answer is exactly $120^\circ$.  
The coordinate numbers are integers, which is nice.  
Also, vectors $\vec{BA}$ and $\vec{BC}$ are of length $\sqrt{54} \approx 7.35$, dot product -27. The angle between them is obtuse.  
If we had vectors of same direction it would be acute. With opposite they are obtuse.  

Is it possible that the question is from a source where coordinates might be different?  
No, I must solve based on provided text.  

Double check arithmetic one last time.  
$(-2)(-5) = 10$.  
$(-7)(5) = -35$.  
$1(1) \cdot 1(2)?$ No $(1)(-2)=-2$.  
Sum: $10 - 35 - 2 = -27$.  
Squares sum:  
$4 + 49 + 1 = 54$.  
$25 + 25 + 4 = 54$.  
Product of squares (magnitude squared): $54 \times 54 / 9 \dots$?  
Magnitude product: $\sqrt{54} \times \sqrt{54} = 54$. No. Magnitude is $\sqrt{54} \approx 7.348$. Product of magnitudes is 54.  
$\cos = -27/54 = -1/2$. Correct.  
$90^\circ$ angle between vectors? Then dot product would be $-|\vec{u}| |\vec{v}| / \dots$ no.  

If I calculated $\vec{BC} = C - B = (-5, 5, -2)$ is correct?  
$C_x = -2, B_x=3$. $C-B$ vector x is -5. Correct.  
$y_C=1, y_B=-4$. $C-B$ vector y is 5. Correct.  
$z_C=-1, z_B=1$. $C-B$ vector z is -2. Correct.  

Okay, I am confident in the result. The angle is $120^\circ$.  

If I were to calculate using Law of Cosines on triangle ABC?  
$AB^2 = (-2)^2 + (-7)^2 + (1)^2 = 54$.  
$BC^2 = 54$.  
$AC^2$:  
$A=(1,-11,2), C=(-2,1,-1)$.  
$AC_x = 1 - (-2) = 3$.  
$AC_y = -11 - 1 = -12$.  
$AC_z = 2 - (-1) = 3$.  
$AC^2 = 9 + 144 + 9 = 162$.  
Using Law of Cosines:  
$c^2 = a^2 + b^2 - 2ab \cos C$. Here angle at B is $C'$.  
If $\theta_B = 120^\circ$:  
$AC_{side}^2 = AB^2 + BC^2 - 2(AB)(BC) \cos(\angle B)$? No, $AC^2 = a^2 + b^2 - 2ab \cos C$.  
Using vectors: $\vec{BA} \cdot \vec{BC}$ vs side lengths.  
$|\vec{CA}|^2 = |\vec{A}|^2 + |\vec{C}|^2 - 2\vec{A}\cdot\vec{C}$. No.  
Law of Cosines for angle $\theta$:  
$c^2 = a^2 + b^2 - 2ab \cos(\theta)$. Here $a=BC, b=AC$? No, side opposite B is AC. Side opposite A is BC. Side opposite C is AB.  
Let's stick to the dot product definition. It's safer than triangle law of cosines unless I can't compute sides.  
Sides:  
$a = BC = \sqrt{54}$.  
$b = AC = \sqrt{162} = 9\sqrt{2}$. (Just random check).  
$c = AB = \sqrt{54}$.  
Using Law of Cosines on angle at B? No, side AC is between B and A? Yes.  
Angle B is between sides BA and BC.  
Sides adjacent to B are $BA$ and $BC$. Side opposite is $AC$.  
$c^2 = a^2 + b^2 - 2ab \cos(\angle B)$.  
$c = AB$.  
$a = BC$.  
$b = AC$? No, side opposite B is $AC$? No.  
Sides are usually $a=BC$, $b=AC$ if vertices are labeled A, B, C in order around perimeter.  
So sides are: $AB$ (length c), $BC$ (length a), $CA$ (length b).  
$\cos(B)$ is opposite to side AC? No. Cosine rule: $c^2 = a^2 + b^2 - 2ab \cos(C)$. Here angle at B is between AB and BC. Side AC is opposite to B. So side $AC$ length squared $b^2 = a^2 + c^2 - 2ac \cos(B)$? No.  
Let vertices be A, B, C. Sides are lengths of segments connecting points in order around perimeter. But we can assume the triangle is formed by these three points. The angle at vertex B is between sides BA and BC.  
The angle subtended by side AC? No, the angle B is the angle between AB and CB (or BA and BC).  
The formula relating lengths $AB, BC, AC$ to angles $\angle A, \angle B, \angle C$.  
$\cos(B) = \frac{a^2 + c^2 - b^2}{2ac}$? No. The formula uses side adjacent. Adjacent sides are AB and BC. Opposite is AC.  
So if we denote $AB=c, BC=a, CA=b$. Then $\cos B = (a^2 + c^2 - b^2) / 2ac$. Or using vectors: $\vec{BA} \cdot \vec{BC} = |BA||BC| \cos B$.  
Using vectors $\vec{BA} = A-B$, $\vec{BC}=C-B$. $|\vec{BA}|=c', |\vec{BC}|=a'$.  
$\cos B = \frac{\vec{BA} \cdot \vec{BC}}{c'a'}$.  
My calculation was correct: $\cos B = -1/2$, angle is 120 degrees.  

The triangle side lengths are not required to be integers, but the vector approach works directly. The answer seems robust.  

Final check of the question phrasing again. "Compute $\angle ABC$".  
If I had to choose between 60 or 120?  
Vectors: $\vec{BA}$ and $\vec{BC}$.  
$\cos \theta = -0.5$. $\theta = 120^\circ$.  
Angle between line AB and line BC at B?  
Lines intersect at B. The lines extend through A and C.  
The angle between the rays BA and BC (in a triangle, interior) is $120^\circ$ (obtuse).  
If it were acute, the cosine would be positive.  
Usually "angle" means smallest positive value between 0 and 180. So 120 is correct.  

Let's do a quick check if $\vec{BA}$ and $\vec{BC}$ point in opposite directions (i.e. B is between A and C? No, just that).  
If $A$ was $(5,1,1)$ and $C$ was $(-1,1,1)$. Then vectors are roughly opposite?  
Here dot product is -27. Both lengths are equal ($\sqrt{54}$). The angle is 120 degrees.  

Is it possible that "angle ABC" means angle $\angle CBA$? No, standard is order of vertices.  
Okay, I'm set on 120 degrees.  

One final verification:  
$A=(1,-11,2)$  
$B=(3,-4,1)$  
$C=(-2,1,-1)$  
Vectors:  
$\vec{BA} = (-2, -7, 1)$  
$\vec{BC} = (-5, 5, -2)$  

Compute dot product $u \cdot v$:  
$(-2)(-5) = 10$  
$(-7)(5) = -35$  
$(1)(-2) = -2$  
Sum: $-27$.  

Compute squared lengths $|u|^2$ and $|v|^2$:  
$|-2|^2 + |-7|^2 + |1|^2 = 4 + 49 + 1 = 54$.  
$|-5|^2 + |5|^2 + |-2|^2 = 25 + 25 + 4 = 54$.  

Cosine: $-27 / (3\sqrt{6} * 3\sqrt{6}) = -27/54 = -1/2$.  

$\angle B = \arccos(-1/2) = 120^\circ$.  
The result is 120.  

I will structure the response to show the vectors, compute dot product and magnitudes, then use the formula for angle.  

One thought: What if the question implies finding $\angle ABC$ where coordinates are on a 2D plane?  
Wait, "in degrees". If points were in 3D but not coplanar, they lie on a sphere. The question is just asking about angle between lines from vertices B to A and C.  
The problem statement doesn't specify the geometry of triangle ABC or its dimensionality. Just 3 coordinates. This implies a standard vector space interpretation.  

There's no trick. The numbers are designed for $\cos = -0.5$.  
If it were something like $A=(1,-1,2)$ and $B=(3,4,1)$ etc, maybe integers align better? No, the calculation is independent of the specific values as long as they satisfy the equation.  
Since the calculation yielded a clean integer angle result, I'm confident.  

Final Answer seems to be 120.  

One check: Does $\angle ABC$ denote the angle at $A, B, C$ where the coordinates are $(x,y,z)$? Yes.  
Is there any chance "ABC" refers to something else like "Angle between lines AB and BC"? No.  
Okay, proceed with 120 degrees.  

I will write down the solution steps clearly.  
1. Identify coordinates of points A, B, C.  
2. Calculate vector $\vec{BA}$ (vector from B to A) or $\vec{AB}$? Note: The angle at vertex B is formed by rays BA and BC. It corresponds to vectors $\vec{BA} = A - B$ and $\vec{BC} = C - B$. Or just the vectors pointing away from B towards A and C.  
3. Compute dot product and magnitudes of $\vec{BA}$ and $\vec{BC}$.  
4. Apply formula $\cos(\theta) = \frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|}$.  
5. Solve for $\theta$.  

Values:  
$\vec{BA} = (-2, -7, 1)$  
$\vec{BC} = (-5, 5, -2)$  
Product of dot product is $-27$.  
Magnitude is $\sqrt{54}$.  
Angle is $120^\circ$.  

Just to be absolutely sure about the coordinates again:  

```text
A=(1,-11,2) -> x=1, y=-11, z=2.
B=(3,-4,1).
C=(-2,1,-1).
```

$\vec{BA} = (-2, -7, 1)$. Correct.  
$\vec{BC} = (-5, 5, -2)$. Correct.  
$(-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$.  
Squares: $4+49+1=54$, $25+25+4=54$.  
$\cos = -27/54 = -1/2$.  
Result $120^\circ$.  

Is there any possibility that $\angle ABC$ means angle between vectors $\vec{BC}$ and $\vec{CA}$?  
No, standard triangle vertex notation usually implies the vertices are listed in order. So $AB$, $BC$, $CA$. Angle at B is formed by sides $BA$ and $BC$.  
If the question was "find the angle $\angle B$" of a plane geometry figure, it's 120.  
So I'll stick to 120.  

Final check: Could it be interpreted as an exterior angle?  
The angle between vectors $\vec{BA}$ and $\vec{BC}$ (which originate from B) is the angle inside the triangle if they point in the same direction as the vector for side lengths, but they point towards vertices A and C. The angle between them is $180 - \alpha$. If interior is acute or obtuse. With dot product negative, it's obtuse. So 120 or 160?  
Usually "angle" means $\in (0, \pi)$, so $[0, 180]$.  
Also, the angle at vertex B in a triangle is generally defined between the segment BA and BC. This is $\arccos(\dots)$. If the result is obtuse, it's 120. If the question meant exterior, it would say so or calculate $\angle (AB, BC)$ as $60^\circ$ maybe? But that requires $\vec{BA}$ and $\vec{BC}$ to be defined differently? No. If I take vectors from B to A and B to C. The angle between them is $120^\circ$.  
This seems robust.  

I will write down the solution now.  

One minor thing: Could "Compute $\angle ABC$" mean angle at vertex B in triangle ABC if it was coplanar?  
Since coordinates are given, maybe we check for collinearity first?  
Wait, vectors are non-zero and form a triangle (area of triangle).  
Actually, $|\vec{BA}| = \sqrt{54}$, $|\vec{BC}| = \sqrt{54}$. If they were perpendicular, dot product would be 0. Not zero. So it's a valid triangle.  
If the problem was "find length of side AC", I can check that: $\sqrt{162} \approx 12.7$.  
Is there any other interpretation?  
$\angle ABC$ is simply $120^\circ$.  

I'll proceed with generating the response.  
The reasoning is solid.  

One more thing, does "Compute $\angle ABC$" imply a specific convention for notation?  
Usually, in geometry problems asking for an angle, it refers to the angle between two rays or lines originating from the vertex.  
Given points $A, B, C$, the rays are $BA$ and $BC$.  
Thus $\theta = \arccos(\frac{(-2)(-5)+(-7)(5)+(1)(-2)}{|\vec{BA}||\vec{BC}|})$.  
Calculated as $120^\circ$.  

If I consider the vectors to be from origin, say $O$ is not involved? No.  
Just $\vec{v_1} = \vec{OA}$? No, vectors are defined as difference of points.  
Okay.  

The solution should show the vectors and the dot product.  
The steps are clear.  

I will format the output with LaTeX.  
\boxed{120^\circ}. Or just the number inside box if requested.  
"Compute $\angle ABC$, in degrees." -> Boxed answer usually contains the degree value or the expression. I will write 120^\circ. Or just 120. Usually "degrees" is specified at the end, so I should probably put the value with the unit? The prompt says "put your final answer within \boxed{}". It's safer to put the full value like $120^\circ$.  

Double check the question: "Please reason step by step".  
So I need to write out the reasoning clearly.  
And then boxed the result.  

Final verification of coordinates reading again.  

```text
A: 1, -11, 2
B: 3, -4, 1
C: -2, 1, -1
```

Vectors:  
$BA = (1-3, -11-(-4), 2-1) = (-2, -7, 1)$  
$BC = (-2-3, 1-(-4), -1-1) = (-5, 5, -2)$  
Dot product $= 10 - 35 - 2 = -27$.  
Squares: $4+49+1 = 54$, $25+25+4 = 54$.  
$\cos \theta = -27 / 54 = -1/2$.  
$\theta = 120^\circ$.  

If there was any chance that the answer is $120 + 60$ or something, it would be weird in such problems.  
Also, if it were $90$, dot product would be 0.  
If it were $60$, dot product would be $\pm \sqrt{54}/\sqrt{54} = \pm 1$. Since it's -0.5, it's not 90 or 60 (which are cosines of these angles).  
So 120 is correct.  

I'm ready to write.  

One tiny check:  
Is it possible the question meant $A, B, C$ in a plane and asked for angle between them?  
Usually this phrasing implies general position unless stated "on a plane".  
However, if they were on a plane, we could compute $\theta = 120^\circ$ relative to the normal? No.  
In a plane geometry context (like in a triangle sheet), if points lie on the same plane, the vectors are in that plane. The angle between vectors $\vec{BA}$ and $\vec{BC}$ is the same regardless of whether they are 3D or planar relative to the vertex B (if we just measure angle at vertex). If they were coplanar but not forming a triangle with origin? No, the triangle formed by points in space. The angle between vectors $BA$ and $BC$ is well defined as determined by their coordinates.  
If we are in 2D plane where vertices are $(1,-11)$, etc., then vectors are in same plane. Angle between them is just dot product.  
The problem doesn't specify a plane or origin reference, so it's purely standard 3D vector geometry.  

Final Answer: 120 degrees.  
\boxed{120^\circ}  


## Answer

To find the angle $\angle ABC$, we interpret this as the angle between the vectors originating from vertex $B$. The vertices are given in a 3D Cartesian coordinate system.  
The points are:  
$A = (1, -11, 2)$  
$B = (3, -4, 1)$  
$C = (-2, 1, -1)$  

First, we define the vectors that form the sides of the angle at vertex $B$. The vector $\vec{BA}$ points from $B$ to $A$, and $\vec{BC}$ points from $B$ to $C$. (Note: Standard notation for "angle at B" in a triangle uses rays originating from B to vertices A and C).  

Let's compute these vectors:  
$$ \vec{BA} = A - B $$  
$$ x_A - x_B = 1 - 3 = -2 $$  
$$ y_A - y_B = -11 - (-4) = -7 $$  
$$ z_A - z_B = 2 - 1 = 1 $$  
So, $\vec{BA} = (-2, -7, 1)$.  

Next, compute the vector $\vec{BC}$:  
$$ \vec{BC} = C - B $$  
$$ x_C - x_B = -2 - 3 = -5 $$  
$$ y_C - y_B = 1 - (-4) = 5 $$  
$$ z_C - z_B = -1 - 1 = -2 $$  
So, $\vec{BC} = (-5, 5, -2)$.  

Now we use the dot product formula to find the angle $\theta$ between these two vectors:  
$$ \cos(\theta) = \frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|} $$  

First, calculate the dot product $\vec{BA} \cdot \vec{BC}$:  
$$ \vec{BA} \cdot \vec{BC} = (-2)(-5) + (-7)(5) + (1)(-2) $$  
$$ = 10 - 35 - 2 $$  
$$ = -27 $$  

Next, calculate the squared magnitudes $|\vec{BA}|^2$ and $|\vec{BC}|^2$:  
$$ |\vec{BA}|^2 = (-2)^2 + (-7)^2 + (1)^2 = 4 + 49 + 1 = 54 $$  
$$ |\vec{BC}|^2 = (-5)^2 + (5)^2 + (-2)^2 = 25 + 25 + 4 = 54 $$  

Finally, calculate the magnitude $|\vec{BA}|$ and $|\vec{BC}|$:  
$$ |\vec{BA}| = \sqrt{54} = 3\sqrt{6} $$  
$$ |\vec{BC}| = \sqrt{54} = 3\sqrt{6} $$  

Now, substitute these values into the cosine formula:  
$$ \cos(\theta) = \frac{-27}{(3\sqrt{6})(3\sqrt{6})} = \frac{-27}{9 \cdot 6} = \frac{-27}{54} = -0.5 $$  

Thus, $\theta = \arccos(-0.5)$.  
Since $\cos(\theta) = -1/2$, the angle is $120^\circ$ (which corresponds to $\theta$ being in the range $[0^\circ, 180^\circ]$).  

\boxed{120^\circ}  
