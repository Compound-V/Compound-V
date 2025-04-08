# Bandit Level 13 -> Level 14

## Objective

The password for Bandit Level 14 is stored in the file `/etc/bandit_pass/bandit14`. In addition, a private SSH key named `sshkey.private` is provided in the Bandit13 home directory. This key is specially configured so that only user `bandit14` can use it to log in to their account. This walkthrough explains each step in detail to help first-timers understand the process and reasoning.

***

### Step 1: Log into Bandit Level 13



1. **Open a Terminal:**\
   Launch your terminal application to start the session.
2.  **Connect to Bandit Level 13:**\
    Use SSH (Secure Shell) to log into Bandit Level 13 by running the following command:

    ```bash
    ssh bandit13@bandit.labs.overthewire.org -p 2220
    ```



    * **Explanation:** This command establishes a secure connection to the OverTheWire server at `bandit.labs.overthewire.org` using port `2220`. You will be prompted to enter the password you obtained from the previous level (Level 12 → Level 13).

***

### Step 2: Explore the Directory



1.  **List Files in Your Home Directory:**\
    Once logged in as Bandit13, check the available files by running:

    ```bash
    ls
    ```



    * **Explanation:** This command displays all files in your current directory. You should see a file named `sshkey.private` among the list. This file contains the private SSH key required to log into Bandit14.


2.  **Check File Permissions:**\
    To better understand file ownership and permissions, execute:

    ```bash
    ls -alh
    ```

    * **Explanation:** The output provides a detailed list of files including permissions, ownership, and file size. Notice that `sshkey.private` is owned by user `bandit14` with restricted read access (`-rw-r-----`), indicating that it’s intended for use only by Bandit14.

***

### Step 3: Locate the Password File



1.  **Navigate to the Password Directory:**\
    The passwords for all levels are stored in the `/etc/bandit_pass/` directory. Change to that directory with:

    ```bash
    cd /etc/bandit_pass
    ```



    * **Explanation:** This command moves you to the directory where each level’s password file is located. This directory is set up by the game to centrally store the passwords.


2.  **List Files in the Password Directory:**\
    Once inside, list the files:

    ```bash
    ls
    ```



    * **Explanation:** You will see a series of files named `bandit0` through `bandit33`. These files each contain the password for their respective levels. Look for the file named `bandit14`, which holds the password for the next level.

***

### Step 4: Read the Password File



1.  **Display the Contents of the Password File:**\
    Use the following command to extract the password:

    ```bash
    cat bandit14
    ```



    * **Explanation:** The `cat` command prints the contents of the file to the terminal. In this case, the file `bandit14` contains the password that you need to log into Bandit Level 14. The output will be a string of characters (for example, `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`) which is the password for Bandit14.

***

### Step 5: Log into Bandit Level 14



1. **Use the Provided SSH Key to Connect:**\
   With the password obtained and the SSH key in hand, use the key to log in to Bandit Level 14 by running:



```bash
ssh -i sshkey.private bandit14@localhost -p 2220
```



*   **Explanation:**

    * The `-i sshkey.private` option tells SSH to use the provided private key for authentication.
    * `bandit14@localhost` specifies that you are logging in as user `bandit14` on the local machine (as `localhost` refers to the current host).
    * `-p 2220` indicates that the connection should be made on port `2220`, which is the standard port used for the game.


* **Note:** You might see a message about the authenticity of the host. Confirm by typing `yes` when prompted. Also, a warning about creating the known\_hosts directory may appear due to permission restrictions, which can be safely ignored in this context.

***

## Conclusion



*   **Key Takeaways:**

    * **Exploring Directories:** Understanding how to navigate and list files on a remote system is essential for identifying key files such as `sshkey.private` and password files.
    * **File Permissions:** Reviewing file permissions with `ls -alh` helps determine which files are accessible and intended for specific users.
    * **Using SSH Keys:** The provided SSH key is used as a secure method to transition to the next level, ensuring that only the intended user (`bandit14`) can log in.


* **Critical Commands Recap:**
  *   Listing files in your home directory:

      ```bash
      ls
      ```
  *   Viewing file permissions:

      ```bash
      ls -alh
      ```
  *   Navigating to the password directory:

      ```bash
      cd /etc/bandit_pass
      ```
  *   Extracting the password:

      ```bash
      cat bandit14
      ```
  *   Logging into Bandit Level 14 with the SSH key:

      ```bash
      ssh -i sshkey.private bandit14@localhost -p 2220
      ```

***
