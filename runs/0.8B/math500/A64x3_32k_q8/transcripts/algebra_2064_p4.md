# test/algebra/2064.json, part 4 of 4

[Previous part](algebra_2064_p3.md) · [Start](algebra_2064.md)

*   Check at $x=-7$: $-(-49) - 5(-7) + 14 = 49 + 35 + 14 = 98$? No, $E(-7)$ should be 0.  
    *   At $x=-7$, $( -7+7)(2-(-7)) = 0 \cdot (9) = 0$.  
    *   My calculation: $-(-49) + 35 + 14 = 49 + 35 + 14$? No.  
    *   $E(x)$ polynomial expansion is correct if evaluated at root?  
    *   Let's re-calculate $(x+7)(2-x)$ value at $x=-7$.  
        *   $(-7+7)(2-(-7)) = 0 \times 9 = 0$.  
    *   My manual calculation: $-(-49) + 35 + 14$? No, that was for $E(x)$ expansion.  
        *   Expansion term by term check:  
            *   Term $x(2) = 2x$. At -7: $2(-7) = -14$.  
            *   Term $x(-x) = -x^2$. At -7: $-49$.  
            *   Term $7(2) = 14$. At -7: $+14$.  
            *   Term $7(-x) = -7x$. At -7: $-7(-7) = +49$.  
        *   Sum: $2(-7) - 49 + 14 + (-7)(-7)$? No.  
        *   $(x+7)(2-x)$.  
            *   $x$ times $(2-x)$ is $2x - x^2$.  
            *   $7$ times $(2-x)$ is $14 - 7x$.  
            *   Total: $-x^2 + (-5)x + 14$.  
        *   At $x=-7$: $-(-49) - 5(-7) + 14 = 49 + 35 + 14$? No, $+35 + 14 = 49$. $49 \neq 0$.  
        *   Why did my check say it was 0?  
            *   Ah, $(x+7)$ is zero at -7. So term 2-(-7) is 2+7? No.  
            *   Let's recalculate expansion: $x(2-x) + 7(2-x)$.  
            *   At $x=-7$:  
                *   $(-7)(2 - (-7)) = (-7)(9) = -63$.  
                *   $7(2 - (-7)) = 7(9) = 63$.  
                *   Sum: $0$. Correct.  
            *   My previous manual check for $x=-7$ was wrong because I thought $(2-(-7))$ is correct? No, $2-(-7)=9$. Yes.  
            *   My expansion calculation error was: I evaluated term by term incorrectly (e.g., $+49$ instead of $-63$ or similar).  
            *   So expansion is correct.  
*   Okay, so roots are -7, 2 for the polynomial inside $P(x) = -(x+7)(2-x)$? No.  
    *   Polynomial expression $E(x) = -4x^2 - 20x + 56$.  
    *   Roots of $E(x)=0$:  
        *   $-4x^2 - 20x + 56 = 0$.  
        *   Divide by -4: $x^2 + 5x - 14 = 0$.  
        *   $(x+7)(x-2) = x^2 - 2x + 7x - 14$? No, sum is $-7+2=-5$, product is 14.  
        *   Yes, roots are correct: $x=-7, 2$.  
*   So $E(x)$ has roots at -7 and 2.  
    *   Since vertex x is -2.5 (midpoint), and it's a downward parabola ($A<0$), max value at vertex should be positive? No, max of a downward parabola with roots -7, 2 implies that the vertex is the highest point above the axis. But since the interval between roots contains -2.5, which is in between -7 and 2, this implies the function decreases to min (vertex) then increases.  


## Answer

*(none: the token cap hit during thinking)*
