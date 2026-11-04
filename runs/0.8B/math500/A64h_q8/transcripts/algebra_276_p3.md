# test/algebra/276.json, part 3 of 3

[Previous part](algebra_276_p2.md) · [Start](algebra_276.md)

$5x(2x) = 10x^2$.  
$5x(3) = 15x$.  
$-8(2x) = -16x$.  
$-8(3) = -24$.  
Sum of linear terms: $15x - 16x = -x$.  
So this works perfectly.  

Now I need to know if the expression $(Ax-8)(Bx+3)$ expands as $AB x^2 + (3A - 8B)x - 24$?  
Or does it expand as $AB x^2 + 3Ax - 8Bx - 24$? No, that would be missing the $5x \cdot 3 = 15x$ term if we consider linear terms.  
But wait!  
My formula check $(Ax)(Bx) + (Ax)(3)$ assumes the term is $3A x$.  
In $(5x-8)(2x+3)$, the term with 'x' from first factor is $5x$. The term in second factor that multiplies it is 3. So we have $5x \cdot 3$. This is a term with coefficient 15? No, wait.  
Is this correct?  
Term of first factor: $(Ax)$. Constant term in expansion? No.  
Let's look at the terms explicitly from the product definition.  
The polynomial $P(x)$ has coefficients.  
Coefficient of $x^2$: $AB$.  
Coefficient of $x$: Sum of products of coeffs of $x$ in each factor?  
$(Ax-8)(Bx+3) = x \cdot (A x - 8) + x \cdot (Bx + 3)$? No.  
Let's use linearity.  
$= A(Bx^2) + (-8)\cdot Bx + A(3)x + (-8)(3)$?  
If I consider $(Ax-8)(Bx+3)$ as product of two polynomials.  
First term: $Ax$. Second: $Bx+3$.  
Product: $AB x^2$ (coeff 10).  
Wait, the first factor's terms are $Ax$ and constant -8. The second's are $Bx$ and constant 3.  
Let's check cross terms again.  
Terms involving 'x': $A \cdot B$, $A \cdot 3$, $(-8) \cdot (-8)$? No.  
Terms with 'x' are:  
From $Ax$:  
- With $Bx$ $\to AB x^2$. (Coeff $AB$).  
  - With constant term 0? No, with the other term of second factor? No.  
$(Ax)(Bx)$ is correct.  
    - With constant term 3? No. $3$ is in second factor, not multiplied by $A$ or anything else to produce linear term.  
Wait. The term is $3 \cdot Ax$? No, the term is $3$. It's a number.  
If I have $(Ax-8)$ and $(Bx+3)$.  
Terms involving 'x' from first factor: $Ax$ and constant -8.  
Terms involving 'x' from second factor: $Bx$ and constant 3.  
Wait, this is wrong because the term "3" in the polynomial $(Bx+3)$ is not $Bx$. It is a number.  
So there is no linear term coming from $Ax \cdot 3$ (which would be $3Ax$) unless I am multiplying by something else.  
Let's check the expansion of $(5x-8)(2x+3)$.  
$5x \cdot 2x = 10x^2$.  
$5x \cdot 3 = 15x$. (Term from first factor).  
$-8 \cdot 2x = -16x$. (Term from second factor? No, this would be $-16x$).  
$-8 \cdot 3 = -24$. (Constant).  
So the terms with coefficients $x$ are: $15x$ and $-16x$.  
Sum is $-1x$.  
This implies $A=5, B=2$ leads to $AB  

## Answer

*(none: the token cap hit during thinking)*
