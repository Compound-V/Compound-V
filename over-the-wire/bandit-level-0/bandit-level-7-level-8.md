# Bandit Level 7 → Level 8

## Objective

The password for the next level is stored in the file **`data.txt`**, **next to the word `millionth`**.

***

### **Step 1: Log into Bandit Level 7**

1. Open a terminal.
2.  Use SSH to connect to Bandit Level 7:

    ```sh
    ssh bandit7@bandit.labs.overthewire.org -p 2220
    ```
3. Enter the password obtained from **Level 6 → Level 7**.

***

### **Step 2: Explore the Directory**

Once logged in, check the available files:

```sh
ls
```

This will show a file named `data.txt`, which contains the required password.

***

### **Step 3: Understanding the Problem**

Since the password is **next to the word `millionth`**, we need to search for this keyword in `data.txt`.

***

### **Step 4: Extracting the Password**

The **`grep`** command is the best choice for finding a specific word in a file. Run:

```sh
grep "millionth" data.txt
```

#### **Explanation:**

* `grep` searches for the keyword `"millionth"` inside `data.txt`.
* It returns the **entire line** that contains this word.
* The password will be **next to the word `millionth`** in the output.

**Expected Output:**

```
millionth    [PASSWORD]
```

***

### **Alternative Approaches**

#### **1. Using `sort` Before `grep` (Unnecessary but Works)**

You used:

```sh
sort data.txt | grep millionth
```

This works but is **not needed**, as `grep` alone is sufficient. Sorting is useful when filtering duplicates but doesn't add much here.

***

### **Step 5: Use the Password to Access Level 8**

Copy the password and move to the next level:

```sh
ssh bandit8@bandit.labs.overthewire.org -p 2220
```

When prompted, enter the password found in **`data.txt`**.

***

### **Conclusion**

* **Best approach:** Use `grep "millionth" data.txt` to extract the password directly.
* **Your approach (`sort data.txt | grep millionth`) also worked**, but `sort` is unnecessary.
* **Move to Level 8 using the extracted password.**
