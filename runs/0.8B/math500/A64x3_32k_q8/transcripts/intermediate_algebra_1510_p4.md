# test/intermediate_algebra/1510.json, part 4 of 4

[Previous part](intermediate_algebra_1510_p3.md) · [Start](intermediate_algebra_1510.md)

Let's pick $z_1=1$. Then $z_2, z_3, z_4$ must sum to -1.  
Is there such a set? Yes. Let's say vertices of equilateral triangle on circle (no, that sums to non-zero).  
Vertices of regular pentagon (sum is 0)? No.  
But we have freedom to choose points.  
Let's just pick $a=1$. Then $b+c+d = -1$.  
If we can find 3 distinct points on unit circle summing to -1?  
Yes, let them be $\phi_2, \phi_3, \phi_4$.  
Is it possible to have $|z_i|=1$ such that $\sum z_i=-1$?  
Let's try. Let $z_2 = 0$ (not allowed).  
Let's try angles $\pi/6, \pi/2, -\pi/3$? No.  
The condition is just that the sum of complex numbers is $-1$.  
Since we can choose any set of distinct points on unit circle, we can definitely find such a set if it exists in terms of "distinct complex numbers".  
Is it possible to satisfy $\sum z_i = 0$ with distinct moduli 1? Yes.  
So, the maximum value is not constrained by existence.  
However, I need the max product of $(a+b)$ etc.  
Let's try to evaluate for specific configuration.  
Let $z_1=1$. Then we need sum of others $-1$.  
Since distinct modulus 1, let's pick $z_2 = e^{i \alpha}$ and others such that they cancel.  
For $n=4$, we can pick $z_2, z_3$ on unit circle? No, just 3 numbers.  
We need 3 numbers summing to -1.  
Let's choose $z_2 = e^{i \pi/6}$. Then we need $z_3+z_4 = -1 - (e^{i \pi/6}) = -0.866 - i(0.866)$? No, sum must be real negative?  
No, the condition $\sum z_i = 0$ means sum is 0 complex number.  
So we need $\sum_{k=1}^4 e^{i \theta_k} = 0$.  
Let's choose angles $\theta_1=2\pi/3, \theta_2=\pi/6, \theta_3=\dots$?  
If I pick $z_1=e^{i \pi/3}$, then we need sum of other 3 to be $-e^{i \pi/3}$.  
Let's try to find such points.  
Actually, the problem likely implies a constraint like "distinct roots of unity". But if  

## Answer

*(none: the token cap hit during thinking)*
