# test/precalculus/580.json (Precalculus, level 3)

> Let $A = (1,-11,2),$ $B = (3,-4,1),$ and $C = (-2,1,-1).$  Compute $\angle ABC,$ in degrees.  

**Correct.** Gold `120^\circ`, predicted `120`. Finish: stop, 12397 tokens, 3 waits, 934.6 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here is the problem:  
Given three points $A$, $B$, and $C$. I need to find the measure of angle $ABC$.  

The coordinates are:  
$A = (1, -11, 2)$  
$B = (3, -4, 1)$  
$C = (-2, 1, -1)$  

There are two possible approaches.  
Method 1: Cosine Rule in the plane or using vectors.  
The angle is between vectors $\vec{AB}$ and $\vec{BC}$. Let's denote points as $A$, $B$, $C$.  
Vector $\vec{BA} = A - B$  
Vector $\vec{BC} = C - B$  

First, let's find vectors:  
$\vec{BA} = (1-3, -11 - (-4), 2 - 1) = (-2, -7, 1)$  
$\vec{BC} = (-2 - 3, 1 - (-4), -1 - 1) = (-5, 5, -2)$  

Now, I can compute the dot product of these two vectors:  
$\vec{BA} \cdot \vec{BC} = (-2)(-5) + (-7)(5) + (1)(-2)$  
$= 10 - 35 - 2$  
$= 10 - 37$  
$= -27$  

I also need to compute the lengths of these vectors.  
Length of $\vec{BA}$: $|\vec{BA}| = \sqrt{(-2)^2 + (-7)^2 + (1)^2} = \sqrt{4 + 49 + 1} = \sqrt{54}$  
Length of $\vec{BC}$: $|\vec{BC}| = \sqrt{(-5)^2 + (5)^2 + (-2)^2} = \sqrt{25 + 25 + 4}$  
$= \sqrt{54}$  

Let's check if this is the correct calculation.  
Points are A(1, -11, 2), B(3, -4, 1), C(-2, 1, -1).  
$\vec{BA} = (1-3, -11-4, 2-1) = (-2, -7, 1)$? No. $B-A = (3-1, -4-(-11), 1-2) = (2, 7, -1)$ or $(A-B) = (-2, -7, 1)$ is correct if order is $A \to B$.  
Let's re-verify vectors.  
$\vec{AB} = B - A = (3-1, -4 - (-11), 1-2) = (2, 7, -1)$.  
Let's find the angle between vector $\vec{AB}$ and vector $\vec{BC}$. Let's call the points $A$, $B$, $C$. So angle is at vertex B? No, "angle ABC" usually implies the angle at vertex B formed by points A, B, C. Yes, that means vectors $\vec{BA}$ or $\vec{AB}$ originating from B.  
So we need $\cos \theta = \frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|}$.  

Let's check the coordinates again carefully.  
$A=(1, -11, 2)$  
$B=(3, -4, 1)$  
$C=(-2, 1, -1)$  
$\vec{AB}$ vector from B to A? Or just vectors originating at origin or vertices? The angle is between two rays.  
Usually $\angle ABC$ is the angle formed by segments $BA$ and $BC$. So the vertex is B.  
The vectors are $\vec{BA}$ and $\vec{BC}$.  
$\vec{BA} = A - B = (1-3, -11 - (-4), 2-1) = (-2, -7, 1)$  
$\vec{BC} = C - B = (-2-3, 1 - (-4), -1-1) = (-5, 5, -2)$  

Let's recompute the dot product $\vec{BA} \cdot \vec{BC}$:  
$= (-2)(-5) + (-7)(5) + (1)(-2)$  
$= 10 - 35 - 2 = -27$. Correct.  

Now compute magnitudes $|\vec{BA}|^2$ and $|\vec{BC}|^2$:  
$|\vec{BA}|^2 = (-2)^2 + (-7)^2 + (1)^2 = 4 + 49 + 1 = 54$.  
$|\vec{BC}|^2 = (-5)^2 + (5)^2 + (-2)^2 = 25 + 25 + 4 = 54$.  

So, the dot product is -27.  
Let's calculate $\cos \theta$:  
$\cos \theta = \frac{-27}{\sqrt{54} \cdot \sqrt{54}}$  
$\cos \theta = \frac{-27}{54}$  

Divide by 27:  
$\cos \theta = -1/2$.  
This implies $\theta = 120^\circ$ (since angle must be between $0$ and $180^\circ$).  

Is it possible I miscalculated?  
Let me double check the coordinates.  
$A=(1,-11,2)$  
$B=(3,-4,1)$  
$C=(-2,1,-1)$  

Vectors $\vec{BA} = A-B$: $x: 1-3=-2$, $y: -11-(-4)=-7$, $z: 2-1=1$.  
$\vec{BC} = C-B$: $x: -2-3=-5$, $y: 1-(-4)=5$, $z: -1-1=-2$.  

Dot product: $(-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$.  
Magnitudes squared:  
$|\vec{BA}|^2 = 4 + 49 + 1 = 54$.  
$|\vec{BC}|^2 = 25 + 25 + 4 = 54$.  
$\cos \theta = \frac{-27}{\sqrt{54} \cdot \sqrt{54}} = -27/54 = -1/2$.  

So $\theta = 120^\circ$.  

Let's quickly check the cosine of angle using the other vector from A.  
$\vec{AB} = (2, 7, -1)$.  
Angle between vectors $\vec{BA}$ and $\vec{BC}$. The vectors should be $(A-B)$ and $(C-B)$.  
This is correct.  

Let's verify coordinates again.  
$A=(1,-11,2)$  
$B=(3,-4,1)$  
$C=(-2,1,-1)$  
Maybe I copied wrong?  
$C = (-2,1,-1)$  
$\vec{BC} = C - B = (-5, 5, -2)$.  
Let's verify $y$-component again.  
$B$ is $(3, -4, 1)$. $C$ is $(-2, 1, -1)$.  
Difference in y is $1 - (-4) = 5$. Correct.  

Check dot product again.  
$x: -2 \times -5 = 10$  
$y: -7 \times 5 = -35$  
$z: 1 \times -2 = -2$  
Sum: $-27$. Correct.  

Let's check magnitudes again.  
$\sqrt{4+49+1} = \sqrt{54}$.  
$\sqrt{25+25+4} = \sqrt{54}$.  

So angle is $120^\circ$.  

However, usually problems like this expect exact answers using cosine of specific angles or maybe a trick. Is there any ambiguity? "angle ABC" usually implies the geometric angle at B.  

Is it possible that $\vec{AB}$ and $\vec{BC}$ are used instead of $\vec{BA}$ and $\vec{BC}$? The angle is defined by two segments starting from A, passing through B, and ending at C. The vertex is B. So yes, vectors originating from B: $\vec{BA}$ and $\vec{BC}$.  

Let's calculate using the other way just in case (checking if I missed something).  
Vector from A to B: $(2, 7, -1)$  
Vector from A to C: $(-2-1, 1 - (-11), -1 - 2) = (-3, 12, -3)$  
Angle at A between $\vec{AB}$ and $\vec{AC}$? No, angle ABC is not the angle at A in the triangle formed. It's the angle subtended by segment AC at B? No, vertices are $A$, $B$, $C$. Angle at B is the angle between BA and BC.  
The sides of the triangle are $c = AB$, $b = BC$, $a = AC$.  
We need the cosine of angle $\theta$ opposite to side $AC$? No, it's simply $\angle ABC$.  
Vectors $\vec{BA}$ and $\vec{BC}$ form the sides at B.  

Let's check if any coordinate typo might be making this trivial or if I messed up arithmetic.  
$\sqrt{54} = 3\sqrt{6}$.  
$|\vec{AB}|^2 = 54$.  
$|\vec{BC}|^2 = 54$.  
$\vec{BA} \cdot \vec{BC} = -27$.  
Angle is $120^\circ$.  

Let's try to visualize or guess.  
$A$ and $B$ are on y-axis. No, that's not relevant here.  
$x_A=1$, $y_A=-11$, $z_A=2$  
$x_B=3$, $y_B=-4$, $z_B=1$  
$x_C=-2$, $y_C=1$, $z_C=-1$  

Let's check for a simpler relation, e.g. $\vec{AB}$ and $\vec{BC}$? No, angle is at B. Vectors are $\vec{BA}, \vec{BC}$.  
Is there any ambiguity about coordinate order? Usually $A, B, C$ implies angle at B in the triangle with vertices A, B, C.  

Let's re-verify calculation of dot product:  
$(-2)(-5) + (-7)(5) + (1)(-2)$  
$= 10 - 35 - 2$  
$= -27$.  
Magnitude squares: $4+49+1 = 54$. $25+25+4 = 54$.  

The result is $\cos \theta = -27/54 = -1/2$.  
So the angle is $120^\circ$.  

Just a sanity check.  
Is it possible to compute using coordinates in terms of unit vectors or something?  
Let's find the direction of each point relative to B.  
$\vec{BA} = (-2, -7, 1)$  
$\vec{BC} = (-5, 5, -2)$  

Angle is $\theta$. $\cos \theta = \frac{-27}{54} = -1/2$.  

Is it possible that I made a mistake in copying coordinates?  
$A = (1, -11, 2)$  
$B = (3, -4, 1)$  
$C = (-2, 1, -1)$  

Let's calculate distance $AB$ and $BC$ again just to ensure they are valid sides.  
$AB^2 = (3-1)^2 + (-4-(-11))^2 + (1-2)^2 = 2^2 + 7^2 + (-1)^2 = 4 + 49 + 1 = 54$.  
$BC^2 = (-2-3)^2 + (1-(-4))^2 + (-1-1)^2 = (-5)^2 + 5^2 + (-2)^2 = 25 + 25 + 4 = 54$.  
So $AB = \sqrt{54}$ and $BC = \sqrt{54}$.  
The triangle is isosceles.  

In an isosceles triangle with base angles equal or sides equal?  
Side lengths are $\sqrt{54}$. So all sides equal to $\sqrt{54}$?  
Let's check AC^2.  
$AC = \sqrt{(-2-1)^2 + (1 - (-11))^2 + (-1-2)^2} = \sqrt{(-3)^2 + (12)^2 + (-3)^2} = \sqrt{9 + 144 + 9} = \sqrt{162}$.  
Is $AC^2$ related to AB? $\sqrt{54} = 6\sqrt{6} \approx 2.07*2.45... = 5.1$. No, $3\sqrt{6} \approx 7.348$.  
$\sqrt{54} \approx 7.34$.  
$AC^2 = 162$. $162/54 = 3$. So $AC^2 = 3 (\sqrt{54})^2$.  
$\sqrt{54}$ is the common base of something? No.  

Let's verify angles again.  
If $\cos \theta = -1/2$, then angle is $120^\circ$.  
Since sides are equal, $\angle BAC$ must also be related.  
By Law of Cosines: $AB^2 = AC^2 + BC^2 - 2 AC \cdot BC \cos \angle A$ ? No, that's for sides opposite to vertices.  
Let's just stick with the direct vector calculation which seems robust.  

One more check on arithmetic.  
$\sqrt{54} \approx 7.348$. $1/2 \times 54 = 27$.  
$-27 / (7.348 \cdot 7.348) = -27/54 = -0.5$. Correct.  
Magnitude check:  
$(-2)^2 = 4$.  
$(-7)^2 = 49$.  
$1^2 = 1$. Sum = 54.  
$(-5)^2 = 25$.  
$(5)^2 = 25$ (since $B_y= -4$, $C_y = 1$, $-4 - (-4) = 0$? No, $y_B=-4$, $y_C=1$. So $1 - (-4) = 5$. Yes).  
$(-2)^2 = 4$.  
$(-2-3)=-5$, $-1-1=-2$.  
$BC^2 = 25 + 25 + 4 = 54$. Correct.  

Is it possible the coordinates are transcribed wrong?  
$A=(1,-11,2)$ -> $1, -11, 2$.  
$B=(3,-4,1)$ -> $3, -4, 1$.  
$C=(-2,1,-1)$.  

Let me re-calculate everything in a more scratchpad style to be absolutely sure.  
Points: $(1,-11,2), (3,-4,1), (-2,1,-1)$  
Vectors $\vec{BA} = A-B = (1-3, -11+4, 2-1) = (-2, -7, 1)$.  
$\vec{BC} = C-B = (-2-3, 1+4, -1-1) = (-5, 5, -2)$.  
Dot Product: $(-2)(-5) + (-7)(5) + (1)(-2)$  
$= 10 - 35 - 2$  
$= -27$. Correct.  

Magnitudes:  
$\sqrt{(-2)^2 + (-7)^2 + 1^2} = \sqrt{4 + 49 + 1} = \sqrt{54}$.  
$\sqrt{(-5)^2 + 5^2 + (-2)^2} = \sqrt{25 + 25 + 4} = \sqrt{54}$.  

So $\cos B = -27/54 = -1/2$.  
$B = 120^\circ$.  

Seems correct.  

What if I used vectors from A and C? No, problem states angle ABC. The vertex is B. Vectors should start at B. So $\vec{BA}$ and $\vec{BC}$.  

Could there be any other interpretation of $\angle ABC$?  
In Euclidean geometry, the notation $\angle XYZ$ usually means the angle at Y between rays XY and YZ.  
So we have $B$ is origin. $A$ and $C$ are points on the plane (or in 3D). The vectors to A from B and C from B form the sides of the angle.  

Let me just double check if I got the signs right for dot product.  
$x_A - x_B = 1 - 3 = -2$.  
$y_A - y_B = -11 - (-4) = -7$. (Since $y_B=-4$)  
$z_A - z_B = 2 - 1 = 1$.  
$y_C - y_B = 1 - (-4) = 5$.  
$x_C - x_B = -2 - 3 = -5$.  
$y_C - y_B = 5$.  
$z_C - z_B = -1 - 1 = -2$.  
Okay, vectors:  
$\vec{BA} = (A.x - B.x, A.y - B.y, A.z - B.z) = (-2, -7, 1)$.  
$\vec{BC} = C - B$ ? No. Angle at B. Vectors emanating from B towards A and C.  
Vector $\vec{BA}$ is point $A$ minus point $B$. Correct.  
Vector $\vec{BC}$ is point $C$ minus point $B$. Correct.  
The dot product was $(-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$.  
Magnitude squareds were both 54.  
Product is negative implies obtuse angle. So $120^\circ$.  

Is there any possibility that the order of points $A, B, C$ matters for calculation? No, it's just naming them.  
The only thing that could be tricky is if coordinates are not orthogonal or similar?  
Let's check orthogonality again.  
Maybe my dot product result of -27 leads to 120 degrees correctly? Yes, $-1/2$ is the cosine.  

Let me just double check the arithmetic on $\sqrt{54}$.  
$54 = 9 \times 6$.  
$\sqrt{54} = 3\sqrt{6} \approx 7.34846$.  

Let's re-verify coordinates one more time from a different source or perspective? No, just manual transcription.  
$A(1,-11,2)$  
$B(3,-4,1)$  
$C(-2,1,-1)$  
Maybe I should check if points are collinear?  
$\vec{AB}$ vs $\vec{AC}$.  
Vector from A to B: $(2, 7, -1)$.  
Vector from A to C: $(-3, 12, -3)$.  
Slope $B-A = 1/2$? No.  
Slope of vector (2,7,-1) vs slope of (-3,12,-3).  
Not collinear.  

Is it possible I should have used $\vec{BC}$ and $\vec{BA}$ but calculated something else? No, geometry is invariant to swapping points if vectors are chosen from B to A and B to C.  
Angle ABC is determined by vectors BA and BC.  
Let's re-verify dot product one more time to be absolutely certain.  
$(-2)(-5) = 10$. Correct.  
$(-7)(5) = -35$. Correct.  
$(1)(-2) = -2$. Correct.  
Sum = $-27$. Correct.  

Let's check the lengths squared one more time.  
$B=(3,-4,1)$  
$A=(1,-11,2)$  
$d_A^2 = (1-3)^2 + (-11+4)^2 + (2-1)^2$ ? No $A-B$.  
$AB$: $(3-1)^2 + (-4-(-11))^2 + (1-2)^2 = 2^2 + 7^2 + (-1)^2 = 54$. Correct.  

$C=(-2,1,-1)$  
$d_C^2 = (-2-3)^2 + (1-(-4))^2 + (-1-1)^2 = (-5)^2 + 5^2 + (-2)^2 = 25 + 25 + 4 = 54$. Correct.  

So it's an isosceles triangle with sides $\sqrt{54}$ in the plane defined by the vectors.  
Angle at B is 120 degrees.  
The vector product magnitude squared is $|\vec{BA}|^2 |\vec{BC}|^2 \cos \theta = |\vec{BA}|^2 + |\vec{BC}|^2 - 2 \vec{BA} \cdot \vec{BC}$.  
We have $\cos^2 \theta$ from dot product.  
$-27 = -(54) (1/2 + 0)?$ No.  
Let's just solve for cos: $\cos \theta = -27 / 54 = -1/2$.  
$\theta = 120^\circ$.  

Let's check if the triangle exists. Sides are $\approx 7.34$ and $68$ degrees? No, $\sqrt{54} \approx 7.348$ and $\sqrt{54} \approx 7.348$  
Base of isosceles triangle with base angles not equal necessarily.  
The base is AC.  

Let's assume the question asks for angle between sides $AB$ and $BC$. This is standard notation $\angle B$.  
In plane geometry (if we view this as 2D), $\angle ABC$ is just an angle in the triangle defined by these points.  

Is there any chance I should interpret "ABC" differently? No.  

What if I made a calculation error in dot product expansion?  
$-7 \times 5 = -35$.  
$(-2) \times (-5) = +10$.  
Sum $10 - 35 - 2 = -27$. Yes.  

Is there any chance I made a calculation error in vector subtraction?  
$\vec{BA} = A - B$.  
$A: (1, -11, 2)$  
$B: (3, -4, 1)$  
$x: 1-3=-2$. $y: -11-(-4) = -7$. $z: 2-1=1$. Correct.  
$\vec{BC} = C - B$.  
$C: (-2, 1, -1)$  
$B: (3, -4, 1)$  
$x: -2-3=-5$. $y: 1-(-4)=5$. $z: -1-1=-2$. Correct.  
Note: earlier I had $\vec{BC} = (-5, 5, -2)$. Correct.  

Is there any chance that the vectors should be swapped? No, vector addition for cosine involves dot product and normalization of magnitudes. It doesn't matter if direction is reversed. $BA \cdot BC$ vs $AB \cdot CB$?  
If we calculate angle between $\vec{BA}$ and $\vec{BC}$. This corresponds to the triangle B-A-C with vertices A, B, C.  
So $\angle ABC$ is indeed the angle at vertex B in the triangle formed by points A, B, C.  

Is it possible that I used wrong coordinates? Let's write them down clearly.  
$A(1,-11,2)$  
$B(3,-4,1)$  
$C(-2,1,-1)$  

Let me check if $B=(3,-4,1)$ is a typo for something else or if I'm misremembering the values.  
Maybe $C=(-2,1,-1)$? Or $A, B, C$ values.  
The provided text is:  
$A = (1,-11,2),$  
$B = (3,-4,1),$  
$C = (-2,1,-1).$  
All look like standard integers.  

Let's do a sanity check with $x,y,z$ components relative to center of triangle?  
No obvious geometric features.  

Could it be that angle at B is 120 degrees, so $\cos \angle ABC = -1/2$.  
$\arccos(-0.5) = 120^\circ$.  

Is there any other interpretation of the question? "Compute angle ABC".  
Sometimes in computer graphics or specific fields, $ABC$ might refer to the projection or something? No, standard math problems assume Euclidean space unless stated otherwise.  
The coordinate geometry calculation is direct and robust.  

Let's do a quick check for alternative interpretations.  
Maybe the question implies calculating distance BC using coordinates $C-B$?  
Distance formula: $\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}$. Yes, I used that.  

Let's consider if there's a simpler way to calculate the angle between vectors.  
$\cos \theta = \frac{1}{\sqrt{54}\sqrt{54}} (-27)$.  
$(-27/54)$ is $-1/2$.  
Is there any chance that $\vec{BA} \cdot \vec{BC}$ is not negative?  
$(-2)(-5)$ is positive 10.  
$(-7)(5)$ is negative -35.  
$(1)(-2)$ is negative -2.  
Sum $10 - 35 - 2 = -27$. No sign error.  

What if I use $\cos A = \frac{\vec{AB} \cdot \vec{AC}}{|\vec{AB}| |\vec{AC}|}$?  
This would be angle at A.  
Let's check if there are any constraints to ensure the triangle is in a specific context or something. No.  

Let's just verify $\sqrt{54}$ again.  
$\sqrt{9 \times 6} = 3\sqrt{6}$.  
$3^2 = 9, 6=1+... no, 54/9=6$. $54/4 = 13.5$. No.  
$54/9 = 6$. Correct.  

Is it possible that I made a typo reading the question? "Compute angle ABC". It's standard.  
The problem asks to reason step by step.  

Step 1: Define vectors $\vec{BA}$ and $\vec{BC}$ (or just one pair of sides from point B).  
Step 2: Compute the dot product of these two vectors.  
Step 3: Compute the magnitude squared of each vector.  
Step 4: Apply the cosine formula.  

Calculations summary:  
$\vec{BA} = (-2, -7, 1)$. $|\vec{BA}|^2 = 54$.  
$\vec{BC} = (-5, 5, -2)$. $|\vec{BC}|^2 = 54$.  
$\vec{BA} \cdot \vec{BC} = 10 - 35 - 2 = -27$.  
$|\cos B| = 27 / 54 = 1/2$. Since angle must be between $0$ and $180$, $\cos B = -1/2$.  
Then $B = 120^\circ$.  

Let's double check if I am misinterpreting the dot product sign.  
If vectors are in opposite directions, they form an obtuse angle, so cosine is negative.  
$\vec{BA}$ points from $B$ to $A$. $\vec{BC}$ points from $B$ to $C$.  
The angle between them is the angle inside the triangle at B.  
Yes.  

One more check on vector subtraction:  
$A=(1, -11, 2)$, $B=(3, -4, 1)$. $BA = A - B = (-2, -7, 1)$. Correct.  
$C=(-2, 1, -1)$. $BC = C - B = (-5, 5, -2)$. Correct.  

I am confident in the result.  

Let's think if there's any tricky coordinate trick like $A, B, C$ are on a sphere or something? No, just points in space.  
Maybe using $\cos(ABC)$ directly from coordinates of vertices A, B, C?  
Using formula involving squared distances:  
$\cos \angle ABC = \frac{d^2(AB^2) + d^2(BC^2) + d^2(CA^2)}{4 AB^2 BC^2 AC^2}$. No that's for something else. It's $\frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|}$.  

Let me check if I'm missing any subtlety about "angle ABC" in a specific plane context or if the coordinates imply a 3D figure (a triangle) where angle is unique. Yes, it's an angle in a triangle. The result holds for any coordinate representation as long as points are defined.  

Let me just quickly check $x$-coordinates again:  
$A=1$, $B=3$, $C=-2$.  
Sums:  
1+3 = 4. -2? No. $1-3=-2$.  
$3+(-2)=1$. No.  
$1, 3, -2$.  
Is there any chance $A=(1, -11, 2)$ is not correct? No.  

I'll format the solution based on these steps.  
Final Answer should be boxed.  

One edge case: what if $\cos \theta = 1/2$? That would be $60^\circ$.  
Is it possible for cosine to be positive? Yes, acute angle.  
Wait, let me re-verify $|\vec{BA} \cdot \vec{BC}|$.  
If dot product was positive, angle could be acute.  
Let's check the signs again.  
$x: -2, -5$ -> $10$.  
$y: -7, 5$ -> $-35$.  
$z: 1, -2$ -> $-2$.  
Is it possible to have $x$ and $y$ such that product is positive?  
Yes, $(-2)(-5)$. But if $y=7$, product would be negative?  
Ah, vector $(0,7)$ times $(-5)$. No.  
Vector components are scalars.  
The calculation: $(-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$.  
It's definitely negative.  

Let's re-read the vector coordinates one last time to avoid silly mistakes.  
$A = (1, -11, 2)$  
$B = (3, -4, 1)$  
$C = (-2, 1, -1)$  
$\vec{BA} = A - B = (1-3, -11 - (-4), 2 - 1) = (-2, -7, 1)$  
$\vec{BC} = C - B = (-2-3, 1 - (-4), -1 - 1) = (-5, 5, -2)$  

$BA \cdot BC = (-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$.  
$|\vec{BA}|^2 = (-2)^2 + (-7)^2 + (1)^2 = 4 + 49 + 1 = 54$.  
$|\vec{BC}|^2 = (-5)^2 + (5)^2 + (-2)^2 = 25 + 25 + 4 = 54$.  

$\cos \theta = -27 / 54 = -1/2$.  
$\theta = 120^\circ$.  

Double check the arithmetic of $\sqrt{54}$.  
$3^2=9$. $6^2=36$. $4.8^2 \approx 23$.  
$7.3^2 = (7+0.3)^2 = 49 + 4.2 + 0.09 \approx 53.29$.  
$7.35^2 \approx 54$. Correct.  

Double check sum of squares for vector magnitude squareds.  
$A=(1,-11,2)$  
$B=(3,-4,1)$  
$C=(-2,1,-1)$  

Distance $AB$:  
$\Delta x = 2, \Delta y = 7, \Delta z = -1$.  
$x^2+y^2+z^2 = 4 + 49 + 1 = 54$.  
Is it $AB^2=54$? Yes.  

Distance $BC$:  
$\Delta x = 5, \Delta y = -1, \Delta z = 0$ ? No, $\Delta y = 1 - (-4) = 5$.  
$x^2+y^2+z^2 = 25 + 25 + 4 = 54$.  
Distance $AC$:  
$\Delta x = -3, \Delta y = 12, \Delta z = -3$.  
$9 + 144 + 9 = 162$.  
Is it possible I made an error in reading coordinates?  
Let me double check the user input string: "C = (-2,1,-1)."  
Yes.  

Is there any chance $\angle ABC$ refers to angle subtended by $AC$?  
No, it's defined on vertices A, B, C. The order matters.  
Angle ABC is angle at vertex B.  
In the standard convention, it is the angle between vectors pointing from B to A and B to C.  

Could there be any confusion with $\vec{CB}$ vs $\vec{BA}$?  
Vector $BA = -27$ magnitude squared 54.  
Angle $\theta$ is same as $\angle(CAB)$ or whatever.  
No, angle at B is between BA and BC.  
Vectors are $A-B$ and $C-B$.  
Is there any ambiguity?  
Usually "angle XYZ" means vectors from vertex X to Y and Z.  
So vertices of angle are B, A, C.  
Vectors $\vec{XB}$ and $\vec{XZ}$.  
No, that would be $\vec{BA}$ and $\vec{BC}$. Yes.  

I am satisfied with the calculation.  

Final check:  
$\cos \theta = -1/2$ means angle is $120^\circ$.  

The question asks to "Compute angle ABC".  
Usually degrees are requested.  
$\boxed{120}$.  

Let's do a quick check on potential typos in my manual transcription vs the prompt.  
Prompt: A=(1,-11,2), B=(3,-4,1), C=(-2,1,-1).  
My derivation used exactly these numbers.  

Is it possible that "angle ABC" is 0 or something? No, sides equal implies isosceles with base AC (or legs AB, BC). The sides are equal so triangle is isosceles with base AC?  
$AB^2 = BC^2 = 54$. Yes.  
Isosceles triangle $ABC$ with $AB=BC=\sqrt{54}$.  
So angles opposite to these sides are $\angle A = \angle C$? No, angle at A and C.  
No, base is AC. The equal sides are AB and BC. So $\angle A = \angle C$.  
Then the third angle $\angle B$ (vertex) would be $180 - 2(\text{angle}_A)$?  
In an isosceles triangle with legs AB and BC:  
$\angle A + \angle C + \angle B = 180$.  
Since $\angle A = \angle C$, then $\angle B + 2\angle A = 180$.  
$AB=BC \implies \cos(A) = AC/AB \times AC / AB$?  
No, Law of Cosines: $AC^2 = AB^2 + BC^2 - 2(AB)(BC)\cos(B)$.  
Here $\angle B$ is angle between vectors.  
The sides are AB and BC, so opposite angles are A and C? No. Sides $a, b, c$. Opposite to a is A, to b is C, to c is B.  
No, in triangle $ABC$, sides are $c = AB$, $b = BC$, $a = AC$.  
Since $AB^2 = 54$ and $BC^2 = 54$, then $c=b$.  
Using Law of Cosines for side AC ($a$):  
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
