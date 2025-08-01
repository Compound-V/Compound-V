# Types of Filesystem

### 📦 1. General File System Structure Recap

Har modern file system ke paas kuch **common components** hote hain:

| Component            | Kaam kya karta hai                                    |
| -------------------- | ----------------------------------------------------- |
| **Superblock**       | FS ke meta info: size, UUID, block size, features     |
| **Inode**            | Har file/folder ka meta info: timestamps, perms, size |
| **Data Blocks**      | Actual content of files                               |
| **Directory**        | Filename → inode mapping                              |
| **Bitmap/Freemap**   | Kaunsa block free/used                                |
| **Journal/COW Tree** | Metadata consistency (journaling ya copy-on-write)    |

***

### 🧱 2. FAT32 – Simplicity King (Old is Gold)

**Use Case**: USB drives, memory cards, UEFI boot

| Feature           | Details                                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| **Superblock**    | Boot sector (first 512 bytes) mein hota hai FS info (volume label, sectors/cluster, etc.)              |
| **Inode nahi**    | No inodes. Directory entry hi file metadata carry karta hai                                            |
| **FAT Table**     | File Allocation Table: ek linked-list type structure jahan har cluster ka next cluster number hota hai |
| **No Journaling** | Koi safety nahi, corruption pe khud hi ro le                                                           |

**Limitation**:

* File size limit: 4 GB
* Volume size limit: 2–32 GB
* Poor recovery

***

### 🧱 3. exFAT – FAT32 ka Modern Bhai

**Use Case**: Modern USBs, cameras, UEFI systems

| Feature                                                    | Details                                                        |
| ---------------------------------------------------------- | -------------------------------------------------------------- |
| **Same FAT Concept**                                       | Still uses a FAT table, but 32→64 bit                          |
| **Cluster Bitmap**                                         | Introduced for free space management (better than linear scan) |
| **Directory Entries**                                      | More flexible and Unicode-support                              |
| **No journaling**                                          | Still risky but faster                                         |
| **Max file size**: 16 EB (practically way more than FAT32) |                                                                |

***

### 🧱 4. NTFS – Windows ka Powerhouse

**Use Case**: Windows OS default FS

| Feature                                     | Details                                                         |
| ------------------------------------------- | --------------------------------------------------------------- |
| **Master File Table (MFT)**                 | Sab kuch ek table mein – har file/folder is an entry in MFT     |
| **Attribute-based**                         | File metadata, data, security – sab kuch attribute ke form mein |
| **$LogFile**                                | Transaction-based journaling                                    |
| **Bitmap for allocation**                   | For clusters and MFT entries                                    |
| **Indexing via B+ trees**                   | Directory listing, lookup speed optimized                       |
| **Compression, encryption, ACL** – built-in |                                                                 |

**Advanced**: NTFS supports Alternate Data Streams (ADS), very flexible structure, self-healing metadata via `chkdsk`.

***

### 🧱 5. ZFS – The Tank

**Use Case**: Enterprise storage, snapshots, NAS, backup

| Feature                                        | Details                                              |
| ---------------------------------------------- | ---------------------------------------------------- |
| **No block groups/AGs**                        | Pura storage ek "pool" hai                           |
| **Uberblock**                                  | Superblock ka big brother – multiple versions stored |
| **Everything checksummed**                     | Metadata + data integrity with strong hashes         |
| **Copy-on-Write (COW)**                        | Every write creates new blocks; ensures atomicity    |
| **Transactional Model**                        | ZIL (ZFS Intent Log), dataset tree, indirect blocks  |
| **Snapshots, clones, RAIDZ**, dedup – built-in |                                                      |

**ZFS ka structure** is very different: everything is **object-based**, no classic inode/block group concept.

***

### 🧱 6. F2FS – Flash-Friendly FS (Android favorite)

**Use Case**: Android phones, SSD/Flash-based systems

| Feature                | Details                                                                  |
| ---------------------- | ------------------------------------------------------------------------ |
| **Segmented design**   | Storage ko segments mein divide karta hai – for better flash performance |
| **Node + Data**        | File = Node blocks + data blocks, metadata = separate                    |
| **NAT/SIT tables**     | Node Address Table, Segment Info Table → for mapping and wear leveling   |
| **Checkpoint**         | Journal-style checkpointing for crash recovery                           |
| **Garbage Collection** | Flash block reuse ke liye automatic GC                                   |

***

### 🧱 7. ReiserFS – Metadata Monster

**Use Case**: Outdated but innovative (old SUSE systems used this)

| Feature                     | Details                                                     |
| --------------------------- | ----------------------------------------------------------- |
| **All metadata in B+ tree** | Inodes, directory, file data sab B+tree mein                |
| **Tail packing**            | Small files ko ek block mein compress karke store karta hai |
| **Journaled metadata**      | Fast metadata operations, journaling support                |
| **Bad maintenance**         | Project dead ho gaya, dev bhi jail gaya 💀                  |

***

### 🧱 8. JFS (IBM's Journaled FS)

**Use Case**: IBM servers, legacy systems

| Feature                             | Details                                  |
| ----------------------------------- | ---------------------------------------- |
| **Extent-based allocation**         | Similar to extents in ext4               |
| **B+ tree indexing**                | Directory structure is fast and scalable |
| **Very efficient journal**          | Lightweight journaling overhead          |
| **Good performance on SMP systems** | Designed for big iron servers            |

***

### 🧾 9. In-Depth Comparative Table

<table data-full-width="true"><thead><tr><th>Feature</th><th>FAT32</th><th>exFAT</th><th>NTFS</th><th>Ext4</th><th>XFS</th><th>Btrfs</th><th>ZFS</th><th>F2FS</th><th>JFS</th></tr></thead><tbody><tr><td>Journaling</td><td>❌</td><td>❌</td><td>✅</td><td>✅ (jbd2)</td><td>✅</td><td>✅ (COW)</td><td>✅ (ZIL)</td><td>✅ (CPT)</td><td>✅</td></tr><tr><td>Max file size</td><td>4 GB</td><td>16 EB</td><td>16 EB</td><td>16 TiB</td><td>8 EiB</td><td>16 EiB</td><td>16 EiB</td><td>3.9 TiB</td><td>4 PiB</td></tr><tr><td>Snapshots</td><td>❌</td><td>❌</td><td>⚠️ (Volume Shadow Copy)</td><td>❌</td><td>❌</td><td>✅</td><td>✅</td><td>❌</td><td>❌</td></tr><tr><td>Metadata indexing</td><td>Linear</td><td>Cluster</td><td>B+ tree</td><td>HTree</td><td>B+ tree</td><td>B-trees</td><td>Indirect Obj</td><td>NAT/SIT</td><td>B+ tree</td></tr><tr><td>COW</td><td>❌</td><td>❌</td><td>❌</td><td>❌</td><td>❌</td><td>✅</td><td>✅</td><td>❌</td><td>❌</td></tr><tr><td>Checksums (data/meta)</td><td>❌</td><td>❌</td><td>⚠️ partial</td><td>✅ (opt)</td><td>❌</td><td>✅ (all)</td><td>✅ (strong)</td><td>✅ (meta)</td><td>❌</td></tr><tr><td>Wear Leveling aware</td><td>❌</td><td>❌</td><td>❌</td><td>❌</td><td>❌</td><td>❌</td><td>❌</td><td>✅</td><td>❌</td></tr><tr><td>ACL/Security features</td><td>❌</td><td>❌</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr></tbody></table>

***

### 🧠 Final Advice:

| Use-case                        | Recommended FS |
| ------------------------------- | -------------- |
| Old device/UEFI boot            | FAT32          |
| Large USB drive (Windows/macOS) | exFAT          |
| Windows OS + ACL/security       | NTFS           |
| Linux General purpose FS        | Ext4           |
| Linux servers, parallel IO      | XFS            |
| Modern Linux, snapshots, RAID   | Btrfs          |
| Enterprise, NAS, ZRAID          | ZFS            |
| Android/Flash devices           | F2FS           |
| Legacy IBM systems              | JFS            |

***
