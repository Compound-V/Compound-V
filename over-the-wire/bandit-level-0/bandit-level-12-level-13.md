# Bandit Level 12 → Level 13

## Objective

The password for the next level is stored in the file `data.txt`. However, this file is not in a readable format. Instead, it is a **hexdump** of a file that has been **repeatedly compressed** using various formats such as **gzip**, **bzip2**, and **tar**. Your task is to **reverse the hexdump**, then **decompress/extract each layer step by step** until you reach a plain text file that contains the password.

***

### Step 1: Log into Bandit Level 12

1. Open a terminal.
2. Connect to Bandit Level 12 using SSH:

```bash
ssh bandit12@bandit.labs.overthewire.org -p 2220
```

3. When prompted, enter the password obtained from **Level 11 → Level 12**.

***

### Step 2: Create a Temporary Working Directory

Since your home directory is not writable, you must work in the `/tmp` directory.

1. Create a secure, temporary directory using `mktemp`:

```bash
mktemp -d
```

This will return something like:

```
/tmp/tmp.nRp7DowByY
```

2. Move into the new directory:

```bash
cd /tmp/tmp.nRp7DowByY
```

3. Copy the data file from your home directory:

```bash
cp ~/data.txt .
```

4. Rename the file for clarity:

```bash
mv data.txt data.hexdump
```

***

### Step 3: Reverse the Hexdump to Binary

The file `data.hexdump` is a **hexdump**, not actual binary data. To recover the original binary file:

```bash
xxd -r data.hexdump > data
```

Now `data` is a binary file. Check its type:

```bash
file data
```

Expected output (example):

```
data: gzip compressed data, was "data2.bin"
```

This tells us the file is compressed using **gzip**.

***

### Step 4: Decompress the First Layer (gzip)

1. Rename the file to add the `.gz` extension (this helps tools recognize it):

```bash
mv data data.gz
```

2. Decompress it:

```bash
gzip -d data.gz
```

Now the output file will again be named `data`.

3. Check the file type again:

```bash
file data
```

Expected output:

```
data: bzip2 compressed data
```

***

### Step 5: Decompress the Second Layer (bzip2)

1. Decompress the file using `bzip2`:

```bash
bzip2 -d data
```

If the decompressed file is named `data.out`, rename it back for clarity:

```bash
mv data.out data
```

2. Check the file type again:

```bash
file data
```

Expected output:

```
data: gzip compressed data
```

***

### Step 6: Decompress the Third Layer (gzip)

1. Rename and decompress:

```bash
mv data data.gz
gzip -d data.gz
```

2. Check the file type:

```bash
file data
```

Expected output:

```
data: POSIX tar archive
```

***

### Step 7: Extract the TAR Archive

1. Rename the file:

```bash
mv data data.tar
```

2. Extract its contents:

```bash
tar -xf data.tar
```

3. List files to see what was extracted:

```bash
ls
```

You will now see a new file, such as `data5.bin`. Continue to check and process this file.

***

### Step 8: Repeat Decompression Steps

For every new file:

1. Check its type:

```bash
file <filename>
```

2. Based on the result:

*   If it is `gzip compressed`, run:

    ```bash
    mv <file> <file>.gz
    gzip -d <file>.gz
    ```
*   If it is `bzip2 compressed`, run:

    ```bash
    bzip2 -d <file>
    ```
*   If it is a `tar archive`, run:

    ```bash
    mv <file> <file>.tar
    tar -xf <file>.tar
    ```

3. After extraction or decompression, continue checking and processing the next file.

<mark style="color:yellow;">Repeat this process several times, until you finally uncover a file that is identified as</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">`ASCII text`</mark><mark style="color:yellow;">.</mark>

***

### Step 9: Read the Final Output

Once the file is in plain text format:

```bash
file data
```

Output:

```
data: ASCII text
```

Now you can read it:

```bash
cat data
```

This will reveal the password for Bandit Level 13.

Example output:

```
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```

***

#### Step 10: Log into Bandit Level 13

Use the extracted password to log in:

```bash
ssh bandit13@bandit.labs.overthewire.org -p 2220
```

When prompted, enter the password you obtained from the `data` file.

***

### Conclusion

In this level, you worked with:

* **Hexdumps**, and learned how to convert them back into binary using `xxd`.
* **File detection** with the `file` command.
* **Multiple compression formats**: gzip, bzip2, tar.
* **Recursive decompression and extraction** to reach the final result.

This level tests your understanding of Linux command-line utilities and your ability to work through multiple layers of obfuscation to uncover hidden data.
