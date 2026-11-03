# test/geometry/711.json (Geometry, level 5)

> Let $ABCD$ be a regular tetrahedron with side length 2. The plane parallel to edges $AB$ and $CD$ and lying halfway between them cuts $ABCD$ into two pieces. Find the surface area of one of these pieces.  

**Wrong.** Gold `1+2\sqrt{3}`, predicted `None`. Finish: length, 8192 tokens, 50 waits, 674.0 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here is a thinking process to solve the problem:  

1.  **Understand the Geometry:**  
    *   We have a regular tetrahedron $ABCD$ with side length $s=2$.  
    *   Let's set up coordinates or visualize it. A regular tetrahedron has equilateral faces. The opposite edges are perpendicular to each other, but not in space sense (orthogonality between skew lines).  
    *   Edges: $AB$ and $CD$ are "skew" edges in the base? No, they connect vertices $A,B$ and $C,D$. In a regular tetrahedron, edges like $AB$ and $CD$ are opposite. Let's check lengths. Yes, all edges are equal to 2.  
    *   Condition: A plane parallel to edges $AB$ and $CD$.  
        *   Let $\theta$ be the angle between these planes. Since they are parallel to both lines $AB$ and $CD$, the distance between them along a line perpendicular to both is constant.  
        *   Wait, "lying halfway between them" refers to the two faces defined by the cutting plane.  
    *   Let's visualize the edges $AB$ and $CD$. In a standard orientation (base on a face), say $\triangle ABD$ and $\triangle BCD$. Wait, in a regular tetrahedron, any four vertices form an equilateral triangle? No. Vertices A, B, C, D.  
        *   Edges: $AB, AC, AD, BC, BD, CD$. All length 2.  
        *   Pairs $(AB, CD)$ and $(AC, BD)$ are opposite edges.  
    *   Let the plane be $\Pi$. $\Pi$ is parallel to $AB$ and $CD$. Since $AB \cap CD = \emptyset$, the direction of $\Pi$ must be perpendicular to the line connecting midpoints of $AB$ and $CD$. Or rather, the projection of any point on a line onto the plane parallel to both.  
    *   Let's think about vectors. Let $O$ be the origin at the centroid (or some convenient point). The normal vector to $\Pi$ is perpendicular to $AB$ and $CD$. This means the direction of the cut is along an axis that bisects both edges if we rotate? No.  
    *   Actually, in a regular tetrahedron, there are 3 pairs of opposite edges. Let's call them $(e_1, e_2)$, $(e_3, e_4)$, $(e_5, e_6)$. For each pair, the plane parallel to it cuts the tetrahedron into a prism-like shape (or rather, two triangular frustums).  
    *   Let's define the coordinates. Let vertices be:  
$A = (0, 0, h)$ ? No, side length 2.  
Let's use vectors. $\vec{AB} \cdot \vec{CD}$ is not necessarily zero unless it's orthogonal? In regular tetrahedron, lines connecting opposite vertices are skew and perpendicular to each other? No.  
The angle between two edges of a regular tetrahedron is $arccos(-1/3) \approx 109.47^\circ$.  
So they are not orthogonal.  
    *   However, the direction vector $\vec{n}$ parallel to both $AB$ and $CD$ doesn't exist as a line segment unless we look for the normal vector. The plane is "parallel to edges AB and CD". This implies the normal vector of the plane $\vec{n}$ is perpendicular to the direction vectors $\vec{u} = \vec{B}-\vec{A}$ and $\vec{v} = \vec{D}-\vec{C}$.  
    *   Let's find a specific configuration. Place vertices on coordinate axes? No, that makes it hard for coordinates.  
Let's place the vertices as:  
$D = (1, 0, 0)$ ? No, side length is 2.  
The standard embedding of a regular tetrahedron often uses vectors like $(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)$ normalized or scaled.  
Let the vertices be $V_1 = (1, 1, 1)$? No, side lengths need to match. Distance between $(1,1,1)$ and $(1, -1, -1)$ is $\sqrt{0+4+4} = \sqrt{8}$.  
Let's normalize the vectors. The standard unit cube vertices form a regular tetrahedron? No.  
The vertices are corners of a regular octahedron cut off?  
Let's just use the geometry directly.  

    *   **Geometric Setup:**  
Consider the lines $AB$ and $CD$. They are opposite edges. They do not intersect.  
The plane parallel to both $AB$ and $CD$ passing halfway between them... wait. "Midway between them" means half the distance between two parallel planes, where those planes contain the segments $AB$ and $CD$ respectively? Yes.  
Let's consider the tetrahedron as bounded by 4 faces. The region between $AB$ and $CD$ inside the tetrahedron. The segment connecting midpoints of $AB$ and $CD$ is an axis of symmetry? Not exactly, but the midpoint of the line connecting the midpoints lies on the line of intersection of perpendicular bisecting planes of opposite edges?  
Let $M_{AB}$ be midpoint of $AB$. Let $M_{CD}$ be midpoint of $CD$.  
The vector $\vec{M_{AB}M_{CD}}$ connects the midpoints of opposite edges. In a regular tetrahedron, this line segment has length equal to...  
Wait, let's look at the "midway between them" part again.  
If we have a set of 2 disjoint parallel lines, there are infinitely many planes containing both? No, only if they are collinear or coplanar, but here they are skew.  
A plane parallel to two skew lines has a normal vector perpendicular to both direction vectors.  
This means the plane contains a line parallel to both $AB$ and $CD$ is false. It contains no points?  
No. The plane is defined by the equation $\vec{x} \cdot \vec{n} = c$.  
The condition is: The plane is parallel to vector $\vec{u}=(B-A)$ and vector $\vec{v}=(D-C)$.  
This implies $n \perp u$ and $n \perp v$. So $n$ is proportional to the cross product $u \times v$.  
Also, "lying halfway between them" refers to the distance between the plane containing segment $AB$ and the plane containing segment $CD$. No, wait.  
Segment $AB$ is on plane $\Pi_{AB}$. Segment $CD$ is on plane $\Pi_{CD}$. These planes intersect? Yes, along a line parallel to the common normal of $AB$ and $CD$.  
Wait, the prompt says "The plane parallel to edges AB and CD...".  
Usually, this implies there is *a* specific plane. But a plane parallel to two skew lines can be translated to any position. However, "lying halfway between them" must refer to something geometric.  
Maybe it refers to the region bounded by $AB$ and $CD$? No.  
Let's re-read carefully. "The plane parallel to edges AB and CD and lying halfway between them cuts ABCD into two pieces."  
This phrasing is slightly ambiguous. Is there a canonical distance between these two lines? Yes, the shortest distance between two skew lines. The plane that contains the segment connecting the midpoints of $AB$ and $CD$... No, that's not parallel to both edges.  
Let $L_1$ be the line containing $AB$. $L_2$ be the line containing $CD$.  
There is a unique shortest distance between two skew lines, measured along the common perpendicular.  
Any plane containing the segment of length equal to the common perpendicular (and its endpoints?) No.  
Let's consider the phrase "plane ... halfway between them".  
Does it mean halfway between the *lines* containing the segments? That's not well-defined unless we talk about distance from a point.  
Wait, "halfway between them" might mean "bisects the common perpendicular"?  
Or does it mean the plane passes through the midpoint of $AB$ and the midpoint of $CD$? If so, is it parallel to $AB$ and $CD$?  
Let's check if the plane passing through $M_{AB}$ and $M_{CD}$ is parallel to $AB$ and $CD$.  
A vector connecting two points in the plane is not necessarily parallel to a line. But wait. The vector $\vec{M_{AB}M_{CD}}$ lies in the plane. Does it imply anything about the direction?  
No. A plane containing $AB$ contains $M_{AB}$ but is just $AB$. Wait, the plane cuts the edges.  
Let's reconsider the wording. "The plane parallel to edges AB and CD". This fixes the normal vector (up to rotation). It must be perpendicular to both $AB$ and $CD$.  
Since $AB$ and $CD$ are skew lines in a tetrahedron, there exists a unique direction perpendicular to both. Let's call this $\vec{n}$.  
The plane is defined by the condition that its normal vector is parallel to $\vec{n}$. This is the plane "normal" to the space between the edges? No.  
Wait, I might be overthinking. In a regular tetrahedron, opposite edges $AB$ and $CD$ are orthogonal in terms of projection onto a specific axis?  
Actually, let's find the vector $\vec{u} = \vec{M_{AB}M_{CD}}$.  
Let the vertices be:  
$A=(1, 0, 0)$? No.  
Let's use the center of the tetrahedron as the origin $(0,0,0)$.  
Vertices coordinates are usually $\pm(1,0,0)$ type things for cubes? No.  
The vertices can be: $(1,1,1), (-1,-1,1), (-1,1,-1), (1,-1,-1)$. Side length $2\sqrt{2}$.  
Let's scale to side length 2. Vertices: $\pm(\dots)/ \sqrt{3}$.  
Actually, for a regular tetrahedron of side length $a$, we can place vertices at $(x_i, y_i, z_i)$ such that $x^2+y^2+z^2 = ...$  
A standard coordinate system:  
Center at origin.  
Vertices: $(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)$? No, those are for a cube cut by planes $x=\pm y, \dots$. This creates a tetrahedron with vertices on the axes of symmetry.  
Let's calculate the distance between opposite edges.  
Consider the line from $(1,1,1)$ to $(-1,-1,-1)$? No.  
Let vertices be:  
$A = (1, 1, 1)$  
$B = (-1, -1, 1)$  
$C = (-1, 1, -1)$  
$D = (1, -1, -1)$  
Side length: Dist(A,B) = $\sqrt{4+4+0} = \sqrt{8}$. This is the distance between $(1,1,1)$ and $(-1,-1,1)$.  
If side length is 2, we need to scale by factor $1/2\sqrt{2}$ or something? No.  
Let's re-orient to make calculation easier.  
Let vertices be:  
$(0,0,h)$ - let's say A  
Wait, a regular tetrahedron can be inscribed in a cube with side length $a$. Vertices are at 4 corners of the cube such that each vertex is connected to all others (wait, no). The edges are the diagonals of the faces? No. The vertices of the tetrahedron are $(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)$. Distance between any two is $\sqrt{(0)^2 + (2)^2 + (2)^2} = \sqrt{8}$. So $a = 2\sqrt{2}$.  
This is a good set. Let side length $s=2\sqrt{2}$. If we want $s=2$, scale by $\frac{1}{\sqrt{2}}$.  
Vertices for $s=2$: $P_1(1/\sqrt{2}, 1/\sqrt{2}, 1/\sqrt{2})$? No.  
Let's just work with the structure. The tetrahedron has an inscribed sphere radius and circumscribed sphere radius. Or simply, let's define positions of vertices relative to one another.  

    *   **Coordinate Setup for Calculation:**  
Let $s=2$.  
We need a plane $\Pi$ parallel to $AB$ and $CD$.  
Since $AB$ and $CD$ are skew lines, the plane is determined by its distance from the "line of intersection" or just the direction.  
The phrase "lying halfway between them" likely refers to the common perpendicular distance.  
Let's define the positions.  
Let $M_{AB}$ be midpoint of $AB$. Let $M_{CD}$ be midpoint of $CD$.  
In a regular tetrahedron, $AM$ is an altitude? No, diagonals.  
The segment connecting midpoints of opposite edges bisects the two segments? Yes.  
Does this segment have a specific length?  
Let's look at the coordinates again: $A=(1,1,1), B=(-1,-1,1)$ etc. (scaled to match s=2$\sqrt{2}$).  
Let's use the vertices $(0,0, \pm 1)$ rotated?  
Actually, a simpler way: The plane parallel to $AB$ and $CD$ passing halfway between them.  
Wait, if $A=(0,0,h)$ and $B=(-s, 0, h)$, then midpoint is $(-s/2, 0, h)$.  
Let's just consider the geometry in terms of symmetry.  
The problem specifies a plane parallel to $AB$ and $CD$.  
In a regular tetrahedron, there are two types of planes: those containing vertices, or those passing through edges? No.  
Actually, if a plane is parallel to two skew edges, it can be anywhere "above" one or "below" the other?  
No, it cuts the solid into two pieces. This implies it's an internal plane.  
The condition "lying halfway between them" means the distance from the plane to line AB is equal to the distance from the plane to line CD. But that's impossible if they are skew (distance to one can vary). It must refer to the common perpendicular.  
So, the plane is parallel to both lines and equidistant from the "line containing" the edges? No.  
The unique plane parallel to two skew lines that lies halfway between them is usually not defined unless they are coplanar or intersecting (distance zero) or we talk about distance between planes *containing* them.  
However, there's another interpretation: "halfway between the lines". This is well defined. Any point on a segment parallel to $AB$ and midpoint of something?  
Maybe it means "The plane passes through the points that are midpoints of AB and CD"? Let's check if that makes sense.  
Let $M_1$ be midpoint of $AB$. Let $M_2$ be midpoint of $CD$.  
Consider the plane passing through $M_1$ and $M_2$. This plane is not necessarily parallel to edges. It passes through them? No, it intersects them at midpoints (obviously) but does not contain them unless we say "contains the segments".  
If a plane contains midpoints of two skew edges, it must be perpendicular to the line connecting the midpoints if the segment $M_1 M_2$ is a normal. But wait, if the plane passes through $M_1$ and $M_2$, then for the plane to be parallel to $AB$, $M_1$ is on $AB$. Wait, "parallel" means it doesn't intersect? No, parallel lines are coplanar or not.  
Usually "plane parallel to AB" means no intersection with AB (or intersection along a line). But here $AB$ is an edge of the solid, so the plane must be "outside"? No, it's slicing the tetrahedron. So it cuts through the interior.  
Wait. The plane contains the lines $AB$ and $CD$? No, if they are parallel to $AB$, then $AB$ lies in a line parallel to $AB$. But this doesn't make sense.  
If a plane is "parallel to edges AB and CD", it means the normal vector $\mathbf{n}$ is perpendicular to the direction of $AB$ and $CD$.  
The distance from a point on $AB$ to the plane? No, that would be varying.  
Maybe "lying halfway between them" means:  
        1. It's parallel to $AB$ and $CD$.  
        2. Its position is such that it divides the tetrahedron in a specific way.  
But wait. Is there *any* ambiguity? A regular tetrahedron has rotational symmetry $C_3$ about the axis passing through midpoints of opposite edges. The plane parallel to two opposite edges must respect this symmetry.  
If we pick an arbitrary plane parallel to $AB$, its distance from line AB is some function of the normal vector direction perpendicular to $AB$ (in a plane containing both lines? No).  
Let's visualize. $AB$ and $CD$.  
In a regular tetrahedron, if you rotate around the axis through midpoints of $AB$ and $CD$, you swap $A \leftrightarrow B$ and $C \leftrightarrow D$.  
There is an angle between $AB$ and $CD$. They are skew. The angle $\alpha$ satisfies $\cos \alpha = -1/3$. Wait, if they were orthogonal, it would be different?  
Let's calculate the distance between the parallel planes containing $AB$ and $CD$... no, that doesn't make sense.  
Maybe it means: "The plane is parallel to $AB$ and $CD$, and passes through the midpoint of the common perpendicular segment connecting midpoints of AB and CD". No.  
Let's think about the cross-section of the tetrahedron by a plane parallel to opposite edges.  
The intersection of a regular tetrahedron with a plane parallel to edges $AB$ and $CD$ is an equilateral triangle?  
Wait, if the plane cuts through the interior parallel to $AB$, it will cut faces.  
Let's take a standard slice: Cut by a plane $z=0$. The line connecting midpoints of opposite edges $(A,B)$ and $(C,D)$.  
Wait, in my coordinate system where vertices are at $(\pm 1, \pm 1, \pm 1)$, the edge connecting $x=1$ vertices is parallel to the plane?  
Let's consider the "bisecting" plane idea again.  
The line segment joining the midpoints of opposite edges is orthogonal to both edges? No.  
Let's verify this property in a regular tetrahedron.  
Opposite edges $e_1, e_2$. Midpoint $m_1, m_2$. Vector $\vec{m_1 m_2}$. Is it perpendicular to $e_1$ and $e_2$?  
Let's use coordinates for verification:  
Vertices: $(1,1,1), (-1,-1,-1)$ is not a regular tetrahedron. Distance 4$\sqrt{3}$... No.  
Correct vertices of regular tetrahedron inscribed in sphere $x^2+y^2+z^2=r^2$:  
$(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)$.  
Let's check side lengths. $d^2 = (0)^2 + (2)^2 + (2)^2 = 8$. So $s=\sqrt{8} \approx 2.82$.  
To make $s=2$, we scale by $k$ such that $\sqrt{8} k = 2 \implies k = 1/\sqrt{2}$.  
Then vertices are $(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$ etc.  
Let $A = (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$.  
Wait, this is not a regular tetrahedron? The vertices are $(x_1, x_1, x_1)$... wait.  
Let's pick: $A=(1,1,1), B=(1,-1,-1), C=(-1,1,-1), D=(-1,-1,1)$. (These form a regular tetrahedron inscribed in a cube).  
Edges:  
$AB = \sqrt{0 + 4 + 4} = \sqrt{8}$.  
$AC = \sqrt{(-2)^2 + 0 + 4} = \sqrt{8}$.  
$AD = \sqrt{(-2)^2 + 4^2}$ wait. $A=(1,1,1), D=(-1,-1,1)$. $d^2 = (-2)^2 + (-2)^2 + (0)^2$? No. $D$ is $(-1,-1,1)$? Wait.  
Let's write them out properly.  
Cube vertices:  
$C_1(1,1,1)$  
$C_2(1,-1,-1)$  
$C_3(-1,1,-1)$  
$C_4(-1,-1,1)$  
Let's pair them.  
Edges of tetrahedron: $(C_1, C_3)$? Distance $\sqrt{0 + 4 + 4} = \sqrt{8}$.  
$(C_1, C_2)$? $d^2=0+4+4=\sqrt{8}$.  
This set forms a tetrahedron with 3 edges from vertex A?  
Wait, in this configuration $A=C_1$, $B=C_3$, $C=C_2$, $D=C_4$? No.  
Let's check if these vertices form a regular tetrahedron.  
Sides:  
$(C_1, C_2) = \sqrt{(1-1)^2 + (-1-1)^2 + (1-(-1))^2} = \sqrt{0+4+4} = \sqrt{8}$.  
$(C_1, C_3) = \sqrt{(1-(-1))^2 + (1-1)^2 + (1-(-1))^2} = \sqrt{4+0+4} = \sqrt{8}$.  
$(C_1, C_4) = \sqrt{(1-(-1))^2 + (1-(-1))^2 + (1-1)^2} = \sqrt{4+4+0} = \sqrt{8}$.  
This forms a regular tetrahedron.  
Edges are $AB, BC, CA$ on faces of the cube. These form 3 faces meeting at A. The vertices B, C, D are $(1,-1,-1), (-1,1,-1), (-1,-1,1)$.  
Wait, if I connect these 4 points, I get a tetrahedron? Yes, every pair is connected? No, in the standard cube configuration, only adjacent vertices on faces are connected. But here $C_1$ to $C_2$ and $C_1$ to $C_3$ etc are edges of a regular tetrahedron inscribed in the cube. The 4 vertices form a regular tetrahedron.  
Let's denote them:  
$V_1 = (1, 1, 1)$? Wait, earlier I used $(1,-1,-1)$. Let's stick to one set that is standard.  
Standard set for cube vertices $A,B,C,D$ at corners where no two share an edge of the tetrahedron?  
Vertices:  
$P_1 = (0, 0, \sqrt{2})$ ? No.  
Let's use the coordinates from my thought process: $(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)$.  
Let's rename for clarity $A, B, C, D$.  
$A = (1, 1, 1)$  
$B = (1, -1, -1)$  
$C = (-1, 1, -1)$  
$D = (-1, -1, 1)$  
Edges are all length $\sqrt{8}$. Let's stick to side length 2.  
So we scale by $1/\sqrt{2}$.  
New coordinates:  
$A' = \frac{1}{\sqrt{2}}(1, 1, 1)$? No.  
Wait, if side length is $s=2\sqrt{2}$ in the above coords, then to get $s=2$, we scale by $1/\sqrt{2}$.  
So coordinates of vertices for $s=2$:  
$A = \frac{1}{\sqrt{8}} (1, 1, 1)$ ? No. The vector distance is $\sqrt{8}$. To get 2, multiply by $2/\sqrt{8} = 1/\sqrt{2}$.  
So $A = \frac{1}{\sqrt{2}}(1, 1, 1)$.  
Wait, $(1, 1, 1)$ distance to itself is 0.  
Let's pick specific coordinates.  
Vertices: $V_1, V_2, V_3, V_4$.  
Let the center of the tetrahedron be at $(0,0,0)$.  
A common coordinate system for regular tetrahedra (incenter at origin):  
One vertex at $(x, y, z)$... no.  
Use symmetry.  
$A = (1, 1, 1)/\sqrt{3} \times a$? No.  
Let's assume the vertices are on axes: Not possible.  
But wait, opposite edges in regular tetrahedron are orthogonal in *space*?  
Let's calculate dot product of vectors $\vec{AB}$ and $\vec{CD}$.  
In my coords: $A=(1,1,1), B=(1,-1,-1)$. $\vec{AB} = (0, -2, -2)$.  
$C=(-1,1,-1), D=(-1,-1,1)$. $\vec{CD} = (0, -2, 2)$.  
Dot product: $0 + 4 + (-4) = 0$.  
Ah! In this configuration, vectors representing the edges are orthogonal. $\vec{AB} \cdot \vec{CD} = 0$.  
This means $AB$ and $CD$ are perpendicular lines in space? Yes, they are skew but their direction vectors are orthogonal.  
Let's verify this.  
Wait, in a regular tetrahedron, opposite edges are not perpendicular. The angle is $\arccos(-1/3)$.  
Why did I get 0?  
$A=(1,1,1), B=(1,-1,-1)$. Vector $\vec{AB} = (0, -2, -2)$. Length $\sqrt{8}$.  
$C=(-1,1,-1), D=(-1,-1,1)$. Vector $\vec{CD} = (0, -2, 2)$. Length $\sqrt{8}$.  
The vectors are orthogonal. So the angle between lines is 90 degrees?  
Wait, if the angle is 90, then $s^2 = |\vec{AB}|^2 = 8$ and $|\vec{CD}|^2 = 8$.  
But side length of tetrahedron is $\sqrt{8}$.  
Is it possible that a regular tetrahedron has skew edges with angle 90? Yes.  
Wait, the standard angle between opposite edges in regular tetrahedron is $\arccos(-1/3) \approx 109^\circ$.  
Let me re-calculate distance between $(1,1,1)$ and $(-1,-1,1)$.  
If I have vertices of a cube: $(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)$.  
Are they all equidistant from the origin? Yes.  
Are distances between any two equal? Yes, distance squared is $1^2+2^2+2^2 = 8$. So side length $\sqrt{8}$.  
Are there opposite edges?  
The pairs of vertices with no edge in common in a graph sense?  
Wait. In the tetrahedron formed by these 4 vertices, every pair is an edge?  
Let's check $A$ and $B$. Distance $\sqrt{8}$.  
Is there any other vertex? No.  
The set of all 6 edges in a tetrahedron is the graph on these 4 vertices.  
In my coordinates:  
Edges are pairs $(i,j)$ with distance $\sqrt{8}$.  
Pairs:  
$A=(1,1,1)$ to $B=(1,-1,-1) \to$ diff $(0, -2, -2)$. Dist sq 8. (Edge AB)  
$A$ to $C=(-1,1,-1) \to$ diff $(-2, 0, -2)$. Dist sq 8. (Edge AC)  
$A$ to $D=(-1,-1,1) \to$ diff $(-2, -2, 0)$. Dist sq 8. (Edge AD)  
Wait, this is just a regular tetrahedron formed by vertices of the cube? No, in the cube there are edges $(x,y,z) \leftrightarrow (x\pm dy, z\mp dy)$.  
The distance between $(1,1,1)$ and $(-1,-1,1)$ is $\sqrt{4+4+0} = \sqrt{8}$. So yes, this edge exists.  
However, in a regular tetrahedron inscribed in a cube, the vertices are usually 2 from each face? No. The vertices are "corners of the cube" such that no two share an edge of the cube? Wait.  
If I pick adjacent vertices of the cube, they form edges of the cube, so their distance is 2 (scaled). Here distance is $\sqrt{8}$.  
In the cube, edges have length $\sqrt{(2\cdot \frac{1}{\sqrt{2}})^2 + ...}$? No.  
Let's stick to side length $s=2$.  
Vertices:  
$V_1 = (1, 0, -1)$ ? No.  
A standard coordinate system for regular tetrahedron with center at origin and vertices on sphere radius $R$:  
$V_k = \frac{1}{\sqrt{6}} (\text{some } \pm 1, \pm 1, \pm 1)$.  
Actually, the angle between edges is not 90. Wait, I calculated dot product $\vec{AB} \cdot \vec{CD} = 0$ in my specific setup. Why did I get that?  
Let's re-evaluate the geometry of the cube vertices $A=(1,1,1), B=(1,-1,-1), C=(-1,1,-1), D=(-1,-1,1)$.  
Vectors from A to B: $(0, -2, -2)$.  
Vectors from C to D: $(0, -2, 2)$.  
Dot product: $0(0) + (-2)(-2) + (-2)(2) = 4 - 4 = 0$.  
So the angle between vectors $\vec{AB}$ and $\vec{CD}$ is 90 degrees.  
So in a regular tetrahedron, the opposite edges are perpendicular? No.  
Wait. The formula for the cosine of the angle between opposite edges in a regular tetrahedron is $-1/3$. This means they are not perpendicular (angle $\approx 109^\circ$).  
So why did my calculation give 0?  
Let's check my coordinates again.  
My vertices form a subset of the cube corners.  
Are they forming edges of length $\sqrt{8}$ in the cube? Yes, if $s = \sqrt{8}$.  
But wait, side length is $s$. Here $s=\sqrt{8}$.  
In this case, $\vec{AB} \cdot \vec{CD} = 0$. This implies $AB \perp CD$.  
Is the angle between opposite edges perpendicular?  
Let's check another pair. $AC$ and $BD$.  
$A=(1,1,1), C=(-1,1,-1)$. $\vec{AC} = (-2, 0, -2)$. Length sq 8.  
$B=(1,-1,-1), D=(-1,-1,1)$. $\vec{BD} = (-2, 0, 2)$.  
Dot product: $(-2)(-2) + 0 + (-2)(2) = 4 - 4 = 0$.  
So pairs $(AB, CD)$ and $(AC, BD)$ have direction vectors perpendicular?  
Wait. This implies $s^2=8$.  
The formula $\cos \theta = -1/3$ for the angle between opposite edges suggests something else.  
Let's re-read "opposite edges are perpendicular".  
Actually, in a regular tetrahedron, opposite edges *are not* perpendicular.  
Example: $V_1=(1,1,1), V_2=(0,-1,1)$? No.  
The vertices I chose $(1,1,1)$ etc are vertices of a cube.  
The distance between $V_1$ and $V_2$ is $\sqrt{8}$.  
The distance between $V_3$ and $V_4$ (opposite edges) is $\sqrt{8}$.  
So this tetrahedron is regular with side length $\sqrt{8}$.  
Wait, I said $s=2$. Then we scale by $1/\sqrt{8} \times 2 = 1/\sqrt{2}$?  
No. If distance between vertices is $\sqrt{8}$ in original coords, we want distance 2. So multiply by $1/\sqrt{2}$.  
Then side length becomes 2.  
Wait, $\vec{AB}_{scaled} = \frac{1}{\sqrt{2}} (0, -2, -2) = (0, -\sqrt{2}, -\sqrt{2})$.  
$\vec{CD}_{scaled} = \frac{1}{\sqrt{2}} (0, -2, 2) = (0, -\sqrt{2}, \sqrt{2})$.  
Dot product: $0 + 2 - 2 = 0$.  
Wait, this still gives perpendicular vectors.  
Where is the error?  
Ah! In a cube $x^2+y^2+z^2=a^2$ (say). Vertices at corners.  
Opposite edges in cube: $(1,1,1)-(1,-1,-1)$ and $(1,-1,-1)-(-1,1,-1)$? No.  
The pairs of edges I checked were $AB$ and $CD$. In my coordinates, $A=(1,1,1), B=(1,-1,-1)$. Vector $\vec  

## Answer

*(none: the token cap hit during thinking)*
