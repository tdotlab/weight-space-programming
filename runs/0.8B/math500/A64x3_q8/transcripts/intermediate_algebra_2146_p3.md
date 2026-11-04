# test/intermediate_algebra/2146.json, part 3 of 3

[Previous part](intermediate_algebra_2146_p2.md) · [Start](intermediate_algebra_2146.md)

If we set $P(x) = x^2 - 2x + 2$, then $P(11)=91 \le 181 \le 201$.  
Is there a reason to pick this one? No.  

Maybe the question implies that for a given $x$, the value of $P(x)$ must be one of the values $A(x)$ and $B(x)$.  
But "satisfying" means *some* quadratic.  
However, looking at similar problems, usually the solution involves setting up an equation like $\min(A(x), B(x)) = P(x)$ or something? No.  

Let's try to interpret the problem differently.  
Maybe the coefficients of $P(x)$ must be integers? Or maybe $P(x)$ has roots at integers?  
If $x^2 - 2x + 2 = A(x)$ is in the range, maybe the polynomial is unique?  
What if $P(11)=181$ fixes the coefficients uniquely? No, we only have 3 constants.  

Let's assume the question is a trick and there's a constraint on $x^2 - 2x + 2 \le P(x) \le 2x^2 - 4x + 3$.  
Notice that $(x-1)^2 + 1$ is an upper bound for $P(x)$? No, lower bound.  
So $P(x)$ must be at least $(x-1)^2 + 1$.  
And $P(x)$ is at most $2(x-1)^2 + 2$.  
If we assume that the inequality must hold *for all real numbers*, then this implies that for any value of $x$, the interval is valid.  
But since $B(x) \ge A(x)$, and they differ by a quadratic, this constraint is satisfied if $P(x)$ stays in between? No, it's always true that $A(x) < P(x) < B(x)$.  
The problem must imply something stronger.  

What if the inequality is actually about *minimization* of $x^2 - 2x + 2$? No.  
Let me search for similar problems or properties.  
Usually, such problems are:  
"Find the maximum value of P(16) given P(11)..."  
But here we don't have a max/min constraint.  

Is it possible that $P(x)$ is the polynomial $x^2 - 2x + 2$? No.  
Let's  

## Answer

*(none: the token cap hit during thinking)*
