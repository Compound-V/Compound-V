---
description: >-
  osqueryi provides a set of built-in virtual tables that represent various
  system data, along with commands to explore and interact with them.
---

# Osqueryi Table

## <mark style="color:red;">**Commands for Interacting with Tables**</mark>

*   **List All Tables**

    * Displays all available tables in the current osqueryi session.&#x20;

    ```sql
    .tables
    ```



*   **View Table Schema**

    * Shows the schema (structure) of a specified table. This command provides detailed column information (data types and descriptions) for each table.

    ```sql
    .schema <table_name>
    ```

    *   Example:

        ```sql
        .schema processes
        ```



*   **Search for Tables by Keyword**

    * Allows you to search for tables related to a specific keyword. This is useful when you’re unsure of which table to query.

    ```sql
    .tables <keyword>
    ```

    *   Example:

        ```sql
        .tables network
        ```



*   **Query Table Data**

    * Executes standard SQL queries to extract data from any available table.

    ```sql
    SELECT * FROM <table_name>;
    ```

    *   Example:

        ```sql
        SELECT * FROM processes;
        ```



*   **Describe Built-In Help**

    * Displays a list of all available commands and their usage.

    ```sql
    .help
    ```



*   **Filter Data**

    * Apply filters using `WHERE` clauses to narrow the data based on specific conditions.

    ```sql
    SELECT * FROM processes WHERE name LIKE '%nginx%';
    ```



*   **Sort and Limit Results**

    * Use `ORDER BY` and `LIMIT` to sort and restrict the number of query results.

    ```sql
    SELECT * FROM processes ORDER BY pid LIMIT 10;
    ```



*   **Count Rows in a Table**

    * Get a count of the number of rows in a table (or after applying filters).

    ```sql
    SELECT COUNT(*) FROM processes;
    ```

***

## <mark style="color:red;">**Expanded List of Tables**</mark>

| <mark style="color:yellow;">**Table Name**</mark> | <mark style="color:yellow;">**Description**</mark>                                                     |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `processes`                                       | Details of running processes.                                                                          |
| `users`                                           | List of system user accounts & details related.                                                        |
| `logged_in_users`                                 | Displays users currently logged into the system, including login time and terminal.                    |
| `listening_ports`                                 | Active listening network ports and associated services.                                                |
| `process_open_sockets`                            | Network sockets opened by running processes, with details on local/remote ports and addresses.         |
| `file`                                            | Metadata of files, such as file path, size, permissions, and timestamp information.                    |
| `file_events`                                     | Tracks events on file access and modifications (requires file integrity monitoring setup).             |
| `kernel_modules`                                  | Displays loaded kernel modules (e.g., drivers), along with memory usage and dependencies.              |
| `crontab`                                         | Lists cron jobs, showing scheduled tasks and their execution times (Linux/macOS).                      |
| `windows_events`                                  | Query Windows Event Logs for system or application events (Windows only).                              |
| `os_version`                                      | Provides details about the OS version, architecture, and build details.                                |
| `programs`                                        | Installed programs on the system (Windows-specific).                                                   |
| `etc_hosts`                                       | Parses the `/etc/hosts` file to list IP and hostname mappings.                                         |
| `etc_services`                                    | Lists entries in `/etc/services`, mapping port numbers to service names.                               |
| `hash`                                            | Computes and retrieves cryptographic hashes (MD5, SHA1, SHA256) for file integrity checks.             |
| `groups`                                          | Lists all user groups in the system and their associated GID.                                          |
| `shadow`                                          | Reads `/etc/shadow` for password hashes, aging, and other account-related data (requires permissions). |
| `uptime`                                          | Shows the system's uptime, load averages, and running time since boot.                                 |
| `system_info`                                     | Basic hardware and system information, including hostname, CPU, memory, and architecture.              |
| `network_interfaces`                              | Lists network interfaces, IP addresses, MAC addresses, and interface statuses.                         |
| `mounts`                                          | Displays mounted filesystems, including device names, mount points, and filesystem types.              |
| `disk_encryption`                                 | Details about disk encryption status (if supported).                                                   |
| `apt_sources`                                     | Lists APT package sources (Debian/Ubuntu systems).                                                     |
| `rpm_packages`                                    | Lists installed RPM packages on Red Hat-based systems.                                                 |
| `service`                                         | Displays details about services running on the system, including the status and the process ID (PID).  |

***

## <mark style="color:red;">**Advanced Query Examples**</mark>



*   **List All Running Processes**

    * Retrieves detailed information about each running process on the system.

    ```sql
    SELECT pid, name, path, cmdline, memory, cpu_percent FROM processes;
    ```



*   **Find Processes by Name**

    * Search for processes that contain a specific term in their name (e.g., "nginx").

    ```sql
    SELECT pid, name, path FROM processes WHERE name LIKE '%nginx%';
    ```



*   **Check Active Listening Ports (TCP)**

    * Lists all active listening TCP ports and their associated services.

    ```sql
    SELECT pid, local_address, local_port, protocol FROM listening_ports WHERE protocol = 'tcp';
    ```



*   **Identify Users with Sudo Privileges (Linux)**

    * Find users with administrative privileges (UID=0).

    ```sql
    SELECT username, uid, groups FROM users WHERE uid = 0;
    ```



*   **Audit File Integrity Changes (Linux)**

    * Monitor changes to critical files like `/etc/passwd` (with file integrity monitoring enabled).

    ```sql
    SELECT * FROM file_events WHERE path = '/etc/passwd' AND action = 'MODIFIED';
    ```



*   **Check Kernel Modules**

    * Retrieve a list of loaded kernel modules with details such as memory usage.

    ```sql
    SELECT name, size, used_by FROM kernel_modules;
    ```



*   **View Installed Software on Windows**

    * Get a list of installed programs on a Windows system.

    ```sql
    SELECT name, version, install_date FROM programs;
    ```



*   **List Cron Jobs (Linux)**

    * Retrieve scheduled cron jobs on Linux or macOS.

    ```sql
    SELECT minute, hour, day, month, weekday, command FROM crontab;
    ```



*   **Display System Information**

    * View basic information about the system, including the hostname, OS version, and uptime.

    ```sql
    SELECT * FROM system_info;
    ```



*   **Analyze Network Interface Details**

    * Retrieve information about all network interfaces and their statuses.

    ```sql
    SELECT name, address, broadcast, mtu FROM network_interfaces;
    ```



*   **File Integrity Monitoring for Sensitive Files**

    * Monitor access to critical files, like `/etc/hosts`.

    ```sql
    SELECT path, atime, mtime FROM file WHERE path = '/etc/hosts';
    ```



*   **List Recently Mounted Filesystems**

    * View all mounted filesystems along with their options.

    ```sql
    SELECT device, mountpoint, fstype FROM mounts WHERE fstype = 'ext4';
    ```

***

## <mark style="color:red;">**Joining Tables for More Complex Queries**</mark>

*   **Join Processes with Users**

    * Combine data from the `processes` and `users` tables to find out which user owns which process.

    ```sql
    SELECT p.pid, p.name, u.username 
    FROM processes p 
    JOIN users u 
    ON p.uid = u.uid;
    ```



*   **Correlating Network and Process Information**

    * Match processes with their open network sockets (e.g., find the process using a particular port).

    ```sql
    SELECT p.name, ps.local_address, ps.local_port 
    FROM processes p
    JOIN process_open_sockets ps
    ON p.pid = ps.pid
    WHERE ps.local_port = 8080;
    ```



* **Correlating Process, User, and Network Information** &#x20;
  * This query retrieves the process details, associated user, and the open network sockets, providing information about the processes, their users, and the ports they are using.

```sql
SELECT p.pid, p.name, u.username, ps.local_address, ps.local_port
FROM processes p
JOIN users u ON p.uid = u.uid
JOIN process_open_sockets ps ON p.pid = ps.pid;
```

***

#### **Additional Features**

1. **Joins and Subqueries**\
   osqueryi allows for powerful SQL operations, including joins across multiple tables and subqueries for advanced data retrieval.
2. **Real-Time File Integrity Monitoring (FIM)**\
   By integrating with file monitoring, osquery can track file modifications in real-time. For instance, `file_events` can be used to track changes to sensitive files like `/etc/passwd`.
3. **Cross-Platform Capabilities**\
   osqueryi is cross-platform (Windows, macOS, Linux), so the same queries and tables can be applied across various environments.
4. **System and Network Health Monitoring**\
   With tables like `system_info`, `listening_ports`, `network_interfaces`, and `process_open_sockets`, you can monitor overall system health and network performance.
