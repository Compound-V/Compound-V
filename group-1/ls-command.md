# ls command

**`ls` — List Directory Contents**

**Syntax:** `ls [options] [directory]`

***

#### **Basic Usage**

1. **`ls`**: List all files and directories in the current directory.
2. **`ls -l`**: List with detailed information (permissions, ownership, file size).
3. **`ls -a`**: Show all files, including hidden files starting with `.`.
4. **`ls -R /home/user`**: List contents of a directory and all subdirectories recursively.
5. **`ls -lh`**: List files with human-readable file sizes (in KB, MB, GB).

***

#### **Combination Usage**

1. **`ls -l | grep "txt"`**: List all files and then search for `.txt` files.
2. **`ls -l /etc | less`**: Pipe the output to `less` for easier navigation when there are many files.
3. **`ls -al > output.txt`**: List all files and redirect the output to a file.

***

#### **Additional Options**

1. **`ls -t`**: Sort files by modification time (newest first).
   * Example: `ls -lt` (detailed list sorted by time).
   * Example: `ls -ltr` (reverse order, oldest first).
2. **`ls -S`**: Sort files by size (largest first).
   * Example: `ls -lS` (detailed list sorted by size).
3. **`ls -d */`**: List only directories.
   * Example: `ls -d */` (list directories in the current folder).
4. **`ls -1`**: List one file per line (useful for scripting).
   * Example: `ls -1`.
5. **`ls --color`**: Enable colored output (default on many systems).
   * Example: `ls --color=auto`.
6. **`ls -i`**: Show inode numbers of files.
   * Example: `ls -i`.
7. **`ls -m`**: List files separated by commas.
   * Example: `ls -m`.
8. **`ls -Q`**: Enclose file names in double quotes.
   * Example: `ls -Q`.
9. **`ls -X`**: Sort files by extension.
   * Example: `ls -lX`.
10. **`ls --group-directories-first`**: List directories before files.
    * Example: `ls --group-directories-first`.

***

#### **Advanced Combinations**

1.  **List files modified in the last 24 hours**:

    ```bash
    ls -l --time-style=+%s | awk -v now=$(date +%s) '{if (now - $6 < 86400) print}'
    ```
2.  **List files larger than 1MB**:

    ```bash
    ls -lh | awk '{if ($5 ~ /M/) print}'
    ```
3.  **Count the number of files in a directory**:

    ```bash
    ls -1 | wc -l
    ```
4.  **List files sorted by size in human-readable format**:

    ```bash
    ls -lhS
    ```
5.  **List files and exclude specific patterns**:

    ```bash
    ls | grep -v ".txt"
    ```
6.  **List files and display total size of the directory**:

    ```bash
    ls -lh | grep -v "^total"
    ```
7.  **List files and filter by permissions**:

    ```bash
    ls -l | grep "^drwx"  # List directories with read, write, and execute permissions for the owner.
    ```
8.  **List files and sort by last access time**:

    ```bash
    ls -lu
    ```
9.  **List files and sort by creation time** (if supported by the filesystem):

    ```bash
    ls -lc
    ```
10. **List files and show only specific columns (e.g., name and size)**:

    ```bash
    ls -lh | awk '{print $9, $5}'
    ```

***

#### **Practical Scripting Examples**

1.  **List all `.log` files and archive them**:

    ```bash
    tar -czvf logs.tar.gz $(ls *.log)
    ```
2.  **List all files and move them to a backup directory**:

    ```bash
    ls | xargs -I {} mv {} backup/
    ```
3.  **List all files and delete those older than 30 days**:

    ```bash
    find . -type f -mtime +30 -exec ls -l {} \;
    ```
4.  **List all files and change their permissions**:

    ```bash
    ls | xargs -I {} chmod 644 {}
    ```
5.  **List all files and count the number of lines in each file**:

    ```bash
    ls | xargs -I {} wc -l {}
    ```

***
