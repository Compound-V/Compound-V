# Bandit Level 11 → Level 12

## Objective

The password for the next level is stored in **`data.txt`**, where all **lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions** (ROT13 encryption).

***

### **Step 1: Log into Bandit Level 11**

1. Open a terminal.
2.  Connect to Bandit Level 11 using SSH:

    ```sh
    ssh bandit11@bandit.labs.overthewire.org -p 2220
    ```
3. Enter the password obtained from **Level 10 → Level 11**.

***

### **Step 2: Check the File**

List the available files:

```sh
ls
```

You'll see **`data.txt`**.

Check its contents:

```sh
cat data.txt
```

Example output (ROT13 encrypted text):

```
Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4
```

This text is encoded using **ROT13**, meaning every letter is shifted **13 places forward** in the alphabet.

***

### **Step 3: Decode ROT13 using the `tr` Command**

Use the `tr` (translate) command to decode the text:

```sh
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

Explanation:

* `'A-Za-z'` matches all **uppercase and lowercase** letters.
* `'N-ZA-Mn-za-m'` shifts them **back 13 positions**, effectively decoding ROT13.

#### **Example Output**

```
The password is 7x16WNeIHi5YkIhWsfFIqoonGTyj9Q4
```

Now, the password for **Level 12** is:

```
7x16WNeIHi5YkIhWsfFIqoonGTyj9Q4
```

***

### **Step 4: Log into Bandit Level 12**

Use the extracted password to log into **Bandit Level 12**:

```sh
ssh bandit12@bandit.labs.overthewire.org -p 2220
```

When prompted, enter the **password obtained from `data.txt`**.

***

### **Conclusion**

* **ROT13 is a simple substitution cipher** where each letter is shifted by **13 places**.
*   **Best command to decode ROT13:**

    ```sh
    cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
    ```
* **Extract the password and use it to log in to Level 12.**
