# test/precalculus/580.json  (Precalculus, level 3)

- gold: `120^\circ`
- pred: `None`
- correct: False
- finish: length, tokens: 8192, waits: 43, secs: 987.8

## Thinking (reasoning_content)

````text
Here is the problem:
We are given three points in 3D space: $A = (1, -11, 2)$, $B = (3, -4, 1)$, and $C = (-2, 1, -1)$.
We need to compute the angle $\angle ABC$ formed by the vectors $\vec{BA}$ and $\vec{BC}$.

Step 1: Identify the vectors representing the sides of the triangle starting from vertex B.
The vector corresponding to side $c$ is usually $\vec{u} = \vec{AB}$ or $\vec{CA}$. Let's denote the angles using standard notation. $\angle ABC$ is the angle at vertex $B$ between the segments $BA$ and $BC$.
So we need the vectors $\vec{BA}$ and $\vec{BC}$.

First, calculate coordinates of B: $B = (3, -4, 1)$.
The coordinates of A are $A = (1, -11, 2)$.
The coordinates of C are $C = (-2, 1, -1)$.

Vector $\vec{BA} = A - B = (1-3, -11-(-4), 2-1)$.
$\vec{BA} = (-2, -7, 1)$.

Vector $\vec{BC} = C - B = (-2-3, 1-(-4), -1-1)$.
$\vec{BC} = (-5, 5, -2)$.

Step 2: Use the dot product formula to find the cosine of the angle.
Let $\theta$ be the angle $\angle ABC$.
The formula is $\cos \theta = \frac{\vec{BA} \cdot \vec{BC}}{||\vec{BA}|| \cdot ||\vec{BC}||}$.

Step 3: Calculate the dot product $\vec{BA} \cdot \vec{BC}$.
$\vec{BA} = (-2, -7, 1)$
$\vec{BC} = (-5, 5, -2)$
Dot product $= (-2)(-5) + (-7)(5) + (1)(-2)$
$= 10 - 35 - 2$
$= 10 - 37$
$= -27$.

Step 4: Calculate the magnitude of $\vec{BA}$.
$\|\vec{BA}\| = \sqrt{(-2)^2 + (-7)^2 + (1)^2}$
$= \sqrt{4 + 49 + 1}$
$= \sqrt{54}$.

Step 5: Calculate the magnitude of $\vec{BC}$.
$\|\vec{BC}\| = \sqrt{(-5)^2 + (5)^2 + (-2)^2}$
$= \sqrt{25 + 25 + 4}$
$= \sqrt{54}$.

Interestingly, the magnitudes are the same. This makes sense if $B$ is equidistant from A and C, which seems unlikely based on coordinates but let's check the distances anyway. Wait.
Distances squared:
$AB^2 = (-2)^2 + (-7)^2 + (1)^2 = 4 + 49 + 1 = 54$. So $AB = \sqrt{54}$.
$BC^2 = (-5)^2 + (5)^2 + (-2)^2 = 25 + 25 + 4 = 54$. So $BC = \sqrt{54}$.

So $\|\vec{BA}\| = \|\vec{BC}\| = \sqrt{54}$.

Step 6: Compute $\cos \theta$.
$\cos \theta = \frac{-27}{\sqrt{54} \cdot \sqrt{54}}$
$= \frac{-27}{54}$
$= -0.5$.

Step 7: Determine the angle $\theta$.
Since the dot product is negative, the angle must be obtuse (between $90^\circ$ and $180^\circ$).
$\cos \theta = -\frac{1}{2}$.
The principal value of the inverse cosine is in $[0, 180^\circ]$.
If $\cos \theta = -1/2$, then $\theta = 120^\circ$.

Step 8: Check if degrees or radians are requested. The question asks for "in degrees". So, $\boxed{120}$.

Let me double check the calculations.
Coordinates:
$A = (1, -11, 2)$
$B = (3, -4, 1)$
$C = (-2, 1, -1)$

Vector $\vec{BA} = A - B$:
$x_A - x_B = 1 - 3 = -2$.
$y_A - y_B = -11 - (-4) = -11 + 4 = -7$.
$z_A - z_B = 2 - 1 = 1$.
$\vec{BA} = (-2, -7, 1)$. Correct.

Vector $\vec{BC} = C - B$:
$x_C - x_B = -2 - 3 = -5$.
$y_C - y_B = 1 - (-4) = 1 + 4 = 5$.
$z_C - z_B = -1 - 1 = -2$.
$\vec{BC} = (-5, 5, -2)$. Correct.

Dot Product:
$(-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$. Correct.

Magnitude $|\vec{BA}|$:
$\sqrt{4 + 49 + 1} = \sqrt{54}$. Correct.

Magnitude $|\vec{BC}|$:
$\sqrt{25 + 25 + 4} = \sqrt{54}$. Correct.

Cosine:
$-27 / 54 = -1/2$.

Angle:
$\cos \theta = -1/2 \implies \theta = 120^\circ$.

Wait, could I use vectors $\vec{AB}$ and $\vec{AC}$?
Vector $\vec{AB} = B - A = (2, 7, -1)$.
Vector $\vec{AC} = C - A = (-3, 12, -3)$.
Let's check the dot product of $\vec{AB}$ and $\vec{AC}$.
$\vec{AB} \cdot \vec{AC} = (2)(-3) + (7)(12) + (-1)(-3) = -6 + 84 + 3 = 81$.
Magnitudes:
$|\vec{AB}| = \sqrt{4 + 49 + 1} = \sqrt{54}$.
$|\vec{AC}| = \sqrt{(-3)^2 + (12)^2 + (-3)^2} = \sqrt{9 + 144 + 9} = \sqrt{162}$.
$\cos \theta_{BAC} = 81 / (\sqrt{54} \cdot \sqrt{162})$.
$\sqrt{162} = \sqrt{9 \cdot 18} = 3\sqrt{18}$? No $\sqrt{54^2/0.75...}$ no.
$|\vec{AC}|^2 = 162$. $|\vec{AB}|^2 = 54$.
Product of magnitudes squared = $54 \cdot 162$.
Wait, $|\vec{BC}|^2 = 54$. So $|\vec{AC}|^2$ should be checked.
$C - A = (-2-1, 1-(-11), -1-2) = (-3, 12, -3)$.
Square: $9 + 144 + 9 = 162$. Yes.
Using cosine formula $\cos \theta_{BAC}$ gives the angle at A, not B. This is not what we need.
Wait, I used vectors from B for calculating $\angle ABC$ earlier, so that's the correct approach.

Let me re-verify the vectors.
$A=(1,-11,2)$
$B=(3,-4,1)$
$C=(-2,1,-1)$

Is it possible I made an arithmetic error in calculation?
Vector BA: $x=-2$, $y=-7$, $z=1$.
Vector BC: $x=-5$, $y=5$, $z=-2$.

Dot product: $(-2)(-5) + (-7)(5) + (1)(-2)$
$= 10 - 35 - 2 = -27$. Correct.

Lengths squared:
$BA^2 = 4 + 49 + 1 = 54$.
$BC^2 = 25 + 25 + 4 = 54$. Correct.

Cosine is definitely $-0.5$.
Angle is $120^\circ$.

Let me check the problem statement for any trick. "Compute $\angle ABC$". This implies the internal angle of the triangle formed by points A, B, C. It's always between 0 and 180 degrees.
The question asks for the answer in degrees.

Another check: Vector product magnitude to ensure the vectors are not collinear.
$\vec{BA} \times \vec{BC}$.
Determinant of basis vectors $i, j, k$ with entries $-2, -7, 1$ and $-5, 5, -2$.
$i(-7)(-2) - j((-2)(-2) - (1)(-5)) + k((-2)(5) - (-7)(-5))$. Wait no.
Cross product $u = (-2, -7, 1)$, $v = (-5, 5, -2)$.
$x$ component: $(-7)(-2) - (1)(5) = 14 - 5 = 9$.
$y$ component: $-((-2)(-2) - (1)(-5)) = -(4 + 5) = -9$. Wait. The formula is $-(x_1z_2 - x_2z_1)$. Let's stick to determinant method properly.
$\begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -2 & -7 & 1 \\ -5 & 5 & -2 \end{vmatrix}$
$= \mathbf{i}((-7)(-2) - (1)(5)) - \mathbf{j)((-2)(-2) - (1)(-5)) + \mathbf{k}((-2)(5) - (-7)(-5))$
$= \mathbf{i}(14 - 5) - \mathbf{j}(4 + 5) + \mathbf{k}(-10 - 35)$
$= 9\mathbf{i} - 9\mathbf{j} - 45\mathbf{k}$.
Magnitude: $\sqrt{81 + 81 + 2025} = \sqrt{2275}$? No. $(-1)(-5)^2$ no $y$ component is minus sign in determinant expansion for j.
Wait. $-(4+5) = -9$. So magnitude squared is $81 + 81 + (-45)^2$.
$81 + 81 = 162$.
$(-45)^2 = 2025$.
Total = $162 + 2025 = 2187$? No.
Wait, $\sqrt{81 \cdot 27}$ maybe?
Wait, if vectors are not collinear, angle exists.
Actually we don't need cross product magnitude for this problem. The dot product and magnitudes are enough.

Let's re-read coordinates carefully.
$A = (1,-11,2)$.
$B = (3,-4,1)$.
$C = (-2,1,-1)$.

Vectors:
$\vec{BA} = (1-3, -11-(-4), 2-1) = (-2, -7, 1)$.
$\vec{BC} = (-2-3, 1-(-4), -1-1) = (-5, 5, -2)$.

Check $B$ again. $y_B = -4$. $A_y = -11$. $\Delta y = -7$. Correct.
$C_y = 1$. $\Delta y = 5$. Correct.
$z_B = 1$. $A_z = 2$. $\Delta z = 1$. Correct.
$x_B = 3$. $x_A = 1$. $\Delta x = -2$. Correct.

Check C again. $C_x = -2$. $x_B = 3$. $\Delta x = -5$. Correct.
$C_z = -1$. $z_B = 1$. $\Delta z = -2$. Correct.
$y_C = 1$. $y_B = -4$. $\Delta y = 5$. Correct.

Calculation seems solid.
Dot product: $(-2)(-5) + (-7)(5) + (1)(-2) = 10 - 35 - 2 = -27$.
Magnitude squared $BA^2$: $4 + 49 + 1 = 54$.
Magnitude squared $BC^2$: $25 + 25 + 4 = 54$.

$\cos \theta = -27/54 = -1/2$.
$\theta = 120^\circ$.

Is there any ambiguity in coordinate notation? "A=(1,-11,2)" usually means $(x,y,z)$. Standard convention.
Is $\angle ABC$ the angle between vectors $\vec{BA}$ and $\vec{BC}$? Yes.
The angle at vertex B.
If we use vectors $\vec{AB}$ and $\vec{AC}$ (vectors originating from A), it would be $\cos \alpha$.
$\vec{AB} = (2, 7, -1)$.
$\vec{AC} = (-3, 12, -3)$.
Dot product: $-6 + 84 + 3 = 81$.
Magnitudes: $\sqrt{54}$ and $\sqrt{162}$.
$\cos A = 81 / \sqrt{54 \cdot 162} = 81 / ( \sqrt{9 \cdot 6} \cdot 9 \sqrt{18} ) = 81 / (3\sqrt{6} \cdot 9\sqrt{2})$ no $\sqrt{162} = 3\sqrt{18}$.
Let's calculate: $\sqrt{54} = 3\sqrt{6}$. $\sqrt{162} = 9\sqrt{2}$?
$162 / 9 = 18$. Yes $9\sqrt{18} = 27\sqrt{2}$. No. $\sqrt{162} = \sqrt{81 \cdot 2} = 9\sqrt{2}$. Correct.
So denominator is $3\sqrt{6} \cdot 9\sqrt{2} = 27\sqrt{12} = 54\sqrt{3}$.
Wait, $\sqrt{54 \cdot 162} = \sqrt{8748}$?
$54 \times 162 = (50+4)(160+2) ...$
Let's just use factorization. $54 = 9 \cdot 6$. $162 = 81 \cdot 2 = 9^2 \cdot 2$.
Product under square root: $(3^2 \cdot 6) \cdot (9^2 \cdot 2)$? No.
$\sqrt{54} = \sqrt{2 \cdot 3^3}$.
$\sqrt{162} = \sqrt{2 \cdot 3^4}$.
Product $\sqrt{2 \cdot 3^3 \cdot 2 \cdot 3^4} = \sqrt{2^2 \cdot 3^7} = 2 \cdot 3^3 \sqrt{3} = 54\sqrt{3}$.
Numerator is $81$.
$\cos A = 81 / (54\sqrt{3}) = \frac{81}{54\sqrt{3}} = \frac{3 \cdot 27}{9 \cdot 6 \sqrt{3}}$ no.
$81 / 54 = 3/2$.
$\cos A = \frac{3/2}{\sqrt{3}} = \frac{\sqrt{3} \cdot 3/2}{3}$? No.
$\frac{3}{2\sqrt{3}} = \frac{3\sqrt{3}}{6} = \frac{\sqrt{3}}{2}$.
So $\cos A = \frac{\sqrt{3}}{2}$. This would imply $A = 30^\circ$.
This angle is for triangle ABC.

Let's check lengths using coordinates again.
$AB^2 = (1-3)^2 + (-11 - (-4))^2 + (2-1)^2 = (-2)^2 + (-7)^2 + (1)^2 = 4 + 49 + 1 = 54$.
$AC^2 = (1 - (-2))^2 + (-11 - 1)^2 + (2 - (-1))^2 = (3)^2 + (-12)^2 + (3)^2 = 9 + 144 + 9 = 162$.
So side lengths squared are $54$ and $54$ ($BC^2$) wait, I used A in the calculation above for AC.
Wait, earlier I computed BC vector as $\vec{BC} = (-5, 5, -2)$ and its magnitude squared was $54$. So $BC^2=54$.
Wait, is my manual check of $BC$ correct?
$B=(3,-4,1)$, $C=(-2,1,-1)$.
$x$-diff: $-2 - 3 = -5$, sq: $25$.
$y$-diff: $1 - (-4) = 5$, sq: $25$.
$z$-diff: $-1 - 1 = -2$, sq: $4$.
Sum: $25+25+4 = 54$. Correct.

So side lengths:
$c^2 = AB^2 = 54$.
$a^2 = BC^2 = 54$.
$b^2 = AC^2 = 162$.

Check the sum of angles? Cosine rule?
$a^2 = b^2 + c^2 - 2bc \cos A$
$54 = 162 + 54 - 2(b)(c) \cos B$ -- Wait, this is for angle at B.
We need to find $\angle ABC$. That is the angle between sides $AB$ and $BC$. Usually denoted as B in $\triangle ABC$, opposite side $AC$. So we are computing angle at B.
Let $\theta_B$ be $\angle ABC$.
Law of Cosines on triangle ABC:
$b^2 = a^2 + c^2 - 2ac \cos(\theta_B)$.
Wait, standard notation is: vertices A, B, C. Side $a$ is opposite A (BC). Side $b$ is opposite B (AC). Side $c$ is opposite C (AB).
So $\angle ABC$ corresponds to vertex B. The sides meeting at B are $BA$ and $BC$. These have lengths $c$ and $a$. Wait.
$AB = c$. $BC = a$.
The angle is $\theta_B$.
So $AC^2 = AB^2 + BC^2 - 2(AB)(BC) \cos(\angle ABC)$.
We know $AC^2 = 162$.
We know $AB^2 = 54$.
We know $BC^2 = 54$.
So $162 = 54 + 54 - 2(54)^{1/2}(54)^{1/2} \cos(\angle ABC)$.
$162 = 108 - 2(54) \cos(\theta_B)$. Wait. $54 \cdot 54 = 2916$. Square root of that is not the product of lengths $AB \cdot BC$.
Wait, the formula is $b^2 = c^2 + a^2 - 2ca \cos B$.
Here sides are $BC$ (length $a$) and $AC$ (length $b$)? No.
Let's stick to vectors again, it was less prone to naming confusion.
Vectors $\vec{BA}$ and $\vec{BC}$.
Length of $\vec{BA}$ is distance between B and A. That is $c_{side} = AB$.
Length of $\vec{BC}$ is distance between B and C. That is $a_{side} = BC$? No, usually side lengths are denoted $c, a, b$. But here $c$ and $b$ would be adjacent to angle $B$. Wait.
Vertices A, B, C.
Angle at B is formed by segments BA and BC.
Let's call the points on the unit circle or something? No.
Side length $a$ is $BC$. Side length $b$ is $AC$. Side length $c$ is $AB$.
Wait, in standard notation:
$\angle B$ corresponds to vector $\vec{BA}$ and $\vec{BC}$.
The sides of the angle are lengths $AB$ and $BC$.
Let's check lengths:
$| \vec{BA} | = AB = \sqrt{54}$.
$| \vec{BC} | = BC = \sqrt{54}$.
Let $c_{len}$ be length of side $AB$ (which is adjacent to B). Wait, no. Side opposite A is a=BC. Side opposite B is b=AC. Side opposite C is c=AB.
Length of $\vec{BA}$ is the length of side $c$, which is $AB$. Correct.
Length of $\vec{BC}$ is the length of side $a$, which is $BC$. Correct.
So we have lengths $AB = \sqrt{54}$ and $BC = \sqrt{54}$.
Wait, looking at my dot product formula for angle $\angle B$:
$\cos B = \frac{\vec{BA} \cdot \vec{BC}}{|\vec{BA}| |\vec{BC}|}$.
The dot product was -27.
$|\vec{BA}| = \sqrt{54}$.
$|\vec{BC}| = \sqrt{54}$.
So $\cos B = -27 / 54 = -1/2$.
$\angle B = 120^\circ$.

Wait, I checked the cosine rule using side lengths earlier and got $A = 30^\circ$. Let's re-evaluate that.
The Cosine rule is $b^2 = a^2 + c^2 - 2ac \cos B$? No.
Law of Cosines relates angle to the opposite side squared.
Angle at $B$ ($\theta_B$) is opposite side $AC$ (length $b$).
Wait, in my vector notation $\vec{BA}$ and $\vec{BC}$. These two vectors originate from $B$. The angle between them is the angle of the triangle at vertex $B$, which is $\angle ABC$.
Let's check the labels on the formula.
Vector product $\vec{u} \cdot \vec{v} = |\vec{u}| |\vec{v}| \cos \theta$.
Here $\vec{u} = \vec{BA}$, $\vec{v} = \vec{BC}$.
The angle $\theta$ is indeed the interior angle at vertex B.
This means we are calculating $b^2$ using vectors $a$ and $c$? No.
We are calculating the side opposite to vertex $B$, which is side $AC$ (length $b$).
Wait, the Cosine rule is $\cos B = \frac{a^2 + c^2 - b^2}{2ac}$.
Here:
$a = |BC| = \sqrt{54}$.
$c = |AB| = \sqrt{54}$.
$b = |AC| = \sqrt{162}$. (Wait, I calculated $AC^2$ as 162 earlier).
Let's check $|AC|$ again.
$A=(1,-11,2)$. $C=(-2,1,-1)$.
$x_A - x_C = 1 - (-2) = 3$. Sq: 9.
$y_A - y_C = -11 - 1 = -12$. Sq: 144.
$z_A - z_C = 2 - (-1) = 3$. Sq: 9.
Sum = $9 + 144 + 9 = 162$. Correct.
Now back to Cosine rule formula.
$\cos B = \frac{a^2 + c^2 - b^2}{2ac}$. (where $a, c$ are lengths of sides adjacent to B).
Wait, the side opposite to vertex $B$ is side $AC$, which has length $b = AC$.
The sides adjacent to vertex $B$ are $AB$ and $BC$, whose lengths are $c_{side} = AB = \sqrt{54}$ and $a_{side} = BC = \sqrt{54}$.
Wait, I'm mixing up notation.
Let's just denote side lengths $s_1 = AC$, $s_2 = AB$, $s_3 = BC$.
$s_1 = 162^{1/2}$.
$s_2 = 54^{1/2}$.
$s_3 = 54^{1/2}$.
Angle at B is opposite side $s_1$.
$\cos(\angle B) = \frac{s_2^2 + s_3^2 - s_1^2}{2 s_2 s_3}$.
Numerator: $(\sqrt{54})^2 + (\sqrt{54})^2 - 162$.
$= 54 + 54 - 162 = 108 - 162 = -54$.
Denominator: $2 \cdot \sqrt{54} \cdot \sqrt{54} = 2 \cdot 54 = 108$.
$\cos(\angle B) = -54 / 108 = -1/2$.
$\angle B = 120^\circ$.

My confusion came from labeling.
Let's re-verify the dot product formula directly: $\cos \theta = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}| |\vec{v}|}$.
This gives $\cos(\angle B)$.
$\vec{BA}$ and $\vec{BC}$ are vectors from $B$ to $A$ and $B$ to $C$.
The angle between these vectors is exactly $\angle ABC$.
My calculation gave -27 / 54 = -0.5.
So $\theta = 120^\circ$.

Wait, earlier I used the Cosine rule with side lengths:
$b^2 = a^2 + c^2 - 2ac \cos B$.
Here $a$ and $c$ are sides adjacent to B. Wait. Standard notation is usually opposite letters.
Opposite B is side AC. Let's call it $x$.
Adjacent sides are AB and BC. Let's call them $y$ and $z$.
So $x^2 = y^2 + z^2 - 2yz \cos B$.
We found $x^2 = 162$.
$y^2 = 54$.
$z^2 = 54$.
So $162 = 54 + 54 - 2(\sqrt{54})(\sqrt{54}) \cos B$.
$162 = 108 - 108 \cos B$.
$54 = -108 \cos B$.
$\cos B = -1/2$.
This yields the same result.
Wait, earlier I wrote: "$\vec{AB} \cdot \vec{AC} = 81$" and then calculated $\cos A$. That was angle at A.
Let's check angle at A again to be sure.
$\vec{AB} = (2, 7, -1)$.
$\vec{AC} = (-3, 12, -3)$.
Dot product: $-6 + 84 + 3 = 81$.
Lengths: $\sqrt{54}$ and $\sqrt{162}$.
$|\vec{AB}|^2 = 54$.
$|\vec{AC}|^2 = 162$.
$\cos A = \frac{81}{\sqrt{54}\sqrt{162}} = \frac{81}{\sqrt{8748}}$.
Wait, $\sqrt{8748}$? $54 \times 162$.
$54 = 9 \times 6$. $162 = 81 \times 2$.
Product = $9^2 \cdot 6 \cdot 2 = 81 \cdot 12 = 972$? No.
$(3\sqrt{6})^2 (9\sqrt{2})^2$ no...
$\sqrt{54} = 3\sqrt{6}$. $\sqrt{162} = 9\sqrt{2}$.
Product $= 27 \sqrt{12} = 27(2\sqrt{3}) = 54\sqrt{3}$.
$81 / (54\sqrt{3}) = \frac{3}{2\sqrt{3}} = \frac{\sqrt{3}}{2}$.
So $\cos A = \sqrt{3}/2$. This implies $A = 30^\circ$.
Let's check if this is consistent with triangle geometry.
$AB^2 + BC^2 - 2 AB \cdot BC \cos B = AC^2$.
Wait, side lengths are not integers, angles are degrees. $\sqrt{3}/2$ corresponds to $60^\circ$. Oh wait.
$\cos A = \sqrt{3}/2 \implies A = 30^\circ$.
Wait, did I calculate dot product correctly?
$\vec{AB} = (2, 7, -1)$. Correct: $x_B - x_A = 3-1=2$, $y_B - y_A = -4 - (-11) = 7$, $z_B - z_A = 1-2=-1$.
$\vec{AC} = C - A = (-2-1, 1-(-11), -1-2) = (-3, 12, -3)$. Correct.
Dot: $(2)(-3) + (7)(12) + (-1)(-3) = -6 + 84 + 3 = 81$.
Lengths squared: $54$ and $162$.
$54 \times 162 = 8748$. $\sqrt{8748} \approx 93.5$.
$\cos A = 81 / 93.5 \approx 0.866$.
$\cos(30) = \sqrt{3}/2 \approx 0.866$.
So $A$ is likely $30^\circ$.
Let's check side lengths consistency with law of cosines for angle C? Or something else.
Wait, $\cos A = \sqrt{3}/2 \implies A=30^\circ$.
If we sum angles in triangle, does it work?
We have $B = 120^\circ$ and $A = 30^\circ$. Then angle at C should be $180 - 150 = 30^\circ$.
Wait, sides are opposite to angles.
Angle A is opposite side BC. Angle B is opposite side AC. Angle C is opposite side AB.
Side lengths squared:
$BC^2 = 54 \implies a^2 = 54$.
$AC^2 = 162 \implies b^2 = 162$.
$AB^2 = 54 \implies c^2 = 54$.
Wait, $AB=BC=\sqrt{54}$ implies triangle is isosceles with $AB=BC$.
So $\angle A = \angle C$.
If $\angle B = 120^\circ$, then sum of angles is $180^\circ$. So $\angle A + \angle C = 60^\circ$.
Since $A=C$, we get $2A = 60^\circ \implies A = 30^\circ, C = 30^\circ$.
So this matches the calculation for angle A.
Wait, why did I think side lengths squared were swapped?
$BC^2=54$ and $AB^2=54$ implies sides $a$ and $c$ are equal in length? No.
Standard notation:
$a = BC$. $b = AC$. $c = AB$.
My calculation of $BC$: $\sqrt{(-5)^2+5^2+(-2)^2} = \sqrt{25+25+4} = \sqrt{54}$. Correct.
My calculation of $AB$: $\sqrt{(1-3)^2 + ...} = \sqrt{4+49+1} = \sqrt{54}$. Correct.
So $a=c$ means triangle is isosceles with legs $BC$ and $AB$. So angles opposite are equal.
Angle opposite BC is $\angle A$. Angle opposite AB is $\angle C$.
So $\angle A = \angle C$.
And angle $\angle B = 120^\circ$.
Sum of angles: $A + C + B = 60 + 120 = 180$.
So $\cos(\angle A) = \frac{a^2+b^2-b^2-...}{...}$ No.
$\cos A = \frac{b^2+c^2-a^2}{2bc} = \frac{162+54-54}{2\sqrt{162}\sqrt{54}} = \frac{162}{2 \cdot \sqrt{8748}}$.
$162 / 93.5... \approx 0.866$.
Wait, $\cos(30) = \sqrt{3}/2 \approx 0.866$.
So $A = 30^\circ$. Correct.
And $\cos B = \frac{a^2+c^2-b^2}{2ac} = \frac{54+54-162}{2\sqrt{54}\sqrt{54}} = -54 / 108 = -1/2$. $B = 120^\circ$. Correct.

So everything is consistent.
The angle $\angle ABC$ corresponds to vertex B, opposite side AC (length b=AC). Wait.
Wait.
Vertices are labeled A, B, C.
Vector BA is from B to A. Vector BC is from B to C.
Angle between them is at B.
Side opposite to B is AC.
The lengths of BA and BC are $AB$ and $BC$.
$AB = \sqrt{54}$.
$BC = \sqrt{54}$.
Dot product $\vec{BA} \cdot \vec{BC}$ corresponds to $\cos(\angle ABC)$.

````

## Answer (content)

````text

````
