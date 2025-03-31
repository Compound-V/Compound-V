# Bandit Level 4 → Level 5

## **Problem Statement**

The password for the next level is stored in the only human-readable file in the `inhere` directory.

### **Commands You May Need**

* `ls` – List files in a directory
* `cd` – Change directory
* `cat` – Read and display file contents
* `file` – Determine the type of a file
* `find` – Locate files and directories
* `du` – Display disk usage

***

### **Step 1: Log into Bandit Level 4**

Use the SSH command to connect to Bandit Level 4.

```bash
ssh bandit4@bandit.labs.overthewire.org -p 2220
```

Enter the password retrieved from Level 3 when prompted.

***

### **Step 2: Navigate to the `inhere` Directory**

Once logged in, list the files and directories in the home directory:

```bash
ls
```

Output:

```
inhere
```

Since `inhere` exists, navigate into it:

```bash
cd inhere
```

Now, list the files inside `inhere`:

```bash
ls
```

Output:

```
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
```

These filenames start with a `-`, which can cause issues when using commands like `cat`.

***

### **Step 3: Identify the Human-Readable File**

Since we need to find a human-readable file, we can use the `file` command.

```bash
file -- *
```

This command will check each file and display its type. The output will be something like:

```
-file00: data
-file01: data
-file02: data
-file03: data
-file04: data
-file05: data
-file06: data
-file07: ASCII text
-file08: data
-file09: data
```

The file `-file07` is identified as **ASCII text**, meaning it is human-readable.

***

### **Step 4: Read the Contents of the Human-Readable File**

Since the filename starts with a `-`, directly using `cat -file07` would result in an error. To correctly read the file, use one of the following approaches:

**Method 1: Use `--` to Stop Option Parsing**

```bash
cat -- -file07
```

**Method 2: Use `./` to Specify the Path**

```bash
file ./-file*
```

By using `./`, we explicitly reference the files in the current directory, avoiding issues with leading dashes.

**Method 3: Use `find` to Pass Filenames Safely**

```bash
find . -maxdepth 1 -type f -exec file {} +
```

This finds all files (`-type f`) in the current directory (`-maxdepth 1`) and runs `file` on them.

**Output:**

```
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
```

***

### **Alternative: Read All Files at Once**

If you want to check all files without opening them one by one, you can use:

```bash
cat -- *
```

However, this will print binary (unreadable) content for non-text files. To filter out only human-readable files, use:

```bash
file ./-file* | grep "ASCII text" | cut -d: -f1 | xargs cat
```

Explanation:

1. `file *` – Checks the type of each file.
2. `grep "ASCII text"` – Filters out human-readable files.
3. `cut -d: -f1` – Extracts the filenames.
4. `xargs cat` – Reads the filtered filenames using `cat`.

This command will print only the human-readable file's content, which includes the password.

***

### **Step 5: Log Out and Log into Bandit Level 5**

Exit the current session:

```bash
exit
```

Then, use the following SSH command to log into Bandit Level 5:

```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
```

Enter the retrieved password when prompted.

***

### **Key Takeaways**

1. **Filenames starting with `-` can cause issues**: Use `cat -- filename` or `cat ./filename` to read them safely.
2. **The `file` command helps differentiate file types**: It’s useful for identifying text files.
3. **Use automation to read multiple files**: The `file * | grep "ASCII text" | cut -d: -f1 | xargs cat` command can quickly locate and read only human-readable files.
4. **Understanding how to bypass common shell pitfalls**: Handling tricky filenames is a valuable skill for Linux-based security challenges.

***

You are now ready for Bandit Level 5.
