# test/geometry/347.json, part 4 of 4

[Previous part](geometry_347_p3.md) · [Start](geometry_347.md)

*   Angle $\angle ACB$ intercepts the arc $AB$ (which corresponds to the arc NOT containing $C$).  
*   The measure of arc $AB$ depends on whether $C$ is on major or minor arc relative to chord $AB$.  
*   If $C$ lies on the major arc, then the arc $AB$ not containing $C$ is the minor arc. Its measure is 180. So inscribed angle $\angle ACB = \frac{1}{2} (180) = 90$.  
*   If $C$ lies on the minor arc (between A and B), then the arc not containing C is the major arc, which has measure 180. So inscribed angle $\angle ACB = \frac{1}{2} (180) = 90$.  
*   In both cases? The intercepted arc for inscribed angle is the one opposite the vertex. If $AB$ are endpoints and $C$ is on circle, the intercepted arc must be the one connecting A to B passing through...  
*   Let's rephrase: Inscribed Angle $\alpha$. Arc it intercepts is $\beta$. $\alpha = \beta / 2$.  
*   If vertices are A, B. The angle at C subtends the arc AB that does NOT contain C. This is the "arc of the circle".  
*   Since $AB$ is a diameter, any chord from one end to the other (diameter) divides circle into two semicircles.  
*   Does this mean Arc AB = 180 or 180-?  
*   If the chord connects $A(-R, 0)$ and $B(R, 0)$ (if center at origin). Then points on major arc are $(x,y)$ such that $x \ge 0$ (if y>0) or something. The length of the semicircle is 180 degrees.  
*   Is the angle subtended by this chord always 90?  
*   Let's check specific example: Circle diameter 2 (radius 1). Points on circle $(x,y)$ with $x^2+y^2=1$.  
*   Take $A=(-1,0), B=(1,0)$.  
*   Pick $C=(0,1)$. Angle is 90.  
*   Pick $C=(0,-1)$. Angle is 90.  
*   Pick $C=(1/\sqrt{2}, 1/\sqrt{2})$. This is on circle? $1/2+1/2=1$. Yes.  
*   Check angle $\angle ACB$.  
    *   Vector $CA = A-C = (-1-1/\sqrt{2}, -1/\sqrt{2})$. No, $(x_A-x_C, y_A-y_C) = (-1-\frac{\sqrt{2}}{2}, \dots)$?  
    *   Angle subtended by chord AB at $C$ is half the angle subtended by arc AB.  
    *   Arc AB (minor arc) has measure 180 degrees?  
    *   Let's check if $AB$ is diameter means arc $AB = 180$.  
        *   Yes, if it passes through center. So any chord connecting two antipodal points subtends a semicircle.  
    *   Therefore $\angle ACB = \frac{1}{2}(\text{measure of arc } AB)$.  
    *   Since measure of arc $AB$ is 180 (since it's a semicircle), angle is 90.  
    *   So, if vertices lie on circle with diameter $AB$, then $\angle ACB = 90^\circ$.  

*   **Is there any other interpretation?**  
*   "Angle B" could be the angle at vertex $B$.  
*   If we calculate $\angle A$ subtends arc $BC$. Then $\angle A = 14 \implies$ arc $BC = 28$.  
*   Since $\triangle ABC$ is inscribed in a circle where $AB$ is diameter, we have Arc $AB = 180$.  
*   This implies that vertex $C$ must lie on the circle such that arc $ACB$ (if vertices order is $A, C, B$?) or something.  
*   Let's check the case where $C$ lies on the major arc. Then $\angle ACB = 90$. So triangle is right angled at $C$.  
*   If $C$ lies on minor arc, does it still form a valid inscribed triangle? Yes. But $\angle C$ subtends the same arc $AB$ (if vertices are order A, B, C). No.  
*   Order: A, B, C. Arc AB is 180. Then angle at C is 90.  
*   What about angle at A? It subtends arc BC. If C lies on minor arc, then the arc from B to C (measured in direction away from A) would be 28 degrees. So $\angle A = 14$.  
*   Then what about $\angle B$? It subtends arc AC. Arc $AC = \text{Arc } AB - \text{Arc } BC$? Or something.  
*   If order is A, C, B (on minor arc). Then arc $CB$ is 28? No. Arc $CB$ would be part of the minor arc.  
*   Arc $AB = 180$. If C is on minor arc, then A-B-C are on circle in a specific order. But chord AB diameter means B is antipodal to A. The points between A and B (excluding endpoints) form the semi-circular region. So if vertices are ordered A, B, C on this semi-circle?  
*   No, vertices must be on the circumcircle. Circumcircle is the full circle or the arc AB (semicircle). Since $AB$ is diameter, circumcircle has two arcs. But since $\triangle ABC$ is inscribed, vertices must lie on the same circle. The condition "$\angle A=14$" and "$\angle C=90$" implies a specific triangle geometry.  
*   Usually, in such problems, we are looking for unique solution. If order of vertices could be ambiguous (i.e. $C$ can be on either side of AB relative to center), does it change $\angle B$? No.  
*   Let's check:  
*   Case 1: $C$ is in the major arc. $\triangle ABC$ right angled at $C$. $\angle B = 76^\circ$.  
*   Case 2: $C$ is on the minor arc (but not including endpoints). Then vertices are ordered $A, C, B$? Or just $A, B$ diameter.  
*   If vertices are on circle, and one side is diameter $AB$, then $\angle C = 90^\circ$. Why? Because $C$ lies on the circle. The angle subtended by chord $AB$ at circumference is 90. So regardless of which arc $C$ lies on (major or minor), if we take the triangle inscribed with vertices on the circle and side AB being a diameter, then $\angle C = 90^\circ$.  
*   This seems to be the key property: "Theorem: In an inscribed triangle, if one side is a diameter of the circumcircle, it's a right triangle."  
*   Is this true? Let's verify.  
*   Draw circle. $AB$ diameter. Place $C$ on major arc (above). Then $\angle ACB = 90$. Yes.  
*   Place $C$ on minor arc (below). Then $\angle ACB = 90$. Yes. (Since inscribed angle subtending semicircle is 90).  
*   So $\angle C$ must be 90 regardless of position on circle, as long as it's on the circumference.  
*   Is there any constraint that forces $C$ to be on major arc? No. But if $C$ was on minor arc, then $AB$ is a diameter, and $\angle C=90$.  
*   However, does this mean the triangle can exist with $\angle A = 14$ and $\angle B = 76$ and $\angle C = 90$? Yes.  
*   Is there any other constraint on the circumradius or positions of vertices? No.  
*   So the calculation holds: $180 - 14 - 90 = 76^\circ$.  

*   **Double check the wording "where AB is a diameter"**.  
*   Does this mean the chord AB has length equal to diameter? Yes.  
*   Is it possible that $\angle A$ refers to $\angle ACB$? No, standard notation for vertices.  
*   Could "$\angle B$" refer to angle $ACB$? Usually $\angle B$ means interior angle at vertex $B$.  

*   **Consider the case where $AB$ is not a diameter of the circumcircle but it is a side?** No, "inscribed in a circle where AB is a diameter".  
*   This phrasing means the triangle is inscribed in a circle that is circumscribing? Or rather, the circumcircle has diameter AB.  
*   The vertices $A, B$ are fixed on circle such that chord $AB$ passes through center and subtends 180 at circumference? No. A chord of a circle with diameter $R$.  
*   If diameter is length 2R. It divides the circle into two semicircles.  

*   **What if the triangle has $\angle C$ as part of the sum?**  
*   "How many degrees are in $\angle B$?"  
*   This implies a unique answer for $\angle B$.  
*   The only way to get another angle is if $AB$ subtends something else? No.  
*   If $\angle A = 14$, $\angle C = 90$. Then $\angle B = 76$.  

*   **Are there any alternative interpretations of "inscribed"?**  
*   Could it be that the triangle is inscribed in a circle where $AB$ is diameter? Yes, that's what I used.  
*   Could it be that the vertices are $A, C, B$ and $\angle A$ refers to angle subtended by side $BC$? No, "$\angle A = 14^\circ$" is standard for vertex A.  

*   **Final sanity check.**  
*   Problem statement: "triangle ABC with angle A = 14 degrees".  
*   Condition: "$AB$ is a diameter of the circumcircle".  
*   Question: Find $\angle B$.  
*   Logic: Since $AB$ is diameter, $\angle ACB = 90^\circ$.  
*   Sum of angles in $\triangle ABC$: $180^\circ$.  
*   Therefore $\angle B + 90^\circ + 14^\circ = 180^\circ$.  
*   $\angle B = 76^\circ$.  

*   **Is there any tricky case where $AB$ is diameter but $C$ lies on the same side as center?**  
*   This means $C$ is not on circumcircle? No, "inscribed" implies vertices on circle. If $C$ was inside, it wouldn't be inscribed in a circle (unless the circle surrounds the triangle). But standard interpretation is $A, B, C$ on the boundary.  
*   If vertices are on circle, and $AB$ is diameter, $\angle C = 90^\circ$.  

*   **Could there be a case where "inscribed in a circle" implies it's not necessarily inscribed in *that* specific circle?**  
*   "A triangle ... is inscribed in a circle". This refers to the existence of the circumcircle.  
*   "... where AB is a diameter." This describes the properties of that circle (the diameter).  

*   **Could there be an interpretation where $AB$ is a leg?**  
*   No, if $AB$ was a leg, it would be given as a side length? No, just "diameter".  
*   If $C$ lies on the segment $AB$, then $\angle C = 180$ or degenerate.  

*   **Is it possible that angle A and B sum to something else?**  
*   Let's re-read carefully. "A triangle ABC with angle A is ...".  
*   Usually, vertices are labeled in order $A-B-C$. But not always. The question says "$\angle A = 14$". This is unambiguous.  

*   **Is there a catch with the diameter subtending angle A?**  
*   Could $\angle A$ be an angle subtended by arc $BC$? Yes, $\angle CAB$.  
*   If this were true, then $28^\circ$ is measure of arc $BC$.  
*   Then $\angle C = 90 \implies$ hypotenuse $AB$.  
*   Then $\angle B = 76$.  
*   This works.  
*   Is there any other relation? No.  

*   **Conclusion:** The answer is 76.  

*   **Let's check for constraints on "degree".** The problem asks for degrees in the final answer. It asks "How many degrees are in".  
*   This implies finding a single number.  

*   **One edge case**: What if $AB$ is not diameter of circumcircle?  
*   "Triangle ... inscribed in a circle where AB is a diameter."  
*   This defines the property of the circle. It's standard phrasing for "circumcircle has diameter AB".  

*   **What if A and B are opposite?**  
*   Yes, that means $AB$ is diameter.  
*   If $AB$ were not diameter, but $C$ was on a circle with radius R? No, diameter condition fixes arc measure.  
*   Since $\angle A = 14$, it's just a specific angle.  

*   **Is it possible that the problem implies a cyclic quadrilateral?**  
*   If $AC$ and $BC$ are chords, and $AB$ is a chord passing through center. No, "diameter".  

*   **Is there any interpretation where AB is not the hypotenuse?**  
*   No, if $\angle C = 90$, then $AB$ is hypotenuse.  

*   **Final check on calculation.**  
*   $\angle B = 180 - \angle A - \angle C$.  
*   Is $\angle C$ definitely 90?  
*   Yes, Thales' Theorem states: In a circle with diameter $AB$, angle $C$ subtended by $AB$ is $90^\circ$.  
*   Or simply: $C$ lies on the major or minor arc relative to the diameter. If inscribed, $\angle C = 90$.  
*   Calculation: $180 - 14 - 90 = 76$.  

*   **What if vertices are in different order?**  
*   $\triangle ABC$ implies standard naming convention where angle at A is adjacent to A.  
*   If vertices were e.g. $C, B, A$, then $\angle A = \angle CAB$. This is the same thing.  

*   **Could "inscribed" mean something else?**  
*   Could it mean the triangle is inscribed in a circle of radius R such that AB is diameter? Yes.  

*   **Are there any other geometric constraints?**  
*   Maybe the triangle is not right angled at C? No, proven to be 90.  
*   Is $\angle A$ measured as acute or obtuse? Given as $14$. Acute.  
*   So $C=90$.  
*   Sum of angles must be less than 180? Yes, it's a triangle.  

*   **Final Answer seems to be 76.**  


## Answer

The problem asks for the measure of angle $\angle B$ in a triangle $\triangle ABC$ that is inscribed in a circle, given that side $AB$ is a diameter and $\angle A = 14^\circ$.  

**Reasoning:**  

1.  **Understand the Geometry:**  
*   The triangle $\triangle ABC$ is inscribed in a circle. This means that all three vertices, $A$, $B$, and $C$, lie on the circumference of this circle.  
*   The problem states that side $AB$ is a diameter of this circle. In geometric terms, if a circle has a diameter passing through two points (chord endpoints), then any point on the circle lies on the same circumcircle.  

2.  **Apply Thales' Theorem:**  
*   Thales' theorem states that an angle inscribed in a semicircle is a right angle ($90^\circ$).  
*   Since side $AB$ is a diameter, $\triangle ABC$ has vertex $C$ (the third vertex) lying on the circle.  
*   Therefore, the angle subtended by the diameter $AB$ at point $C$ is a right angle. Thus, $\angle ACB = 90^\circ$.  
*   Alternatively, using the definition of an inscribed triangle, if we are given a triangle with vertices on a circle and one side is a diameter, that specific side acts as the hypotenuse (or chord), and the vertex at the end of the diameter subtends a $90^\circ$ angle.  

3.  **Calculate Angle $\angle B$:**  
*   The sum of angles in any triangle is always $180^\circ$.  
*   In $\triangle ABC$, the vertices are $A, B, C$.  
*   We know:  
*   $\angle A = 14^\circ$  
*   $\angle ACB = 90^\circ$  
*   The third angle, $\angle B$, can be found using the subtraction property:  
$$ \angle B = 180^\circ - (\angle A + \angle C) $$  
$$ \angle B = 180^\circ - (14^\circ + 90^\circ) $$  
$$ \angle B = 180^\circ - 104^\circ $$  
$$ \angle B = 76^\circ $$  

**Alternative Interpretation Check:**  
Is it possible that $\angle A$ is subtended by arc $BC$? Yes, and since $\triangle ABC$ is inscribed in a circle with diameter $AB$, this configuration is consistent. The calculation holds regardless of the exact position of $C$ on the major or minor arc, as long as the vertex $C$ forms a valid triangle with side $AB$ being a diameter, which forces $\angle ACB = 90^\circ$.  

Thus, the measure of $\angle B$ is uniquely determined.  

**Final Answer:**  
The measure of angle $B$ is $76^\circ$.  

\boxed{76}  
