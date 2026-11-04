# test/counting_and_probability/803.json, part 3 of 3

[Previous part](counting_and_probability_803_p2.md) · [Start](counting_and_probability_803.md)

The problem asks for the probability that a point $(x,y)$ chosen randomly from the region defined by $0 \le x \le 8$ and $0 \le y \le 4$ satisfies the condition $x + y \le 4$, where the selection is uniform over the sample space.  

**1. Determine the Sample Space Area:**  
The sample space $\Omega$ is the rectangle defined by the inequalities:  
$$ x \in [0, 8] $$  
$$ y \in [0, 4] $$  
This is a square with side lengths $L = 8 - 0 = 8$ and $W = 4 - 0 = 4$.  
The total area of the sample space is:  
$$ |\Omega| = 8 \times 4 = 32 $$  

**2. Determine the Favorable Region:**  
The event of interest is the probability that the condition $x + y \le 4$ holds for a random point in $\Omega$. This represents the area of the region inside the square bounded by:  
- The line segment connecting $(0,4)$ and $(4,0)$ (since $x=0 \implies y=4$, and $y=0 \implies x=4$).  
- The coordinate axes.  

The vertices of this favorable region are:  
- $(0,0)$ (on the origin)  
- $(4,0)$ (on the x-axis)  
- $(0,4)$ (on the y-axis)  

This region forms a right-angled triangle with legs along the coordinate axes and length $L=4$ on each side.  
The area of this triangle is:  
$$ A_{favorable} = \frac{1}{2} \times (\text{base}) \times (\text{height}) $$  
Using base=4 and height=4:  
$$ A_{favorable} = \frac{1}{2} \times 4 \times 4 = 8 $$  

**3. Calculate the Probability:**  
The probability $P(x+y \le 4)$ is the ratio of the area of the favorable region to the total area of the sample space:  
$$ P(E) = \frac{A_{favorable}}{|\Omega|} = \frac{8}{32} $$  

Simplifying the fraction:  
$$ \frac{8}{32} = \frac{1}{4} $$  

**Answer:**  
The probability is $\frac{1}{4}$.  

\boxed{\frac{1}{4}}  
