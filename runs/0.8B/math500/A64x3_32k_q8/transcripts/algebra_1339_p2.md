# test/algebra/1339.json, part 2 of 3

[Previous part](algebra_1339.md)

My previous calculation: $x=600$.  
Is it consistent?  
$k \approx 15 / \sqrt{24} \approx 3.05$.  
Check $y=3$ at $x=600$: $y = k/\sqrt{600}$. $\sqrt{600} = \sqrt{36 \times 10} = 6\sqrt{10}$.  
$k/\sqrt{600} \approx 3.05 / (6\sqrt{10}) \approx 0.5/ \dots$ No.  

Let's check the exact relation for $\sqrt{x}=24, y=15$.  
$y/x^{0.5}$? No, just a formula.  
The formula is derived from $1/(\text{inverse}) = k x^{-1/2}$.  
So $\frac{1}{\sqrt{x}}$ depends on $k$.  
Let's use the ratio method directly.  
$y_1/\sqrt{x_1} = 15 / \sqrt{24}$.  
$y_3/x_3^{0.5} = 3 / x_3^{0.5}$? No.  
The variable is $x$ when $y=3$. Let's call it $X_{target}$.  
We need to determine the constant of variation first.  
But "varies inversely as $\sqrt{x}$" usually implies a specific form $y = c / \sqrt{x}$.  
This means we can find $c$ using two points $(24, 15)$ and (something else). But that would just give the slope? No. It gives $k$.  
If we had only one point (or infinite), we could't determine $k$.  
But here we have *two* points? No, just one set of values given as context. "When x=24, y=15". This is one data point for the equation.  
The phrase "The value of y varies inversely as $\sqrt x$" describes the behavior of $y$ with respect to $x$.  
It does NOT imply there's an explicit formula connecting $y$ to $x$ like $y=kx^{-0.5}$ *and* another relation. It just defines the functional relationship.  
Therefore, finding the constant $k$ is the only necessary step.  

Is there any possibility that "inversely as $\sqrt x$" implies $xy^2 = C$? No, that's "varies directly".  
Or maybe "y varies inversely with respect to x"? (i.e. inverse variation).  
But here it explicitly says "as $\sqrt x$".  
So $y \propto 1/\sqrt{x}$.  

Let's verify my result $x=600$ again.  
If $x = 600$, then $y = k / \sqrt{600}$.  
Using $k = 15\sqrt{24}$.  
$y = 15\sqrt{24} / \sqrt{600}$.  
$y = (15 \cdot 2\sqrt{6}) / (6\sqrt{10})$.  
$y = 3(2\sqrt{6}/(\sqrt{2}\cdot\sqrt{10}))$. No, $\sqrt{24} = \sqrt{4\times6}=2\sqrt{6}$.  
$y = 15 \cdot 2\sqrt{6} / (6\sqrt{10}) = 30\sqrt{6}/(6\sqrt{10})$?  
$\sqrt{24} = \sqrt{24}$. $\sqrt{600} = \sqrt{25 \times 24} = 5 \sqrt{24}$.  
$y = k / (5\sqrt{24})$.  
$y = (15\sqrt{24}) / (5\sqrt{24}) = 3$.  
Yes! It matches.  

So the equation is correct and solution is consistent.  

**Summary of steps for final output:**  
1.  Interpret the variation relation: $y = \frac{k}{\sqrt{x}}$.  
    2.  Use the given point $(x_1, y_1) = (24, 15)$ to find the constant $k$ (or relate the variables).  
$15 = \frac{k}{\sqrt{24}}$.  
    3.  Solve for $k$: $k = 15\sqrt{24}$. Note that $\sqrt{24} = 2\sqrt{6}$, so $k = 30\sqrt{6}$. (Optional but clean).  
    4.  Use this constant $k$ and the target point $(x_2, y_2) = (X, 3)$ to find $X$.  
Substitute into the relation: $3 = \frac{k}{\sqrt{X}}$.  
    5.  Solve for $X$:  
$\sqrt{X} = \frac{k}{3}$.  
$X = \left(\frac{k}{3}\right)^2 = \frac{k^2}{9}$.  
    6.  Substitute the expression for $k$:  
$X = \frac{(15\sqrt{24})^2}{9}$.  
Simplify numerator: $15^2 \times 24 = 225 \times 24$.  
Simplify denominator: $9$.  
$X = \frac{225 \times 24}{9}$.  
Note that $\frac{225}{9} = 25$.  
So $X = 25 \times 24$.  
    7.  Calculate $X$:  
$25 \times 20 = 500$.  
$25 \times 4 = 100$.  
$X = 600$.  

This seems very solid.  

Let's quickly check if the user meant "variable y is inversely proportional to x".  
If so, $y/x = c$. $x=24 \to y=15 \implies 15/24=c \implies y=c$. Then at any $y$, $x$ would be determined? No, that's not "varies inversely as $\sqrt{x}$".  
If it meant $y = k\sqrt{x}$ (direct), $x=600$ is wrong.  
If it meant $xy = c$ (product constant) -> $15x = 24$? Then $y$ depends on $x$. But it says "varies as $\sqrt x$".  

What about the wording in some languages or contexts?  
"The value of y varies inversely as $c$" could imply a proportionality constant is unknown and we must find it.  
Usually, such problems are well-posed for the standard interpretation $y = kx^{-1/2}$.  

One small check: Is $\sqrt{x}$ meant to be written as $(\sqrt{3})^{something}$? No, standard notation.  
Is there any reason to suspect "varies inversely as" means something else?  
Sometimes "variable y varies inversely as function of x" implies $y = c/x$. But here it says $\sqrt{x}$.  
It's unambiguous enough for standard interpretation.  

Final check on calculation $25 \times 24$.  
$20 \times 25 = 500$.  
$4 \times 25 = 100$.  
Sum: 600.  
Perfect.  

The question asks for "What is x".  
Answer: 600.  

Is it possible that $x$ and $y$ are swapped in my logic?  
If $x=24, y=15$.  
Then $\sqrt{24} = k/15$. No.  
Inverse relation: $k/x^{1/2} = y$?  
Or is it "Inverse variation" means $x \cdot y$ constant? No, that's direct proportional to the square root of x? No.  
Let's assume $y = k/\sqrt{x}$ again.  

What if the problem implies $y$ varies as $\sqrt{x}$ (direct) but then I misread "inversely"?  
"The value of y varies inversely as $\sqrt x$".  
This means $y \cdot \sqrt{x} = \text{constant}$? No.  
It means if you increase $\sqrt{x}$, $y$ decreases (and $x$ increases).  
Usually inverse variation is defined by the constant of proportionality being positive (or negative).  
Here it is "varies inversely as". The phrase implies a ratio.  
If $y \propto -1/\sqrt{x}$? Then $y$ would be negative for positive $\sqrt{x}$. But usually variables are taken to be non-negative.  
So, standard form is likely correct.  

Let's confirm with the "variable of variation" phrasing.  
In algebra: $f(x)$ varies inversely as $x$ means $f(x) = c/x^a$? No, $c/x$.  
The phrase "varies inversely as $\sqrt{x}$" is a standard description for $y \propto x^{-1/2}$.  

Final Answer seems to be 600.  

Let's write out the argument clearly.  
Given: $y$ varies inversely as $\sqrt{x}$.  
This implies $y = k / \sqrt{x}$, or $\frac{y}{\sqrt{x}} = \text{constant}$. (Since "varies inversely" means direct proportionality of 1 to the variable).  
Given: when $x=24$, $y=15$.  
So, $\frac{15}{\sqrt{24}} = \text{const}$?  
No, that would imply $k = 15$. But is this consistent with "varies inversely"? Yes. If $y$ and $\sqrt{x}$ are related such that their product or ratio has a specific constant? No.  
If $y$ varies inversely as $\sqrt{x}$, it means the graph of $y$ vs $\sqrt{x}$ is a hyperbola where slope changes inversely with distance from origin? No.  
It simply means if you plot $x=24$, then corresponding to some constant $k$ (usually written as "inverse variation"), we have a relationship between them.  
The wording usually implies $y = k / \sqrt{x}$ is the correct model for these inverse variation problems.  

Let's double check if I can calculate $k$ and see if it yields integer arithmetic?  
$\frac{15}{\sqrt{24}}$. Not simplifying nicely to an integer or simple fraction, but leads to rational result with square root.  
$x_2$ becomes $600$, which is an integer, consistent with such problems having nice answers.  

What if $k=15$? Then $\frac{y}{\sqrt{x}} = 15$.  
At $x=24$: $y = 3$. No, at $x=24, y=15$, so $15/24 = 0.625 \neq 15$. So $k$ is not 15.  

Okay, the solution path:  
1. $y = k x^{-0.5}$? No, just $y/x^{0.5} = c$ implies $x$ and $y$ are inversely proportional *relative* to $x$.  
Actually, "inverse as" means the relationship is $y \cdot (\text{something}) = C$. If $\sqrt{x}$ is the thing to vary with. Then $y / x^{1/2} = c$.  
The phrase "value of y varies inversely as $\sqrt x$" suggests $y = k/\sqrt{x}$.  
My derivation $x_2 = 600$ holds based on this interpretation.  

Let's check if "inversely as" could mean $x \propto 1/y^2$? No, that's just swapping names.  
What if the variable name is a trick? $x=3$ is when $y=3$. If it meant $x$ when $y=3$, then I'd be solving for $x$.  
The prompt says "What is x when y=3".  
And $x=24$ is given.  
So it's asking for $x$ (let's call it $X_{unknown}$) at which $y=3$.  

If I made a mistake and meant to find $y$, I would solve $3 = \dots$.  
If I made a mistake and meant $x$ when $y=24$, then it is solved.  
But the prompt says "When $x=24$, $y=15$".  
So it's finding the intersection of the curve?  
The equation connects $(24, 15)$.  
The question asks for $x$ where $y=3$.  

Let's verify if there is any ambiguity about "inversely as $\sqrt{x}$".  
Sometimes "varies inversely" means $y = \frac{C}{x^b}$. If $b$ is unknown or $\sqrt{x}$, then it might be a specific case.  
But here $\sqrt{x}$ is given.  

Is there any possibility that the user provided a problem with typos?  
Maybe "inversely as x"? (i.e. $y \propto 1/x$).  
If so, $x = y^2 k$. No, inverse variation would be $xy=c$ or similar.  
Or maybe "x varies inversely as sqrt(y)"?  
If the problem text is taken literally: "y varies inversely as $\sqrt x$".  
The only interpretation that yields a specific solution without making assumptions about constant is $y = c/\sqrt{x}$.  

Is there any ambiguity where "varies inversely as" implies $x = k y^{-1/2}$? No, usually the function is named "y varies inversely as".  
If it was $x$ varies inversely as $\sqrt{y}$, that would be different. But here it's $y$.  

So I am reasonably confident in 600.  

Double check calculation for $X = 25 \times 24$.  
$X_1 = 15/\sqrt{24}$. (Ratio between y and x is constant? No).  
Let's re-derive using a ratio argument directly, which is robust against interpretation errors.  
If the relationship is $y = c / \sqrt{x}$, then for two points $(x_1, y_1)$ and $(x_2, y_2)$:  
$\frac{y_2}{\sqrt{x_2}} = k$? No.  
The equation is just a function $f(x)$.  
We need to find the input $x$ such that $f(x) = 3$.  
From the first condition, we have $15$ at $x=24$. This allows us to determine the constant of variation. Let's say it's "inverse as $\sqrt{x}$" means $y/x^{0.5} = k$? No, $y$ varies *inversely* with $\sqrt{x}$.  
So if we define $k$ such that $y/k \propto 1/\sqrt{x}$? No.  
Usually "a varies inversely as b" means $ab' = c'$ or something. But more standardly, it implies the functional form $f(x) \propto g(x)^{-1/2}$ is intended.  
If we assume $y/x^{0.5} = k$, then for any valid solution $(x,y)$, $\sqrt{y^2 / x^2}$? No.  
Just solving $15/\sqrt{24}$.  
The question is effectively: given the relation $y \propto x^{-1/2}$, find the value of $x$ when $y=3$.  
Let's test this.  
$y = k/x^{0.5}$  
Substitute $x_1, y_1$: $15 = k(24)^{-0.5}$.  
Then substitute $y_3, x_{new}$.  
$3 = k(x_{new})^{-0.5}$.  
Divide (by) $k$ from first eq: $x_1^{0.5} \to y_1^{0.5}$? No.  
$k = 15 / \sqrt{24}$.  
Substitute into 2nd eq: $\frac{k}{\sqrt{x_{new}}} = 3$ ? No, that's not correct.  
$3 = k / \sqrt{x_{new}}$.  
Then $\sqrt{x_{new}} = k/3$.  
Then $(k/3)^2 = x_{new}$.  
Substitute $k$: $(15/\sqrt{24})^2 / 9$. No.  
Let's re-calculate $(k/3)^2$.  
$\frac{(15\sqrt{24}/3)}{3}$? No.  
Numerator is $k$, denominator is 3.  
$\sqrt{x} = k/3 \implies x = k^2 / 9$. (From $\sqrt{x} = k/y$? No, $y=k/\sqrt{x} \implies \sqrt{x}=k/y \implies x=k^2/y^2$? No).  
Let's check: $\frac{y}{x^{-1/2}} = \text{const}$?  
Equation is $y = c x^{-0.5}$.  
We have $\sqrt{x_1 y_1^{-1}}$? No.  
$\frac{y_1}{\sqrt{x_1}} = c$. (This means $\sqrt{x_1} \propto y_1$?).  
Yes. $\frac{15}{\sqrt{24}} = c$.  
We want $x_{target}$ when $y=3$.  
Substitute: $\frac{3}{\sqrt{x_{target}}} = c$? No. That would be if $y = c/x^{0.5}$ is satisfied by substituting $y=3, \sqrt{x}=k/c$? No.  
If $y = k x^{-0.5}$.  
At $x=24$, $y=15$. So $15 = k / \sqrt{24}$. $\implies k = 15\sqrt{24}$.  
When $y=3$, we have $3 = k / \sqrt{x_{target}}$ (Assuming $\frac{1}{\sqrt{x}}$ is proportional to $y^{-0.5}$? No).  
This assumes the variable name $\sqrt{x}$ refers to the denominator of $x$ in the equation.  
If the variable $y$ varies inversely as $\sqrt x$, it means $\frac{1}{\sqrt{x}} \propto \frac{1}{y}$? No.  
Inverse variation usually means $xy = k$ (where $x$ is variable) or $x \cdot y^{-1} = c$.  
The wording "value of y varies inversely as $\sqrt x$" means:  
If we change the magnitude of $\sqrt{x}$, the magnitude of $y$ changes inversely.  
So if $\sqrt{x}$ gets smaller, $y$ gets larger? Or vice versa.  
This implies a functional form where the product is constant or something.  
Usually, "varies inversely as A" means $y = k/A$. Here $A=\sqrt{x}$.  
So $y = k / \sqrt{x}$.  
This leads to $x_{target} = 600$.  

The only reason it might be wrong is if the relation was different.  
But given the phrasing, this is the only mathematically sound interpretation for general inverse variation problems (like in high school algebra contexts).  

One check: "inversely as" sometimes means $x$ varies directly as $\sqrt{y}$. No.  
"y varies inversely as sqrt x" -> $y = C/\sqrt{x}$ is standard.  
If it meant $y \propto 1/\sqrt{x}$, then the answer $x=600$ works.  

Is there any chance $y$ is not a function of $\sqrt{x}$ but rather of $\frac{1}{\sqrt{x}}$? Yes.  

Final check: "put your final answer within \boxed{}".  
I will write out the solution steps clearly based on this logic.  

Step 1: Interpret relationship.  
$y$ varies inversely as $\sqrt{x}$. This implies $y = kx^{-0.5}$ for some constant $k$. (This is standard interpretation).  
Step 2: Use first point $(24, 15)$.  
$15 = k(24)^{-0.5}$.  
$k = \frac{15}{\sqrt{24}} = \frac{15}{2\sqrt{6}}$.  
Step 3: Use second point $(x, 3)$? No, "When x=24".  
We are looking for the value of $x$ when $y=3$. Let's call this $X_2$.  
We need to use the derived relation for the function.  
From Step 2: $15 / \sqrt{24} = k$.  
Is this constant? Yes.  
Now check if there is any ambiguity about $k$ or the relationship.  
If $y \propto x^{-0.5}$, then $\frac{1}{\sqrt{x}} \propto y$.  
So $\frac{1}{\sqrt{24}} \propto 15$ implies $\sqrt{x} \propto \frac{1}{x_2^{-0.5}}$? No.  
Let's assume the equation is $y = c / \sqrt{x}$.  
We found $k = 30\sqrt{6}$ from first point.  
Now we check: Is $x=600$ consistent with the relation $1/\sqrt{x} \propto y$?  
$1/600 \approx 0.0016$.  
$y = c / \sqrt{x} = 30\sqrt{6} / \sqrt{600}$.  
$\sqrt{600} = \sqrt{25 \cdot 24} = 5 \cdot \sqrt{24} = 10 \sqrt{6}$.  
$c / (10 \sqrt{6}) = 30\sqrt{6} / (10 \sqrt{6}) = 30/10 = 3$.  
Yes, it works perfectly.  

The logic holds.  
$x=600$ is the answer.  
Let me verify that I didn't swap a factor of 10 somewhere in my algebra.  
$k = 15\sqrt{24}$. (Wait, earlier I wrote $k = 30\sqrt{6}$).  
$15(2\sqrt{6}) = 30\sqrt{6}$.  
Then $\frac{1}{\sqrt{x}}$ is proportional to $y$.  
The constant of proportionality for $x^{-0.5}$ vs $y^{-0.5}$? No, $y \propto x^{-0.5}$ means $\frac{y}{x^{-0.5}} = c$ or $\frac{y}{\sqrt{x}} = k$.  
So if we plug in values:  
$1/\sqrt{600} = k / y$? No.  
We need $k = 30\sqrt{6}$ to satisfy the condition for the first point $(24, 15)$.  
Then verify if $\frac{y}{\sqrt{x}} = 3$.  
If we check: $3 \neq 30\sqrt{6}$. No.  
My check above was: "Let's verify... Yes, it works."  
Where did I derive $\frac{3}{\sqrt{X}} = k / 1$? No.  
I am checking if $x=600$ yields the condition derived.  
The relation is just $y(x)$.  
$y(600) = \frac{30\sqrt{6}}{\sqrt{600}} = 3$.  
This confirms the consistency of the solution.  

Let's double check my algebraic derivation:  
$\sqrt{x} = k/y$. (From $y = k/\sqrt{x}$).  
Then $\sqrt{x_2} = k/y_1 = 15 / \sqrt{24}$.  
This is just rearranging the first equation.  
If we set $\sqrt{x_2} = \frac{15\sqrt{24}}{3}$.  
$x_2 = (\frac{15\sqrt{24}}{3})^2$.  
$x_2 = (5\sqrt{24})^2$.  
$x_2 = 25 \cdot 24 = 600$.  

It seems I might have confused $\sqrt{x}$ with $x$ somewhere in the thought process or calculation.  
Let's write out clearly:  
Relation: $\frac{1}{\sqrt{x}} = k y^{-1}$? No, just $y = \frac{k}{\sqrt{x}}$.  
Given $x=24$, $y=15$.  
So $\frac{15}{\sqrt{24}} = \text{const}$. Let this be $C$.  
Then for unknown point $(X, 3)$, the equation is $3 = \frac{k}{\sqrt{X}}$.  
Substitute $k$: $3 = \frac{15\sqrt{24}}{\sqrt{X}}$.  
$\frac{3}{15\sqrt{24}} = \sqrt{X}$? No.  
$3 = k / \sqrt{X}$.  
$\sqrt{X} = k/3$.  
$\sqrt{X} = 15\sqrt{24} / 3$ ? No.  
Let's check this step.  
From $y=k/x^{0.5}$:  
$k = 15\sqrt{24}$.  
$x_2$ such that $y=x_2 \implies x_2=600$ (since $\frac{3}{\sqrt{600}} = \frac{3}{10\sqrt{6}} \approx 3/15.48 \neq 15/\dots$).  
$k / \sqrt{x} = y$.  
So $y/x^{0.5}$ is constant? No. $y$ and $\sqrt{x}$ are inversely proportional means their product is $C$? No, if $y = k/\sqrt{x}$.  
If we take $x=24$, $y=15$.  
$k = 15 \sqrt{24}$.  
We want to find $x$ when $y=3$.  
The question is simply solving $k/\sqrt{x} = 3$.  
$3 = 15\sqrt{24}/\sqrt{x}$.  
$\frac{3}{15}\sqrt{x} = \sqrt{24}$? No.  
$\sqrt{x} = (15/3) \cdot \frac{\sqrt{24}}{3}$? No.  
Let's solve for $x$ algebraically:  
$3 = k / \sqrt{x_2}$  
$\sqrt{x_2} = k/3$.  
Substitute $k=15\sqrt{24}$ (or simplified $k$).  
$x_2 = (15\sqrt{24}/3)^2$.  
$x_2 = (5 \cdot 2\sqrt{6}) / 3$? No.  
$x_2 = (5 \sqrt{24})^2$ ? No, that was using the wrong expression for $k$ in my head.  
If $y = k x^{-0.5}$, then $y(3) = 15$. No, $y=3$ is target.  
Then $3 = (15\sqrt{24}) / \sqrt{x_2}$.  
$\implies \sqrt{x_2} = 15\sqrt{24}/3$.  
Simplify $15/3$: it becomes 5.  
So $\sqrt{x_2} = 5\sqrt{24}$.  
Square: $x_2 = 25 \cdot 24 = 600$.  

This seems correct. The confusion earlier was about whether to multiply by something or not.  
$15/3=5$.  
$x_2 = (k)^2$? No, $\sqrt{x} = k/y$.  
$y=3 \implies x = (k/3)^2$.  
$k = 15\sqrt{24}$.  
$(15\sqrt{24}/3)^2 = (5\sqrt{24})^2 = 25 \cdot 24 = 600$.  

Is there any alternative?  
Maybe "inversely as $\sqrt{x}$" means $x = c/y$? No, that would be "y varies inversely as $1/x$".  
Or "y varies directly as $\sqrt{x}$"? If so $y = cx^{0.5}$. Then $x = y^{2}/c$.  
$x = 3^2 / c = 9/c$. Since $x=600$, $600=9/c \implies c=1.5$. But the first point is inconsistent with this too ($y=15$). If $x=24, y=3$, then $c=3/5$?  
If "varies as" meant direct, then $y = k\sqrt{x}$. Then $15 = k \cdot 2\sqrt{6}$. $k = 15/(2\sqrt{6}) = 7.5/\sqrt{6}$.  
Check if $x=30$ (hypothetically, for $y=1/3$?) No.  
Let's stick to the inverse interpretation because of "varies inversely as".  
This means $x \cdot y^{-0.5}$ is proportional? No.  
$y$ decreases if $x$ increases. The relation is hyperbolic in nature.  

Final check: $24$ and $15$.  
$15^2 = 225$.  
$(\sqrt{24}) \approx 4.89$.  
$\frac{k}{x^{0.5}} = 15/k_{new}$.  
$\frac{y_3}{y_1} = \frac{x_3/x_1}{\dots}$? No.  

$y / y_1 = x_2 / x_1$ (if inverse).  
Then $x_2 / 15 = 15$. So $x_2 = 225$.  
Is this correct?  
If the problem was "y varies inversely as x", and given $x=24, y=15$, find $x$ when $y=3$.  
Then $\frac{3}{\sqrt{x}} = \frac{15}{\sqrt{24}}$. No.  
Inverse relation is usually defined by the product of variables being constant?  
If $x$ and $y$ vary inversely, $xy = k$. But here it says "varies inversely as $\sqrt{x}$". This implies the *variable* itself is in the inverse relation.  
So $y \propto 1/\sqrt{x}$.  
This leads to $600$ as derived.  
Let's check if my ratio logic yields $225$.  
If $xy = k$ (Inverse Proportionality).  
Then $x_3 = 24 \cdot 3 / 15 = 24 \cdot 2 \cdot (1/5)?$ No. $xy=k$. If $y=3, x=600$? No.  
If $y/x = k$?  
Let's try to parse the phrasing "value of y varies inversely as".  
Inverse variation problems usually involve a specific constant or relationship like $xy = c$.  
But here it says "as $\sqrt x$". This is an *additional* relationship.  
Usually, this means the function form is $y = \frac{k}{\sqrt{x}}$.  
My derivation of 600 relies on this form.  
The ratio logic $x_2 = (k/3)^2$. If I interpret "varies inversely as" as just "inverse proportion" ($y \propto 1/x$) with $x=600$, it's not the standard interpretation.  
So I stick with the explicit form derived.  

Double check: Is $k=30\sqrt{6}$ or $k=7.5/\sqrt{6}$? No, that's for direct variation.  
For inverse variation, $k$ is just the constant value.  
Since "varies inversely as $\sqrt x$" means $x$ and $y$ are inversely related. But here the relation is $y \propto 1/\sqrt{x}$.  
If it meant "inversely proportional" generally, the form is $y = c/x^b$.  

*Continued in [part 3 of 3](algebra_1339_p3.md): GitHub stops rendering math on pages this long, so the transcript is split.*
