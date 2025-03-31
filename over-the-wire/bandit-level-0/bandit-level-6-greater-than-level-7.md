# Bandit Level 6 -> Level 7

## **Objective**

The goal of this level is to locate the password for **Bandit Level 7**. The password is stored in a file somewhere on the system, with the following attributes:

1. **Owned by user** `bandit7`
2. **Owned by group** `bandit6`
3. **Exactly 33 bytes in size**

Since the file is located somewhere on the server, we must efficiently search for it.

***

### **Step 1: Logging into Bandit Level 6**

To begin, establish an SSH connection to the Bandit server using the credentials from the previous level.

```sh
ssh bandit6@bandit.labs.overthewire.org -p 2220
```

When prompted, enter the password obtained from **Level 5 → Level 6**.

***

### **Step 2: Locating the Password File**

The password file can be found using the `find` command, which allows us to filter files based on specific attributes.

#### **Executing the `find` Command**

Run the following command to search for a file that meets all the given conditions:

```sh
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

#### **Explanation of the Command:**

* `/` → Starts searching from the **root directory** to ensure no locations are skipped.
* `-type f` → Searches for **files only**, excluding directories.
* `-user bandit7` → Filters results to show only files **owned by user `bandit7`**.
* `-group bandit6` → Further filters results to show only files **owned by group `bandit6`**.
* `-size 33c` → Matches files that are **exactly 33 bytes** in size (`c` stands for bytes).
* `2>/dev/null` → Redirects error messages (such as "Permission Denied") to `/dev/null` to keep the output clean.

#### **Command Output:**

After executing the command, the system returns multiple "Permission Denied" errors for restricted directories. However, it successfully finds the target file:

```
/var/lib/dpkg/info/bandit7.password
```

This confirms the location of the password file.

***

### **Step 3: Extracting the Password**

Now that the file has been identified, use the `cat` command to display its contents:

```sh
cat /var/lib/dpkg/info/bandit7.password
```

#### **Command Output:**

```
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
```

<mark style="color:yellow;">This is the password for</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">**Bandit Level 7**</mark><mark style="color:yellow;">.</mark>

***

#### **Alternative Approach: Using `grep`**

Another way to check for the password is by using the `grep` command. However, in this case, `grep` is unnecessary because we already have the file path.

If we wanted to confirm the file’s existence using `grep`, we could have used:

```sh
grep bandit7 /var/lib/dpkg/info/*
```

This would list all files in `/var/lib/dpkg/info/` that contain the word "bandit7", potentially revealing the password file.

***

### **Step 4: Logging into Bandit Level 7**

With the obtained password, proceed to log into **Bandit Level 7**:

```sh
ssh bandit7@bandit.labs.overthewire.org -p 2220
```

When prompted, enter the password retrieved from the file.

***

### **Conclusion**

#### **Most Efficient Solution:**

1.  Use `find` to locate the password file:

    ```sh
    find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
    ```
2.  Display the password using `cat`:

    ```sh
    cat /var/lib/dpkg/info/bandit7.password
    ```
3. Use the retrieved password to log into Bandit Level 7.

This approach ensures an efficient and precise search while avoiding unnecessary manual exploration.
