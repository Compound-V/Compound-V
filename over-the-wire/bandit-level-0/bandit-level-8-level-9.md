# Bandit Level 8 → Level 9

## Objective

The password for the next level is stored in the file **`data.txt`**, and it is the **only line of text that occurs only once**.

***

### **Step 1: Log into Bandit Level 8**

1. Open a terminal.
2.  Use SSH to connect to Bandit Level 8:

    ```sh
    ssh bandit8@bandit.labs.overthewire.org -p 2220
    ```
3. Enter the password obtained from **Level 7 → Level 8**.

***

### **Step 2: Explore the Directory**

Once logged in, check the available files:

```sh
ls
```

This will show a file named `data.txt`.

Check its contents:

```sh
cat data.txt
```

The file contains many repeated lines, but **only one line appears exactly once**—this is our target.

***

### **Step 3: Finding the Unique Line**

We can use the **`sort`** and **`uniq`** commands to filter out repeated lines and find the unique one.

#### **Best Approach**

```sh
sort data.txt | uniq -u
```

#### **Explanation:**

* `sort data.txt`: Sorts the lines alphabetically, grouping identical ones together.
* `uniq -u`: Prints only the lines that appear **exactly once** (removes duplicates).

The output will be the **password**.

***

### **Alternative Approaches**

#### **1. Using `sort | uniq -c` to Understand Data**

To see how many times each line appears:

```sh
sort data.txt | uniq -c
```

**Example Output:**

```
   10 abcdefg
    1 P@ssw0rd!
   15 qwerty123
   20 testline
```

The unique line (which appears only **once**) is our password:

```sh
P@ssw0rd!
```

Now, extract only that line:

```sh
sort data.txt | uniq -c | grep " 1 "
```

***

### **Step 4: Use the Password to Access Level 9**

Copy the password and move to the next level:

```sh
ssh bandit9@bandit.labs.overthewire.org -p 2220
```

When prompted, enter the password found in **`data.txt`**.

***

### **Conclusion**

* **Best command:** `sort data.txt | uniq -u`
* **Alternative for verification:** `sort data.txt | uniq -c | grep " 1 "`
* **Move to Level 9 using the extracted password.**
