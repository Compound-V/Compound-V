---
description: This is just me writing some modules because I was sitting Idle
---

# (Day-1) - Writing Modules

## 🏗️ Module Build Plan (Pre-`main.py`)

We’ll build each module in isolation so they’re individually testable, then weave them together in `main.py` later.

| 🔧 Module                | Purpose                                  | Testing File         |
| ------------------------ | ---------------------------------------- | -------------------- |
| `input_handler.py`       | Validate domain + load wordlist          | ✅ `test_input.py`    |
| `enumerator.py`          | Combine subdomains + threaded DNS checks | ✅ `test_enum.py`     |
| `resolver.py`            | Filter wildcard DNS + fetch records      | ✅ `test_resolver.py` |
| `probe.py` (optional)    | HTTP/ICMP live checks                    | ✅ `test_probe.py`    |
| `enricher.py` (optional) | WHOIS / ASN / GeoIP enrichments          | ✅ `test_enricher.py` |
| `exporter.py`            | Save to JSON, CSV, Markdown              | ✅ `test_export.py`   |

***

## 📦 Day 1 - Module: `input_handler.py`

This module prepares the input for your DNS enumeration tool:

* **Validates the domain name** (e.g. `example.com`)
* **Loads and cleans the wordlist file** (e.g. `["www", "dev", "admin"]`)
* Returns both in a format your scanner can work with.

**Without this, you might be feeding junk into the scanner and getting false results or crashes. So `input_handler.py` makes sure our inputs are clean, verified, and ready to roll.**

### 📂 Code - input\_handler.py

```python
import re

# Part 1 - Validates the domain name (e.g. example.com)
def validate_domain(domain):
    # Use regex to ensure domain is well-formed (e.g. not http://)
    pattern = r"^(?:\*\.)?(?!-)[A-Za-z0-9-]{1,63}(?<!-)(?:\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*\.[A-Za-z]{2,63}\.?$"$"
    return re.match(pattern, domain)

# Part 2 - Loads and cleans the wordlist file (e.g. ["www", "dev", "admin"])
def load_wordlist(path):
    try:
        with open(path, 'r') as file:
            # Strip whitespace and skip blanks
            words = [line.strip() for line in file if line.strip()]
        if not words:
            print("[!] Wordlist file is empty.")
        return words
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {path}")
        return []
        

# Part 3 - Returns both in a format our scanner can work with.
def prepare_input(domain, wordlist_path):
    if not validate_domain(domain):
        print(f"[!] Invalid domain format: {domain}")
        return None, []

    words = load_wordlist(wordlist_path)
    if not words:
        print("[!] No words loaded from wordlist.")
        return domain, []

    return domain, words
```

***

### 🧠 Why These Choices?

| Function            | What It Does                       | Why It's Smart                              |
| ------------------- | ---------------------------------- | ------------------------------------------- |
| `validate_domain()` | Filters out malformed domains      | Prevents crashing on `http://foo` or `.com` |
| `load_wordlist()`   | Reads a list of subdomain prefixes | Lightweight, skips empty lines              |
| `prepare_input()`   | Centralizes input cleaning         | Keeps logic tidy and expandable             |

***

### 🔹 Part 1 - `validate_domain(domain)`

```python
import re

# Part 1 - Validates the domain name (e.g. example.com)
def validate_domain(domain):
    # Use regex to ensure domain is well-formed (e.g. not http://)
    pattern = r"^(?:\*\.)?(?!-)[A-Za-z0-9-]{1,63}(?<!-)(?:\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*\.[A-Za-z]{2,63}\.?$"
    return re.match(pattern, domain)
```

#### 🧠 What’s Happening Here?

* Uses a regular expression to check if the domain is valid

Examples it accepts:

* `example.com`
* `secure.mail.example.co.uk`

Examples it rejects:

* `http://example.com` (has protocol)
* `-weird.com` (starts with a dash)
* `example.` (ends with dot but no TLD)

#### 🔍 Why This Regex?

* Doesn’t rely on external libraries (lightweight)
* Covers standard formats while avoiding malformed inputs
* **Regular Expressions** (regex) are pattern-matching rules used to validate or find structured data

```
r"^(?:\*\.)?(?!-)[A-Za-z0-9-]{1,63}(?<!-)(?:\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*\.[A-Za-z]{2,63}\.?$"
```

It matches:

* Any standard domain (`example.com`, `secure.google.co.uk`)
* Prevents malformed stuff (`http://badinput`, `-broken.com`)

Regex is like firewall rules for strings—it blocks junk and lets only clean stuff through.

#### 🔚 End Result:

You confirm the target domain is clean and usable before scanning begins.

***

### 🔹 Part 2 - `load_wordlist(path)`

```python
# Part 2 - Loads and cleans the wordlist file (e.g. ["www", "dev", "admin"])
def load_wordlist(path):
    try:
        with open(path, 'r') as file:
            # Strip whitespace and skip blanks
            words = [line.strip() for line in file if line.strip()]
        if not words:
            print("[!] Wordlist file is empty.")
        return words
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {path}")
        return []
```

#### 🧠 What’s Happening Here?

* Tries to open the file path
* Reads line by line, strips whitespace
* Skips empty lines
* Returns the cleaned wordlist
* Shows error if the file is missing

#### 🔍 Why This Approach?

* We use `.strip()` to remove spaces and newline characters
* We check if the list is empty to avoid silent failures
* We handle missing files with a clean error instead of crashing the tool

#### 🔚 End Result:

You get a Python list like:

```python
["www", "admin", "secure", "ftp"]
```

Which becomes:

```python
["www.example.com", "admin.example.com", ...]
```

***

### 🔹 Part 3: `prepare_input(domain, wordlist_path)`

```python
# Part 3 - Returns both in a format our scanner can work with.
def prepare_input(domain, wordlist_path):
    if not validate_domain(domain):
        print(f"[!] Invalid domain format: {domain}")
        return None, []

    words = load_wordlist(wordlist_path)
    if not words:
        print("[!] No words loaded from wordlist.")
        return domain, []

    return domain, words
```

#### 🧠 What’s Happening Here?

* Runs both validation and wordlist loading in a single function
* Prevents malformed domains and empty wordlists from continuing
* Returns `domain, wordlist` for scanning modules to use

#### 🔍 Why Combine These?

*   It keeps your `main.py` clean with just one call:

    ```python
    domain, subdomains = prepare_input(args.domain, args.wordlist)
    ```
* It acts like an **input gatekeeper**, only letting clean, verified data enter the framework

#### 🔚 End Result:

A ready-to-use input set that looks like:

```python
("example.com", ["www", "dev", "admin", "secure"])
```

***
