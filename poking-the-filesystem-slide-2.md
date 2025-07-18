# Poking the Filesystem - slide 2

## <mark style="color:yellow;">Filesystem Ke Fundamentals Aur Internals</mark>

### <mark style="color:yellow;">Filesystem Kya Hai?</mark>

_**Filesystem**_ operating system ka ek core component hai jo _**files ko disk ya partition pe organize, store, aur manage karta hai**._ Yeh ek systematic method hai jo data structures ke through files ke storage, retrieval, aur metadata management ko handle karta hai, taaki OS aur applications files ke saath efficiently kaam kar sakein.



*   <mark style="color:yellow;">**Definition**</mark><mark style="color:yellow;">:</mark>\
    Filesystem ek method aur set of data structures hai jo operating system use karta hai files ko disk ya partition pe track aur organize karne ke liye. Yeh decide karta hai ki files ka data kahan store hoga aur kaise access hoga.

    * **Example**: Jab tum apne USB drive mein “vacation.jpg” save karte ho, filesystem decide karta hai ki yeh photo disk ke specific sectors mein kahan jayega aur file explorer se kaise open hoga.
    * **Technical Detail**: _<mark style="color:yellow;">**Filesystem raw disk storage**</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">(jo binary 0s aur 1s ka collection hota hai)</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">**ko logical format mein convert karta hai.**</mark>_ Yeh metadata (jaise file name, size, permissions, timestamps) aur actual file content ke beech coordination karta hai. Virtual File System (VFS) layer ke through OS filesystem ke saath interact karta hai, jo alag-alag filesystem types (ext4, NTFS) ko standard interface deta hai.


*   <mark style="color:yellow;">**Filesystem Banane Ka Process**</mark><mark style="color:yellow;">:</mark>\
    <mark style="color:green;">Filesystem create karna matlab disk ya partition ko initialize karna, jisme book-keeping data structures jaise superblock, inode table, aur block allocation table disk pe likhe jate hain.</mark>

    * **Example**: Jab tum ek 1TB hard disk ko ext4 format mein format karte ho, OS superblock, inode table, aur data blocks ke liye space allocate karta hai, jisse disk file storage ke liye ready ho jati hai.
    * **Technical Detail**: <mark style="color:orange;">**Formatting ke dauraan disk ke sectors ko fixed-size blocks (jaise 4KB) mein divide kiya jata hai.**</mark> _**Superblock filesystem ka metadata rakhta hai**, **inode table files ke metadata ke liye space reserve karta hai**, aur **block allocation table track karta hai ki kaunse blocks free ya used hain**. Yeh process OS ke system calls_ **(jaise `mkfs.ext4`)** _ke through hota hai, jo disk ko structured filesystem mein badalta hai._


*   <mark style="color:yellow;">**UNIX Filesystems Ka Design**</mark><mark style="color:yellow;">:</mark>\
    UNIX filesystems (jaise ext4, XFS, BTRFS) ka core design similar hota hai, lekin unki implementation alag hoti hai, jo specific use-cases (speed, reliability, scalability) ke liye optimize hoti hain.

    * **Example**: ext4 journaling ke through data corruption se protect karta hai, jabki XFS bade datasets (jaise video editing servers) ke liye high-speed read/write deta hai. BTRFS advanced features jaise snapshots aur compression offer karta hai.
    * **Technical Detail**_**:**_ _<mark style="color:blue;">UNIX filesystems hierarchical structure follow karte hain, jisme superblock top-level metadata rakhta hai, inodes file metadata store karte hain, aur directories file names ko inodes se link karte hain. Har filesystem apne block allocation (extent-based ya bitmap-based), journaling (write-ahead logging ya copy-on-write), aur error handling mechanisms ke through optimize hota hai.</mark>_



### <mark style="color:yellow;">Filesystem Internals: Core Concepts</mark>

Filesystem ke internal workings ko samajhne ke liye kuch key concepts hain jo har filesystem mein central hote hain. Inko detailed aur technical lekin simple language mein samjhte hain:



1.  <mark style="color:yellow;">**Superblock**</mark><mark style="color:yellow;">:</mark>\
    Superblock filesystem ka master control block hota hai jo pure **filesystem ke critical metadata ko store karta hai.** Yeh filesystem ka blueprint hai.

    * **Kya Store Hota Hai?**:
      * Filesystem ka total size (bytes mein).
      * Total aur free inodes ki count.
      * Free aur used disk space (blocks mein).
      * Filesystem type (jaise ext4, NTFS), block size, aur mount options.
    *   **Example**: Agar tumhari 1TB hard disk ext4 format mein hai **(ext4 ke case mein typically 5% root ke liye reserved)** aur maan lo ussme 524GB ki storage pre-occupied hai , toh iss case me superblock batata hai ki total raw memory 1024GB hai aur  500GB free hai, 1 million inodes available hain, aur block size 4KB hai.


    * **Technical Detail**: Superblock disk ke fixed location (usually first few sectors) pe store hota hai aur filesystem mount karte time kernel ke through read hota hai. Agar superblock corrupt ho jaye, filesystem mount nahi hoga, kyunki OS ko filesystem ka structure samajh nahi ayega. Modern filesystems (jaise ext4) multiple backup superblocks rakhte hain, jo `fsck` tool (file system check) se recover kiye ja sakte hain. Backup superblocks typically alternate sectors pe store hote hain (jaise sector 32768, 98304).


2.  <mark style="color:yellow;">**Inode**</mark><mark style="color:yellow;">:</mark>\
    Inode (index node) ek file ya directory ka metadata store karta hai, siwaye file name ke, jo directory mein store hota hai.

    * **Kya Store Hota Hai?**:
      * File size (bytes mein).
      * Permissions (read/write/execute for user, group, others).
      * Ownership (User ID, Group ID).
      * Timestamps (creation, modification, access, metadata change).
      * Direct aur indirect data block pointers (jahan file content store hota hai).
    * **Example**: Jab tum “vacation.jpg” open karte ho, filesystem uske inode number (jaise 1234) se metadata (size: 5MB, permissions: read-only, owner: user1) aur data block locations fetch karta hai.
    * **Technical Detail**: Har file ya directory ka unique inode number hota hai, jo disk pe inode table mein store hota hai. Inode table ek fixed-size array hai jo filesystem creation ke time allocate hoti hai. Inode mein typically 12 direct block pointers, 1 single indirect, 1 double indirect, aur 1 triple indirect pointer hote hain, jo large files ke data blocks ko link karte hain. File name directory entry (dentry) mein inode number ke saath map hota hai, jo filesystem ko modular aur efficient banata hai.


3.  **Dentry (Directory Entry)**:\
    Dentry ek filename aur uske corresponding inode number ka mapping hota hai, jo directory mein store hota hai. Yeh file lookup ke liye critical hai.

    * **Example**: Directory `/home/user/photos/` mein “vacation.jpg” ka name aur inode number 1234 store hota hai. Jab tum file open karte ho, filesystem dentry se inode number, phir inode se file data tak jata hai.
    * **Technical Detail**: Dentry Virtual File System (VFS) layer mein cached hota hai taaki frequent lookups fast ho sakein. Dentry structure mein filename, inode number, parent directory, aur caching metadata (jaise cache validity) shamil hota hai. VFS layer filesystem ke path resolution (jaise /home/user/photos/vacation.jpg) ko handle karta hai, jisme dentries key role play karti hain.


4.  **Data Block**:\
    Data blocks filesystem ke woh units hain jahan file ka actual content (text, images, videos) store hota hai. Har file ke data blocks uske inode se linked hote hain.

    * **Example**: “vacation.jpg” ke pixel data ya “notes.txt” ka text content data blocks mein store hota hai. Inode in blocks ke addresses rakhta hai.
    * **Technical Detail**: Data blocks ka size filesystem ke design pe depend karta hai (ext4 mein default 4KB, XFS mein variable). Blocks contiguous (sequential) ya fragmented (scattered) ho sakte hain. Inode ke direct block pointers small files ke liye kaafi hote hain, lekin bade files ke liye indirect blocks use hote hain. Block allocation algorithms (jaise bitmap ya extent-based) storage efficiency aur performance ko optimize karte hain.


5. **Indirection Block**:\
   Indirection block ek special block hai jo large files ke dynamically allocated data blocks ke addresses store karta hai jab inode ke direct block pointers khatam ho jate hain.
   * **Example**: Ek 10GB video file “movie.mp4” ke liye, inode ke 12 direct block pointers khatam hone ke baad single indirect block (jo aur data blocks ke pointers rakhta hai), double indirect, ya triple indirect blocks use hote hain.
   * **Technical Detail**: Indirection blocks hierarchical structure follow karte hain. Single indirect block ek table hai jo data block pointers store karta hai. Double indirect block ek table hai jo single indirect blocks ko point karta hai, aur triple indirect block double indirect blocks ko point karta hai. Yeh design large files (terabytes tak) ko support karta hai, lekin read/write operations mein extra overhead add karta hai kyunki multiple pointer lookups chahiye hote hain.

### Kyun Important Hain Yeh Concepts?

* **Filesystem Organization**: Superblock, inodes, dentries, aur data blocks milke filesystem ko structured aur accessible banate hain, jisse file operations (read, write, delete) efficient hote hain.
* **Security Implications**: Inodes ya superblock mein malicious tampering (jaise malware ya hacking) se filesystem compromise ho sakta hai, jisse data loss, unauthorized access, ya system crash ho sakta hai.
* **Performance**: Data blocks aur indirection blocks ka design read/write speed, storage efficiency, aur scalability ko affect karta hai. Optimized block allocation aur caching (jaise dentries ka VFS caching) performance ko boost karta hai.

### Practical Use Aur Security Measures

Filesystem ke in concepts ko samajhna system design, security, aur maintenance ke liye zaroori hai. Niche kuch practical measures hain:

* **Regular Backups**: Superblock aur inode corruption se bachne ke liye filesystem ka regular backup rakho.
  * **Example**: Tools jaise `rsync` (incremental backups) ya `dd` (full disk image) use karo taaki data safe rahe.
  * **Technical Detail**: Backups mein superblock, inode table, aur data blocks ka snapshot liya jata hai, jo recovery ke liye critical hota hai.
* **Filesystem Checks**: `fsck` tool use karo taaki superblock, inode, aur data block inconsistencies ko detect aur fix kiya ja sake.
  * **Example**: `fsck /dev/sda1` ext4 partition ke errors (jaise corrupt inodes ya bad blocks) ko check aur repair karta hai.
  * **Technical Detail**: `fsck` superblock ke backup copies aur inode table ko scan karta hai taaki inconsistencies (jaise orphaned inodes ya invalid pointers) fix ho sakein.
* **Secure Design**: Filesystem design mein strong metadata validation (jaise checksums) aur error-checking mechanisms add karo taaki malicious changes detect ho sakein.
  * **Example**: Cryptographic checksums (SHA-256) inode aur superblock metadata ke liye use ho sakte hain taaki tampering ka pata chale.
  * **Technical Detail**: Filesystems jaise BTRFS checksums natively support karte hain, jo data integrity check karte hain.
* **Monitoring**: Filesystem ke critical operations (jaise mount, unmount, block allocation) ko monitor karo taaki unauthorized changes ka pata chale.
  * **Example**: Tools jaise `auditd` use karo taaki filesystem events (jaise file creation ya deletion) track ho sakein.
  * **Technical Detail**: Kernel audit subsystem filesystem calls (jaise openat, unlink) ko log karta hai, jo security analysis ke liye useful hai.

### Key Takeaways

* **Filesystem Kya Hai**: Filesystem files ko disk pe organize aur track karta hai using data structures jaise superblock, inodes, dentries, aur data blocks.
* **Core Concepts**:
  * **Superblock**: Filesystem ka master index, jo size, inodes, aur config details rakhta hai.
  * **Inode**: File metadata (size, permissions, timestamps) aur data block pointers store karta hai.
  * **Dentry**: Filename aur inode number ka mapping, jo file lookup ke liye zaroori hai.
  * **Data Block**: File ka actual content store karta hai.
  * **Indirection Block**: Large files ke extra data block pointers manage karta hai.
* **Mahatva**: Yeh concepts filesystem ke organization, security, aur performance ke foundation hain.
* **Security Tips**: Regular backups, `fsck` checks, secure design (checksums), aur monitoring se filesystem safe aur reliable rahega.

***

#### Follow-Up Questions (Agar Aapke Pass Hain)

Agar aapke pass is slide ke related koi sawal hain, toh please share karo. Main unhe Hindi mein, isi structured format mein (direct jawab, examples, details, aur summary ke sath) answer karunga. Niche ek example format hai follow-up questions ke liye:

1. **Sawal**: Superblock corrupt hone se kya hota hai?
   * **Jawab**: Direct answer about superblock corruption effects.
   * **Kaise Hota Hai?**: Explanation of corruption causes (e.g., hardware failure, malware).
   * **Example**: Real-world scenario (e.g., corrupted superblock se filesystem mount nahi hota).
   * **Detail**: Technical breakdown of recovery process (e.g., using backup superblock).
2. **Sawal**: Inodes aur dentries mein kya fark hai?
   * **Jawab**: Short answer on their differences.
   * **Kaise Kaam Karte Hain?**: Explanation of their roles in filesystem.
   * **Example**: How a file lookup uses dentries and inodes.
   * **Detail**: Technical details on their structure and storage.

