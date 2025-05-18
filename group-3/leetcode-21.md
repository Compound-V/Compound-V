---
description: Merge two sorted list
---

# Leetcode : 21

***

#### Problem Samajh Lo

Ye problem hai do sorted linked lists ko merge karne ka. Linked list kya hoti hai? Soch, jaise train ke dibbe ek line mein judte hain, har dibbe mein ek value hoti hai aur ek pointer jo agle dibbe ko point karta hai. Yahan:

* **Input**: Do linked lists `list1` aur `list2`, dono sorted hain (chhote se bade numbers, non-decreasing order).
* **Kaam**: In dono ko merge karke ek naya sorted linked list banana hai, aur isme original nodes ko use karna hai (naye nodes nahi banane).
* **Output**: Merged list ka head return karna hai.

**Examples**:

1. `list1 = [1,2,4]`, `list2 = [1,3,4]` → Output: `[1,1,2,3,4,4]`
   * Dono lists sorted hain, merge karne pe ek sorted list milegi.
2. `list1 = []`, `list2 = []` → Output: `[]`
   * Dono khali hain, toh output bhi khali.
3. `list1 = []`, `list2 = [0]` → Output: `[0]`
   * Ek list khali, dusri mein ek node, toh wahi return hoga.

**Constraints**:

* Lists mein nodes 0 se 50 tak ho sakte hain.
* Node values -100 se 100 tak honge.
* Dono lists sorted hain (non-decreasing, matlab equal values bhi ho sakte hain).

***

#### Linked List Ka Basic Concept

Bhai, pehle linked list samajh le, kyunki ye problem ispe based hai:

* Linked list ek data structure hai jisme **nodes** hote hain.
* Har node mein do cheez hoti hain:
  1. **Value** (yahan integer, e.g., 1, 2, 4).
  2. **Next Pointer** (agle node ka address).
* Last node ka next pointer `NULL` hota hai (list khatam).
* **Head** list ka pehla node hota hai, jisse list start hoti hai.

**Example**: `[1,2,4]` linked list ka structure:

```
Node1: [val=1, next=Node2] -> Node2: [val=2, next=Node3] -> Node3: [val=4, next=NULL]
```

C mein linked list ke node ko aise define karte hain:

```c
struct ListNode {
    int val;           // Node ki value
    struct ListNode* next; // Agle node ka pointer
};
```

***

#### Solution Idea (Logic in Hinglish)

Bhai, is problem ko solve karne ke liye hum do sorted lists ko merge karenge jaise do sorted decks of cards ko milate hain. Logic ye hai:

1. Ek **dummy node** banayenge jisse merged list start hogi. Ye help karta hai edge cases handle karne mein (jaise khali lists).
2. Do pointers rakhnge, ek `list1` ke head pe aur ek `list2` ke head pe.
3. Har step mein compare karenge dono lists ke current nodes ki values:
   * Jo value chhoti hai, usko merged list mein jodenge.
   * Uska pointer aage badhayenge (next node pe).
4. Jab ek list khatam ho jaye, dusri list ke bache hue nodes ko merged list ke end mein jod denge.
5. Last mein dummy node ke next pointer ko return karenge (kyunki dummy node actual list ka part nahi hai).

**Example Dry Run** (`list1 = [1,2,4]`, `list2 = [1,3,4]`):

* Start: `list1 = 1->2->4`, `list2 = 1->3->4`, `dummy = []`, `curr = dummy`.
* Step 1: `list1->val (1) <= list2->val (1)`, toh `list1` ka 1 jodenge:
  * `curr->next = list1`, `list1 = list1->next (2)`, `curr = curr->next`.
  * Merged: `[]->1`.
* Step 2: `list1->val (2) > list2->val (1)`, toh `list2` ka 1 jodenge:
  * `curr->next = list2`, `list2 = list2->next (3)`, `curr = curr->next`.
  * Merged: `[]->1->1`.
* Step 3: `list1->val (2) <= list2->val (3)`, toh `list1` ka 2 jodenge:
  * Merged: `[]->1->1->2`.
* Step 4: `list1->val (4) > list2->val (3)`, toh `list2` ka 3 jodenge:
  * Merged: `[]->1->1->2->3`.
* Step 5: `list1->val (4) <= list2->val (4)`, toh `list1` ka 4 jodenge:
  * Merged: `[]->1->1->2->3->4`.
* Step 6: `list1 = NULL`, toh `list2` ke bache hue (4) jodenge:
  * Merged: `[]->1->1->2->3->4->4`.
* Return: `dummy->next` (1->1->2->3->4->4).

***

#### C Code

Ab code likhte hain, aur har line ko baad mein detail mein samjhaunga.

```c
#include <stdio.h>
#include <stdlib.h>

// Linked list node ka structure
struct ListNode {
    int val;
    struct ListNode* next;
};

// Function to merge two sorted lists
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    // Dummy node banaya to handle edge cases
    struct ListNode dummy;
    struct ListNode* curr = &dummy;
    dummy.next = NULL;
    
    // Jab dono lists mein nodes hain
    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            curr->next = list1; // list1 ka node jodo
            list1 = list1->next; // list1 aage badhao
        } else {
            curr->next = list2; // list2 ka node jodo
            list2 = list2->next; // list2 aage badhao
        }
        curr = curr->next; // curr pointer aage badhao
    }
    
    // Bachi hui list ko jod do
    if (list1 != NULL) {
        curr->next = list1;
    } else if (list2 != NULL) {
        curr->next = list2;
    }
    
    return dummy.next; // Merged list ka head return karo
}

// Helper function to create a new node (testing ke liye)
struct ListNode* newNode(int val) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    return node;
}

// Helper function to print list (testing ke liye)
void printList(struct ListNode* head) {
    struct ListNode* temp = head;
    printf("[");
    while (temp != NULL) {
        printf("%d", temp->val);
        temp = temp->next;
        if (temp != NULL) printf(",");
    }
    printf("]\n");
}

int main() {
    // Test Case 1: list1 = [1,2,4], list2 = [1,3,4]
    struct ListNode* list1 = newNode(1);
    list1->next = newNode(2);
    list1->next->next = newNode(4);
    
    struct ListNode* list2 = newNode(1);
    list2->next = newNode(3);
    list2->next->next = newNode(4);
    
    printf("Test Case 1:\n");
    printf("list1 = ");
    printList(list1);
    printf("list2 = ");
    printList(list2);
    struct ListNode* merged = mergeTwoLists(list1, list2);
    printf("Output: ");
    printList(merged);
    
    // Test Case 2: list1 = [], list2 = []
    list1 = NULL;
    list2 = NULL;
    printf("\nTest Case 2:\n");
    printf("list1 = []\nlist2 = []\n");
    merged = mergeTwoLists(list1, list2);
    printf("Output: ");
    printList(merged);
    
    // Test Case 3: list1 = [], list2 = [0]
    list1 = NULL;
    list2 = newNode(0);
    printf("\nTest Case 3:\n");
    printf("list1 = []\nlist2 = ");
    printList(list2);
    merged = mergeTwoLists(list1, list2);
    printf("Output: ");
    printList(merged);
    
    return 0;
}
```

***

#### Detailed Explanation (Har Cheez Break Down)

**1. Header Files**

```c
#include <stdio.h>
#include <stdlib.h>
```

**Kya hai ye?**

* `<stdio.h>`: Input-output ke liye, jaise `printf` function.
* `<stdlib.h>`: Memory allocation ke liye, jaise `malloc` (new nodes banane ke liye testing mein use kiya).

**Kyun use kiye?**

* `printf`: Test cases ke input aur output print karne ke liye.
* `malloc`: Testing ke liye new nodes dynamically allocate karne ke liye.

**Standard Syntax**:

* `#include <library_name.h>`

**Alternatives**:

* `<stdio.h>` ka koi alternative nahi kyunki `printf` ke liye ye zaroori.
* `<stdlib.h>` skip kar sakte the agar hum static nodes banate, lekin `malloc` testing ke liye convenient hai.

**Common Mistakes**:

* `<stdio.h>` bhool jana aur `printf` use karna → Undeclared function error.
* `<stdlib.h>` bhool jana aur `malloc` use karna → Compilation error.
* Header file ka naam galat likhna, jaise `stdio` ke bajaye `studio`.

***

**2. Linked List Node Structure**

```c
struct ListNode {
    int val;
    struct ListNode* next;
};
```

**Kya hai ye?**

* Ye ek `struct` hai jo linked list ke node ko define karta hai.
* `int val`: Node ki value (e.g., 1, 2, 4).
* `struct ListNode* next`: Pointer jo agle node ko point karta hai.
* `struct ListNode` isliye likha kyunki C mein struct ko recursively define karne ke liye type naam chahiye.

**Kyun use kiya?**

* Linked list ke har node ko value aur next pointer chahiye, ye standard tarika hai.
* Problem mein diya gaya hai ki nodes ka structure aisa hi hoga.

**Standard Syntax**:

*   Struct definition:

    ```c
    struct struct_name {
        data_type member1;
        data_type member2;
    };
    ```

**Alternatives**:

*   `typedef` use kar sakte the for cleaner syntax:

    ```c
    typedef struct ListNode {
        int val;
        struct ListNode* next;
    } ListNode;
    ```

    Fir `struct ListNode*` ke bajaye `ListNode*` likh sakte the.
* `val` ko `double` ya `float` bhi bana sakte the, lekin problem mein integers hain.

**Common Mistakes**:

* `struct` keyword bhool jana jab pointer define karte hain.
* `next` pointer ko `struct ListNode` ke bajaye `int*` ya galat type dena.
* Struct ke members ka order galat karna.

***

**3. Function Definition**

```c
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2)
```

**Kya hai ye?**

* Ye function do linked lists ke heads (`list1`, `list2`) leta hai aur merged list ka head return karta hai.
* Return type `struct ListNode*` hai kyunki humein linked list ka head pointer return karna hai.

**Kyun use kiya?**

* Problem ka core logic yahin implement hota hai.
* Pointers use kiye kyunki linked lists C mein pointers se handle hoti hain.

**Standard Syntax**:

*   Function syntax:

    ```c
    return_type function_name(parameter_type param1, parameter_type param2) {
        // Code
    }
    ```

**Alternatives**:

*   Recursive function use kar sakte the:

    ```c
    struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
        if (list1 == NULL) return list2;
        if (list2 == NULL) return list1;
        if (list1->val <= list2->val) {
            list1->next = mergeTwoLists(list1->next, list2);
            return list1;
        } else {
            list2->next = mergeTwoLists(list1, list2->next);
            return list2;
        }
    }
    ```

    Ye compact hai, lekin stack overflow ka risk hai bade inputs pe.
* `void` function bana sakte the jo merged list ko parameter mein modify karta, lekin head return karna cleaner hai.

**Common Mistakes**:

* Return type galat likhna, jaise `int` ke bajaye `struct ListNode`.
* Parameters ke pointers galat handle karna.
* `return` statement bhool jana.

***

**4. Dummy Node Setup**

```c
struct ListNode dummy;
struct ListNode* curr = &dummy;
dummy.next = NULL;
```

**Kya hai ye?**

* `dummy` ek temporary node hai jo merged list ke shuru mein rakhte hain.
* `curr` ek pointer hai jo merged list ke current node ko track karta hai.
* `dummy.next = NULL` se dummy node ka next pointer initialize kiya.

**Kyun use kiya?**

* Dummy node edge cases handle karta hai, jaise jab dono lists khali hain ya ek list khali hai.
* `curr` pointer hamesha merged list ke last node ko point karta hai, jisse new nodes jodna easy hota hai.
* `dummy.next` ko `NULL` set kiya kyunki shuru mein merged list khali hai.

**Standard Syntax**:

* Struct variable: `struct struct_name variable;`
* Pointer assignment: `struct_name* pointer = &variable;`
* Member access: `variable.member = value;`

**Alternatives**:

* Dummy node ke bajaye direct `list1` ya `list2` se start kar sakte the, lekin edge cases (e.g., khali lists) ke liye extra checks chahiye hote.
*   `malloc` se dynamic dummy node bana sakte the:

    ```c
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    ```

    Lekin static node simpler hai kyunki humein sirf temporary node chahiye.

**Common Mistakes**:

* `dummy.next` initialize nahi karna, jisse garbage value aa sakti hai.
* `curr` ko galat initialize karna, jaise `curr = dummy` (pointer mismatch).
* Dummy node ke concept ko skip karna, jisse edge cases fail ho jate hain.

***

**5. Main Merge Logic**

```c
while (list1 != NULL && list2 != NULL) {
    if (list1->val <= list2->val) {
        curr->next = list1;
        list1 = list1->next;
    } else {
        curr->next = list2;
        list2 = list2->next;
    }
    curr = curr->next;
}
```

**Kya hai ye?**

* Ye loop tab tak chalta hai jab dono lists mein nodes hain (`list1` aur `list2` `NULL` nahi hain).
* Har iteration mein:
  * Compare karte hain `list1->val` aur `list2->val`.
  * Chhoti value wala node merged list mein jodte hain (`curr->next`).
  * Uski list ka pointer aage badhate hain (`list1 = list1->next` ya `list2 = list2->next`).
  * `curr` ko new node pe move karte hain.

**Kyun use kiya?**

* Dono lists sorted hain, toh chhoti value pehle jodni hai taaki merged list bhi sorted rahe.
* `<=` isliye use kiya kyunki lists non-decreasing hain (equal values ho sakti hain).
* `curr` ko move karna zaroori hai kyunki humein hamesha last node pe new node jodna hai.

**Standard Syntax**:

*   `while` loop:

    ```c
    while (condition) {
        // Code
    }
    ```
* Pointer member access: `pointer->member`
* Logical AND: `condition1 && condition2`

**Alternatives**:

*   `if-else` ke bajaye ternary operator use kar sakte the (lekin less readable):

    ```c
    curr->next = (list1->val <= list2->val) ? list1 : list2;
    (list1->val <= list2->val) ? (list1 = list1->next) : (list2 = list2->next);
    ```
* Recursive approach (upar diya gaya) bhi ek option tha.
* Separate function bana sakte the comparison ke liye, lekin chhote code ke liye zarurat nahi.

**Common Mistakes**:

* `NULL` check bhool jana, jisse `list1->val` pe crash ho jata hai.
* `<=` ke bajaye `<` likhna, jisse equal values galat handle hote hain.
* `curr = curr->next` bhool jana, jisse list ka structure bigad jata hai.
* `list1` ya `list2` ko aage nahi badhana, jisse infinite loop ban jata hai.

***

**6. Handling Remaining Nodes**

```c
if (list1 != NULL) {
    curr->next = list1;
} else if (list2 != NULL) {
    curr->next = list2;
}
```

**Kya hai ye?**

* Jab ek list khatam ho jati hai, dusri list ke bache hue nodes ko merged list ke end mein jod dete hain.
* `curr->next` ko bachi hui list ke head se link karte hain.

**Kyun use kiya?**

* Ek list khatam hone ke ba traumas, dusri list mein nodes bache ho sakte hain (e.g., `list1 = [1,2,4]`, `list2 = [1,3,4,5,6]`).
* Un nodes ko directly jodna safe hai kyunki lists already sorted hain.

**Standard Syntax**:

*   `if-else`:

    ```c
    if (condition) {
        // Code
    } else if (condition) {
        // Code
    }
    ```

**Alternatives**:

*   Single condition:

    ```c
    curr->next = list1 != NULL ? list1 : list2;
    ```

    Ye compact hai, lekin thoda less readable.
* Loop ke andar hi handle kar sakte the, lekin alag `if` clearer hai.

**Common Mistakes**:

* Bache hue nodes ko jodna bhool jana, jisse output incomplete hota hai.
* `curr->next` ke bajaye `curr` modify karna, jo list ka structure bigad deta hai.
* `NULL` check galat karna.

***

**7. Return Statement**

```c
return dummy.next;
```

**Kya hai ye?**

* `dummy.next` merged list ka actual head hai.
* `dummy` ek temporary node tha, toh usko skip karke uska next return karte hain.

**Kyun use kiya?**

* Problem mein merged list ka head return karna hai.
* `dummy.next` direct merged list ka start point deta hai.

**Standard Syntax**:

* `return expression;`

**Alternatives**:

*   Agar dummy node nahi use kiya hota, toh pehla node manually track karna padta:

    ```c
    struct ListNode* head = NULL;
    // Logic to set head
    return head;
    ```

    Lekin dummy node simpler hai.

**Common Mistakes**:

* `dummy` return karna instead of `dummy.next`, jisse extra node output mein aata hai.
* `return` bhool jana, jo undefined behavior deta hai.

***

**8. Helper Functions (Testing ke Liye)**

```c
struct ListNode* newNode(int val) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    return node;
}

void printList(struct ListNode* head) {
    struct ListNode* temp = head;
    printf("[");
    while (temp != NULL) {
        printf("%d", temp->val);
        temp = temp->next;
        if (temp != NULL) printf(",");
    }
    printf("]\n");
}
```

**Kya hai ye?**

* `newNode`: Ek naya node banata hai given value ke saath.
* `printList`: Linked list ko print karta hai `[1,2,3]` format mein.

**Kyun use kiya?**

* `newNode`: Test cases ke liye linked lists manually banane ke liye.
* `printList`: Input aur output visually dekhne ke liye.

**Standard Syntax**:

* `malloc`: `pointer = (type*)malloc(size);`
* Loop for traversal: `while (pointer != NULL)`

**Alternatives**:

*   Static nodes bana sakte the:

    ```c
    struct ListNode n1 = {1, NULL};
    ```

    Lekin `malloc` flexible hai.
* `printList` ke bajaye debug ke liye breakpoints ya logging use kar sakte the.

**Common Mistakes**:

* `malloc` ke return value ko check nahi karna (e.g., `NULL` ho sakta hai).
* `node->next` initialize nahi karna, jisse garbage value aati hai.
* `printList` mein `temp` ko `NULL` check nahi karna, jo crash kar sakta hai.

***

**9. Main Function**

```c
int main() {
    // Test cases setup and execution
}
```

**Kya hai ye?**

* Test cases ke liye lists banayi, merge kiya, aur results print kiye.
* `main` program ka entry point hai.

**Kyun use kiya?**

* Problem ke examples ko test karne ke liye.
* Output verify karne ke liye.

**Standard Syntax**:

* `int main() { return 0; }`

**Alternatives**:

* User input se lists banane ka code likh sakte the.
* Automated testing framework use kar sakte the.

**Common Mistakes**:

* `return 0` bhool jana.
* Test cases mein edge cases miss karna (e.g., khali lists).

***

**10. Common Mistakes in This Problem**

* **NULL Pointer Dereference**: `list1->val` access karna jab `list1` `NULL` hai.
* **Memory Leaks**: `malloc` use kiya aur `free` nahi kiya (testing mein issue ho sakta hai).
* **Incorrect Merging**: Nodes ka order galat karna, jisse unsorted list banta hai.
* **Edge Cases Miss**: Khali lists ya single-node lists handle nahi karna.
* **Dummy Node Misuse**: `dummy` ko directly return karna instead of `dummy.next`.
* **Infinite Loop**: `list1` ya `list2` ko aage nahi badhana.

***

**11. Test Results**

Output:

```
Test Case 1:
list1 = [1,2,4]
list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Test Case 2:
list1 = []
list2 = []
Output: []

Test Case 3:
list1 = []
list2 = [0]
Output: [0]
```

**Kyun Aisa Output?**

* **Test Case 1**: Dono lists merge hui, sorted order mein.
* **Test Case 2**: Dono khali, toh `dummy.next = NULL` → `[]`.
* **Test Case 3**: `list1` khali, `list2` ka node jod gaya.

***

**12. General Tips for Linked Lists**

1. **Draw It**: Linked list problems ke liye paper pe nodes aur pointers draw kar.
2. **NULL Checks**: Har pointer access se pehle `NULL` check kar.
3. **Dry Run**: Logic ko chhote examples pe test kar.
4. **Edge Cases**: Khali lists, single node, unequal lengths test kar.
5. **Practice**: Linked list ke basic operations (insert, delete, traverse) seekh.

***
