# test/precalculus/580.json (Precalculus, level 3)

> Let $A = (1,-11,2),$ $B = (3,-4,1),$ and $C = (-2,1,-1).$  Compute $\angle ABC,$ in degrees.  

**Wrong.** Gold `120^\circ`, predicted `\cos \theta = \frac{-27}{\sqrt{54} \cdot \sqrt{54}}`. Finish: length, 8192 tokens, 2 waits, 1286.0 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here is the problem:  
We are given three points in 3D space: $A = (1, -11, 2)$, $B = (3, -4, 1)$, and $C = (-2, 1, -1)$.  
We need to compute the angle $\angle ABC$ formed by the vectors $\vec{BA}$ and $\vec{BC}$.  

Step 1: Identify the vectors representing the sides of the triangle starting from vertex B.  
The vector corresponding to side $c$ is usually $\vec{a} \cdot \vec{b}$ where $A$ and $B$ are points on a line, but for an angle at vertex $B$, we need vectors originating from $B$.  
Vector $\vec{BA} = A - B$.  
Vector $\vec{BC} = C - B$.  

Let's calculate $\vec{BA}$:  
$x_{\vec{BA}} = x_A - x_B = 1 - 3 = -2$  
$y_{\vec{BA}} = y_A - y_B = -11 - (-4) = -11 + 4 = -7$  
$z_{\vec{BA}} = z_A - z_B = 2 - 1 = 1$  
So, $\vec{BA} = \langle -2, -7, 1 \rangle$.  

Let's calculate $\vec{BC}$:  
$x_{\vec{BC}} = x_C - x_B = -2 - 3 = -5$  
$y_{\vec{BC}} = y_C - y_B = 1 - (-4) = 1 + 4 = 5$  
$z_{\vec{BC}} = z_C - z_B = -1 - 1 = -2$  
So, $\vec{BC} = \langle -5, 5, -2 \rangle$.  

Step 2: Compute the dot product of these two vectors.  
$\vec{BA} \cdot \vec{BC} = (x_{\vec{BA}})(x_{\vec{BC}}) + (y_{\vec{BA}})(y_{\vec{BC}}) + (z_{\vec{BA}})(z_{\vec{BC}})$  
$\vec{BA} \cdot \vec{BC} = (-2)(-5) + (-7)(5) + (1)(-2)$  
$= 10 - 35 - 2$  
$= 10 - 37$  
$= -27$.  

Step 3: Compute the magnitudes (lengths) of these two vectors.  
$\|\vec{BA}\| = \sqrt{(-2)^2 + (-7)^2 + (1)^2}$  
$= \sqrt{4 + 49 + 1}$  
$= \sqrt{54}$  

$\|\vec{BC}\| = \sqrt{(-5)^2 + (5)^2 + (-2)^2}$  
$= \sqrt{25 + 25 + 4}$  
$= \sqrt{54}$  

Interesting, the lengths are equal. This means triangle ABC is an isosceles right-angled triangle? No, it's just isosceles. Let's recheck the arithmetic.  
$\vec{BA} = (-2, -7, 1)$. $(-2)^2 + (-7)^2 + 1^2 = 4 + 49 + 1 = 54$. Correct.  
$\vec{BC} = (-5, 5, -2)$. $(-5)^2 + (5)^2 + (-2)^2 = 25 + 25 + 4 = 54$. Correct.  

Step 4: Use the dot product formula to find $\cos \theta$, where $\theta$ is the angle between $\vec{BA}$ and $\vec{BC}$.  
$\cos \theta = \frac{\vec{BA} \cdot \vec{BC}}{\|\vec{BA}\| \|\vec{BC}\|}$  

Substitute the values:  
$\vec{BA} \cdot \vec{BC} = -27$  
$\|\vec{BA}\| = \sqrt{54}$  
$\|\vec{BC}\| = \sqrt{54}$  

$\cos \theta = \frac{-27}{\sqrt{54} \cdot \sqrt{54}} = \frac{-27}{54} = -\frac{1}{2}$.  

Step 5: Find the angle $\theta$ using $\cos^{-1}(-1/2)$.  
Since $-1 < -1/2 \le 1$, an inverse cosine exists.  
We know that $\cos(60^\circ) = 1/2$.  
So $\cos(\pi - \pi/3)$? No, cosine is in the second quadrant.  
$\cos(120^\circ) = -\frac{1}{2}$. Or $2\pi/3$ radians.  

Let's convert to degrees:  
$\theta = 180^\circ - 60^\circ = 120^\circ$.  

Alternatively, $\theta = \arccos(-0.5) = 120^\circ$.  

Is it possible I misread the coordinates?  
$A = (1,-11,2)$  
$B = (3,-4,1)$  
$C = (-2,1,-1)$  

Vectors:  
$\vec{BA} = A - B = (1-3, -11-(-4), 2-1) = (-2, -7, 1)$  
$\vec{BC} = C - B = (-2-3, 1-(-4), -1-1) = (-5, 5, -2)$  

Dot product: $(-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$. Correct.  
Magnitudes: $\sqrt{4+49+1} = \sqrt{54}$, $\sqrt{25+25+4} = \sqrt{54}$. Correct.  

Calculation of cosine: $-27/54 = -0.5$. Correct.  
Angle: $\arccos(-0.5) = 120^\circ$.  

Is there any ambiguity? "angle ABC" means the interior angle at vertex B. The formula $\theta = \arccos(\frac{\vec{BA}\cdot\vec{BC}}{|\vec{BA}||\vec{BC}|})$ gives exactly this angle. Since it's between vectors from $B$, it is the internal angle of the triangle formed by points A, B, C in 3D space.  

Let's double check the calculations just to be safe.  
$y_A - y_B = -11 - (-4) = -7$. Correct.  
$x_C - x_B = -2 - 3 = -5$. Correct.  
$z_C - z_B = -1 - 1 = -2$. Correct.  

Maybe I should convert to degrees as requested. The result is $120^\circ$.  

Is there any other interpretation? Maybe the order of points matters for orientation? No, angle is unsigned magnitude of turn between two rays meeting at B.  
The triangle sides are $c$, $a$, $b$ relative to vertices $A, B, C$ respectively in standard notation $\triangle ABC$, but here the angle requested is $\angle ABC$, which corresponds to vector $\vec{BA}$ and $\vec{BC}$.  
Everything seems consistent.  

Let's quickly check if there's a typo in my manual calculation of the dot product.  
$(-2)(-5) = 10$  
$(-7)(5) = -35$  
$(1)(-2) = -2$  
Sum: $10 - 35 - 2 = -27$. Yes.  

Let's check magnitude calculation again.  
$\sqrt{54} \approx 7.348$.  
$-27 / (54)$ is correct.  
So angle is definitely related to cosine of -60 degrees or something else? No, $\cos \alpha = x$, find angle.  
If $\cos \alpha = -1/2$, then $\alpha = 120^\circ$.  

Let's verify the points again just in case I'm crazy.  

```text
A=(1,-11,2)
B=(3,-4,1)
C=(-2,1,-1)
```

$\vec{BA} = (-2, -7, 1)$  
$\vec{BC} = (-5, 5, -2)$  

Cross product to check?  
$\vec{BA} \times \vec{BC}$ should be perpendicular.  
Determinant of matrix with rows $\vec{BA}, \vec{BC}, \vec{k}$.  
$\begin{vmatrix} i & j & k \\ -2 & -7 & 1 \\ -5 & 5 & -2 \end{vmatrix}$  
$i$-component: $(-7)(-2) - (1)(5) = 14 - 5 = 9$.  
$j$-component: $-( (-2)(-2) - (1)(-5) ) = -( 4 - (-5) ) = -( 9 ) = -9$.  
$k$-component: $(-2)(5) - (-7)(-5) = -10 - 35 = -45$.  
Cross product $\vec{n} = \langle 9, -9, -45 \rangle$.  
Let's check if it's perpendicular to $\vec{BA}$.  
$\langle -2, -7, 1 \rangle \cdot \langle 9, -9, -45 \rangle = (-2)(9) + (-7)(-9) + (1)(-45) = -18 + 63 - 45 = 0$. Correct.  
Let's check perpendicular to $\vec{BC}$.  
$\langle -5, 5, -2 \rangle \cdot \langle 9, -9, -45 \rangle = (-5)(9) + (5)(-9) + (-2)(-45) = -45 - 45 + 90 = -90 + 90 = 0$. Correct.  

The dot product calculation was $\vec{BA} \cdot \vec{BC}$.  
In my manual check, I can recompute using cross product to see if the angle is related? No, simpler to stick to cosine.  
The vectors are non-zero, so angle is defined.  

Is it possible that $\cos \theta$ should be something else?  
Maybe checking with a different method.  
Let coordinates be $A, B, C$.  
$\vec{AB} = (2, 7, -1)$, $\vec{AC} = (-3, 12, -3)$.  
Lengths:  
$\|\vec{AB}\|^2 = 4 + 49 + 1 = 54$.  
$\|\vec{AC}\|^2 = 9 + 144 + 9 = 162$.  
$\vec{AB} \cdot \vec{AC} = (2)(-3) + (7)(12) + (-1)(-3) = -6 + 84 + 3 = 81$.  
Use cosine rule on triangle ABC:  
$AC^2 = AB^2 + BC^2 - 2(AB)(BC) \cos C$ ? No, usually we want angle between $BA$ and $BC$, which is angle at B.  
Law of Cosines for Angle B:  
$AC^2 = AB^2 + BC^2 - 2(AB)(BC) \cos(\angle B)$  
Here $\vec{BA} = \vec{C-B}$ is not a side length, but the vectors connecting vertices.  
Let $a, b, c$ be lengths of sides $BC$, $CA$, $AB$.  
Lengths squared:  
$c^2 = AB^2 = 54$.  
$b^2 = AC^2 = 162$. (Let's recheck A-C)  
$x_A - x_C = 1 - (-2) = 3$  
$y_A - y_C = -11 - 1 = -12$  
$z_A - z_C = 2 - (-1) = 3$  
Sum of squares: $9 + 144 + 9 = 162$. Correct.  
$a^2 = BC^2 = 54$. (Recheck B-C)  
We calculated this before as 54. Correct.  

Equation:  
$b^2 = c^2 + a^2 - 2ac \cos B$  
$162 = 54 + 54 - 2(54) \cos B$ (Note $a=BC$, $c=AB$? No, standard notation is $a$ opposite A, $b$ opposite B, $c$ opposite C. But here angles are between segments connecting to vertices.  
Side lengths are:  
$c_{side} = AB = 54^{1/2}$  
$a_{side} = BC = 54^{1/2}$ (No, let's call them side u and v).  
Lengths of AB is $\sqrt{54}$. Lengths of BC is $\sqrt{54}$.  
Let $x = AB$, $y = BC$. We have $x=y$.  
We need angle B. Let's look at $\triangle ABC$.  
Sides are $AB, BC, CA$.  
$AB^2 = 54$.  
$BC^2 = 54$.  
$AC^2 = 162$.  
Using Law of Cosines:  
$AC^2 = AB^2 + BC^2 - 2(AB)(BC) \cos(\angle ABC)$  
$162 = 54 + 54 - 2(AB)(BC) \cos B$  
$162 = 108 - 2(54^{1/2})(54^{1/2}) \cos B$  
$162 = 108 - 54(2) \cos B$ (Since $x^2+y^2=x y$ is not what we want, it's just product of squared lengths).  
Let's use the vectors for angle directly. It was easier.  
The dot product calculation gave $\cos B = \frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|}$.  
$\vec{BA}$ connects $B$ to $A$. Length is $c_{side}$.  
$\vec{BC}$ connects $B$ to $C$. Length is $a_{side}$.  
The formula for angle between $\vec{BA}$ and $\vec{BC}$ is correct.  
Calculation:  
Dot product was -27.  
Lengths were $\sqrt{54}, \sqrt{54}$.  
Product of lengths is 54.  
$\cos B = -27 / 54 = -1/2$.  
$B = 120^\circ$.  

Let me recheck the law of cosines substitution step carefully.  
The term $-2(AB)(BC) \cos B$ corresponds to vector dot product relation?  
Vectors are $\vec{BA}$ and $\vec{BC}$.  
$\vec{BA} \cdot \vec{BC} = |\vec{BA}| |\vec{BC}| \cos B$.  
So $\cos B = \frac{-27}{54}$.  
Then $-162 + 108 - 108$ ? No.  
From Law of Cosines: $b^2 = c^2 + a^2 - 2ca \cos B$. Here $a=BC$, $c=AB$. The angle is at $B$.  
So $AC^2 = AB^2 + BC^2 - 2(AB)(BC) \cos B$.  
$162 = 54 + 54 - 2(\sqrt{54})(\sqrt{54}) \cos B$.  
$162 = 108 - 2(54) \cos B$. (Assuming product of lengths is $|\vec{BA}||\vec{BC}| = \sqrt{54}\sqrt{54}=54$).  
So $162 = 108 - 2(54) \cos B$ ? No.  
$\vec{BA}$ and $\vec{BC}$ have lengths $\sqrt{54}$.  
The dot product is $\vec{BA} \cdot \vec{BC} = -27$.  
So $-27 = (\sqrt{54})(\sqrt{54}) \cos B = 54 \cos B$.  
$162 + 2(54) \cos B = 54+54+...$ No.  
$AB^2 = 54$, $BC^2 = 54$, $AC^2 = 162$.  
From $\vec{BA} \cdot \vec{BC}$:  
$\vec{BA} \cdot \vec{BC} = -27$.  
$\|\vec{BA}\| \|\vec{BC}\| = \sqrt{54} \sqrt{54} = 54$.  
So $\cos B = -27 / 54 = -1/2$. $B = 120^\circ$.  

Now check the Law of Cosines relation:  
$AC^2 = AB^2 + BC^2 - 2(AB)(BC) \cos(\angle ABC)$  
$162 = 54 + 54 - 2(\sqrt{54})(\sqrt{54}) (-1/2)$  
$162 = 108 + (2)(54)/2 = 108 + 54 = 162$.  
This is consistent.  

Let's re-read the coordinates just to be paranoid.  
$A = (1,-11,2)$  
$B = (3,-4,1)$  
$C = (-2,1,-1)$  
$\vec{BA} = A-B = (1-3, -11-(-4), 2-1) = (-2, -7, 1)$.  
$(-2)^2 + (-7)^2 + 1^2 = 4+49+1 = 54$. Correct.  
$\vec{BC} = C-B = (-2-3, 1-(-4), -1-1) = (-5, 5, -2)$.  
$(-5)^2 + (5)^2 + (-2)^2 = 25+25+4 = 54$. Correct.  
Dot product: $(-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$. Correct.  

Everything seems correct. The answer is $120^\circ$.  

Double check if there are any tricks with "in degrees".  
Usually inverse trig functions give radians in math libraries, but asking for degrees implies final output should be in degrees.  
The question asks to "Compute $\angle ABC,$ in degrees."  

Are there alternative interpretations?  
Could $A,B,C$ be vectors from origin? No, usually $(x,y,z)$ notation means position vector if not specified as free space coordinates?  
But then the problem would say $A, B, C$ are position vectors. The notation $A=(...)$ usually denotes coordinates in $\mathbb{R}^3$.  
If they were position vectors from origin, points are same. Distance between $A$ and $B$ is $|\vec{b}-\vec{a}|$ if interpreted as position vectors? No, usually coordinates are given.  
Let's assume standard Cartesian coordinates.  

Could the question be 2D? $z$ components are different.  
Points are in $\mathbb{R}^3$. So triangle is in 3D space (not necessarily planar with z-axis?).  
If points are coplanar, they form a triangle in 3D space. The angle is still defined.  
If not coplanar... well any three points define a plane and thus form a triangle (degenerate or not) in Euclidean space. $\angle ABC$ is the angle between vectors from B to A and B to C. This angle is always well-defined.  

Final check of the question text "Compute $\angle ABC,$ in degrees."  
Is it possible the order of subtraction was $B-A$ and $B-C$? No, angle at vertex $B$. Vectors must originate at $B$.  
So $\vec{BA}$ and $\vec{BC}$.  

Let's write down the steps for the final response.  
1. Define vectors $\vec{BA}$ and $\vec{BC}$.  
2. Calculate magnitudes $|\vec{BA}|$ and $|\vec{BC}|$.  
3. Calculate dot product $\vec{BA} \cdot \vec{BC}$.  
4. Use formula $\cos B = \frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|}$ to find $\cos B$.  
5. Compute angle $B$ in degrees.  

Calculations recap:  
$\vec{BA} = (-2, -7, 1)$  
$\vec{BC} = (-5, 5, -2)$  
$|\vec{BA}|^2 = 4 + 49 + 1 = 54$. $|\vec{BA}| = \sqrt{54}$.  
$|\vec{BC}|^2 = 25 + 25 + 4 = 54$. $|\vec{BC}| = \sqrt{54}$.  
$\vec{BA} \cdot \vec{BC} = 10 - 35 - 2 = -27$.  
$\cos B = \frac{-27}{\sqrt{54}\sqrt{54}} = -\frac{27}{54} = -\frac{1}{2}$.  
$B = \arccos(-1/2)$.  
Since $-1 < -1/2$, angle is in quadrant II (for $0 \le \theta \le 180^\circ$).  
$\cos(120^\circ) = -0.5$.  
Thus $B = 120^\circ$.  

Seems robust.  

One minor thing: Is it possible the problem implies a 2D projection? No "in 3D space" or just coordinates in $\mathbb{R}^3$ are given. The formula for angle works regardless of dimension, as long as vectors are defined properly.  
Are they collinear? $1-2 \approx 0.5$. $\sqrt{54}$ vs $|\vec{AB}| = \sqrt{54}$. No.  

Let's quickly check if there is any common pitfall.  
Vectors pointing *away* from B. Yes, $\vec{BA}$ and $\vec{BC}$.  
If it was $\vec{BC}$ and $\vec{AB}$, it would be the same magnitude vectors (since angle between lines is usually considered acute/obtuse based on internal geometry). The dot product with reversed vector flips sign of dot product. $-\cos B = 1/2 \implies \cos(-B) = -\cos B$. Angle between $\vec{AB}$ and $\vec{BC}$? $\vec{BA} = -\vec{AB}$. Dot product is $-27$ vs dot product of $\vec{BC}$ and $\vec{AB}$ which would be $10+35-2=43$??  
Let's check.  
$\vec{AB} = (2, 7, -1)$.  
$\vec{BC} = (-5, 5, -2)$.  
Dot: $(2)(-5) + (7)(5) + (-1)(-2) = -10 + 35 + 2 = 27$.  
This is positive.  
If we took $\vec{BA}$ and $\vec{BC}$ dot product was $-27$.  
So $\cos \theta = \frac{-27}{54} = -0.5$.  
If we took angle between vectors from B to C and B to A, it's $120^\circ$.  
Let's visualize coordinates roughly.  
A=(1,-11,2) -> roughly (1, -11, 2) [Left, Down, Up] relative to origin? No, just position.  
B=(3,-4,1) -> Center.  
C=(-2,1,-1) -> Left.  
$y_A = -11$, $y_B = -4$. So A is much lower than B.  
$x_C = -2$, $x_B = 3$. C is to left of B.  
$z_C = -1$, $z_B = 1$. C is below B.  
Let's check the displacement from B to A: $\Delta y = -7$, very large negative.  
Displacement B to C: $\Delta y = 5$, positive. $\Delta x = -5, -2$ (left).  
So vector BA goes "mostly down" and slightly left/right?  
Vector (-2, -7, 1). Down is mostly component. Left. Slightly Up.  
Vector BC goes Right to Left? No x decreases from 3 to -5 (-5-(-5)?). $x_C=-2$, $x_B=3$. So $x$ changes by $-5$. Yes, moving left.  
$y$ changes by $1-(-4)=5$. Up or Down? Wait, $y_A=-11$, $y_C=1$. $C$ is above origin but below B ($y_B=-4$). No.  
$y_B = -4$. $y_C = 1$. $y_A = -11$.  
So relative to B:  
$y$ component of BA is $-7$. (Down)  
$y$ component of BC is $5$. (Up?) No, $1 - (-4) = 5$. So Up.  
$z$ component of BA is $1$. (Right).  
$z$ component of BC is $-2$. (Left).  
So from B(3, -4, 1):  
A is at $(1, -11, 2)$ -> x: $1-3=-2$ (L), y: $-11-(-4)=-7$ (D), z: $2-1=1$ (U).  
C is at $(-2, 1, -1)$ -> x: $-2-3=-5$ (L), y: $1-(-4)=5$ (U), z: $-1-1=-2$ (D).  

Let's look at components:  
Vector BA: L(2 units), D(7 units), U(1 unit).  
Vector BC: L(5 units), U(5 units), D(2 units).  

Visual estimation:  
BA points "Down" quite a bit. BC points "Up".  
To close the loop B->A->C back to B?  
If I walk from B to A, I am going down a lot.  
Then I turn to C.  
If BA is roughly South-West-North-East...  
Let's just trust the math.  
Dot product negative means angle > 90 degrees.  
Since lengths are equal ($\sqrt{54}$), it implies an isosceles triangle.  
An isosceles triangle with base AC and vertex B? No, $AB = BC$. Yes, since magnitudes of BA and BC are $\sqrt{54}$.  
Triangle has equal sides AB and BC. So isosceles at B.  
We have a base AC.  
The length of the third side $AC$ is $\sqrt{162} = 3\sqrt{18}$? No, $9+144+9 = 162$. $162 = 81 \times 2 = (9)^2 \times 2$. So $\sqrt{162} = 9\sqrt{2}$.  
Sides are $\sqrt{54} = 3\sqrt{6}$ and $3\sqrt{6}$.  
Triangle sides: $a=3\sqrt{6}, b=3\sqrt{6}, c=9\sqrt{2}$.  
Let's check triangle inequality.  
$\sqrt{54} + \sqrt{54} = 2\sqrt{54} = 2(3\sqrt{18})$? No $\sqrt{54} \approx 7.35$. Sum $\approx 14.7$. $c = 9(1.414) \approx 12.7$.  
Triangle inequality holds.  
Is it a right triangle?  
If isosceles with equal legs, angle at B determines if the base is perpendicular to bisector. Bisector length squared?  
In an isosceles triangle $AB=BC=a$, $AC=b$. Height to AC divides AC into two parts.  
$\cos(120^\circ) = -0.5$. So angle is obtuse.  
Is it right angled? No, $\cos B = -1/2$. If it were right angled at B, $\cos B = 0$.  
If right angled at A: $BC^2 = AB^2 + AC^2$? $54 = 54 + 162$ False.  
If right angled at C: $AB^2 = BC^2 + AC^2$? $54 = 54 + 162$ False.  
So it's just an obtuse isosceles triangle.  

Are there any subtle points?  
Coordinates check again.  
A(1,-11,2). B(3,-4,1). C(-2,1,-1).  
$y_A - y_B = -7$. $y_C - y_B = 5$.  
Is it possible that $\vec{BA} \cdot \vec{BC}$ should be calculated with coordinates swapped?  
$\vec{AB} = (2, 7, -1)$.  
$\vec{CB} = (5, -5, 2)$.  
Dot product: $(2)(5) + (7)(-5) + (-1)(2) = 10 - 35 - 2 = -27$. Same result.  
Magnitude $\vec{AB}$ is same as magnitude of $\vec{BA}$.  
Magnitude $\vec{CB}$ is same as magnitude of $\vec{BC}$.  
Angle between $\vec{AB}$ and $\vec{CB}$ is angle $B$.  
$\cos B = -27 / 54 = -1/2$.  
The calculation is consistent.  

Final answer seems to be 120 degrees.  

One check on the text formatting "Compute $\angle ABC,$ in degrees."  
Is there any ambiguity with "Compute"? It just asks for the number.  
I will provide the steps clearly.  

Steps:  
1. Find vectors $\vec{BA}$ and $\vec{BC}$.  
$\vec{BA} = A - B = (1-3, -11-(-4), 2-1) = (-2, -7, 1)$  
$\vec{BC} = C - B = (-2-3, 1-(-4), -1-1) = (-5, 5, -2)$  
2. Calculate magnitudes squared: $|\vec{BA}|^2 = (-2)^2 + (-7)^2 + 1^2 = 4 + 49 + 1 = 54$. So $|\vec{BA}| = \sqrt{54}$.  
$|\vec{BC}|^2 = (-5)^2 + 5^2 + (-2)^2 = 25 + 25 + 4 = 54$. So $|\vec{BC}| = \sqrt{54}$.  
3. Calculate dot product: $\vec{BA} \cdot \vec{BC} = (-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$.  
4. Apply cosine rule formula: $\cos \theta = \frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|}$.  
$\cos \theta = \frac{-27}{\sqrt{54}\sqrt{54}} = \frac{-27}{54} = -0.5$.  
5. Determine angle: $\theta = \arccos(-0.5) = 120^\circ$.  

Looks solid.  

Is there any chance "in degrees" implies radians in the output? No, usually explicitly requested as degrees means $^\circ$.  
Also "Compute" suggests a numerical value or simplified expression. $120$ is an integer.  
If I had to express it in terms of arccos... but "in degrees" implies numerical.  

Final check:  
Does the problem statement imply a coordinate system? Yes, $(x,y,z)$.  
Is it Euclidean space? Standard assumption.  
Is there any ambiguity about $\angle ABC$ being external or internal? The interior angle is standard.  

Calculation check 2:  
$(-7)(5) = -35$. Correct.  
$(1)(-2) = -2$. Correct.  
$(-2)(-5) = 10$. Correct.  
Sum $-27$. Correct.  
$49+4=53$, $53+1=54$. Correct.  
$25+25=50$, $50+4=54$. Correct.  
$\sqrt{54}/\sqrt{54} = 1$.  
$-27/54 = -1/2$.  
$\arccos(-1/2) = 120^\circ$.  
Seems perfectly correct.  

I will formulate the response now.  


## Answer

To find the angle $\angle ABC$, we need to consider the vectors representing the sides of the triangle originating from vertex $B$. Specifically, these are the vectors $\vec{BA}$ and $\vec{BC}$.  

**Step 1: Determine the vectors $\vec{BA}$ and $\vec{BC}$.**  
We are given the coordinates of points $A$, $B$, and $C$:  
$A = (1, -11, 2)$  
$B = (3, -4, 1)$  
$C = (-2, 1, -1)$  

The vector $\vec{BA}$ is calculated as $\mathbf{a} = A - B$:  
$$ \vec{BA} = (1 - 3, -11 - (-4), 2 - 1) = (-2, -7, 1) $$  

The vector $\vec{BC}$ is calculated as $\mathbf{b} = C - B$:  
$$ \vec{BC} = (-2 - 3, 1 - (-4), -1 - 1) = (-5, 5, -2) $$  

**Step 2: Calculate the magnitudes (lengths) of these vectors.**  
$$ |\vec{BA}| = \sqrt{(-2)^2 + (-7)^2 + 1^2} = \sqrt{4 + 49 + 1} = \sqrt{54} $$  
$$ |\vec{BC}| = \sqrt{(-5)^2 + (5)^2 + (-2)^2} = \sqrt{25 + 25 + 4} = \sqrt{54} $$  

**Step 3: Calculate the dot product $\vec{BA} \cdot \vec{BC}$.**  
$$ \vec{BA} \cdot \vec{BC} = (-2)(-5) + (-7)(5) + (1)(-2) $$  
$$ = 10 - 35 - 2 $$  
$$ = -27 $$  

**Step 4: Use the dot product formula to find $\cos \angle ABC$.**  
Let $\theta$ be the angle $\angle ABC$. According to the dot product definition for vectors of equal magnitude (or just general vectors), $\vec{u} \cdot \mathbf{v} = |\mathbf{u}| |\mathbf{v}| \cos \theta$. Here, $|\vec{BA}| = \sqrt{54}$ and $|\vec{BC}| = \sqrt{54}$.  

$$ \cos \theta = \frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|} $$  
$$ \cos \theta = \frac{-27}{\sqrt{54} \cdot \sqrt{54}} $$  
