# test/intermediate_algebra/1365.json, part 2 of 2

[Previous part](intermediate_algebra_1365.md)

So the function decreases on $(-\infty, 15]$ and increases on $[15, \infty)$.  
The global minimum is indeed at $x=15$.  
Since the interval of interest is $[p, 15]$, which is a subset of $(-\infty, 15]$, the function is monotonic decreasing on this sub-interval.  
Therefore, the minimum value on $[p, 15]$ is attained at the rightmost point, which is 15.  

Value is $f(15) = |15-p| + |15-15| + |15-(p+15)|$  
$= (15-p) + 0 - p = 15 - 2p$.  
**HOLD ON**.  

Let me re-calculate $f(15)$ carefully.  
$f(15) = |15-p| + |15-15| + |15-(p+15)|$  
$= |15-p| + 0 + | -p |$  
Since $0 < p$, $|15-p| = 15-p$.  
And $|-p| = p$.  
So $f(15) = (15-p) + 0 + p = 15$.  

Why did I write $15-2p$ just now in my head?  
Ah, $|x-p|$ is $(15-p)$, $|x-(p+15)|$ is $(p+15-15) = p$. No.  
Let's check the term for $x=15$: $|15-(p+15)| = |-p| = p$.  
So sum is $(15-p) + 0 + p = 15$. Correct.  

Earlier calculation:  
Term 2 was $(15-x)$ at $x=15$, which is 0.  
Term 3 was $((p+15)-x)$. At $x=15$, value is $p$.  
Term 1 was $(x-p)$. At $x=15$, value is $15-p$.  
Sum: $(15-p) + (0) + (p) = 15$.  

My previous simplification:  
$f(x) = (x-p) + (15-x) + (p+15-x)$  
At $x=15$:  
$(15-15) + (15-15) + (p+15-15) = 0 + 0 + p$. No.  

Let's re-expand the simplified formula at $x=15$.  
The terms were:  
1. $|x-p| = x-p$ for $x \in [p, 15]$.  
   2. $|x-15| = 15-x$ for $x \in [p, 15]$.  
    3. $|x-(p+15)| = p+15-x$ for $x \in [p, 15]$.  

Sum: $(x-p) + (15-x) + (p  

## Answer

*(none: the token cap hit during thinking)*
