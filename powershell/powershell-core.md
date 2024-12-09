---
description: This document covers for PowerShell (Core)
---

# Powershell (Core)

## INTRODUCTION

**For installation instructions or updates, refer to** [**Microsoft Learn**](https://learn.microsoft.com/en-us/powershell/)

### <mark style="color:blue;">**PowerShell 1.0 (Released November 14, 2006)**</mark>

**Key Features**:

* Introduced object-oriented scripting using cmdlets (`Get-Process`, `Set-Service`).
* Enabled task automation through pipelines and object-based output.
* Focused primarily on system administration for Windows XP SP2, Vista, and Server 2003.

**Limitations**:

* No remoting or advanced debugging.
* Integration with third-party tools was minimal.

***

### <mark style="color:blue;">**PowerShell 2.0 (October 2009)**</mark>

**Key Features**:

* **Remoting**: Allowed remote execution via WS-Management protocol.
* **ISE**: Added an Integrated Scripting Environment for debugging and scripting.
* Introduced background jobs and advanced module support (`Import-Module`, `New-PSSession`).
* Improved security through script signing.

**Compatibility**:\
Pre-installed on Windows 7 and Windows Server 2008 R2; available for older systems like XP SP3.

***

### <mark style="color:blue;">**PowerShell 3.0 (September 2012)**</mark>

**Key Features**:

* Workflow automation for long-running tasks.
* Enhanced IntelliSense in ISE.
* Automatic module loading.
* New cmdlets for Windows Management Framework, expanding the library to over 2,300 cmdlets.

**Compatibility**:\
Pre-installed on Windows 8 and Windows Server 2012; supported on Windows 7 SP1.

***

### <mark style="color:blue;">**PowerShell 4.0 (October 2013)**</mark>

**Key Features**:

* Introduced **Desired State Configuration (DSC)** for declarative management of infrastructure.
* Enhanced debugging tools and third-party system integrations.

**Compatibility**:\
Bundled with Windows 8.1 and Windows Server 2012 R2.

***

### <mark style="color:blue;">**PowerShell 5.0 (February 2016)**</mark>

**Key Features**:

* Added package management capabilities like Chocolatey.
* Improved DSC with partial configurations.
* New cmdlets for registry, file operations, and system security improvements.

**Compatibility**:\
Pre-installed on Windows 10 and Server 2016.

***

### <mark style="color:blue;">**PowerShell 5.1 (January 2017)**</mark>

**Key Features**:

* Enhanced **remoting** with SSH.
* Introduced cross-platform plans by transitioning to PowerShell Core.
* Improved Windows PowerShell backward compatibility.

**Compatibility**:\
Included in Windows 10 (Anniversary Update).

***

### <mark style="color:blue;">**PowerShell Core 6.0 (January 2018)**</mark>

**Key Features**:

* First cross-platform version (Windows, macOS, Linux).
* Based on .NET Core, enabling lightweight and modular automation.
* Enhanced performance and open-source module support.

***

### <mark style="color:blue;">**PowerShell 7.0 (March 4, 2020)**</mark>

**Key Features**:

* Unified the development of PowerShell Core and Windows PowerShell.
* Introduced pipeline parallelization (`ForEach-Object -Parallel`).
* Added null-coalescing operators (`??`, `??=`) for efficient scripting.
* Improved error handling (`try`, `catch`, `finally`).

***

### <mark style="color:blue;">**PowerShell 7.1 (November 11, 2020)**</mark>

**Key Features**:

* Enhanced usability with experimental features like PSReadLine 2.2.
* Improved compatibility with older Windows PowerShell modules.

***

### <mark style="color:blue;">**PowerShell 7.2 (November 8, 2021)**</mark>

**Key Features**:

* Enabled updates via Microsoft Update.
* Introduced performance improvements and better security for remoting.
* Improved DSC capabilities as a separate gallery module.

***

### <mark style="color:blue;">**PowerShell 7.3 (November 9, 2022)**</mark>

**Key Features**:

* Enhanced predictive IntelliSense for command-line input.
* Improved error messaging and module compatibility.

***

### <mark style="color:blue;">**PowerShell 7.4.6 (Latest Stable)**</mark>

**Key Features**:

* Critical fixes and improved stability for cross-platform automation.
* Enhanced support for Azure, bulk data processing, and OpenSSH features.

**Compatibility**:\
Available across Windows, macOS, and Linux platforms but excludes older Windows systems like 7 and 8.

​

