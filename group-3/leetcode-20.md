---
description: Valid Parentheses
---

# Leetcode : 20

***

#### Problem Recap (Valid Parentheses)

Ye problem hai ek string check karne ka, jisme sirf brackets hote hain: `(`, `)`, `{`, `}`, `[`, `]`. Tujhe batana hai ki string valid hai ya nahi. Valid hone ke rules:

1. Har opening bracket (`(`, `{`, `[`) ka same type ka closing bracket (`)`, `}`, `]`) hona chahiye.
2. Brackets ka order sahi hona chahiye (pehle jo open hua, uska close last mein).
3. Har closing bracket ka ek matching opening bracket hona chahiye.

**Examples**:

* `"()"` → Valid (ek pair, perfect).
* `"()[]{}"` → Valid (teen pairs, sab sahi order mein).
* `"(]"` → Invalid (mismatch, `(` ka `)` nahi, `]` ka `[` nahi).
* `"([])"` → Valid (nested, lekin sab match).

***

#### Code (C Language)

Ye hai pura code, aur iske baad har line, har concept ko detail mein samjhaunga.

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isValid(char *s) {
    char stack[10000]; // Stack array for storing opening brackets
    int top = -1;     // Stack ka top pointer, -1 matlab khali
    
    for (int i = 0; s[i] != '\0'; i++) {
        char ch = s[i];
        
        // Opening brackets ko stack mein push karo
        if (ch == '(' || ch == '{' || ch == '[') {
            stack[++top] = ch;
        }
        // Closing brackets ke liye check karo
        else if (ch == ')' || ch == '}' || ch == ']') {
            if (top == -1) { // Stack khali hai, no opening bracket
                return false;
            }
            char last = stack[top--]; // Pop karo last opening bracket
            if (ch == ')' && last != '(') return false;
            if (ch == '}' && last != '{') return false;
            if (ch == ']' && last != '[') return false;
        }
    }
    
    return top == -1; // Stack khali hona chahiye for valid string
}

int main() {
    char *test_cases[] = {"()", "()[]{}", "(]", "([])", "", "((()))", "([)]", "{"};
    int n = sizeof(test_cases) / sizeof(test_cases[0]);
    
    for (int i = 0; i < n; i++) {
        printf("Input: %s, Output: %s\n", test_cases[i], isValid(test_cases[i]) ? "true" : "false");
    }
    
    return 0;
}
```

***

#### Detailed Explanation (Har Cheez Break Down)

**1. Header Files**

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
```

**Kya hai ye?**

* Header files C mein libraries hain jo pre-written code rakhte hain. Ye code humein functions aur data types dete hain jo hum directly use kar sakte hain.
* `#include` ka matlab hai ki hum us library ko apne program mein add kar rahe hain.

**Kyun use kiye?**

* `<stdio.h>`: Ye **Standard Input/Output** ke liye hai. Isme functions hain jaise:
  * `printf()`: Screen pe output print karne ke liye.
  * `scanf()`: Input lene ke liye (is code mein nahi use kiya).
  * Humne `printf` use kiya test cases ke results dikhane ke liye.
* `<string.h>`: Ye string-related functions ke liye hai, jaise:
  * `strlen()`: String ki length nikalne ke liye.
  * `strcmp()`: Do strings compare karne ke liye.
  * Is code mein directly toh nahi use kiya, lekin string handling ke liye include karna safe hai (C mein strings tricky hoti hain).
* `<stdbool.h>`: Ye **boolean** data type ke liye hai, jo C mein by default nahi hota (purane C mein).
  * Isse hum `bool`, `true`, aur `false` use kar sakte hain.
  * Humara function `isValid` bool return karta hai (`true` ya `false`), isliye ye include kiya.

**Standard Syntax**:

* `#include <library_name.h>`: Ye standard tarika hai libraries include karne ka.
* Agar apni custom header file hoti, toh `#include "myfile.h"` likhte (double quotes).

**Alternatives kya the?**

* `<stdio.h>` ka koi alternative nahi tha kyunki `printf` ke liye ye zaroori hai.
* `<string.h>` skip kar sakte the kyunki humne koi string function use nahi kiya, lekin future-proof ke liye rakha.
* `<stdbool.h>` ke bina hum `int` use kar sakte the (`0` for false, `1` for true), lekin `bool` code ko readable banata hai.

**Common Mistakes**:

* Header file include nahi karna, aur `printf` ya `bool` use karne ki koshish karna → Error milega.
* Galat header file include karna, jaise `<stdlib.h>` jab zarurat na ho.
* `#include` ke baad semicolon (`;`) lagana → Syntax error.

***

**2. Function Definition**

```c
bool isValid(char *s)
```

**Kya hai ye?**

* Ye ek function hai jo string `s` ko input lega aur check karega ki valid hai ya nahi.
* `bool` return type hai, matlab function ya toh `true` ya `false` return karega.
* `char *s` matlab input ek string hai. C mein string ko `char` array ke roop mein ya pointer ke roop mein pass karte hain.

**Kyun use kiya?**

* `bool` isliye kiya kyunki problem mein bas valid/invalid check karna hai, aur `true`/`false` clean way hai result dikhane ka.
* `char *s` isliye kiya kyunki C mein strings ko pointer ke through pass karte hain. `char s[]` bhi likh sakte the, lekin `*s` zyada common hai function arguments ke liye.

**Standard Syntax**:

* `return_type function_name(parameter_type parameter_name)`:
  * `return_type`: Kya return hoga (e.g., `int`, `bool`, `void`).
  * `function_name`: Function ka naam (e.g., `isValid`).
  * `parameter_type`: Input ka type (e.g., `char *`).
  * `parameter_name`: Input ka naam (e.g., `s`).

**Alternatives kya the?**

* `bool` ke bajaye `int` use kar sakte the (`0` for false, non-zero for true), lekin `bool` modern aur readable hai.
* `char *s` ke bajaye `char s[]` likh sakte the, lekin dono ka kaam same hai function mein.

**Common Mistakes**:

* Return type mismatch, jaise `bool` declare kiya aur `int` return kar diya.
* Function ka naam galat likhna ya parameter type galat dena.
* Function ke end mein `return` statement bhool jana.

***

**3. Stack Setup**

```c
char stack[10000];
int top = -1;
```

**Kya hai ye?**

* `stack` ek array hai jo opening brackets (`(`, `{`, `[`) store karega. Array ka size 10000 isliye rakha kyunki problem ke constraints mein string ki max length 10^4 (10,000) hai, toh worst case mein itne brackets ho sakte hain.
* `top` ek integer variable hai jo batata hai stack ka sabse upar ka element kahan hai. `-1` isliye kiya kyunki stack khali hai shuru mein.

**Kyun use kiya?**

* **Stack**: Is problem mein humein brackets ka order track karna hai. Stack ka concept perfect hai kyunki ye "Last In, First Out" (LIFO) follow karta hai. Jo bracket last mein aaya, uska closing pehle check hoga.
* **Array for Stack**: C mein stack banane ka simple tarika hai array use karna. Hum `top` pointer se track karte hain ki kitne elements hain.
* **Size 10000**: Problem ke constraint ke hisaab se string mein max 10,000 characters ho sakte hain. Har character ek bracket hai, toh worst case mein 10,000 opening brackets ho sakte hain.
* **top = -1**: Jab stack khali hota hai, `top` ko `-1` set karte hain kyunki array ka index 0 se start hota hai. Jab pehla element push karenge, `top` 0 ho jayega.

**Standard Syntax**:

* Array declare karne ka syntax: `data_type array_name[size];`
  * `char stack[10000];` → 10,000 `char` store kar sakta hai.
* Variable declare karne ka syntax: `data_type variable_name = value;`
  * `int top = -1;`

**Alternatives kya the?**

*   **Dynamic Array**: `malloc()` se dynamic memory allocate kar sakte the, jaise:

    ```c
    char *stack = (char *)malloc(10000 * sizeof(char));
    ```

    Lekin static array simpler hai aur problem ke size fixed hai, toh zarurat nahi.
* **Linked List for Stack**: Stack ko linked list se bhi implement kar sakte the, lekin array faster aur easier hai chhote problems ke liye.
* **Smaller Size**: Agar string length chhoti hoti, toh `stack[100]` ya `stack[50]` bhi kaam karta, lekin constraints ke hisaab se 10000 safe hai.
* **top Initialization**: `top = 0` bhi use kar sakte the, lekin fir push/pop logic change karna padta (e.g., pehle element `stack[0]` pe daalte aur `top` ko increment karte).

**Common Mistakes**:

* Array ka size chhota rakhna (e.g., `stack[10]`), jo bade inputs ke liye overflow karega.
* `top` ko initialize nahi karna, jisse garbage value aa sakti hai.
* Array ke bahar access karna (e.g., `stack[10000]`), jo segmentation fault dega.

***

**4. Loop Through String**

```c
for (int i = 0; s[i] != '\0'; i++)
```

**Kya hai ye?**

* Ye ek `for` loop hai jo string ke har character ko ek ek karke check karta hai.
* `s[i]` se hum string ka current character access karte hain.
* `s[i] != '\0'` check karta hai ki string khatam nahi hui. C mein string ke end mein `\0` (null character) hota hai.

**Kyun use kiya?**

* String ke har character ko process karna zaroori hai kyunki humein har bracket check karna hai.
* `\0` check karna C mein standard tarika hai string ke end tak jane ka, kyunki C strings null-terminated hoti hain.

**Standard Syntax**:

*   `for` loop ka syntax:

    ```c
    for (initialization; condition; update) {
        // Code
    }
    ```

    * `int i = 0`: Loop variable `i` ko 0 se start karo.
    * `s[i] != '\0'`: Jab tak string ka character null nahi hai, loop chala.
    * `i++`: Har iteration ke baad `i` ko increment karo.

**Alternatives kya the?**

*   **While Loop**:

    ```c
    int i = 0;
    while (s[i] != '\0') {
        // Code
        i++;
    }
    ```

    Same kaam karta, bas syntax alag.
*   **strlen()**: String ki length pehle nikal sakte the aur uske basis pe loop chalate:

    ```c
    int len = strlen(s);
    for (int i = 0; i < len; i++)
    ```

    Lekin `\0` check karna faster hai kyunki `strlen` bhi internally loop chalata hai.

**Common Mistakes**:

* `\0` check bhool jana, jisse loop string ke bahar chala jata hai (undefined behavior).
* `i` ko galat increment karna, jaise `i--` likh dena.
* Loop condition galat likhna, jaise `s[i] != 0` (zero nahi, `\0` hota hai).

***

**5. Processing Characters**

```c
char ch = s[i];
```

**Kya hai ye?**

* `ch` ek variable hai jo current character store karta hai.
* `s[i]` se hum string ka `i`th character lete hain aur `ch` mein rakhte hain.

**Kyun use kiya?**

* `s[i]` ko bar bar likhne se code messy ho jata, aur `ch` use karna readable hai.
* Character ko alag variable mein store karke conditions check karna easier hai.

**Standard Syntax**:

* Variable assignment: `data_type variable_name = value;`
  * `char ch = s[i];` → `ch` mein `s[i]` ki value copy hoti hai.

**Alternatives kya the?**

*   `s[i]` directly use kar sakte the har condition mein, jaise:

    ```c
    if (s[i] == '(' || s[i] == '{' || s[i] == '[')
    ```

    Lekin ye code ko thoda repetitive banata.
* `char` ke bajaye `int` use kar sakte the, lekin `char` sufficient hai kyunki brackets single characters hain.

**Common Mistakes**:

* `ch` ko declare nahi karna aur directly use karna (undeclared variable error).
* Galat data type use karna, jaise `int ch` jab character chahiye.

***

**6. Check Opening Bracket**

```c
if (ch == '(' || ch == '{' || ch == '[') {
    stack[++top] = ch;
}
```

**Kya hai ye?**

* Ye condition check karta hai ki current character opening bracket hai ya nahi.
* Agar hai, toh usko stack mein push karte hain.
* `stack[++top] = ch`:
  * `++top`: Pehle `top` ko increment karo (e.g., -1 se 0).
  * `stack[top] = ch`: Us index pe character store karo.

**Kyun use kiya?**

* Opening brackets ko track karna zaroori hai kyunki closing brackets ko inke saath match karna hoga.
* Stack mein push karna isliye kiya kyunki stack ka LIFO order brackets ke nesting ke liye perfect hai.
* `++top` isliye kiya kyunki humein pehle top ko badhana hai, fir element daalna hai (pre-increment).

**Standard Syntax**:

*   `if` condition:

    ```c
    if (condition) {
        // Code
    }
    ```

    * `ch == '('`: Check karta hai ki `ch` equal hai `(` se.
    * `||`: Logical OR, matlab koi bhi condition true hone pe block execute hoga.
* Array assignment: `array_name[index] = value;`

**Alternatives kya the?**

*   **Switch Case**:

    ```c
    switch (ch) {
        case '(': case '{': case '[':
            stack[++top] = ch;
            break;
    }
    ```

    Thoda compact hota, lekin `if` zyada readable hai.
* **Post-increment**: `stack[top++] = ch` bhi likh sakte the, lekin logic change karna padta (e.g., `top` ko 0 se initialize karna).
*   **Separate Function**: Push operation ke liye alag function bana sakte the:

    ```c
    void push(char stack[], int *top, char ch) {
        stack[++(*top)] = ch;
    }
    ```

    Lekin chhote program ke liye zarurat nahi.

**Common Mistakes**:

* `top++` ke bajaye `top` likhna, jisse stack overwrite ho jata hai.
* Opening brackets galat check karna, jaise `ch == '{'` ke bajaye `ch == "{"` (double quotes string ke liye hote hain).
* Array ke bahar push karna (e.g., `top >= 10000`), jo segmentation fault dega.

***

**7. Check Closing Bracket**

```c
else if (ch == ')' || ch == '}' || ch == ']') {
    if (top == -1) {
        return false;
    }
    char last = stack[top--];
    if (ch == ')' && last != '(') return false;
    if (ch == '}' && last != '{') return false;
    if (ch == ']' && last != '[') return false;
}
```

**Kya hai ye?**

* Ye block closing brackets ke liye hai.
* Pehle check karta hai ki stack khali toh nahi (`top == -1`). Agar khali hai, matlab koi opening bracket nahi tha, toh invalid.
* `char last = stack[top--]`:
  * Stack ke top element ko `last` mein store karo.
  * `top--`: Top ko decrement karo (pop operation).
* Fir check karta hai ki closing bracket ka matching opening bracket hai ya nahi.

**Kyun use kiya?**

* Closing bracket ke liye check karna zaroori hai kyunki problem ka core hai brackets ka matching.
* Stack khali hone ka check isliye kiya kyunki agar closing bracket aaya aur koi opening bracket nahi hai, toh string invalid hai.
* Matching check (`ch == ')' && last != '('`) isliye kiya kyunki brackets ka type same hona chahiye.

**Standard Syntax**:

*   `else if`:

    ```c
    else if (condition) {
        // Code
    }
    ```

    * Pehle `if` ke false hone pe ye check hota hai.
* Logical AND (`&&`): Dono conditions true hone chahiye.
* Array access and decrement: `array_name[index--]`.

**Alternatives kya the?**

*   **Mapping Approach**: Ek array ya struct bana sakte the jo closing aur opening brackets map kare:

    ```c
    char map[256] = {0};
    map[')'] = '('; map['}'] = '{'; map[']'] = '[';
    if (map[ch] != last) return false;
    ```

    Ye compact hota, lekin thoda complex.
*   **Switch Case**:

    ```c
    switch (ch) {
        case ')': if (last != '(') return false; break;
        case '}': if (last != '{') return false; break;
        case ']': if (last != '[') return false; break;
    }
    ```

    Readable, lekin `if` statements simpler hain.
* **Early Exit**: Stack khali hone ka check loop ke shuru mein kar sakte the, lekin code ka flow bigad jata.

**Common Mistakes**:

* Stack khali check bhool jana, jisse `top == -1` pe array access karne se crash hota hai.
* Matching conditions galat likhna, jaise `ch == '('` ke bajaye `ch == ')'`.
* `top--` ke bajaye `top` likhna, jisse stack pop nahi hota.

***

**8. Final Check**

```c
return top == -1;
```

**Kya hai ye?**

* Loop ke baad, ye check karta hai ki stack khali hai ya nahi.
* `top == -1` true hoga agar stack khali hai, matlab sab brackets match ho gaye → `true` return.
* Agar stack khali nahi, matlab kuch opening brackets ka closing nahi mila → `false` return.

**Kyun use kiya?**

* Stack khali hona valid string ka final condition hai.
* `top == -1` simple aur direct check hai.

**Standard Syntax**:

* `return expression;`: Function se value return karta hai.
* Comparison: `variable == value`.

**Alternatives kya the?**

*   Explicit condition:

    ```c
    if (top == -1) return true;
    else return false;
    ```

    Lekin `return top == -1` chhota aur clear hai.
* `top <= -1` ya `top < 0` bhi likh sakte the, lekin `top == -1` exact hai.

**Common Mistakes**:

* `return` bhool jana, jisse function undefined behavior deta hai.
* Galat condition likhna, jaise `top == 0` (0 matlab ek element bacha hai).

***

**9. Main Function**

```c
int main() {
    char *test_cases[] = {"()", "()[]{}", "(]", "([])", "", "((()))", "([)]", "{"};
    int n = sizeof(test_cases) / sizeof(test_cases[0]);
    
    for (int i = 0; i < n; i++) {
        printf("Input: %s, Output: %s\n", test_cases[i], isValid(test_cases[i]) ? "true" : "false");
    }
    
    return 0;
}
```

**Kya hai ye?**

* `main` function program ka entry point hai. C program yahan se shuru hota hai.
* `test_cases` ek array hai jo test strings rakhta hai.
* `sizeof(test_cases) / sizeof(test_cases[0])` se array ki length nikalte hain.
* Loop chalake har test case ko `isValid` function mein bhejte hain aur result print karte hain.
* `return 0` batata hai ki program successfully chala.

**Kyun use kiya?**

* Test cases run karne ke liye `main` function zaroori hai.
* Array of strings (`char *test_cases[]`) isliye banaya kyunki multiple test cases ko ek jagah store karna tha.
* `printf` se results dikhaye kyunki humein output dekhna hai.
* `return 0` standard hai C mein successful execution ke liye.

**Standard Syntax**:

*   `main` function:

    ```c
    int main() {
        // Code
        return 0;
    }
    ```
* Array of strings: `char *array_name[] = {"string1", "string2", ...};`
* `sizeof`: Array ke size ko bytes mein deta hai.
* `printf` format: `printf("format_string", arg1, arg2, ...);`
  * `%s`: String ke liye.
  * : New line.

**Alternatives kya the?**

*   **Hardcoded Tests**: Test cases ko loop ke bajaye individually run kar sakte the:

    ```c
    printf("Input: %s, Output: %s\n", "()", isValid("()") ? "true" : "false");
    ```

    Lekin loop zyada scalable hai.
*   **Dynamic Input**: User se input lene ke liye `scanf` use kar sakte the:

    ```c
    char s[10000];
    scanf("%s", s);
    printf("%s\n", isValid(s) ? "true" : "false");
    ```

    Lekin test cases fixed the, toh array better tha.
* **Other Output Methods**: File mein output likh sakte the ya GUI use kar sakte the, lekin `printf` simplest hai.

**Common Mistakes**:

* `main` ke return type ko `void` karna (C mein `int` standard hai).
* `return 0` bhool jana, jo non-standard hai.
* `printf` mein format specifier galat use karna, jaise `%d` string ke liye.
* Array size calculate karte waqt galti, jaise `sizeof(test_cases)` directly use karna.

***

**10. Logic Explanation (Kyun Aisa Likha?)**

**Stack-Based Logic**:

* **Kyun Stack?**: Brackets ka order matter karta hai. Jaise, agar `([` hai, toh closing order `])` hona chahiye. Stack ka LIFO (Last In, First Out) ye guarantee karta hai ki last opening bracket pehle close hoga.
* **Kyun Array?**: C mein stack implement karne ka sabse simple tarika array hai. Linked list ya dynamic memory bhi use kar sakte the, lekin array fast aur straightforward hai.
* **Kyun Push/Pop?**: Opening brackets ko push kiya kyunki unko store karna tha. Closing brackets ke liye pop kiya kyunki latest opening bracket se match karna tha.
* **Kyun Top = -1?**: Stack khali hone ka clear indicator chahiye tha. `-1` standard hai jab array ka index 0 se start hota hai.

**Alternative Logics**:

*   **Counter Approach**: Har type ke bracket ke liye counter bana sakte the:

    ```c
    int paren = 0, curly = 0, square = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '(') paren++;
        else if (s[i] == ')') paren--;
        // Similar for {}/[]
        if (paren < 0 || curly < 0 || square < 0) return false;
    }
    return paren == 0 && curly == 0 && square == 0;
    ```

    Lekin ye nested brackets ke order ko nahi check karta, toh galat hai (e.g., `([)]` ko valid bol dega).
* **Recursive Approach**: String ko recursively parse kar sakte the, lekin complex aur slow hota.
* **Two-Pass Approach**: Pehle length check karte, fir order, lekin stack single pass mein sab solve kar deta hai.

**Kyun Ye Logic Best Hai?**

* **Efficiency**: O(n) time (ek loop) aur O(n) space (stack ke liye).
* **Simplicity**: Stack ka concept intuitive hai aur code clean hai.
* **Robustness**: Sab edge cases (empty string, single bracket, nested brackets) handle karta hai.

***

**11. Common Mistakes in This Problem**

* **Stack Overflow**: Array ka size chhota rakhna (e.g., `stack[10]`) jab input bada ho.
* **Segmentation Fault**: Stack khali hone ka check nahi karna aur `stack[-1]` access karna.
* **Mismatched Brackets**: Matching logic galat likhna, jaise `)` ke liye `[` check karna.
* **Missing Return**: Loop ke baad `return` bhool jana.
* **String Termination**: `\0` check nahi karna, jisse loop string ke bahar chala jata hai.
* **Uninitialized Variables**: `top` ko initialize nahi karna, jo garbage value deta hai.
* **Test Case Misses**: Edge cases (empty string, single bracket) test nahi karna.

***

**12. Test Results and Analysis**

**Output**:

```
Input: (), Output: true
Input: ()[]{}, Output: true
Input: (], Output: false
Input: ([]), Output: true
Input: , Output: true
Input: ((())), Output: true
Input: ([)], Output: false
Input: {, Output: false
```

**Kyun Aisa Output?**

* `"()"`: Ek pair, stack khali ho gaya → `true`.
* `"()[]{}"`: Teen pairs, sab match, stack khali → `true`.
* `"(]"`: Mismatch, `(` ka `]` nahi ho sakta → `false`.
* `"([])"`: Nested, sab match, stack khali → `true`.
* `""`: Khali string, koi bracket nahi, stack khali → `true`.
* `"((()))"`: Deep nesting, sab match → `true`.
* `"([)]"`: Galat nesting, `[` ka `)` pehle aaya → `false`.
* `"{`: Unclosed bracket, stack khali nahi → `false`.

***

**13. General Tips for Coding (Tujhe Aage Kaam Ayega)**

1. **Ek Line Samajh**: Har line ka matlab likh comment mein. Code ko chhote pieces mein tod.
2. **Paper Pe Solve**: Logic samajhne ke liye dry run kar. Stack ka flow paper pe bana.
3. **Errors Se Seekh**: C mein errors normal hain (segmentation fault, undefined behavior). Error message padh aur debug kar.
4. **Practice Simple Problems**: LeetCode, HackerRank pe Easy problems se shuru kar.
5. **Google Kar**: Syntax bhool jaye toh Google karna sharma nahi. Stack Overflow tera dost hai.
6. **Consistency**: Har din thoda code kar, dheere dheere expert ban jayega.

***
