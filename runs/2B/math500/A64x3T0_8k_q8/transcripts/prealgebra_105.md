# test/prealgebra/105.json (Prealgebra, level 1)

> A figure skater is facing north when she begins to spin to her right. She spins 2250 degrees. Which direction (north, south, east or west) is she facing when she finishes her spin?  

**Correct.** Gold `\text{east}`, predicted `east`. Finish: stop, 8118 tokens, 4 waits, 1022.9 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's a thinking process that leads to the correct solution:  

1.  **Analyze the Problem:**  
    *   **Initial State:** Facing North.  
    *   **Action:** Spins to the right (clockwise rotation).  
    *   **Angle of Rotation:** 2250 degrees.  
    *   **Goal:** Determine the final facing direction.  

2.  **Visualize and Convert Units:**  
    *   A full circle is $360^\circ$.  
    *   To find out where she ends up, I can look at how many full rotations she completes first, and then the remaining angle.  
    *   $2250 \div 360$:  
        *   $2250 / 360 = 6.25$  
    *   She makes 6 full spins (2280 is 6*360, actually $6 \times 60 = 360$, so $6 \times 1/4 = 1.5$. Let's re-calculate carefully).  

    *   *Correction on mental math:*  
        *   $6 \times 360 = 2160$.  
        *   So she completes 6 full turns.  
        *   Remaining angle: $2250 - 2160 = 90^\circ$.  

    *   *Alternative calculation using the fraction of a circle:*  
        *   $2250 / 360 = 75 / 4 = 18.75 \times \pi$? No, let's stick to numbers.  
        *   $2250 / 360$:  
            *   $360 \times 2 = 720$.  
            *   $360 \times 4 = 1440$.  
            *   $360 \times 6 = 2160$.  
            *   So, 6 full turns (minus a fraction) is accurate.  

3.  **Analyze the Direction of Rotation:**  
    *   "Spins to her right."  
    *   In the Northern Hemisphere context (or standard map conventions): North is Up ($+y$), East is Right ($+x$). Wait, on a compass facing North, if I turn "right," I am turning clockwise.  

4.  **Step-by-Step Angle Tracing:**  
    *   Start Position: Facing North. Let's call this Vector $V_{start} = (0, +1)$ in Cartesian coordinates. Or just stick to compass directions.  
    *   Rotation: Clockwise (to the right).  
    *   Rotation: $90^\circ$ clockwise.  
        *   North $\xrightarrow{CW 90}$ South? No.  
        *   Let's draw a compass circle mentally or on paper:  
            *   N (12 o'clock) -> R turns to E (3 o'clock). This is $+90$.  
            *   So 90 degrees clockwise = East.  

    *   Rotation: $2250$ degrees total.  
    *   $2250 \div 360$:  
        *   $2250 - (6 \times 360) = 2250 - 2160 = 90$.  
    *   So, she does 6 full turns + $90$ degrees.  
    *   Since each full turn brings her back to North, she is effectively facing the same direction after every 360, but we are calculating where she ends up in that specific cycle.  

    *   Let's re-verify the math.  
        *   Start: North (0 deg or 90 deg depending on convention). Let's say North is $0^\circ$.  
        *   Clockwise is positive? No, standard math is counter-clockwise.  
        *   Let's just use the physical movement.  
        *   North $\rightarrow$ Right turn (Clockwise).  
        *   90 deg $\rightarrow$ East.  
        *   Next 90 deg $\rightarrow$ South.  
        *   Next 90 deg $\rightarrow$ West.  
        *   Next 90 deg $\rightarrow$ North.  
    *   So, she completes 2 turns ($720^\circ$). $2250 - 720 = 1530$.  
\*   1530 / 360 = 4.25.  
    *   Let's do it with one more approach: Total degrees modulo 360.  

    *   Let North be $0^\circ$ or just track the movement relative to North.  
    *   She moves clockwise (Right).  
    *   Angle $\theta = 2250^\circ$.  
    *   Full circle is 360 degrees.  
    *   How many times does she cross a reference point?  
    *   $360 \times 2 = 720$. $720$ brings her back to North (after turning right twice). She needs to turn another $1530$ degrees.  
    *   $360 \times 4 = 1440$.  
    *   This means she has rotated $2250$ total degrees.  
    *   $2250 / 360$:  
        *   $360 \times 6 = 2160$.  
        *   So she spins $6$ full times. She is still facing North (after turning right).  
        *   Remaining angle: $2250 - 2160 = 90^\circ$.  

    *   Current position: Facing North, after making 360-degree spins, but we are looking at the specific remainder.  
    *   She has already completed 6 full rotations (360x6 = 2160).  
    *   She needs to rotate an additional $90$ degrees in the right-hand direction (clockwise).  

5.  **Determine Final Direction:**  
    *   Start: North.  
    *   Move Clockwise (Right):  
        *   South (No, 90 is East? No. N=Up, E=Right. Turn Right from Up goes to Right).  
        *   So, North $\rightarrow$ East is 90 degrees clockwise.  
        *   North $\rightarrow$ South... no, wait.  
            *   Standard Compass:  
                *   North: 12 o'clock  
                *   East: 3 o'clock (Right)  
                *   South: 6 o'clock  
                *   West: 9 o'clock  
    *   Let's check the rotation direction again. "Spins to her right". This is a clockwise spin.  

    *   Start at N (12 o'clock position).  
    *   Turn Right (CW) 90 degrees $\rightarrow$ She faces East.  
    *   Turn Right CW 180 degrees $\rightarrow$ She faces South.  
    *   Turn Right CW 270 degrees $\rightarrow$ She faces West.  
    *   Turn Right CW 360 degrees $\rightarrow$ She faces North.  

    *   Let's map the $90^\circ$ remainder in the calculation ($2250 - 2160 = 90$) to compass directions relative to North.  
        *   The angle is just a count of degrees, but we established that after $360^\circ$, the direction is the starting direction (North).  
        *   She spins right. This creates an arc.  
        *   If she spins 90 degrees clockwise from North:  
            *   Imagine a clock face. 12 is North.  
            *   Turn Right (Clockwise) by 90 degrees brings the top position to the 3 o'clock position.  
            *   3 o'clock position corresponds to **East**.  

    *   Let's double check "Spins to her right".  
        *   In physics/mechanics problems, usually, we define rotation angles based on a convention (CCW). However, here, it's simple navigation: "spin to her right".  
        *   Facing North. Turning right means 90 deg CW is East.  
        *   If she spins $90^\circ$, she faces East.  
        *   If she spins $180^\circ$, she faces South.  
        *   If she spins $270^\circ$, she faces West.  
        *   If she spins $360^\circ$, she faces North.  
    *   Now look at the remainder: $90^\circ$.  
    *   $2250 \pmod{360} = 90$.  
    *   So, relative to North (the starting direction), she has turned clockwise by $90$ degrees.  
    *   Therefore, her final direction is **East**.  

6.  **Verify using the standard "Turn Right" logic:**  
    *   Facing North.  
    *   To turn right:  
        *   Turn a bit $\rightarrow$ East? No, that's a huge leap. Let's trace it carefully.  
\*   N (0) -> E (90).  
        *   If she turns $270^\circ$ CW to go "right" fully, she faces West.  
    *   She spins $2250^\circ$.  
    *   $2250 = 6 \times 360 + 90$.  
    *   Since the rotation is continuous (or rather, a full loop), we look at the net displacement.  
    *   Start facing North.  
    *   Spin right $\rightarrow$ East.  
    *   Spin right $\rightarrow$ South.  
    *   Spin right $\rightarrow$ West.  
    *   Spin right $\rightarrow$ North.  
    *   Total spin = 6 full spins + 90 deg.  
    *   90 deg to the right of facing North is East.  

7.  **Is there any ambiguity?**  
    *   "Spins to her right" implies Clockwise (Clock).  
    *   "Spins to her left" implies Counter-Clockwise.  
    *   Does "to her right" imply a direction of the plane of rotation or a directional vector? No, it's about turning towards herself.  
    *   Start: North.  
    *   Turn Right (Clockwise).  
    *   Move $\rightarrow$ East.  
    *   $2250 \pmod{360}$ is 90 degrees.  
    *   If I start facing North and turn $90^\circ$ to the right: I face **East**.  

Let's re-read carefully to ensure no misinterpretation of "spins".  
Sometimes people confuse radians and degrees, but 2250 is degrees.  
Does she pass through South or West?  
If she spins $90^\circ$ CW starting from North:  
*   She is looking at North (0 degrees).  
    *   To the right of North is East (or South depending on how you define it).  
    *   On a map: N=Top, E=Right. Turn Right $\rightarrow$ Go East.  
    *   If you are in a circle: 12 o'clock (North) -> turn right -> go to 3 o'clock (East).  
    *   If the answer were South, she would have to spin "to her left" to get from North to South (Counter-Clockwise is turning left? No. Imagine facing North, facing a wall East of you. Turn left to face West. Turn right to face South... no that's confusing.)  

Let's be precise:  
*   Facing North.  
    *   Right hand moves: Clockwise on a compass face.  
    *   N (Up).  
    *   90 deg clockwise $\rightarrow$ East (Right side of compass).  
    *   Therefore, she faces East.  

**Calculation Check:**  
*   $2250 / 360 = 6.25$  
    *   She spins 6 full times ($2160^\circ$).  
    *   Remaining angle: $2250 - 2160 = 90^\circ$.  
    *   Since the spin is "to her right" (clockwise), moving $90^\circ$ clockwise from North leads directly to **East**.  

8.  **Common Pitfall Check:**  
    *   Sometimes people think of N as 0, and turning right increases or subtracts angle in math convention ($+x$).  
    *   However, let's look at the "right" turn again.  
        *   Facing North (facing Up). Right hand points East (Right). Left hand points West (Left).  
        *   If you spin clockwise (to the right), you move from Up towards East.  
    *   What if the question implies she spins 2250 degrees, but is a figure skater? Skaters rotate around an axis through their center of mass (usually vertical if holding blades straight, though here "spins to her right" suggests angular momentum change). The physics holds.  
    *   Is it possible "to her right" refers to the direction of rotation vector? In standard right-handed coordinate systems ($x$ right, $y$ up, $z$ out), a positive spin (CCW) creates torque in $+x$ (Right). A negative spin (CW) is into $-x$. But physically "spin to her right" means the angular velocity vector points *away* from her or towards her? No, it just means she is rotating clockwise.  
    *   So Clockwise is the key keyword.  

Let's check the number 2250 again.  
$2250 - 1080 = 1170$.  
$1170 - 630 = 540$.  
$540 - 360 = 180$. (This is getting nowhere).  

Let's stick to the simplest: $2250 \pmod{360} = 90$.  
N -> CW -> E.  
Is it possible she turns "to her right" meaning something else? No, standard English.  

Let's check if there is an alternative interpretation of "Spins to her right".  
Maybe "spins" implies she spins in place, rotating her body axis.  
If she starts North, and rotates clockwise (to her right), she faces East after 90 degrees.  

Is there any trick with the number 2250?  
$2250 / 45 = 50$.  
$360 / 45 = 8$.  
So it's not a "nice" round number of turns. It's $6 \frac{1}{4}$.  
If it were $90^\circ$, she would face East.  

What if the question meant she spins *against* gravity? Irrelevant.  
What if she spins North (Up)? No, "facing".  

Let's re-read carefully: "She spins to her right."  
Imagine a clock. The top is N.  
If you spin to your right, you sweep the arc from 12 to 3. You face East.  
This seems extremely straightforward. Why is it a reasoning problem? Maybe just checking if I know how to divide degrees and handle direction.  

Is there any possibility that "spins to her right" means she spins *around* her center of mass, such that the axis changes? No, spinning on the body axis keeps the same orientation of the axes (assuming a normal spin).  

What if "spins to her right" implies turning 180 degrees?  
Some people say "spin right" might mean she is facing N and spins to E (90) or South (270)?  
No, standard convention:  
Facing N. Right hand points East. To turn right, you turn towards the East.  

Let's verify with a counter-example if any.  
If I spin North, turn 180 degrees to the right, I face South?  
Start facing N (up). Turn Left (CCW) -> West? No, turn Left faces E? No.  
Facing Up. Turn Left (Counter Clockwise).  
Imagine clock: Top -> Right is CW. Left is CCW.  
Left hand points to 9 o'clock (West). So turning "Left" means going to the West.  
Turning "Right" means going to the East? No.  
Let's hold a stick in front of you pointing North.  
Turn your head Right. You now look at the 3 o'clock position on the wall (East).  
Turn your head Left. You now look at the 9 o'clock position (West).  

So:  
Start = North (0) or Up.  
"Spin to her right" = Clockwise rotation ($\text{CW}$).  
$2250^\circ$ total clockwise.  
Modulo 360 = 90 degrees CW.  
From North, rotating Clockwise by 90 degrees results in facing **East**.  

Let's check the "Spin to her right" definition again.  
If you face a wall (N is perpendicular to floor? No, standard map N is Up).  
If I am on the ground facing North (Up towards sky), and I spin to my right.  
My right hand is East.  
So my body turns 90 degrees towards East.  
I now face East.  

What if "spins to her right" implies she spins around the vertical axis (which keeps her feet still)?  
Yes, that's what a spin on ice does. She stays upright. Her direction of travel changes from North to East.  
This confirms East.  

Is there any chance "spins to her right" means she goes towards the South?  
If you stand facing N and turn Left 90 degrees... you face West.  
If you stand facing N and turn Right 90 degrees... you face East.  
If you spin 180, you face West (if you spun left)? No.  
Facing N. Spin CW 180 -> Face S? No.  
Let's trace a point on the wall.  
Point at $(0, R)$. Facing $N$ (positive Y).  
Rotate clockwise by $\pi$ ($180^\circ$). New position is $(0, -R)$ (facing South).  
So 180 deg CW is South?  
Let's check coordinates.  
North is $+y$. East is $+x$.  
Facing North means vector is $\vec{v} = (0,1)$.  
Spin Right (Clockwise) means the tangent to the path at top of circle goes in positive x direction (East).  
So after 90 degrees: Vector points $(1,0)$ -> East. Correct.  
After 180 degrees: Vector points $(0,-1)$ -> South. Correct.  
So the mapping is:  
90 deg CW = East  
180 deg CW = South  
270 deg CW = West  
360 deg CW = North  

The question gives 2250 degrees.  
$2250 \pmod{360}$.  
$2250 - (6 \times 360) = 90$.  
So we are looking for the vector after 90 deg CW rotation.  
Result: East.  

Let's check the "left" case just to be sure I didn't mix them up.  
Facing North (Up). Spin Left (CCW).  
90 deg -> Face West (Left hand is West? No. N is top. Turn left -> West? Wait.)  
Imagine compass rose.  
Top: N. Right: E. Bottom: S. Left: W.  
Turn CCW (Counter Clockwise):  
Rotate the clock hand to the left.  
12 o'clock goes to 9 o'clock position. This is West.  
So CW = Right turn = East.  
My previous deduction was: "If I spin to my right, I face East."  
Let's double check this simple fact because it's common in puzzles.  
Scenario: You are walking North. You turn to your right (East). Correct.  
Imagine a circle of points labeled 0, 180.  
If you are at the North pole and rotate clockwise...  
Usually, math problems use counter-clockwise as positive.  
Let's stick to the compass definition.  
N -> East is Right Turn.  
Therefore $270^\circ$ (Right turn) = West?  
Hold on. Let's be very strict about "Right".  
If I am standing in front of a wall.  
I face North (towards the wall). No, facing North means looking at a point on a map that is North. Or facing a person standing North of me.  
Let's use the clock analogy again, it was robust.  
Clock: 12 is N. 3 is E. 6 is S. 9 is W.  
Right turn (Clockwise) means moving from 12 towards 3, then 4? No, CW moves 12->3->6->9->12.  
So:  
Start at 12 (N).  
Move 90 deg $\rightarrow$ At 3 (E). Direction is East.  
Move 180 deg $\rightarrow$ At 6 (S). Direction is South.  
Move 270 deg $\rightarrow$ At 9 (W). Direction is West.  

Is this correct?  
If I face North (Up) and turn Right. My hands move to my right. If I face N, my left hand points East. No.  
Facing North.  
Left hand is West (or South? No, imagine a T shape).  
N is Up. E is Right. S is Down. W is Left.  
Turn Right (Clockwise): Up $\rightarrow$ Right.  
N $\rightarrow$ E.  
Turn Left (Counter-Clockwise): Up $\rightarrow$ Left.  
N $\rightarrow$ W.  

So, $90^\circ$ CW = East.  
Is this consistent with the phrase "spin to her right"? Yes.  
Example: A figure skater spins to her right. She is looking up. She moves to her right side. She faces East.  

If I assume "Right" means "South" in some universe? No, standard convention applies.  

Calculation again: $2250 / 360 = 6.25$.  
Remaining part of circle is 1/4 of a full circle (since 6.25 - 6 = 0.25).  
0.25 circle is 90 degrees.  
Direction:  
She starts facing North.  
She spins $6.25$ turns in the "to her right" direction.  
If we consider the path: North (start) $\xrightarrow{1} \dots \xrightarrow{360}$ N (end of cycle).  
We are looking at where she ends up relative to start, modulo full rotations.  
So effectively, she spins 90 degrees clockwise from North.  
Clockwise from North is East.  

Let's check the other way "Left" just in case the user meant spinning around her center and I got the direction wrong based on a brain fart.  
If I spin to my Left (CCW): N $\rightarrow$ W $\rightarrow$ S $\rightarrow$ E $\rightarrow$ N.  
90 deg CCW = West.  

Is there any reason "spin to her right" might mean something else?  
In some contexts, a turn is a displacement in the direction of the tangent. But this is angular rotation. "Right" usually refers to the relative orientation of the hand or the side of the body.  
Facing N (Up). Right side is East. Turn Right $\rightarrow$ Face East.  

Final verification:  
If you face North, spin 180 degrees to your right (turn 90 deg CW + 90 deg CCW? No).  
Spin 180 degrees to the right: You go N -> S?  
N is up. Turn Right (Clockwise). 180 deg clockwise brings you to South?  
Let's check the clock logic again.  
12 o'clock. Rotate CW by 180 degrees $\rightarrow$ 6 o'clock position. Position is South. So facing South.  
So yes, N -> S is 180 deg Right turn.  

What about the number 2250?  
$2250 / 360 = 6 + 90/360$.  
The fraction of a circle remaining is 90 degrees.  
90 degrees Right Turn from North leads to East.  

Let's assume the question meant "spin to her left".  
Then 90 deg Left $\rightarrow$ West.  
But it says "right". So East.  

Are there any caveats about "spins"?  
Maybe spin implies a change in orientation due to rotation? No, direction of travel for angular velocity is what defines facing.  
Facing North = Up along axis Y.  
Right hand turns CCW? Or CW?  
Standard physics: Angular velocity vector $\vec{\omega}$.  
If I am rotating CW (clockwise on the sky), $\vec{\omega}$ points down ($-z$).  
My face direction rotates towards East.  
So, if I have my back to the wall, and turn right (CW), I am facing East relative to the ground frame if I was facing North?  
No, just visualizing "Facing North" means the vector $\vec{n}$ points North. The skater spins, but her body axis rotates CW.  
After 90 deg rotation, the body axis is at the angle -90 deg (relative to N). -90 deg relative to North is East?  
Let's define angles.  
Angle of face $A = \text{North} + \theta$ (CW).  
$\theta_{start} = 0$.  
$\theta_{end} = 2250^\circ$.  
Since we are interested in direction modulo 360.  
$\theta_{final\_dir} = 0 + (2250 \pmod{360})$.  
$2250 \pmod{360} = 90$.  
Direction corresponding to angle $+90^\circ$ (CW from N) is East.  

Let's verify the mapping of angles again carefully.  
If $\theta$ increases as CW, then $90^\circ$ increase means CW 90 deg.  
Does increasing angle represent CW or CCW?  
Math convention: Standard Polar coordinates usually start at X-axis ($+x$, East) and go to Y-axis ($+y$, North).  
This is confusing because in the problem, $+y$ is North.  
So if $\theta$ starts at 90 (North), then increasing $\theta$ moves clockwise? No, standard polar coordinates move counter-clockwise.  
Let's just use "Right" and "Left".  
Facing N. Right turn = CW rotation on compass.  
Start: N.  
Move CW 90 deg. You are facing E.  
Move CW 180 deg. You are facing S.  
Move CW 270 deg. You are facing W.  
This creates a standard cycle.  

If this is wrong (e.g. if N to S was considered right turn?), let's visualize again.  
Imagine a map.  
North arrow pointing up.  
East arrow pointing right.  
South arrow pointing down.  
West arrow pointing left.  
You are looking at the North arrow.  
Turn Right (Clockwise).  
The North arrow moves to the Right side of you.  
It points towards where? Towards the East arrow.  
So she faces East.  

This logic seems sound and robust.  

Let's calculate $2250 \pmod{360}$ one more time just to be absolutely certain I didn't mess up division.  
$360 \times 1 = 360$  
$360 \times 4 = 1440$. (Total $1800$)  
$2250 - 1440 = 810$.  
$360 \times 2 = 720$.  
$810 - 720 = 90$.  
So remainder is 90.  

Result: Facing East.  

Could the answer be South?  
This would happen if she spun to her right (CCW) and it was a different convention, or I mixed up Left/Right.  
If N (Up) -> CCW 90 deg -> Left hand points North? No. Left hand is West?  
Let's check the compass again.  
N=12\. E=3. S=6. W=9.  
Turn "Left" (Counter-Clockwise): 12 -> 9 (West).  
Turn "Right" (Clockwise): 12 -> 3 (East).  

So if she spins to her right, she ends up facing East.  

Is it possible the question implies she starts spinning in place, so her feet are stationary, and the rotation is just an illusion? No, that's what a spin does.  

Is it possible "spin to her right" refers to the direction of angular velocity vector?  
If she spins clockwise, the axis points into the page (or down).  
The question asks "Which direction is she facing". This implies the final orientation of her body relative to North/South/East/West.  

So, the answer is East.  

One edge case: Is it possible "spins to her right" means she spins *on* the side? No.  
What if "2250 degrees" refers to a rotation around a different axis (like rolling)? No, figure skater spins on the horizontal axis in place.  

Final Answer Formulation:  
1.  Start facing North ($0^\circ$).  
    2.  Rotation is clockwise ("to her right").  
    3.  Total rotation = $2250^\circ$.  
    4.  Calculate net rotation relative to starting point (modulo $360^\circ$).  
    5.  $2250 \div 360 = 6$ with a remainder of $90^\circ$.  
    6.  She completes 6 full spins and turns an additional $90^\circ$.  
    7.  Facing North and turning clockwise ($90^\circ$) results in facing East.  

Double check the math:  
$2250 / 360$:  
$360 \times 10 = 3600$  
$360 \times 6 = 2160$  
$2250 - 2160 = 90$.  
Remainder is 90.  
North -> Right (CW) -> 90 deg -> East.  

What if "right" implies turning left on the map because of map orientation? No, right hand rule for vectors or simply cardinal directions.  
Facing N (up).  
Right side is East.  
Left side is West.  
Turn Right = Move to East.  

If I spin 270 degrees to the right:  
Start at N.  
90 deg -> E.  
180 deg -> S.  
270 deg -> W.  
So $2250 \pmod{360} = 90$.  
She ends up facing East.  

Is there any interpretation where she ends up at South?  
Only if "spins to her right" meant "turns towards the center" or something weird? No, figure skaters spin in place (conserving angular momentum).  

Let's write down the solution steps clearly.  
1. Identify initial direction: North.  
   2. Identify rotation: $90^\circ$ clockwise (Right).  
    3. Perform arithmetic: Divide total degrees by 360 to find full rotations and remainder.  
$2250 / 360 = 6$ R $90$.  
    4. Determine direction for remainder: A $90^\circ$ clockwise turn from North results in facing East.  

One minor sanity check on "spin to her right".  
In many physics problems, a positive rotation is defined as counter-clockwise (CCW).  
If the problem uses standard math coordinates where North is +Y and X is Right:  
A rotation of $+90$ degrees (CCW) would face West.  
A rotation of $-90$ degrees (CW) would face East.  
"Spin to her right" describes the physical action of turning clockwise on a map where N is Up.  
Therefore, CW.  

The only ambiguity is if the skater's coordinate system (body) is different from the map coordinates. But "facing North" and "spinning to her right" are relative to the external frame (map) unless specified.  
If you face North, turning to your right puts you towards the East side of the compass rose.  

The answer should be East.  

Let's check if there is any tricky wording about "direction she finishes".  
Maybe she stops spinning and faces a certain way? No, spinning 2250 degrees means she is still in the same orientation relative to the axis (unless she tumbled). "Spins" usually implies rotation around a vertical axis.  

What if the problem meant $2250$ is not degrees? It says "degrees".  

Final check of arithmetic:  
$6 \times 360 = 2160$.  
$2250 - 2160 = 90$.  
Start N. Clockwise 90 deg -> East.  

If the rotation was CCW (Left):  
Start N. CCW 90 deg -> West.  

Given "right", it is East.  


## Answer

To determine the skater's final direction, we need to break down the spin into full rotations and any remaining angular displacement relative to her starting orientation.  

1.  **Identify Initial Direction:** The skater starts facing **North**.  

2.  **Analyze the Rotation Type:** She spins "to her right."  
    *   In standard navigation (and compass directions), if you are facing North, turning to your right means rotating towards the East (clockwise on a map). If you were facing South, turning right would be to the West, but in this context, it implies the relative motion of her body axis turning clockwise.  

3.  **Perform Angle Arithmetic:**  
    *   We calculate how many times she completes a full circle ($360^\circ$) and what is left over.  
    *   $2250 \div 360 = 6$ with a remainder.  
    *   Calculation:  
        *   $6 \times 360 = 2160$  
        *   $2250 - 2160 = 90^\circ$  
    *   This means she completes 6 full spins ($2160^\circ$) and then spins an additional $90^\circ$.  

4.  **Determine the Final Direction:**  
    *   She has completed 6 full rotations, which means her orientation relative to North (facing North) is restored after every 360-degree turn.  
    *   We only need to consider the remaining angle: $90^\circ$ clockwise rotation from North.  
    *   Starting face: **North**.  
    *   Moving clockwise (to the right) by $90^\circ$:  
        *   North ($12$ o'clock) $\rightarrow$ East ($3$ o'clock).  

Therefore, after spinning $2250$ degrees to her right, she will be facing **East**.  

\boxed{east}  
