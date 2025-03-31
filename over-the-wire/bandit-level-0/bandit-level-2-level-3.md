# Bandit Level 2 → Level 3

## **Problem Statement**

The password for the next level is stored in a file named `spaces in this filename` located in the home directory.

### **Commands You May Need**

* `ls` – List files in a directory
* `cd` – Change directory
* `cat` – Read and display file contents
* `file` – Determine the type of a file
* `du` – Display disk usage of files and directories
* `find` – Locate files and directories

***

### **Step 1: Log into Bandit Level 2**

To begin, use the SSH command to log in to Bandit Level 2. Use the password obtained from Level 1.

```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
```

When prompted, enter the password retrieved from the previous level.

***

### **Step 2: List the Files in the Home Directory**

Once logged in, use the `ls` command to list the files in the home directory:

```bash
ls
```

Output:

```
spaces in this filename
```

The file we need is named `spaces in this filename`, which includes spaces in its name. This is important because spaces in filenames require special handling when used in the terminal.

***

### **Step 3: Handling Filenames with Spaces**

Files that contain spaces cannot be referenced directly without proper formatting. There are several ways to deal with filenames that contain spaces:

1.  **Use Escape Characters (`\`)**: Place a backslash (`\`) before each space:

    ```bash
    cat spaces\ in\ this\ filename
    ```
2.  **Use Quotation Marks (`""` or `''`)**: Enclose the filename in double or single quotes:

    ```bash
    cat "spaces in this filename"
    ```

    or

    ```bash
    cat 'spaces in this filename'
    ```
3.  **Use `./` Before the Filename**: This is useful when dealing with filenames that may cause confusion with commands:

    ```bash
    cat ./spaces\ in\ this\ filename
    ```

***

### **Step 4: Read the Password**

Using any of the above methods, execute the command:

```bash
cat "spaces in this filename"
```

Output:

```
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
```

This is the password for Bandit Level 3.

***

### **Step 5: Log Out and Log into Bandit Level 3**

Once the password is retrieved, log out using:

```bash
exit
```

Then, use the following SSH command to log into Bandit Level 3:

```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
```

Enter the password obtained in the previous step when prompted.

***

### **Key Takeaways**

1. **Filenames with spaces require special handling**:
   * Use backslashes (`\`) to escape spaces.
   * Use double (`""`) or single (`''`) quotes around the filename.
   * Prefix the filename with `./` to avoid confusion with commands.
2. **Always list files first**: Before interacting with files, use `ls` to check for hidden files, special characters, or unusual filenames.
3. **Keep a record of passwords**: Since passwords are required to progress, maintaining a local text file with passwords for each level is recommended.

***

By following these steps, you should now be successfully logged into Bandit Level 3, ready for the next challenge.
