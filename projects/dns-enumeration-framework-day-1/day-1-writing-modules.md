---
description: This is just me writing some modules because I was sitting Idle
---

# (Day-1) - Writing Modules

### 📦 Module: `input_handler.py`

This module’s job is to:

* Load a wordlist of subdomains to brute-force later
* Validate that the domain input is correctly formatted
* Return both to be used by the core scanner

Let’s walk through each function:



```mermaid
flowchart TD
    A["main.py (CLI)"] --> B1["Validate Domain"]
    A --> B2["Parse Flags"]
    A --> B3["Load Wordlist"]
    B1 --> C["input_handler"]
    B2 --> C
    B3 --> C

    C --> D["enumerator.py"]
    D --> D1["Active Recon"]
    D --> D2["Passive Recon"]
    D --> D3["Threading Engine"]

    D --> E["resolver.py"]
    E --> F["Wildcard Filtering & DNS Record Resolution"]

    F --> G["probe.py (Optional)"]
    G --> H["Live Check (HTTP/ICMP)"]

    F --> I["enricher.py (Optional)"]
    I --> J["WHOIS / ASN / Reverse DNS"]

    H --> K["exporter.py"]
    J --> K
    F --> K

    K --> L["Output as JSON / CSV / Markdown"]
```

***

