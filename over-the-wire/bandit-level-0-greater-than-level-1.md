# Bandit Level 0 -> Level 1

## **Problem Statement**

You need to retrieve the password for the next level. It is stored in a file named `readme` located in the **home directory**.

Once you have the password, use **SSH on port 2220** to log into the next level (`bandit1`).

***

## **Hints**

*   You may need the following commands:

    ```bash
    ls, cd, cat, file, du, find
    ```
* Keep a **local file** for passwords and solutions, as passwords are not stored automatically.
* Passwords **may change**, so keeping detailed **notes** helps when revisiting challenges.

***

## **Solution**

### **Step 1: SSH into Bandit Level 0**

Run the following command to log in:

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

* The password for **bandit0** is: `bandit0` (default).

***

### **Step 2: Locate the `readme` file**

After logging in, list the files in the **home directory**:

```bash
ls
```

This should display:

```plaintext
readme
```

***

### **Step 3: Read the password from the `readme` file**

Use the `cat` command to display its contents:

```bash
cat readme
```

This will output the **password** for `bandit1`.

Once the password is obtained, exit the current session using:

```bash
exit
```

Then, log in to `bandit1` using the retrieved password

> ### Troubleshooting
>
> #### Issue: Permission Denied
>
> **Error message:**
>
> ```
> Permission denied (publickey).
> ```
>
>
>
> **Solution:**\
> <mark style="color:yellow;">**This error occurs if an attempt is made to connect to**</mark><mark style="color:yellow;">**&#x20;**</mark><mark style="color:yellow;">**`bandit1`**</mark><mark style="color:yellow;">**&#x20;**</mark><mark style="color:yellow;">**while still inside the**</mark><mark style="color:yellow;">**&#x20;**</mark><mark style="color:yellow;">**`bandit0`**</mark><mark style="color:yellow;">**&#x20;**</mark><mark style="color:yellow;">**shell. Exit the current session using:**</mark>
>
> ```bash
> exit
> ```
>
> Then retry the `ssh` command from the **local terminal**.

***

### **Step 4: Log into Bandit Level 1**

Use the retrieved password to log into `bandit1`:

```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
```

When prompted, enter the **password** found in `readme`.

***

## **Key Takeaways**

Always **check the home directory** for relevant files.\
Use `ls`, `cat`, and `cd` to navigate and read files.\
Maintain a **local record** of passwords and solutions.

