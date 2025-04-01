# Bandit Level 9 → Level 10

## Objective

The password for the next level is stored in the file **`data.txt`**, and it is one of the few **human-readable strings**, **preceded by several `=` characters**.

***

### **Step 1: Log into Bandit Level 9**

1. Open a terminal.
2.  Use SSH to connect to Bandit Level 9:

    ```sh
    ssh bandit9@bandit.labs.overthewire.org -p 2220
    ```
3. Enter the password obtained from **Level 8 → Level 9**.

***

### **Step 2: Explore the Directory**

Check the available files:

```sh
ls
```

This will show `data.txt`.

Check its contents:

```sh
cat data.txt
```

However, this file contains **mostly unreadable characters**, making `cat` not very useful.

***

### **Step 3: Extract Human-Readable Text**

Since `data.txt` has mostly binary or unreadable data, we can use the **`strings`** command to extract human-readable text:

```sh
strings data.txt
```

This will display all readable strings in the file.

***

### **Step 4: Filter the Password**

Since the password is **preceded by several `=` characters**, we can use `grep` to extract the relevant line:

```sh
strings data.txt | grep "=========="
```

This command:

* Extracts human-readable text (`strings data.txt`).
* Searches for lines containing `==========` (`grep "=========="`).

***

### **Step 5: Extracting the Password**

The output should look something like this:

```
========== the
========== passwordi
========== is
========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```

The password is the last word in this sequence:

```
FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```

***

### **Step 6: Move to the Next Level**

Use the password to log into Bandit Level 10:

```sh
ssh bandit10@bandit.labs.overthewire.org -p 2220
```

When prompted, enter the extracted password.

***

### **Conclusion**

*   **Best command to find the password:**

    ```sh
    strings data.txt | grep "=========="
    ```
* **Alternative:** Manually inspect `strings data.txt` output.
* **Use the extracted password to move to Level 10.**
