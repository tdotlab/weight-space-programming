# test/algebra/276.json, part 3 of 3

[Previous part](algebra_276_p2.md) · [Start](algebra_276.md)

Note: $AB$ must be 10. So $A,B$ can be $(1,10), (-1,-10), (2,5), (-2, -5)$.  
Also $(5,2)$ and $(-5,-2)$ are not in the set of pairs with product 10 if we consider negative signs? No.  
Let's list systematically:  
Factors of 10: $\pm 1, \pm 2, \pm 5, \pm 10$.  
Pairs $(A,B)$ with $AB=10$:  
   - $(1, 10)$ -> linear term: $3(1) - 8(10) = -77$. (Reject)  
   - $(2, 5)$ -> linear term: $3(2) - 8(5) = -34$. (Reject)  
   - $(5, 2)$ -> linear term: $3(5) - 8(2) = -1$. (Accept)  
   - $(-1, -10)$ -> product is 10. But let's check sign again. If A=-1, B=-10. Then $AB=10$.  
Linear term: $3(-1) - 8(-10) = -3 + 80 = 77$. (Reject)  
   - $(-5, -2)$ -> linear term: $3(-5) - 8(-2) = -15 + 16 = 1$. (Reject)  
Or if A=-5, B=2? Product is -10. Not allowed for $AB=10$.  

So the unique pair of coefficients is $(A, B) = (5, 2)$.  
Thus $AB + B = 10 + 2 = 12$.  

The question is "What is AB+B?".  
Answer 12.  

The question might be a trick where there are multiple pairs but A and B are integers? No.  
If $(A,B) = (5, -2)$ is considered valid factorization $Ax-8$ and $Bx+3$. Then $AB = -10 \neq 10$.  
So this pair doesn't satisfy the leading coefficient condition (or rather product of A and B must be 10 if we assume standard expansion). But in my derivation, I enforced $AB=10$.  
The problem statement does not require $(Ax-8)(Bx+3)$ to have leading coeff 10?  
It just says "expression can be written as". The expression is fixed. The form must match the expression exactly.  
Since $A$ and $B$ are variables of the factorization, I must satisfy the equation derived from coefficient matching.  
If I pick $(A,B) = (5, -2)$ for a different reason? No, product $AB=-10  

## Answer

*(none: the token cap hit during thinking)*
