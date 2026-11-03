# test/counting_and_probability/389.json (Counting & Probability, level 2)

> Mikka wants to order a pizza with two different toppings. He has 8 different toppings to choose from. How many different pizzas could he order?  

**Correct.** Gold `28`, predicted `28`. Finish: stop, 7132 tokens, 23 waits, 513.3 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's a thinking process that leads to the solution:  

1.  **Analyze the Request:**  
    *   **Goal:** Calculate the number of different pizzas Mikka can order.  
    *   **Condition 1:** The pizza has two distinct toppings. (Implies we are choosing between specific pairs from the set).  
    *   **Condition 2:** He has 8 different toppings to choose from. Let's call this the total population $N=8$.  
    *   **Interpretation:** Is "two different toppings" a requirement for the count? Yes, he wants pizzas with *two* specific toppings selected.  

2.  **Identify the Mathematical Structure:**  
    *   This is a combination problem (choosing items from a larger set without regard to order).  
    *   We are selecting 2 toppings from 8.  
    *   The phrase "How many different pizzas" implies that the arrangement matters? No, pizza plates usually have the order of toppings (toppings at the top left or right) and the specific type. But here, since it says "Two different toppings", the core constraint is *how many* ways to choose *two* distinct items from 8.  
    *   Wait, let's re-read the phrasing carefully: "Mikka wants to order a pizza with two different toppings. He has 8 different toppings to choose from."  
    *   Usually, "different pizzas" implies specific ordering of the toppings (e.g., topping A on top and B on bottom) OR it just means the count of possible subsets. However, looking at standard combinatorial problems: "Ordering a pizza with two toppings" is usually interpreted as picking 2 items from a set of distinct items to put on a plate. If the toppings were identical (e.g., Red and Green are indistinguishable), we wouldn't be talking about *different* pizzas. Here, all 8 toppings are distinct.  

3.  **Step-by-Step Calculation:**  
    *   Let $n$ be the number of available toppings: $n = 8$.  
    *   We want to choose a set of 2 toppings ($k=2$).  
    *   Since there are 8 toppings, and we need to select 2 specific ones from these 8.  
    *   Let's check if order matters. Does "A on top and B on bottom" count as different from "B on top and A on bottom"? Yes, that is a difference in pizza composition (top vs side). The prompt asks for the number of *different pizzas*.  

4.  **Wait, hold on.** Let's re-read again: "Mikka wants to order a pizza with two different toppings."  
    *   This implies we are selecting *two specific items* from the set of 8.  
    *   If order matters (e.g., Top-Left vs Bottom-Right), it's combinations of size 2 ($ \binom{N}{k} $).  
    *   If order doesn't matter (e.g., just the set $\{A, B\}$ makes a pizza), it is also combinations.  
    *   BUT, usually, in these problems (like "How many different pizzas"), we are selecting 2 toppings. Let's assume **Combinations**: The problem is finding the number of ways to choose 2 distinct items from 8 distinct items.  

5.  **Calculation:**  
    *   Total toppings $N = 8$.  
    *   Number of toppings to select = $k = 2$.  
    *   Formula: $ \binom{n}{k} = \frac{n!}{k!(n-k)!} $.  
    *   Here $ n = 8 $, $ k = 2 $.  
    *   $ \binom{8}{2} = \frac{8 \times 7}{2 \times 1} = 4 \times 7 = 28 $.  

6.  **Alternative Interpretation Check:**  
    *   Could the question imply picking a specific *type* of pizza? No, it asks for "How many different pizzas".  
    *   Is there any ambiguity in "with two different toppings"? It implies we are choosing toppings to put on a plate. If he chooses $T_1$ and $T_2$, they must be distinct. Since all 8 are different, this is straightforward.  

7.  **Is it Permutations?**  
    *   Sometimes, "pizza order" means the sequence of toppings (e.g., Tomato sauce on bottom, cheese on top). This would be a permutation problem. But usually, when asking for the number of pizzas, we assume the physical placement matters less than the selection, i.e., a set of toppings is sufficient to identify a unique pizza configuration if you are talking about a set of items from a specific pool.  
    *   However, let's look at the wording: "He has 8 different toppings". This means he can pick any pair. The question asks "How many different pizzas". If two pizzas had the same composition (e.g., Tomato and Pepper), they would be identical. The question implies he selects a subset of size 2 from the set $\{T1..T8\}$.  
    *   Let's consider if order mattered in the selection process. Since there are only 2 toppings selected, and all are distinct, $A$ and $B$ are distinguishable. If I have just two pizza items (e.g., "Pizza with Tomato and Cheese"), that is one unique configuration regardless of whether I list them as {T1, T2} or {T2, T1}. But since the problem states "with two different toppings", usually implies we select two distinct items.  
    *   Usually, in standard math contexts (like AMC/AMC 8 problems), if it says "pick a subset of size $k$" from a set, it refers to combinations ($n \choose k$). If order matters for the pizza (i.e., which topping is on top vs bottom), it would say "order matters" or "permutations".  
    *   Therefore, assuming standard Combination/Selection: $\binom{8}{2} = 28$.  

    *   *Wait, let me double check the wording "two different toppings".*  
    *   Does "different toppings" imply that if I have two distinct types of toppings (e.g., Cheese and Onion), do I distinguish them by their specific names? No. But here, they are just 8 distinct items from a pool. The question asks for the number of pizzas. If Mikka has 8 specific toppings available to choose from:  
        *   Top Pizza: {Tomato, Cheese}  
        *   Bottom Pizza: {Cheese, Tomato} -> This would be the same pizza if order doesn't matter? No, usually "Pizza with Tomato and Cheese" is one distinct thing.  
        *   But wait, if I have 8 toppings, say $T_1$ through $T_8$, all distinct.  
        *   If Mikka wants a "pizza with two different toppings".  
        *   Does he mean he has a pizza plate with 2 distinct items (a subset of the pool) on it?  
        *   Let's check the standard phrasing of this problem type (often found in online quizzes or textbooks).  
        *   Common question: "A group of 8 people want to eat...".  
        *   Common question: "How many different pizzas can he order?" with 2 toppings.  
        *   Interpretation A: Combinations ($n \choose k$).  
        *   Interpretation B: Permutations ($P(n, k)$) if the topping sequence (top/bottom) matters (which it doesn't logically, since a pizza usually has toppings listed left-to-right, but the specific selection of "tomatoes" is one way to form a pizza).  

    *   Let's re-evaluate based on common sense and math conventions.  
    *   If I have 2 items in a set $\{A, B\}$, how many ways can I choose a pizza?  
    *   If the toppings are "Tomato" (T1) and "Pepper" (T2). The pizza has T1 and T2.  
    *   Is {T1, T2} different from {T2, T1}? Yes or No depending on the context. In many pizza contexts (ordering at a shop), the order matters. A pizza is often described by ingredients ordered. So $2! = 2$ pizzas? But usually, "How many pizzas" implies "what are the possible distinct items". If you have {T1, T2} and {T2, T1}, are they different?  
    *   Usually, "pizza toppings" imply a set of ingredients on a plate. However, often these problems simplify to: You choose 2 items from 8. If the items are distinct (8 toppings), then it is $\binom{8}{2}$.  

    *   Let's look at similar examples in literature.  
    *   Example: "You have 5 different types of apples, how many combinations of 3?" -> $\binom{5}{3} = 10$. (Combination).  
    *   Example: "A group has 6 distinct people. How many ways can we form a committee of 2?" -> Usually $\binom{6}{2}$ or $P(6, 2)$. If it's a team, order matters (Chairman vs Vice-Chairman). But if it's about toppings on a plate, the "tomato" part vs the "pepper" part is usually considered distinct from the perspective of just "two items". However, in many math riddles, simply asking for the number of *different pizzas* implies selecting 2 items from the set to put onto a specific plate. If the toppings are $T_1$ and $T_2$, the pizza is defined by that set $\{T_1, T_2\}$. Since all $T_i$ are distinct, any subset of 2 is different (assuming they are distinct).  
    *   Let's look at the wording again. "Two different toppings". This phrase usually implies we select two items from the total set. It does not imply an ordered sequence for the pizza. The phrase "Pizza with X and Y" is just the set $\{X, Y\}$.  

    *   *Decision:* I will assume combinations ($N \choose k$).  
    *   $N = 8$. $k=2$.  
    *   $\binom{8}{2} = \frac{8 \times 7}{2} = 28$.  

    *   *Wait, let me check the phrase "two different toppings".*  
    *   Is there a catch? Maybe Mikka just wants to order a pizza that has at least one of these two types (e.g. Pizza T1 + Pizza T2). That would be $8+8=16$ pizzas if he had specific pairs, or $16 \times 8$? No.  
    *   Let's stick to the most straightforward interpretation: Selecting a subset of size 2 from 8 distinct items.  

    *   Let's double check if "different toppings" implies that we are picking specific types (e.g., A, B, C) and the set is just {A,B} which can be reordered or not.  
    *   If it was permutations ($P(8, 2)$), the answer would be $8 \times 7 = 56$.  
    *   Let's think about pizza toppings. If I want a tomato-pizza and a pepper-pizza, those are distinct pizzas? Yes. If I put them in sequence (Tomato on top, Pepper on bottom) vs (Pepper on top, Tomato on bottom), does the problem imply that? Usually not. It asks for "how many different pizzas".  
    *   However, standard interpretation of "How many ways to choose 2 toppings" is combinations $\binom{8}{2}$.  

    *   Let's try to find if there is any other constraint. "He has 8 different toppings". If he wants a pizza with two toppings (A and B), then A and B are the toppings.  
    *   This sounds like the standard $C(n,k)$ problem.  

    *   Is it possible the question implies "Order of toppings matters"?  
    *   Let's re-read carefully: "Mikka wants to order a pizza with two different toppings."  
    *   If I pick Pizza 1 (tomato, pepper) and Pizza 2 (pepper, tomato).  
    *   Usually, we say "Pizzas are unique if their toppings are different". But does the problem state that?  
    *   "How many different pizzas could he order?" implies a specific instance of pizza.  
    *   If I have tomatoes $T1..T8$, and peppers $P1..P8$. If I want a pizza with toppings from the set $\{T_i, T_j\}$, and I just say "a pizza" it refers to the physical item. But since there is only 2 toppings specified, this usually implies selecting two distinct items.  
    *   Let's check for any trick regarding "two different toppings". Does that imply we are looking at sets? Yes.  
    *   If the answer were permutations ($56$), it would be phrased "How many ways can he order... with two toppings where A on top, B on bottom is different from B on top, A on bottom?" That's unlikely unless stated.  
    *   The most standard interpretation for a general riddle or math problem asking for the count of subsets is combinations.  

    *   Calculation: $\binom{8}{2} = 28$.  

    *   Wait, let me play devil's advocate. Could "different toppings" mean we are picking from a set of types (e.g., {1, 2}, where types are just labels for the specific toppings)?  
    *   If there are only two types of toppings available in Mikka's inventory (e.g., he has Type A and Type B). Then $8$ is the pool. But "different toppings" usually refers to specific attributes of the pizzas.  
    *   Let's assume the question asks for the number of combinations: 28.  

    *   Let me check if there's any ambiguity about "order".  
    *   A pizza is just a plate with toppings. If I order a tomato-pizza and a pepper-pizza, are they different? Usually yes (e.g., Tomato on top of Cheese vs Pepper on top of Tomato). But since the prompt says "pizza with two different toppings", it likely means we are choosing a subset of size 2 from the given 8.  
    *   Let's assume the question is "How many combinations of 2 distinct items can be formed from a set of 8 distinct items?".  
    *   Answer: $\binom{8}{2} = 28$.  

    *   Wait, could it be $1/8$? No.  
    *   Let's verify the phrase "two different toppings". This is slightly unusual phrasing for a math problem because usually, we say "choose two toppings" (implies combinations) or "choose two toppings" (implies permutations). However, the result $\binom{n}{k}$ assumes items are distinct. The prompt states "He has 8 different toppings". If there were only 2 types (e.g., Pepper and Cheese), he could choose any pepper or cheese. But he specifies *two* toppings.  
    *   Let's stick with the combination interpretation ($\binom{8}{2} = 28$).  

    *   *Alternative Interpretation:* "Pizza" implies the whole plate has a specific arrangement (e.g., toppings A, B on top of C). No, that's overthinking.  
    *   Let's assume standard combination logic for this type of problem.  

    *   One more check: Is it possible that "different toppings" means the toppings are distinct objects (like different fruits), and he needs to pick two? The answer $\binom{8}{2}$ stands out as the most mathematically sound interpretation of selecting 2 distinct items from a set of distinct items without considering order.  
    *   However, there is a very specific logic puzzle where "different pizzas" means ordering matters (e.g., A, B vs B, A).  
    *   Let's search for similar problems online to see the convention.  
    *   "How many different pizzas with two toppings can be ordered?" usually leads to combinations ($\binom{n}{k}$) if it just asks for selection. If order matters, it asks for permutations. Without further info (like "tomato on one side"), the default assumption in combinatorics is that we are choosing a set of items.  

    *   Wait, let's check the context. "Mikka wants to order a pizza with two different toppings."  
    *   This sounds like he selects a subset of 2 toppings. If the answer were permutations, it would be 56. But if I select {A, B}, is that distinct from {B, A}? In real life, yes or no? If you just have tomatoes and peppers, a tomato-pizza (tomato on top) and a pepper-pizza (pepper on top) are different pizzas. A tomato-pepper plate vs pepper-tomato plate. The prompt doesn't specify "topped with" specific toppings A or B, but "two different toppings". If I pick a pizza that contains a tomato and a cheese, that's one. If I pick a pizza that contains a pepper and a mushroom...  
    *   Wait, is there any ambiguity in the phrasing "He has 8 different toppings"? It means 8 distinct items.  
    *   Is it possible "different toppings" refers to specific *types*? E.g., Toppings are just categories (e.g., Tomato and Pepper). If he has 8 different types of items, does he mean the types are the same, or is there only one type of topping available? "He has 8 different toppings to choose from." This strongly implies that *each* of the 8 items in his list is a unique ingredient. Since it says "different toppings", and asks for pizzas with "two different toppings", we must select two distinct ingredients.  
    *   Therefore, we choose 2 ingredients out of 8.  
    *   $\binom{8}{2} = 28$.  

    *   Let's think if there is a trap.  
    *   Could the question be asking about permutations? "Order matters" often appears in riddles where you can swap toppings. But here, we have 2 distinct items to select. Usually, unless specified (e.g., "How many different orders of toppings"), the order does not matter (just a set).  

    *   Let's calculate:  
    *   If $n=8$ and we need 2 toppings.  
    *   Number of ways = $8 \times 7 / 2 = 28$.  

    *   Wait, looking at the wording again: "He has 8 different toppings to choose from." This implies he has a list of ingredients. He wants to order *a* pizza with *two* toppings.  
    *   If I have 8 choices (e.g., Apple, Banana), and I want to select a pizza containing one of the chosen fruits? No, "pick two different toppings".  
    *   This sounds like:  
        *   Item 1: T1  
        *   Item 2: T2  
        *   ...  
        *   Item 8: T8.  
    *   Mikka picks 2 items from these.  
    *   Number of ways = $\binom{8}{2}$.  

    *   If the question was "How many different pizzas can he order" (implying he wants a pizza that satisfies the criteria), and the criteria is "with two different toppings".  
    *   The only potential interpretation is if the question implies permutations (ordering matters). But standard math convention dictates $\binom{n}{k}$ unless order is emphasized.  

    *   Let's consider if there's any constraint on the pizza size or other factors. No.  

    *   Wait, could "two different toppings" mean 2 *types* of toppings?  
    *   If he has types A, B, C, D... (and all are available). Then he chooses a subset.  
    *   This leads to $\binom{8}{2}$.  

    *   What if he needs to select 2 specific toppings from the set of 8? (e.g. Pizza with Tomato and Pepper).  
    *   Is there a case where it's 56? Only if order matters. For example, "How many ways can you order two different toppings such that T1 is on top..." No, just "different pizzas".  
    *   I'll stick to the combination.  

    *   Let's do a sanity check. If he has only 2 types of toppings (e.g., Tomatoes and Peppers). Then he can make Pizza A with both (tomato-pepper) or Pizza B with neither? No, "order a pizza with two different toppings".  
    *   This sounds like selecting 2 distinct items from the set.  

    *   Final check: The phrase "different toppings" might imply that if I have {Tomato, Onion} it's valid, but maybe {Onion, Tomato} is not? No, since they are distinct items in his collection (all 8 are different).  
    *   Wait, does the prompt say he has *one* pizza or *many* pizzas? "Mikka wants to order a pizza". Singular.  
    *   "How many different pizzas could he order?"  
    *   This implies we are selecting 2 toppings from the set of 8 such that they form a unique combination.  

    *   Wait, is it possible this is a problem about *permutation*? Let's look for any nuance.  
    *   If I have tomatoes and peppers. Is the pizza {Tomato, Pepper} different from {Pepper, Tomato}? Usually yes. A pizza has an order of toppings (top vs side). In the absence of context implying "order matters" (which is rare in simple math problems unless specified as permutations), it's safer to assume combinations ($\binom{n}{k}$) if order doesn't matter for the selection.  
    *   However, in many contexts (like selecting a set of toppings from a plate to serve someone), order does NOT matter. You just want "a plate with X and Y".  
    *   I will proceed with $\binom{8}{2} = 28$.  

    *   Wait, what if the phrasing "different toppings" implies that we should select items such that they are distinct? Since they are from a set of 8 different items, any pair is distinct.  
    *   Let's consider if there's an ambiguity regarding "different pizzas". If Mikka has a set of toppings $\{1..8\}$ and wants to form pizzas with 2 of them. The answer is always combinations.  

    *   Is it possible the question implies "Pizza with two toppings" (i.e. 2 toppings) from *any* pair? No, "two different toppings".  
    *   If he has 8 toppings, and asks for pizzas with 2 different toppings. He needs to choose 2 distinct items from his collection.  
    *   Result: 28.  

    *   Let me re-read the question very carefully to ensure I haven't missed a word about order.  
    *   "Mikka wants to order a pizza with two different toppings. He has 8 different toppings to choose from."  
    *   There is no word "order".  
    *   So, combinations is correct.  

    *   Step-by-step:  
    *   We are selecting 2 items from a set of 8 distinct items.  
    *   Number of ways = $\binom{8}{2}$.  
    *   $\binom{8}{2} = \frac{8 \times 7}{2 \times 1} = 4 \times 7 = 28$.  

    *   Alternative: Permutations $P(8, 2) = 56$.  
    *   Why would it be permutations? If I order the pizza. A "Pizza with toppings T1 and T2" is usually described as a set of items. If the problem was "Order the toppings", then permutations. But here it's just "order a pizza". This phrasing is standard for choosing subsets (combination) unless specified otherwise.  
    *   Wait, in some contexts like combinatorial design, if order matters, it might be $n^2$ or something. No.  
    *   Let's stick to $\binom{n}{k}$.  

    *   Wait, looking at similar questions online (e.g. "How many different pizzas can be made from 8 toppings?"):  
    *   Often, the context is just selecting a subset of size $k$ from $n$ distinct items. The number of combinations $\binom{8}{2}$ applies here.  

    *   Let's check if there's any tricky interpretation about "different toppings" meaning specific types (like different varieties).  
    *   If toppings are just labels like 1, 2, ..., 8 (distinct), then subsets are distinct.  
    *   If toppings were not distinct (e.g. 8 different toppings but with only 2 possible types, and he wants to order pizzas from the set of those 2 types?), it would be $P(n, k)$. But here "He has 8 different toppings" implies there are 8 available items.  
    *   So $\binom{8}{2}$ seems the robust answer.  

    *   Let's double check the prompt's source style or intent. This looks like a standard high school math problem.  
    *   The phrase "different pizzas" is slightly ambiguous, but "with two different toppings" clarifies the items. Since all items are different, the only way they differ is if I have {A, B} vs {B, A}. If it were permutations, it would likely ask for orders of selection.  
    *   However, if I look at a specific source: "How many different pizzas could he order?" with 8 toppings.  
    *   The answer is $\binom{8}{2}$.  
    *   Why? Because you have to choose the set of two toppings.  
    *   Example: Pick 2 apples from 10. $\binom{10}{2} = 45$ pizzas (combinations).  
    *   If order mattered, it would be $\binom{8+1}{2}$ or something? No, usually we don't mix apples and oranges unless specified.  
    *   Wait, I recall a similar problem from a textbook where "How many different ways can you arrange 5 toppings on the pizza?" -> $P(n,r)$ (Permutation). But that's usually if the toppings are just placed in a line or sequence. Since this is a plate, order matters for the visual appearance (Tomato on top vs Pepper on top).  
    *   BUT: "He has 8 different toppings to choose from." This implies the list of toppings available.  
    *   If he picks "tomatoes" and "peppers", does it matter which is on top or bottom?  
    *   Let's assume order doesn't matter (just a set). The resulting pizza is {Tomato, Pepper}. If the other side has Cheese, then it's {Cheese, Tomato} vs {Pepper, Cheese} - no.  
    *   Actually, usually "order of toppings" on a plate matters for flavor and taste, but physically, if you just order the plates with tomatoes and peppers, you can have the plate containing (Tomato, Pepper) or (Pepper, Tomato).  
    *   Let's check standard interpretation.  
    *   If I say "How many pizzas can he order?" It means how many valid combinations of toppings exist.  
    *   I will provide the combination answer 28.  

    *   Wait, let me look at the phrasing again: "He has 8 different toppings to choose from."  
    *   Is it possible that Mikka wants to order a pizza where there are exactly *two* distinct toppings? Yes.  
    *   Does he have any constraint on *how* they are placed (e.g., on a specific side)? No.  
    *   So, just the subset selection is the core of the problem.  

    *   Wait, I should consider if "different toppings" means that the toppings themselves are different from each other. Since there are 8 distinct items in the set, picking 2 distinct items yields unique subsets. The count is $\binom{8}{2}$.  
    *   Let's confirm with an example:  
    *   Set: {Apple, Orange, Banana, Cherry}. Pick any 2.  
    *   Combinations: (A,B), (A,C)...  
    *   If order mattered: ABC is different from BAC. But usually pizza toppings are listed as "topped with [tomato], and topped with [pepper]" vs "topped with [pepper], and topped with [tomato]". Wait, that's not a common phrasing for a single plate.  
    *   Usually, we refer to the set of ingredients on the pizza. If I order a pizza with 2 ingredients, it is usually just one item (the set).  

    *   Final Answer: 28.  


## Answer

To determine the number of different pizzas Mikka can order, we need to interpret the problem as a combination problem.  

**1. Understanding the Problem:**  
*   **Total available items:** The problem states that Mikka has **8 different toppings**. Let's call this set $S = \{t_1, t_2, ..., t_8\}$. Since there are 8 distinct toppings, each has a unique identity from the set.  
*   **Goal:** Mikka wants to order a pizza with **two different toppings**. He needs to select two toppings from his collection of 8 to place on the pizza plate.  
*   **Question:** How many *different* pizzas can he order?  

**2. Mathematical Modeling:**  
The problem asks for the number of ways to choose 2 items (toppings) from a set of 8 distinct items.  
*   Since all 8 toppings are distinct and distinct in identity, choosing one topping makes it unique from other possible toppings.  
*   However, the phrase "different toppings" usually refers to the *set of toppings on the pizza*. If we have tomatoes and peppers, that is one specific pizza type (tomato-pepper). If we have peppers and tomato, that is the same pizza type in terms of composition.  
    *   Wait, let's reconsider the wording carefully. Does "order matters" apply to the *selection* or just the selection *of the set*?  
    *   In standard combinatorial problems involving selecting toppings for a pizza (or similar), unless the order of toppings on the plate is explicitly mentioned as important for identification (e.g., "which side has what"), we assume **combinations**. We select a subset of 2 toppings. For example, if Mikka chooses $\{A, B\}$, he forms one pizza. If he chooses $\{B, A\}$, it's still the same set of ingredients, so it's the same pizza (or the plate is just the same).  
    *   However, often in these types of logic puzzles, we treat the "topping" as an item from a pool. The question effectively asks for the number of combinations $\binom{n}{k}$.  

**3. Calculation:**  
*   We need to select $k = 2$ toppings from a total of $n = 8$.  
*   Formula: $ \binom{n}{k} = \frac{n!}{k!(n-k)!} $  
*   Substituting the values:  
$$ \binom{8}{2} = \frac{8!}{2!(8-2)!} = \frac{8!}{2!6!} $$  
$$ \binom{8}{2} = \frac{8 \times 7}{2 \times 1} $$  
*   Calculation:  
$$ 4 \times 7 = 28 $$  

So, the number of distinct combinations of two toppings he can pick is **28**.  

**Note:** Even if we consider order (i.e., Top and Bottom), since there are no constraints on which topping is "top" or "bottom" (it's just a set of items to put on a plate), it doesn't change the number of unique combinations. The question asks for the count of pizzas (combinations).  

Therefore, there are **28** possible ways Mikka can order this pizza.  

\boxed{28}  
