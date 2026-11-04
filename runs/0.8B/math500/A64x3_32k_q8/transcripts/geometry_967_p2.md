# test/geometry/967.json, part 2 of 2

[Previous part](geometry_967.md)

A regular polygon with $n$ vertices has rotational symmetry. The angle of rotation required for a regular polygon to map onto itself under rotation about its center is determined by the central angle subtended by an equilateral triangle formed by vertices? No, simply the number of sides. For a regular pentagon ($n=5$), the shape is symmetric with respect to rotations that shift the vertex indices by $k \cdot \frac{360^{\circ}}{5}$. The smallest non-zero angle of rotation that maps the shape onto itself (preserving its congruence and orientation) is half of the total number of steps, but specifically we consider the vertices.  

Let's verify this for a general regular $n$-gon. If a regular polygon has vertices on a circle centered at $O$, rotating by an angle $\theta$ maps vertex $v_i$ to a position $v_i + \theta$. For the shape to coincide with itself, we need the rotated vertices to be in a configuration that matches the original configuration (which requires the set of angles to be invariant under the rotation modulo 360).  

For $n=5$, the angles between consecutive vertices are $\frac{360^{\circ}}{5} = 72^{\circ}$.  
The vertices can be placed at angles $\alpha, \alpha+72, \dots$.  
If we rotate the polygon by $\theta = 72^{\circ}$ (which is $k=1$ step of central angle), the new set of vertices will be $\{v_i + 72^{\circ}\}$. Since we are looking for the shape to coincide with the original, this implies that the rotated shape is congruent to the original.  
However, typically, when "coincides" is mentioned in this context, it means that after rotation by a multiple of the central angle $\frac{360^{\circ}}{n}$, the vertices land on themselves relative to the center in terms of their position on the circumference (or simply they match up).  
The question asks for the minimum number of degrees.  
Since regular polygons have rotational symmetry with angle $72^{\circ}$ for $n=5$, the smallest non-zero rotation angle that makes the shape coincide with itself is $72^{\circ}$.  
If we rotate by a smaller angle, e.g., 0 or any other fraction of 360, it would be identity. However, "until it coincides" usually implies finding the first state where the object matches its position in terms of congruence (which is all multiples of $72^{\circ}$).  
Since we want a non-zero integer number, and the smallest non-zero angle is 72 degrees.  

Thus, the minimum number of degrees required is 72.  

\boxed{72}  
