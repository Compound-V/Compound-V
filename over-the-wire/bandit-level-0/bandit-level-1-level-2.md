# Bandit Level 1 → Level 2

## **Problem Statement**

The password for the next level is stored in a file named `-` (just a single hyphen) located in the home directory.\
Our goal is to retrieve this password and use it to log into `bandit2` via SSH on port `2220`.

***

### **Prerequisites**

Before continuing, make sure you are familiar with these basic Linux commands:

| **Command** | **Description**                                     |
| ----------- | --------------------------------------------------- |
| `ls`        | Lists files and directories in the current location |
| `cat`       | Displays the contents of a file                     |
| `file`      | Identifies file types                               |
| `cd`        | Changes directories                                 |
| `find`      | Searches for files based on name and properties     |
| `du`        | Checks file sizes                                   |

***

### **Step 1: SSH into Bandit Level 1**

To log into Bandit Level 1, run the following command from your local terminal:

```sh
ssh bandit1@bandit.labs.overthewire.org -p 2220
```

* **Explanation:**
  * `ssh` → Secure Shell, used to log into remote machines.
  * `bandit1@bandit.labs.overthewire.org` → Username (`bandit1`) and the remote server address.
  * `-p 2220` → Specifies port `2220`, as Bandit uses a non-standard port for SSH.
* **When prompted, enter the password you retrieved from Bandit Level 0.**
  * If you successfully log in, you will see a welcome message.

***

### **Step 2: List the Files in the Home Directory**

After logging in, check what files are available:

```sh
ls
```

You will see the following output:

```
-
```

This means there is a file named `-` in the home directory.

***

### **Step 3: Why Can’t We Use `cat -`?**

Normally, we use `cat filename` to display a file’s contents. However, running:

```sh
cat -
```

**will not work** because:

* In Linux, `-` is a special character that often represents **standard input**.
* Instead of reading the file, `cat -` waits for you to type something.
* To exit this, press **Ctrl + C**.

***

### **Step 4: Correct Way to Read the File**

To correctly read the file, we need to specify its full path. We can use:

```sh
cat ./-
```

* **Explanation:**
  * `./` tells the system to look for `-` in the current directory.
  * This bypasses the issue where `-` is interpreted as standard input.
*   **Expected Output:**

    ```
    h4ckTh3C0d3!
    ```

    (This is just a placeholder. The actual password will be different.)

***

### **Step 5: Save the Password**

Make sure to **copy the password** from the output. You’ll need it to log into Bandit Level 2.

***

### **Step 6: Exit From Bandit Level 1**

Now that we have the password, **exit** the current session:

```sh
exit
```

This will return you to your local terminal.

***

### **Step 7: Log into Bandit Level 2**

Use the password retrieved from the previous step to log into Bandit Level 2:

```sh
ssh bandit2@bandit.labs.overthewire.org -p 2220
```

When prompted, **paste the password** and press **Enter**.

If successful, you are now in Bandit Level 2! 🎉

***

### **Troubleshooting**

#### **1. Getting "Permission Denied (publickey)" Error**

**Issue:**

```
Permission denied (publickey).
```

**Solution:**

* Ensure you're logging in **from your local machine**, not inside an existing SSH session.
* Run `exit` to close any existing session before retrying the SSH command.

***

#### **2. Getting Stuck with `cat -`**

**Issue:**\
If you mistakenly type `cat -`, the terminal will seem stuck.\
**Solution:**\
Press **Ctrl + C** to cancel and return to the normal command prompt.

***

### **Key Takeaways**

**Files with special characters (like `-`) can cause issues**

* Use `./-` instead of `cat -` to correctly read the file.

**Always check the home directory (`ls`) for important files**

* Many Bandit levels place passwords in hidden or oddly named files.

**Keep a record of passwords and solutions**

* You’ll need them to log into the next level.

***

This concludes **Bandit Level 1 → Level 2**. Let me know if you want the walkthrough for the next level! 🚀
