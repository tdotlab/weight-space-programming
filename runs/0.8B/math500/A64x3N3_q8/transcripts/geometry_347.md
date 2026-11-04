# test/geometry/347.json (Geometry, level 3)

> A triangle $\triangle ABC$ with $\angle A = 14^\circ$ is inscribed in a circle where $AB$ is a diameter. How many degrees are in $\angle B$?  

**Correct.** Gold `76^\circ`, predicted `76`. Finish: stop, 14502 tokens, 2 waits, 1572.4 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's my thought process for solving this geometry problem:  

1.  **Analyze the Request:**  
    *   **Given:** A triangle $\triangle ABC$.  
    *   **Condition 1:** $AB$ is a diameter of the circle on which $\triangle ABC$ is inscribed.  
    *   **Condition 2:** $\angle A = 14^\circ$ (This refers to the vertex angle at vertex $A$).  
    *   **Goal:** Find the measure of $\angle B$ in degrees.  

2.  **Recall Relevant Geometric Theorems:**  
    *   *Angle in a semicircle theorem:* If an angle of a triangle is inscribed in a semicircle, that angle subtends the arc and equals $90^\circ$ if it's a right angle. Here we are given $AB$ is diameter. So $\angle C$ (the angle at vertex $C$, opposite to $Diameter AB$) must be $90^\circ$.  
        *   *Correction/Refinement:* Let's look closer. $\triangle ABC$ is inscribed in a circle with $AB$ as the diameter. The vertices are on the circle. The segment connecting the endpoints of the diameter is the hypotenuse of any right-angled triangle formed by chords connecting the endpoints of the diameter. If an angle $\angle C$ subtends the diameter $AB$, then $\angle C = 90^\circ$.  
        *   *Check:* Is this a valid interpretation? The problem states "A triangle... inscribed in a circle where $AB$ is a diameter." Usually, "inscribed in a circle" means all vertices lie on the circle. If $AB$ is the diameter, the angle subtended by $AB$ at any point on the arc (not containing the center or endpoints) would be something else, but specifically, $\angle ACB$ subtends the diameter $AB$. Yes, this theorem holds: An angle inscribed in a semicircle is a right angle. Therefore, $\angle C = 90^\circ$.  

    *   *Sum of angles in a triangle:* The sum of interior angles is always $180^\circ$.  
    *   Let the vertices be $A$, $B$, and $C$.  
    *   We have $\angle A = \angle CAB = 14^\circ$.  
    *   We know $\angle C = \angle ACB = 90^\circ$ (because $AB$ is the diameter of the circumcircle).  

3.  **Step-by-Step Calculation:**  
    *   Let the measure of angle $\angle B$ be denoted as $\beta$.  
    *   The sum of angles in $\triangle ABC$ is: $\angle A + \angle B + \angle C = 180^\circ$.  
    *   Substitute the known values: $14^\circ + \angle B + 90^\circ = 180^\circ$.  
    *   Rearrange to solve for $\angle B$:  
$\angle B + 104^\circ = 180^\circ$  
$\angle B = 180^\circ - 104^\circ$  
$\angle B = 76^\circ$.  

4.  **Verification:**  
    *   If $AB$ is the diameter, then $\angle C = 90^\circ$.  
    *   The triangle has a right angle at $C$.  
    *   The vertex angle at $A$ is given as $14^\circ$.  
    *   Therefore, the remaining angles are $\angle B$ and $\angle A$.  
    *   Sum of these two must be $180^\circ - 90^\circ = 90^\circ$.  
    *   Since $\angle A = 14^\circ$, then $\angle B + \angle A = 90^\circ$ is incorrect because it implies $\angle B + 14^\circ = 90^\circ$.  
    *   Let's check the angle addition: $\angle A + \angle B + \angle C = 180^\circ$.  
    *   $14^\circ + \angle B + 90^\circ = 180^\circ$  
    *   $104^\circ + \angle B = 180^\circ$  
    *   $\angle B = 180^\circ - 104^\circ$  
    *   $\angle B = 76^\circ$.  

5.  **Is there any ambiguity?**  
    *   Does the problem imply $A, B, C$ are in a specific order? Usually, for triangles, vertex labels define positions.  
    *   Is "inscribed" referring to vertices on the circle? Yes, standard convention.  
    *   Is it possible that $\angle A = 14^\circ$ is not the angle at $A$? The problem says "where $\angle A = 14^\circ$". By definition of a vertex in a triangle labeled $ABC$, this refers to $\angle CAB$.  
    *   So, $\angle CAB = 14^\circ$.  
    *   Since $AB$ is the diameter, the angle subtended by it at the circumference is right. This means $\angle ACB = 90^\circ$? No. The angle *at* the circumference is formed by chords connecting vertices to endpoints of the arc. If we take the endpoints of the diameter $A$ and $B$, the angle at a point $C$ on the circle subtended by them (which are opposite points) is a right angle ($90^\circ$). Is this true? Yes, any angle inscribed in a semicircle is a right angle.  
    *   So $\angle ACB = 90^\circ$.  
    *   We know the sum of angles: $14^\circ + \angle B + 90^\circ = 180^\circ$.  
    *   So $\angle A + \angle B = 90^\circ$ is not correct because it assumes a specific relationship like an isosceles triangle or similar.  
    *   Let's double check the logic.  
        *   Angle at $C$ (opposite diameter $AB$) is right angle?  
        *   Consider points $A, B$ as endpoints of the diameter. The circle passes through $A$ and $B$. Any other point on the circle defines an inscribed angle $\alpha$. If that point is not $C$, say it is $D$. Then $\angle ADB = 90^\circ$.  
        *   Let's re-evaluate. Is $\angle C$ subtended by the diameter?  
        *   The vertices are $A, B, C$. $AB$ is a chord (diameter). $C$ is on the circle.  
        *   Does angle at $C$ (which corresponds to $\angle ACB$) subtend the diameter?  
        *   Yes, if we connect points $A$ and $B$, then for any point $P$ on the circumference other than $A$ and $B$, $\angle APB$ is half the arc measure subtended by $AB$. Since $AB$ is a diameter, the arc $AB$ (the semicircle) is $180^\circ$.  
        *   The inscribed angle theorem states that an angle $\angle APC$ inscribed in the circle is equal to half the intercepted arc.  
        *   The angle $\angle ACB$ intercepts the arc $AB$ which is $180^\circ$. Thus $\angle ACB = \frac{1}{2}(360) = 90^\circ$. No, that logic applies if we look at the "intercepted" arc. The intercepted arc is the one *inside* the angle.  
        *   Let's be precise. Let circle be $S$. Points on $S$ are $A$ and $B$. $C$ is a point on $S$. $\angle ACB$ is an inscribed angle. The chord connecting endpoints of the diameter is $AB$.  
        *   If we consider the circle, then $AB$ is a diameter. The angle at any other point on the circumference (on the opposite side) formed by chord $AB$ must be $90^\circ$.  
        *   Since vertices are $\triangle ABC$, the angles are $\angle A = \angle CAB$, $\angle B = \angle CBA$, $\angle C = \angle BCA$.  
        *   Given $\angle CAB = 14^\circ$.  
        *   We need to find $\angle ACB$.  
        *   $AB$ is the diameter. Therefore, $\angle ACB = 90^\circ$ is correct. This is a standard result: The angle subtended by a diameter in a semicircle is a right angle. Here, vertices $A, B, C$ are on the circle with diameter $AB$. Thus $\angle ACB$ is an angle inscribed in a semicircle?  
        *   Yes, vertices are on the circle, chord $AB$ is part of it. $C$ is the vertex. So $\angle ACB$ subtends the arc $AB$. Since $AB$ is a diameter, the arc $AB$ is a semi-circle ($180^\circ$). The inscribed angle subtending a semi-circle is a right angle.  
        *   Therefore $\angle C = 90^\circ$.  
    *   This logic holds up perfectly.  

6.  **Calculation Review:**  
    *   Triangle Angles: $\angle A + \angle B + \angle C = 180^\circ$.  
    *   Given $\angle A = 14^\circ$.  
    *   Calculated $\angle C = 90^\circ$ (Right Angle).  
    *   Substitute into equation: $14^\circ + \angle B + 90^\circ = 180^\circ$.  
    *   $\angle B = 180^\circ - 104^\circ$.  
    *   $\angle B = 76^\circ$.  

7.  **Alternative Interpretation Check:**  
    *   Could the problem mean something else by "inscribed in a circle"?  
    *   Is it possible $AB$ is not the chord connecting endpoints, but just a segment? Yes, a diameter is a line segment passing through the center. In geometry problems, "triangle inscribed in a circle" usually refers to vertices on the circumcircle, and $AB$ being a diameter implies $A, B$ are opposite ends of the diameter.  
    *   So the setup is: $\angle A = 14^\circ$. $AB$ is diameter. $\angle C = 90^\circ$. Then $\angle B = 76^\circ$.  

8.  **Double check:** Is it possible to interpret "AB is a diameter" differently?  
    *   If $A, B$ are endpoints of the diameter, then $\angle ACB = 90^\circ$.  
    *   What if $C$ lies on the extension of the arc? Still, the inscribed angle subtended by $AB$ is right.  
    *   Let's consider vertices order: Usually cyclic triangle implies $A-B-C-A$ around the circle.  
    *   If $\angle A = 14^\circ$, and $\angle C = 90^\circ$, then $\angle B = 180 - (14+90) = 76^\circ$.  

    *   Could there be another interpretation? For example, is the "triangle" defined by sides $AB$ and something else?  
        *   "A triangle $\triangle ABC$ with $\angle A = 14^\circ$"  
        *   "$\angle B$" refers to angle at vertex $B$.  
    *   The question is straightforward.  

9.  **Structure the Answer:**  
    *   State the theorem: An inscribed angle in a semicircle is a right angle.  
    *   Identify that since $AB$ is a diameter, $\angle C = 90^\circ$. (Or better say, vertices lie on circle with diameter AB).  
    *   Sum the angles of triangle ABC: $\angle A + \angle B + \angle C = 180^\circ$.  
    *   Substitute knowns: $14^\circ + \angle B + 90^\circ = 180^\circ$.  
    *   Solve for $\angle B$.  
    *   Final result.  

10. **Refining the explanation:**  
    *   The prompt asks to put final answer in `\boxed{}`.  
    *   Reasoning steps must be clear.  
    *   Step 1: Identify that $AB$ being a diameter means $\angle ACB = 90^\circ$. Explain why (Thm: Angle in semicircle). Or simpler logic: In the circumcircle of triangle $ABC$, the angle subtended by chord $AB$ is $\angle ACB$. Since $AB$ is diameter, arc $AB$ is a semi-circle, hence inscribed angle is right.  
    *   Step 2: Use sum of angles property. $14 + B + 90 = 180$.  
    *   Step 3: $B = 76^\circ$.  

    *   Is there any trap? Like the vertices are ordered on the circle differently?  
        *   $\angle A$ is angle at vertex A. Sides are $BA$ and $CA$.  
        *   Side $BC$ connects B and C.  
        *   $AB$ is diameter. So arc $ABC$ contains the whole semi-circle. Arc $ACB$ has length 180 degrees? Or arc AB has length 180?  
        *   Let's visualize. Circle center O. A at (-R, 0). B at (R, 0). C on circle somewhere.  
        *   $\angle C = \angle BCA$. This is inscribed angle intercepting arc AB. Since chord endpoints A and B are diameter ends, the intercepted arc is 180 degrees (the semi-circle not containing C? Or containing C?).  
        *   The inscribed angle theorem: Angle subtended by an arc at the circumference is half the measure of that arc.  
        *   Here, angle $\angle ACB$ subtends the arc $AB$ *not* containing $C$.  
        *   Since $A$ and $B$ are opposite endpoints of a diameter, the arc $AB$ (the long one) is 180 degrees? Or is it just defined by points?  
        *   If vertices lie on circle in order A, B, C: The angle $\angle ACB$ subtends the arc $AB$. If $A$ and $B$ are endpoints of diameter, then the minor or major arc is 180. Any inscribed angle subtending the semi-circle (which spans from A to B) is a right angle?  
        *   Let's check: Arc $ACB = 180^\circ$. Angle $\angle ACB$ intercepts the segment $AB$ which is the diameter?  
        *   The chord connecting opposite endpoints of a diameter is a diameter itself.  
        *   Inscribed angle theorem says $\alpha$ subtends arc $XY$. If $X=A, Y=B$, then arc $AB$ is 180 degrees. So $\angle ACB = 90^\circ$. Correct.  
    *   Let's check arc measures again. Arc AB (minor or major) can be considered as a semicircle because $A$ and $B$ are diameter endpoints. The angle at circumference subtended by the diameter is right angle.  
        *   Does this mean $\angle C = 90^\circ$? Yes.  

    *   Are there any other cases?  
        *   What if the order of points on circle is not $A, B, C$ but some permutation? The name of triangle implies standard labeling around the interior vertices. Usually, for a specific triangle shape, $\angle A$, $\angle B$, and $\angle C$ refer to the internal angles opposite sides $c, b, a$.  
        *   So $\angle B$ is at vertex $B$, opposite side $AC$.  
        *   We know $AB$ is diameter. This makes triangle $ABC$ right-angled?  
        *   Let's check if any other interpretation exists for "$\angle B$". Usually, angles are at the vertices.  
    *   The logic seems robust. The sum of angles in a triangle is constant ($180^\circ$). The only variable here is angle $\angle C$. Since $AB$ is diameter, $\angle C = 90^\circ$.  

    *   Final check:  
$14 + \angle B + 90 = 180$  
$\angle B = 76$.  

    *   Let's quickly check if there are other constraints or misinterpretations of "inscribed in a circle where AB is a diameter".  
        *   Maybe the triangle is $ABC$, and we know $\angle C=90^\circ$ but maybe vertices order?  
If vertices are A, B, C.  
If $AB$ is diameter. $\angle C = 90^\circ$ implies $\angle ACB$ (angle at C). This requires $C$ to be on the semicircle.  
Then in a right triangle, hypotenuse is side opposite right angle. Side opposite $\angle C$ is $AC$. Side adjacent $\angle A$ is $AC$.  
If $AC = BC$, then it's equilateral. But here we are given $\angle A = 14^\circ$. If $\triangle ABC$ is right angled at $C$, and $\angle A = 14^\circ$, then $\angle B = 76^\circ$.  
Then side $AC$ would be hypotenuse of right triangle $ABC$?  
Yes. Since $\angle C=90$, $AB$ is the hypotenuse.  
So, $AB$ is the diameter. The hypotenuse is a chord in a semicircle. This is consistent with $AB$ being a diameter.  
However, we need to verify the condition: Does $A, B, C$ lie on circle such that $\angle A = 14^\circ$, $AB$ is diameter? Yes.  
In this case, $\angle C = 90^\circ$.  
Then sum of angles: $14 + \angle B + 90 = 180$.  
Therefore $\angle B = 76$.  

    *   Is it possible that $C$ lies on the other side of $AB$?  
If $A, B$ are fixed endpoints of diameter. $C$ is somewhere on the circle. The triangle is formed by these points.  
Angle at vertex $B$: $\angle ABC$. This subtends arc $AC$.  
Angle at vertex $A$: $\angle BAC = 14^\circ$. This subtends arc $BC$.  
If we use inscribed angles subtended by arcs:  
Angle at A (in the circle, not in triangle) would be half of arc BC.  
Angle at B (in the circle) is half of arc AC?  
Let's check. $\angle ABC$ subtends arc $AC$.  
Since $\angle B = 90^\circ$ is a common misconception (or confusion with other theorems), I must be careful not to use that.  
Here, we need $\angle BAC + \angle ABC + \angle BCA = 180^\circ$.  
Given $AB$ is diameter. This implies $\angle ACB = 90^\circ$.  
Therefore, sum is $14 + \angle B + 90 = 180$, so $\angle B = 76^\circ$.  

    *   Let's check the case where $\angle C = 90^\circ$ isn't true.  
Why would it not be true? Only if the vertices aren't $A, B, C$ in that specific order on a semicircle. But for "inscribed", they must be on the circle. If $AB$ is diameter, then $C$ cannot lie on the minor arc $AB$. $C$ can only be on the major arc $AB$.  
The inscribed angle theorem holds for any point on the major arc $AB$.  
Any point $C$ on the semicircle (arc $AB$) yields $\angle ACB = 90^\circ$.  
Since $A, B, C$ are distinct vertices of a triangle (implied), $C$ is just one vertex. So $\triangle ABC$ is right-angled at $C$.  

    *   Therefore, the calculation is solid.  

    *   Double check: What if $C$ is on the minor arc? Then $\angle ACB = 180 - 90 = 90$?  
The inscribed angle subtends the major arc or the chord?  
If a point is on the arc not containing the diameter, it's on the other side of the semicircle.  
Let the circle be $x^2 + y^2 = r^2$. Let A at (-1, 0). B at (1, 0). C at some $(x, y)$.  
Angle at C is angle between lines CA and CB?  
Line CA connects (-1, 0) to $(x, y)$. Slope $m_1 = (y - 0)/(x + 1)$.  
Line CB connects (1, 0) to $(x, y)$. Slope $m_2 = (y - 0)/(x - 1)$.  
Tangent at C. Angle between chords?  
Let's just use the property: $\angle ACB$ subtends arc $AB$. Since arc $AB$ is a diameter ($180^\circ$), angle is 90.  
Is it possible to have $\angle ACB = 180 - 90$?  
This would be if C was on the minor arc AB, which would mean C and A are "opposite" in the sense of angle subtraction, but for inscribed angles, you just take the angle inside the triangle. The vertices must be distinct. If C is on the other side (which it isn't by definition of triangle shape), then the angle subtended is different?  
Let's visualize. Circle with diameter 1 to 2. Center at origin. C is a point. Angle ACB.  
If C is on upper semicircle ($y > 0$), angle ACB is inscribed in the semi-circle. The intercepted arc is the major one (or the whole circle if it goes over)?  
No, for $\angle ACB$, the points $A$ and $B$ are endpoints of a chord. If $C$ is on the circle, then the locus of the vertex lies on the circumcircle. The angle $\angle C$ depends on the arc subtended by $AB$.  
Since $A$ and $B$ are endpoints of diameter, arc $AB$ (not containing any point other than the center or vertices) corresponds to a half circle.  
For any point $C$ not on the segment connecting $A$ and $B$, does $\angle ACB = 90^\circ$?  
Let's check: If $C$ lies on the major arc $AB$, then angle is inscribed angle theorem says it equals 1/2 of semi arc. That means $90$.  
What if $C$ lies on the minor arc? Then the "angle" inside the triangle is defined differently. But for a convex polygon like triangle, vertices are usually distinct points in order around the circle.  
If vertices are labeled $\triangle ABC$, then the triangle is formed by lines connecting these points. The vertices on the circumcircle are ordered angularly. Usually this implies the minor arc $AB$ or semicircle logic applies to the specific configuration.  
Since it's a "triangle" inscribed, the angle at C is defined as $\angle ACB$.  
For any point $C$ on the circle such that $C \neq A$ and $C \neq B$, the arc $AB$ subtended by $\angle C$? The theorem says angle = half arc. Since diameter defines arc measure 180.  
If $\angle ACB$ is inscribed, it subtends arc $AB$ not containing $C$.  
If we assume standard naming convention where vertices go around the perimeter.  
Say we go $A \to B \to C$ along the circle?  
Then angle at $C$ subtends arc $AB$? Or does it subtend the other arc?  
Usually inscribed angles subtended by sides of triangle have specific values based on geometry.  
In any case, the most standard interpretation is that $\triangle ABC$ is inscribed in a semicircle with diameter $AB$, meaning $C$ lies on one side of the line perpendicular to $AB$?  
The property "angle in semicircle is 90 degrees" implies that if you connect endpoints of diameter, and any point on arc, you get a right angle. This works for any vertex.  
So $\angle C = 90^\circ$.  
Thus $14 + B + 90 = 180 \implies B = 76^\circ$.  

    *   Let's check if $\angle A$ is subtended by arc $BC$.  
    *   If $AB$ is diameter, then $\angle C = 90^\circ$ implies $AC^2 + BC^2 = AB^2$?  
In a circle with chord $c$, if it forms a triangle inscribed. $AB$ diameter implies $C$ makes $C$ lie on the arc. Since it's a right triangle, the vertices satisfy $\angle C = 90^\circ$.  
This is consistent with the "Pythagorean theorem in the circle" (if we think of it as a right triangle inscribed in a semi-circle).  
So $B=76^\circ$ is derived from sum of angles.  

    *   Is there any geometric configuration where $\angle A \neq 14$ but sum holds?  
The question asks for the angle given $\angle A = 14$. It implies that this is a specific condition to be solved, likely leading to a unique solution.  
With $A=14$, $C=90$ fixed.  

    *   Could there be an issue with "triangle $\triangle ABC$"?  
Maybe the order of vertices? If $AB$ is diameter. The triangle has angles $A, B, C$.  
$\angle A = \angle CAB$. Given 14.  
We need $\angle B = \angle CBA$.  
The sum is $C + A + B = 180$.  
Is it possible that $\angle B$ refers to something else? Unlikely.  
So I'm confident in the result.  

    *   Let's double check if "AB is a diameter" implies $\triangle ABC$ has hypotenuse AB?  
In a right triangle inscribed in a circle with hypotenuse $c$, the hypotenuse subtends a semicircle. The angle opposite it, which is the angle at the circumference, is 90 degrees.  
If we have a triangle $ABC$ on a circle with diameter $AB$.  
Then $\angle C$ (or rather vertex angle $C$, usually referring to $\angle BCA$) is subtended by chord $AB$. Since $AB$ is diameter, the arc $AB$ is semicircle. The angle inscribed subtending a semicircle is 90 degrees. So $\angle ACB = 90^\circ$.  
This confirms my logic again.  

    *   Let's re-read carefully: "A triangle ABC with $\angle A = 14^\circ$ is inscribed in a circle where AB is a diameter."  
Does this mean the angle at vertex $A$ (interior of triangle, usually denoted as $\angle A$ or $\angle CAB$) is given as $14^\circ$?  
Yes, standard notation.  
"AB is a diameter" implies $C$ lies on the circle such that $ACB$ is a valid inscribed angle configuration.  
So $C=90^\circ$.  
Sum of angles = 180.  
$\angle B = 76^\circ$.  

    *   Let's think if there are other possibilities. Could it be that the triangle is acute?  
If $\angle A = 14$, $\angle C = 90$ (impossible for a triangle where two angles sum to 90 and one is 14). $90+14=104 \neq 180$. So it is not obtuse.  
Is it equilateral? If $A=B=C=36$? Then $\angle A = \angle B$. But $\angle C = 90$. This would mean triangle has a right angle, so equilateral is impossible ($36+36+36=108$ vs 180).  
So it's a right triangle.  

    *   Is there any trick with the "inscribed in a circle" phrasing?  
Sometimes "triangle inscribed in a circle where AB is a diameter" might imply that $C$ lies on the extension of something or the vertices are ordered such that angle A doesn't subtend the diameter?  
Usually, if you say "Triangle ABC is inscribed in circle with diameter AB", it implies $\angle C = 90^\circ$.  
But what if the order is different? If $A$ and $B$ are endpoints of diameter, but $C$ is not on the semicircle containing $AB$?  
The problem says "inscribed in a circle". Vertices on the boundary.  
If vertices are ordered around the circle as A, B, C...  
Then arc AB is 180 degrees.  
Angle $\angle C = \angle ACB$ subtends arc $AB$. Measure is 90.  
Angle $\angle A$ subtends arc $BC$.  
Angle $\angle B$ subtends arc $AC$.  
If $A=14$, then $B + C = 166$?  
$C=90 \implies B+90=166 \implies B=76$.  
If the order was different, say A-B-C...  
Does "AB is a diameter" imply arc AB is semicircle? Yes.  
So $B$ subtends the remaining part of the circle (arc AC).  
Arc $AC + Arc BC = 360 - 180 = 180$.  
This assumes arc AC and arc BC partition the circle? Or are they the same side?  
If vertices are in order A, B, C...  
Then $\angle C$ subtends arc AB. Since AB is diameter, angle is 90.  
$\angle A$ subtends arc $BC$. Arc $BC = 360 - 2\theta_C$?  
Let's check arcs again.  
Circle total 360.  
Chord AB is the diameter. It divides circle into two semi-circles.  
The inscribed angle $\angle ACB$ subtends arc AB (minor or major).  
If C is on the "major" arc, then angle subtended by chord AB is 90?  
Let's visualize. A at 9 o'clock. B at 3 o'clock.  
C could be at 12 o'clock (top of circle).  
Then $\angle ACB$ (intercepted by A and B, not containing C) subtends the arc from A to B through...  
If C is top point, it's on the arc from B back to A via center?  
Arc AB via Top? That is semi-circle. Yes. Angle at C is right angle.  
What if C is somewhere else? Say 4 o'clock (lower half).  
Then $\angle ACB$ intercepts the arc from A to B going through...  
If C is on the circle, and A, B are endpoints of diameter.  
The angle subtended by AB at any point $P$ on the major arc is right.  
The inscribed angle theorem applies to vertices of a triangle inscribed in a circle.  
Since it's a triangle ABC, and $AB$ is diameter.  
So $\angle ACB = 90^\circ$. This must hold for any configuration where $C$ lies on the circumference such that $A, B$ are distinct from $C$. If $C$ was outside (not possible since it's inscribed), or if the vertices were arranged differently. But standard problem interpretation implies convex hull of points.  
So $\angle C = 90^\circ$ is safe.  

    *   Is there a case where $\angle A = \angle ABC$?  
Then $C=14$. But then $B$ and $A$ must be on same side of $C$ or something?  
If $C$ is between $A$ and $B$, then arc $AB$ (the one containing C) would not be a semicircle unless it spans the whole circle.  
Let's draw standard diagram. Circle center O. Diameter AB horizontal.  
Points A, B on circle.  
Point C lies on the upper or lower part of circle.  
Case 1: C is on upper arc AB (semicircle). Then $\angle ACB = 90^\circ$. Angle $\angle CAB$ subtends arc CB.  
Angle $\angle ABC$ subtends arc CA.  
We know $\angle CAB = 14^\circ$.  
The angle subtended by diameter at the circumference is 90.  
This angle is at vertex C (or B, or A depending on placement).  
Let's check vertex assignment.  
Triangle has vertices $A$, $B$, $C$. Angle $\angle A = 14^\circ$. Angle $\angle B$? Angle $\angle C$?  
The problem gives $\angle A = 14^\circ$. It says "how many degrees in $\angle B$".  
This implies finding the angle at vertex $B$.  
In a right triangle, sum of angles is 180.  
If $\triangle ABC$ is right-angled at $C$, then $A+B+C = 90 + A + 90 = 180+A \implies B=90-A$.  
With $A=14$, $B=76$.  

    *   What if the triangle was right angled at $A$?  
Then $\angle C = 90^\circ$ is wrong.  
If $\triangle ABC$ has $\angle A = 14^\circ$. If it was inscribed in a circle where $AB$ was diameter...  
This implies $\angle C$ (vertex angle) subtends the diameter $AB$. Since $C$ is on the circle, the angle $\angle C$ formed by $AC$ and $BC$ must be 90 degrees.  
Why? Because the chord connecting endpoints of the diameter subtends an angle at circumference equal to half the central angle ($180^\circ$) or it's just a property of circles that $\angle ACB = 90^\circ$.  
This is the most standard interpretation.  

    *   Is there any ambiguity about the angle name? "in $\angle B$" might mean measure $x$.  
    *   Let's check if the problem meant $\triangle ABC$ where $\angle A, \angle C, \angle B$ are given or something else.  
"A triangle ABC with $\angle A = 14^\circ$ is inscribed in a circle where AB is a diameter."  
It does not say $\angle C=90$. It says $\angle A=14$.  
If we use the property that for $AB$ diameter, $\angle ACB$ (at $C$) is 90.  
Then $\angle B = 76^\circ$.  

    *   Is there any interpretation where $\angle B$ is not an angle of the triangle but just a number in degrees?  
"How many degrees are in $\angle B$?" - clearly asking for angle measure.  

    *   Could it be that $A, B, C$ are ordered such that $AB$ is diameter, but vertices order is $B, A, C$ or something?  
If the triangle inscribed in a circle has AB as a diameter. Then vertices must lie on the circumcircle.  
If $\angle CAB = 14$, then $\angle C = \angle ACB$.  
For this to form a valid triangle where $AB$ is a diameter, $C$ must be such that $AB$ subtends a semicircle? Or $ACB$ is a right triangle.  
If it's not specified which angle is 90, then the theorem $\angle ACB = 90^\circ$ implies that vertex C is on the semicircle opposite to diameter AB.  
Since $C$ must be distinct from $A$ and $B$, this works.  
The only ambiguity is whether "AB is a diameter" forces a right angle at $C$ or not? It always does for any point $C$ not collinear with A and B on the circle.  

    *   Let's check if $\angle C$ could be something else.  
If we assume $\triangle ABC$ is general.  
The vertices are $A, B, C$.  
Is it possible that $\angle C$ (i.e. $\angle BCA$) subtends a different arc than $\angle A$?  
Angle at vertex $C$ subtends arc $AB$. Since $AB$ is diameter, arc $AB = 180^\circ$.  
Therefore inscribed angle at circumference $\angle ACB$ (assuming C is on the circle not containing the midpoint of chord AB) is $1/2 * 180 = 90$.  
This seems the only logical path.  

    *   Let's check if there's any tricky case like "AB is a diameter" implies $\angle C = 180$?  
If A, B, C are collinear, it doesn't form a triangle (degenerate).  
Since $AB$ is a diameter, the circle goes through A and B. The triangle inscribed must be non-degenerate.  

    *   So, $\angle ACB = 90^\circ$.  
    *   Sum of angles: $14 + \angle B + 90 = 180$.  
    *   $\angle B = 76^\circ$.  

    *   One check on the "degree" notation. The question asks for degrees. So final answer should be integer.  
    *   Is it possible that the angle $\angle A$ is an angle at vertex A? Yes, $\angle CAB$.  
    *   Does $\angle A$ being 14 mean $\angle CAB = 14$? Or something else? "In a triangle... where AB is diameter". Standard.  

    *   Let's verify the sum of angles again.  
Triangle vertices $A, B, C$.  
Side lengths are $c, b, a$. $a = BC, b=AC, c=AB$.  
Hypotenuse $a$ or hypotenuse $b$?  
Since $\angle C = 90^\circ$, side opposite is AB. So $AB$ is the hypotenuse.  
This means $AB^2 = AC^2 + BC^2$.  
In a right triangle inscribed in a circle (with diameter), yes, hypotenuse is diameter.  
The angle $\angle A$ is $\angle CAB$. It subtends arc $BC$.  
Angle $\angle B$ is $\angle ABC$. It subtends arc $AC$.  
Arc $AB = 180^\circ$.  
So measure of arc $BC + \text{measure}(arc AC) = 180^\circ$?  
Yes, the full circle has points $A, B, C$.  
Arc $ABC$ (from A to B via C and center?)  
The arc subtended by angle $\angle A$ is arc $BC$.  
Angle $\angle B$ is subtended by arc $AC$.  
If we know $\angle A = 14^\circ$, then measure of arc $BC = 2 \times 14^\circ = 28^\circ$.  
Since total circumference is 360, and arc $AB$ (diameter endpoints) corresponds to a semicircle ($180^\circ$).  
So arc $BC + \text{arc } AC$ should sum to arc $AB$? Or arc $AC$ + arc $CB = 28^\circ$.  
Is this correct?  
Angle at A is subtended by arc BC. Angle at B is subtended by arc AC.  
Sum of arcs = 360 - arc AB (since C is on circle).  
If $C$ is between $B$ and $A$ angularly?  
Or $C$ is opposite to A?  
Let's draw circle. Point A at top, B at bottom (diameter). C is somewhere.  
Angle $\angle A = 14^\circ$ subtends arc BC. So arc BC corresponds to angle 28 degrees.  
Then total angle $\angle C$ (at $C$, inscribed angle) subtends arc $AB$. Since $AB$ is diameter, this is the semicircle. Angle is 90.  
Does the sum of angles in triangle equal 180?  
The vertices are on the circle.  
The sum of central angles for arcs $\angle A + \angle B + \angle C = 360$.  
This is only valid if we are talking about full rotation.  
In the circle, vertices $A, B, C$ form a triangle. The arc between A and B (the one NOT containing C) is $180^\circ$.  
Arc between A and C and Arc between B and C must sum to 360 - 180 = 180?  
Yes. Arc AC + Arc BC = 180? Or maybe just Arc AC + Arc CB = arc ABC?  
If vertices are ordered around the circle as A, B, C (counterclockwise).  
Then $\angle A$ subtends arc $BC$. Measure of arc $BC$ is not 28. Arc $BC$ is part of the semicircle defined by diameter AB.  
Let's check if Arc BC + Arc AC = Arc AB.  
If order is A, B, C. Then Arc BC connects B to C?  
If we denote vertices as vectors on circle: $\vec{A}, \vec{B}, \vec{C}$.  
$\angle A$ corresponds to vertex $A$, sides $AB$ and $AC$. It subtends arc $BC$.  
$\angle B$ corresponds to vertex $B$, sides $BA$ and $BC$. It subtends arc $AC$.  
$\angle C$ corresponds to vertex $C$, sides $CA$ and $CB$. It subtends arc $AB$.  
The sum of angles in a triangle inscribed in circle is not just related to sum of arcs.  
For the circumcircle, the sum of arcs intercepted by an angle at the center (or vertices).  
In circle geometry: $\angle A + \angle B + \angle C$?  
This doesn't have a fixed sum equal to 360 degrees for the arcs unless we talk about full circle.  
Here, the triangle angles $\angle A, \angle B, \angle C$ are inscribed angles.  
The angle at vertex $A$ intercepts arc $BC$.  
The angle at vertex $B$ intercepts arc $AC$.  
The angle at vertex $C$ intercepts arc $AB$.  
We know the measure of the intercepted arc for $\angle B$ is half the angle of arc? Or inscribed angle?  
Inscribed angles subtend arcs. So $\angle A = \frac{1}{2} m(arc BC)$. $\angle B = \frac{1}{2} m(arc AC)$. $\angle C = \frac{1}{2} m(arc AB)$.  
Since $AB$ is a diameter, arc $AB$ (minor or major?) corresponds to half circle.  
So $m(arc AB)$ must be 180 degrees? Or does it subtend 90 degrees at center?  
Inscribed angle theorem: $\angle ACB = \frac{1}{2} m(arc AB)$.  
So if $\angle C = 90^\circ$, then $arc AB$ (the one not containing C) is 180.  
This means arc $AB$ is a semi-circle. This implies vertices A and B are endpoints of diameter.  
Thus the triangle inscribed is formed by A, B, C on the circle. Since $\angle C = 90^\circ$, this fits perfectly.  
So $m(arc AB)$ (the one not containing C) must be 180 degrees?  
Or does it subtend the semicircle?  
If $\angle ACB = 90^\circ$, it means chord $AB$ is the diameter.  
Yes, this implies $A$ and $B$ are endpoints of a diameter.  
And since $\triangle ABC$ is inscribed in circle with these points, the vertices must be on the semicircle arc $AB$.  
Let's say the arc is $ACB$. Then angle at C is $90^\circ$.  
Then sum of angles: $\angle A + \angle B + 90 = 180$.  
So $\angle B = 76^\circ$.  

    *   The only potential confusion is if "AB is a diameter" means something else, like AB is tangent? Or chord connecting specific points?  
"A triangle ABC inscribed in a circle where AB is a diameter." - Unambiguous.  
So the logic holds.  

    *   Are there any counter-intuitive interpretations?  
What if $AB$ is not the hypotenuse?  
If $\angle C = 90$, then side opposite is AB, so AB is hypotenuse.  
Is it possible that angle at B is subtended by a different arc?  
Suppose A and B are endpoints of diameter. C is on circle.  
Then $\angle ACB$ (angle at C) intercepts the major arc AB if $C$ is between minor arc endpoints...  
But inscribed angles always sum to 90 with diameter subtended ones?  
Let's re-verify: In a circle, any angle $\theta$ inscribed in the semicircle is 90 degrees.  
Yes, that is a standard result.  
The only condition for this is that the points are not collinear. If $C$ lies on segment AB, then it's degenerate. Since C is on circle and AB is diameter (distinct), C cannot be on AB.  
So C forms a right angle.  

    *   Let's double check with another method: coordinates.  
Center O = (0,0). A = (-1, 0), B = (1, 0) (Diameter AB length 2).  
Circle passes through origin and (-1,0) and (1,0)?  
Equation of circle: $x^2 + y^2 = R^2$.  
Radius R = 1.  
Triangle ABC inscribed in circle with points A(-1,0), B(1,0).  
Let C be at $(x_c, y_c)$ on the unit circle.  
We need to find the angles.  
$\angle A$ is angle between chord $AB$ and $AC$.  
Vector $AB = (2, 0)$. This is along x-axis.  
Vector $AC = (x_c + 1, y_c)$.  
$\cos A = \frac{\vec{AC} \cdot \vec{AB}}{|\vec{AC}| |\vec{AB}|} = \frac{(x_c + 1)}{2}$.  
This is not correct for finding angle. Use dot product of vectors?  
Let's look at inscribed angles subtended by arcs.  
$m(arc AB) = 180^\circ$. (This corresponds to the central angle of a semicircle).  
The inscribed angle theorem states: Angle at circumference $\alpha$ subtends arc $BAC$? Or something.  
For vertex A, it subtends arc $BC$.  
Angle $C$ subtends arc $AB$. Since arc AB is 180 degrees (semicircle), $\angle C = 90^\circ$.  
This confirms $C=90^\circ$ without complex trig.  
Then for vertex B, it subtends arc $AC$.  
Arc $AC = 360 - m(arc BC) - m(arc AB)$?  
We don't know $m(arc AC}$ yet. But we can find sum of angles in the circle using inscribed angles sum:  
Angle $\angle A$ (subtending arc BC) + Angle $\angle B$ (subtending arc AC) + Angle $\angle C$ (subtending arc AB) = 180?  
Or is there a property that $\angle A + \angle B + \angle C$ isn't the same as arcs?  
Actually, inscribed angle $\angle C$ subtends arc $AB$. Since arc $AB$ is a semicircle (measure 180), inscribed angle is $180/2 = 90$.  
So if $\angle A=14$, then $\angle B + \angle C = 166$. And $\angle C=90 \implies \angle B=76$.  
This relies on arc AB measure being 180.  
Is it possible that arc AB is not semicircle?  
"AB is a diameter". Diameter implies length equals radius, passes through center. It divides the circle into two equal halves. The angle subtended at circumference by this diameter is always 90?  
Let's verify.  
Consider a point $C$ on the circle. If we connect $A$ and $B$. $AB$ is a chord.  
Angle $\angle ACB$ subtends arc $AB$.  
Does it mean the arc $AB$ is 180? Yes, if $AB$ is diameter. The minor arc is 180 (assuming C not on minor arc). If C were on major arc, angle would be smaller?  
Example: Arc AB = 240 degrees? But AB is a diameter.  
A point on the circle can only lie on either the arc from one end to other through center or just that line?  
The chord connects two points. The measure of the inscribed angle is half the measure of its intercepted arc.  
Since $A$ and $B$ are endpoints of a diameter, the minor arc $AB$ has measure 180 degrees? Or is it the major arc?  
Diameter divides circle into two arcs: semicircles. Each has measure 180 degrees.  
The inscribed angle $\angle ACB$ intercepts the segment connecting A and B?  
If C lies on one of the semi-circular sectors, say the upper half. It subtends arc AB.  
Is it intercepted by minor or major?  
Let's visualize.  
Circle center O. A at 9, B at 3.  
Angle $\angle ACB$ (where C is at 12).  
This angle intercepts the arc from C to A via... ?  
The intercepted arc for the angle subtended by the segment $AB$ inside the circle?  
Usually it's the arc NOT containing the vertex.  
Since C (12) is on major arc of A-B (which passes through 6, 4, etc)?  
Or does it matter if we are using "semicircle" or not?  
In my example:  
Points A(9), B(3). Arc AB = 60 degrees (minor). Major = 300.  
Inscribed angle at C on upper semicircle (12) intercepts the arc from A to B NOT containing C.  
From 12 to 9 via 15, 13...? Or from 3 to 180 via 6?  
In this configuration, C(12) is not between A and B on the same side of center. It's in the opposite quadrant.  
The angle subtended by the arc connecting A and B (going through C?) would be $180 - \angle ACB$ if C was in specific spot?  
Let's stick to the theorem: Inscribed angle subtending a diameter is 90 degrees.  
This statement holds regardless of minor or major arc, provided it subtends the semi-circle defined by the chord AB.  
If $AB$ is a diameter, then for any point $C$, the angle $\angle ACB$ subtended by this diameter is equal to... what?  
Consider points A(9) and B(3).  
Point C at 12 (North Pole). Angle $\angle ACB$.  
Chords connect A-C, B-C.  
The arc intercepted is the one on the circle opposite to vertex?  
Let's calculate angles explicitly using coordinates or geometry.  
Triangle inscribed in semicircle with diameter AB. The vertices $A, B$ are fixed. The arc $AB$ must be a specific arc. Since it's a diameter, the arcs between A and B are 180 degrees.  
If C is on this circle, then $\angle ACB = \frac{1}{2} (m(arc AB \text{ not containing } C))$.  
Arc AB (major) + Arc (minor)?  
Usually "inscribed in a semicircle" means the triangle lies inside the semi-circle. This implies $C$ is on one side of diameter line $AB$.  
However, if we just look at the circle geometry: The angle $\angle ACB$ subtends arc $AB$. Since A and B are endpoints of diameter, arc $AB$ (which spans the semi-circle) measures 180 degrees? Or is it something else?  
If we take the semi-circle of arc AB. This arc has measure 180 degrees.  
The angle $\angle ACB$ subtends the arc between A and B (the one not containing C).  
Since $AB$ are endpoints, this arc corresponds to the semicircle (measure 180) if we go from A to B "through" the center? Or is it just a chord?  
In any standard geometric setup for inscribed angles:  
Angle $\theta$ inscribed in circle with vertices on circumference.  
If side $AB$ is diameter, then angle at C must be 90.  
This property is universal for circles.  
So my assumption about "arc AB being semicircle" being the key is correct. The logic holds.  

    *   Is there any interpretation where $C$ could be anywhere such that $\angle B \neq 76$?  
If $AB$ diameter implies $ACB = 90$. This forces sum of angles to be $180$.  
Then $\angle B$ is determined by remaining angle.  
The problem asks for $\angle B$. It gives $\angle A = 14$. It must be a valid triangle.  
Is it possible that the question implies a non-triangular configuration? "A triangle". Implies existence of such triangle.  
The question asks for $\angle B$ degrees in a right triangle.  
Therefore, $B = 76^\circ$ seems to be the intended answer.  

    *   Just to be absolutely sure about "inscribed in a circle where AB is a diameter".  
Does it imply that A and B are opposite ends of the diameter? Yes.  
Is it possible that A and B are not opposite? If AB is a diameter, it's a line segment passing through center. So yes, they are opposite endpoints.  
Does this triangle imply $A$ and $B$ are vertices? Yes.  
So $\angle C = 90^\circ$.  
Sum $14 + \angle B + 90 = 180$.  
Result $76$.  

    *   Could the question be interpreted as: Triangle inscribed in circle, AB is diameter. Find angle at A (14) implies... maybe we should consider other interpretations of $\triangle ABC$?  
Usually, in a triangle inscribed in a circle with side $AB$, vertices $A, B$ are endpoints. The chord $AB$ defines the arc.  
If we draw it: Circle.  
Vertex A, B. Angle A = 14. Side AB is diameter.  
This means angle subtended by diameter at circumference is right angle?  
Yes. Let's check this step carefully.  
Imagine a circle. Draw chord $AB$. Place a point $C$ on the circle such that $\angle ACB = \theta$.  
The theorem states $\theta = 90^\circ$ if and only if arc $AB$ (not containing C) is a semicircle.  
This is true for any chord connecting opposite endpoints of diameter.  
So $\triangle ABC$ is inscribed in circle with AB as diameter. Then angle at $C$ is right angle.  
Since it's a triangle, vertices are distinct.  
Angle $A = 14^\circ$.  
The sum of angles in a triangle is 180 degrees.  
$\angle B + \angle A + \angle C = 180^\circ$.  
$\angle B + 14^\circ + 90^\circ = 180^\circ$.  
$\angle B = 76^\circ$.  

    *   What if the order of vertices on the circle is different? E.g. C-A-B or A-B-C?  
If vertices are labeled $A, B, C$ in that order.  
Usually triangle ABC means vertices are ordered around the perimeter.  
This matches standard conventions.  
Is it possible for A and B to be endpoints of diameter such that angle A is defined as $\angle CAB = 14^\circ$? Yes.  
If vertices are $A, B, C$, then angle $A$ is between $AC$ and $AB$.  
This subtends arc $BC$.  
Angle $C$ is between $CB$ and $CA$. This subtends arc $AB$.  
If $\angle A = 14^\circ$, then $m(arc BC) = 28^\circ$.  
Since $A, B$ are endpoints of diameter, arc $AB$ is 180.  
Then $C$ lies on the semicircle.  
The angle subtended by $ACB$ (the triangle's vertex C) subtends the arc $AB$?  
This would be $\angle ACB$ (in terms of inscribed angles, which is usually denoted as $\angle ACB$ or just $\angle B$ in other contexts? Usually $C$ is a vertex).  
Yes, vertex $C$ subtends arc $AB$.  
If arc $AB$ is 180, then angle is 90.  
So the configuration is fixed.  

    *   Let's check alternative: Could $\angle A = 14^\circ$ be a typo for $\angle C = 14$?  
The question asks "How many degrees are in $\angle B$?". If it meant $\angle C$, it would be $180 - (90+14) = 76$. It's the same result.  
What if $\angle A = 14^\circ$ is $\angle CAB$? Yes, we used that.  
Is there any ambiguity with angle at $B$? "in $\angle B$". This refers to vertex B.  

    *   Final sanity check.  
If $\angle A = 14$, then arc $BC$ is 28.  
Arc $AC$ + Arc $BC$ must sum to 180 (if C is on opposite semi-circle from AB? Or if order is A, B, C... then C is in the middle).  
Actually, arc $AB$ = 180. Arc $CB$ + Arc $BA$?  
If vertices are ordered A, B, C around the circle.  
Then $\angle A$ subtends arc BC (minor or major?). Assuming standard triangle shape, it subtends the arc $BC$ not containing A.  
Angle $\angle C$ subtends arc AB. This is 180 degrees? Or is it half of a larger arc?  
Since diameter connects A and B, the angle at any point on the circle on the *major* arc (containing the center?)...  
Theorem: Inscribed angles are equal if they subtend arcs of same measure.  
Theorem: Angle in semicircle is 90.  
If C is on major arc AB, then $\angle ACB = 90$.  
Then $\angle A + \angle B = 180 - 90 = 90$.  
This implies that $\angle A$ and $\angle B$ are acute or right?  
We found $A=14$ (acute), so $\angle B$ must be 76 (obtuse).  
So triangle is right-angled at $C$, angle A at $B$ is 76, angle C is 90.  
Is it possible that $\angle C = 90$ is wrong?  
If $AB$ is diameter. Then any point on circle (not on segment) forms a triangle.  
Does the angle at C subtend arc AB? Yes.  
Does arc AB correspond to the semicircle defined by diameter?  
Yes, because A and B are endpoints of diameter. The arc connecting them spans 180 degrees (the semi-circle).  
So the angle at C is indeed 90.  

    *   Conclusion: $\angle B = 76^\circ$.  


## Answer

To solve this problem, we can use the properties of angles inscribed in a circle and the theorem concerning right triangles formed by a diameter.  

1.  **Identify the Geometric Configuration:**  
We are given a triangle $\triangle ABC$ inscribed in a circle with vertices $A$, $B$, and $C$. The side $AB$ is specified as the diameter of the circle. This means that the segment connecting points $A$ and $B$ passes through the center of the circle and divides the semicircle defined by $AB$ into two equal parts, each measuring $180^\circ$.  

2.  **Apply the Angle Subtended by a Diameter Theorem:**  
The "Angle in a semicircle" theorem states that an angle inscribed in a semicircle is a right angle (equal to $90^\circ$). In this specific configuration, since the side $AB$ is the diameter of the circumcircle, the angle at vertex $C$ formed by the chords connecting $A$ and $B$ is the inscribed angle.  
Therefore, $\angle ACB = 90^\circ$.  

*Alternatively, we can verify this using properties of arcs:*  
The vertices $A$ and $B$ are endpoints of the diameter. Thus, the arc subtended by the chord $AB$ (the segment connecting them) is a semicircle, which measures $180^\circ$. An inscribed angle that subtends an arc of $180^\circ$ in a circle must be equal to half of that measure, or it's simply that any point on the circumference (where the triangle is placed) forming such a chord creates a right angle if we interpret $\angle C$ appropriately. But standard theorem applies: "An angle inscribed in a semicircle is $90^\circ$". Since vertices $A, B$ are on a circle and form a diameter arc with vertex $C$, the triangle is inscribed.  

*Correction/Refinement of Step 1:*  
If $\angle ACB = 90^\circ$, then the sum of angles in $\triangle ABC$ would be:  
$$ \angle A + \angle B + \angle C = 180^\circ $$  
Substituting the known value for $\angle C$:  
$$ 14^\circ + \angle B + 90^\circ = 180^\circ $$  
$$ 104^\circ + \angle B = 180^\circ $$  
$$ \angle B = 180^\circ - 104^\circ $$  
$$ \angle B = 76^\circ $$  

3.  **Confirm the Logic:**  
Given $\angle A = 14^\circ$. The problem states $\triangle ABC$ has $AB$ as diameter. This implies that vertex $C$ is located on the circle such that $\angle C = 90^\circ$. The sum of angles in a triangle is always $180^\circ$.  
$$ \angle A + \angle B + \angle C = 180^\circ $$  
$$ 14^\circ + \angle B + 90^\circ = 180^\circ $$  
$$ \angle B = 76^\circ $$  

The angle $B$ is $76^\circ$.  

\boxed{76}  
