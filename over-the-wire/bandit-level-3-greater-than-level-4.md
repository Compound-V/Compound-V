# Bandit Level 3 -> Level 4

## **Problem Statement**

The password for the next level is stored in a hidden file inside the `inhere` directory.

### **Commands You May Need**

* `ls` – List files in a directory
* `cd` – Change directory
* `cat` – Read and display file contents
* `file` – Determine the type of a file
* `du` – Display disk usage of files and directories
* `find` – Locate files and directories

***

### **Step 1: Log into Bandit Level 3**

Use the SSH command to connect to Bandit Level 3.

```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
```

When prompted, enter the password retrieved from the previous level.

***

### **Step 2: Identify the `inhere` Directory**

After logging in, list the files and directories in the home directory:

```bash
ls
```

Output:

```
inhere
```

The directory `inhere` exists, which means it may contain the hidden file mentioned in the level goal.

***

### **Step 3: Navigate to the `inhere` Directory**

Change into the `inhere` directory using:

```bash
cd inhere
```

Confirm the current directory using:

```bash
pwd
```

Output:

```
/home/bandit3/inhere
```

Now, list the files inside `inhere`:

```bash
ls
```

Output:

```
(no output)
```

This suggests that the file might be hidden.

***

### **Step 4: List Hidden Files**

Use the `-a` flag with `ls` to display hidden files:

```bash
ls -alh
```

Output:

```
total 12K
drwxr-xr-x 2 root    root    4.0K Sep 19  2024 .
drwxr-xr-x 3 root    root    4.0K Sep 19  2024 ..
-rw-r----- 1 bandit4 bandit3   33 Sep 19  2024 ...Hiding-From-You
```

The file named `...Hiding-From-You` is visible now. The multiple leading dots make it a hidden file.

***

### **Step 5: Read the File to Get the Password**

Use the `cat` command to read the file contents:

```bash
cat ...Hiding-From-You
```

Output:

```
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
```

This is the password for Bandit Level 4.

***

### **Step 6: Log Out and Log into Bandit Level 4**

Exit the current session:

```bash
exit
```

Then, use the following SSH command to log into Bandit Level 4:

```bash
ssh bandit4@bandit.labs.overthewire.org -p 2220
```

Enter the retrieved password when prompted.

***

### **Key Takeaways**

1. **Hidden files start with a dot (`.`)**: Regular `ls` commands do not show them. Use `ls -a` to display all files, including hidden ones.
2. **Using `ls -alh` is helpful**: It provides detailed information, including file permissions and sizes.
3. **Carefully handle filenames with special characters**: The file `...Hiding-From-You` had multiple dots, which could be misleading. Using `ls -a` was necessary to find it.
4. **Keep track of passwords**: Ensure you save each password securely to avoid repeating levels.

***

You are now ready for Bandit Level 4.
