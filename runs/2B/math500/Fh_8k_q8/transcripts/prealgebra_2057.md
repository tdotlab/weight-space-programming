# test/prealgebra/2057.json (Prealgebra, level 4)

> Yann and Camille go to a restaurant.  If there are 10 items on the menu, and each orders one dish, how many different combinations of meals can Yann and Camille order if they refuse to order the same dish? (It does matter who orders what---Yann ordering chicken and Camille ordering fish is different from Yann ordering fish and Camille ordering chicken.)  

**Correct.** Gold `90`, predicted `90`. Finish: stop, 7616 tokens, 27 waits, 1022.4 s.

*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*

## Thinking

Here's a thinking process that leads to the solution:  

1.  **Analyze the Problem:**  
    *   **Scenario:** Two people (Yann and Camille) are choosing from a restaurant menu.  
    *   **Menu Size ($n$):** There are 10 items on the menu.  
    *   **Number of Choices per Person:** Yann chooses one dish, Camille chooses one dish. This implies $2^N = 2^{10}$ if there were no restrictions, or more accurately $10 \times 10$. The order matters (Yann first, then Camille).  
    *   **Constraint:** Yann and Camille refuse to order the same dish. They want a "different combination" based on who orders what.  
    *   **Specific wording check:** "It does matter who orders what---Yann ordering chicken and Camille ordering fish is different from Yann ordering fish and Camille ordering chicken." This implies permutations are relevant.  

2.  **Break Down the Logic:**  

    *   **Total Combinations without restriction:**  
        *   Yann can choose any of the 10 items (10 options).  
        *   Camille can choose any of the 10 items (10 options).  
        *   Total ways = $10 \times 10 = 100$.  

    *   **Apply the Restriction (No one orders the same dish):**  
        *   Since Yann chooses first and Camille is distinct from him, we need to count the number of pairs where $X \neq Y$, where $X$ and $Y$ are chosen from $\{1, 2, ..., 10\}$.  

    *   **Calculation Method 1: Subtraction**  
        *   Total possibilities = 100 (as established above).  
        *   Unwanted cases: Both choose the same dish.  
            *   Dish A can be chosen by Yann AND Camille together.  
            *   How many dishes are there? 10.  
            *   Number of same-dish pairs = $10 \times 1$ (where Camille follows Yann) or just count directly: Yann picks X, Camille picks X. There are 10 such scenarios.  
        *   Wishes to compute: Total - Unwanted = Combinations without restriction - Cases where dishes match = $100 - 10$.  
        *   Result: $90$.  

    *   **Calculation Method 2: Direct Counting**  
        *   Think of the order in which choices are made. Yann picks one, Camille picks one.  
        *   Let's say Yann picks Dish A (which is a specific dish). There are 10 options for Yann.  
        *   For each choice of Yann's dish, how many choices does Camille have to avoid that dish?  
            *   If Camille refuses the same dish, she has $10 - 1 = 9$ choices available.  
        *   Total combinations = (Choices for Yann) $\times$ (Choices for Camille).  
        *   Total combinations = $10 \times 9$.  
        *   Result: $90$.  

3.  **Sanity Check the Question Details:**  
    *   "Yann and Camille go to a restaurant" - Standard setup.  
    *   "If there are 10 items on the menu" - Set size = 10.  
    *   "each orders one dish" - Discrete choice.  
    *   "how many different combinations of meals can Yann and Camille order if they refuse to order the same dish?"  
    *   "It does matter who orders what..." - Explicit confirmation that $(Y=A, C=B)$ is distinct from $(Y=B, C=A)$.  

4.  **Wait, let me double check the wording carefully.**  
    *   Sometimes "combinations" in combinatorics means sets (order doesn't matter), but here it specifically clarifies with the example: "Yann ordering chicken and Camille ordering fish is different from Yann ordering fish and Camille ordering chicken." This clearly treats $(A, B)$ as distinct from $(B, A)$.  
    *   Wait, let's look at the wording again. "Refuse to order the same dish". Does this imply Yann cannot choose the *same* dish Camille chose? No, it usually implies $Yann(Dish) \neq Camille(Dish)$.  
    *   Let's re-read carefully: "combinations of meals can Yann and Camille order if they refuse to order the same dish".  
    *   Usually, this means: We form a meal for Yann ($M_Y$) and a meal for Camille ($M_C$).  
    *   Condition: $M_Y \neq M_C$. (Assuming "order the same dish" refers to the specific item on the menu being identical).  
    *   Let's verify with small numbers.  
        *   Menu: Apple, Banana, Cherry (3 items).  
        *   Yann wants to order a pair $(A, B) \neq (C, A)$ etc.  
        *   Total pairs: $3^2 = 9$.  
        *   Same dish pairs: (Apple,Apple), (Banana,Banana), (Cherry,Cherry). There are 3 such cases.  
        *   Pairs where they don't match: $9 - 3 = 6$.  
        *   List: $(A, B)$, $(A, C)$, $(B, A)$, $(B, C)$, $(C, A)$, $(C, B)$. Wait.  
        *   Let's check my subtraction logic again.  
            *   Total = 9.  
            *   Matching: (Apple, Apple). There are $N=3$ items for the second person too. So there are $3 \times 1 = 3$ matching pairs where Yann picks X and Camille picks X.  
            *   Difference: $9 - 3 = 6$.  
        *   Wait, is it possible I missed something?  
            *   Let's check the list of distinct ordered pairs $(Yann, Camille)$ from $\{1,2,3\}^2$.  
            *   (1,1), (1,2), (1,3) -> Yann has apple. Camille has apple, banana, cherry. 3 cases where they are different. Wait, no.  
            *   Let's do it properly.  
            *   Case: Yann orders Dish 1 (Apple).  
                *   Camille can order Dish 2 (Banana). Different? Yes.  
                *   Camille can order Dish 3 (Cherry). Different? Yes.  
                *   Camille can order Dish 1 (Apple). Same? No.  
            *   Case: Yann orders Dish 2 (Apple - wait, let's use the numbers 1,2,3).  
            *   Let's say Yann picks 1. Then Camille picks from {2, 3}. That's $3-1=2$.  
            *   If Yann picks 2. Camille picks from {1, 3}. That's $3-1=2$.  
            *   If Yann picks 3. Camille picks from {1, 2}. That's $3-1=2$.  
            *   Total = $2+2+2 = 6$.  

    *   Okay, let's re-evaluate the subtraction method ($N^2 - N$).  
        *   Total options for Yann = 10.  
        *   For a specific dish, say "Fish".  
            *   If Yann picks Fish: Camille can pick "Apple", "Banana", ..., "Chicken" (9 choices).  
            *   So if we fix Yann's choice to be Dish X, there are $N-1$ choices for Camille.  
        *   Sum over all possible Yannah choices: $10 \times 9 = 90$.  

    *   **Is it possible the question implies they pick a dish together?**  
        *   "Yann and Camille go to a restaurant... if there are 10 items on the menu, and each orders one dish". This means individual decisions. Yann orders 1. Camille orders 1.  

    *   **Another Interpretation: Permutation**  
        *   Yann chooses an item $y$. Camille chooses an item $c$.  
        *   Total space is $\{1..10\} \times \{1..10\}$. Size = 100.  
        *   Constraint: $y \neq c$ (where items are identical).  
        *   Valid pairs = $10 \times 9 = 90$.  

    *   **What about "refuse to order the same dish"?**  
        *   Could it mean Yann cannot order a dish that Camille already ordered? No, they are ordering from the menu *together* or sequentially.  
        *   It implies Yann does not want Camille's specific item if he ordered it... wait, no, "same dish". Usually means the same item.  
        *   Example: If Yann orders Chicken, and Camille orders Chicken, that is a violation.  
        *   So, my logic holds.  

    *   **Alternative Interpretation (Ordering of Menu):**  
        *   What if they choose *sets*?  
        *   Set notation usually implies order doesn't matter. But the problem explicitly states "Yann ordering chicken and Camille ordering fish is different from Yann ordering fish and Camille ordering chicken." This is a permutation.  

    *   **Conclusion so far:** 90.  

5.  **Let's double check similar problems online or in literature.**  
    *   Problem type: Permutations of combinations with restrictions.  
    *   Often called "Ordered Combinations" or "Permutations" or "Distinct Orders".  
    *   If $N$ items, distinct choices for Person A and Person B where A != B (in terms of item).  
    *   Number of permutations = $P(N, 2) = N \times (N-1)$.  

6.  **Let's verify the constraints again.**  
    *   Menu items: 10 distinct options. Let's call them $D_1, ..., D_{10}$.  
    *   Yann chooses an option from these. Say $y \in \{1..10\}$.  
    *   Camille chooses an option from these. Say $c \in \{1..10\}$.  
    *   Condition: The condition "refuse to order the same dish" means we count pairs $(y, c)$ such that they are not equal? Wait.  
    *   Let's check the wording "If they refuse to order the same dish".  
    *   Interpretation 1: A dish cannot be ordered by both. Yann orders $D_1$, Camille cannot order $D_1$.  
        *   This is standard interpretation ($y \neq c$).  
    *   Interpretation 2: They refuse to share the same meal conceptually, but they choose items from a pool where "the dish" means specific types (e.g., Pasta, Salad).  
        *   Same result.  

    *   Is there any ambiguity about "combinations"?  
        *   Sometimes people use "combination" loosely to mean "way to order". Since the prompt specifies distinct ordering matters for individuals, we treat it as an ordered tuple.  
        *   If they were asking for "pairs of dishes selected by Yann and Camille", usually that implies the set $\{yann\_dish, camille\_dish\}$.  
        *   However, since $(Chicken, Fish) \neq (Fish, Chicken)$, it asks for ordered pairs.  

    *   Let's check if there is an interpretation where "refuse to order the same dish" means Yann and Camille cannot both pick from the subset of available items... No, that's overthinking.  
    *   What if "Yann ordering chicken and Camille ordering fish" refers to their *names*?  
        *   If Yann orders Chicken (item) vs Fish (item).  
        *   Wait, does "Chicken" refer to a name of the dish or the person's choice? "Yann ordering chicken". Usually means the item on the menu is named "chicken" (or "fries", or "salad"). Let's assume these are items.  

    *   **Another edge case: Is there any overlap?**  
        *   Suppose there are 3 items. $P(3,2) = 3 \times 2 = 6$.  
        *   Pairs: $(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)$. Total 6.  
        *   Constraint $x \neq y$? Yes, all distinct pairs have $x \neq y$.  
        *   Is it possible to interpret "refuse to order the same dish" as "cannot order the same item" if they are friends? If they both want Chicken, that's a conflict. But usually in these math puzzles, "same dish" means identical menu items.  

    *   Let's look at the result again. $10 \times 9 = 90$.  
    *   Is it possible they can order dishes but not *the same*? No, the constraint is explicitly stated.  
    *   The prompt asks for "different combinations of meals". This implies an ordered list of dishes: (Dish_1, Dish_2).  

    *   Let's check if there is any tricky interpretation where the menu has items that are subsets?  
        *   Usually menus have discrete items like 50s, fries, steak. They are distinct.  

    *   Let's consider the phrase "combinations of meals". This might be interpreted as a combination (multiset) if order didn't matter, but then it would explicitly say "order doesn't matter". Here it says order matters.  

    *   **Wait, is there a possibility that Yann chooses *after* Camille?**  
        *   The prompt asks "how many different combinations of meals can Yann and Camille order". It lists the two people as agents. Since it specifies "Yann ordering chicken and Camille ordering fish" (specific example), the person identity matters.  

    *   Let's re-read carefully to ensure no hidden constraints like "Yann must get a unique dish, but he can't share the same one with Camille".  
    *   Actually, the wording is: "If there are 10 items on the menu, and each orders one dish... they refuse to order the same dish."  
    *   This phrasing usually implies that the set of dishes available for Yann must not intersect with the set of dishes available for Camille in any way? No, that's impossible. "Refuse to order the same dish" is a pairwise constraint. $D_{Yann} \neq D_{Camille}$.  

    *   **Final check:**  
        *   Items: 10.  
        *   People: 2 (distinct).  
        *   Action: Choose distinct items for each person.  
        *   Formula: $N(N-1)$.  
        *   Calculation: $10(9) = 90$.  

    *   Let's consider if "refuse to order the same dish" implies that Yann cannot choose *a specific* item if Camille chose it, but they have their own menus? No, "refuse to order the same dish" implies they both go for a meal where no two people ordered from the same menu item.  

    *   **Is there any possibility of misreading "combinations"?**  
        *   Combinations usually refers to sets $\{A, B\}$. If $A$ and $B$ are distinct (e.g., set {chicken, fish}), order might not matter in terms of the set itself, but the prompt clarifies order matters ($Y=C_1, C=K \neq Y=C_2, K=Y_1$). So this is an ordered pair $(A,B)$.  

    *   **Could it be 10 options per person? Yes.**  
        *   "If there are 10 items on the menu" -> Total pool = 10.  
        *   Each orders one dish -> Yann chooses from 10, Camille chooses from 10.  

    *   **Final Answer Formulation:**  
        *   Step 1: Identify total possible choices for Yann (10).  
        *   Step 2: Identify total possible choices for Camille (10).  
        *   Step 3: Note that the outcome depends on who orders what, establishing an ordered pair. Total potential pairs = $10 \times 10 = 100$.  
        *   Step 4: Apply constraint. Yann and Camille refuse to order the same dish. This means we must subtract cases where both order the same dish.  
        *   Step 5: Count invalid cases (Same dish). If Yann orders Dish $x$, Camille can order any of the 9 remaining dishes? Or does it imply they are distinct? Yes, "refuse to order the same". Wait, usually if you refuse to order the *same* thing, you pick different things.  
            *   Let's verify: If Yann picks "Pizza" and Camille picks "Pizza", is that a valid outcome for them refusing to order the same dish? No. They did not refuse; they both took Pizza.  
            *   The condition "refuse to order the same dish" implies we want outcomes where $D_{Yann} \neq D_{Camille}$.  
        *   Step 6: Calculation = Total - Invalid = $100 - 9$? No, wait.  
            *   Is it invalid if both pick Pizza? Yes.  
            *   If Yann picks Pizza (1 case) and Camille picks Pizza (1 case). This is 1 case.  
            *   Wait, my previous subtraction logic was: $10 \times 9$.  
            *   Let's re-evaluate "Total - Same".  
            *   Total = 100.  
            *   Same = If Yann picks Pizza (1) and Camille picks Pizza (1). That is 1 case per dish. Since there are 10 dishes, there are 10 same-dish cases.  
            *   So $100 - 10 = 90$.  

    *   Wait, I need to check the math logic again in my head.  
        *   Logic A: Direct count.  
            *   Yann picks $d_y \in \{1..10\}$. (10 choices)  
            *   Camille picks $d_c \in \{1..10\}$ such that $d_c \neq d_y$. (9 choices for each choice of $d_y$).  
            *   Total = $\sum_{d_y=1}^{10} 9 = 90$. Correct.  
        *   Logic B: Subtraction.  
            *   Pairs are sets $\{(Y, C)\}$ from $10 \times 10$. (100 pairs).  
            *   Invalid: $Y=C$. There are 10 such pairs for each of the 10 items? No.  
                *   For item 1: (1,1) is invalid.  
                *   For item 2: (2,2) is invalid.  
                *   For item 3: (3,3) is invalid.  
                *   ...  
                *   Wait, there are only 10 items. So the pairs (1,1), (2,2), ..., (10,10) are the only ones where Y=C. That's exactly 10 pairs.  
            *   So Total Valid = $100 - 10 = 90$. Correct.  

    *   Wait, is there any interpretation where "combinations of meals" means combinations of people? No.  
    *   Is it possible that Camille has *no* choices for specific dishes because Yann's choice affects hers?  
        *   The question says "If there are 10 items on the menu". It implies independent selection process based on pool size.  
        *   If they refused to order *each other*, say, if Yann orders Chicken and Camille refuses to order Fish... wait.  
        *   Usually "refuse to order the same dish" means "do not pick the same item from the menu".  
        *   But what if "Yann ordering chicken" is specific? Yes, it says "Yann ordering chicken". The item must be on the menu.  

    *   **Let's check a counter-interpretation just in case.**  
        *   Suppose Yann chooses Chicken (C). Camille refuses to order C. So Camille can choose any of 9.  
        *   Suppose Yann chooses Fish (F). Camille refuses to order F. So Camille can choose any of 9.  
        *   The problem asks for the number of combinations.  
        *   It could be read as: Yann picks from 10. Camille picks from 10 \ {Yann's dish}. This is $10+9 = 9$ total? No, that doesn't make sense because they can pick anything *other* than what the other picked.  
        *   So it is simply $N(N-1)$.  

    *   What if "refuse to order the same dish" means Yann cannot order a dish X if Camille has ordered X?  
        *   If this were a sequential scenario (Yann orders, then Camille orders):  
            *   Scenario 1: Yann picks from 10. Camille picks any of remaining 9.  
            *   Wait, does "refuse to order the same dish" apply regardless of who chooses first?  
            *   "They refuse to order the same dish" is a condition on the final outcome $(D_Y, D_C)$. The condition is $D_Y \neq D_C$.  
            *   Whether it's sequential or simultaneous doesn't change the count.  
            *   If Yann picks Fish and Camille picks Fish (both ordered Fish), they refused to order different dishes? No, "refuse to order the same dish" means the constraint is that they don't pick from the set of menu items $\{i\}$ for both. So if they both order fish, that's a violation.  
            *   My logic holds.  

    *   **What if "combinations" implies sets?**  
        *   Prompt: "(It does matter who orders what---Yann ordering chicken and Camille ordering fish is different from Yann ordering fish and Camille ordering chicken.)"  
        *   This phrasing explicitly validates Permutations over Combinations. So we are looking for the number of ordered pairs $(D_Y, D_C)$.  

    *   **Final Answer:** 90.  

7.  **Summary of Steps for Output:**  
    *   Identify the number of items on the menu ($N = 10$).  
    *   Identify the number of choices per person ($N$ for both).  
    *   Calculate total possible pairings without restriction ($N \times N = 100$).  
    *   Subtract the cases where Yann and Camille order the same dish (where they are identical in value, i.e., $Yann=Dish X, Camille=Dish X$, or just check the logic: $10 \text{ dishes} \times 1 \text{ person each}$... wait).  
    *   Let's re-verify "Subtraction".  
        *   If Yann orders Dish A (1 choice) and Camille refuses to order Dish A (0 choices), that is one scenario. But there are 9 other dishes for Camille. So if we just want the set of all valid combinations.  
    *   Wait, I'm looping in my head on subtraction logic again. Let's write it cleanly.  
        *   Set $S = \{1, ..., 10\}$.  
        *   We need pairs $(a, b)$ from $S \times S$ such that $a \neq b$.  
        *   Total pairs = $|S|^2 = 100$.  
        *   Invalid pairs: $a = b$. There are $10$ such pairs in the Cartesian product: $(1,1), (2,2), ..., (10,10)$.  
        *   Valid pairs = Total - Invalid = $100 - 10 = 90$.  

    *   Let's double check if there is a different reading. "If there are 10 items on the menu" could be interpreted as Yann orders one dish, Camille orders another? Yes.  
    *   What if they can choose multiple dishes? No "orders one dish".  
    *   What if "combinations of meals" implies that the two people order a meal set, i.e., $\{D_1, D_2\}$. If so, does the pair (Chicken, Fish) count as one combination?  
        *   The prompt says "Yann ordering chicken and Camille ordering fish is different from Yann ordering fish and Camille ordering chicken".  
        *   This confirms we are counting distinct ordered pairs.  
        *   In set theory terms, this would be $S = \{C, F\}$ (a set of size 2). This corresponds to $\{C, C'\}$ or $\{F, F'\}$. But order matters, so $(C,F) \neq (F,C)$.  

    *   Result is 90.  

    *   Let's re-read "If there are 10 items on the menu". Does this include Yann's choice?  
    *   It usually means the pool from which they draw. Yes.  

    *   Wait, could "combinations" imply *order doesn't matter* but the clarification contradicts it?  
        *   Standard English usage: "Combination" implies order doesn't matter (e.g., a pair of shoes {Left, Right} is same as {Right, Left}). "Permutation" implies order matters.  
        *   The prompt explicitly uses an example to differentiate between "Yann ordering chicken" and "Yann ordering fish". This is clearly about the person's role.  
        *   Therefore, this is a permutation problem (ordered pairs).  
    *   Could the answer be $10 \times 10$?  
        *   No, because of "refuse to order the same dish".  
    *   Could the answer be $10 + 9 = 19$?  
        *   That's summing things.  
    *   Could it be related to sets where order doesn't matter but we consider distinct people?  
        *   If I have a set of pairs $\{ (Chicken, Fish), (Fish, Chicken) \}$ and treat them as one "combination" of meals ordered by two friends... The prompt explicitly says they are different.  

    *   **Final Answer:** 90.  

    *   Let's consider if the question implies Yann and Camille choose independently but from a *common* menu?  
        *   Yes, that's what it means. $P(Yann) \cap P(Camille)$.  
        *   Wait, does "combinations of meals" imply they pick one meal each, so the outcome is $(Meal_Y, Meal_C)$.  
    *   Is there any trick about the names? No.  

    *   One slight nuance: Does "Yann ordering chicken" mean Yann selects Chicken from a pool? Or does it mean Yann's ordered item is Chicken? Yes.  
    *   Let's check for potential misinterpretations of "combinations".  
        *   Usually in math competitions, "how many different combinations" can be tricky if the prompt defines order matters.  
        *   The prompt explicitly defines order matters. So we just stick to permutations.  
    *   Is there any interpretation where they share a single "Meals"? Like a shared menu? No, "orders one dish".  

    *   Let's verify if the problem implies $N=10$. Yes.  
    *   Formula $10 \times 9 = 90$.  

    *   Could there be an interpretation where they choose *sets* of dishes from the menu? No, "each orders one dish".  

    *   Final check on the subtraction logic.  
        *   Total permutations: $P(10, 2)$? No, that's if you pick two distinct items from a set without replacement for the two people. Yes, exactly $P(10, 2)$.  
        *   Wait, is $P(n,r)$ used when order matters and no repetition allowed?  
            *   For Person A: $r_1$ choices.  
            *   For Person B: $r_2$ choices.  
            *   Constraint: $Item(A) \neq Item(B)$.  
            *   Total = $10 \times (10-1) = 90$.  
    *   This seems robust.  

    *   Wait, is it possible that "different combinations of meals" means the combination of dishes ordered by the group?  
        *   If Yann orders Chicken and Camille orders Fish -> {Chicken, Fish}.  
        *   If Yann orders Fish and Camille orders Chicken -> {Fish, Chicken}.  
        *   If this interpretation were true, there would only be 10 combinations (sets). But the prompt says they are different. So it's definitely 90.  

    *   Wait, I see "If there are 10 items on the menu".  
        *   Does the phrase "combinations of meals" refer to the set of items ordered by the two people?  
        *   If the prompt meant the set $\{D_Y, D_C\}$ as a combination, it would usually say "how many ways can they order different dishes?" or similar. But the example says: "Yann ordering chicken and Camille ordering fish is different from Yann ordering fish and Camille ordering chicken".  
        *   This implies $(Chicken, Fish) \neq (Fish, Chicken)$.  
        *   This confirms we are counting permutations.  

    *   Therefore, calculation $10 \times 9 = 90$.  

    *   Wait, is there an interpretation where "refuse to order the same dish" means they refuse to order the *same type of dish*? E.g. if both want Chicken, they can't do it.  
        *   If Yann picks Chicken (1 choice). Camille picks Fish (9 choices).  
        *   If Yann picks Fish (9 choices). Camille picks Chicken (8 choices)? No.  
        *   It means the set of valid ordered pairs is $\{(a,b) \in \{1..10\}^2 \mid a \neq b\}$.  

    *   Just to be pedantic, what if "combinations" implies order doesn't matter?  
        *   The prompt explicitly clarifies it's different.  
        *   So, we are not calculating combinations of sets. We are calculating ordered pairs.  
        *   Number of ways = 90.  

    *   One edge case: Is "refuse to order the same dish" implying that if Yann orders A, Camille cannot order A? Or does it imply they share a pool but cannot both pick items from the intersection? No, "refuse to order the same dish" implies a constraint between their two choices. $D_1 \neq D_2$.  

    *   The answer is 90.  


## Answer

To solve this problem, we need to determine the number of distinct ways Yann and Camille can order one dish each from a menu of 10 items, such that they do not both choose the same dish.  

**Step 1: Determine the total available choices for each person.**  
The restaurant has a menu with 10 items. Since "each orders one dish", Yann has 10 possible options to choose from ($n_Y = 10$). Camille also has 10 possible options to choose from ($n_C = 10$).  

**Step 2: Determine the total number of ordered pair possibilities without restriction.**  
If there were no restrictions, the number of ways they could order dishes would be the product of their individual choices (since Yann's choice is distinct from Camille's choice in terms of counting combinations, but we need to apply the constraint later).  
Total possible ordered pairs $(D_Y, D_C) = 10 \times 10 = 100$.  

**Step 3: Apply the restriction "refuse to order the same dish".**  
The problem explicitly states that it matters who orders what (permutation logic), and we must count combinations where Yann and Camille do not order the same dish. This implies a constraint on the chosen dishes, such that they are distinct items ($D_Y \neq D_C$).  

There are two main ways to calculate this:  
1.  **Subtraction Method:** Start with the total number of possible outcomes and subtract the outcomes that violate the condition (Yann and Camille choosing the same dish).  
    *   Total outcomes = 100  
    *   Unwanted outcomes (where they choose the same dish): For each of the 10 dishes on the menu, there is exactly one way both Yann and Camille could choose it ($D_Y = \text{Dish}_i$ and $D_C = \text{Dish}_i$). This gives us 10 unwanted pairs: $(\text{Dish}_1, \text{Dish}_1), (\text{Dish}_2, \text{Dish}_2), ..., (\text{Dish}_{10}, \text{Dish}_{10})$.  
    *   Valid outcomes = Total - Unwanted = $100 - 10 = 90$.  

2.  **Direct Counting Method:** Calculate the number of choices for Camille based on Yann's choice, summing up all valid options.  
    *   If Yann chooses a specific dish (say, Item A), there are 9 other items remaining on the menu for Camille to pick from. (She cannot pick A).  
    *   This is valid for every dish Yann chooses: $10 \text{ choices for Yann} \times 9 \text{ choices for Camille}$.  
    *   Total = $10 \times 9 = 90$.  

Both methods lead to the same result. The problem asks for "different combinations of meals" but clarifies that who orders what is distinct (Yann ordering A and Camille ordering B $\neq$ Yann ordering B and Camille ordering A). This confirms we are counting the permutations.  

Final Answer: 90.  

\boxed{90}  
