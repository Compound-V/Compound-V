# git\_hub\_ssh\_setup\_q\_a\_guide.md

````md
# GitHub SSH Setup – Question & Answer Guide

---

## Q1: What is the correct mental model for GitHub SSH?

**Answer:**
SSH uses a key pair:
- A **private key** that stays on your machine
- A **public key** that you upload to GitHub

GitHub never stores your private key. Authentication works only when the private key on your machine matches a public key stored on GitHub.

If the private key is lost, that SSH identity cannot be used again.

---

## Q2: What should I check before setting up GitHub SSH?

**Answer:**
First, confirm Git is installed:

```bash
git --version
```

Then check whether an SSH key already exists:

```bash
ls ~/.ssh
```

You are specifically looking for:
- `id_ed25519`
- `id_ed25519.pub`

If both exist, you may already have a usable SSH key.
If either is missing, you need to generate a new one.

---

## Q3: I do not see `id_ed25519` or `id_ed25519.pub`. What should I do?

**Answer:**
You need to generate a new SSH key.

Run:

```bash
ssh-keygen -t ed25519 -C "github@your-username"
```

When prompted:
- Press Enter to accept the default file location
- Press Enter twice to skip setting a passphrase

This creates:
- `~/.ssh/id_ed25519` (private key)
- `~/.ssh/id_ed25519.pub` (public key)

---

## Q4: I generated a key. Is that enough?

**Answer:**
No. You must load the key into the SSH agent so it can be used.

Run:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

You should see a message confirming the key was added.

---

## Q5: How do I add my SSH key to GitHub?

**Answer:**
First, copy your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the entire output (one line).

Then on GitHub:
1. Go to Settings → SSH and GPG keys
2. Click New SSH key
3. Enter a title (for example, `laptop-2025`)
4. Set Key type to **Authentication Key**
5. Paste the public key
6. Save

The key must start with `ssh-ed25519`.

---

## Q6: How do I verify that SSH is working with GitHub?

**Answer:**
Run:

```bash
ssh -T git@github.com
```

If successful, GitHub will greet you by username and confirm authentication.

If you see `Permission denied (publickey)`, then:
- The key is not added to GitHub, or
- The key is not loaded into the SSH agent, or
- The wrong key is being used

---

## Q7: How should I clone repositories once SSH is set up?

**Answer:**
Always use the SSH URL:

```bash
git clone git@github.com:USERNAME/REPO.git
```

If Git asks for a password, you are using the wrong URL.

---

## Q8: I already have an SSH key on GitHub. Can I reuse it?

**Answer:**
Only if you still have the matching private key file on this machine.

GitHub cannot give you your private key back.
If the private key is missing, that GitHub SSH key cannot be used again.

In that case:
- Generate a new SSH key
- Add it to GitHub
- Delete the old unused key from GitHub

---

## Q9: What is the SHA256 fingerprint shown on GitHub?

**Answer:**
It is only an identifier for a public key.

It is not a password, not a login method, and cannot be used to authenticate.

---

## Q10: What is `known_hosts` and why doesn’t it authenticate me?

**Answer:**
`known_hosts` stores fingerprints of servers you have connected to before.

It confirms the server’s identity, not yours.
Authentication requires your private key.

---

## Q11: What should I do if I change machines or reinstall my OS?

**Answer:**
SSH keys do not survive reinstallations unless backed up.

You must:
- Generate a new SSH key
- Add it to GitHub
- Remove the old key if it is no longer usable

---

## Q12: What is the minimum Git workflow I should remember?

**Answer:**
These commands cover most daily work:

```bash
git clone git@github.com:user/repo.git
git status
git add .
git commit -m "message"
git push
```

---

## Q13: How can I avoid losing SSH access again?

**Answer:**
Back up your private key securely after creating it:

```bash
cp ~/.ssh/id_ed25519 ~/.ssh/id_ed25519.backup
```

Store it in a secure, encrypted location.

---

## Final Rule to Remember

GitHub SSH works only when:
- The private key exists on your machine
- The matching public key is added to GitHub
- You use the SSH repository URL

If any one of these is missing, authentication will fail.
````

<br>
