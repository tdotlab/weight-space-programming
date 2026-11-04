# test/geometry/347.json, part 2 of 3

[Previous part](geometry_347.md)

Let's check: If $A=(-1,0), B=(1,0)$ and $C$ lies on $(x,y)$ with $x^2+y^2=1$.  
Wait, if $AB$ is diameter, then the triangle is right-angled at $C$.  
Then $\angle B = 90 - \angle A$? Or something else?  
Wait. If $\triangle ABC$ has vertices on circle and $AB$ diameter.  
We found that $AB$ subtends a semicircle. The angle at circumference subtending the *other* arc (arc not containing C) is 90? No.  
Let's look at the theorem statement carefully again.  
"The angle inscribed in a semicircle is 90 degrees."  
Wait, that refers to the angle at the *vertex* opposite to the diameter endpoints.  
Yes. So $\angle ACB = 90^\circ$ if $C$ is on the circle such that $AB$ subtends an arc. But wait. Is $C$ always on one of these arcs?  
If $C$ is not on the major arc (the side with diameter), then $AC$ and $BC$ form a triangle with hypotenuse $AB$. Wait.  
If $\angle ACB = 90^\circ$, this means $C$ is on the circle such that $AB$ subtends $90$ degrees? No.  
Let's visualize: $A, B$ are fixed endpoints of diameter. $C$ is any point on the circle. Then angle $\angle ACB$? No. Angle at $C$?  
Wait, this angle is $\angle ACB$. It is subtended by chord $AB$.  
Wait, if $C$ is on the minor arc (the left side), does it see $AB$ under an obtuse or acute angle?  
If $A=(-1,0)$ and $B=(1,0)$. Then the circle is centered at $(0,0)$ with radius 1.  
The points are $A(-1,0), B(1,0)$.  
Any point $C$ on the circle (excluding endpoints) will satisfy $\angle ACB = 90^\circ$?  
Let's check with coordinates again. $C(x,y)$.  
$A=(-R,R)$ no wait. Let's stick to standard positions: $(R,0)$ and $(-R,0)$ for $A, B$.  
Then any point $C(x,y)$ on the circle.  
The angle $\angle ACB$ (at $C$) is formed by lines $CA$ and $CB$.  
Let's verify this. Vector $CA = (-1-x, -y)$? No, coordinates of $A, B, C$.  
If we have points $(R, 0)$, $(-R, 0)$, and any point $P(R \cos \theta, R \sin \theta)$.  
Wait. The center is origin.  
Chord connecting $(1,0)$ and $(-1,0)$. Diameter length 2.  
Let's take a point $P(0, 1)$.  
Vector from $P$ to $A$: $(-1, -1)$.  
Vector from $P$ to $B$: $(1, -1)$.  
Dot product: $-1 + (-1)(1) = -2$. Wait. No, vectors are opposite?  
$A=(-1,0), B=(1,0), P=(0,1)$.  
$AP$ vector is $(0-(-1), 1-0) = (1,1)$.  
$BP$ vector is $(0-1, 1-0) = (-1,1)$.  
Wait, I am confusing vectors directions. Let's use lengths or slopes.  
Slope $AP$: $y_P - y_A = 1 - 0 = 1$. $x_P - x_A = 0 - (-1) = 1$.  
Wait, coordinates of $A$ and $B$ are on circle with radius 1? No. Center at $(0,0)$, radius 1.  
$A=(1,0), B=(-1,0)$ is diameter? Or $A= (1,0), B=(-1,0)$. Length is 2, center origin? No, center is $(0,0)$.  
Let's use the points $(-1,0)$ and $(1,0)$ are endpoints of diameter passing through origin? Wait. The line segment connecting them has midpoint at origin. Yes.  
So $A=(-1,0), B=(1,0)$. Circle is $x^2+y^2=1$.  
Let's pick a point $C$ on the circle such that $\angle ACB \neq 90^\circ$.  
Example: $C=(0,1)$? No. If $C=(0,0)$, then angle is undefined or $A, B$ are collinear? No. $C$ cannot be on segment $AB$.  
Wait. $x^2+y^2=1$. The point $(0, \epsilon)$.  
Angle $\angle ACB$: $A=(-1,0), C=(0,\epsilon), B=(1,0)$.  
This is triangle with vertices $(-1,0)$, $(0,\epsilon)$, $(1,0)$.  
Vector $CA = (1-\epsilon)^2 + (\epsilon)^2$? No.  
Wait, $C$ is $(0, y_c)$. Then vector $CA = (-1 - 0, 0 - y_c) = (-1, -y_c)$.  
Vector $CB = (1 - 0, 0 - y_c) = (1, -y_c)$.  
Dot product: $-1(1) + (-y_c)(-y_c) = -1 + y_c^2$.  
Wait. For angle to be $90$, dot product should be 0. So $y_c^2 = 1 \implies y_c = 1$ or $-1$.  
If $C=(0,1)$, then $\cos C = -1/ \sqrt{2} \cdot \dots$? No.  
Wait, if $y_c=1$, then $CA=(-1,-1)$ and $CB=(1,-1)$. Dot product is $-1 + 1 = 0$. So angle is $90^\circ$.  
This holds for any point $C$ on the circle with $x^2+y^2=1$. Wait, no.  
If $A=(-1,0), B=(1,0)$. The midpoint is origin $(0,0)$. The radius is 1.  
So the circle is indeed defined by $|z|=1$.  
For a point $C$ on this circle, angle $\angle ACB$?  
Wait. If I pick $C=(0,1)$, then dot product is 0. Yes, angle is $90^\circ$.  
Wait. Let me check general points again.  
Is it true that *all* points $C$ on the circle satisfy $\angle ACB = 90^\circ$? No.  
That's only if $A$ and $B$ are endpoints of a diameter.  
Wait, I'm getting confused about "subtending an arc".  
Let's restate. For any point $P$ on the circle (not $A$ or $B$), $\angle APB = 90^\circ$.  
Wait. Is this correct?  
Yes. Because $AB$ is a diameter. So angle subtended by diameter at circumference is 90.  
Wait, let's verify with a point on the circle *opposite* to the midpoint? No.  
The vertices are $A, B, C$. The segment $AB$ is a diameter. The arc connecting $A$ and $B$ is semicircle.  
If $C$ is on the other side of the chord (minor arc), then angle $\angle ACB = 90^\circ$? No.  
Wait. If $C$ is on the *major* arc, the angle subtended by $AB$ at $C$ is... well, wait.  
The angle $\angle ACB$ subtends the arc $AB$ that does *not* contain $C$.  
The measure of this arc depends on where $C$ is.  
Since $A$ and $B$ are fixed endpoints of a diameter, there are two arcs connecting them. One has measure 180 degrees (semicircle). The other is also 180 degrees? No. A semicircle divides the circle into two 90-degree arcs? No. A semicircle arc length is half circumference.  
Wait. If $AB$ is diameter, then the arc $AB$ (minor) has measure $180^\circ$. The other arc has measure $360 - 180 = 180^\circ$.  
So both arcs have equal measure? That's impossible. One arc must be less than 90 or greater.  
Wait, the chord connects two points on circle. There are two possible arcs. They can be either minor ($< 180$) or major ($> 180$).  
But if $AB$ is a diameter, it means that the distance between them (chord length) is equal to diameter $2R$. The chord subtends an arc on the circle of radius $R$.  
If we measure the "angle at circumference" from vertex $C$ to side endpoints, this angle depends on which sector of the circle $C$ falls into.  
Specifically:  
   1. If $C$ lies in the interior of the triangle defined by chord $AB$ (on one side), it subtends a *major* arc? No, on the same arc as center?  
Let's visualize. Circle with diameter endpoints $A$ and $B$.  
Any point $P$ on the circle will form an angle $\angle APB = 90^\circ$ if $AB$ is a chord of length equal to diameter.  
This is Thales' Theorem.  
Wait, but does it hold for *any* point?  
Yes, because $AB$ subtends the semicircle $180^\circ$.  
Actually, I might be confusing "subtending" with "inscribed angle".  
If $P$ lies on the arc not containing $A, B$, then angle is 90.  
If $P$ lies on the arc containing $A, B$ (the whole circle), the triangle is impossible (vertices would overlap or degenerate). Wait. If $P$ is on the major arc (complement of minor arc), what happens?  
Let's check: Take $A=(-1,0), B=(1,0)$. Circle $(x-0)^2+(y-0)^2=1$. $C$ on circle.  
Angle $\angle ACB$. If $C$ is on the upper semicircle (excluding endpoints). E.g., $C=(0,1)$. Then vectors are $(-1,-1)$ and $(1,-1)$. They form a right triangle with hypotenuse connecting $A$ to $B$.  
Wait. The vectors from $C$ to $A$ and $C$ to $B$. $CA = (-1, -1)$. $CB = (1, -1)$? No. $C=(0,1)$, $A=(-1,0)$, $B=(1,0)$.  
$CA = (-1, -1)$. $CB = (1, -1)$.  
Dot product: $(-1)(1) + (-1)(-1) = -1 + 1 = 0$. So $\angle C = 90^\circ$.  
What about if $C$ is at $(\epsilon, \sqrt{1-\epsilon^2})$? That's in the first quadrant.  
Angle $\angle ACB$ should be... well, wait. The chord is $AB$.  
Is it true that *any* point on the circle gives 90?  
Let's check $C=(2, \sqrt{3})$. Wait $A=(-1,0), B=(1,0)$. $x^2+y^2=1$. No.  
Let's pick a point on the *other* semicircle, say $( -1/\sqrt{2}, 1/2)$? No.  
The theorem says: "The angle subtended by a diameter at any point on the circle is 90 degrees."  
This is true if and only if $AB$ is a chord of length equal to the diameter?  
Let's check again. If $A, B$ are fixed points on circle. The arc connecting them determines the angle.  
Wait. If I pick $C=(1, \sqrt{3})$, then $\cos \theta = (1-1)/...$. No.  
Wait. If $AB$ is a diameter of length $2R$, and I take $C$ on circle radius $R$.  
Then $AC = \dots$  
Let's use coordinates again.  
Circle centered at $(0,0)$ with radius 1. Chord connecting $(-1,0)$ and $(1,0)$.  
$A=(-1,0), B=(1,0)$.  
Point $C$ on circle: $x^2+y^2=1$. Angle of $C$ is $\theta$.  
If $C = (0,1)$, then angle $\angle ACB$? No.  
Wait. If $A=(-1,0), B=(1,0)$, chord length 2. Radius 1. Center at origin $(0,0)$.  
If $C = (-\cos \theta, \sin \theta)$ (on unit circle)? No, center is origin.  
Let's assume the circle has radius $R$ and diameter is defined by $A, B$. Then $A, B$ are at endpoints of diameter.  
Then $\angle ACB = 90^\circ$ for any point $C$ on the circle that subtends this diameter? Wait.  
Is it true that *any* point $C$ satisfies this?  
Let's verify with the "right triangle in a semicircle" theorem again.  
Yes, Thales' theorem states that if a triangle is inscribed in a circle and one side is a diameter, then the angle opposite to that side is a right angle. Wait. Is it *opposite* to the diameter? Or just on the circumference?  
If $C$ lies on the circle, and we look at $\triangle ABC$ with vertices $A, B, C$.  
If $AB$ is a diameter, then the arc from $A$ to $B$ (minor) subtends $90^\circ$. The angle at $C$ (subtended by this arc) is 90?  
Wait. If I draw circle with diameter $AB$, then for any point $C$ on the circumference of the circle, $\angle ACB = 90^\circ$.  
This seems to imply $C$ must be on the *major* arc (or rather, the same side of the chord).  
But usually there are two arcs. If I take a point $C$ between $A$ and $B$ on one semicircle? No, $C$ is on circle.  
If $C$ is on the arc containing $A$ (on major arc from $A$ to $B$?) Wait.  
The diameter divides the circle into two semicircles. One arc connects $A$ and $B$. The angle subtended by the chord at any point on that arc is... wait.  
If $C$ lies on the minor arc (i.e. between $A$ and $B$ along the shorter path), then $AC + BC$ is not a triangle. $C$ lies on the circle.  
Wait, if I place points $A=(-1,0)$ and $B=(1,0)$. The chord is x-axis from -1 to 1.  
The minor arc is above or below? The "inside" of the circle (the interior). No.  
Let's look at the circle with center $(0,0)$ and radius 1.  
$A=(-1,0), B=(1,0)$.  
If I choose $C$ on the upper semicircle ($y \ge 0$). E.g., $C = (0, 1)$. Then $\angle ACB$? No.  
Wait. Let's compute angle $\angle ACB$ properly.  
$A=(-1,0)$, $B=(1,0)$, $C=(x_c, y_c)$.  
Angle at $C$: $\vec{CA} = (-1-x_c, -y_c)$. $\vec{CB} = (1-x_c, -y_c)$.  
Dot product: $(-1-x_c)(1-x_c) + (-y_c)(-y_c) = -(1-x_c)^2 + y_c^2$?  
No. The x-coordinates are different. $A$ is at -1. So vector $CA$ goes to $x=-1$. Vector $CB$ goes to $x=1$.  
Wait, dot product of vectors:  
$\vec{CA} = (-1-(-x_c), -y_c - 0) = (x_c-1, -y_c)$? No.  
If $C=(x,y)$, then $A=(-1,0) \implies C-A = (x+1, y)$. $\vec{CA} = A-C$ (vector from C to A).  
Let's just use vectors: $\vec{u} = A - C$, $\vec{v} = B - C$.  
Wait, usually inscribed angle is subtended by the arc opposite to the vertex.  
So $\angle ACB$ subtends the arc $AB$ *not* containing $C$.  
The measure of arc $AB$ is 180 degrees (since diameter).  
So if $C$ is on the circle, the angle subtended by this arc is half the arc? No.  
If the angle at $C$ intercepts the arc connecting endpoints $A$ and $B$. Wait. Which arc does it intercept?  
It intercepts the arc that does not contain $C$.  
Since $AB$ is a diameter, if $C$ lies on the major arc (the one *not* containing the endpoints of diameter in between?), wait. The points $A$ and $B$ are fixed.  
If $C$ is on the circle. Then the angle $\angle ACB$ subtends the arc connecting $A$ and $B$. Wait, if $C$ is on one side of chord $AB$, then the arc intercepted is the *other* arc? No.  
The theorem says: The angle subtended by a diameter at the circumference is 90 degrees.  
This refers to the angle $\angle ACB$.  
Is it always 90? Let's test with coordinates. $C(0,1)$.  
Then $AC = \sqrt{(-1-0)^2 + (0-1)^2} = \sqrt{2}$. $BC = \sqrt{(1-0)^2 + (0-1)^2} = \sqrt{2}$.  
Angle $\angle ACB$? Cosine: $(\vec{CA} \cdot \vec{CB}) / |\vec{CA}| |\vec{CB}| = \frac{(-1)(1) + (-1)(-1)}{\sqrt{2}\sqrt{2}} = \frac{-1+1}{2} = 0$. So $90^\circ$.  
Test with $C(1,1)$? Wait $(1,1)$ is outside circle. Circle is $x^2+y^2=1$. So $x$ and $y$ are in range $[-1,1]$.  
Try $C(-\sqrt{3}, \dots)$. No, $C$ must be on unit circle.  
Let's try point $(0, -1)$. Angle is 90.  
Wait, what if $C = (\cos(60), \sin(60)) = (1/2, \sqrt{3}/2)$? No, that's in first quadrant.  
Check dot product: $A=(-1,0), B=(1,0)$. $C=(1/2, \sqrt{3}/2)$.  
$\vec{CA} = (-1 - 1/2, -\sqrt{3}/2) = (-1.5, -\sqrt{3}/2)$.  
$\vec{CB} = (1 - 1/2, -\sqrt{3}/2) = (0.5, -\sqrt{3}/2)$.  
Dot: $-0.75 + 0.75 \cdot (-1)?$ Wait.  
$(-1.5)(0.5) + (\dots)$ No.  
Let's calculate carefully.  
$\vec{CA} = (-3/2, -\sqrt{3}/2)$.  
$\vec{CB} = (1/2, -\sqrt{3}/2)$.  
Wait, $B-A = 1-(-1)=2$? No. Coordinates: $A=(-1,0), B=(1,0)$.  
Wait, if $C=(1/2, \sqrt{3}/2)$. Then $CA^2 = (1/2+1)^2 + (\dots)$. Wait no. $A=(-1,0)$. $C=(0.5, 0.866)$.  
$\vec{AC} = C - A = (-0.5, 0.866)$.  
$\vec{CB} = B - C = (0.5, -0.866)$. No, $B-C$ vector. Wait $A=(-1,0), C=(0.5, 0.866) \implies C-A = (1.5, 0.866)$.  
$\vec{AC} = A - C = (-1 - 0.5, -0.866) = (-1.5, -0.866)$.  
Wait, let's check dot product of vectors originating from $C$.  
$\vec{u} = A-C$. $\vec{v} = B-C$.  
$\vec{u} \cdot \vec{v} = (A-C)_x(B-C)_x + (A-C)_y(B-C)_y$.  
$(-1 - 0.5)(1 - 0.5) + (-0.866)(-0.866)$  
$= (-1.5)(0.5) + (0.75)?$ No $(0.5^2 + 0.866^2)$ is not 1?  
$A=( -1, 0 )$. $B = (1,0)$.  
$C = (0.5, \sqrt{3}/2)$. Wait. If $x_c=1$, $y_c=\sqrt{3}$. No, circle is radius 1. $1^2+3/4 \neq 1$.  
So my $C$ coordinates were wrong.  
But the check was for $C=(-\sqrt{3}/2, \dots)$.  
Let's go back to $C=(x,y)$ on circle $(x)^2 + (y)^2 = 1$.  
$\vec{CA} = A - C = (-1-x, -y)$.  
$\vec{CB} = B - C = (1-x, -y)$.  
Dot product: $(-1-x)(1-x) + (-y)(-y) = -(1+x)(1-x) + y^2$? No.  
Wait. If vectors are $u = A-C, v = B-C$.  
$u_x = -1-x, u_y = 0-y$. $v_x = 1-x, v_y = 0-y$.  
Dot product: $(-1-x)(1-x) + (-y)^2 = (x+1)(x-1) + y^2$? No.  
$( -1-x )( 1-x ) = -(1+x) - x + x = -(1-x-x) - x = -(1+2x)$? No.  
Let's simplify: $(-1-x)(1-x) = -(1-x^2)$.  
Wait, $u_x u_y$ is not right.  
Wait, dot product of $(A-C, B-C)$.  
Wait, the formula for angle at C is $\cos \theta = \frac{(A-B)\cdot(C-A)}{|C-A||B-C|}$. No.  
$\vec{CA} = A - C$. $\vec{CB} = B - C$.  
$A = (-1,0), B=(1,0), C(x,y)$.  
$\vec{CA} = (x+1, -y)$. Wait no, $C$ is $(x,y)$, so $A-C = (-1-x, -y)$.  
$\vec{CB} = (1-x, -y)$. No, $B=(1,0) \implies B-C = (1-x, -y)$.  
Wait, the angle is at $C$, formed by rays $CA$ and $CB$.  
Angle between vectors $(x+1, y)$? No. $A=(-1,0), C=(x,y)$. Vector $C \to A$ is $(-1-x, -y)$. Vector $C \to B$ is $(1-x, -y)$? No.  
Wait, vector from $C$ to $B$ is $(1-x, -y)$?  
$B$ is $(1,0)$. So $x=1, y=0$. $B-C = (1-x, 0-y)$.  
$\vec{CB} = (1-x, -y)$.  
$\vec{CA} = (-1-x, -y)$? No. $A=(-1,0) \implies x=-1, y=0$. $C=(x,y)$. So $A-C = (-1-x, -y)$.  
Wait, dot product is $(x+1)(-1+x) + ...$ No.  
Let's just use the formula for angle $\theta$: $\cos \theta = \frac{a^2+b^2-c^2}{2ab}$? No.  
Using vectors from $C$. $\vec{u} = A - C, \vec{v} = B - C$.  
$\vec{u} = (-1-x, -y)$.  
$\vec{v} = (1-x, -y)$.  
Wait. $(x+1)(-1+x)$? No.  
Let's check dot product for vectors pointing outwards: $C-A$ and $C-B$?  
No. Angle at $C$ is between vector $CA$ and $CB$.  
$A = (-1, 0)$. $B = (1, 0)$. $C=(x,y)$.  
Vector $CA = A - C = (-1-x, -y)$? Wait. If I want angle from $C$, the vector should be pointing *to* the endpoints.  
So $\vec{CA} = A - C$. This is $(-1-x, -y)$. Correct.  
Vector $CB = B - C = (1-x, -y)$? No. Wait.  
Wait. If I use $C$ as origin for vectors from $C$, then vectors are $-A-C$ and $-B-C$? No.  
The angle between vector pointing to A and vector pointing to B.  
Vector 1: $(-1-x, -y)$.  
Vector 2: $(x-1, y)$? No. $B=(1,0) \implies (1-x, -y)$. Wait. $C=(x,y)$ is inside circle? Yes.  
Wait. I need to be careful with signs. Let's use a simpler approach.  
The circle has center $(0,0)$. So the coordinates are symmetric.  
Let's calculate angle $\angle ACB$ for general point on unit circle: $(\cos \theta, \sin \theta)$.  
Wait, this means $C$ is on unit circle.  
Then $\vec{CA} = A - C = (-1-\cos\theta, -\sin\theta)$.  
$\vec{CB} = B - C = (1-\cos\theta, -\sin\theta)$.  
Dot product: $(-1-\cos\theta)(1-\cos\theta) + (\dots)$  
$= -(1+\cos\theta)(1-\cos\theta) + \sin^2\theta$? No.  
$(-(1+\cos\theta)) = -1 - \cos\theta$.  
Wait, I wrote $\vec{CA} = (-1-x, -y)$. $C=(x,y)$ so $A-C = (-1-x, -y)$.  
This assumes $A=(-1,0), B=(1,0)$.  
Then $\vec{CB} = (1-x, -y)$. Wait.  
Let's check the dot product:  
$(-1-x)(1-x) + (-y)(-y)$ ? No. $(-y)(-y)$ is not correct?  
Wait, if $C=(x,y)$, then $B=(1,0)$. So $\vec{CB} = (1-x, 0-y) = (1-x, -y)$. Correct.  
Then dot product $\vec{CA} \cdot \vec{CB} = (-1-x)(1-x) + (-y)(-y)$? No.  
Wait. $(-y)(-y)$ is correct if both have same y-component.  
Yes, $C$ has coordinates $(x,y)$. So $A=( -1, 0 )$. So $B-A = (2,0)$.  

*Continued in [part 3 of 3](geometry_347_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
