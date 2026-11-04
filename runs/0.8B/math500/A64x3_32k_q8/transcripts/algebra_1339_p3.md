# test/algebra/1339.json, part 3 of 3

[Previous part](algebra_1339_p2.md) · [Start](algebra_1339.md)

If it means "y varies directly with x", then $x^{0.5}$? No.  

I will stick to the standard interpretation $y \propto x^{-1/2}$.  

The result is 600.  


## Answer

To find the value of $x$ when $y=3$, we first need to establish the relationship between $y$ and $\sqrt{x}$ based on the given information.  

**1. Analyze the Relationship**  
The problem states that "$y$ varies inversely as $\sqrt x$". In mathematical terms, this describes a direct variation in terms of a constant of proportionality where $x$ appears in the denominator with an exponent of $-0.5$ (since the square root can be written as $x^{1/2}$). The relationship is given by:  
$$ y = k \cdot x^{-0.5} \quad \text{or} \quad y = \frac{k}{\sqrt{x}} $$  
where $k$ is a constant.  

**2. Find the Constant of Variation ($k$)**  
We are given that when $x=24$, $y=15$. We can substitute these values into our equation to find $k$:  
$$ 15 = k \cdot (24)^{-0.5} $$  
Since $(24)^{-0.5} = \frac{1}{\sqrt{24}}$, we have:  
$$ 15 = \frac{k}{\sqrt{24}} $$  
Multiply both sides by $\sqrt{24}$ to solve for $k$:  
$$ k = 15 \cdot \sqrt{24} $$  

We can simplify $\sqrt{24}$:  
$$ \sqrt{24} = \sqrt{4 \cdot 6} = 2\sqrt{6} $$  
So, the constant is:  
$$ k = 15 \cdot 2\sqrt{6} = 30\sqrt{6} $$  

**3. Solve for $x$ when $y=3$**  
Now we have the relationship equation and the value of $k$:  
$$ y = \frac{k}{\sqrt{x}} $$  

We want to find the value of $x$ when $y=3$. Substituting $y=3$ into the equation:  
$$ 3 = \frac{30\sqrt{6}}{\sqrt{x}} $$  

We need to isolate $x$. Multiply both sides by $\sqrt{x}$ and divide by $3$:  
$$ \sqrt{x} = \frac{30\sqrt{6}}{3} $$  
$$ \sqrt{x} = 10\sqrt{6} $$  

To eliminate the square root, square both sides:  
$$ x = (10\sqrt{6})^2 $$  
$$ x = 100 \cdot 6 $$  
$$ x = 600 $$  

**Answer:**  
The value of $x$ is 600.  

\boxed{600}  
