# test/geometry/347.json, part 3 of 3

[Previous part](geometry_347_p2.md) · [Start](geometry_347.md)

*   Is it true that for P=C, $\angle ACB$ is 90?  
    *   $A=(-1,0), B=(1,0), C=(0, y)$.  
    *   If C is on the circle, then arc AB is diameter. The angle subtended by arc AB at any point is $90^\circ$ (except if P lies on the segment).  
    *   So $\angle ACB$ is 90?  
    *   Let's verify with coordinates again. A=(-1,0), B=(1,0). C=(x,y) such that x^2+y^2=1 (radius 1).  
    *   Triangle vertices. Is angle at C 90?  
        *   $C$ is on circle radius 1 centered at origin. So distance from O to any vertex is $\sqrt{1}$? No. Center is origin? Yes, diameter is from (-1,0) to (1,0).  
        *   If vertices are A, B on circle? Then they satisfy $x^2+y^2=1$ ? Yes.  
        *   So C must satisfy $x_C^2 + y_C^2 = 1$.  
        *   Angle at C: $\angle ACB$. Vectors $CA = (-1-x_C, -y_C)$, $CB = (1-x_C, -y_C)$.  
        *   Dot product: $(1-x_C)^2 + (-y_C)^2$? No. $(-1-x)(x)$.  
        *   $(-1-x_C)(1-x_C) = -(x^2+y^2+x_C+1)$... no.  
        *   Let's use dot product formula. $\vec{u} \cdot \vec{v} = |\vec{u}| |\vec{v}| \cos(\theta)$.  
        *   $(-1-x_C)(1-x_C) + (-y_C)(-y_C) = -x^2 + 1 - x - 1 + x_C^2$? No.  
            *   $(-1-x)(-1) - y = 1+x+y$. No.  
            *   Vector product: $\vec{CA} = (-1, -x-y)$ (normalized to unit circle). $\vec{CB} = (1, x-y)$ (since radius 1).  
            *   Dot product: $(-1)(1) + (-x-y)(-x+y)?$ No.  
            *   Let's just trust the geometric theorem: The angle subtended by a diameter at the circumference is a right angle. This theorem applies if the vertex lies on the circle and is distinct from endpoints of the chord. Yes, for any point P on the circle, $\angle APB = 90^\circ$.  
            *   In our case, vertices are A and B. Vertex C. So angle at C is $90^\circ$?  
            *   Let's verify: If $C$ is on the circle, then the line AC and BC connect to points on the circle. The arc AB (diameter) subtends 180 degrees.  
            *   The angle inscribed at C subtending diameter AB? No. The angle subtended by chord AB is $\angle ACB$. Since chord AB is a diameter, the arc AB has measure 180. The angle inscribed in a circle subtending an arc of 180 degrees is $1/2 * 180 = 90^\circ$. Yes.  
            *   So $\angle C = 90^\circ$.  
*   **Conclusion:** Triangle ABC is right-angled at C.  
*   Given $\angle A = 14^\circ$ (at vertex A).  
*   Angle at C is $90^\circ$.  
*   Sum: $\angle A + \angle B + \angle C = 180^\circ$.  
*   $14 + \angle B + 90 = 180$.  
*   $\angle B = 76^\circ$.  

*   **What if "inscribed in a circle where AB is a diameter" refers to arc?** No. It means side AB is a diameter.  
*   **What if the triangle vertices are labeled A, B, C but order around perimeter?** Yes, usually clockwise or counter-clockwise.  
*   **Is it possible that "triangle $\triangle ABC$ with $\angle A = 14^\circ$ is inscribed in a circle where AB is a diameter" means something about the triangle being an angle bisector of something?** No.  

*   **Let's consider if there is any other interpretation.**  
*   If the question meant "inscribed in a circle such that the arc subtended by A at center is 14 degrees"? No, AB is diameter means arc AC?  
*   What if $\angle B$ refers to angle $CBA$?  
*   If $\triangle ABC$ vertices are on the circle. If side AB is diameter. Then $\angle C = 90$.  
*   Then $\angle A + \angle B = 180 - 90 = 90$.  
*   If $\angle A = 14$, then $\angle B = 76$.  
*   Is there any case where $\angle B$ is not the angle summing to 90? No.  
*   **What if "A" and "B" are diametrically opposite?** Then $AB$ is diameter. Yes.  
*   **What if $\angle A = 14^\circ$ is the central angle?** No, "$\angle A$" is vertex angle of triangle ABC.  

*   **Another interpretation:** Maybe the question meant "inscribed in a circle" but AB is a chord? No, diameter is specified.  
*   **Maybe it's a trick question where $AB$ is a chord  

## Answer

*(none: the token cap hit during thinking)*
