---
description: >-
  Os-query is an operating system instrumentation framework for Windows, OS X
  (macOS), and Linux. The tools make low-level operating system analytics and
  monitoring both performant and intuitive.
---

# OS - Query

## <mark style="color:green;">**Introduction**</mark>

<mark style="color:yellow;">**Os-query exposes an operating system as a high-performance relational database.**</mark> This allows you to write SQL queries to explore operating system data.

With Os-query, SQL tables represent abstract concepts such as -&#x20;

1. Running processes
2. Loaded kernel modules
3. Open network connections&#x20;
4. Browser plugins
5. Hardware events
6. File hashes

### _You can download Os-query from ->_ [_https://osquery.io/_](https://osquery.io/)&#x20;

## <mark style="color:green;">**Features of Os-query**</mark>

**1. Distributed Host Monitoring with&#x20;**<mark style="color:red;">**osqueryd**</mark>

* **Purpose:**
  * Schedule and execute queries across your entire infrastructure.
  * Maintain insight into security, performance, configuration, and state changes.
* **Key Capabilities:**
  * Aggregates query results over time.
  * Generates logs indicating infrastructure state changes.
  * Integrates seamlessly into your log aggregation pipeline via a **robust plugin architecture**.

_<mark style="color:blue;">In simple terms osqueryd is a tool that lets you run checks (queries) on all your computers and servers to see how they’re doing & keeps track of changes over time and creates logs to show what’s different.</mark>_

_<mark style="color:blue;">Why it’s useful?</mark>_

* _<mark style="color:blue;">You can use these logs to monitor security, performance, and system settings.</mark>_
* _<mark style="color:blue;">It works with whatever log system you already use, thanks to its flexible plugin system.</mark>_

***

**2. Interactive Query Console with&#x20;**<mark style="color:red;">**osqueryi**</mark>

* **Purpose:**
  * Provides a SQL-based interactive console for system exploration and debugging.
* **Use Cases:**
  * Incident response.
  * Diagnosing system operations issues.
  * Troubleshooting performance problems.
* **Features:**
  * Full SQL language support.
  * Dozens of prebuilt system tables for ease of querying.

***

**3. Cross-Platform Support**

* **Supported Platforms:**
  * Windows, macOS, Ubuntu, CentOS, and other enterprise Linux distributions.
* **Benefits:**
  * Unified monitoring across varied infrastructure (Windows/macOS clients and Linux servers).
  * Leverages low-level operating system APIs.

***

**4. Native Packages for Easy Deployment**

* **Out-of-the-Box Availability:**
  * Prebuilt native packages for all supported operating systems.
* **Customization Support:**
  * Extensive tooling and documentation for creating and deploying custom packages.

***

**5. Flexible Deployment and Custom Integration**

* **Ease of Rollout:**
  * Comprehensive O**s-query user guide** with deployment documentation.
* **Customizability:**
  * Environment-specific features are hot-swappable at runtime via custom plugins.
  * Supports deep infrastructure integration through **existing or custom plugins**.

***

**6. High-Performance Modular Codebase**

* **Features:**
  * Built with modular components and documented public APIs.
  * Components can be recombined to create new applications and tools.
* **Language Binding Support:**
  * Bindings for multiple languages via a **Thrift interface**.
  * Allows the use of familiar technologies for tool development.
