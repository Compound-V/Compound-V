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
<pre>

flowchart TD
    A["main.py (CLI Entry Point)"] --> B1["Validate Domain"]
    A --> B2["Parse Flags"]
    A --> B3["Load Wordlist"]
    B1 --> C["input_handler.py"]
    B2 --> C
    B3 --> C

    C --> D["enumerator.py"]
    D --> D1["Active Recon (if --active)"]
    D --> D2["Passive Recon (if --passive)"]
    D --> D3["Threading Engine"]

    D1 --> E["Subdomains from Brute-force"]
    D2 --> F["Subdomains from OSINT/API"]

    E --> G["resolver.py"]
    F --> G

    G --> H["Wildcard Detection + DNS Records"]

    H --> I["probe.py (if --probe)"]
    I --> J["Liveness Check via HTTP/ICMP"]

    H --> K["enricher.py (if --enrich)"]
    K --> L["WHOIS / ASN / Reverse DNS"]

    H --> M["exporter.py"]
    J --> M
    L --> M

    M --> N["Results: JSON / CSV / Markdown"]

</pre>
```



***

