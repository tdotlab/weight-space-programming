# test/geometry/347.json (Geometry, level 3)

> A triangle $\triangle ABC$ with $\angle A = 14^\circ$ is inscribed in a circle where $AB$ is a diameter. How many degrees are in $\angle B$?  

**Correct.** Gold `76^\circ`, predicted `76`. Finish: stop, 7587 tokens, 1 waits, 603.6 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's my thought process for solving this geometry problem:  

1.  **Analyze the Request:**  
    *   **Given:** A triangle $\triangle ABC$.  
    *   **Condition 1:** Angle $A = 14^\circ$ (specifically $\angle BAC = 14^\circ$).  
    *   **Condition 2:** The triangle is inscribed in a circle. This implies the vertices lie on the circumference.  
    *   **Condition 3:** Side $AB$ is a diameter.  
    *   **Goal:** Find the measure of angle $\angle B$ (specifically $\angle ABC$).  

2.  **Recall Relevant Geometric Theorems:**  
    *   **Inscribed Angle Theorem:** An angle $\theta$ inscribed in a circle is half of the central angle $2\theta$ that subtends the same arc. Also, an inscribed angle equals half the measure of its intercepted arc.  
    *   **Thales's Theorem (Diameter Theorem):** If $AB$ is a diameter and $C$ lies on the circle, then $\angle ACB = 90^\circ$. This is a crucial property.  

3.  **Visualize/Draw the Diagram:**  
    *   Imagine a circle. Let the center be $O$.  
    *   Draw diameter $AB$. Since $A$ and $B$ are on the circle, the line segment connecting them passes through the center.  
    *   Pick a point $C$ on the circle such that it forms a triangle with $AB$.  
    *   We are given $\angle BAC = 14^\circ$. This is an inscribed angle subtending arc $BC$.  

4.  **Identify Key Relationships:**  
    *   Since $AB$ is the diameter, $\angle C$ (which is $\angle ACB$) must be a right angle ($90^\circ$).  
    *   The problem asks for $\angle B$, which is $\angle ABC$.  

5.  **Formulate an Equation/Solution:**  
    *   Consider $\triangle ABC$.  
    *   We have the sum of angles in a triangle: $\angle A + \angle B + \angle C = 180^\circ$.  
    *   Alternatively, consider the arc lengths or intercepted arcs.  

    *   *Method 1: Using Arcs*  
        *   $\angle A$ (specifically $\angle BAC$) subtends the arc $BC$.  
        *   The measure of arc $BC$ is equal to the measure of angle $A$. So, arc $BC = 2 \times 14^\circ = 28^\circ$.  
        *   Since $AB$ is a diameter, the semicircle corresponds to $180^\circ$ (or half a circle).  
        *   The angle at the circumference, $\angle C$, subtends the arc $ABC$ (the semicircle). No, $\angle C$ is an inscribed angle subtending the arc $ADC...$ no, it's subtending the major arc $AB$. Let's be precise.  
        *   Angle $A$ subtends arc $BC$.  
        *   Angle $C$ is the inscribed angle subtending the semicircle (arc $ABC$? No).  
        *   Let's look at the angles relative to the vertices.  
        *   $\angle A = 14^\circ$. This angle is $\angle BAC$. It intercepts arc $BC$. Measure of arc $BC = 2 \times 14^\circ = 28^\circ$.  
        *   Point $C$ is on the circle. Points $A, C, B$ are in some order on the circle. Since it's a triangle inscribed in a circle, $C$ is distinct from $A$ and $B$.  
        *   Since $AB$ is a diameter, $A$ and $B$ divide the circle into two semicircles. The angle $\angle ACB = 90^\circ$ (Thales's Theorem).  
        *   Now, let's look at $\angle B$, which is $\angle ABC$. This angle intercepts arc $AC$.  
        *   Let $x$ be the measure of arc $AC$.  
        *   Then $\angle ABC = x / 2$. So $x = 2 \times \angle B$.  

    *   *Method 2: Using the Sine Rule*  
        *   In triangle $ABC$, sides are $a, b, c$ (opposite to $A, B, C$).  
        *   Law of sines: $a / \sin A = b / \sin B = c / \sin C$.  
        *   Here $c = AB$ is the diameter. So $AB = 2R$.  
        *   $\sin C = \sin 90^\circ = 1$.  
        *   $AB / \sin A = c / \sin A$. No, this gives circumdiameter. Circumdiameter $= c/\sin C = AB / 1 = AB$ (since $AB$ is diameter). This makes sense.  
        *   We need $\angle B$. We know $\angle A = 14^\circ$, $\angle C = 90^\circ$.  
        *   So $180^\circ - 14^\circ - 90^\circ = 76^\circ$.  

    *   *Method 3: Direct calculation with arcs*  
        *   The circle is a full $360^\circ$.  
        *   Arc $ACB$ (the arc from $A$ to $B$ not passing through $C$) is $180^\circ$ if $C$ were on that semicircle? No.  
        *   Angle $C = 90^\circ$. This means the arc $AB$ (not containing $C$) is a semicircle ($180^\circ$). This assumes $A, B$ are endpoints of diameter.  
        *   We are given $\angle A = 14^\circ$. This is an inscribed angle subtending arc $BC$.  
        *   So, measure of arc $BC = 2 \times 14^\circ = 28^\circ$.  
        *   Since the arc $AC$ + arc $CB$ = arc $AB$ (semicircle).  
        *   Arc $AB = 180^\circ$.  
        *   So, arc $AC = 180^\circ - \text{arc } BC = 180^\circ - 28^\circ = 152^\circ$.  
        *   Angle $\angle B$ subtends arc $AC$.  
        *   Therefore, $\angle B = \frac{1}{2} \times (\text{arc } AC)$.  
        *   $\angle B = 152^\circ / 2 = 76^\circ$.  

    *   *Method 4: Sine Rule calculation directly.*  
        *   Triangle $ABC$ is a right-angled triangle because $AB$ is the hypotenuse (diameter).  
        *   $\angle B + \angle A = 90^\circ$? No, that's if it's a right triangle with hypotenuse opposite to angle. Yes, hypotenuse $c=AB$.  
        *   The angle opposite side $AC$ is $\angle B$. The angle opposite side $BC$ is $\angle A$.  
        *   So $\tan A = AC / BC$? Not useful directly without lengths.  
        *   But we have the sum of angles in triangle:  
$$14^\circ + \angle B + 90^\circ = 180^\circ$$  
$$\angle B = 180^\circ - (14^\circ + 90^\circ)$$  
$$\angle B = 180^\circ - 104^\circ$$  
$$\angle B = 76^\circ$$  

    *   *Method 5: Inscribed angle theorem check.*  
        *   $\angle A$ intercepts arc $BC$. So measure of arc $BC$ is $2 \times 14 = 28$.  
        *   The point $C$ is somewhere. Since it's a triangle, it's not on the line $AB$.  
        *   Angle $\angle B$ is an inscribed angle intercepting arc $AC$.  
        *   The measure of arc $AC$ depends on where $C$ is located relative to $A$ and $B$.  
        *   We know arc $BC = 28^\circ$.  
        *   The total circle is $360^\circ$. Arc $AC + \text{Arc } BC + \text{Arc } AB (\text{minor})$? No.  
        *   Since $AB$ is diameter, the arc subtended by $AB$ (not containing $C$) is $180^\circ$. This is the upper semicircle. The angle $\angle ACB = 90^\circ$.  
        *   So the arc from $A$ to $B$ not passing through $C$ is a semi-circle ($180^\circ$).  
        *   We established earlier: Arc $AC + \text{Arc } CB = \text{Arc } AB$ (major/semi).  
        *   Let's re-verify the arc addition.  
            *   Arc $AB$ (semicircle) = $180^\circ$.  
            *   Arc $BC$ is part of it? Or is $C$ on one side?  
            *   In $\triangle ABC$, vertices are ordered $A, B, C$ around the circle.  
            *   Inscribed angle $\angle A$ (at vertex $A$) intercepts arc $BC$.  
            *   So measure of arc $BC = 2 \times 14^\circ = 28^\circ$.  
            *   Since $AB$ is diameter, the circle is divided into two semicircles: one containing $C$, one not containing $C$.  
            *   $\angle C = 90^\circ$. This confirms arc $BC + \text{arc } CA = 180^\circ$. (The semicircle opposite to angle $B$). No, the inscribed angle at $C$ intercepts arc $AB$ (the one containing neither endpoints? No, that's a straight line).  
            *   Let's stick to the property: The sum of two non-right angles in a right triangle is 90. This is the most robust way.  

    *   *Let's re-read the problem carefully to ensure no misinterpretation.*  
        *   "Triangle $\triangle ABC$". Vertices A, B, C.  
        *   "$\angle A = 14^\circ$" usually means $\angle BAC$.  
        *   "inscribed in a circle" -> standard setup.  
        *   "$AB$ is a diameter". This fixes the position of $C$. Since it's a triangle, $C \neq A, B$. So $\angle C \neq 0, 180$.  
        *   Thales's Theorem: If $AB$ is diameter, angle subtended by $AB$ at any point on circle (other than A and B) is $90^\circ$. Thus $\angle ACB = 90^\circ$.  
        *   Sum of angles in $\triangle ABC$: $\angle A + \angle B + \angle C = 180^\circ$.  
        *   $14^\circ + \angle B + 90^\circ = 180^\circ$.  
        *   $\angle B = 76^\circ$.  

    *   *Are there any ambiguities?*  
        *   Could "Angle A" mean something else? In triangle geometry, angles are usually denoted by the vertex inside the angle. So $\angle A$ is at vertex $A$.  
        *   Could "inscribed in a circle where AB is a diameter" imply specific ordering of points? No, symmetry makes it irrelevant for the calculation.  
        *   Could it be a non-Euclidean geometry context? Usually, unless specified, assume Euclidean geometry.  

6.  **Double check with alternative interpretation (just in case):**  
    *   What if $C$ is on the arc such that the angle subtended by arc $AC$ at $B$ is requested? Yes, that's $\angle B$.  
    *   Calculation:  
        *   Circle diameter $D$.  
        *   Arcs corresponding to vertices.  
        *   Angle $A = 14^\circ \implies$ Arc $BC = 28^\circ$. (Assuming $C$ is on the circle such that the chord subtends this angle).  
        *   Is $\angle B$ determined?  
            *   Yes, in a right triangle inscribed in a circle, the angles are complementary.  
            *   Since sum of angles = 180, and one is 90 (Thales), the other two must sum to 90.  
            *   So $\angle A + \angle B = 90^\circ$.  
            *   $14^\circ + \angle B = 90^\circ$?  
            *   Let's check the complement relation again.  
            *   In right triangle $ABC$, $\tan(\text{angle}) = \text{adj}/\text{opp}$.  
            *   $\tan(A) = BC/AC$.  
            *   $\tan(B) = AC/BC$.  
            *   Therefore $\tan(B) = 1/\tan(A)$, so $B = 90 - A$.  
            *   This holds if the right angle is at $C$ (opposite to diameter). Yes, Thales's theorem.  
        *   Is it possible that the arc measure isn't what I thought?  
            *   Inscribed angle $\theta$ intercepts arc $2\theta$.  
            *   $\angle A = 14^\circ$ intercepts arc $BC$. So arc $BC = 28^\circ$.  
            *   Angle $\angle B$ intercepts arc $AC$.  
            *   Angle $\angle C = 90^\circ$ intercepts arc $AB$ (semicircle). So arc $AB$ is $180^\circ$.  
            *   Arc $AB = \text{Arc } AC + \text{Arc } CB$? Or is it Arc $AC$ - Arc $CB$?  
            *   Let's trace the circle. Points A, B are endpoints of diameter. C is on the circumference.  
            *   The arc from A to B contains points C? No, if it contains C, then angle C would be half the angle subtended by the other semicircle? No.  
            *   If $C$ lies on the semicircle from $A$ to $B$, then the measure of arc $AB$ not containing $C$ is $180^\circ$. This arc $AB_{not C}$ consists of Arc $AC$ + Arc $CB$? No.  
            *   Let's define arcs by endpoints.  
            *   Let's say we traverse the circle starting at A, going towards B.  
            *   If C is between A and B on that semicircle: Arc AC + Arc CB = 180.  
            *   $\angle A$ subtends arc $CB$. So measure(arc CB) = $2 \times 14 = 28$.  
            *   Then measure(Arc AC) = $180 - 28 = 152$.  
            *   $\angle B$ is the inscribed angle at vertex B. It subtends arc AC (the one "inside" the triangle, or just the arc between endpoints A and C not containing B). Yes.  
            *   So $\angle B = \frac{1}{2} \text{measure}(Arc AC)$.  
            *   $\angle B = \frac{1}{2} (152^\circ) = 76^\circ$.  

    *   What if C is on the other semicircle? i.e., between A and B via the "other side"?  
        *   Symmetry. The problem specifies "triangle $\triangle ABC$". Order doesn't change the set of points.  
        *   However, there is a case where arc addition might differ.  
        *   Suppose C is on the major arc AB (i.e., not the diameter). Since $AB$ is a diameter, there are two arcs from A to B. One is 180 degrees. The other is 180 degrees? No, circle is split into two semicircles by the diameter line.  
        *   Any point C on the circle (except A and B) lies on exactly one of these two semicircles.  
        *   If C is on one semicircle, arc $AC$ + arc $CB = 180^\circ$. (The whole semicircle).  
            *   $\angle A$ subtends arc $BC$? Let's check inscribed angle definition. The vertex is at the "top" of a chord.  
            *   Angle $\angle BAC$ has vertex at $A$. Its rays pass through $B$ and $C$. So it intercepts the arc between $B$ and $C$ not containing $A$.  
            *   Is that correct? Yes, $\angle A$ intercepts arc $BC$.  
            *   So measure of arc $BC = 2 \times 14^\circ = 28^\circ$.  
            *   The total arc length from A to B along the semicircle containing C is sum of Arc AC + Arc CB? Or Arc AB (diameter)? No, if C is on that semicircle, then the points A, C, B appear in order.  
                *   Arc $AB$ (semicircle) = Arc $AC$ + Arc $CB$.  
            *   Therefore $180^\circ = \text{Arc } AC + \text{Arc } BC$.  
            *   $\text{Arc } AC = 180^\circ - 28^\circ = 152^\circ$.  
            *   Now consider angle $\angle B$ (vertex at $B$, rays $BA$ and $BC$). It intercepts the arc $AC$ not containing $B$.  
                *   In the sequence A, C, B... no, in a circle with diameter AB, points are arranged such that A and B separate the circle. If C is on one semicircle (say upper), then the order is A -> C -> B.  
                *   The angle at B intercepts arc AC?  
                    *   Angle $\angle ABC$. Vertex $B$. Rays go to $A$ and $C$. Arc intercepted is arc $AC$ not containing $B$.  
                    *   Since order is A-C-B, the arc not containing $B$ is indeed the minor arc (if A,B,C close) or major? No.  
                    *   Let's visualize.  
                    *   Circle center O. Diameter AB horizontal. B at right, A at left.  
                    *   Point C somewhere above.  
                    *   Angle $\angle BAC$. Vertex A. Rays to B and C. Intercepted arc is BC (upper arc).  
                    *   Angle $\angle ABC$. Vertex B. Rays to A and C. Intercepted arc is AC (left part of circle, upper semicircle).  
                    *   Yes, arc $AC$ is the one between A and C on the upper side.  
                    *   Measure of arc $BC = 28^\circ$.  
                    *   Measure of arc $AB$ (upper) = $180^\circ$.  
                    *   So arc $AC + \text{arc } BC = 180^\circ$.  
                    *   $\text{arc } AC + 28^\circ = 180^\circ \Rightarrow \text{arc } AC = 152^\circ$.  
                    *   Angle $\angle ABC$ intercepts arc $AC$.  
                    *   Is it the intercepted arc? Angle $\angle ABC$ subtends arc $ADC$ where D is some point on circle between B and C? No, just the arc connecting A and C not passing through B.  
                    *   Since A, C are on upper semicircle, and B is on right end... The arc AC connects A to C. Does it pass through B? No. Does it contain D? Not specified. But the inscribed angle theorem works with the arc "inside" the angle.  
                    *   If order is A-C-B (on circle), then angle at B looks "across" from C to A. It intercepts arc AC.  
                    *   The measure is half the measure of arc AC.  
                    *   So $\angle B = 152 / 2 = 76^\circ$.  

    *   What if order is A-B-C? (i.e. A, then C, then B? No, that's not a triangle inscribed).  
    *   If points are in order A, B, C around the circle:  
        *   Arc $AC$ + Arc $CB$ = Arc $AB$ (minor)? No.  
        *   If A, B, C are consecutive. Then $\angle ACB$ subtends arc $AB$. Since AB is diameter, arc $AB$ is 180? No. Arc $AB$ not containing C.  
        *   The arc intercepted by angle at C must be the arc between A and B that does NOT contain C. That would be the diameter arc (semicircle). So $\angle C = 90$. Correct.  
        *   Angle at A ($\angle BAC$) intercepts arc $BC$. Measure is $2 \times 14 = 28$.  
        *   If order is A, C, B around the circle (semicircle), then Arc $AB$ consists of Arc $AC$ + Arc $CB$. Sum is 180.  
        *   Arc $BC$ corresponds to angle A. $2 \times 14 = 28$.  
        *   So Arc $AC = 152$. Angle B intercepts arc AC. $\angle B = 76$.  
    *   Are there any other configurations?  
        *   Can angle A be "reflex"? No, standard geometry implies interior angles < 180.  
        *   Does the circle have multiple centers? No.  

7.  **Final Verification:**  
    *   Given: Triangle inscribed in circle with $AB$ diameter.  
    *   Theorem: If $AB$ is diameter, $\angle C = 90^\circ$.  
    *   In right triangle $\triangle ABC$, $\angle A + \angle B + \angle C = 180^\circ$.  
    *   Given $\angle A = 14^\circ$.  
    *   Substitute: $14^\circ + \angle B + 90^\circ = 180^\circ$.  
    *   $\angle B = 180 - 104 = 76^\circ$.  

    *   Is there any ambiguity in "Angle A = 14"? Could it be angle at vertex $B$? No, "$\angle B$" usually refers to the angle at B, but "$\angle A = 14$" refers to angle at A.  
    *   Is there any case where C is on the diameter? If C is on the diameter, it's not a triangle (collinear). So $C$ must be off the diameter.  

    *   Let's check if there are other interpretations of "inscribed".  
        *   Maybe "ABC" means vertices A, B, C but orientation matters?  
        *   Usually $\triangle ABC$ refers to the set of points.  
        *   Is it possible that the angle is $\angle ACB$? No, "$\angle B$" asks for the angle at vertex B.  

    *   Are there two possible answers?  
        *   Suppose we consider the other arc $AB$. If $C$ lies on the circle, arc measure sum is fixed.  
        *   Since it's a triangle inscribed in a circle (implied non-degenerate), C cannot be A or B.  
        *   There are two positions for C on the major arc AB and minor arc AB? No, just upper/lower. It creates the same triangle geometry (reflected). So angle B is the same.  

    *   What if $\angle A$ was obtuse? Then it would be > 90. But given 14.  
    *   What if $AB$ wasn't a diameter? Problem states it is.  

    *   Let's write down the steps clearly.  
        1.  Identify properties of circle and inscribed angles.  
        2.  Identify the specific theorem for the angle at vertex opposite to the diameter.  
        3.  Perform arithmetic subtraction.  

    *   Step 1: The vertices $A, B, C$ lie on a circle. $AB$ is a diameter.  
    *   Step 2: According to Thales's Theorem (or property of inscribed angles), an angle inscribed in a semi-circle is a right angle ($90^\circ$). Therefore, $\angle ACB = 90^\circ$.  
    *   Step 3: In triangle $ABC$, the sum of interior angles is $180^\circ$.  
$$\angle A + \angle B + \angle C = 180^\circ$$  
    *   Step 4: Substitute known values. $\angle A = 14^\circ$, $\angle C = 90^\circ$.  
    *   Step 5: Solve for $\angle B$.  
$$14^\circ + \angle B + 90^\circ = 180^\circ$$  
$$\angle B = 180^\circ - 104^\circ = 76^\circ$$  

    *   Does this seem too simple? Sometimes geometry problems have a catch.  
        *   "How many degrees are in $\angle B$?"  
        *   Could it be that the triangle is defined differently? No.  
        *   What if $C$ lies on the major arc such that angle A intercepts the other semicircle? No, angle at A subtends arc BC. Since AB is diameter, arc BC + arc AC = 180 (assuming C is between them). This relies on C being "between" A and B.  
        *   Let's check the case where C is on the minor arc.  
            *   If $C$ lies on the minor arc $AB$, then $\triangle ABC$ exists? Yes, but wait. If $C$ is on the circle segment defined by diameter AB (semicircle), the sum of angles is still 180.  
            *   Let's check "intercepted arc" again.  
            *   Angle at A ($\angle BAC$) intercepts arc $BC$. This arc goes from $B$ to $C$ not passing through $A$.  
            *   If $AB$ is diameter, there are two arcs between $A$ and $B$: Arc 1 (upper), Arc 2 (lower). Both are 180? No, the lines from center connect to ends. They define two semicircles. The whole circle is partitioned into arc from A to B (clockwise) and arc from B to A (counter-clockwise). These sum to 360.  
            *   If $C$ is on Arc 1 (say, upper), then Arc $BC$ + Arc $AC$ = Arc $AB$? No. Arc $AB$ is the whole semi-circle? No, that's just a segment. The arc from A to B contains C if C is between them.  
            *   If C is on the upper semicircle, it lies somewhere between A and B. So Arc(A...C) + Arc(C...B) = Arc(A...B) = 180.  
            *   $\angle A$ intercepts arc $BC$. Measure = $2 \times 14 = 28$.  
            *   Then Arc(AC) = $180 - 28 = 152$.  
            *   Angle B ($\angle ABC$) intercepts arc $AC$ (the one not containing B). This is Arc AC. Measure = 152.  
            *   $\angle B = 152 / 2 = 76$.  
        *   If $C$ is on the lower semicircle, it lies between A and B. Same result.  

    *   Is there a case where Arc BC does not include C? No, arc connects endpoints of an angle at vertex.  
    *   So $\angle B = 76^\circ$.  

    *   Just to be absolutely sure, is it possible that $\angle A$ refers to the interior angle of the sector or something weird? No, "triangle ABC".  
    *   Is it possible $A=14$ means arc $AB$ is 14? No, "Angle A = 14" means $\angle BAC = 14$.  

    *   Let's check a similar problem online to ensure no common misinterpretation.  
        *   Problem: Triangle inscribed in circle, AB diameter, angle A = 15 degrees. Find angle B? Answer is $90-15=75$.  
        *   This confirms the logic.  

    *   Final check of the question phrasing: "A triangle $\triangle ABC$ with $\angle A = 14^\circ$ is inscribed in a circle where $AB$ is a diameter."  
    *   Everything aligns. The logic holds up via two distinct methods (sum of angles and arc measure).  

    *   One small detail: Is it possible that the triangle is oriented such that $\angle A = 14$ implies something else? No, standard notation.  
    *   Result: 76.  

    *   Let me construct the final response.  
        1.  State Thales's Theorem to establish $\angle C = 90^\circ$.  
        2.  Use sum of angles in a triangle ($A+B+C=180$).  
        3.  Calculate $B = 180 - 90 - 14$.  
        4.  Result is 76.  

    *   Alternative thought: Could the "inscribed" part imply it's not a right triangle? No, inscribed in circle with diameter means right angle at third vertex. This is a theorem. If $AB$ were a chord (not diameter), we wouldn't know unless more info was given. But it's specified as diameter.  

    *   Calculation:  
$180 - 90 = 90$  
$90 - 14 = 76$.  
    *   The answer is 76 degrees.  

    *   Formatting:  
"put your final answer within \boxed{}"  
So, \boxed{76}. Or just the text inside. Usually just the number or the value with unit if asked. The prompt asks "How many degrees". I will provide the number and degree symbol.  

    *   One more check: Did I interpret $\angle B$ correctly? Yes, angle at vertex B.  
    *   Did I interpret $\angle A$ correctly? Yes, angle at vertex A.  

    *   What if the question implies $C$ is fixed relative to $A, B$ in terms of orientation? No info given. But the triangle is just a shape inscribed. The property holds regardless.  

    *   Final Answer seems solid.  


## Answer

To find the measure of angle $\angle B$ in triangle $\triangle ABC$, we use the properties of a circle and its inscribed triangles (angles).  

**Step 1: Use Thales's Theorem.**  
Thales's Theorem states that if a triangle is inscribed in a circle such that one side of the triangle is a diameter, then the angle opposite to the diameter is a right angle ($90^\circ$).  
In this problem, $AB$ is a diameter. Therefore, the angle $\angle C$ (which is $\angle ACB$) subtended by the arc $AB$ (the one not containing $C$, or rather, the angle opposite the diameter in the triangle context) is a right angle.  
$$ \angle C = 90^\circ $$  

**Step 2: Use the Sum of Angles in a Triangle.**  
The sum of the interior angles of any triangle is always $180^\circ$. In triangle $\triangle ABC$:  
$$ \angle A + \angle B + \angle C = 180^\circ $$  

**Step 3: Substitute the known values and solve for $\angle B$.**  
We are given that $\angle A = 14^\circ$ (which is $\angle BAC$) and we found that $\angle C = 90^\circ$. Substituting these into the equation:  
$$ 14^\circ + \angle B + 90^\circ = 180^\circ $$  

Now, solve for $\angle B$:  
$$ \angle B = 180^\circ - (14^\circ + 90^\circ) $$  
$$ \angle B = 180^\circ - 104^\circ $$  
$$ \angle B = 76^\circ $$  

Alternatively, using the inscribed angle theorem:  
The measure of an inscribed angle is half the measure of its intercepted arc.  
$\angle A$ intercepts arc $BC$, so $\text{arc } BC = 2 \times 14^\circ = 28^\circ$.  
Since $AB$ is a diameter, arc $AB$ (the semicircle) measures $180^\circ$. The arc $AC$ consists of the remaining part of the semicircle: $\text{arc } AC = 180^\circ - 28^\circ = 152^\circ$.  
$\angle B$ is an inscribed angle intercepting arc $AC$, so:  
$\angle B = \frac{1}{2} \times (\text{measure of arc } AC) = \frac{1}{2} \times 152^\circ = 76^\circ$.  

Both methods yield the same result.  

\boxed{76}  
