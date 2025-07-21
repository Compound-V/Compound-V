# Poking the Filesystem - slide 3



***

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:yellow;">**USER SPACE Kya Hai?**</mark>



* <mark style="color:orange;">**USER SPACE Linux Filesystem Stack ka pehla aur sabse upar wala layer hai jahan**</mark> <mark style="color:orange;">**user-level applications, shells, aur libraries kaam karte hain.**</mark> Yeh user-mode mein operate karta hai aur kernel se alag ek secure environment provide karta hai jahan aap apne programs aur commands run karte hain.
* Yeh layer user aur system ke beech ek interface hai, jahan aapki daily activities – jaise files edit karna, commands run karna, ya scripts likhna – shuru hoti hain.
* Simple analogy: Yeh ek control room hai jahan se aap puri building (filesystem) ko manage karte hain, lekin actual kaam backend (kernel) se hota hai.
* Example: Jab aap terminal mein `cat file.txt` ya `vim myfile.txt` type karte hain, yeh USER SPACE ke andar hota hai jahan aapka command shuru hota hai.
* Description: Yeh section aapke diya huye structure mein teen sub-sections rakhta hai – Applications, Shells, aur Standard C Library – jo saath mein kaam karke user experience ko smooth banate hain.



#### <mark style="color:yellow;">**Core Content Kya Hai Aur Kaise Kaam Karta Hai?**</mark>



*   <mark style="color:yellow;">**1.1 Applications:**</mark>

    * **Kya Hai?**: Yeh user-level tools hain jaise `cp` (copy), `mv` (move), `cat` (concatenate), `vim` (text editor), `nano`, `grep`, aur bhi kai commands jo files ya data ke saath kaam karte hain.
    * **Kaise Kaam Karta Hai?**: Yeh tools Standard C Library (glibc) ke zariye system calls (jaise `open`, `read`, `write`, `close`) use karte hain. Yeh directly disk se baat nahi karte, balki kernel ke zariye data access karte hain, jo security aur abstraction deta hai.
    * **Extra Details**: Har tool apna specific kaam karta hai – `cp` files copy karta hai, `grep` text search karta hai – aur yeh sab user-friendly commands hote hain jo complex operations chhupate hain.
    * Example: Aap `cp file1.txt file2.txt` karte hain – yeh `open` (source file), `read`, `write` (destination file), aur `close` syscalls chalata hai.


*   <mark style="color:yellow;">**1.2 Shells (bash, zsh, fish)**</mark><mark style="color:yellow;">:</mark>

    * **Kya Hai?**: Yeh command-line interpreters hain jo aapke commands (jaise `ls`, `echo`, redirection `>`) ko execute karte hain. Popular shells hain `bash` (Bourne Again Shell), `zsh` (Z Shell), aur `fish` (Friendly Interactive Shell).
    * **Kaise Kaam Karta Hai?**: Yeh `fork` (naya process banane), `exec` (command run karne), aur `wait` (process complete hone ka intezaar) system calls use karte hain. Yeh bhi piping (`|`) aur redirection (`>`, `<`) jaise features support karte hain.
    * **Extra Details**: Shells ek scripting environment bhi provide karte hain – aap `.sh` files likh sakte hain jo multiple commands ko automate karte hain. Har shell ke apne features hote hain, jaise `zsh` ka auto-completion.
    * Example: Aap `echo "Hello" > file.txt` karte hain – shell `fork` karke ek process banata hai, `exec` se `echo` run karta hai, aur `write` syscall se data file mein daalta hai.


*   <mark style="color:yellow;">**1.3 Standard C Library (glibc / musl)**</mark><mark style="color:yellow;">:</mark>

    * **Kya Hai?**: Yeh ek library hai jo C programming language ke liye syscalls ke wrappers provide karta hai. Do main versions hain – `glibc` (GNU C Library) aur `musl` (lightweight alternative).
    * **Kaise Kaam Karta Hai?**: Yeh high-level functions (jaise `open()`, `read()`, `write()`) ko low-level syscalls (jaise `syscall(SYS_openat)`, `syscall(SYS_read)`) mein convert karta hai. Yeh developers ko hardware details se door rakhta hai.
    * **Extra Details**: glibc bada aur feature-rich hai, jabki musl lightweight aur security-focused hai. Yeh library multi-threading aur locale support bhi deta hai.
    * Example: Aapka `fopen("file.txt", "r")` call glibc ke zariye `open` syscall mein badal jata hai, jo kernel ko file kholne ka signal deta hai.



#### <mark style="color:yellow;">**Technical Depth**</mark>



* **Process Isolation**: USER SPACE ke processes kernel se alag hain, jo memory protection aur privilege levels (user mode vs kernel mode) se secure hote hain. Yeh ek ring architecture (Ring 3 for user, Ring 0 for kernel) mein kaam karta hai.
* **System Call Mechanism**: Jab koi application ya shell syscall karta hai, yeh ek software interrupt (jaise `int 0x80` ya `syscall` instruction) ke zariye kernel mein jata hai. Yeh context switch ek thodi der ke liye performance affect karta hai lekin security deta hai.
* <mark style="color:orange;">**Library Role**</mark><mark style="color:orange;">: glibc/musl ek abstraction layer hai jo POSIX standards follow karta hai. Yeh file descriptors (integer IDs for open files) manage karta hai aur buffers use karke data transfer ko optimize karta hai.</mark>
* **Interaction**: Applications aur shells glibc ke functions call karte hain, jo kernel ke system call table se mapped hote hain. Yeh table har syscall ke liye ek unique number (jaise SYS\_open = 2) rakhta hai.



1.  <mark style="color:yellow;">**Practical Example**</mark>

    * Scenario: Aap ek file create aur edit karna chahte hain.
    * Process:
      1. Aap terminal mein `vim myfile.txt` type karte hain – yeh `vim` application (USER SPACE) hai.
      2. `vim` `open` syscall ke zariye file kholta hai (glibc ke through).
      3. Aap "Hello World" type karte hain – `write` syscall trigger hota hai.
      4. Save karne pe `close` syscall file ko band karta hai.
      5. Shell (bash) yeh process manage karta hai aur aapko prompt wapas deta hai.
    * Check: `cat myfile.txt` se dekhein ki "Hello World" save hua hai, aur `strace -e open,write,close vim myfile.txt` se syscalls trace kar sakte hain.


2.  <mark style="color:yellow;">**Kyun Zaroori Hai?**</mark>

    * **User Control**: Yeh aapko apne kaam (file management, scripting) ko control karne deta hai bina kernel ke complexity mein jane ke.
    * **Abstraction**: glibc low-level hardware access chhupata hai, jo developers aur users ke liye easy banata hai.
    * **Customization**: Alag-alag shells aur tools aapke workflow ko personalise karte hain.


3.  <mark style="color:yellow;">**Security Aur Maintenance Tips**</mark>

    * **Permissions**: `chmod 644 file.txt` se file access limit karen taaki sirf owner edit kar sake.
    * **Monitoring**: `lsof` ya `ps` se running processes check karen aur `strace` se syscall patterns dekhen.
    * **Updates**: `apt update && apt upgrade` se glibc aur shell packages update karen taaki security patches lagein.
    * **Sandboxing**: Sensitive operations ke liye `chroot` ya containers use karen.



***

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:yellow;">VFS (Virtual Filesystem Switch)</mark>



1.  <mark style="color:yellow;">**VFS Kya Hai?**</mark>

    * VFS Linux Filesystem Stack ka ek central layer hai jo sabhi filesystems ke beech ek abstract aur unified interface provide karta hai. Yeh kernel ke andar kaam karta hai aur user-space ko alag-alag filesystems (jaise ext4, XFS, Btrfs) ke saath ek consistent tareeke se interact karne deta hai.
    * Yeh ek middleware ki tarah kaam karta hai jo filesystem-specific details ko chhupata hai aur ek standard API deta hai, jisse user programs ko chinta nahi karni padti ki backend mein kaunsa filesystem hai.
    * Simple analogy: Yeh ek universal translator hai jo alag-alag bhasha (filesystem) bolne wale devices ko ek hi zuban mein samjha deta hai.
    * Example: Jab tu `ls /mnt/data` chalata hai aur teri disk pe ext4 hai, VFS usko handle karta hai – agar wahan Btrfs hota, toh bhi wahi command kaam karta.


2.  <mark style="color:yellow;">**Core Content Kya Hai Aur Kaise Kaam Karta Hai?**</mark>

    * **Purpose**: VFS ka maqsad <mark style="color:green;">multiple filesystems ko ek saath chalane dena hai, user-space se aane wali requests ko filesystem drivers tak pahunchana, aur performance ko optimize karna.</mark>
    * **Core Structures**:
      * `super_block`: Yeh mounted filesystem ki metadata rakhta hai, jaise block size aur mount point.
      * `inode`: Har file ya directory ko disk pe represent karta hai, jisme size, permissions, aur data pointers hote hain.
      * `dentry`: Directory entries ka cache hai jo pathnames (jaise /home/user/file.txt) ko inodes se jodta hai.
      * `file`: Yeh ek process-specific open file handle hai jo read/write operations ke liye istemal hota hai.
    * **Caches**:
      * `dcache`: <mark style="color:orange;">Dentry cache jo path lookup ko tezi se karta hai,</mark> memory mein pathname-to-inode mapping store karta hai.
      * `icache`: <mark style="color:orange;">Inode cache jo file metadata aur data ko RAM mein rakhta hai taaki disk access kam ho.</mark>
    * **Operation Tables**:
      * `file_operations`: Yeh table `read()`, `write()`, `mmap()`, `ioctl()` jaise file-level operations ko define karta hai.
      * `inode_operations`: Yeh `create()`, `lookup()`, `link()`, `unlink()` jaise inode-level operations handle karta hai.
      * `super_operations`: Yeh `mount()`, `statfs()`, `write_super()`, `sync_fs()` jaise filesystem-level tasks manage karta hai.
    * Example: Tu `cat /home/user/doc.txt` karta hai – VFS `dentry` se /home/user/doc.txt ka path resolve karta hai, `inode` se file data ka location nikaalta hai, aur `file_operations.read()` se content ko user-space mein bhejta hai.


3.  <mark style="color:yellow;">**Technical Depth**</mark>

    * VFS ek object-oriented design pe based hai jo kernel mein function pointers ke zariye kaam karta hai. Har filesystem (jaise ext4) apna set of operations register karta hai jo VFS ke tables mein load hote hain.
    * `dcache` aur `icache` LRU (Least Recently Used) algorithm use karte hain taaki purane entries ko replace karke memory ko manage karen, jo caching efficiency badhata hai.
    * Yeh layer filesystem drivers ke saath dynamically interact karta hai – jab tu ek naya filesystem mount karta hai (jaise `mount /dev/sda1 /mnt`), VFS uska `super_block` aur operation tables initialize karta hai.
    * Multithreading support hai – VFS multiple processes ke simultaneous file access ko handle kar sakta hai, lekin yeh locks (jaise mutexes) use karke race conditions se bachata hai.


4.  <mark style="color:yellow;">**Practical Example**</mark>

    * Scenario: Tu ek system mein do alag-alag filesystems (ext4 aur Btrfs) check karna chahta hai.
    * Process:
      1. Tu `ls /mnt/ext4` aur `ls /mnt/btrfs` commands chalata hai.
      2. VFS `dentry` cache se pathnames resolve karta hai aur respective filesystem drivers (ext4, Btrfs) ko activate karta hai.
      3. `inode` se file metadata fetch hota hai, aur `file_operations` se directory listing user-space mein bheja jata hai.
      4. Screen pe file names dikhayi dete hain.
    * Check: `df -T` se mounted filesystems aur unke types check kar sakta hai, ya `cat /proc/mounts` se VFS ke mounted points dekh sakta hai.


5.  <mark style="color:yellow;">**Kyun Zaroori Hai?**</mark>

    * **Flexibility**: Yeh alag-alag filesystems (local, network, virtual) ko ek platform pe laata hai, jaise ext4 aur NFS ko ek saath chalane deta hai.
    * **Uniformity**: User-space ko ek consistent interface deta hai, jisse developers ko har filesystem ke liye alag code likhne ki zarurat nahi padti.
    * **Performance Boost**: `dcache` aur `icache` se disk I/O kam hota hai, aur operation tables se optimized execution milta hai.


6. <mark style="color:yellow;">**Security Aur Maintenance Tips**</mark>
   * **Integrity Checks**: `fsck` ya `e2fsck` se filesystem corruption check karo aur fix karo.
   * **Cache Sync**: `sync` command se ensure karo ki cache ka data disk pe flush ho jaye, khas kar shutdown se pehle.
   * **Performance Tuning**: `sysctl` se VFS cache size adjust karo ya `vm.vfs_cache_pressure` tweak karo.
   * **Logging**: `dmesg` se VFS-related errors ya warnings monitor karo.



***

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:yellow;">**FILESYSTEM IMPLEMENTATIONS**</mark>



1.  <mark style="color:yellow;">**FILESYSTEM IMPLEMENTATIONS Kya Hai?**</mark>

    * FILESYSTEM IMPLEMENTATIONS Linux Filesystem Stack ka woh hissa hai jo VFS ke neeche aata hai aur actual data storage aur management ke liye responsible hota hai. Yeh alag-alag types ke filesystems ko implement karta hai jo disk ya memory pe data organize karte hain.
    * Yeh layer VFS ke abstract interface ko real-world filesystems (jaise ext4, NFS) se jodti hai, jahan specific features jaise journaling, indexing, ya networking support add hote hain.
    * Simple analogy: Yeh ek factory hai jo VFS ke blueprint (abstract design) ko alag-alag products (filesystems) mein badal deta hai, har ek ke apne features ke saath.
    * Example: Jab tu `mkfs.ext4 /dev/sdb1` karke ek ext4 filesystem banata hai, yeh layer usko create aur manage karta hai.


2.  <mark style="color:yellow;">**Core Content Kya Hai Aur Kaise Kaam Karta Hai?**</mark>

    * **Purpose**: Yeh filesystems ko VFS ke liye specific implementations deta hai, jo data storage, retrieval, aur metadata management handle karte hain.
    * **Types Aur Sub-Categories**:
      * **Local Filesystems**:
        * **ext4, XFS, Btrfs, F2FS**: Yeh disk-based filesystems hain jo local storage (HDD/SSD) pe kaam karte hain.
        * **Features**: Block allocation, journaling (data consistency), metadata management, aur directory indexing.
        * **ext4 Example**:
          * Journaling (via JBD2) jo data corruption se bachata hai.
          * Extents jo space efficiency badhate hain (bade files ke liye).
          * HTree indexing jo directory lookup ko tezi se karta hai.
          * Delayed allocation jo write performance optimize karta hai.
      * **Network Filesystems**:
        * **NFS**: Network File System jo RPC (Remote Procedure Call) ke zariye remote mounts ko support karta hai.
        * **CIFS/SMB**: Windows-compatible sharing ke liye istemal hota hai, jaise network drives.
        * **FUSE**: Filesystem in Userspace jo user-level filesystem support deta hai (jaise SSHFS).
      * **Virtual / Pseudo Filesystems**:
        * **procfs**: `/proc` directory jo process information (jaise `/proc/cpuinfo`) provide karta hai.
        * **sysfs**: `/sys` directory jo kernel objects aur hardware info deta hai.
        * **tmpfs**: In-memory filesystem jo RAM mein temporary data store karta hai (jaise `/dev/shm`).
    * Example: Tu `mount -t nfs remote:/data /mnt` karta hai – NFS network filesystem implement karta hai aur VFS ke through data access deta hai.


3.  <mark style="color:yellow;">**Technical Depth**</mark>

    * Har filesystem apna data structure aur algorithm use karta hai – jaise ext4 ka journaling JBD2 module ke zariye crash recovery deta hai, jabki Btrfs copy-on-write (CoW) use karta hai snapshots ke liye.
    * Local filesystems block allocation ke liye bitmap ya extent-based systems use karte hain, jo disk space ko manage karta hai.
    * Network filesystems jaise NFS RPC protocol aur locking mechanisms (jaise NLM) use karte hain taaki remote data access synchronized rahe.
    * Pseudo filesystems jaise procfs aur sysfs kernel memory se directly data generate karte hain, bina physical disk ke, jo runtime information provide karta hai.


4.  <mark style="color:yellow;">**Practical Example**</mark>

    * Scenario: Tu ek system mein local aur network filesystem use karna chahta hai.
    * Process:
      1. Tu `mkfs.ext4 /dev/sdc1` chalake ek ext4 filesystem banata hai aur `mount /dev/sdc1 /mnt/local` karta hai.
      2. `ls /mnt/local` se files check karta hai – ext4 ka HTree indexing tezi se directory list deta hai.
      3. Phir `mount -t nfs server:/data /mnt/network` karke NFS mount karta hai.
      4. `ls /mnt/network` se remote files access hote hain – NFS RPC calls handle karta hai.
    * Check: `df -h` se mounted filesystems ki size aur type dekho, ya `cat /proc/mounts` se verify karo.


5.  <mark style="color:yellow;">**Kyun Zaroori Hai?**</mark>

    * **Variety**: Alag-alag needs ke liye alag filesystems (local, network, virtual) provide karta hai.
    * **Efficiency**: Features jaise journaling (ext4) ya CoW (Btrfs) data integrity aur performance badhate hain.
    * **Scalability**: Network filesystems jaise NFS distributed systems ke liye scale karte hain.


6. <mark style="color:yellow;">**Security Aur Maintenance Tips**</mark>
   * **Consistency Checks**: `fsck` ya `btrfs check` se filesystem errors detect aur fix karo.
   * **Access Control**: `chmod` aur `chown` se file permissions set karo, khas kar network filesystems ke liye.
   * **Backup**: Network filesystems (NFS) ke liye regular backups (jaise `rsync`) rakho.
   * **Monitoring**: `iostat` ya `nfsstat` se performance aur errors track karo.
