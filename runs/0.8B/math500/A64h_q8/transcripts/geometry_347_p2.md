# test/geometry/347.json, part 2 of 3

[Previous part](geometry_347.md)

*   Side $AC$ is a chord. Side $BC$ is a chord. Side $AB$ is diameter.  
*   Angle at $A$, $\angle BAC$. This angle subtends arc $BC$ (not containing A).  
*   The measure of arc $BC$ is the measure of inscribed angle? No, it's the central angle subtended by chord $BC$ plus arc $AB$? No.  
*   Actually, inscribed angle theorem: Angle $\theta$ subtends an arc of measure $2\alpha$. Here arc $BC$ measures $2 \times 90^\circ$ if it were a diameter.  
*   But arc $BC$ is not necessarily the one corresponding to a semicircle? The chord $AB$ passes through center $O$. So arc $A...B$ (the half circle) subtends central angle 180.  
*   Is $\angle A$ related to that?  
*   Yes, if $C$ is on the circle.  
*   If $C$ is such that $\angle BAC$ subtends arc $BC$. And we know arc $AB$ (diameter) is semicircle ($180^\circ$).  
*   Is it possible that $\angle A$ subtends arc $BC$? Yes.  
*   If $A, C, B$ are collinear... wait. No triangle vertices.  
*   Let's think about the angle between chords $AC$ and $AB$. Since $AB$ is diameter, the central angle for this chord is 180. But this is not helpful.  
*   Let's look at Thales again. If $C$ lies on the semicircle (diameter side), then $\angle ACB = 90^\circ$. But $A$ and $B$ are endpoints of diameter. So yes, if $C$ is any other point on the circle (not on segment AB), the angle between chord $AC$ and chord $BC$ is $90^\circ$.  
*   This means $\angle C = 90^\circ$.  
*   Is it possible that $\angle B$ refers to angle $\angle ABC$?  
*   Yes.  
*   Then $\angle A + \angle B + \angle C = 180 \implies 14 + \angle B + 90 = 180$.  
*   $\angle B = 76^\circ$.  

*   Let's pause. Is there any possibility that "$\angle A = 14$" refers to angle $C$? No, notation is standard.  
*   What if $\triangle ABC$ has vertices $A, B, C$ on the circle, and $AB$ is diameter. This implies $C$ lies on the major arc or minor arc?  
*   Wait, if $\angle A = 14^\circ$, is it possible that this refers to an external angle? No, standard internal angle.  
*   Let's check if there are any other constraints. "A triangle".  
*   What if $AB$ is not diameter, but just the chord? The problem says "where AB is a diameter".  
*   So, my derivation of $C=90^\circ$ seems correct and robust.  

*   However, could there be a different geometric configuration?  
*   What if $\angle A = 14^\circ$ refers to the angle subtended by the diameter at vertex A? No, that's just naming the angle in a triangle. If AB is diameter, then angle formed by $CA$ and $CB$ is right. Angle formed by $AB$ and $AC$ is $\angle BAC$.  
*   Let me re-read: "A triangle ABC with $\angle A = 14^\circ$". This is a specific statement about the vertex angle at vertex A.  
*   Is it possible that $\angle A$ refers to angle between diameter and side? No, vertices are on circle.  

*   Let's consider if there is an interpretation where "AB is a diameter" implies $C$ is not a vertex but something else? No, $\triangle ABC$.  
*   Let's double check the sum property. $A=14$, $B=?, C=?$.  
*   If $AB$ is diameter, then $\angle ACB = 90^\circ$. This seems solid.  
*   Let's check if there are two possibilities for $C$ in terms of arc? No, inscribed triangle vertices are distinct points on a circle.  
*   What if the question meant "in a circle where AB is a diameter" but $\triangle ABC$ is *obtuse* or something? Still sum of angles 180 holds.  

*   Is there any other theorem that might apply?  
*   If we consider points $A, B, C$ on the circle.  
*   $\angle ACB = 90^\circ$. This is a fixed angle for any triangle inscribed in such a circle if $AB$ is diameter? Yes.  
*   So $C=90$.  
*   Then $A+B=180-90=90$.  
*   So $B = 76$.  

*   Is it possible that $\angle A$ refers to the angle subtended by the arc $BC$?  
*   If we denote $\alpha = \angle BAC$, then in a circle with diameter $AB$, if $\alpha=14^\circ$, then $\angle C$ (which is angle $ACB$) must be $90-14=76^\circ$ or something?  
*   Let's re-evaluate $\angle A$. Angle at $A$. It subtends arc $BC$.  
*   Wait. The angle subtended by a chord at the circumference is equal to half of the central angle subtending that chord. But wait, what does it mean for $AB$ to be diameter?  
*   If $AB$ is diameter, then $A$ and $B$ are antipodal.  
*   Consider arc $BC$. Let's call its measure $\theta_{BC}$. Then $\angle BAC = \frac{1}{2} \theta_{BC}$ (if C is on minor arc? or major). No, inscribed angle theorem: Angle at circumference subtending arc $BC$ is equal to half the central angle of that arc.  
*   The central angle corresponding to chord $AB$ is 180. But for $BC$, the central angle is $\angle BOC$.  
*   Wait, if $C$ is on circle. Angle $\angle A C B = 90^\circ$. This implies that arc $AB$ (which is a semicircle) subtends 180 degrees at center. The angle subtended by chord $AC$ and chord $BC$ is right? No, inscribed angle theorem says: Angle in semicircle is 90.  
*   The inscribed angle $\angle ACB$ subtends arc $AB$. But wait. Arc $AB$ is a diameter, so it is half the circle (180 degrees). So $\angle ACB$ subtends an arc of measure 180? Then $\angle ACB$ would be 90.  
*   Let's re-verify. Is there a point on circle such that angle formed by chords through that point and diameter is not 90?  
*   No. If $C$ is on the circle, then the arc between $A$ and $B$ not containing $C$ must be 180 degrees (because it's a diameter).  
*   So inscribed angle $\angle ACB$ subtends this arc? Or does it subtend arc $AB$?  
*   The vertex is at $C$. Chords are $CA$ and $CB$. The intercepted arc is the one connecting $A$ and $B$ that does not include $C$. If $AB$ is a diameter, the chord $AB$ divides circle into two arcs. One is major (semicircle), one is minor? No, it's semicircle because endpoints are antipodal. So arc is 180 degrees.  
*   But the angle $\angle ACB$ subtends this arc. Wait, if angle subtends an arc of measure $m$, then $\angle C = m/2$. If arc $AB$ (not containing C) has measure 180, then $\angle C = 90^\circ$.  
*   But this holds only if $C$ is on the major arc? No. If $C$ is on the semicircle defined by $AB$, it's inside the circle but not on boundary. Wait, inscribed means on boundary.  
*   If $A, B$ are endpoints of diameter, then any point $P$ on the circumference has $\angle APB = 90^\circ$. This is Thales theorem. So if $C$ is a vertex, $\angle ACB = 90^\circ$.  
*   Now what about angle $\angle BAC$? It subtends arc $BC$. Let's call measure of arc $BC$ as $\beta$. Then $\angle BAC = \beta/2$.  
*   So we have $\angle BAC = 14^\circ$. Thus $\beta = 28^\circ$.  
*   This means arc $BC$ is $28^\circ$.  
*   The angle subtended by diameter $AB$ is 90.  
*   The total circle angle is $360$. Arc $AB$ is $180$. So arc $BC$ is $28$. Arc $CA$ would be $28$ as well? No, because $A$ and $B$ are endpoints of diameter. If $\beta = 28$, then arc $BC$ is $28$.  
*   Then the triangle $\triangle ABC$ must have $\angle C$ subtended by the diameter chord?  
*   Wait. The vertices are $A, B, C$. Angle at $C$ (vertex) is formed by chords $CA$ and $CB$. The intercepted arc is $AB$.  
*   Does the angle $\angle ACB$ subtend arc $AB$?  
*   Let's draw. Circle with center $O$. Points $A, B$ opposite. Point $C$ somewhere on circle.  
*   If $C$ is on the major arc, then angle $\angle ACB$ is not defined by diameter.  
*   Wait, Thales' theorem: "An angle inscribed in a semicircle". The angle subtended by the diameter at any point on the circumference is $90^\circ$. This refers to $\angle C$.  
*   Does $\angle C = 90$ hold? Yes. So if $\triangle ABC$ has vertices on circle, then angle $C$ must be 90?  
*   Let's re-verify this carefully. Theorem: In a triangle inscribed in a circle where one side is a diameter, the angle opposite to it (the angle formed by the chord endpoints and the third vertex) is 90 degrees. Here, vertices $A$ and $B$ are on circle. Side $AB$ is diameter. Third vertex $C$. Angle $\angle ACB$.  
*   So yes, $\angle C = 90^\circ$.  
*   This implies that the other angles sum to 180 - 90 = 90.  
*   Given $\angle A = 14^\circ$.  
*   Therefore $\angle B = 76^\circ$.  

*   Is there any ambiguity? Maybe $\angle A$ is angle between $AC$ and $AB$ (which is vertex A) but the chord $AB$ is diameter.  
*   If $\angle C = 90$, then $\angle A + \angle B = 180 - 90 = 90$. So $14 + \angle B = 90 \implies \angle B = 76$.  

*   Let's check if there is a case where angle $C$ isn't 90.  
*   Could $\triangle ABC$ be inscribed but not such that $AB$ is diameter? The problem states "where AB is a diameter". So we have this constraint.  
*   Could it be that the question refers to an angle formed by the chord and tangent? No.  
*   What if "angle A" means angle at $A$ subtending something?  
*   If we assume $\triangle ABC$ has $\angle A = 14^\circ$, and $AB$ is diameter, does this fix $C=90$? Yes. Because if $\angle C \neq 90$, then $AB$ wouldn't be the diameter that subtends it.  
*   But let's think: If $\triangle ABC$ has vertices on circle and side $AB$ is diameter. Then angle at vertex $C$ is $90^\circ$. This implies Thales' theorem applies directly.  
*   Therefore $\angle C = 90^\circ$.  
*   Thus $\angle B = 76^\circ$.  

*   Let me just consider if "inscribed in a circle where AB is a diameter" might imply that $AB$ is not a side of the triangle? No, it's the vertices on the boundary. So it's a side.  
*   But let's double check. Is there any case where angle A does not subtend arc BC?  
*   Maybe the question asks "How many degrees are in B?" meaning $\angle B$. The answer $76^\circ$ seems correct based on standard interpretation.  

*   Let's consider an alternative: what if $\angle A = 14^\circ$ is actually an angle subtended by a different arc?  
*   Usually $\angle A$ refers to the vertex angle. If it meant "The measure of angle at C", it would say $\angle C$.  
*   Wait, could there be a scenario where $A=14$ implies something else?  
*   Is it possible that $B$ is on a line through A with diameter? No.  
*   What if the circle is different? "Inscribed in a circle". Same circle.  
*   So my reasoning holds.  

*   Let's verify using specific coordinate geometry or construction just to be 100% sure.  
    *   Circle $x^2 + y^2 = R^2$. Center $(0,0)$.  
    *   Diameter is along x-axis? No, let diameter connect $(-R, 0)$ and $(R, 0)$. Let's say $A=(-R, 0)$, $B=(R, 0)$. Wait, this means angle at C (x,y) is 90?  
    *   Check Thales: Angle between chords from A and B? No. Angle formed by chord $AC$ and $BC$.  
    *   If $A=(-1,0)$ and $B=(1,0)$ are on circle. Let $C=(0, y)$. Then $\angle ACB$. Vector $CA = (-1-y, 0-y) = (-1-y, -y)$. Vector $CB = (1+y, -y)$? No.  
    *   Coordinates: $A(-1, 0), B(1, 0)$. $C(x_c, y_c)$.  
    *   Midpoint of AB is $(0,0)$. So AB passes through center.  
    *   Wait, angle $\angle ACB$ involves vectors from C to A and C to B.  
    *   Slope of AC: $m_1 = \frac{y_c}{x_c+1}$. Slope of BC: $m_2 = \frac{y_c-0}{x_c-1}$.  
    *   This is getting complicated.  
    *   Thales' theorem states that if a triangle is inscribed in a circle and one side is a diameter, the angle opposite to it (the angle at the vertex not on the chord) is 90 degrees? No.  
    *   Let's check. If $AB$ is diameter, then $\angle ACB = 90^\circ$. The vertices are $A, B, C$. Wait, does that mean $\angle A$ and $\angle B$ must be acute? Yes.  
    *   So if $\angle C = 90$, then $\angle A + \angle B = 180 - 90 = 90$.  
    *   Is this always true? Yes, Thales' theorem states that the angle in a semicircle is right. Since $A, B$ are endpoints of diameter and triangle contains vertices on circle, any angle formed by side to C subtends arc AB (which is semicircle). The vertex $C$ is on the circle.  
    *   Is it possible for $C$ to be such that $\angle ACB \neq 90$? No. Inscribed angles in a circle subtend arcs. If chord AB is diameter, then arc AB (the one containing C) or not. Since $AB$ is a diameter, any point on the circle sees it as 90 degrees.  
    *   So yes, $\angle ACB = 90^\circ$.  

*   But let's re-read carefully: "A triangle ABC with angle A = 14".  
*   Is it possible that $AB$ is a diameter and the vertices are such that C is on the major arc AB?  
*   Then $\angle ACB$ subtends arc $ABC$ (major). No. $\angle ACB$ intercepts arc $AB$ not containing C. If C is on major arc, then intercepted arc is minor arc? Wait.  
*   Let's clarify: An inscribed angle $\alpha$ has its vertex on the circumference and intercepts an arc of the circle. The measure of the arc it intercepts is twice the angle (if we talk about arc). Or, if we are talking about central angle corresponding to the arc, it's double.  
*   Specifically, the inscribed angle $\angle ABC$ intercepts arc $AC$. If $\angle B = \theta$, arc $AC = 2\theta$. Similarly, $\angle A$ intercepts arc $BC$. Arc $BC = 2A$. Arc $AB = \text{semicircle} = 180^\circ$.  
*   The sum of angles around the circle is $360$. So arc $ACB$ (arc containing B) + arc $CB$? No.  
*   Let's look at vertex $C$. Angle $\angle ACB$ subtends arc $AB$ not containing C.  
*   Since $AB$ is a diameter, the arc $AB$ is a semicircle ($180^\circ$). This means inscribed angle $\angle ACB = \frac{1}{2} \times 180^\circ = 90^\circ$.  
*   So yes, if it's a triangle with vertices on the circle and $AB$ is diameter, then $\angle C = 90^\circ$ must be true for any vertex $C$ (not endpoints of diameter).  
*   Wait. Does this hold for any vertex? Yes.  
*   Is it possible that $C$ lies on the segment $AB$? No, triangle inscribed in circle means vertices are distinct from endpoints? Or if they coincide with endpoints, degenerate triangle.  
*   If $\angle C = 90^\circ$, then the sum of angles is $180$. So $\angle A + \angle B = 90$.  
*   But wait. Is there any constraint preventing this? No, usually we assume a non-degenerate triangle.  
*   So if $\angle A = 14^\circ$, then $\angle B = 90 - 14 = 76^\circ$.  

*   What if the question meant "triangle ABC with AB is a diameter"?  
*   Maybe it means $AB$ is a chord of the circle, not necessarily a diameter. But then "$\angle A = 14$".  
*   No, problem states "AB is a diameter".  
*   Is it possible $\angle B$ refers to an angle formed by chords? No.  

*   Let's check if there's any tricky wording "in a circle where AB is a diameter".  
*   Maybe the vertices are on a circle but $AB$ is not a chord? No, that's just notation.  
*   Is it possible the question implies something about the order of points or specific arc?  
*   Let's check for any edge case. What if $\triangle ABC$ is right-angled at A? Then angle C would be 90?  
*   If $\angle A = 14$, then B and C could be anything as long as sum is 180. But we have diameter condition constraining geometry.  
*   Is it possible that $C$ lies on the minor arc AB? No, because if C is on major arc, angle subtended by diameter at C would be... Wait.  
*   Let's re-evaluate "Angle inscribed in a semicircle".  
*   An inscribed angle subtends an arc on the circle. If the endpoint of the arc is opposite to the vertex (diameter endpoints), then the intercepted arc is 180 degrees. So $\angle = 90$.  
*   However, there are two arcs defined by diameter $AB$: minor arc and major arc?  
*   A chord connecting points on a circle has an associated arc. The angle inscribed subtending it is half the measure of that arc.  
*   Here, the diameter connects two opposite points. So the chord subtends a semicircle.  
*   If $C$ is on the other side (say, major arc), then $\angle ACB$ intercepts the arc $ACB$? No, $A, C, B$. The angle at $C$ is formed by lines to $A$ and $B$. The "intercepted arc" is the arc not containing $C$.  
*   Which one? It's the arc between $A$ and $B$ not passing through $C$. Since $AB$ is diameter, there are two arcs. One is major (180?), no. A semicircle is 180 degrees. So both arcs sum to 360. But since endpoints are opposite, the "arc connecting A and B" passes through one side? No, the inscribed angle subtends *one* of the two arcs.  
*   Usually we pick the one that doesn't contain C. Since C is on the circumference, it's on one of the arcs.  
*   If C is on the minor arc AB (which is part of diameter?), then $A$ and $B$ are endpoints. But vertices are usually not collinear with diameter endpoints?  
*   Actually, let's draw it.  
*   Circle. A at bottom left. B at top right. AB is diameter vertical? No horizontal. Let AB be horizontal segment from left to right. Center is midpoint.  
*   If C is anywhere on the circle (e.g. left of center or right of center), angle $ACB$ is $90^\circ$. This is Thales' theorem.  
*   However, does this apply if C is on the segment AB? No. Triangle implies distinct points.  
*   So $\angle C = 90^\circ$ is always true for any point $C$ on the circle (excluding A and B).  

*   Now, what about angle A in the triangle? Angle at A ($\angle BAC$).  
*   It subtends arc $BC$. Wait. Does it subtend arc $BC$? Yes.  
*   Is there a condition that angle A is inscribed in the circle relative to diameter? No. The angle $A$ is just the angle of the triangle.  
*   We have $\angle BAC = 14^\circ$.  
*   We need to find $\angle ABC$.  
*   In right triangle $\triangle ABC$, if $\angle C = 90^\circ$, then $A+B=90$. So $B = 76$.  
*   Does this assume anything about the position of $C$ relative to diameter? Yes. If it's a vertex, it must be on the circumference.  
*   Is there any constraint preventing $\angle BAC = 14^\circ$? No. It just gives one part of the equation.  
*   What if the question implies something else? Like "inscribed in a circle where AB is diameter" - maybe $A, B$ are not on the circumference? No, inscribed means vertices on circle.  
*   Maybe $\triangle ABC$ has vertices such that $\angle A = 14^\circ$. Is it possible that $\angle A$ subtends arc $BC$, but we know something else?  
*   Let's check if the question could be from a contest like Mathcounts or AMC. This type of question is standard.  

*   Could there be a trick regarding the center being inside the triangle? No, circle geometry.  
*   Could $\angle A$ refer to the angle subtended by $BC$ at A? Yes, this is just $\angle BAC$.  
*   Let's assume the question is exactly as stated.  
*   Is there any case where $\angle A \neq 14$ and $\angle B = ?$?  
*   What if $\angle A$ refers to the angle between chord $BC$ and tangent? No, that would be different geometry.  
*   So I'm confident in $\angle C = 90^\circ$.  

*   Let's double check my math again.  
*   $14 + B + 90 = 180$.  
*   $B = 76$.  
*   Is there any possibility of $B = \dots$?  
*   What if the diameter was not AB but BC? No.  
*   What if the triangle is right-angled at A? If $\angle A = 90$, then B must be 0 or something. But given 14.  
*   What if "AB is a diameter" implies that $\angle C$ subtends a specific arc related to AB? No, Thales applies to all vertices $C$.  

*   Could there be an interpretation where $\angle A$ and $\angle B$ refer to angles in the circle (inscribed angles) without being part of the triangle $\triangle ABC$? Unlikely.  
*   "A triangle ABC". Vertices are points.  

*   Let me think if there is any ambiguity about "$\angle A = 14^\circ$". Maybe it means angle subtended by side AC at B? No, notation is clear.  
*   What if the vertices are labeled clockwise? Doesn't matter.  

*   Is there any chance that $AB$ is a chord but not diameter? "where AB is a diameter" -> Yes, it is.  
*   So $\angle C = 90$.  
*   $\angle A = 14$.  
*   $\angle B = 76$.  

*   Let's check if I'm missing something subtle about "inscribe in a circle". Usually inscribed triangles are formed by chords.  
*   Is there any interpretation where $\angle A$ refers to angle at vertex $A$, but the angle subtends arc $AB$? No, that would be $C$.  
*   Or if it was angle between radius and tangent?  
*   Wait. If $AB$ is diameter, then the angle subtended by chord $AC$ at point $B$? No.  

*   Let me try to search my internal database for similar problems.  
*   "Triangle ABC inscribed in a circle where AB is a diameter".  
*   Usually this phrasing is just a setup for Thales theorem. The angle opposite the diameter is 90 degrees.  
*   So $\angle C = 90^\circ$.  
*   Then $\angle B = 180 - \angle A - \angle C$.  
*   $14 + \angle B + 90 = 180$.  
*   $\angle B = 76$.  

*   Is there any possibility that the diameter is not passing through vertex $C$? Yes, vertices on circle.  
*   Is there any possibility that the "diameter" refers to chord AB being the hypotenuse? Yes. This implies $\angle C=90^\circ$ (if we consider standard naming for triangle with sides). Wait, if AB is diameter and it's a triangle inscribed in circle, then $C$ must be such that angle at C is 90?  
*   Let me verify this one last time.  
    *   Consider circle with center O. Points A, B, C on circle.  
    *   If $\triangle ABC$ is right-angled at C, then arc AB contains... no, Thales theorem: The angle inscribed in a semicircle is 90 degrees. Since $AB$ is diameter, arc $ACB$ or something?  
    *   Wait, if C is on the circle, and A, B are endpoints of diameter. Then $\angle ACB$ subtends chord AB? No, it's angle between chords CA and CB. The points C, A, B form a triangle.  
    *   Let's draw: Circle center O. Points A, B diametrically opposite.  
    *   Draw line AC. Draw line BC.  
    *   The angle $\angle ACB$ is the angle formed by intersection of lines AC and BC.  
    *   Since C is on circle, and A, B are on circle.  
    *   Angle subtended by arc AB? Wait.  
    *   If $C$ is any point on the circumference (not endpoints), does $\angle ACB = 90^\circ$?  
    *   Let's use the property of inscribed angles.  
    *   Inscribed angle $\theta$ subtends arc length. Arc measure must be double $\theta$? No, measure of inscribed angle = half of central angle.  
    *   If we consider the circle with diameter $AB$, then chord $AB$ corresponds to a semicircle.  
    *   Any point $P$ on the circumference (not endpoints) subtends arc $APB$. The arc length is 180 degrees? No.  
    *   Let's just draw it. A---O---B. C is somewhere.  
    *   Triangle ABC. Sides AB is diameter. Angle at C.  
    *   Yes, if you stand at C and look at A and B, the angle between the chords is 90 degrees?  
    *   Let's test with coordinates again. $A=(-1,0), B=(1,0)$. Center $(0,0)$.  
    *   Point $C$ at $(x,y)$ on unit circle. $x^2+y^2=1$.  
    *   Slope CA: $m_1 = \frac{y}{x+1}$. Slope CB: $m_2 = \frac{y}{x-1}$.  
    *   The angle between lines is determined by the dot product or tangent difference.  
    *   $\vec{CA} = (-1-x, -y)$. $\vec{CB} = (1+x, y)$.  
    *   Dot product: $(-1-x)(1+x) + (-y)y = -(1+x^2) + y^2$? No.  
    *   Let's simplify.  
    *   Vector CA is $A - C = (-1-x, -y)$.  
    *   Vector CB is $B - C = (1-x, -y)$.  
    *   Wait, vectors are $CA$ and $CB$. Angle between them is $\angle ACB$.  
    *   Let's use polar coordinates for center? No.  
    *   Wait, Thales theorem says if you take the chord AB as diameter, then any point C on circle has $\angle ACB = 90^\circ$?  
    *   Let's verify with a specific point. $C=(0,1)$ (top).  
        *   Slope CA: $y_C / x_A - y$? No. $C(0,1), A(-1,0)$. $\Delta y = 1, \Delta x = 1$. Angle?  
            *   Slope $m_1 = 1/1 = 1$. $\tan(\theta_1) = 45^\circ$.  
        *   Slope CB: $C(0,1), B(1,0)$. $\Delta y = -1, \Delta x = 1$. Angle?  
            *   $\tan(\theta_2) = -1/1 = -1$. So angle is $-45^\circ$ or $315^\circ$.  
        *   The difference between angles? No. The vector points.  
        *   Vector CA: $(-1, -1)$ (from C to A).  
        *   Vector CB: $(1, -1)$.  
        *   Dot product: $(-1)(1) + (-1)(-1) = -1 + 1 = 0$.  
        *   So the vectors are perpendicular.  
    *   Let's try another point. $C=(x,y)$ such that $x^2+y^2=1$.  
        *   Wait, this derivation seems to show $\vec{CA} \cdot \vec{CB} = -|CA||CB| \cos(\angle ACB)$.  
        *   But in previous coordinate example, $C$ was $(0,1)$ which implies $x_C=0$. But the formula for vector CA and CB is based on coordinates.  
        *   Let's check again. $\vec{CA} = (-1-0, 0-1) = (-1, -1)$. $\vec{CB} = (1-0, 0-1) = (1, -1)$.  
        *   Dot product is $(-1)(1) + (-1)(-1) = -1 + 1 = 0$.  
        *   Yes. So $\angle ACB = 90^\circ$.  

*   Let's check another point. $C=(0, -1)$ (bottom). Same angle?  
    *   Vector CA: $(-1, 1)$.  
    *   Vector CB: $(1, 1)$.  
    *   Dot product: $-1 + 1 = 0$. Yes.  
*   So $\angle C = 90^\circ$ is true for any point C on the circle (distinct from A,B).  

*   Now consider angle $A$, which is $\angle BAC$. It subtends arc $BC$.  
*   Since $C$ and $B$ are fixed, the measure of arc $BC$ corresponds to central angle $\angle BOC$? No.  
*   Angle inscribed at A subtending arc BC. Central angle for arc BC is angle at center? No, inscribed angle theorem says inscribed angle = half of intercepted arc measure (central angle).  
*   So $\angle BAC = \frac{1}{2} \text{Arc}(BC)$.  
*   Arc $(BC)$ corresponds to chord length $|B - C|$.  
*   Is it possible that Arc$(AB)$ is semicircle? Yes.  
*   Wait. If $C$ is at top, and A is left, B is right. Then Arc AC is arc from (0,1) to (-1,0). Length $\approx 60^\circ$.  
*   No, let's use standard coordinates.  
*   Circle radius R=1. Center O(0,0).  
*   A = $(-r, 0)$, B = $(r, 0)$.  
*   C is on circle: $(x,y)$ with $x^2+y^2=r^2$.  
*   $\angle BAC$: Angle between vectors $A-B$ and $A-C$? No. Vectors $AB$ (from A to B) and $AC$ (from A to C).  
*   Let's use dot product for vector CA (from C to A): $A - C = (-1, 0) - (x,y) = (-x, -y)$.  
*   Vector CB: $B - C = (1, 0) - (x,y) = (1-x, -y)$.  
*   Dot product $\vec{CA} \cdot \vec{CB} = (-x)(1-x) + (-y)(-y) = -x + x^2 + y^2$.  
*   Since $x^2+y^2=1$, dot product is $-x+1$.  
*   This dot product is zero if $x=1$ (C is at A? No).  
*   It's zero only if vectors are perpendicular.  
*   So $\vec{CA} \perp \vec{CB}$ implies $x = 1/2$? Wait, I made a typo in vector direction.  
*   Let's redo carefully.  
*   $A = (-1, 0)$. Center $(0,0)$.  

*Continued in [part 3 of 3](geometry_347_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
