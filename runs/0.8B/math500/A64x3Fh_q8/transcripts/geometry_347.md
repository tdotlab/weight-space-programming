# test/geometry/347.json (Geometry, level 3)

> A triangle $\triangle ABC$ with $\angle A = 14^\circ$ is inscribed in a circle where $AB$ is a diameter. How many degrees are in $\angle B$?  

**Correct.** Gold `76^\circ`, predicted `76`. Finish: stop, 13938 tokens, 3 waits, 1519.3 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's my thought process for solving this geometry problem:  

1.  **Analyze the Request:**  
    *   **Given:** A triangle $\triangle ABC$.  
    *   **Condition 1:** $AB$ is a diameter of the circle on which $\triangle ABC$ is inscribed.  
    *   **Condition 2:** $\angle A = 14^\circ$ (This refers to the vertex angle at vertex $A$).  
    *   **Goal:** Find the measure of $\angle B$ in degrees.  

2.  **Recall Relevant Geometric Theorems:**  
    *   *Circle Theorem:* An inscribed angle is half the subtended arc. Or, a key theorem: An angle inscribed in a semicircle is a right angle ($90^\circ$).  
    *   Let's look at the specific conditions here. We are given a triangle $\triangle ABC$.  
        *   $AB$ connects vertices $A$ and $B$.  
        *   The condition "$AB$ is a diameter" implies that the segment connecting $A$ and $B$ is the diameter of the circumcircle of $\triangle ABC$.  
    *   *Implication:* If the chord $AB$ is a diameter, any angle subtended by this diameter at the circumference lies on the major arc (or rather, since $ABC$ is inscribed in the circle, any point on the other side of the diameter $AC$ creates an inscribed angle).  
    *   However, let's re-read carefully. The problem asks for $\angle B$.  
        *   Usually, we denote angles like $\angle B = \angle ABC$.  

3.  **Apply the "Angle in a Semicircle" Property:**  
    *   Let's consider the triangle vertices on a circle.  
    *   If $AB$ is a diameter of the circumcircle, then $\angle ACB$ (the angle at vertex $C$) subtends the diameter $AB$.  
    *   Is there any ambiguity about which side of the line containing $AB$ is "subtended"?  
        *   In circle geometry, an inscribed angle subtending a chord is defined by its position on the major arc relative to the center? No, it's just: If the segment $AB$ passes through the midpoint of the circle, it's diameter. Then $\angle ACB = 90^\circ$ (Thales' theorem) provided that $C$ is not on the line segment $AB$.  
        *   But here, the question asks for $\angle B$ ($\angle ABC$).  

    *   Let's re-read carefully: "A triangle $\triangle ABC$ with $\angle A = 14^\circ$ is inscribed in a circle where $AB$ is a diameter."  
    *   Is it possible that the vertices of the triangle are defined by some order?  
        *   If $AB$ is the diameter, then point $C$ lies on the circle.  
        *   If we consider the inscribed angle theorem: $\angle ACB = 90^\circ$.  
            *   Then in $\triangle ABC$, sum of angles is $180^\circ$.  
            *   $\angle A + \angle B + \angle C = 180^\circ$.  
            *   $14^\circ + \angle B + 90^\circ = 180^\circ$.  
            *   $\angle B = 180^\circ - 180^\circ = 0$? No, that means triangle is degenerate. This assumes $\triangle ABC$ is the specific one formed by vertices $A, C, B$ as angles are measured at $C$. The problem asks for angle at vertex $B$ (or maybe just angle at vertex $B$).  
            *   Let's check the notation. Usually, $\angle A$ refers to the interior angle at vertex $A$. $\angle B$ refers to the interior angle at vertex $B$. $\angle C$ refers to the interior angle at vertex $C$.  
            *   The question is: $\angle B$. This usually means $\angle ABC$.  
    *   Let's re-evaluate the property of the circle.  
        *   We know that in a triangle inscribed in a circle, $AB$ is a diameter.  
        *   Is it possible that $\triangle ABC$ isn't the triangle itself? No, "$\triangle ABC$ ... inscribed" implies vertices are on the circle.  
    *   Let's look at the notation again: "where $AB$ is a diameter". This usually means $A, B$ are endpoints of the diameter.  
    *   Therefore, $\angle ACB = 90^\circ$? No, that theorem says if a point is on the circumference, it subtends the diameter. If $C$ lies on the circle, and $AB$ is the diameter, then $\angle ACB = 90^\circ$.  
    *   However, let's look at the problem phrasing again: "How many degrees are in $\angle B$?".  
        *   This implies we need to determine the value of angle $ABC$ based on the given information.  
        *   If we assume standard triangle orientation where vertices are listed counterclockwise (e.g., starting from A, going to B and then C), then $\angle B$ is an interior angle.  
        *   Let's test the logic:  
            1.  $AB$ is diameter of circle passing through $A, B, C$.  
            2.  Angle subtended by a diameter at any point on the circumference is $90^\circ$. Which points are "on the circumference"? Vertices $A, C, B$. The angle at vertex $C$ (which is $\angle ACB$) subtends arc $AB$. Arc $AB$ is the whole semicircle. The angle *at the circumference* subtended by a diameter is $90^\circ$.  
            3.  Thus, $\angle ACB = 90^\circ$? Or could it be that $C$ lies on the minor arc? No, any point on the circle forms a right angle with endpoints of diameter. So $\angle ACB = 90^\circ$.  
            4.  Then in $\triangle ABC$, $\angle A + \angle B + \angle C = 180^\circ$.  
$14^\circ + \angle B + 90^\circ = 180^\circ$.  
$\angle B = 180 - 104 = 76^\circ$?  
        *   This seems too straightforward. Let's check the alternative interpretation where "AB is a diameter" might refer to something else or I am misinterpreting the problem context.  

    *   Could the question be: "$\angle A = 14^\circ$" refers to angle $C$? No, "A triangle... where AB is a diameter". That's specific.  
    *   Let's reconsider the angle $\angle B$. Is it possible that $B$ is the vertex of an angle that isn't subtending a semicircle? No, if $AB$ is diameter, any point on the circle forms a right angle. This includes $C$. So $\angle ACB = 90^\circ$.  
    *   But the question asks for $\angle B$. If $\angle C = 90^\circ$, then $\angle A + \angle B = 90^\circ$ (if we consider cyclic quadrilateral or something, but it's just a triangle).  
    *   Let's check if $\angle A$ and $\angle B$ are defined in a different way. Maybe the diagram shows $AB$ as an *arc*? No, usually points represent vertices of angles.  
    *   Is there any other interpretation?  
        *   What if the question meant $\angle C = 14^\circ$? "triangle ABC inscribed... angle A is 14". It says "A" and "$B$" are letters. So $\angle A$ is at vertex $A$.  
    *   Let's look for a potential trap. Is it possible that the circle doesn't pass through $C$? The phrase "inscribed in a circle where AB is a diameter" strongly implies $\triangle ABC$ lies on that circle, i.e., vertices $A$, $B$, and $C$ are on the circle.  

    *   So the problem reduces to:  
Given triangle $ABC$ inscribed in a circle such that chord $AB$ is the diameter.  
Find angle $B$ (at vertex $B$).  
Theorem: Angle subtended by a diameter at any other point on the circumference is $90^\circ$.  
Which points are on the circumference? $C$ and $A$ (since $\angle A$ refers to vertex $A$). $A, B, C$ are vertices of the triangle. So $\angle ACB = 90^\circ$.  
    *   This would imply $\angle B + \angle A = 90^\circ$ is wrong? No.  
    *   The angles of a triangle are sum to $180$.  
    *   If $\angle C = 90^\circ$, and $\angle A = 14^\circ$, then $\angle B = 180 - (90 + 14) = 76^\circ$.  

    *   Is it possible that the problem meant $C$ is a point on the arc? No. "ABC" implies vertices of the triangle.  
    *   Let's consider if the circle is centered at $A$ or something else.  
        *   If $\angle A = 14^\circ$, this angle refers to angle at vertex $A$.  
        *   Is it possible that the condition "$AB$ is a diameter" implies we can use Power of a Point or just basic geometry? No, the standard theorem applies directly.  

    *   Let's double-check my interpretation. Does "AB is a diameter" mean segment AB connects A and B and passes through center O? Yes.  
    *   If $AB$ is diameter, then $\angle ACB = 90^\circ$.  
    *   Why is this so simple? Because it relies on the property that any angle subtended by a diameter is a right angle ($90^\circ$). It does not rely on specific coordinates.  

    *   Is there any catch with the term "inscribed in"?  
        *   Usually inscribed means all vertices are on the circle. Here $A, B, C$ are on the circle.  
    *   Let's check if I missed something about $\angle B$. Maybe $\angle A = \angle C$? No.  

    *   Let's check for any other interpretation of "$\angle A$". Could it mean angle between side $c$ and $b$? Yes.  
    *   Let's check if $\triangle ABC$ could be defined such that the vertices are not in order around the circle.  
        *   E.g., vertices $A, B, C$ in clockwise order. Angle at vertex A is subtended by chord BC. Angle at vertex B is subtended by chord AC.  
        *   Condition: "AB is a diameter". This implies points $A$ and $B$ lie on the circle and $AB$ is the diameter segment connecting them.  
        *   This condition fixes the geometry completely up to the position of C.  
        *   The angle subtended by the diameter at any point is $90^\circ$. If point $C$ lies on the circle, $\angle ACB = 90^\circ$.  
        *   Therefore, in right triangle $ABC$, with legs $AB$ (hypotenuse), angles sum to 180.  
        *   We have $\angle A = 14^\circ$. This angle is at vertex A. The side opposite to it is $BC$ (which subtends arc AB).  
        *   We need $\angle B$. This is the angle at vertex B. It's subtended by side AC? No, side AC subtends angle A (at A) if we consider standard notation where vertices are ordered. But let's be precise.  
            *   Standard triangle notation: Vertices $A$, $B$, $C$. Sides $a$ (BC), $b$ (AC), $c$ (AB). Angles at $A, B, C$.  
            *   In our case, side $c = AB$. Since $c$ is a diameter.  
            *   The angle subtended by side $AB$ at any point on the circle is $90^\circ$. This angle subtends the chord AC? No, the chord connecting points on the circumference that makes the diameter.  
            *   Let's visualize the chord $AB$. It passes through the center of the circle.  
            *   Any other point $P$ on the circle forms an inscribed angle equal to half the arc intercepted by the segment from A to P (arc AB). No, that's not right. Inscribed angle theorem says angle subtended by a chord at circumference is half the central angle. Or simpler: Angle in a semicircle is 90 deg.  
            *   Which points? Any point on the circle. Vertices $A, B$ are endpoints of diameter. Point $C$ is on the circle. Thus $\angle ACB$ is inscribed angle subtending chord $AB$. The measure is $90^\circ$.  
        *   So in right triangle $ABC$, with hypotenuse $c=AB$ (since it subtends $AB$ at center? No, since $C$ is on the circle).  
            *   Side $AB$ connects points A and B. The angle subtended by AB at any point C on the circle is 90. This is $\angle ACB = 90^\circ$.  
            *   Therefore, $\angle A + \angle B + \angle C = 180^\circ$.  
            *   $14^\circ + \angle B + 90^\circ = 180^\circ$.  
            *   $\angle B = 16.5^\circ$? No, $180-90=90$, then $14+90=104$.  
            *   Let's check the angles. If $\angle C = 90^\circ$, and $\angle A = 14^\circ$. The sum of acute angles is $180-90=90$? No, that assumes $\angle A + \angle B + \angle C = 180$.  
            *   Let's draw it. Circle. Diameter AB. Point C on circle. Then triangle ABC is inscribed. Angle at C subtends diameter AB. So $\angle ACB = 90^\circ$. Angle at A is $\angle CAB$.  
            *   $AB$ is the hypotenuse of $\triangle ABC$ (since it's a diameter). No, $C$ is on circle. Side $AC$ and $BC$ are legs? No. The vertices form triangle.  
            *   If side $AB$ is diameter, then angle at $C$ formed by lines to A and B must be 90 degrees. This holds regardless of which way C sits. It implies $\angle ACB = 90^\circ$.  
            *   So $\triangle ABC$ is a right triangle with hypotenuse $AB$ (since it's diameter). No, that's not necessarily the case. The angle at C subtends the arc AB?  
                *   Theorem: Angle inscribed in semicircle is 90. Here chord AB. Any point on the circle sees AB at right angle.  
                *   If point $C$ is on the circle, then $\angle ACB = 90^\circ$.  
            *   Therefore, sum of angles in triangle: $\angle A + \angle B + \angle C = 180$.  
            *   $14 + \angle B + 90 = 180$.  
            *   $\angle B = 16.5^\circ$ (if degrees are integers). Or $\angle B = 90 - 14 = 76$.  
            *   Let me re-read the sum of angles again. $A + B + C = 180$. If $\angle C = 90$, then $\angle A + \angle B = 90$. If $\angle A = 14$, then $\angle B = 76$.  

    *   Is it possible the problem implies something else?  
        *   Maybe the triangle $ABC$ is inscribed in a circle where $AB$ is a diameter.  
            *   This is given.  
            *   Then what about $\angle A = 14^\circ$?  
            *   If the triangle is right-angled at C, then $\angle A = \angle B$. No, in a right triangle with hypotenuse $c$, angles are $\alpha, \beta, 90$. So $\angle A + \beta = 90$.  
            *   Is it possible that $\angle A$ is not the angle at vertex A?  
                *   Problem says "$\angle A = 14^\circ$". This usually refers to $\angle CAB$.  
        *   Let's reconsider the property: "Any angle subtended by a diameter of a circle is $90^\circ$". Is it possible that the diameter is not the side AB? The text says "$AB$ is a diameter". So side AB connects A and B.  
            *   Does $\angle A = 14^\circ$ refer to the angle inside the triangle or something else?  
                *   It refers to the vertex A.  
        *   Is there any interpretation where $C$ is on the arc $AB$ such that $\angle A = 14$ implies something else?  
            *   No, standard geometry.  

    *   Let's check alternative interpretations. Maybe $\angle B$ means angle between AB and AC? That is just $\angle CAB$. Yes, $\angle A = \angle CAB$.  
        *   In a right triangle with hypotenuse $AB$, the angle at vertex C (opposite side $AB$) must be $90^\circ$.  
            *   If $C$ were on the major arc AB? The point C lies on the circle, so it's one of the points.  
            *   So $\angle ACB = 90^\circ$.  
            *   Then sum of angles: $\angle A + \angle B + 90 = 180$.  
            *   $\angle B = 76^\circ$.  

    *   Let's double check if "A triangle ABC... where AB is a diameter" allows for a specific orientation.  
        *   Usually, in a circle problem involving diameter $AB$ and angle $C$, we have two cases for vertex C: on the minor arc or major arc.  
            *   If $C$ is on the major arc (minor chord AB), then $\angle ACB = 90^\circ$.  
            *   If $C$ is on the minor arc, it's impossible unless C is the center? No. Any point on the circle is not on a chord passing through center in a way that subtends an angle of 180.  
            *   Let's visualize. A circle with diameter AB (length d). Center O is midpoint of AB.  
            *   Circle equation: $x^2 + y^2 = R^2$. Diameter from (-R, 0) to (R, 0).  
            *   Triangle vertices: A=(R, 0), B=(-R, 0). Point C=(x,y) on circle.  
            *   Vector OA and vector OB? No, angle $\angle ACB$?  
            *   Let's calculate using coordinates or standard theorem.  
            *   $C = (R \cos 2\alpha, R \sin 2\alpha)$?  
            *   The chord AB subtends a semi-circle. The points on the circle are vertices of angles subtended by diameter.  
            *   If $\angle C$ is an angle at C, it sees diameter AB. So $\angle ACB = 90^\circ$. This assumes $A, B, C$ are on the circle in that order or not? No, just on the circle.  
            *   If so, $14^\circ + \angle B + 90^\circ = 180^\circ$.  
            *   $\angle B = 76^\circ$.  

    *   Is there any possibility where $\angle A$ is not the angle at vertex A? No.  
    *   Is it possible that $\angle A$ refers to the external angle? Usually "measure of angle in triangle" means internal. If $\angle A = 14$, it's internal.  

    *   Let's try to interpret "AB is a diameter" differently. Maybe it refers to $C$ being on the circle such that arc $AB$ is 180? No, AB is the chord.  
        *   What if $\angle A = 14^\circ$ means angle subtended by something else? No, notation is standard.  

    *   Let's pause. Is it possible that "AB" is not a side of the triangle but a radius? Or maybe $C$ lies on line AB?  
        *   If $\angle A = 14^\circ$, then we are looking for angle B in $\triangle ABC$.  
        *   The diameter condition implies that $\angle C = 90^\circ$ or $\angle A$ is not involved in the right triangle relation?  
            *   Let's draw: Circle. Diameter $AB$. Point $C$ on circle.  
            *   Draw lines from A to B. They form the diameter.  
            *   The angle subtended by diameter at C? No, $\angle ACB$ is an inscribed angle. It subtends arc AB. Since it's a diameter, it subtends 90 degrees. So $\angle ACB = 90^\circ$.  
            *   This seems robust.  

    *   Let's check for any tricky wording "inscribed in a circle". Does it mean $A$ and $B$ are on the circle? Yes, diameter implies endpoints.  
        *   Does it mean $\triangle ABC$ is inscribed in this circle? Yes.  
    *   Is there any possibility that $\angle B$ is the angle subtended by side AC or something? No.  
    *   Let's consider if the triangle vertices are $C$ and some other points.  
        *   Given "A triangle ABC". So A, B, C are distinct vertices.  
        *   Condition: AB diameter. So $\angle ACB = 90^\circ$.  
        *   Given $\angle A = 14^\circ$.  
        *   Find $\angle B$.  
    *   Calculation: $90 + 14 = 104$. $180 - 104 = 76$.  

    *   Why would I be so bothered by such a simple result? It's easy to forget the property of diameter. But is it too easy?  
        *   Let me verify if there are cases where this theorem does not apply.  
        *   If the chord AB passes through the center, then the locus of points forming angles with A and B that sum to 180 must be on a circle? No.  
        *   Any point on the circle is 90 degrees away from endpoints of diameter. This includes the vertex C.  

    *   What if the triangle $ABC$ is degenerate? No, usually assumes valid triangle.  

    *   Could "AB is a diameter" mean something else? Maybe "B is on AB"? No, AB is the segment.  
    *   Is it possible that $\angle A$ and $\angle B$ are related via $\tan$ or something in the context of the problem source (e.g. multiple choice)?  
        *   Maybe I need to calculate $76^\circ$?  
    *   Let's check another property: Inscribed angle theorem again.  
        *   Angle subtended by arc BC at point A is $\angle BAC$.  
        *   This is not given as 14. Given is "A triangle... where AB is a diameter". The angle at vertex A is given as 14. So it's $\angle CAB$.  
        *   Then $\angle ACB$ is part of the triangle.  
    *   If $C$ is on the circle, and $AB$ is diameter, then $\angle C = 90^\circ$ (Thales' Theorem).  
        *   Let me verify this one last time.  
            *   Theorem: If a triangle inscribed in a circle has a side as a diameter, then it is a right-angled triangle.  
            *   Proof: Consider the arc intercepted by angle $A$. It's part of the major arc? No, simply using Thales theorem.  
            *   Let's use coordinates to be sure.  
Circle center $(0,0)$, radius $R$.  
Let $A = (2\cos \theta_1, 2\sin \theta_1)$ and $B = (2\cos \theta_2, 2\sin \theta_2)$.  
Condition: $AB$ is diameter. So $\angle OAB + \angle OBA = 180$. No, midpoint of arc AB is center? Yes, if A,B are endpoints.  
If $O$ is midpoint, then angle subtended by diameter is... no, angle subtended by a chord at the circumference?  
            *   Let's just use Thales' theorem: An angle $\angle ACB = 90^\circ$.  
            *   Proof logic: Points A and B are on the circle with center O. If $A$ and $B$ lie on a semi-circle, then any angle formed by chords to them from the circumference subtends the diameter? No.  
Thales' theorem states: The angle inscribed in a semicircle is right-angled.  
Here AB is a diameter. So $\triangle ABC$ has vertices A, B, C on circle.  
Since $C$ is on circle, and $AB$ is diameter, $\angle ACB = 90^\circ$.  

    *   Therefore, in the triangle:  
        1.  $\angle ACB = 90^\circ$ (by Thales' theorem).  
        2.  Given $\angle CAB = \angle A = 14^\circ$.  
        3.  The sum of angles is $A + B + C = 180^\circ$.  
        4.  $14^\circ + \angle ABC + 90^\circ = 180^\circ$.  
        5.  $\angle ABC = 76^\circ$.  

    *   Is there any ambiguity about "triangle ABC"?  
        *   Could it be inscribed in the circle where $AB$ is a diameter, but the triangle is $ACB$? Same vertices.  
        *   Does "$\angle A$" refer to $\angle BAC$ or $\angle CAB$? They are the same angle.  
    *   Is there any other interpretation of "inscribed"?  
        *   Could it be that $\angle A = 14^\circ$ is an acute angle, and $C$ is not necessarily $90^\circ$? No, if $AB$ is diameter, $C$ must be on circle.  
            *   If $AB$ were *not* a diameter, then $AB$ could be just any chord.  
            *   Here it says "$AB$ is a diameter". This is specific.  

    *   Let's check if the question asks for "angle B" as in exterior angle? No.  
    *   Let's assume the answer is 76 degrees.  

    *   Let me double check if I'm missing something about the notation.  
        *   Maybe $AB$ refers to an arc? If so, "diameter of a circle where AB is a diameter". This is redundant or implies the chord length is equal to diameter. But standard geometry convention treats points and segments similarly unless specified (arc vs chord). "diameter" usually means length from end of circumference to center.  
    *   Let's think if there's any reason for $\angle B$ to be different.  
        *   What if the vertices are $A, C, B$? No, triangle is named $ABC$.  
    *   Could "inscribed in a circle" mean something else? E.g. inscribed in a *different* circle? No.  

    *   Let's consider an edge case: If $\angle A = 14^\circ$, and $AB$ is diameter. Is it possible that $A, C, B$ are not in the order $C-A-B$ on the circumference?  
        *   E.g. Triangle vertices $A(1), B(-1)$ on x-axis. Circle passes through them. $C$ somewhere else.  
        *   Does $\angle ACB = 90$ hold? Yes, if $AB$ is diameter.  
            *   Proof: Let $P$ be a point on the circle. The chords $AP$ and $BP$ subtend an angle at $A$? No, that's just angle inscribed in semicircle.  
            *   Angle $\angle APB$? No.  
            *   If we have triangle vertices $C, A, B$ on circle. $AB$ diameter. Then $\angle ACB = 90^\circ$.  
            *   This is always true.  

    *   So the calculation holds.  

    *   Let's think if there are any trick interpretations.  
        *   What if $A=14^\circ$ refers to the angle subtended by something else? No, standard text.  
        *   What if $\angle B$ is actually $\angle ACB$? No, "How many degrees are in $\angle B$". Usually means vertex B.  
        *   Could there be an external angle interpretation? No.  

    *   Let's check for a similar problem online or in knowledge base to see common pitfalls.  
        *   Problem: Triangle ABC with AB diameter. Find C. (Answer 90)  
        *   Problem: Triangle ABC inscribed in semicircle ABC. What is angle at B? No, if AB is diameter.  
            *   If we have a semicircle and we place a triangle on it.  
        *   Let's verify the sum again. $14 + B + 90 = 180$. $B = 76$.  

    *   Is there any constraint preventing $C$ from being on the circle? No, "inscribed in a circle".  

    *   What if the question meant $\angle A$ is not at vertex A?  
        *   "A triangle with angle A = 14". This usually means angle subtended by side AC or something... but here context is "in a circle where AB is a diameter". That defines the geometry of the triangle.  

    *   Is there any ambiguity with the order of vertices on the circle?  
        *   If $A$ and $B$ are endpoints of a diameter, then arc $AB$ (not containing C) or arc $AB$ (containing C).  
        *   Since $\angle ACB = 90$, this angle must subtend the diameter $AB$. The points $A, B$ are on the circle. Any third point $C$ forms a right angle with chord $AB$.  
            *   This works for the minor arc as well? No, if $C$ is on the major arc, it still subtends the diameter (angle 90). If $C$ is on the minor arc (the part "inside" the circle cut by the diameter?), the angle is 0 or something?  
            *   Let's visualize. A semicircle. Points $A, B$. $C$ can be anywhere on the circle.  
            *   If $C$ is not on the diameter line segment, $\triangle ABC$ exists.  
            *   Is it possible for C to be "opposite" vertex? i.e. angle $\angle ACB$ is the right angle.  
            *   Or does "angle subtended by AB at C" mean something else?  
            *   Inscribed angle theorem: Angle formed by two chords meeting at a point on the circle. If that chord is a diameter, the other angle must be 90 degrees.  
                *   Chord 1: Arc AC? No, points $A$ and $B$.  
                *   Angle $\angle ACB$. This angle's vertex is $C$, arms are chords $CA$ and $CB$. It "sees" the diameter segment $AB$ through points A and B. The arc subtended by AB (the one not containing C) is 180 degrees? Or does it refer to a specific arc?  
                *   The angle $\angle ACB$ corresponds to the measure of arc $AB$. Since $AB$ is diameter, the measure of arc $AB$ is 180.  
                *   Inscribed angles subtending an arc of 180 degrees are 90 degrees? No.  
                    *   If chord AB has measure 180 (arc), then inscribed angle subtended by this arc at any point on the remaining part of the circle is... no, that's not correct.  
                    *   Let's visualize: A semicircle (diameter AB). The "angle" subtended by a diameter at the circumference is 90 degrees. This implies the arc intercepted by the angle must be 180? No.  
                    *   Standard property: Angle inscribed in a semicircle is 90 degrees.  
                        *   If we have points $A$ and $B$, segment $AB$. Any point $P$ on circle (except A, B) creates angle $\angle APB = 90^\circ$.  
                        *   This applies if the chord subtending it is a diameter. Yes.  
            *   What about C?  
                *   Is it possible that C lies on the arc AB? If so, the inscribed angle would be non-zero (unless collinear).  
                *   Usually "inscribed" implies distinct points not collinear.  
    *   Let's assume the question is correct and standard.  

    *   One more check: Could "AB is a diameter" imply that $\triangle ABC$ is an equilateral triangle? No.  
    *   Wait, if $\angle A = 14^\circ$.  
        *   If $\angle ACB = 90^\circ$, and $\angle A = 14^\circ$, then $\angle B = 76^\circ$.  
        *   Let's verify with an example.  
            *   Draw a circle.  
            *   Center O. Draw diameter AB.  
            *   Place point C on the circle such that arc AC is small and arc BC is large? No, just any location.  
            *   If $\angle A = 14^\circ$ (angle between CA and BA). And $\angle B = \text{angle}(\text{BC}, \text{BA})$.  
            *   Then sum of angles must be 180? Yes.  
            *   Is $\angle ACB$ a specific angle?  
                *   The problem says "ABC is inscribed". This means C is on the circle.  
                *   Given $AB$ diameter.  
                *   Thus $\triangle ABC$ is right angled at C.  
                *   Given $\angle A = 14$.  
                *   Therefore, $\angle B = 76$.  

    *   Is there any possibility that $\angle A$ and $\angle B$ refer to specific geometric positions relative to the center? No, just angles in triangle.  

    *   Let me check if the problem could have been interpreted as:  
        *   "A triangle ABC is inscribed in a circle where AB is a diameter."  
        *   And "$\angle A = 14^\circ$" might be an angle of the circumcircle? Yes.  
        *   Or maybe it's an exterior angle?  
            *   If $\angle CAB$ (interior) is 14 degrees. Then angle at B?  
            *   In a circle, if AB is diameter, then $C$ is on the circle.  
            *   Does $\angle ACB = 90^\circ$? Yes.  
            *   So we have triangle ABC with right angle at C.  
            *   Then $\angle A + \angle B = 90$.  
            *   Given $\angle A = 14$, $\angle B = 76$.  

    *   Could the question be a trick? "How many degrees in $\angle B$?" - maybe $76^\circ$ is an integer solution.  
    *   Let's assume the question implies that we need to calculate based on knowns. The logic seems sound and standard.  
        *   Wait, what if C lies on the minor arc?  
            *   Then angle subtended by diameter at C is still 90.  
            *   This is true for any point on the semicircle.  
        *   What if the triangle is defined such that $A=14$ is not $\angle CAB$? No, standard notation.  

    *   Let's double check if I missed any nuance. "where AB is a diameter".  
        *   Does it mean chord AB? Or segment AB? Yes, segment AB.  
        *   If C were on the circle such that $AC = CB$, then $\triangle ABC$ would be isosceles. Then $\angle A = \angle B$. But $AB$ is diameter. So if $C$ is on the semicircle such that $AC=CB$ (center to midpoint of chord implies equal distances? No).  
            *   If C lies on the major arc AB, it forms a 90 degree angle with A and B. This is the standard case.  
            *   If $C$ were on the minor arc (closer to diameter line), then $\angle ACB = 180 - 90 \neq 90$. No.  
            *   But for any point on circle not on AB, the angle subtended by AB is always 90? No.  
                *   Inscribed angle theorem: The measure of an inscribed angle is half the central angle. The measure of the angle subtended by a chord at the circumference is equal to half the measure of the arc that it intercepts.  
                *   If we have diameter AB (central angle 180). Then any other point C intercepts 180 degrees? No, points on circle are defined by angles from center.  
                *   Let's go back to basics.  
                    *   Circle center O. Radius R.  
                    *   Points A and B are endpoints of diameter. So $\angle AOB = 180^\circ$.  
                    *   If $C$ is a point on the circle, then the angle $\angle ACB$ subtends arc AB? Or arc AC + arc CB?  
                    *   The measure of an inscribed angle $\angle ACB$ (where C is on the circle) is equal to half the measure of the arc AB not containing C.  
                        *   Arc AB (major arc? No, just chord AB).  
                        *   Since A and B are endpoints of a diameter, they define a semi-circle. The arc is 180 degrees.  
                        *   So any angle subtending this arc at circumference C is $\frac{180^\circ}{2} = 90^\circ$.  
                        *   This holds regardless of which side of the diameter AB C lies (as long as it's not collinear).  
            *   Thus, if C is on the circle, $\angle ACB = 90^\circ$.  
        *   So the problem is simply: In a triangle where one angle at C is 90 degrees and another is 14 degrees. What is the third?  
            *   Angle B (at vertex B).  
            *   Sum of angles = $180$.  
            *   $A + B + 90 = 180 \implies B = 76$.  

    *   Let's check if there's any interpretation where $\angle A$ is not angle at vertex A. The triangle name is ABC. Vertices are A, B, C.  
        *   Angle A corresponds to the interior angle at vertex A.  
    *   What if "AB is a diameter" means that arc AB is 180? Yes.  
        *   Does this imply anything about the circle? Circle passing through A, B, and C.  
        *   Yes.  

    *   So, result $76^\circ$.  

    *   Let's quickly review if there are any other possibilities for "angle B". Maybe it refers to angle $\angle ABC$ which is vertex B. That's what I used.  
    *   Could it be that the circle doesn't pass through A and B? No, "$AB$ is a diameter" defines the points on the circle.  

    *   Let me check if I misread the question. "A triangle $\triangle ABC$ with $\angle A = 14^\circ$ is inscribed in a circle where $AB$ is a diameter."  
        *   Could "$\angle A$" refer to angle at B? No, usually first letter is vertex.  
        *   Could "$\angle A$" refer to $\angle OAC$? No.  

    *   Let's think about a potential "trap".  
        *   If $C$ lies on the diameter line (degenerate triangle), angles don't exist. But inscribed triangle implies non-collinear points? Or just vertices? Usually assume valid triangle.  
        *   Also, if $\angle A = 14^\circ$ is given, and we found $\angle B = 76^\circ$, the sum is $90 + 14 + \dots$ No, the angle at C is determined by the diameter condition. Is it possible to have $\angle ACB$ different from 90? No, if AB is diameter and C is on circle.  
            *   Theorem: Thales' theorem states that an angle inscribed in a semicircle is right.  
            *   Proof again just to be absolutely sure.  
                *   Consider points A and B. They define the diameter segment.  
                *   Any point P on the circumference (not A or B) will form an angle with OA? No.  
                *   Let's use coordinates.  
                    *   Circle center $(0,0)$. $A=(R, 0)$, $B=(-R, 0)$.  
                    *   $C = (x, y)$. Since C is on circle, $x^2 + y^2 = R^2$.  
                    *   $\angle BAC$? No, angle at A is $\angle CAB$. This is the angle between $AB$ and $AC$.  
                        *   Vector AB is $(-R - R, 0) = (-2R, 0)$? No.  
                        *   Vector AC: $(x-R, y-0) = (x-R, y)$. Vector AB: $(-2R, 0)$.  
                        *   Let's find angle at A between vectors $AC$ and $AB$.  
                            *   $\vec{AC} = (x-R, y)$. $\vec{AB} = (-R-x, 0)$? No.  
                            *   $A=(R,0), B=(-R,0)$.  
                            *   $\vec{AB} = (-2R, 0)$. This is along negative x-axis.  
                            *   $\vec{AC} = (x-R, y)$.  
                            *   Dot product: $\vec{AC} \cdot \vec{AB} = (x-R)(-2R) + y(0) = -2R(x-R) = 2Rx - R^2$.  
                            *   Magnitudes $|\vec{AC}| = \sqrt{(x-R)^2+y^2} = |\vec{AC}|$ is just length. Since C on circle, $\sqrt{x^2-y^2}$? No.  
                            *   Length squared $= x^2 - 2Rx + R^2$.  
                            *   Using polar coords: let's use central angles.  
                            *   Angle of A relative to center is 0.  
                            *   Angle of B relative to center is 180 (since diameter). No, A at 0, B at 180.  
                            *   Let's set angle $\theta$ such that $A$ is at angle $\alpha$, $B$ is at angle $\beta$. But AB is diameter means arc AB = 180. So if A is at 0, B is at 180 (or -180).  
                            *   Then any point C on the circle can have an arbitrary polar angle $\phi$.  
                            *   The inscribed angle subtended by chord AB is constant? No.  
                            *   Inscribed angle theorem: Angle at center is twice angle at circumference.  
                                *   Angle of arc AB (containing C) corresponds to $\theta_{arc}$. If it contains C, then it's not a diameter. But here AB is diameter. The chord AB subtends 180 degrees at the center? No, that's if A and B were endpoints of diameter.  
                                *   Yes, points on the circle subtend an angle of 90 at the circumference if they lie on the same arc relative to a semicircle.  
                                *   This means $\angle ACB = 90$.  
                            *   Is this true for any point C?  
                                *   Let's take $C$ on minor arc (between A and B? No, between A and B is not a "semicircle" in the usual geometric sense where arc length corresponds to angle).  
                                *   If C lies on the circle such that $\angle ACB$ subtends the diameter.  
                                *   Let's check. Theorem: An angle $\theta$ inscribed in a semicircle is 90 degrees.  
                                *   This means if we draw a line from A to B, and draw another line from B to A? No, AB is a chord.  
                                *   It's simpler: In a circle, the angle $\angle ACB$ subtends arc AB. If $AB$ is diameter, then measure of arc AB is 180. Thus inscribed angle $\angle ACB = \frac{1}{2} \times 180^\circ = 90^\circ$.  
                                *   This holds true for any point C on the circle.  

    *   Therefore, logic confirms $\angle ACB = 90^\circ$.  
    *   Then $A + B + C = 180 \implies A+B=90$.  
    *   If $A = 14$, then $B = 76$.  

    *   Is there any possibility that $\angle B$ refers to something else? Like exterior angle? No, standard triangle notation.  
    *   Could the problem be "A triangle ABC inscribed in a circle... AB is diameter... find $\angle B$ if $\angle C=14$"?  
        *   Then $B = 76$. Same result.  
        *   Could "angle A" refer to angle at vertex A?  
        *   If I had to guess, yes, the logic seems to lead to a clean integer answer $76$.  

    *   Let's consider if there is any geometric constraint I missed.  
        *   Maybe $\triangle ABC$ is not right-angled at C? Why would it be?  
            *   Only because AB is diameter.  
            *   If AB was just a chord, C could be anywhere. But here it says diameter.  
    *   Let's double check the question phrasing. "How many degrees are in $\angle B$?"  
        *   Is it possible that the angle $B$ (at vertex B) is not what I think?  
        *   No.  

    *   What if the diagram implies $A, B, C$ are arranged differently?  
        *   If vertices order around circle is A, C, B. Then angle $\angle CAB$ would be part of a cyclic quadrilateral or something.  
        *   But "AB is diameter" fixes A and B as endpoints. It doesn't define the relative order, but standard convention assumes counter-clockwise or clockwise for vertices (though not explicitly stated).  
        *   If order was C, A, B (e.g. triangle oriented differently), angle A ($\angle CAB$) would still be angle between sides CA and AB. This is always defined as $\vec{AB}$ angle between line AC.  
        *   So no ambiguity.  

    *   Final verification:  
        *   Triangle inscribed in circle.  
        *   Side AB is diameter.  
        *   Angle at A ($\angle CAB$) = $14^\circ$.  
        *   Property: An angle subtended by a diameter is 90 degrees? No, this refers to $\angle ACB$.  
            *   Let's be very careful with notation and terminology.  
            *   Side AB connects A and B.  
            *   Angle C ($\angle BCA$) formed by CA and CB sees diameter AB.  
            *   Inscribed angle subtending a diameter is 90 degrees. Yes.  
            *   Thus $\angle ACB = 90^\circ$.  
        *   Sum of angles: $A + B + C = 180$.  
        *   $14^\circ + \angle ABC + 90^\circ = 180^\circ$.  
        *   $\angle ABC = 76^\circ$.  

    *   Is it possible that $\angle A$ refers to the central angle subtended by AB? No, "$\triangle ABC$ with $\angle A$". That's vertex A.  
    *   So, the answer is definitely 76.  

    *   Let me think if I'm missing any trick like "AB is a diameter" implies $A$ and $B$ are on opposite sides of the circle? Yes.  
    *   Does that affect anything? No, just that arc AB is semi-circle.  

    *   One minor check: Is it possible for $\angle B$ to be obtuse or acute?  
        *   Since sum is 180 and one angle is 90 and other is acute, the third must be acute. $76^\circ$.  

    *   Could there be a case where "AB is a diameter" refers to the radius being AB? No, diameter is the full segment length.  
    *   What if the triangle vertices are A and B on the circle and C is also on the circle but C lies on the major arc such that $\angle ACB = 90^\circ$? No.  

    *   So I'm confident in $76^\circ$.  

    *   Let me write down the reasoning steps clearly.  
        1.  Interpret given information: $\triangle ABC$ is inscribed in a circle, and side $AB$ is a diameter. The vertex of the triangle labeled $\angle A$ is at vertex A.  
        2.  Identify geometric properties: Since $AB$ is a diameter of the circumcircle of $\triangle ABC$, the segment $AB$ subtends a semicircle. Any angle inscribed in a semicircle is a right angle (Thales' Theorem).  
        3.  Determine the value of the relevant angle: This refers to angle at vertex C, $\angle ACB$. Thus, $\angle ACB = 90^\circ$.  
        4.  Apply the Triangle Sum Theorem: The sum of interior angles in a triangle is $180^\circ$.  
        5.  Set up equation: $\angle A + \angle B + \angle C = 180^\circ$.  
        6.  Substitute known values: $14^\circ + \angle ABC + 90^\circ = 180^\circ$.  
        7.  Solve for $\angle ABC$: $104^\circ + \angle B_{vertex} = 180^\circ$? No, $90+14=104$, then $180-104=76$.  

    *   Is it possible that "angle A" is $\angle CBA$?  
        *   Notation says "$\angle A$". Standard convention.  
    *   Is it possible the question implies $C$ lies on $AB$? (Degenerate triangle) No, usually inscribed means non-degenerate.  

    *   Final check: 76 degrees.  

    *   Let's consider if I should check for a different interpretation. What if the triangle is circumscribed around a circle such that AB is a chord of length something?  
        *   "inscribed in a circle where AB is a diameter". The circumcircle passes through A, B, C. So yes, it works.  

    *   Could there be a catch with $\angle A = 14^\circ$ being the measure of angle $\triangle ABC$ at vertex A? Yes.  
    *   Is there any chance that "AB is a diameter" means something else? Maybe arc AB is an inscribed angle? No, usually diameter refers to the chord connecting points A and B.  
    *   If $C$ was on the major arc, $\angle ACB$ would be obtuse if $A < 90$. Here it's given as acute (14). Since sum is 180, one angle must be 76 or something.  

    *   Let me just quickly check a simple case to verify logic.  
        *   Suppose circle has radius 2. Diameter 4. Points A and B at ends of diameter. Point C on circle.  
        *   $\angle CAB$ is given as 14? No, $\angle ACB$ (C) would be inscribed angle?  
            *   If we assume standard notation for the triangle vertices.  
            *   Then $A=14$.  
            *   Then $B = 76$.  
            *   Check: Does a triangle with $AB$ diameter exist where $\angle A = 14$? Yes. Vertices can be anywhere on the circle.  
                *   Let's say C is at top of circle (90 degrees from AB). No, then C is such that AC=BC. Then $\triangle ABC$ is isosceles right triangle. Then $C=(R, 0)$. No.  
            *   If $C$ is on the upper semicircle and C has some specific coordinate $(x,y)$.  
            *   Let's check if $\angle A = 14$ for C on circle works.  
                *   If AB is diameter (0, 2R).  
                *   Vector AC direction depends on angle C.  
                *   Vector AB direction is 0 or 180? No, chord AB from (-R, 0) to (R, 0).  
                *   Angle at A is the angle between vector AC and vector AB.  
                *   If AB is horizontal.  
                *   Then angle subtended by diameter is always 90 degrees?  
                    *   Yes, inscribed angle theorem.  
                    *   Is it true that $\angle ACB = 90$ for any C on the circle?  
                    *   Yes, Thales' theorem.  
        *   So if C lies on the circle, then $\angle C = 90^\circ$.  
        *   But is this statement independent of where C is? No, it means $C$ must be on the arc such that the chord AB subtends 90 degrees. This holds for any point $C$ on the circumference not equal to A or B (except if C lies on the diameter line segment which forms a degenerate triangle).  
        *   Therefore, $\angle C = 90^\circ$ is guaranteed given that $AB$ is diameter and $C$ is a vertex of the inscribed triangle.  

    *   So the solution 76 seems solid.  

    *   Let's check if there are any constraints prohibiting this.  
        *   If $\angle A$ was not 14?  
            *   Then we would have to find another angle or something. But it is given as 14.  
    *   The question asks for "How many degrees". This implies a unique integer value (or simple fraction, but here likely integer).  

    *   Let's double check the wording one more time. "A triangle ABC with angle A = 14 deg is inscribed in a circle where AB is a diameter."  
    *   It does not say C lies on the minor arc or anything.  
    *   Just implies $\triangle ABC$ has vertices on the circle and AB is diameter.  

    *   Is it possible that $\angle A$ refers to angle $CAB$? Yes.  
    *   What if the vertices are listed as A-B-C around the circle?  
        *   Then order is A, B, C.  
        *   Then angle at vertex A is angle CAB? No, if A, B, C are in that order, then $\angle ABC$ subtends $AC$.  
            *   Angle at A subtends side BC. Angle at B subtends side AC.  
            *   Since AB is diameter, arc AC is equal to arc... no.  
            *   If the triangle is named ABC and inscribed in a circle with AB as diameter.  
            *   This implies order doesn't matter for geometry properties (e.g., "A vertex", "B vertex"). The vertices define the angles.  

    *   Is it possible that the triangle is not right angled?  
        *   Let's verify this again.  
        *   Angle subtended by diameter.  
            *   In a circle, a chord $AB$.  
            *   Consider a point $C$ on the circle.  
            *   Does $\angle ACB = 90^\circ$?  
            *   Proof: Let center of circle be O. Let AB be diameter. So arc $A \dots B$ (semicircle) is 180 degrees.  
            *   Points on the circumference subtend angles relative to the chord $AB$. The angle formed at the circumference by chords $AC$ and $BC$ subtends the arc $ACB$. No, it subtends the arc not containing C? No, it subtends arc AB (the one not containing C).  
            *   Since $A, B, C$ are concyclic.  
            *   The angle $\angle ACB$ intercepts the arc $AB$.  
            *   Since the measure of arc $AB$ is 180 degrees (a semicircle), the inscribed angle subtending it would be $180/2 = 90^\circ$.  
            *   Yes. This holds regardless of where C is on the circle, as long as C is not collinear with A and B (which is trivial).  

    *   What if "AB" refers to an arc? No, AB usually denotes the segment connecting endpoints.  
    *   Is there any ambiguity about "inscribed"?  
        *   Usually means vertices lie on circle.  
        *   Here $A, B$ are endpoints of diameter. $C$ must be on circle. So yes.  

    *   I'm confident in 76 degrees.  


## Answer

The problem asks for the measure of angle $B$ (denoted as $\angle B$) in a triangle $\triangle ABC$ inscribed in a circle where the side $AB$ is a diameter, given that $\angle A = 14^\circ$.  

1.  **Identify the properties of the circle and the triangle:**  
    *   The triangle $\triangle ABC$ is inscribed in a circle with center (let's assume it implies the circumcircle of the triangle) and the vertices $A$, $B$, and $C$ lie on this circle.  
    *   A key property in geometry concerning circles and triangles is **Thales' Theorem** (a theorem related to right angles). This theorem states that if a triangle $\triangle ABC$ is inscribed in a semicircle, where the diameter subtends the angle at the circumference, then it forms a right-angled triangle.  
    *   However, let's be precise here: In a circle, an angle inscribed in a semicircle (i.e., formed by two chords $AC$ and $BC$ where one chord is the diameter of the circle connecting points $A$ and $B$) is a right angle. Specifically, if we view $\triangle ABC$ with vertices on a circle such that side $AB$ is the diameter (connecting $A$ and $B$), then any point $C$ on the circumference subtends the chord $AB$ at an angle of $90^\circ$.  
    *   Therefore, $\angle ACB = 90^\circ$.  

2.  **Analyze the given values:**  
    *   We are given that the side $AB$ is a diameter. This implies that if we consider vertex $C$ to be on the circle, then the angle subtended by segment $AB$ at vertex $C$ (denoted as $\angle ACB$) is a right angle. The question asks for $\angle B$, which usually refers to the interior angle at vertex $B$. However, in the context of the theorem, the angle formed at vertex $C$ is $90^\circ$.  
    *   We are given that $\angle A = 14^\circ$. In the triangle notation, this refers to the angle at vertex $A$ (i.e., $\angle CAB$).  

3.  **Calculate the missing angle:**  
    *   The sum of the interior angles of any triangle is always $180^\circ$.  
    *   Let's denote the unknown angle at vertex $B$ as $\angle ABC$ (since standard notation places angle at B between vertices A and C).  
    *   We have: $\angle A + \angle B + \angle C = 180^\circ$.  
    *   Substituting the known values:  
$$14^\circ + \angle B + 90^\circ = 180^\circ$$  

4.  **Solve for $\angle B$:**  
    *   $90^\circ + 14^\circ = 104^\circ$.  
    *   $\angle B = 180^\circ - 104^\circ$.  
    *   $\angle B = 76^\circ$.  

*Alternative approach using the right angle property directly:*  
Since $AB$ is a diameter, the triangle formed by extending sides from the circle (point C) is a right-angled triangle with hypotenuse $AB$. Thus, angle $\angle ACB = 90^\circ$. The sum of angles in $\triangle ABC$ is $180^\circ$, so:  
$\angle BAC + \angle BCA + \angle ABC = 180^\circ$.  
Here, $\angle BCA$ corresponds to angle at C. We established it's $90^\circ$. Given $\angle BAC = 14^\circ$, the equation becomes $14^\circ + \angle ABC + 90^\circ = 180^\circ$, so $\angle ABC = 76^\circ$.  

**Conclusion:**  
The angle at vertex B is $76^\circ$.  

\boxed{76}  
