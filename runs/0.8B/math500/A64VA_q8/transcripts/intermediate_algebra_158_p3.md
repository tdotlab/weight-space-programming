# test/intermediate_algebra/158.json, part 3 of 3

[Previous part](intermediate_algebra_158_p2.md) · [Start](intermediate_algebra_158.md)

If I have variables $a, b, c, d$.  
$\partial f / \partial a = b^2 c^3 d^4$. (Deriv wrt $a$ is coeff of $a$, which is 1. So it's just that.)  
$\partial f / \partial b = 2ab c^3 d^4$. (Deriv of $b^2$).  
$\partial f / \partial c = 3 a b^2 c^2 d^4$. (Deriv of $c^3$ is $3c^2$, coeff is $b^2 a d^4$? No. The term is $(a \cdot b^2 \cdot c^3 \cdot d^4)$).  
$\partial f / \partial d = 4 a b^2 c^3 d^3$. (Deriv of $d^4$).  

Let's re-verify the derivative of $c^3$ term.  
The term is $(a)(b^2)(c^3)(d^4)$.  
Partial wrt $c$: it involves $c^3$. Deriv is $3c^2$. The other terms are $a b^2 d^4$ (since they don't contain $c$). So yes, $\frac{\partial f}{\partial c} = 3 a b^2 c^2 d^4$? No.  
Let's check the exponents in my previous "Lagrange" derivation.  
I had: $\lambda = \dots$.  
Wait, I see now that I might have misapplied $f_a, f_b, f_c, f_d$.  
Let's use the property that gradients of variables are independent.  
Let's write out the vector forms.  
$\nabla f = (0, 0, 0)$? No.  
$\nabla f = (\frac{\partial f}{\partial a}, \frac{\partial f}{\partial b}, \dots)$.  
If $\frac{\partial f}{\partial a} = b^2 c^3 d^4$, then $\nabla f$ first component is $b^2 c^3 d^4$.  
$\frac{\partial f}{\partial b} = 2a b c^3 d^4$? No. It's $a \cdot (1) \cdot b \cdot 2c^3 d^4$?  
Let's check again.  
$f = a b^2 c^3 d^4$.  
$\frac{\partial f}{\partial b} = \frac{\partial}{\partial b}(a \cdot b^2 \cdot c^3 \cdot d^4) = 1 \cdot a \cdot 2b \cdot c^3 \cdot d^4 + a \cdot b^2 \cdot 0$. No.  
This assumes $c$ and $d$ are variables too? No, they are constants wrt $b$.  
So yes, $\frac{\partial f}{\partial b} = 2ab c^3 d^4$.  
But this is wrong. The term is $a \cdot b^2 \cdot c^3 \cdot d^4$.  
So partial w.r  

## Answer

*(none: the token cap hit during thinking)*
