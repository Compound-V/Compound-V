# Find Command

## `find` Command: Complete Guide in Hinglish

Yeh document `find` command ka ek poora guide hai jo Linux/Unix systems mein files aur directories dhoondhne ke liye use hota hai. Isme hum `find` ke basics, syntax, options, operators, aur real-world examples cover karenge. Yeh guide beginners se lekar advanced users tak ke liye banaya gaya hai, aur isse online GitBook ya documentation ke liye use kar sakte ho.

### **`find` Command Kya Hai?**

`find` ek powerful command-line tool hai jo files aur directories ko recursively (yani folder ke andar ke folders aur files tak) dhoondhta hai. Tum isse bol sakte ho ki kaunsi files dhoondhni hain based on:

* File ka naam
* Size
* Type (file, directory, symbolic link, etc.)
* Permissions
* Modification ya access time
* User ya group ownership, aur bhi bohot kuch!

**Basic Syntax**:

```bash
find [path...] [options/conditions] [actions]
```

* **path**: Kahan dhoondhna hai, jaise `.` (current directory), `/home`, ya `/`.
* **options/conditions**: Filters jo batate hain ki kaunsi files match karni hain, jaise `-name`, `-size`, `-type`.
* **actions**: Found files ke saath kya karna hai, jaise `-print`, `-exec`, `-delete`.

**Note**: Agar koi action nahi diya, toh default action `-print` hota hai, jo matched files ke paths print karta hai.

### **Kaise Kaam Karta Hai?**

1. **Recursive Search**: `find` ek path se shuru karta hai aur uske andar ke saare sub-directories aur files ko check karta hai.
2. **Conditions**: Tum conditions dete ho, jaise `-name "*.txt"` ya `-size +100k`, jo decide karti hain ki kaunsi files match hongi.
3. **Symbolic Links Handling**:
   * `-H`: Command line mein diya gaya symbolic link uski actual file ke details dekhega.
   * `-L`: Har symbolic link (command line ya traversal mein) uski actual file ke details dekhega.
   * Agar dono nahi diya, toh symbolic link ke khud ke details dekhega.
4. **Infinite Loop Protection**: Agar koi directory loop mein aa jata hai (jaise symbolic link ke wajah se), `find` usse detect karta hai aur error message deta hai ya continue karta hai.

### **Important Options aur Primaries**

Yeh kuch main filters ya conditions hain jo `find` ke saath use hote hain:

1. **`-name pattern`**: File ka naam match karta hai (wildcards jaise `*`, `?` use kar sakte ho).
   * Example: `find . -name "*.txt"` – saari `.txt` files.
2. **`-iname pattern`**: Case-insensitive naam match karta hai.
   * Example: `find . -iname "readme*"` – `README`, `readme`, `ReadMe` sab match karega.
3. **`-path pattern`**: Poora path match karta hai.
   * Example: `find / -path "/home/user/docs/*.txt"`.
4. **`-type c`**: File type specify karta hai:
   * `f`: Regular file
   * `d`: Directory
   * `l`: Symbolic link
   * `b`: Block device
   * `c`: Character device
   * `p`: FIFO (named pipe)
   * `s`: Socket
   * Example: `find . -type f` – sirf files.
5. **`-size n[unit]`**: File ka size check karta hai.
   * Units: `c` (bytes), `k` (KB), `M` (MB), `G` (GB).
   * Example: `find . -size +10M` – 10 MB se badi files.
6. **`-perm mode`**: File permissions match karta hai.
   * Example: `find . -perm 644` – 644 permissions wali files.
   * `-perm -644`: Kam se kam 644 permissions.
7. **`-mtime n`**: Files jo last `n` days mein modified hui hain.
   * `+n`: n days se zyada purani.
   * `-n`: n days se kam purani.
   * Example: `find . -mtime -7` – last 7 din mein modified files.
8. **`-atime n`**: Files jo last `n` days mein accessed hui hain.
9. **`-ctime n`**: Files jinka status last `n` days mein change hua.
10. **`-user uname`**: Specific user ki files.
    * Example: `find /home -user john`.
11. **`-group gname`**: Specific group ki files.
12. **`-nouser` / `-nogroup`**: Files jo kisi valid user ya group se nahi hain.
13. **`-newer file`**: Files jo given file se recently modified hain.
    * Example: `find . -newer ref.txt`.
14. **`-exec command {} \;`**: Found files pe command run karta hai.
    * Example: `find . -name "*.bak" -exec rm {} \;` – `.bak` files delete karega.
15. **`-exec command {} +`**: Multiple files ko ek saath process karta hai (faster).
    * Example: `find . -name "*.jpg" -exec mv {} ../images/ +`.
16. **`-ok command {} \;`**: `-exec` jaisa, lekin har file ke liye confirmation maangta hai.
17. **`-prune`**: Specific directories ko skip karta hai.
    * Example: `find . -path "./temp" -prune -o -print`.
18. **`-depth`**: Directory ke contents ko pehle process karta hai, fir directory ko.
19. **`-xdev`**: Dusre filesystems (jaise mounted drives) mein nahi jata.

### **Operators for Combining Conditions**

Tum conditions ko combine kar sakte ho in operators ke saath:

* **`( expr )`**: Expressions ko group karta hai.
* **`! expr`**: Negation (NOT). Example: `find . ! -name "*.txt"` – non-text files.
* **`expr1 -a expr2`**: AND operation (default hota hai agar `-a` nahi likha).
* **`expr1 -o expr2`**: OR operation.
* **Precedence**: `( )` > `!` > `-a` > `-o`.



## `find` Command: 45 Practical Test Cases in Hinglish

Bhai, `find` command Linux/Unix ka ek super powerful tool hai jo files aur directories ko dhoondhne ke liye use hota hai. Chahe tu specific naam wali files dhoondhna chahe, badi size wali files, ya recently modified files, `find` sab kuch kar sakta hai. Is section mein hum 45 practical test cases cover karenge, jo real-world scenarios ke liye banaye gaye hain. Har test case mein hum clearly batayenge ki **Goal kya hai**, **Logic/Approach kya hai**, **Command kaunsa use karna hai**, **Output kaisa dikhega**, aur **Kya Hua** is command se. Yeh Hinglish mein hai taaki beginners bhi easily samajh sakein aur pros ke liye bhi detailed ho. 😎

***

### **Test Cases (1-45)**

#### 1. **Saari Files aur Directories List Karo**

* **Goal**: Current directory ke saare files aur folders ke details (permissions, size, timestamp) dekhna.
* **Logic/Approach**: `find` ko current directory (`.`) se shuru karenge, koi filter nahi lagayenge, aur `-exec ls -l` se detailed output lenge.
*   **Command**:

    ```bash
    find . -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 ./file1.txt
    drwxr-xr-x 2 user user 4096 Jul 10 2025 ./folder1
    -rw-r--r-- 1 user user 2048 Jul 10 2025 ./folder1/file2.txt
    ```
* **Kya Hua**: Yeh command current directory ke saare files aur folders ke paths aur details (permissions, size, timestamp) dikhata hai. `2>/dev/null` errors (jaise `Permission denied`) ko hide karta hai.

***

#### 2. **Specific File Extension Dhoondho**

* **Goal**: `/home` directory mein saari `.txt` files ke details dekhna.
* **Logic/Approach**: `-name "*.txt"` use karke `.txt` extension wali files filter karenge, aur `/home` path se search ko limit karenge taaki speed badhe.
*   **Command**:

    ```bash
    find /home -type f -name "*.txt" -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 /home/user/doc1.txt
    -rw-r--r-- 1 user user 2048 Jul 11 2025 /home/user/notes.txt
    ```
* **Kya Hua**: Command ne `/home` mein sirf `.txt` files dhoondhi aur unke details (permissions, size, timestamp) dikhaye. `-type f` ensure karta hai ki sirf regular files show ho.

***

#### 3. **Case-Insensitive File Name Search**

* **Goal**: Current directory mein `readme` naam se shuru hone wali files dhoondhna, chahe case kuch bhi ho (README, readme, ReadMe).
* **Logic/Approach**: `-iname` use karenge jo case-insensitive search karta hai, aur `-exec ls -l` se details lenge.
*   **Command**:

    ```bash
    find . -type f -iname "readme*" -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 ./README.md
    -rw-r--r-- 1 user user 2048 Jul 10 2025 ./readme.txt
    -rw-r--r-- 1 user user 3072 Jul 10 2025 ./ReadMe.doc
    ```
* **Kya Hua**: Yeh command case-insensitive tarike se `readme` se shuru hone wali files dhoondhta hai aur unke details dikhata hai.

***

#### 4. **Specific Folder Skip Karo**

* **Goal**: Current directory mein sab kuch list karo, lekin `temp` folder aur uske contents skip karo.
* **Logic/Approach**: `-path "./temp" -prune` use karke `temp` folder ko skip karenge, aur baaki files/folders ke details `-exec ls -l` se lenge.
*   **Command**:

    ```bash
    find . -path "./temp" -prune -o -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 ./file1.txt
    drwxr-xr-x 2 user user 4096 Jul 10 2025 ./docs
    -rw-r--r-- 1 user user 2048 Jul 10 2025 ./docs/note.txt
    ```
* **Kya Hua**: Yeh command `temp` folder ko skip karke baaki saare files aur folders ke details dikhata hai.

***

#### 5. **Sirf Directories Dhoondho**

* **Goal**: Current directory mein sirf directories ke details dekhna.
* **Logic/Approach**: `-type d` use karke sirf directories filter karenge, aur `-exec ls -l` se details lenge.
*   **Command**:

    ```bash
    find . -type d -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    drwxr-xr-x 2 user user 4096 Jul 10 2025 ./
    drwxr-xr-x 2 user user 4096 Jul 10 2025 ./docs
    drwxr-xr-x 2 user user 4096 Jul 10 2025 ./temp
    ```
* **Kya Hua**: Yeh command sirf directories ke paths aur details dikhata hai, files ko ignore karta hai.

***

#### 6. **Badi Files Dhoondho**

* **Goal**: 10 MB se badi files ke details dekhna.
* **Logic/Approach**: `-size +10M` use karke 10 MB se badi files filter karenge, aur `-exec ls -l` se details lenge.
*   **Command**:

    ```bash
    find . -type f -size +10M -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 12582912 Jul 10 2025 ./movie.mp4
    -rw-r--r-- 1 user user 15728640 Jul 10 2025 ./backup.zip
    ```
* **Kya Hua**: Command ne 10 MB se badi files dhoondhi aur unke details (permissions, size, timestamp) dikhaye.

***

#### 7. **Permissions ke Hisaab se Files**

* **Goal**: Files jo exact 755 permissions ke hain, unke details dekhna.
* **Logic/Approach**: `-perm 755` use karke exact 755 permissions wali files filter karenge.
*   **Command**:

    ```bash
    find . -type f -perm 755 -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rwxr-xr-x 1 user user 1024 Jul 10 2025 ./script.sh
    -rwxr-xr-x 1 user user 2048 Jul 10 2025 ./bin/app
    ```
* **Kya Hua**: Yeh command 755 permissions (executable for all) wali files ke details dikhata hai.

***

#### 8. **Recently Modified Files**

* **Goal**: Last 7 din mein modified files ke details dekhna.
* **Logic/Approach**: `-mtime -7` use karke last 7 din mein modified files filter karenge.
*   **Command**:

    ```bash
    find . -type f -mtime -7 -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 ./note.txt
    -rw-r--r-- 1 user user 2048 Jul 11 2025 ./project/code.py
    ```
* **Kya Hua**: Command ne last 7 din mein modified files dhoondhi aur unke details dikhaye.

***

#### 9. **Files Delete Karo**

* **Goal**: Saari `.bak` files delete karna.
* **Logic/Approach**: `-name "*.bak"` use karke `.bak` files filter karenge, aur `-exec rm {} \;` se delete karenge.
*   **Command**:

    ```bash
    find . -type f -name "*.bak" -exec rm {} \; 2>/dev/null
    ```
* **Output**: Koi output nahi, kyunki files delete ho jati hain.
* **Kya Hua**: Command ne saari `.bak` files delete kardi, aur `2>/dev/null` ne errors hide kiye.

***

#### 10. **Files Move Karo**

* **Goal**: Saari `.old` files ko `../archive/` folder mein move karna.
* **Logic/Approach**: `-name "*.old"` use karke `.old` files filter karenge, aur `-exec mv` se move karenge.
*   **Command**:

    ```bash
    find . -type f -name "*.old" -exec mv {} ../archive/ \; 2>/dev/null
    ```
* **Output**: Koi output nahi, files move ho jati hain.
* **Kya Hua**: Saari `.old` files `../archive/` mein move ho gayi.

***

#### 11. **Multiple Files Ek Saath Process Karo**

* **Goal**: Saari `.jpg` files ko ek saath `../images/` folder mein move karna.
* **Logic/Approach**: `-name "*.jpg"` use karke `.jpg` files filter karenge, aur `-exec mv {} +` se ek saath move karenge (faster).
*   **Command**:

    ```bash
    find . -type f -name "*.jpg" -exec mv {} ../images/ + 2>/dev/null
    ```
* **Output**: Koi output nahi, files move ho jati hain.
* **Kya Hua**: Saari `.jpg` files ek saath `../images/` mein move ho gayi, aur yeh method faster hai kyunki ek hi `mv` command run hota hai.

***

#### 12. **Confirmation ke Saath Delete**

* **Goal**: `.tmp` files delete karna, lekin har file ke liye confirmation maangna.
* **Logic/Approach**: `-name "*.tmp"` use karke `.tmp` files filter karenge, aur `-ok rm {} \;` se confirmation ke saath delete karenge.
*   **Command**:

    ```bash
    find . -type f -name "*.tmp" -ok rm {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    <rm ... ./file.tmp>? [y/n]
    ```
* **Kya Hua**: Har `.tmp` file ke liye confirmation maangta hai; agar `y` dabaya toh file delete hoti hai.

***

#### 13. **Newer Files Dhoondho**

* **Goal**: `ref.txt` se recently modified files ke details dekhna.
* **Logic/Approach**: `-newer ref.txt` use karke files filter karenge jo `ref.txt` se nayi hain.
*   **Command**:

    ```bash
    find . -type f -newer ref.txt -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 11 2025 ./newfile.txt
    -rw-r--r-- 1 user user 2048 Jul 12 2025 ./updated.doc
    ```
* **Kya Hua**: Command ne `ref.txt` se recently modified files dhoondhi aur unke details dikhaye.

***

#### 14. **Symbolic Links Dhoondho**

* **Goal**: System mein saare symbolic links ke details dekhna.
* **Logic/Approach**: `-type l` use karke sirf symbolic links filter karenge.
*   **Command**:

    ```bash
    find / -type l -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    lrwxrwxrwx 1 root root 10 Jul 10 2025 /home/user/link_to_file -> file1.txt
    lrwxrwxrwx 1 root root 12 Jul 10 2025 /usr/bin/python3 -> python3.8
    ```
* **Kya Hua**: Command ne system ke symbolic links dhoondhe aur unke details dikhaye.

***

#### 15. **Combine Conditions (AND/OR)**

* **Goal**: Last 7 din mein modified `.txt` ya `.md` files ke details dekhna.
* **Logic/Approach**: `-name "*.txt" -o -name "*.md"` use karke `.txt` ya `.md` files filter karenge, aur `-mtime -7` se recent files lenge.
*   **Command**:

    ```bash
    find . -type f \( -name "*.txt" -o -name "*.md" \) -mtime -7 -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 ./note.txt
    -rw-r--r-- 1 user user 2048 Jul 11 2025 ./README.md
    ```
* **Kya Hua**: Command ne last 7 din mein modified `.txt` ya `.md` files ke details dikhaye.

***

#### 16. **Avoid Other Filesystems**

* **Goal**: Current filesystem mein `.log` files ke details dekhna, mounted drives ko skip karke.
* **Logic/Approach**: `-xdev` use karke mounted filesystems skip karenge, aur `-name "*.log"` se `.log` files filter karenge.
*   **Command**:

    ```bash
    find / -xdev -type f -name "*.log" -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 /var/log/app.log
    ```
* **Kya Hua**: Command ne current filesystem ke `.log` files dhoondhi, mounted drives ko skip kiya.

***

#### 17. **Depth-First Search**

* **Goal**: Directories ke details depth-first tarike se dekhna (sub-directories pehle).
* **Logic/Approach**: `-depth` use karke contents pehle process karenge, aur `-type d` se sirf directories lenge.
*   **Command**:

    ```bash
    find . -depth -type d -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    drwxr-xr-x 2 user user 4096 Jul 10 2025 ./docs/subfolder
    drwxr-xr-x 2 user user 4096 Jul 10 2025 ./docs
    drwxr-xr-x 2 user user 4096 Jul 10 2025 ./
    ```
* **Kya Hua**: Command ne directories ko depth-first order mein list kiya (sub-directories pehle).

***

#### 18. **Files by User/Group**

* **Goal**: `john` user aur `developers` group ke files ke details dekhna.
* **Logic/Approach**: `-user john -group developers` use karke specific user aur group ke files filter karenge.
*   **Command**:

    ```bash
    find /home -type f -user john -group developers -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 john developers 1024 Jul 10 2025 /home/john/project.c
    -rw-r--r-- 1 john developers 2048 Jul 10 2025 /home/john/script.sh
    ```
* **Kya Hua**: Command ne `john` user aur `developers` group ke files ke details dikhaye.

***

#### 19. **Orphaned Files**

* **Goal**: Files jo kisi valid user ya group ke nahi hain, unke details dekhna.
* **Logic/Approach**: `-nouser -nogroup` use karke orphaned files filter karenge.
*   **Command**:

    ```bash
    find / -type f -nouser -nogroup -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 999 999 1024 Jul 10 2025 /tmp/unknown_file
    ```
* **Kya Hua**: Command ne files jo kisi valid user ya group se nahi hain, unke details dikhaye.

***

#### 20. **Complex Example: Multiple Conditions**

* **Goal**: `/home` mein `.txt` ya `.doc` files jo 100 KB se badi hain, unko `/backup/` mein copy karna.
* **Logic/Approach**: `-name "*.txt" -o -name "*.doc"` aur `-size +100k` use karke files filter karenge, aur `-exec cp` se copy karenge.
*   **Command**:

    ```bash
    find /home -type f \( -name "*.txt" -o -name "*.doc" \) -size +100k -exec cp {} /backup/ \; 2>/dev/null
    ```
* **Output**: Koi output nahi, files copy ho jati hain.
* **Kya Hua**: Command ne `.txt` ya `.doc` files jo 100 KB se badi hain, unko `/backup/` mein copy kiya.

***

#### 21. **Empty Files Dhoondho**

* **Goal**: Khali files (0 bytes) ke details dekhna.
* **Logic/Approach**: `-empty` use karke khali files filter karenge, aur `-type f` se sirf files lenge.
*   **Command**:

    ```bash
    find . -type f -empty -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 0 Jul 10 2025 ./empty.txt
    -rw-r--r-- 1 user user 0 Jul 10 2025 ./docs/blank.doc
    ```
* **Kya Hua**: Command ne khali files ke details dikhaye.

***

#### 22. **Files by Number of Hard Links**

* **Goal**: Files jo exactly 2 hard links ke hain, unke details dekhna.
* **Logic/Approach**: `-links 2` use karke 2 hard links wali files filter karenge.
*   **Command**:

    ```bash
    find . -type f -links 2 -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 2 user user 1024 Jul 10 2025 ./file.txt
    ```
* **Kya Hua**: Command ne 2 hard links wali files ke details dikhaye.

***

#### 23. **Files Sort Karo**

* **Goal**: `.txt` files ke paths ko alphabetically sort karke dekhna.
* **Logic/Approach**: `-name "*.txt"` se `.txt` files filter karenge, aur `| sort` se output ko sort karenge.
*   **Command**:

    ```bash
    find . -type f -name "*.txt" -exec ls -l {} \; 2>/dev/null | sort
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 ./docs/note.txt
    -rw-r--r-- 1 user user 2048 Jul 10 2025 ./file1.txt
    ```
* **Kya Hua**: Command ne `.txt` files ke details alphabetically sort karke dikhaye.

***

#### 24. **Files ko Gzip Karo**

* **Goal**: Saari `.log` files ko compress (gzip) karna.
* **Logic/Approach**: `-name "*.log"` use karke `.log` files filter karenge, aur `-exec gzip` se compress karenge.
*   **Command**:

    ```bash
    find . -type f -name "*.log" -exec gzip {} \; 2>/dev/null
    ```
* **Output**: Koi output nahi, `.log` files `.log.gz` ban jati hain.
* **Kya Hua**: Command ne saari `.log` files ko gzip format mein compress kiya.

***

#### 25. **Search with Regex**

* **Goal**: `.txt` files jo regular expression se match karte hain, unke details dekhna.
* **Logic/Approach**: `-regex ".*\.txt$"` use karke `.txt` files filter karenge.
*   **Command**:

    ```bash
    find . -type f -regex ".*\.txt$" -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 ./file1.txt
    -rw-r--r-- 1 user user 2048 Jul 10 2025 ./docs/note.txt
    ```
* **Kya Hua**: Command ne regex pattern se match hone wali `.txt` files ke details dikhaye.

***

#### 26. **Config Files with Specific Size**

* **Goal**: 25 KB se badi aur 28 KB se chhoti `.conf` files ke details dekhna.
* **Logic/Approach**: `-name "*.conf"`, `-size +25k`, aur `-size -28k` use karke files filter karenge.
*   **Command**:

    ```bash
    find /etc -type f -name "*.conf" -size +25k -size -28k -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 root root 26240 Jul 10 2025 /etc/sample.conf
    ```
* **Kya Hua**: Command ne 25-28 KB ke beech wali `.conf` files ke details dikhaye.

***

#### 27. **Files Modified in Specific Date Range**

* **Goal**: 2020-01-01 se 2021-01-01 ke beech modified `.conf` files ke details dekhna.
* **Logic/Approach**: `-newermt` aur `! -newermt` use karke date range mein files filter karenge.
*   **Command**:

    ```bash
    find /etc -type f -name "*.conf" -newermt 2020-01-01 ! -newermt 2021-01-01 -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 root root 26240 Mar 15 2020 /etc/sample.conf
    ```
* **Kya Hua**: Command ne 2020-01-01 se 2021-01-01 ke beech modified `.conf` files ke details dikhaye.

***

#### 28. **Files with Write Permissions for Others**

* **Goal**: Files jo “others” ke liye writable hain, unke details dekhna.
* **Logic/Approach**: `-perm /o=w` use karke writable files filter karenge.
*   **Command**:

    ```bash
    find /home -type f -perm /o=w -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-rw-rw- 1 user user 1024 Jul 10 2025 /home/user/public.txt
    ```
* **Kya Hua**: Command ne files jo others ke liye writable hain, unke details dikhaye.

***

#### 29. **Files by Specific User and Size**

* **Goal**: `john` user ke 100 KB se badi files ke details dekhna.
* **Logic/Approach**: `-user john` aur `-size +100k` use karke files filter karenge.
*   **Command**:

    ```bash
    find /home -type f -user john -size +100k -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 john john 105000 Jul 10 2025 /home/john/document.pdf
    ```
* **Kya Hua**: Command ne `john` user ke 100 KB se badi files ke details dikhaye.

***

#### 30. **Files in Multiple Directories**

* **Goal**: `/etc` aur `/home` mein `.conf` files ke details dekhna.
* **Logic/Approach**: Multiple paths (`/etc /home`) aur `-name "*.conf"` use karke files filter karenge.
*   **Command**:

    ```bash
    find /etc /home -type f -name "*.conf" -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 root root 26240 Jul 10 2025 /etc/sample.conf
    -rw-r--r-- 1 user user 27000 Jul 10 2025 /home/user/app.conf
    ```
* **Kya Hua**: Command ne `/etc` aur `/home` mein `.conf` files ke details dikhaye.

***

#### 31. **Files by Specific Group**

* **Goal**: `developers` group ke files ke details dekhna.
* **Logic/Approach**: `-group developers` use karke files filter karenge.
*   **Command**:

    ```bash
    find /home -type f -group developers -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user developers 1024 Jul 10 2025 /home/user/code.c
    ```
* **Kya Hua**: Command ne `developers` group ke files ke details dikhaye.

***

#### 32. **Files Accessed Recently**

* **Goal**: Last 7 din mein accessed files ke details dekhna.
* **Logic/Approach**: `-atime -7` use karke recently accessed files filter karenge.
*   **Command**:

    ```bash
    find /home -type f -atime -7 -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 /home/user/recent.txt
    ```
* **Kya Hua**: Command ne last 7 din mein accessed files ke details dikhaye.

***

#### 33. **Files with Sticky Bit**

* **Goal**: Files jo sticky bit ke saath hain, unke details dekhna.
* **Logic/Approach**: `-perm /1000` use karke sticky bit wali files filter karenge.
*   **Command**:

    ```bash
    find /tmp -type f -perm /1000 -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rwxrwxrwt 1 user user 1024 Jul 10 2025 /tmp/sticky_file
    ```
* **Kya Hua**: Command ne sticky bit wali files ke details dikhaye.

***

#### 34. **Files with Exact Permissions**

* **Goal**: Exact 600 permissions wali files ke details dekhna.
* **Logic/Approach**: `-perm 600` use karke exact permissions wali files filter karenge.
*   **Command**:

    ```bash
    find /etc -type f -perm 600 -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw------- 1 root root 1024 Jul 10 2025 /etc/secure.conf
    ```
* **Kya Hua**: Command ne exact 600 permissions wali files ke details dikhaye.

***

#### 35. **Files with No Owner**

* **Goal**: Files jo kisi valid user ke nahi hain, unke details dekhna.
* **Logic/Approach**: `-nouser` use karke orphaned files filter karenge.
*   **Command**:

    ```bash
    find / -type f -nouser -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 999 999 1024 Jul 10 2025 /tmp/orphan.txt
    ```
* **Kya Hua**: Command ne files jo kisi valid user ke nahi hain, unke details dikhaye.

***

#### 36. **Files with No Group**

* **Goal**: Files jo kisi valid group ke nahi hain, unke details dekhna.
* **Logic/Approach**: `-nogroup` use karke files filter karenge.
*   **Command**:

    ```bash
    find / -type f -nogroup -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user 999 1024 Jul 10 2025 /tmp/nogroup.txt
    ```
* **Kya Hua**: Command ne files jo kisi valid group ke nahi hain, unke details dikhaye.

***

#### 37. **Files Modified in Last Hour**

* **Goal**: Last 60 minutes mein modified files ke details dekhna.
* **Logic/Approach**: `-mmin -60` use karke recently modified files filter karenge.
*   **Command**:

    ```bash
    find /home -type f -mmin -60 -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 13 2025 /home/user/log.txt
    ```
* **Kya Hua**: Command ne last 60 minutes mein modified files ke details dikhaye.

***

#### 38. **Files with Specific Extension and User**

* **Goal**: `john` user ke `.log` files ke details dekhna.
* **Logic/Approach**: `-name "*.log" -user john` use karke files filter karenge.
*   **Command**:

    ```bash
    find /home -type f -name "*.log" -user john -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 john john 1024 Jul 10 2025 /home/john/app.log
    ```
* **Kya Hua**: Command ne `john` user ke `.log` files ke details dikhaye.

***

#### 39. **Files in Subdirectories Only**

* **Goal**: Files jo kam se kam 2 levels ke subdirectories mein hain, unke details dekhna.
* **Logic/Approach**: `-mindepth 2` use karke subdirectories ke files filter karenge.
*   **Command**:

    ```bash
    find /home -mindepth 2 -type f -name "*.txt" -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 /home/user/docs/note.txt
    ```
* **Kya Hua**: Command ne subdirectories (2 levels deep) ke `.txt` files ke details dikhaye.

***

#### 40. **Files Excluding Specific Extension**

* **Goal**: `.bak` files ke alawa baaki files ke details dekhna.
* **Logic/Approach**: `! -name "*.bak"` use karke `.bak` files exclude karenge.
*   **Command**:

    ```bash
    find /home -type f ! -name "*.bak" -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 /home/user/file.txt
    ```
* **Kya Hua**: Command ne `.bak` files ko chhodkar baaki files ke details dikhaye.

***

#### 41. **Files with Specific Inode**

* **Goal**: Specific inode number wali files ke details dekhna.
* **Logic/Approach**: `-inum` use karke specific inode wali files filter karenge.
*   **Command**:

    ```bash
    find /home -type f -inum 123456 -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 10 2025 /home/user/file.txt
    ```
* **Kya Hua**: Command ne specific inode number wali files ke details dikhaye.

***

#### 42. **Files with Detailed Stat Output**

* **Goal**: `.conf` files ke detailed stats (inode, times, etc.) dekhna.
* **Logic/Approach**: `-name "*.conf"` use karke files filter karenge, aur `-exec stat` se detailed output lenge.
*   **Command**:

    ```bash
    find /etc -type f -name "*.conf" -exec stat {} \; 2>/dev/null
    ```
*   **Output**:

    ```
      File: /etc/sample.conf
      Size: 26240           Blocks: 52         IO Block: 4096   regular file
      Device: 801h/2049d      Inode: 123456      Links: 1
      Access: (0644/-rw-r--r--)  Uid: ( 1000/   user)   Gid: ( 1000/   user)
      Access: 2025-07-10 10:00:00.000000000 +0000
      Modify: 2025-07-10 10:00:00.000000000 +0000
      Change: 2025-07-10 10:00:00.000000000 +0000
      Birth: -
    ```
* **Kya Hua**: Command ne `.conf` files ke detailed stats (inode, permissions, times) dikhaye.

***

#### 43. **Files with Specific Name Pattern**

* **Goal**: `nginx` naam wali `.conf` files ke details dekhna.
* **Logic/Approach**: `-name "*nginx*.conf"` use karke specific naam wali files filter karenge.
*   **Command**:

    ```bash
    find /etc -type f -name "*nginx*.conf" -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 root root 26240 Jul 10 2025 /etc/nginx/nginx.conf
    ```
* **Kya Hua**: Command ne `nginx` naam wali `.conf` files ke details dikhaye.

***

#### 44. **Files Modified in Last Minute**

* **Goal**: Last 1 minute mein modified files ke details dekhna.
* **Logic/Approach**: `-mmin -1` use karke recently modified files filter karenge.
*   **Command**:

    ```bash
    find /home -type f -mmin -1 -exec ls -l {} \; 2>/dev/null
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 user user 1024 Jul 13 2025 /home/user/recent.txt
    ```
* **Kya Hua**: Command ne last 1 minute mein modified files ke details dikhaye.

***

#### 45. **Complex Example with Sorting**

* **Goal**: 25-28 KB ke beech wali `.conf` files jo 2020-03-03 ke baad modified hui hain, unke details sorted order mein dekhna.
* **Logic/Approach**: `-name "*.conf"`, `-size +25k -size -28k`, aur `-newermt 2020-03-03` use karke files filter karenge, aur `| sort` se output sort karenge.
*   **Command**:

    ```bash
    find /etc -type f -name "*.conf" -size +25k -size -28k -newermt 2020-03-03 -exec ls -l {} \; 2>/dev/null | sort -k 6,7
    ```
*   **Output**:

    ```
    -rw-r--r-- 1 root root 26240 Mar 15 2020 /etc/sample.conf
    -rw-r--r-- 1 user user 27000 Apr 01 2021 /home/user/app.conf
    ```
* **Kya Hua**: Command ne 25-28 KB ke beech wali `.conf` files jo 2020-03-03 ke baad modified hui hain, unke details sorted order (date ke hisaab se) mein dikhaye.

***

### **Tips for Using These Test Cases**

* **Test Pehle**: Har command ko pehle `-print` ke saath run karke check kar ki kaunsi files match ho rahi hain.
* **Error Handling**: `2>/dev/null` use kar taaki `Permission denied` errors na dikhein.
* **Precision**: Specific paths (`/etc`, `/home`) aur patterns (`*nginx*.conf`) use karke search ko narrow kar.
* **Output Customization**: `-exec ls -lh` use karo agar human-readable sizes chahiye.
* **GitBook Integration**: In test cases ko apne `find_command.md` mein add kar, aur har case ke liye subheading bana taaki navigation easy ho.

### **Best Practices aur Tips**

1. **Quoting**: File names mein spaces ya special characters hote hain, toh quotes use karo: `find . -name "*.txt"`.
2. **Performance**:
   * `-exec ... {} +` use karo jab badi sankhya mein files process karni ho.
   * `-prune` use karke unnecessary directories skip karo.
3. **Safety**:
   * `-ok` use karo destructive actions (jaise `rm`) ke liye.
   * Pehle `-print` laga ke test karo ki kaunsi files match ho rahi hain.
4. **Debugging**:
   * Agar output nahi mil raha, toh `-print` add karo ya verbose output ke liye `strace` use karo.
5. **Symbolic Links**: `-L` use karo agar actual files ke details chahiye.
6. **Combining Commands**: `find` ke output ko `xargs`, `sort`, ya `grep` ke saath pipe karke aur process kar sakte ho.

### **Common Pitfalls**

1. **Special Characters**: `*`, `?`, `(`, `)` jaise characters ko quote karo, warna shell unhe expand kar sakta hai.
2. **Permissions Denied**: Agar `Permission denied` error aaye, toh `sudo` use karo ya `-path` se restricted folders skip karo.
3. **Infinite Loops**: Symbolic links ke wajah se loop ho sakta hai, isliye `-L` ya `-H` carefully use karo.

### **Conclusion**

`find` command ek bohot powerful tool hai jo files aur directories ko dhoondhne ke liye flexible aur detailed options deta hai. Is guide mein humne basic syntax se lekar advanced examples tak cover kiya. Agar tujhe aur specific use cases chahiye ya koi confusion hai, toh experiment karo aur practice karo. Documentation ke liye yeh guide GitBook ya kisi aur platform pe easily use ho sakta hai!
