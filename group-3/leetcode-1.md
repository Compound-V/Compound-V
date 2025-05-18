---
description: Two Sums
---

# Leetcode : 1

## Two Sum Problem - Hinglish Detailed Notes

***

### 1. Problem Samjho (Problem Description)

Tumhe ek array `nums` diya hai jisme numbers hain, aur ek number `target` diya hai.

Kaam ye hai:

* Aise do **alag alag** numbers ke index do jo jod ke `target` banaate hain.
* Return karna hai un dono numbers ke **indices** (position).
* Guarantee hai ki aisa exact **ek hi solution** hai.
* Same element ko do baar use nahi kar sakte.
* Indices order se koi farak nahi padta.

**Example:**

```c
nums = [2, 7, 11, 15], target = 9
Output: [0, 1]   // kyunki nums[0] + nums[1] == 9 hai
```

***

### 2. Code ka Full Version (Simple Brute Force)

```c
#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {  
            if (nums[i] + nums[j] == target) {       
                int* result = malloc(2 * sizeof(int)); 
                result[0] = i;                         
                result[1] = j;                         
                *returnSize = 2;                      
                return result;                        
            }
        }
    }
    *returnSize = 0;  // agar koi pair nahi mila
    return NULL;      // NULL return karte hain jab answer nahi mile
}

int main() {
    int nums[] = {2, 7, 11, 15};  
    int target = 9;                
    int returnSize;               

    int* result = twoSum(nums, 4, target, &returnSize);

    if (result != NULL) {
        printf("Answer: [%d, %d]\n", result[0], result[1]);
        free(result);  // allocated memory free karna zaroori hai
    } else {
        printf("No valid input pairs.\n");
    }
    return 0;
}
```

***

### 3. Step-by-Step Explanation

#### 3.1 `#include <stdio.h>` aur `#include <stdlib.h>`

* `stdio.h` se hum `printf` jaisi functions use karte hain.
* `stdlib.h` se hum memory allocate karne ke liye `malloc` aur `free` functions use karte hain.

***

#### 3.2 Function Signature:

```c
int* twoSum(int* nums, int numsSize, int target, int* returnSize)
```

* `int*` matlab ye function ek integer pointer return karega (address jahan humare result ka array store hai).
* `int* nums` matlab ek pointer hai jo `nums` array ko point karta hai.
* `int numsSize` array ki length.
* `int target` wo number jiska hum sum dhoondh rahe hain.
* `int* returnSize` ek pointer hai jahan hum result ka size batayenge (usually 2 agar pair milta hai).

***

#### 3.3 Logic ke andar:

```c
for (int i = 0; i < numsSize; i++) {
    for (int j = i + 1; j < numsSize; j++) {
        if (nums[i] + nums[j] == target) {
```

* Pehla loop `i` ko har index pe le jaata hai.
* Doosra loop `j` ko `i + 1` se start karta hai taaki same element do baar na le.
* Check karte hain kya `nums[i] + nums[j] == target`?

Agar match milta hai toh:

```c
int* result = malloc(2 * sizeof(int));
result[0] = i;
result[1] = j;
*returnSize = 2;
return result;
```

* Hum heap memory mein 2 integer ke liye space allocate karte hain (kyunki hume 2 indices return karne hain).
* Indices store karte hain `result[0]` aur `result[1]`.
* `*returnSize` ko 2 set karte hain matlab do elements return ho rahe hain.
* Fir ye pointer return kar dete hain.

***

#### 3.4 Agar pair nahi mila:

```c
*returnSize = 0;
return NULL;
```

* `returnSize` ko zero karte hain, matlab koi valid pair nahi mila.
* NULL pointer return karte hain.

***

#### 3.5 `main()` Function

```c
int nums[] = {2, 7, 11, 15};
int target = 9;
int returnSize;

int* result = twoSum(nums, 4, target, &returnSize);
```

* Array aur target define karte hain.
* `twoSum` call karte hain.
* `&returnSize` se address pass karte hain taaki function size update kar sake.

***

#### 3.6 Result ko Print aur Memory free karna

```c
if (result != NULL) {
    printf("Answer: [%d, %d]\n", result[0], result[1]);
    free(result);  // Memory leak se bachne ke liye free karna zaroori
} else {
    printf("No valid input pairs.\n");
}
```

* Agar result NULL nahi, toh indices print karte hain.
* `free(result)` call karke dynamically allocated memory wapas release kar dete hain.

***

### 4. Important Concepts (Asaan Hindi/Hinglish Mein)

#### 4.1 Pointers kya hote hain?

* Pointer ek variable hota hai jo **memory address** ko store karta hai.
* `int* ptr` ka matlab `ptr` ek pointer hai jo integer ko point karta hai.
* Hum pointers se arrays, dynamic memory ko access karte hain.

***

#### 4.2 Dynamic Memory Allocation (malloc/free)

* `malloc` ka matlab "memory allocate karna" runtime pe, yani jab program chal raha ho.
* Static memory jese `int arr[10]` compile time pe fix ho jaata hai.
* Agar hume run-time pe size pata chalna ho tab `malloc` use karte hain.
* `malloc` ko allocate karne ke baad **hamare paas ek pointer aata hai** jise hum use kar sakte hain.
* Jab kaam ho jaata hai toh `free()` se memory release karna bahut important hai varna memory leak hoga.

***

#### 4.3 Static vs Dynamic Memory

| Static (Fixed) Array              | Dynamic Array (malloc)                    |
| --------------------------------- | ----------------------------------------- |
| Size compile time pe fix hota hai | Size runtime pe decide karte hain         |
| Memory stack pe allocate hoti hai | Memory heap pe allocate hoti hai          |
| Fast access                       | Thoda slow kyunki heap se access hoti hai |
| Limited size, compile time known  | Flexible size                             |

***

#### 4.4 Why Return Pointer?

* Hum function se 2 values (indices) return karna chahte hain.
* Simple int return karne se sirf ek value milegi.
* Isliye hum dynamically allocate karke pointer return karte hain jo array jaisa behave kare.

***

### 5. Code ka Flow (Logic stepwise)

1. `main()` call karta hai `twoSum`.
2. `twoSum` loop ke andar check karta hai har pair `(i, j)`.
3. Agar pair ka sum target ke barabar hai, toh dynamic memory allocate karke indices store karta hai.
4. Return karta hai result pointer.
5. Agar nahi mila, toh NULL return karta hai.
6. `main` check karta hai pointer, agar valid hai toh print karta hai.
7. `main` free karta hai allocated memory.

***

### 6. Mistakes Jo Avoid Karni Chahiye

* `malloc` ka return NULL hone par check nahi karna.
* `free` na karna memory leak banata hai.
* Function ke andar local array return karna (function ke bahar wo array exist nahi karega).
* Same element do baar use karna (isliye inner loop `j = i + 1` se start hota hai).
* Pointer misuse — NULL dereference ya invalid access.

***

### 7. Time Complexity

* Nested loop: O(n²) — matlab agar array mein 1000 elements hain toh 1,000,000 operations ho sakte hain.
* Simple aur asaan solution, lekin large inputs ke liye slow.

***

### 8. Agar Optimization karni ho?

* Use **hash map** (C mein hash table) — O(n) time complexity milega.
* Lekin hash map thoda advance topic hai.

***

### 9. Kuch Tips & Best Practices

* Har `malloc` ke baad `NULL` check karo.
* `free` karna mat bhoolo.
* Functions ko chhote aur specific rakho.
* Variables ka naam meaningfull rakho.
* Comment likhna mat bhoolo.

***

## Summary:

```markdown
# Two Sum Problem in C (Hinglish)

- Given array and target sum, find two indices whose values add up to target.
- Solution uses nested loops to check pairs.
- Returns dynamically allocated array of indices.
- Uses pointers, dynamic memory allocation (`malloc` and `free`).
- Code explained with stepwise flow and best practices.
- Time complexity: O(n²).
- Dynamic memory helps return arrays of variable size.
- Always free memory after use to avoid leaks.
```

***
