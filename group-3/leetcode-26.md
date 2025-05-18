---
description: Remove Duplicates from Sorted Array
---

# Leetcode : 26

#### Problem Samajh Lo

Ye problem ek **sorted array** se duplicates hatane ka hai. Array sorted hai, matlab elements chhote se bade order mein hain (non-decreasing, yani equal values bhi ho sakte hain). Tujhe:

1. Array ko **in-place** modify karna hai, yani usi array mein changes karne hain, naye array nahi banane.
2. Har unique element ko ek baar rakhna hai, aur unka original order same rakhna hai.
3. Array ke first `k` elements mein unique elements hone chahiye, aur `k` return karna hai.
4. `k` ke baad ke elements ka koi matlab nahi (woh kuch bhi ho sakte hain).

**Examples**:

1. `nums = [1,1,2]` → Output: `k = 2`, `nums = [1,2,_]`
   * Unique elements: 1, 2. `k = 2` return karo, aur array ke pehle 2 elements 1 aur 2 honge.
2. `nums = [0,0,1,1,1,2,2,3,3,4]` → Output: `k = 5`, `nums = [0,1,2,3,4,_,_,_,_,_]`
   * Unique elements: 0, 1, 2, 3, 4. `k = 5`, array ke pehle 5 elements inhi honge.

**Constraints**:

* Array ki length: 1 se 3 \* 10^4 tak.
* Elements: -100 se 100 tak.
* Array sorted hai (non-decreasing order).

***

#### Array Ka Basic Concept

Bhai, pehle array samajh le kyunki ye problem array pe based hai:

* **Array** ek data structure hai jisme elements ek line mein store hote hain, ek ke baad ek.
* Har element ka **index** hota hai (0 se start), aur hum `array[index]` se element access karte hain.
* C mein array ka size fixed hota hai, aur memory contiguous (ek ke baad ek) hoti hai.
* **Example**: `int nums[] = {1, 1, 2};`
  * `nums[0] = 1`, `nums[1] = 1`, `nums[2] = 2`.
  * Size: 3 elements.

**In-Place** ka matlab:

* Tumhe array ke andar hi changes karne hain, naye array nahi banane.
* Extra space (jaise temporary array) use nahi karna chahiye, warna solution optimal nahi hoga.

***

#### Solution Idea (Logic in Hinglish)

Bhai, is problem ko solve karne ke liye hum **two-pointer technique** use karenge. Sorted array hai, toh duplicates ek ke baad ek honge. Logic ye hai:

1. Ek pointer (`write`) rakho jo unique elements ki position track karega.
2. Dusra pointer (`read`) array ke har element ko scan karega.
3. Jab bhi ek naya unique element mile, usko `write` position pe daal do aur `write` ko aage badhao.
4. Kyunki array sorted hai, hum previous unique element se compare kar sakte hain.
5. Last mein `write` ki value `k` hogi, jo unique elements ki count hai.

**Example Dry Run** (`nums = [0,0,1,1,1,2,2,3,3,4]`):

* Start: `write = 1`, `read = 1`, `nums = [0,0,1,1,1,2,2,3,3,4]`.
* Step 1: `read = 1`, `nums[1] = 0`, `nums[0] = 0` (same, skip).
* Step 2: `read = 2`, `nums[2] = 1`, `nums[0] != 1`, toh `nums[write] = 1`, `write++`.
  * \`nums = \[0,1,1,1,1,2,2,3,3警方
* Step 3: `read = 3`, `nums[3] = 1` (same as `nums[1]`, skip).
* Step 4: `read = 4`, `nums[4] = 1` (same, skip).
* Step 5: `read = 5`, `nums[5] = 2`, `nums[1] != 2`, toh `nums[write] = 2`, `write++`.
  * `nums = [0,1,2,1,1,2,2,3,3,4]`.
* Aise hi chalta hai, end mein: `nums = [0,1,2,3,4,2,2,3,3,4]`, `write = 5`.
* Return `k = 5`.

***

#### C Code

Ab code likhte hain, aur har line ko baad mein detail mein samjhaunga.

```c
#include <stdio.h>

// Function to remove duplicates
int removeDuplicates(int* nums, int numsSize) {
    // Edge case: agar array khali ya ek element
    if (numsSize <= 1) return numsSize;
    
    // Write pointer unique elements ke liye
    int write = 1;
    
    // Read pointer array scan karega
    for (int read = 1; read < numsSize; read++) {
        // Agar current element previous se different hai
        if (nums[read] != nums[write - 1]) {
            nums[write] = nums[read]; // Unique element ko write position pe daal do
            write++; // Write pointer aage badhao
        }
    }
    
    return write; // Unique elements ki count
}

// Helper function to print array (testing ke liye)
void printArray(int* nums, int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%d", nums[i]);
        if (i < size - 1) printf(",");
    }
    printf("]\n");
}

int main() {
    // Test Case 1
    int nums1[] = {1, 1, 2};
    int size1 = sizeof(nums1) / sizeof(nums1[0]);
    printf("Test Case 1:\nInput: ");
    printArray(nums1, size1);
    int k1 = removeDuplicates(nums1, size1);
    printf("Output: k = %d, nums = ", k1);
    printArray(nums1, k1);
    
    // Test Case 2
    int nums2[] = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int size2 = sizeof(nums2) / sizeof(nums2[0]);
    printf("\nTest Case 2:\nInput: ");
    printArray(nums2, size2);
    int k2 = removeDuplicates(nums2, size2);
    printf("Output: k = %d, nums = ", k2);
    printArray(nums2, k2);
    
    return 0;
}
```

***

#### Detailed Explanation (Har Cheez Break Down)

**1. Header Files**

```c
#include <stdio.h>
```

**Kya hai ye?**

* `<stdio.h>`: Input-output ke liye, `printf` function ke liye.

**Kyun use kiya?**

* Test cases ke input aur output print karne ke liye.

**Standard Syntax**:

* `#include <library_name.h>`

**Alternatives**:

* Koi alternative nahi tha kyunki `printf` ke liye `<stdio.h>` zaroori hai.
* Agar file mein output likhna hota, toh `<stdio.h>` mein `fprintf` use karte, lekin yahan console output kaafi tha.

**Common Mistakes**:

* `<stdio.h>` bhool jana aur `printf` use karna → Undeclared function error.
* Galat header likhna, jaise `stdlib.h` jab zarurat na ho.

***

**2. Function Definition**

```c
int removeDuplicates(int* nums, int numsSize)
```

**Kya hai ye?**

* Ye function array `nums` aur uska size `numsSize` leta hai, duplicates hatata hai, aur unique elements ki count `k` return karta hai.
* `int* nums`: Array ka pointer (C mein arrays pointers ke roop mein pass hote hain).
* `int numsSize`: Array ka size, kyunki C mein array pass karte waqt size nahi pata hota.
* `int` return type kyunki `k` (unique elements ki count) return karna hai.

**Kyun use kiya?**

* Problem ka core logic yahin implement hota hai.
* `int*` isliye kiya kyunki array in-place modify karna hai.
* `numsSize` zaroori hai kyunki array ke end tak jana hai.

**Standard Syntax**:

*   Function syntax:

    ```c
    return_type function_name(parameter_type param1, parameter_type param2) {
        // Code
    }
    ```

**Alternatives**:

* `void` function bana sakte the jo `k` ko pointer parameter mein return karta, lekin `int` return simpler hai.
* `nums` ko `int nums[]` likh sakte the, lekin `int*` same hai function parameters mein.

**Common Mistakes**:

* `numsSize` check nahi karna, jisse array ke bahar access ho sakta hai.
* Return type galat likhna, jaise `void` jab `int` chahiye.
* `return` statement bhool jana.

***

**3. Edge Case Check**

```c
if (numsSize <= 1) return numsSize;
```

**Kya hai ye?**

* Agar array khali hai (`numsSize = 0`) ya ek element hai (`numsSize = 1`), toh koi duplicates nahi honge, toh directly `numsSize` return karo.

**Kyun use kiya?**

* Edge cases handle karne ke liye:
  * Khali array: `k = 0`.
  * Single element: `k = 1`, koi duplicate nahi.
* Ye check se code robust banta hai.

**Standard Syntax**:

*   `if` condition:

    ```c
    if (condition) {
        // Code
    }
    ```
* `return value;`

**Alternatives**:

* Edge case ko loop ke andar handle kar sakte the, lekin alag check cleaner hai.
* `numsSize == 0` alag se check kar sakte the, lekin `<= 1` dono cases cover karta hai.

**Common Mistakes**:

* Edge case bhool jana, jisse empty array pe crash ho sakta hai.
* Galat condition likhna, jaise `numsSize < 1`.

***

**4. Write Pointer Initialization**

```c
int write = 1;
```

**Kya hai ye?**

* `write` ek pointer hai jo unique elements ki position track karta hai.
* `write = 1` isliye kiya kyunki pehla element (`nums[0]`) hamesha unique hota hai (kyunki koi previous element nahi hai).

**Kyun use kiya?**

* `write` batata hai ki agla unique element kahan daalna hai.
* Pehla element unique hai, toh `write` ko 1 se start kiya taaki dusre element se comparison shuru ho.

**Standard Syntax**:

* Variable initialization: `data_type variable_name = value;`

**Alternatives**:

* `write = 0` se start kar sakte the aur pehla element manually copy karte, lekin `write = 1` simpler hai kyunki pehla element already sahi jagah pe hai.
* `write` ke bajaye koi aur naam (e.g., `uniquePos`) use kar sakte the, lekin `write` descriptive hai.

**Common Mistakes**:

* `write` ko 0 se start karna aur extra copy karna, jo redundant hai.
* `write` initialize nahi karna, jisse garbage value aati hai.

***

**5. Main Loop**

```c
for (int read = 1; read < numsSize; read++) {
    if (nums[read] != nums[write - 1]) {
        nums[write] = nums[read];
        write++;
    }
}
```

**Kya hai ye?**

* `for` loop array ke elements ko scan karta hai, `read` pointer ke saath.
* `read = 1` se start kiya kyunki pehla element unique hai.
* `nums[read] != nums[write - 1]` check karta hai ki current element previous unique element se different hai.
* Agar different hai, toh `nums[write]` pe copy karo aur `write` increment karo.

**Kyun use kiya?**

* **Two-Pointer Technique**: `read` sab elements dekhta hai, aur `write` unique elements ki jagah track karta hai.
* `nums[write - 1]` se compare kiya kyunki `write - 1` last unique element ki position hai.
* In-place modification ke liye `nums[write] = nums[read]` kiya.

**Standard Syntax**:

*   `for` loop:

    ```c
    for (initialization; condition; update) {
        // Code
    }
    ```
* Array access: `array_name[index]`
* Comparison: `value1 != value2`

**Alternatives**:

*   **While Loop**:

    ```c
    int read = 1;
    while (read < numsSize) {
        if (nums[read] != nums[write - 1]) {
            nums[write] = nums[read];
            write++;
        }
        read++;
    }
    ```

    Same kaam, bas syntax alag.
* **Extra Array**: Ek temporary array mein unique elements store kar sakte the, lekin ye in-place nahi hota.
* `write` ke bajaye `nums[write - 1]` compare karne ke liye alag variable rakh sakte the, lekin zarurat nahi.

**Common Mistakes**:

* `read = 0` se start karna, jisse pehla element unnecessarily check hota hai.
* `nums[write]` ke bajaye `nums[read]` modify karna, jo logic bigad deta hai.
* `write++` bhool jana, jisse unique elements overwrite ho jate hain.
* `!=` ke bajaye `==` likhna, jo galat logic banata hai.

***

**6. Return Statement**

```c
return write;
```

**Kya hai ye?**

* `write` unique elements ki count hai, jo `k` ke roop mein return hota hai.

**Kyun use kiya?**

* Problem mein `k` return karna hai, aur `write` exactly wahi track karta hai.
* Loop ke baad `write` final count deta hai.

**Standard Syntax**:

* `return expression;`

**Alternatives**:

*   Explicit variable:

    ```c
    int k = write;
    return k;
    ```

    Lekin `return write` direct hai.
* `write - 1` return karna galat hota kyunki `write` hi count hai.

**Common Mistakes**:

* `return numsSize` karna, jo duplicates count karta hai.
* `return` bhool jana, jo undefined behavior deta hai.

***

**7. Helper Function (Testing ke Liye)**

```c
void printArray(int* nums, int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%d", nums[i]);
        if (i < size - 1) printf(",");
    }
    printf("]\n");
}
```

**Kya hai ye?**

* Array ko `[1,2,3]` format mein print karta hai testing ke liye.

**Kyun use kiya?**

* Input aur output visually dekhne ke liye.
* Test cases ke results verify karne ke liye.

**Standard Syntax**:

* Function definition: `void function_name(parameters)`
* `printf` format: `printf("format_string", args);`

**Alternatives**:

* Manual print statements test cases mein likh sakte the.
* Debugging ke liye breakpoints ya logging use kar sakte the.

**Common Mistakes**:

* `size - 1` check bhool jana, jisse extra comma print hota hai.
* `nums[i]` access karte waqt `size` check nahi karna, jo crash kar sakta hai.

***

**8. Main Function**

```c
int main() {
    // Test cases setup and execution
}
```

**Kya hai ye?**

* Test cases ke arrays banaye, `removeDuplicates` call kiya, aur results print kiye.
* `main` program ka entry point hai.

**Kyun use kiya?**

* Problem ke examples test karne ke liye.
* Output verify karne ke liye.

**Standard Syntax**:

* `int main() { return 0; }`
* Array initialization: `int array[] = {values};`
* Size calculation: `sizeof(array) / sizeof(array[0])`

**Alternatives**:

* User input se arrays banane ka code likh sakte the.
* Automated testing framework use kar sakte the.

**Common Mistakes**:

* `return 0` bhool jana.
* Array size galat calculate karna.
* Test cases mein edge cases miss karna.

***

**9. Common Mistakes in This Problem**

* **Array Bounds**: `numsSize` ke bahar array access karna.
* **Not In-Place**: Extra array use karna, jo problem ke against hai.
* **Order Change**: Elements ka original order bigad jana.
* **Edge Cases Miss**: Empty array, single element, ya all duplicates wale cases handle nahi karna.
* **Wrong Comparison**: `nums[read]` ko galat index se compare karna.
* **Write Pointer Issue**: `write` ko increment nahi karna ya galat initialize karna.

***

**10. Test Results**

Output:

```
Test Case 1:
Input: [1,1,2]
Output: k = 2, nums = [1,2]

Test Case 2:
Input: [0,0,1,1,1,2,2,3,3,4]
Output: k = 5, nums = [0,1,2,3,4]
```

**Kyun Aisa Output?**

* **Test Case 1**: `[1,1,2]` → Unique: `[1,2]`, `k = 2`.
* **Test Case 2**: `[0,0,1,1,1,2,2,3,3,4]` → Unique: `[0,1,2,3,4]`, `k = 5`.

***

**11. Logic Kyun Best Hai?**

* **Two-Pointer Technique**:
  * O(n) time complexity (ek loop).
  * O(1) space complexity (in-place, koi extra space nahi).
* **Simple aur Robust**: Edge cases (khali array, single element, all duplicates) handle karta hai.
* **Sorted Property Use**: Kyunki array sorted hai, previous element se compare karna kaafi hai.

**Alternative Logics**:

*   **Extra Array**: Unique elements ko naye array mein store karo, fir copy back:

    ```c
    int temp[30001];
    int k = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i == 0 || nums[i] != nums[i-1]) {
            temp[k++] = nums[i];
        }
    }
    for (int i = 0; i < k; i++) {
        nums[i] = temp[i];
    }
    return k;
    ```

    Lekin ye in-place nahi, aur extra O(n) space leta hai.
* **Set-Based**: Hash set mein unique elements store karo, lekin ye bhi extra space leta hai aur order maintain karna complex hai.
* **Sort Again**: Duplicates hatao aur fir sort karo, lekin problem mein already sorted array diya hai, toh redundant hai.

***

**12. General Tips for Array Problems**

1. **Bounds Check**: Hamesha array ke size ke andar raho, warna crash hoga.
2. **Dry Run**: Paper pe small examples ke saath logic test kar.
3. **In-Place Socho**: Extra space avoid karo jab in-place kaha ho.
4. **Edge Cases**: Empty array, single element, ya extreme values test kar.
5. **Practice**: Array-based problems (e.g., LeetCode Easy) solve kar.

***
