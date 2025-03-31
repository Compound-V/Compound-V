# Bandit Level 0

## **Problem: Bandit Level 0**

### **Goal:**

Log into the game using SSH.

### **Given Information:**

* **Host:** `bandit.labs.overthewire.org`
* **Port:** `2220`
* **Username:** `bandit0`
* **Password:** `bandit0`

### **Commands You May Need:**

* `ssh`

## **Solution:**

To log in, use the following SSH command:

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

When prompted for a password, enter:

```
bandit0
```

Once logged in, go to the **Level 1** page to proceed.

**Helpful Reading Material:**

* [Secure Shell (SSH) on Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)
* [How to use SSH on wikiHow](https://www.wikihow.com/Use-SSH)
