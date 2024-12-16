---
description: Basics and Terms
---

# Microsoft PowerShell Notes

### Overview of PowerShell

PowerShell is a task automation and configuration management framework developed by Microsoft. It includes a command-line shell and an associated scripting language.

**PowerShell ISE (Integrated Scripting Environment):**

* Used for scripting and testing commands.
* Allows users to run multiple commands simultaneously.
* A script in PowerShell is essentially a collection of commands that can be executed together.

***

#### [PowerShell Cmdlets: A Detailed Guide](./#powershell-cmdlets-a-detailed-guide)

[**PowerShell IntelliSense Overview**](./#powershell-intellisense-overview)



***

### Using Cmdlets and Piping

* **Cmdlet Execution:** Cmdlets can be executed directly in the PowerShell terminal.
* **Piping (|):**
  * The pipe character `|` passes the output of one cmdlet as input to another.
  * Example: `Get-Process | Measure-Object` counts the number of processes running.

#### Example Commands:

1.  **Get All Commands:**

    ```
    Get-Command
    ```

    * Lists all available commands in the session.
2.  **Count Commands:**

    ```
    Get-Command | Measure-Object
    ```

    * Displays the total number of commands available.
3.  **List Imported Commands:**

    ```
    Get-Command -ListImported | Measure-Object
    ```

    * Shows commands imported in the current session.

***

### PowerShell Modules

#### What Are Modules?

Modules are containers for cmdlets, providers, functions, workflows, variables, and more. They extend the functionality of PowerShell.

#### Types of Modules:

1. **Available Modules:** Modules present on the system but not loaded into the current session.
2. **Imported Modules:** Modules loaded into the current session.

#### Listing Modules:

1.  **List Modules in Current Session:**

    ```
    Get-Module
    ```
2.  **List All Available Modules:**

    ```
    Get-Module -ListAvailable
    ```

#### Importing Modules:

* **Automatic Import:**
  * In PowerShell 5.0 and above, modules are automatically imported when you use a cmdlet from that module.
*   **Manual Import:**

    ```
    Import-Module ModuleName
    ```

    * Example: `Import-Module ActiveDirectory`

#### Listing Commands in a Module:

```
Get-Command -Module ModuleName
```

* Example: `Get-Command -Module NetTCPIP` lists all cmdlets in the `NetTCPIP` module.

#### Downloading Missing Modules:

* Use the **PowerShell Gallery** to find and install modules.
*   Example:

    ```
    Install-Module -Name ModuleName
    ```

    * Example: `Install-Module -Name Pester`

#### Commonly Used Modules:

1. **Microsoft.PowerShell.Management** - Commands for system management (e.g., `Get-Service`, `Stop-Process`).
2. **Microsoft.PowerShell.Utility** - Utility cmdlets (e.g., `Format-List`, `Sort-Object`).
3. **ActiveDirectory** - Manage Active Directory resources.
4. **NetTCPIP** - Networking cmdlets (e.g., `Get-NetIPAddress`, `New-NetRoute`).
5. **PSReadLine** - Enhances the command-line experience with features like syntax highlighting and history search.

***

### Exploring and Using Commands

#### Get-Help

* Provides detailed information about cmdlets.
*   Example:

    ```
    Get-Help Get-Process
    ```
*   Use `-Online` to access documentation from the Microsoft website:

    ```
    Get-Help Get-Process -Online
    ```

#### Aliases:

* PowerShell allows aliases (shortcuts) for cmdlets.
* Example: `ls` is an alias for `Get-ChildItem`.
*   List all aliases:

    ```
    Get-Alias
    ```

#### Examples of Frequently Used Cmdlets:

1.  **Managing Processes:**

    ```
    Get-Process
    Stop-Process -Name ProcessName
    ```
2.  **File System Management:**

    ```
    Get-ChildItem -Path C:\ -Recurse
    Copy-Item -Path SourcePath -Destination DestinationPath
    ```
3.  **Service Management:**

    ```
    Get-Service
    Start-Service -Name ServiceName
    Stop-Service -Name ServiceName
    ```
4.  **Network Management:**

    ```
    Get-NetIPAddress
    Test-NetConnection -ComputerName google.com
    ```
5.  **Event Logs:**

    ```
    Get-EventLog -LogName Application
    Clear-EventLog -LogName Application
    ```

***

### Advanced Techniques

#### Variables:

* Variables in PowerShell are prefixed with `$`.
*   Example:

    ```
    $name = "John Doe"
    Write-Output $name
    ```

#### Loops:

1.  **For Loop:**

    ```
    For ($i = 0; $i -lt 5; $i++) {
        Write-Output $i
    }
    ```
2.  **Foreach Loop:**

    ```
    $items = 1..5
    Foreach ($item in $items) {
        Write-Output $item
    }
    ```

#### Functions:

* Functions allow you to encapsulate reusable logic.
*   Example:

    ```
    Function Get-Greeting {
        Param ([string]$Name)
        "Hello, $Name!"
    }

    Get-Greeting -Name "Alice"
    ```

#### Error Handling:

*   **Try-Catch:**

    ```
    Try {
        Get-Item -Path "C:\NonExistentFile.txt"
    } Catch {
        Write-Error "An error occurred: $_"
    }
    ```

#### Scheduling Tasks:

* Use the `ScheduledTasks` module to automate recurring tasks.
*   Example:

    ```
    New-ScheduledTaskTrigger -Daily -At 9am
    Register-ScheduledTask -Action (New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File Script.ps1") -Trigger $trigger -TaskName "MyTask"
    ```

***

### Best Practices

1. **Use Verb-Noun Convention:** Always follow the standard naming convention for cmdlets and functions.
2.  **Comment Your Scripts:**

    ```
    # This script retrieves all running processes
    Get-Process
    ```
3. **Use `Get-Help` for Documentation:** Ensure you understand cmdlets before using them.
4. **Test Scripts in ISE:** Always test scripts in a controlled environment before deploying.
5. **Use Error Handling:** Implement `Try-Catch` blocks to gracefully handle errors.
6. **Avoid Hardcoding:** Use variables and parameters for flexibility.
