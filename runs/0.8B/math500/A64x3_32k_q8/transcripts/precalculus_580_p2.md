# test/precalculus/580.json, part 2 of 2

[Previous part](precalculus_580.md)

$a^2 = b^2 + c^2 - 2bc \cos B$.  
Here $b=c=\sqrt{54}$.  
$a^2 = 54 + 54 - 2(54) \cos B$.  
Also, from coordinate geometry, we calculated $\vec{BA} \cdot \vec{BC}$.  
$\vec{BA}$ is vector from B to A. $\vec{BC}$ is from B to C.  
So these are the sides of the triangle.  
$AB = \sqrt{54}$. $BC = \sqrt{54}$.  
Dot product of these two vectors was -27.  
Cosine formula: $-1/2$.  
So angle B is 120 degrees.  
Isosceles with base AC?  
If $\cos B = -1/2$, then $\angle ABC = 120^\circ$.  
Side lengths $AB=BC$. The base angle is equal to (vertex) opposite side? No, vertex angle.  
Since AB=BC, the angles at A and C are equal.  
Sum of angles: $B + A + C = 180$.  
$120 + A + A = 180 \implies 2A = 60 \implies A = 30^\circ$.  
Let's check if this is consistent with coordinates.  
If $\angle ABC = 120$, then $\cos(ABC) = -1/2$.  
Also by Law of Cosines, $AC^2 = 54 + 54 - 2(54)(-1/2) = 108 + 54 = 162$.  
And $AC^2 = 162$ as computed earlier from $A=(1,-11,2), C=(-2,1,-1)$.  
Is there a check for angle A?  
$\vec{AB} \cdot \vec{AC}$? No.  
Let's calculate $\cos(\angle BAC)$.  
Vectors: $\vec{BA}$ and $\vec{BC}$. Angle is 120.  
Then $\vec{AB}$ has same magnitude $54$ but opposite direction to $\vec{BA}$.  
Angle between $\vec{AB}$ and $\vec{AC}$?  
$\cos(\angle BAC) = \frac{\vec{AB} \cdot \vec{AC}}{|\vec{AB}| |\vec{AC}|}$.  
We don't have this. But we calculated $AC^2$ using coordinates.  
Let's check dot product $\vec{BA} \cdot \vec{BC}$ again to be absolutely sure.  
$\vec{BA} = (-2, -7, 1)$.  
$\vec{BC} = (-5, 5, -2)$.  
$(-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$.  
Correct.  

Is it possible that I made a mistake in identifying vectors?  
Maybe $\vec{AB}$ and $\vec{AC}$?  
Angle is "ABC", meaning B is the vertex. So between AB and CB? No, from B to A and B to C.  
The order of points in notation usually implies vertices. $A$ and $C$. The angle at B is formed by lines BA and BC.  
This is what I calculated.  
So $\cos \theta = -1/2 \implies \theta = 120^\circ$.  

There seems to be no ambiguity.  

What if the problem meant "compute $\angle ABC$ where $\angle A=90$"? No, that would change coordinates or angles.  

The solution seems solid.  

Double check the question text again for any subtle hint.  
"Compute angle ABC"  
No tricky wording found.  

I will formulate the response now.  
Steps:  
1. Define vectors starting from B: $\vec{BA} = A - B$ and $\vec{BC} = C - B$.  
2. Substitute coordinates into vectors.  
3. Calculate dot product $d$.  
4. Calculate magnitudes squared $m_1, m_2$.  
5. Use cosine rule to find angle.  

Calculation:  
$\vec{BA} = (1-3, -11-(-4), 2-1) = (-2, -7, 1)$.  
$\vec{BC} = (-2-3, 1-(-4), -1-1) = (-5, 5, -2)$.  
$\vec{BA} \cdot \vec{BC} = 10 - 35 - 2 = -27$.  
$|\vec{BA}|^2 = 4 + 49 + 1 = 54$.  
$|\vec{BC}|^2 = 25 + 25 + 4 = 54$.  
$\cos \theta = \frac{-27}{\sqrt{54}\sqrt{54}} = -\frac{27}{54} = -\frac{1}{2}$.  
$\theta = 120^\circ$.  

Looks perfect.  
Final answer format requires \boxed{}.  
The question asks to put the final answer within `\boxed{}`.  
I should write the reasoning clearly.  
Is there any alternative interpretation of coordinates? No.  
Is there any chance of degree vs radians? Degrees usually implied.  
Answer is 120 degrees.  

One small check: Is it possible that $A, B, C$ form an equilateral triangle in some transformed space? No, they are just numbers.  

Let's verify with a quick random guess.  
If $\vec{BA} \cdot \vec{BC} = -27$, and $\cos \theta = -0.5$, angle is 120.  
Let's check if $AC^2$ matches something else. No need.  

Final result: 120.  
The problem asks for angle ABC.  
Is it possible that the points are $(1,-11,2)$ and $(3,-4,1)$? Yes.  
I am confident.  

The reasoning is clear.  
Coordinates provided: A(1,-11,2), B(3,-4,1), C(-2,1,-1).  
Vectors BA = (-2,-7,1)  
VCBC = (-5,5,-2)? No. $\vec{BC} = C-B$.  
$C - B$: $x: -2-3=-5$, $y: 1-(-4)=5$, $z: -1-1=-2$.  
Yes.  
$BA \cdot BC = 10 - 35 - 2 = -27$.  
$|BA|^2 = 4 + 49 + 1 = 54$.  
$|BC|^2 = 25 + 25 + 4 = 54$.  
Cosine is -1/2.  
Angle is 120 degrees.  

One subtle point: What if I used vectors $AB$ and $AC$?  
The angle at B would be between $\vec{BA}$ and $\vec{BC}$.  
If the question asked for angle ABC, it means angle at vertex B.  
Standard convention: vertices are named in order around perimeter usually? No, just points.  
Wait, $\angle ABC$ is the angle formed by segments AB and BC with vertex B.  
Yes.  

The solution holds.  

One more thing. What if $A=(1,-11,2)$ meant something else? No.  
Is there any chance that coordinates are in a different system (e.g. spherical)? No, "Compute angle ABC" implies Euclidean space.  
And the prompt is in LaTeX code style, suggesting math context.  

So answer 120.  

The solution should show work:  
1. Identify vertices and vectors.  
2. Calculate magnitudes.  
3. Calculate dot product.  
4. Solve for cosine.  
5. Convert to degrees.  

Wait, $\cos \theta = -1/2$. $\arccos(-1/2) = 120^\circ$. Correct.  

Let's quickly check the vector arithmetic one more time.  
$A(1, -11, 2)$  
$B(3, -4, 1)$  
$C(-2, 1, -1)$  
$A-B$: $(1-3, -11+4, 2-1) = (-2, -7, 1)$. Correct.  
$C-B$: $(-2-3, 1+4, -1-1) = (-5, 5, -2)$. Correct.  
Dot product:  
$x_1 x_2 + y_1 y_2 + z_1 z_2$  
$(-2)(-5) = 10$  
$(-7)(5) = -35$  
$(1)(-2) = -2$  
Sum: $10 - 37 = -27$. Correct.  

Magnitudes:  
$BA^2 = 4 + 49 + 1 = 54$. Correct.  
$BC^2 = 25 + 25 + 4 = 54$. Correct.  

The angle is $\arccos(-1/2)$.  

Is there any other interpretation of "Compute angle ABC"?  
Could it be in radians? "Compute angle ABC" usually implies a number in degrees unless specified.  
I'll provide degrees.  

Final check. Is it possible that points $A, B, C$ are not collinear in 3D but just forming a triangle? Yes.  
Is it possible the angle is not $ABC$? No, standard definition.  
Everything seems fine.  

I will formulate the final response now.  
The problem asks to compute the angle $\angle ABC$. The vertices of the angle are $B$. The vectors originating from $B$ are towards $A$ and $C$. Thus we define $\vec{BA}$ and $\vec{BC}$.  
Let's check if any coordinate typo could be subtle.  
If I transcribed the coordinates wrong, say $A = (1,-11,2)$ was $(1, 1, -11, 2)$? No, just copying what was there.  
$B = (3, -4, 1)$.  
$C = (-2, 1, -1)$.  
All clear.  

If the coordinates were $A(1,-11,2)$ and $B(-3, -4, 1)$? No, that would change sign of x in BA vector.  
My calculation used specific numbers. I am confident.  

Result: 120 degrees.  

The steps are:  
1. Define the vectors representing the sides of angle ABC originating at B.  
$\vec{BA} = A - B$  
$\vec{BC} = C - B$  
2. Calculate the coordinates of $A, B, C$.  
$B$ is the reference point.  
3. Compute $\cos \theta = \frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|}$.  
4. Substitute and solve for $\theta$.  

The calculation is straightforward verification of arithmetic.  
Final check on result magnitude:  
If $\vec{BA} = (10, -20, 1)$, $\vec{BC} = (-5, 5, -2)$.  
Dot product would be large negative. If magnitudes are roughly equal and dot product is negative, angle approaches 90.  
Here dot product is negative 27, magnitude of dot product is small compared to squares?  
If $|\vec{BA} \cdot \vec{BC}| \approx \sqrt{54}^2$, then $\cos^2 \theta \approx -1/3$ ? No.  
The result is robust.  

I'll write out the solution clearly.  
Coordinates:  
$x_A = 1, y_A = -11, z_A = 2$  
$x_B = 3, y_B = -4, z_B = 1$  
$x_C = -2, y_C = 1, z_C = -1$  

$\vec{BA} = (1-3, -11-(-4), 2-1) = (-2, -7, 1)$  
$\vec{BC} = (-2-3, 1-(-4), -1-1) = (-5, 5, -2)$  

$|\vec{BA}|^2 = (-2)^2 + (-7)^2 + (1)^2 = 4 + 49 + 1 = 54$.  
$|\vec{BC}|^2 = (-5)^2 + (5)^2 + (-2)^2 = 25 + 25 + 4 = 54$.  

$\vec{BA} \cdot \vec{BC} = (-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$.  
$\cos(\angle ABC) = \frac{-27}{\sqrt{54}\sqrt{54}} = \frac{-27}{54} = -\frac{1}{2}$.  
$\angle ABC = \arccos(-0.5) = 120^\circ$.  

Seems good to go.  

One tiny thing: Could the problem be interpreted as $A=(1,-11,2)$ is not in space but something else?  
No, standard coordinate geometry notation implies 3D. "Compute angle ABC" in this context with coordinates $(x,y,z)$ suggests a plane or general triangle.  
The solution stands.  

One last thought: Could the order of B be confusing with the name of a vertex? No.  
Angle ABC is standard.  

Is there any trick where $B$ lies on a line perpendicular to $AC$? No such thing as $A, B, C$.  

Okay, I'm ready.  


## Answer

To compute the angle $\angle ABC$, we can use vector algebra with the coordinates of the points. The vertices of the triangle are given by:  
$A = (1, -11, 2)$  
$B = (3, -4, 1)$  
$C = (-2, 1, -1)$  

The angle at $B$, denoted $\angle ABC$, is formed by the vectors originating from point $B$. Let us denote these vectors as:  
$\vec{BA} = A - B$ and $\vec{BC} = C - B$.  

First, we calculate the components of these vectors based on the coordinates.  

1.  **Calculate vector $\vec{BA}$:**  
$$ \vec{BA} = (x_A - x_B, y_A - y_B, z_A - z_B) $$  
$$ \vec{BA} = (1 - 3, -11 - (-4), 2 - 1) $$  
$$ \vec{BA} = (-2, -7, 1) $$  

2.  **Calculate vector $\vec{BC}$:**  
$$ \vec{BC} = (x_C - x_B, y_C - y_B, z_C - z_B) $$  
$$ \vec{BC} = (-2 - 3, 1 - (-4), -1 - 1) $$  
$$ \vec{BC} = (-5, 5, -2) $$  

Next, we compute the dot product $\vec{BA} \cdot \vec{BC}$ and the magnitudes of these vectors. The magnitude squared is given by $|\vec{v}|^2$.  

The dot product $\vec{BA} \cdot \vec{BC}$ is:  
$$ \vec{BA} \cdot \vec{BC} = (-2)(-5) + (-7)(5) + (1)(-2) $$  
$$ = 10 - 35 - 2 $$  
$$ = -27 $$  

The magnitude squared of $\vec{BA}$ is:  
$$ |\vec{BA}|^2 = (-2)^2 + (-7)^2 + (1)^2 $$  
$$ |\vec{BA}|^2 = 4 + 49 + 1 = 54 $$  
$$ |\vec{BA}| = \sqrt{54} = 3\sqrt{6} $$  

Similarly, the magnitude squared of $\vec{BC}$ is:  
$$ |\vec{BC}|^2 = (-5)^2 + (5)^2 + (-2)^2 $$  
$$ |\vec{BC}|^2 = 25 + 25 + 4 = 54 $$  
$$ |\vec{BC}| = \sqrt{54} = 3\sqrt{6} $$  

We can find the cosine of the angle $\theta$ at point $B$ using the dot product formula:  
$$ \cos \theta = \frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|} $$  
Substituting the values calculated above:  
$$ \cos \theta = \frac{-27}{\sqrt{54} \cdot \sqrt{54}} $$  
Since $\sqrt{54} \cdot \sqrt{54} = 54$, we have:  
$$ \cos \theta = \frac{-27}{54} = -\frac{1}{2} $$  

Finally, we find the angle $\theta$ in degrees using the arccosine function. Since the result is between $-1$ and $1$ and negative, it corresponds to an obtuse angle in the range $(0, 180^\circ)$.  
$$ \theta = \arccos\left(-\frac{1}{2}\right) $$  
$$ \theta = 120^\circ $$  

The angle $\angle ABC$ is $120^\circ$.  

\boxed{120}  
