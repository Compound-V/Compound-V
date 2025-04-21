# Bandit Level 13 -> Level 14

## Objective

The password for the next level is not stored in a standard file that can be read. Instead, it is accessible by logging into the next level using an SSH private key provided in the current level. The file containing the private key is named `sshkey.private`.

***

### Step 1: Log into Bandit Level 13

In your terminal, use the following SSH command to log into the Bandit Level 13 account:

```bash
ssh bandit13@bandit.labs.overthewire.org -p 2220
```

When prompted, enter the password you obtained from Level 12.

***

### Step 2: Explore the Home Directory

Once logged in, list the contents of the home directory:

```bash
ls
```

You should see the file `sshkey.private`.

For more detailed information about the file, use:

```bash
ls -alh
```

You will notice that the file is readable and owned by the `bandit14` user.

***

### Step 3: Understand the Use of the SSH Key

The private key in `sshkey.private` allows passwordless authentication via SSH into the `bandit14` account. This means that instead of using a password, you will use this key to access the next level.

***

### Step 4: Attempting to Change File Permissions (Optional)

SSH often requires that private key files be accessible only by the owner. Normally, you would run:

```bash
chmod 600 sshkey.private
```

However, due to permission restrictions in this environment, you will not be able to change the file's mode. This does not prevent you from using the key as-is.

***

### Step 5: Log in as Bandit14 Using the Private Key

While still in the Bandit13 session, run the following command to use the private key and log into the Bandit14 account:

```bash
ssh -i sshkey.private bandit14@localhost -p 2220
```

* The `-i` flag specifies the identity file (i.e., the private key).
* `localhost` refers to the same machine, as both accounts exist on the same server.
* `-p 2220` sets the appropriate port for the OverTheWire Bandit server.

If prompted about host authenticity, type `yes` to proceed.

***

### Step 6: Confirm Successful Login

After logging in, verify that you are now the `bandit14` user:

```bash
whoami
```

The command should return:

```
bandit14
```

***

### Step 7: Retrieve the Password for the Next Level

Read the contents of the password file for the next level:

```bash
cat /etc/bandit_pass/bandit14
```

You will receive a password string similar to the following:

```
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```

Record this password for future use in the next level.

***

### Summary

In this level, you have:

* Located and identified a private SSH key
* Used the key to securely log in as the `bandit14` user via localhost
* Retrieved the password for the next level

***

### Next Step

Log into Bandit Level 14 using the password you just acquired:

```bash
ssh bandit14@bandit.labs.overthewire.org -p 2220
```

Let me know if you would like a walkthrough for Level 14 → Level 15.
