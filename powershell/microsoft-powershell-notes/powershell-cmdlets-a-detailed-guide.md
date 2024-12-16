---
description: This guide provides a comprehensive overview of PowerShell cmdlets
---

# PowerShell Cmdlets: A Detailed Guide

### What Are Cmdlets?

Cmdlets are lightweight commands in PowerShell that perform specific functions. They are designed as specialized .NET classes and are the building blocks of PowerShell scripting and automation.

#### Structure of Cmdlets

Cmdlets follow a standardized naming convention:

```powershell
Verb-Noun [-Parameter] <Argument>
```

* **Verb:** Specifies the action (e.g., `Get`, `Set`, `Remove`, `New`).
* **Noun:** Specifies the resource or object the action is performed on (e.g., `Process`, `Service`).
* **Parameter:** Optional arguments to customize behavior.

**Example:**

```powershell
Get-Process -Name "notepad"
```

**Categories of Cmdlets**

Cmdlets can be classified into various categories based on the tasks they perform:

1. **Information Cmdlets** (e.g., `Get-Help`, `Get-Command`)
2. **File System Cmdlets** (e.g., `Get-Item`, `Set-Item`, `Remove-Item`)
3. **Process Cmdlets** (e.g., `Get-Process`, `Start-Process`, `Stop-Process`)
4. **Service Cmdlets** (e.g., `Get-Service`, `Start-Service`, `Stop-Service`)
5. **Event Cmdlets** (e.g., `Get-EventLog`, `New-EventLog`)
6. **Network Cmdlets** (e.g., `Test-Connection`, `Get-NetIPAddress`)
7. **Security Cmdlets** (e.g., `Get-User`, `Set-User`)
8. **System Cmdlets** (e.g., `Get-ComputerInfo`, `Set-ExecutionPolicy`)

***

### Common PowerShell Cmdlets

#### Basic Cmdlets for Getting Started

1.  **Retrieve System Information:**

    ```powershell
    Get-Process       # Lists running processes
    Get-Service       # Lists services on the system
    Get-EventLog      # Retrieves event log entries
    ```
2.  **Working with Files and Directories:**

    ```powershell
    Get-ChildItem     # Lists files and directories (alias: ls)
    Copy-Item         # Copies a file or folder
    Remove-Item       # Deletes a file or folder
    ```
3.  **Managing Users and Groups:**

    ```powershell
    Get-LocalUser     # Lists local users on the system
    Get-LocalGroup    # Lists local groups
    Add-LocalUser     # Creates a new local user
    ```
4.  **Basic System Administration:**

    ```powershell
    Restart-Computer  # Restarts the system
    Stop-Process      # Stops a running process
    Start-Service     # Starts a stopped service
    Stop-Service      # Stops a running service
    ```

***

### Discovering Cmdlets

PowerShell provides several built-in cmdlets for discovering and learning about other cmdlets.

#### Get-Command

Find all available cmdlets, functions, aliases, and scripts:

```powershell
Get-Command
```

Filter by verb or noun:

```powershell
Get-Command -Verb Get       # Lists all cmdlets that use the verb "Get"
Get-Command -Noun Service   # Lists cmdlets related to services
```

#### Get-Help

Retrieve detailed help documentation for any cmdlet:

```powershell
Get-Help Get-Process
```

Update help files:

```powershell
Update-Help
```

#### Get-Member

Inspect the properties and methods of objects returned by a cmdlet:

```powershell
Get-Process | Get-Member
```

***

### Filtering and Sorting Output

#### Filtering with Where-Object

Use `Where-Object` to filter data based on conditions:

```powershell
Get-Process | Where-Object {$_.CPU -gt 100}
```

#### Sorting with Sort-Object

Use `Sort-Object` to sort data:

```powershell
Get-Service | Sort-Object -Property Status
```

***

### Cmdlets for Automation

#### Exporting Data

Save cmdlet output to files:

```powershell
Get-Process | Export-Csv -Path "processes.csv" -NoTypeInformation
```

#### Importing Data

Read data from CSV files:

```powershell
Import-Csv -Path "processes.csv"
```

#### Scheduled Tasks

Create scheduled tasks using cmdlets:

```powershell
New-ScheduledTask -Action (New-ScheduledTaskAction -Execute "notepad.exe") -Trigger (New-ScheduledTaskTrigger -At 8am -Daily)
```

***

### Advanced Cmdlets

#### Remoting

Execute commands on remote computers:

```powershell
Invoke-Command -ComputerName RemotePC -ScriptBlock { Get-Process }
```

#### Managing Modules

Install and manage PowerShell modules:

```powershell
Find-Module -Name "Az"
Install-Module -Name "Az"
Get-Module -ListAvailable
```

#### REST API Integration

Interact with REST APIs using `Invoke-RestMethod`:

```powershell
$response = Invoke-RestMethod -Uri "https://api.github.com/users/octocat"
$response.name
```

***

### Custom Cmdlets

You can create your own cmdlets using PowerShell functions.

#### Example: Custom Cmdlet

```powershell
Function Get-Square {
    Param(
        [int]$Number
    )
    $Number * $Number
}

Get-Square -Number 5
```

***

### Cmdlet Best Practices

1. Use meaningful and standardized verbs (e.g., Get, Set, Remove, Test).
2.  Always include help documentation in custom cmdlets:

    ```powershell
    <#
    .SYNOPSIS
    Brief description of the cmdlet.
    .DESCRIPTION
    Detailed description of what the cmdlet does.
    .PARAMETER <ParameterName>
    Description of the parameter.
    .EXAMPLE
    Example usage of the cmdlet.
    #>
    ```
3.  Validate input using parameters:

    ```powershell
    Param(
        [ValidateRange(1, 100)]
        [int]$Age
    )
    ```

***

