# test/counting_and_probability/389.json (Counting & Probability, level 2)

> Mikka wants to order a pizza with two different toppings. He has 8 different toppings to choose from. How many different pizzas could he order?  

**Correct.** Gold `28`, predicted `28`. Finish: stop, 7740 tokens, 4 waits, 665.1 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's a thinking process that leads to the solution:  

1.  **Analyze the Request:**  
    *   **Goal:** Calculate the number of different pizzas Mikka can order.  
    *   **Condition 1:** The pizza has two distinct toppings. (Note: This usually implies *order matters*, or it might imply we select specific toppings and arrange them to form a set? Or does "order" here just mean the combination, not permutation? Let's re-read carefully).  
    *   **Condition 2:** He needs to choose from 8 different toppings.  
    *   **Constraint:** "Two different toppings." This phrasing is slightly ambiguous. Does it mean the pizza has exactly two toppings? Yes, that's the most straightforward interpretation. Or does it mean he picks a subset of two distinct toppings? Let's look at standard logic puzzle interpretations. Usually, "Two different toppings" means 2 specific items are selected from 8 available options. The remaining toppings don't matter (unless they're just placeholders for other things). However, the phrase "How many *different* pizzas" suggests uniqueness based on the composition of the pizza.  
    *   **Interpretation:** Mikka chooses two toppings out of 8 to put on his pizza.  
    *   **Calculation:** Combinations ($C(8, 2)$) or Permutations if the specific arrangement matters (e.g., pepperoni mushroom vs. mushroom pepperoni). However, "order" isn't mentioned in "two different toppings". Let's look at the phrasing again: "How many different pizzas could he order?" A pizza is defined by the set of ingredients on it. The order of toppings usually implies an ordered list (like a menu item), but if toppings are distinct types, usually, the set is sufficient to define the pizza unless it specifies "how to arrange toppings".  
    *   **Standard Math Problem Interpretation:** If we are choosing from 8 items and selecting exactly 2 items. The order in which we place them on the pizza does not matter (it's a selection).  
        *   Case A: Select 2 toppings.  
            *   Formula: $\binom{n}{k}$. Here $n=8, k=2$.  
    *   **Alternative Interpretation:** Does "order" imply he orders them in the order they come on the pizza? That would make it permutations ($P(n, k)$), but the question is just asking for the *set* of pizzas. Usually, these questions are about combinations.  
    *   **Context Clues:** Mikka wants to order *two different toppings*. He has 8 options. The number of *distinct sets* of two toppings he can choose is the standard interpretation.  

2.  **Formulate the Math Problem:**  
    *   Total items (options): $N = 8$.  
    *   Items to be chosen: $K = 2$ distinct toppings.  
    *   This is a combination problem.  

3.  **Perform the Calculation:**  
    *   Use Combination Formula: $C(n, k) = \frac{n!}{k!(n-k)!}$.  
    *   Substitute values: $C(8, 2) = \frac{8!}{2!(8-2)!}$.  
    *   Expand factorials: $C(8, 2) = \frac{8!}{2!6!}$.  
    *   Cancel terms: $C(8, 2) = \frac{8 \times 7}{2 \times 1}$.  
    *   Calculate:  
        *   Numerator: $56$  
        *   Denominator: $2$  
        *   Result: $28$.  

4.  **Double Check with Alternative Interpretations:**  
    *   *What if the toppings are indistinguishable?* (e.g., a pizza with "Pepperoni" and "Mushroom", and we just want a specific set). Since he has "two different toppings", it likely refers to two distinct *types* of toppings.  
    *   *What if order matters?* (e.g., he puts Pepperoni on the top, then Mushroom on bottom. He wants to know how many unique pizzas *he can* order, implying the order is variable? Or does he pick a specific combination and arrange it?) "How many different pizzas could he order" implies the set of toppings is fixed. However, if the pizza has two *specific* toppings (like a pepperoni + mushroom), then order matters because which one is on top vs. bottom might be determined by flavor preference or location?  
    *   Let's look at similar problems. "How many ways to arrange 2 items from 8 distinct choices?" Usually, this implies permutations ($P(8,2)$) if positions are fixed (top, bottom). However, since the question asks for "different pizzas", and typically pizza toppings are considered a set of ingredients, we usually stick to combinations ($C(8, 2)$).  
    *   *Let's check the wording "Two different toppings".* It doesn't say "in any specific order". If it meant permutations, it would likely ask "In how many ways can he arrange the two toppings...". But it says "How many different pizzas...". A pizza has a set of toppings. Usually, if order matters, we list them as (A, B), which is distinct from (B, A). However, if the problem is standard, usually "pizzas" implies sets. Let's look at the phrasing "two *different* toppings". This sounds like $T1$ and $T2$.  
    *   Let's re-read: "He has 8 different toppings to choose from. How many different pizzas could he order?"  
    *   Common interpretation in combinatorics (e.g., math competitions): Choosing a subset of size $k$ from $n$ is a combination ($C(n,k)$). If the question is "What is the probability that a specific ordering happens?", it's different. But here, it asks for the number of possible pizzas.  
    *   Usually, if a person makes a selection for a pizza, the order in which they add them to the stack doesn't define the unique pizza unless distinct types are specified. For example, a pepperoni pizza is different from a pepperoni pizza with cheese. If we select "pepperoni" and "mushroom", that's one specific combination. The toppings don't necessarily need to be placed in an ordered sequence to constitute the pizza.  
    *   Therefore, I will proceed with Combination logic ($C(8, 2)$).  

    *   *Self-Correction/Refinement:* If the question were "How many ways could he order them if he puts pepperoni and mushroom on it?", that's permutations ($P(8,2) = 56$). But standard English usage for "pizza" refers to the composition (a set of ingredients), not the sequence.  
    *   However, there is a catch: Mikka has a budget or time constraint? No constraint mentioned. Just "order a pizza".  

    Let's assume the most standard interpretation:  
    - Selecting 2 toppings from 8 distinct items.  
    - Calculation: $C(8, 2)$.  

    Let's calculate again just to be sure.  
    $\binom{8}{2} = \frac{8 \times 7}{2 \times 1} = 28$.  

    Is there any ambiguity about "different toppings"?  
    If he has a box of toppings: {Toppings A, B, C...}. He chooses 2. The order of choosing doesn't matter. (He picks {A, C}).  

    What if the question is interpreted as permutations? If Mikka puts Pepperoni on top, Mushroom on bottom... that's just a sequence of 2 items from an 8-item list. But usually, "pizza" implies the composition.  
    Let's check for similar problems online or in textbooks. "How many pizzas with two different toppings?" Usually refers to combinations ($C(8, 2)$).  
    However, some sources might interpret it as permutations ($P(8, 2)$) if they view it as a menu order. But since the question asks for the number of *different* pizzas, we are counting distinct sets of ingredients.  

    Let's write down the steps for Combination.  
    1. Total options = 8.  
    2. Toppings to select = 2 (two different types).  
    3. Formula: $\frac{8 \times 7}{2 \times 1}$.  
    4. Result: 28.  

    Let's check if the phrase "Two different toppings" implies that the toppings are distinguishable. They are distinguished by their names or just because there is one of each. If he has a pizza with Pepperoni and Mushroom, does swapping them count? No, usually the set {Pepperoni, Mushroom} vs {Mushroom, Pepperoni}.  
    However, if we look at permutations ($8 \times 7$), the order matters. But "different pizzas" implies uniqueness. If I buy a pizza with cheese and pepperoni (order irrelevant) and a pepperoni cheese pizza, those are usually considered same unless there's flavor difference? No, standard interpretation: The set of toppings determines the identity of the pizza.  

    Final check on logic:  
    - "How many different pizzas could he order?" -> Total number of unique combinations.  
    - We have 8 options.  
    - We need to pick 2.  
    - Calculation: $C(8,2) = 28$.  

    Let's double-check if "different toppings" implies something else. Maybe it means "two types of toppings"? Or maybe the order doesn't matter?  
    If he puts them in an array (Top, Bottom), that is a sequence. But since the question says "order a pizza", and asks for pizzas (singular). Usually, "how many ways to choose toppings" refers to combinations.  

    Let's assume the standard combinatorial choice problem context (e.g., "How many ways can you pick 2 items from 8...").  

    Step-by-step reasoning:  
    1. Mikka wants to select a set of two distinct toppings from his pool of 8 options.  
    2. Since the order of selection doesn't change the pizza's unique identity (a pizza with topping 'A' and topping 'B' is the same as a pizza with topping 'B' and topping 'A'), we treat this as a combination problem. We need to choose which 2 toppings are included.  
    3. The calculation uses the combination formula $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.  
    4. Here $n=8$ and $k=2$.  
    5. $\binom{8}{2} = \frac{8 \times 7}{2 \times 1} = 28$.  

    Is there any reason to consider Permutations? If he places the toppings on a specific plate with a fixed order (e.g. A, B), then yes. But usually "how many pizzas" counts distinct compositions, not arrangements.  
    However, sometimes in these riddles, if it's just about toppings, and no distinction is made between the choice of which one is added first, the set approach applies. If he asks how many ways to arrange 2 items, that would be $P(8,2)$. But the question is "How many *different* pizzas".  
    Let's consider if the prompt implies a specific permutation logic. If I pick toppings T1 and T2, and order them (T1 on top, T2 on bottom), it might be considered 2 different pizzas from 8 options? No, usually distinct pizzas are defined by their set of ingredients.  
    However, looking at the wording "order a pizza with two different toppings", the question is slightly ungrammatical if referring to order. It says "order a pizza [with] two different toppings".  
    Let's assume it means: "How many unique sets of toppings can be formed?" (28) or "How many ways to arrange them?" (56).  
    Usually, standard math problem phrasing for this type ("how many distinct pizzas") implies combinations ($C$), as the order is not specified in "how to choose", but "which ones" is implied.  

    Let's re-read carefully: "He has 8 different toppings... How many different pizzas could he order?"  
    If I pick T1 and T2, I have a pizza. This pizza has 2 distinct toppings. The set {T1, T2} generates the pizza.  
    If I picked T2, T1? Same pizza? Or is there any difference in flavor if they are arranged? Usually, yes or no depending on context, but mathematically "set of ingredients" is the pizza definition.  

    Let's check for similar questions with 8 items and 2 items.  
    Question: "How many different pizzas could he order?" (Usually refers to combinations).  
    Answer: $\binom{8}{2} = 28$.  

    However, consider a nuance: If the question meant permutations ($P(8,2)$), it would usually specify the order matters or ask about arrangement. Without that, we assume set selection.  

    Let's verify the phrase "two different toppings".  
    Does it mean the toppings are distinguishable (e.g. cheese, pepperoni) or are they distinct *types*? It just means 2 items. Since the list is distinct ($8$), and we need to choose $k=2$, we calculate combinations.  

    Final check: Is there any scenario where order matters?  
    "He orders a pizza with two toppings."  
    If he wants to order a pizza, the order in which he picks them might not matter (set). But if the prompt meant "How many distinct sets of 2 toppings are there?", that's C(8,2).  
    If the prompt meant "In how many ways can he order the topping sequence...", that's P(8,2) = 56.  
    However, let's look at the provided solution in a standard format or context. The phrasing is typical for "Combinations".  

    Let's assume the intended meaning is **Combination**.  
    Why? Because "order" in the question might be referring to the selection process (what toppings he has), but the output is "number of pizzas". If the order mattered, it would be a permutation.  
    Let's provide the calculation for combinations ($28$) as it is the most standard interpretation for selecting items from a set for a set size.  

    *Self-Correction:* Wait, if I select pepperoni and mushroom, and swap them? No, swapping toppings in this context (combinations) usually results in the same pizza. But if he puts them on a table (Top/Bottom), does order matter?  
    If I have to choose 2 different toppings from 8, how many *distinct* pizzas do I get?  
    I get a set of ingredients. The ingredients define the pizza.  
    So, it's combinations.  

    Let's consider an edge case: "He has 8 different toppings to choose from." (Total $N=8$).  
    He selects exactly two.  
    Number of ways to pick = $\binom{8}{2}$.  
    Calculation: $28$.  

    Is it possible the question is asking about Permutations?  
    "How many different pizzas" vs "How many ways".  
    If I have 5 options for toppings, and I want to make a pizza. Usually, if there's an order, it implies a sequence or position.  
    Let's stick to combinations as primary.  

    Let's try to reason why permutations might be intended. If the prompt was "How many ways can he arrange two toppings on his plate?" that would be 56. But it asks "How many different pizzas". A pizza is usually defined by its ingredients. So, {Pepperoni, Mushroom}. It's distinct from {Mushroom, Pepperoni}. Both result in the same pizza if you just look at what's on it.  
    However, in some riddles, they use "how many ways" for combinations and "order matters". But here, it's a simple "How many pizzas".  
    I will stick with 28.  

    Let's re-read again: "He has 8 different toppings to choose from."  
    Maybe it implies that the toppings are *available* in an infinite supply? Or is it limited to 8 options? Yes.  
    If he needs to order "two different toppings", this means picking two distinct items.  

    Let's verify with a small number to ensure no confusion.  
    Total toppings = 3.  
    He wants pizza with 2 toppings.  
    Combinations: $\binom{3}{2} = 3$. ({1,2}, {1,3}, {2,3}).  
    Permutations (Order): $3 \times 2 = 6$ (e.g., Top/Bottom).  

    Usually, in these types of logic puzzles (often generated by AI or similar contexts), if "two different toppings" is the key phrase, it often implies distinctness.  
    Let's assume combinations ($C(8,2)$) because a pizza is not ordered unless specified otherwise, and "how many different pizzas" asks for the set of ingredients.  
    Answer 28.  

    However, if the question is interpreted as "He chooses two toppings, putting them in order on his plate", it might be permutations ($56$). Let's think about how a person would say "I want to order a pizza with two toppings". Usually, they mean "What do I get?" or "Can I get two different things?".  
    But let's look at the phrasing "How many different pizzas could he order?".  
    If I say "I have 2 apples and 3 oranges", and I want to make a pizza.  
    Usually, the order of selection doesn't matter for uniqueness (you pick Apples and Oranges).  
    Therefore, Combinations.  

    Let's calculate $P(8,2)$ just in case:  
    $\frac{8!}{1!7!} = 56$.  
    But if I say "How many pizzas with a specific arrangement", that's permutations.  
    The phrasing is "How many *different* pizzas". Usually "different" means distinct compositions.  
    Thus, combinations.  

    Let's write the response based on combinations.  

    **Step 1:** Identify total number of choices for toppings ($n$). $n = 8$.  
    **Step 2:** Identify number of toppings to select ($k$). The pizza needs "two different toppings". We assume we choose exactly 2 toppings, and they need to be *different* (which is standard if there's only one type of topping mentioned, but here we just have 8 available options for specific toppings).  
    **Step 3:** Identify if order matters. The question asks for the number of different pizzas. Since a pizza consists of two distinct ingredients, and we don't specify an order (like "pepperoni on top"), picking one set {A, B} is the same as picking {B, A}.  
    **Step 4:** Calculate using Combinations formula $\binom{n}{k}$ where $n$ is total items and $k$ is items to choose.  
    Formula: $\binom{8}{2} = \frac{8!}{2!(8-2)!} = \frac{8 \times 7}{2 \times 1} = 28$.  

    *Alternative thought:* If the question was from a specific context like "order matters" (like filling a basket with distinct items), sometimes permutations are used. But given "How many different pizzas", it's ambiguous.  
    Let's search my internal knowledge base for similar riddles.  
    Often, this phrasing is used in simple probability/geometry problems where the order of ingredients on the pizza doesn't matter because we just look at the *set*. Or sometimes, if the toppings are distinct, does swapping them count? If I pick a pepperoni pizza and then swap it with a cheese pizza, those are different pizzas.  
    But "How many different pizzas" means how many unique sets of ingredients.  
    So $C(8, 2)$.  

    Final check on the prompt: "Mikka wants to order a pizza with two different toppings."  
    Does this imply that the topping *types* must be different (e.g., not both cheese and pepperoni)? Or does it simply mean he is adding two distinct items?  
    Since there are 8 available, it implies we pick 2 from 8.  
    Since "order" isn't specified in the order of toppings on the pizza (usually), but "order" might refer to "order of toppings"?  
    Let's assume "two different toppings" is a subset constraint (2 distinct items).  
    The answer 28 seems robust for this interpretation.  

    However, there is another interpretation: Maybe he chooses 2 *distinct* toppings from the pool of *all* toppings? Yes, that's what "choose from" implies.  
    Is it possible "two different toppings" means the pizza must have exactly 2 distinct toppings? Yes.  
    If he picked 3 toppings, say {A, B, C}, that might be one pizza (e.g. a triple topping). But the question says "pizza with *two* different toppings". It does not explicitly say "single layer" or specific count. It implies the set has size 2.  
    So it is definitely $\binom{8}{2}$.  

    One more check: Could the phrase "order a pizza with two different toppings" imply that he orders them in sequence (like order of ingredients)?  
    Usually, if you order ingredients, you list them.  
    If I say "I order 2 distinct toppings", it is ambiguous. But usually, the answer for "how many pizzas" assumes the set composition only.  

    I will provide the solution based on combinations ($C(8,2)$).  

    **Calculation:**  
    $n=8$  
    $k=2$  
    $\binom{8}{2} = \frac{8 \cdot 7}{2} = 28$.  

    Final Answer: 28.  

    *Self-Correction/Double Check:* Is it possible the question implies he is choosing an ordered list (e.g. $p_1, p_2$)?  
    If the question was "How many ways can Mikka arrange two toppings?", that would be 56.  
    Since it asks for "different pizzas", and a pizza with ingredients $(t_1, t_2)$ and $(t_2, t_1)$ might be different in context of ordering (like top vs bottom), but usually distinct sets matter. Let's think if there is any standard riddle where the answer is 56.  
    In combinatorics questions like "Number of ways to arrange 4 letters", that matters. For "pizza with 2 toppings", since it's just a selection, it's combinations. If I say "I have 2 apples and want to buy pizza with them, order doesn't matter", then the answer is $\binom{8}{2}$.  
    I will stick to 28.  

    One edge case: The phrase "order" in the question "He wants to order a pizza with two different toppings" might be a bit of a distraction from the standard "choose two items".  
    Actually, re-reading carefully: "Mikka wants to order a pizza with two different toppings." It implies he is selecting 2 toppings.  
    He chooses 2. They must be different? Yes.  
    Since there are no flavors or specific attributes listed in other contexts that might make them indistinguishable (like just "pepperoni" and "pepperoni"), and we have distinct items, they are distinguishable.  
    If I say "He has 2 distinct apples to choose from", does order matter? No, he wants *a* pizza with two different apples. That means the set {A, B} is what matters.  
    So 28.  

    Let's write out the response.  
    1. Identify total toppings available: $n = 8$.  
    2. Identify toppings needed: $k = 2$.  
    3. Determine if order matters: No, "order a pizza" usually implies selection from a set of ingredients, where the specific arrangement doesn't create a new unique product unless it specifies position on top/bottom or flavor difference (which are usually ignored). However, usually for "How many ways to select", we use combinations.  
    4. Calculate combinations: $\binom{8}{2} = \frac{8 \times 7}{2 \times 1} = 28$.  

    If I had to assume permutations ($P(8,2)$), the logic would be "He has a specific arrangement of 2 toppings".  
    Let's check if there's any context implying distinct *order* (Top/Bottom) matters. If it meant Top/Bottom matters, it would likely say "How many ways can he put toppings on his pizza?" or "Arrange toppings in an order". The question asks for pizzas. A pizza with ingredients T1 and T2 is just T1 and T2.  
    Therefore, 28.  

    Let's verify if there is any other interpretation.  
    Could "two different toppings" mean the *set* must have exactly two distinct elements? Yes.  
    Does it imply that there are no others? No, he has 8.  
    Does it imply the order of picking matters? No.  
    So, standard combination logic applies.  

    Wait, could it be a question about "How many different pizzas (sets of toppings) can Mikka make?"  
    If so, $\binom{8}{2}$.  
    If he picks {A, B} -> Pizza 1.  
    If he picks {B, A} -> Pizza 2. (If the topping "A" is the same as "B"? No, distinct options.)  
    So yes, unique set composition determines the pizza.  
    Thus, combinations.  

    Final check: "He has 8 different toppings to choose from."  
    This sounds like a standard math problem asking for combinations of $n$ items chosen with replacement or just without? It says "choose from" (without replacement implied if there are only 8 types and we pick from them).  
    If he wants to order a pizza *with* two toppings, and the question is simple, it's usually $\binom{n}{k}$.  

    Let's try to interpret "Two different toppings" as a specific constraint. Like "The toppings must be distinct". Since he has 8, if all 8 were distinct, we pick any subset of size 2.  
    If the question was "How many pizzas could he order with at least 3 toppings?", that would be $1 + \dots$? No.  

    Let's assume the simplest path: Combinations.  
    Answer: 28.  

    *One small possibility:* Maybe the question implies ordering matters (top/bottom) because sometimes "order a pizza" is used to denote sequence. If so, answer is 56. But I will provide the combination logic as it's safer for "different pizzas".  
    Let's look at the phrasing again: "He has 8 different toppings to choose from. How many different pizzas could he order?"  
    "Different pizzas" -> Combinations (sets).  
    Why? Because if I pick pepperoni, then cheese (top) and mushroom (bottom), that's a specific sequence. But if the question asks for pizzas, usually that means the set of toppings.  

    Actually, let's reconsider standard logic questions found in similar contexts (like "Mathcounts" or general math competitions).  
    Problem: "There are 5 distinct items on a table. How many ways can you pick 3?" -> Combinations ($\binom{5}{3}$).  
    Here, "How many different pizzas" asks for the number of unique sets of toppings.  
    So $\binom{8}{2}$.  

    Let's proceed with this logic.  
    $n=8$, choose 2.  
    Answer 28.  

    (If I were to consider permutations, I would need more justification or if the phrase "order" refers to placing them in slots on a plate. But "Pizza" as a whole object is best defined by its ingredients. The order of ingredients within a set doesn't change the pizza unless specified. Since no position is mentioned, order doesn't matter.)  

    Let's write down the solution clearly.  
    1. Identify total number of choices for toppings $N=8$.  
    2. Identify number of toppings needed to be chosen: $k=2$.  
    3. We need to calculate the number of ways to choose exactly 2 toppings from 8 distinct options. This is a combination problem.  
    4. Formula: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.  
    5. Calculation: $\binom{8}{2} = \frac{8 \times 7}{2 \times 1} = 28$.  

    Final check: Does "different toppings" mean he has *only* 2 distinct types of toppings? Yes, "two different toppings".  
    Does "order a pizza with two different toppings" imply that the order of picking them matters? Usually no. It's a selection problem.  

    One subtle interpretation: Mikka wants to order a pizza with *exactly* two different toppings. He has 8 different toppings. How many ways can he choose exactly two distinct items from 8?  
    If all 8 are distinct (which they are), then it is simply $\binom{8}{2}$.  
    However, if the question was "How many pizzas *with* a specific set of ingredients?", then it's just combinations.  

    I will provide the answer as 28.  

    *Final check:* What if "different toppings" means "distinct items" (e.g. A and B are different from C and D)? Yes, that's standard.  
    If he has to pick a pizza *with two toppings*, it implies picking 2.  
    If the question meant "How many ways to arrange toppings", it would usually be phrased as such.  
    Since "order" is in the prompt but not used in the description, and "different pizzas" implies sets, we go with combinations.  

    *Correction:* Re-reading "He has 8 different toppings to choose from."  
    This sounds like a selection problem.  
    If he picks {A}, it's 1 pizza? No, that's not how it works. He needs to order a pizza. A pizza is made of 2 ingredients.  
    So he chooses 2. The order doesn't matter for the "pizza".  
    Therefore, $\binom{8}{2}$.  

    One final thought: Is there any interpretation where "different toppings" implies they must be different *types* (e.g. not just two of one type)? That's consistent with "two different" (implied distinct types). Since we have 8 distinct options, he can pick any subset of size 2.  

    Answer seems to be 28.  
    However, let me double check if there is a standard problem like this that asks for permutations ($P(8,2)$).  
    Often in these "pizzas" or "menus", if an item is specified (e.g., "Pepperoni and Cheese"), order matters on the menu. But if it's just "how many ways to choose toppings", combinations.  
    Usually, questions about pizzas ask for sets of ingredients (combinations).  

    Let's assume the question meant permutations. If I have 8 items, and I want to arrange them into a sequence. The number of arrangements is $P(8,2) = 8 \times 7 = 56$.  
    Why might this be? "Mikka wants to order a pizza with two different toppings."  
    If he just wants the final product (the pizza), it doesn't specify position.  
    But if the question is interpreted as "How many ways can he choose a set of toppings?" -> 28.  
    Usually, in combinatorics, picking distinct items from a collection (without regard to sequence) is combinations. Arranging them in a sequence (ordering) is permutations.  
    "Pizza with two toppings" implies the set.  
    I will provide 28.  

    *Alternative View:* Maybe he wants to order a pizza with *two different* toppings (meaning distinct from each other and maybe not just any toppings?). If there are $n$ options, he selects 2.  
    Let's look for similar wording in my database of problems.  
    "How many ways to choose two items from 5?" -> 10.  
    "How many pizzas with pepperoni and cheese?" -> Usually sets.  

    Given the phrasing "He has 8 different toppings", it sounds like a simple combination problem. I'll stick with 28.  
    Also, usually these riddles don't ask for permutations unless "order" or "arrangement" is explicitly mentioned as relevant to the final count (e.g., "How many orders can he make?", implies specific order). "How many different pizzas could he order?" asks for distinct pizza identities (combinations).  

    Final decision: 28.  
    The calculation $\frac{8 \times 7}{2} = 28$.  


## Answer

To find the number of different pizzas Mikka can order, we need to determine how many unique sets of toppings he can select from his pool of 8 options.  

1.  **Identify the available options:** Mikka has 8 different toppings in total.  
2.  **Identify the requirement:** He wants to choose exactly two different toppings. This is a standard combination problem where we need to select a subset of 2 items from a larger set of 8 distinct items. The question asks for the number of *different* pizzas, which implies that the identity of the pizza is determined by the combination of its ingredients (a specific set of 2 toppings).  
3.  **Determine the type of problem:** Since the order in which he selects or adds them to his plate doesn't define a new unique pizza (unless we are discussing permutations), we calculate the number of combinations ($\binom{n}{k}$). Here, $n = 8$ and $k = 2$.  
4.  **Calculate the combinations:**  
    The formula for combinations is:  
    $$C(n, k) = \frac{n!}{k!(n-k)!}$$  

    Substituting the values into the formula:  
    $$C(8, 2) = \frac{8!}{2!(8-2)!} = \frac{8!}{2!6!}$$  

    We can cancel out $(8!)$ from the numerator and $(8-2)!$ in the denominator:  
    $$C(8, 2) = \frac{8 \times 7}{2 \times 1}$$  

    Now, perform the arithmetic:  
    $$C(8, 2) = \frac{56}{2} = 28$$  

Therefore, there are 28 different ways to choose 2 toppings from 8 available options. If order mattered in the sense of a specific arrangement (top/bottom), it would be $P(8, 2) = 56$, but given the context of ordering a set-based pizza, combinations is the standard interpretation.  

\boxed{28}  
