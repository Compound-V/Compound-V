# Poking the Filesystem slides and Structure of Linux Filesystem Stack

```markdown
# Linux Filesystem Stack

│
├── 1. USER SPACE
│   │
│   ├── 1.1 Applications
│   │   ├── Tools: cp, mv, cat, vim, etc.
│   │   ├── Use syscalls via libc (open, read, write)
│   │   └── Interact with files, not the disk directly
│   │
│   ├── 1.2 Shells (bash, zsh, fish)
│   │   ├── Executes file commands (ls, echo, redirection)
│   │   └── Uses fork, exec, wait system calls
│   │
│   └── 1.3 Standard C Library (glibc / musl)
│       ├── Provides wrappers for syscalls
│       ├── open() → syscall(SYS_openat)
│       ├── read(), write(), close(), etc.
│       └── Abstracts low-level syscall interface
│
├── 2. VFS (Virtual Filesystem Switch)
│   │
│   ├── 2.1 Purpose
│   │   ├── Abstract layer for all filesystems
│   │   └── Provides a uniform API to user-space
│   │
│   ├── 2.2 Core Structures
│   │   ├── super_block → Mounted filesystem
│   │   ├── inode       → Represents a file on disk
│   │   ├── dentry      → Maps pathnames to inodes
│   │   └── file        → Represents open file handle (per process)
│   │
│   ├── 2.3 Caches
│   │   ├── dcache → Dentry cache (path lookup)
│   │   └── icache → Inode cache
│   │
│   └── 2.4 Operation Tables
│       ├── file_operations     → read(), write(), mmap(), etc.
│       ├── inode_operations    → create(), lookup(), link(), etc.
│       └── super_operations    → mount(), statfs(), write_super(), etc.
│
├── 3. FILESYSTEM IMPLEMENTATIONS
│   │
│   ├── 3.1 Local Filesystems
│   │   ├── ext4, XFS, Btrfs, F2FS
│   │   ├── Handle block allocation, journaling, metadata
│   │   └── Ext4 Example:
│   │       ├── Journaling (via JBD2)
│   │       ├── Extents (for space efficiency)
│   │       ├── HTree indexing for directories
│   │       └── Delayed allocation
│   │
│   ├── 3.2 Network Filesystems
│   │   ├── NFS → Remote mount using RPC
│   │   ├── CIFS/SMB → Windows-compatible sharing
│   │   └── FUSE → User-space filesystem support
│   │
│   └── 3.3 Virtual / Pseudo Filesystems
│       ├── procfs → /proc (process info)
│       ├── sysfs  → /sys (kernel objects)
│       └── tmpfs  → In-memory file store (RAM disk)
│
├── 4. PAGE CACHE (In-Memory File Cache)
│   │
│   ├── 4.1 Purpose
│   │   ├── Speeds up file access by avoiding disk I/O
│   │   └── Shared across all processes and filesystems
│   │
│   ├── 4.2 Write Path
│   │   ├── App writes → kernel buffers page in RAM
│   │   ├── Page marked dirty
│   │   └── Flushed to disk later by writeback daemon
│   │
│   ├── 4.3 Read Path
│   │   ├── If page in cache → served from RAM
│   │   └── If not → fetched from disk into page cache
│   │
│   └── 4.4 Writeback / Flushers
│       ├── flush-<device> threads
│       ├── kswapd → Frees memory under pressure
│       ├── sync / fsync / msync → User-level flush triggers
│       └── drop_caches → Clear caches via proc interface
│
├── 5. BLOCK LAYER
│   │
│   ├── 5.1 Purpose
│   │   ├── Middle layer between FS and drivers
│   │   └── Manages I/O queues and scheduling
│   │
│   ├── 5.2 Core Structures
│   │   ├── bio         → Block I/O operation structure
│   │   ├── request     → Merged and optimized I/O
│   │   ├── queue       → Device-specific request queue
│   │   └── elevator    → I/O scheduler (noop, deadline, BFQ)
│   │
│   ├── 5.3 Features
│   │   ├── I/O merging, reordering
│   │   ├── Prioritization and throttling
│   │   └── blk-mq → Multiqueue support for SSDs/NVMe
│   │
│   └── 5.4 Key APIs
│       ├── submit_bio()
│       └── blk_execute_rq()
│
├── 6. BLOCK DEVICE DRIVERS
│   │
│   ├── 6.1 Role
│   │   ├── Interface with hardware (disks, SSDs)
│   │   └── Convert bio → hardware-specific protocol
│   │
│   ├── 6.2 Responsibilities
│   │   ├── DMA setup
│   │   ├── Queue management
│   │   ├── Interrupt handling
│   │   └── Register/MMIO interaction
│   │
│   ├── 6.3 Examples
│   │   ├── sdX     → SCSI/SATA devices
│   │   ├── nvmeXnY → NVMe devices
│   │   ├── loopX   → File-backed devices
│   │   └── srX     → CD/DVD-ROM
│   │
│   └── 6.4 Debug Tools
│       ├── lsblk, blkid, udevadm
│       ├── /sys/block/, /dev/, /proc/partitions
│       └── hdparm, iostat
│
└── 7. PHYSICAL STORAGE HARDWARE
    │
    ├── 7.1 Types
    │   ├── HDD → Magnetic platters, moving head
    │   ├── SSD → NAND flash with FTL
    │   ├── NVMe → PCIe interface, parallel I/O
    │   ├── USB / SD Cards → External, plug-and-play
    │   └── RAID → Redundant array of drives
    │
    ├── 7.2 Components
    │   ├── Platters / NAND chips
    │   ├── Firmware
    │   └── Sector layout (512B or 4K)
    │
    └── 7.3 Stores
        ├── Raw file data
        ├── Superblocks and metadata
        ├── Journals and logs
        └── Boot sectors, partitions, extents
```

***

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption><p>Complete Linux filesystem stack</p></figcaption></figure>

**Slide 1**

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

**Slide 2**

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

**Slide 3**

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

Slide 4

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

Slide 5

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

Slide 6

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

Slide 7

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

Slide 8

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

Slide 9

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>
