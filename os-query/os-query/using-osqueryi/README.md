---
description: >-
  osqueryi is the interactive query interface for the osquery tool. It provides
  a SQL-like environment where users can explore their operating system and
  query system data in real time.
---

# Using osqueryi

## <mark style="color:yellow;">Introduction</mark>

<mark style="color:red;">**osqueryi**</mark>**&#x20;is the osquery interactive console/shell.**&#x20;

In this mode, Os-query is completely standalone, does not communicate with a daemon[^1], and does not need to run as an administrator (although some tables may return fewer results when running as non-administrator).

<mark style="color:orange;">**How It Differs From osqueryd ?**</mark>

* **osqueryi**: Meant for ad-hoc, real-time exploration and testing. It’s an interactive tool.
* **osqueryd**: A daemon that runs scheduled queries, collects results over time, and integrates with logging systems for continuous monitoring.

#### you can download Os-query from -> [https://osquery.io/](https://osquery.io/)

**Launch osqueryi -> Open a terminal or command prompt and run** `osqueryi` **to start the interactive shell.**

## <mark style="color:yellow;">Key Features</mark>

* **Interactive SQL Shell**: Run real-time queries to explore system data.
* [**Pre-Built Tables**](osqueryi-table.md): Access system info like processes, users, and network connections.
* **Ad-Hoc Querying**: Perform quick investigations without setup.
* **Cross-Platform**: Works on Windows, macOS, Linux, and more.
* **Fast and Lightweight**: Instant results with minimal overhead.
* **Query Testing**: Test queries before deploying them in osqueryd.
* **SQL Syntax**: Uses familiar SQL commands for ease of use.

## <mark style="color:yellow;">**Osqueryi Use Cases**</mark>

1. **Incident Response**: Investigate suspicious activities.
2. **System Debugging**: Diagnose performance and configuration issues.
3. **Security Auditing**: Identify vulnerabilities and misconfigurations.
4. **Compliance Checks**: Ensure systems meet policies.
5. **Query Testing**: Develop and validate queries.
6. **Forensics**: Analyze logs, file integrity, and network activity.
7. **Inventory Management**: Report on software, hardware, and system states.





[^1]: A **daemon** is a background process that runs independently to perform system or service-related tasks.
