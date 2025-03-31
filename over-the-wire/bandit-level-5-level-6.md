# Bandit Level 5 → Level 6

## **Problem Statement -**

The password for the next level is stored in a file somewhere under the `inhere` directory and has all of the following properties:

* It is **human-readable**
* It is **1033 bytes in size**
* It is **not executable**

### **Commands You May Need**

* `ls` – List files in a directory
* `cd` – Change directory
* `cat` – Read and display file contents
* `file` – Determine the type of a file
* `find` – Locate files and directories
* `du` – Display disk usage

### **Solution**

### **Step 1: Listing Directory Contents**

After logging into Bandit Level 5, navigate to the `inhere` directory:

```sh
cd inhere
```

List the contents of the directory to see its structure:

```sh
ls -alhR
```

This will show multiple subdirectories (`maybehere00` to `maybehere19`), each containing files.

### **Step 2: Finding the Target File**

Since the file has specific attributes (1033 bytes, human-readable, and non-executable), use the `find` command to search for it.

**Best Approach (Using find with exact filters)**

```sh
find . -type f -size 1033c ! -executable
```

* `.` → Search in the current directory (`inhere`) and its subdirectories
* `-type f` → Look for files only
* `-size 1033c` → Find files that are **1033 bytes**
* `! -executable` → Exclude executable files

This command will return the path to the file containing the password.

### **Step 3: Reading the Password**

Once the file is found, use `cat` to display its content:

```sh
cat ./maybehereXX/filename
```

(Replace `maybehereXX/filename` with the actual file path found in the previous step.)

The output will be the password for the next level.

### <mark style="color:orange;">**Alternative Approaches (Optimized Find Command with Output Processing)**</mark>

An expert would optimize the `find` command with `xargs` or `exec`:

```sh
find . -type f -size 1033c ! -executable -exec cat {} +
```

This immediately finds and prints the password without needing manual intervention.

### <mark style="color:yellow;">File Types in Linux</mark>

> Here’s a **detailed comparison** of different file naming conventions in Linux and how they behave:

| **File Type**                                          | **Example**                           | **Behavior**                                          | **Issue**                                                      | **Solution**                                            |
| ------------------------------------------------------ | ------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------- |
| **Normal file**                                        | `file2`                               | Standard file, no special rules                       | No issue                                                       | `cat file2`                                             |
| **Hidden file**                                        | `.file2`                              | Starts with `.` and is hidden by default              | Not shown in normal `ls` output                                | Use `ls -a` to list, `cat .file2` to view               |
| **File starting with `-`**                             | `-file2`                              | Treated as a **command option** instead of a filename | `cat -file2` fails because `-file2` looks like an option       | Use `cat ./-file2` or `cat -- -file2`                   |
| **File with spaces**                                   | `my file.txt`                         | Space splits filename into two arguments              | `cat my file.txt` treats `my` and `file.txt` as separate files | Use `cat "my file.txt"` or `cat my\ file.txt`           |
| **File with special characters (`$`, `@`, `&`, etc.)** | `file$1`, `file@name`                 | Symbols like `$` may be interpreted by the shell      | `$` may be treated as a variable                               | Use `cat "file$1"` or `cat 'file@name'`                 |
| **File with newlines in the name**                     | `file↵name` (newline inside filename) | The filename includes an actual newline character     | Causes confusion in scripts and commands                       | Use `ls -b` to see special characters, rename with `mv` |
| **File with only spaces (`" "`)**                      | `" "`                                 | Looks like an empty filename                          | Hard to reference manually                                     | Use `ls -b` to find, access with `cat "./ "`            |
| **File with a trailing space**                         | `"file2 "`                            | Extra space at the end                                | Can be mistaken for another file                               | Reference it using `cat "file2 "`                       |

> This table provides a **quick reference** for handling different types of filenames in Linux!

### **Conclusion**

The most efficient method is using `find` with exact filters to quickly locate the file and `cat` to display the password.
