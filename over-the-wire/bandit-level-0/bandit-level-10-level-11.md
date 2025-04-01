# Bandit Level 10 → Level 11

## Objective

The password for the next level is stored in the file **`data.txt`**, which contains **Base64 encoded data**.

***

### **Step 1: Log into Bandit Level 10**

1. Open a terminal.
2.  Use SSH to connect to Bandit Level 10:

    ```sh
    ssh bandit10@bandit.labs.overthewire.org -p 2220
    ```
3. Enter the password obtained from **Level 9 → Level 10**.

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

Example output (Base64 encoded text):

```
VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==
```

This indicates that the data is **Base64 encoded**.

***

### **Step 3: Decode the Base64 Data**

Since `data.txt` is encoded in **Base64**, use the `base64` command to decode it:

```sh
base64 -d data.txt
```

or

```sh
cat data.txt | base64 --decode
```

Example output:

```
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```

The password for **Level 11** is:

```
dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```

***

### **Step 4: Log into Bandit Level 11**

Use the extracted password to log into **Bandit Level 11**:

```sh
ssh bandit11@bandit.labs.overthewire.org -p 2220
```

When prompted, enter the **password obtained from `data.txt`**.

***

### **Conclusion**

*   **Best command to decode Base64 data:**

    ```sh
    base64 -d data.txt
    ```
*   **Alternative command:**

    ```sh
    cat data.txt | base64 --decode
    ```
* **Extract the password and use it to log in to Level 11.**
