# Bandit Level 14 → Level 15

## Objective

Retrieve the password for the next level by **submitting the current password** to a service running on **localhost** (your own machine) at **port 30000**.

This exercise introduces a simple example of how networking services can receive and respond to data via TCP ports.

***

### Step 1: Log Into Bandit Level 14

Use SSH (Secure Shell) to access the Bandit server as the `bandit14` user. Run this command in your terminal:

```bash
ssh bandit14@bandit.labs.overthewire.org -p 2220
```

**Explanation of the command:**

* `ssh`: The command used to start a secure shell session.
* `bandit14@bandit.labs.overthewire.org`: Connects to the remote server as user `bandit14`.
* `-p 2220`: Specifies the port number (2220) that the Bandit SSH server uses.

When prompted, enter the password you retrieved in Level 13.

***

### Step 2: Understand the Challenge

The instructions specify that the password for the next level can be retrieved by sending the **current password** to **port 30000** on **localhost**.

* `localhost`: This refers to the current machine you are logged into, in this case the Bandit server.
* `port 30000`: A network port where a program is running and waiting to receive input.

You are expected to interact with this service and provide it with the current password.

***

### Step 3: Use Netcat to Communicate with Port 30000

The tool we'll use to communicate with the service is `nc` (short for **Netcat**), a command-line utility used for reading from and writing to network connections.

Run the following command:

```bash
nc localhost 30000
```

### **Explanation of the command:**

* `nc`: Invokes Netcat.
* `localhost`: Tells Netcat to connect to the local machine.
* `30000`: The specific port number the service is listening on.

Once the connection is established (you will see a blinking cursor), paste the current password:

```
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```

Then press **Enter**.

The service will respond with a message. It should be something like:

```
Correct! The password is: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```

This is the password for **Bandit Level 15**.

***

### Step 4: Save the New Password

Copy the output carefully and save the password. You will need it to log into the next level.

***

### Summary of Commands Used

| Command                                            | Purpose                                                                               |
| -------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `ssh bandit14@bandit.labs.overthewire.org -p 2220` | Logs into the Bandit server as user `bandit14` using SSH on port 2220                 |
| `nc localhost 30000`                               | Opens a connection to the local server on port 30000 using Netcat                     |
| `cat /etc/bandit_pass/bandit14` (optional)         | Displays the password for `bandit14`, useful if you forgot it from the previous level |

***

### Next Step

To proceed to **Bandit Level 15**, run the following command:

```bash
ssh bandit15@bandit.labs.overthewire.org -p 2220
```

When prompted, use the password you just retrieved.

***
