# How to setup Kali Linux with WSL2

## WSL 2 + Kali Linux Setup Guide for Windows (2025 Edition)

✅ Perfect for: Windows 10 (2004+), Windows 11, or Windows Server 2022+\
💡 Who’s this for? Beginners and power users alike—this is your ultimate blueprint for setting up WSL 2 and Kali Linux with essential tools.

### Roadmap

1. **Prepare Your System** - Check for WSL and enable it if needed.
2. **Set WSL 2 as Default** - Ensure optimal performance.
3. **Install Kali Linux** - Add Kali without unwanted distros.
4. **Initialize Kali** - Set up your Linux account.
5. **Update Kali** - Keep it secure and current.
6. **Enable Systemd** - Enhance compatibility.
7. **Install Tools** - Add utilities and pentesting tools.
8. **Optimize & Troubleshoot** - Customize and fix issues.

***

### Step 1: Prepare Your System

**What You’ll Do:**

* Check if WSL is already installed.
* Enable WSL and install Kali Linux if needed, avoiding unwanted distros like Ubuntu.

**Instructions:**

1. **Check for Existing WSL Installation:**
   * Open PowerShell as Administrator (right-click Start → PowerShell (Admin)).
   *   Run:

       ```powershell
       wsl --list --verbose
       ```
   * **Output Interpretation:**
     * If you see a list of distributions (e.g., Ubuntu, Kali), WSL is installed. Note their versions (1 or 2).
     * If no distributions are listed or you get an error (e.g., “not recognized”), WSL is not enabled.
2. **Install WSL 2 and Kali Linux:**
   *   **If WSL is not installed:**\
       Run:

       ```powershell
       wsl --install -d kali-linux
       ```

       This command:

       * Enables WSL.
       * Activates Virtual Machine Platform.
       * Sets WSL 2 as the default version.
       * Installs _only_ Kali Linux (no Ubuntu).
   *   **If WSL is already installed:**\
       Install Kali directly:

       ```powershell
       wsl --install -d kali-linux
       ```

       This adds Kali without affecting existing distros.
3. **Verify Installation:**
   *   Run:

       ```powershell
       wsl --list --verbose
       ```
   * Confirm Kali Linux is listed with `VERSION = 2`.
   * If it’s version 1, upgrade it later in Step 2.
4. **(Optional) Remove Unwanted Distros:**
   *   If `wsl --install` (without `-d kali-linux`) was run earlier and installed Ubuntu, remove it:

       ```powershell
       wsl --unregister Ubuntu
       ```
   * Replace `Ubuntu` with the name of any distro you don’t want.
5. **(Optional) Set Kali as Default Distro:**
   *   To launch Kali by default when running `wsl`:

       ```powershell
       wsl --set-default kali-linux
       ```

**Common Problems:**

* **“I accidentally installed Ubuntu and want only Kali.”**
  * **Fix:** Run `wsl --unregister Ubuntu` to remove it, then verify with `wsl --list --verbose`.
* **“wsl --install doesn’t work.”**
  * **Cause:** Outdated Windows version.
  * **Fix:** Check your version with `winver`. Update to Windows 10 (2004+) or Windows 11 via Settings → Update & Security.

**Alternative Manual Installation:**\
If you prefer full control or don’t want `wsl --install`:

1.  Enable WSL and Virtual Machine Platform:

    ```powershell
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```
2. Reboot your PC.
3.  Set WSL 2 as default:

    ```powershell
    wsl --set-default-version 2
    ```
4.  Install Kali:

    ```powershell
    wsl --install -d kali-linux
    ```

***

### Step 2: Set WSL 2 as Default

**What You’ll Do:**\
Ensure all distros (new or existing) use WSL 2 for better performance.

**Instructions:**

*   In PowerShell (Admin):

    ```powershell
    wsl --set-default-version 2
    ```
*   If Kali is installed but shows version 1:

    ```powershell
    wsl --set-version kali-linux 2
    ```
*   Verify:

    ```powershell
    wsl --list --verbose
    ```

    Look for `VERSION = 2` next to Kali.

**Common Problem:**

* **“Command fails or defaults to WSL 1.”**
  * **Cause:** WSL kernel outdated.
  * **Fix:** Update with `wsl --update` and retry.

***

### Step 3: Install Kali Linux

#### What You’ll Do:

Get Kali Linux onto your system via your preferred method.

#### Option 1: Microsoft Store

* Open the **Microsoft Store**.
* Search for **“Kali Linux”**.
* Click **Get** → **Install**.
* [Direct Link](https://www.microsoft.com/store/apps/9PKR34TNCV07).

#### Option 2: Command Line (CLI)

*   In PowerShell (Admin):

    ```powershell
    wsl --install -d kali-linux  
    ```

#### Already Have WSL but Not Kali?

*   List available distros:

    ```powershell
    wsl --list --online  
    ```
*   Install Kali:

    ```powershell
    wsl --install -d kali-linux  
    ```

#### Common Problem:

* **“Installation fails (Store or CLI)”**
  * **Cause:** Network issues or Store glitches.
  * **Fix:** Ensure a stable internet connection. For Store issues, reset it via Settings → Apps → Microsoft Store → Reset.

***

### Step 4: Initialize Kali

#### What You’ll Do:

Launch Kali for the first time and set up your account.

#### Instructions:

*   In PowerShell or CMD:

    ```cmd
    kali  
    ```
* **First Launch:**
  * Kali extracts its filesystem (takes a minute).
  * You’ll be prompted to create a **username** and **password**. This is your Linux account—don’t lose it!

#### Common Problem:

* **“No prompt for username/password”**
  * **Cause:** Incomplete installation.
  * **Fix:** Uninstall with `wsl --unregister kali-linux`, then reinstall with `wsl --install -d kali-linux`.

***

### Step 5: Update Kali

#### What You’ll Do:

Ensure Kali is secure and up-to-date.

#### Instructions:

*   Inside Kali’s terminal:

    ```bash
    sudo apt update && sudo apt full-upgrade -y  
    sudo apt autoremove --purge -y  
    ```
*   Optional: Check your system info:

    ```bash
    neofetch  
    ```

#### Common Problem:

* **“Update fails”**
  * **Cause:** No internet or bad repositories.
  * **Fix:** Test connectivity with `ping google.com`. If it fails, run `sudo dhclient eth0` to reset networking.

***

### Step 6: Enable Systemd

#### What You’ll Do:

Add Systemd support for better tool compatibility.

#### Instructions:

*   Edit the WSL config file:

    ```bash
    sudo nano /etc/wsl.conf  
    ```
*   Add this:

    ```ini
    [boot]  
    systemd=true  
    ```
* Save (Ctrl+O, Enter, Ctrl+X).
*   Shut down WSL:

    ```powershell
    wsl --shutdown  
    ```
*   Relaunch Kali:

    ```cmd
    kali  
    ```
*   Verify Systemd:

    ```bash
    ps -p 1 -o comm=  
    ```

    * Should return: `systemd`.

#### Common Problem:

* **“Systemd doesn’t start”**
  * **Cause:** Config error or improper shutdown.
  * **Fix:** Double-check `/etc/wsl.conf` syntax and rerun `wsl --shutdown`.

***

### Step 7: Install Tools

#### What You’ll Do:

Add essential utilities and pentesting tools.

#### Instructions:

*   Basic tools:

    ```bash
    sudo apt install -y git curl wget unzip net-tools htop neofetch zsh  
    ```
*   Pentesting tools:

    ```bash
    sudo apt install -y nmap sqlmap metasploit-framework gobuster john hydra  
    ```

#### Common Problem:

* **“Tool installation fails”**
  * **Cause:** Permission issues or package conflicts.
  * **Fix:** Always use `sudo`. If errors persist, run `sudo apt update` and retry.

***

### Step 8: Optimize & Troubleshoot

#### What You’ll Do:

Polish your setup and fix lingering issues.

#### Instructions:

*   **Set Kali as Default:**

    ```powershell
    wsl --set-default kali-linux  
    ```
* **GUI Apps (Windows 11 WSLg):**\
  Test with `gedit`, `nautilus`, or `wireshark`.
*   **Check Version:**

    ```powershell
    wsl --list --verbose  
    ```
*   **Switch to WSL 2:**

    ```powershell
    wsl --set-version kali-linux 2  
    ```
*   **Reset if Needed:**

    <pre class="language-powershell"><code class="lang-powershell"><strong>wsl --unregister kali-linux  # Remove Kali  
    </strong>wsl --shutdown              # Reset WSL  
    </code></pre>

#### Common Problem:

* **“GUI apps don’t launch”**
  * **Cause:** Missing X server (Windows 10) or WSLg issue (Windows 11).
  * **Fix:** Install VcXsrv/X410 (Windows 10) or ensure WSLg is enabled (Windows 11).

***

### Common Problems & Solutions

1. **WSL Won’t Start:**
   * **Fix:** Ensure WSL and Virtual Machine Platform are enabled (Step 1).
2. **No Internet in Kali:**
   * **Fix:** Run `sudo dhclient eth0` in Kali.
3. **Permission Errors:**
   * **Fix:** Use `sudo` and verify your user isn’t root (recreate if needed).
4. **Slow Performance:**
   * **Fix:** Confirm WSL 2 is active with `wsl --list --verbose`.

***

### Next Steps

✅ You’ve got a fully functional WSL 2-powered Kali Linux setup!

#### Want More?

* Install **Oh-My-Zsh** for a slick terminal.
* Use **Dotfiles** to sync configs.
* Automate with a `kali-bootstrap.sh` script.
* Run tools like **Metasploit**, **Burp Suite**, or **BeEF**.
* Explore port forwarding for network services.

📬 Need the `wsl-kali-tools.sh` script or a hacker-themed terminal? Let me know!

***
