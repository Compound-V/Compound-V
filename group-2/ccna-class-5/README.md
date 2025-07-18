# CCNA Class 5

## **TCP/IP Model ->**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption><p>OSI vs TCP/IP</p></figcaption></figure>

## OSI vs TCP/IP Protocol comparison Chart

For a more detailed information on various types of Protocols visit here - [https://app.gitbook.com/o/S8ryH0vAvYEHMKmmraM2/s/M6VSMZcJH3jwhttYSu6b/\~/changes/29/group-2/ccna-class-5/chart-of-protocols](https://app.gitbook.com/o/S8ryH0vAvYEHMKmmraM2/s/M6VSMZcJH3jwhttYSu6b/~/changes/29/group-2/ccna-class-5/chart-of-protocols)

<table><thead><tr><th>OSI Layer</th><th>TCP/IP Layer</th><th width="425">Protocols</th></tr></thead><tbody><tr><td>Application (L7)</td><td>Application</td><td>HTTP, HTTPS, FTP, FTPS, TFTP, SFTP, SMTP, IMAP, POP3, SNMP, DNS, DHCP, Telnet, SSH, NTP, SIP, MQTT, XMPP, LDAP, WHOIS, Gopher, NNTP, BGP, IRC, SLP, RDP, H.323, Diameter, OpenVPN, TLS/SSL, WebSockets.</td></tr><tr><td>Presentation (L6)</td><td>(Merged in App Layer)</td><td>SSL, TLS, XDR, MIME, ASCII, EBCDIC, GIF, JPEG, MPEG, MP3, BMP, PNG, Unicode, XML, HTML, MIDI, TIFF, PDF, QuickTime</td></tr><tr><td>Session (L5)</td><td>(Merged in App Layer)</td><td>NetBIOS, RPC, PPTP, SOCKS, SDP, ASP, RTCP, RTP, iSCSI, TLS, H.245, SMB, PPTP, SSH, RTSP</td></tr><tr><td>Transport (L4)</td><td>Transport</td><td>TCP, UDP, SCTP, DCCP, RSVP, QUIC, RUDP (Reliable UDP), MPTCP (Multipath TCP)</td></tr><tr><td>Network (L3)</td><td>Internet</td><td>IP (IPv4, IPv6), ICMP, IGMP, IPsec, GRE, L2TP, ARP, RARP, BGP, OSPF, RIP, IS-IS, EIGRP, VRRP, LDP, NDP, MPLS, PIM (Protocol Independent Multicast)</td></tr><tr><td>Data Link (L2)</td><td>Network Access</td><td>Ethernet, IEEE 802.3, IEEE 802.11 (Wi-Fi), PPP, HDLC, Frame Relay, ATM, FDDI, L2TP, ARP, RARP, STP (Spanning Tree Protocol), LLDP, CDP, VTP, ISL, MPLS, AAL (ATM Adaptation Layer)</td></tr><tr><td>Physical (L1)</td><td>Network Access</td><td>IEEE 802.3 (Ethernet), IEEE 802.11 (Wi-Fi), Bluetooth, USB, DSL, SONET, GSM, LTE, NR (5G), ISDN, Token Ring, Coaxial, Fiber Optic, Infrared, Radio Waves</td></tr></tbody></table>

***

## **📌 OSI vs. TCP/IP: An Advanced Comparison**

### **1️⃣ Overview of Both Models**

| Feature          | OSI Model                                            | TCP/IP Model                                          |
| ---------------- | ---------------------------------------------------- | ----------------------------------------------------- |
| **Full Name**    | Open Systems Interconnection Model                   | Transmission Control Protocol/Internet Protocol Model |
| **Structure**    | 7 Layers                                             | 4 Layers                                              |
| **Developed By** | ISO (International Organization for Standardization) | DoD (Department of Defense, USA)                      |
| **Usage**        | Conceptual model for understanding networking        | Practical model used for real-world networking        |
| **Flexibility**  | More theoretical, rarely used as-is                  | Directly implemented in real networks                 |

***

### **2️⃣ Layer-by-Layer Breakdown**

**🔹 OSI Model Layers & Protocols**

| OSI Layer                  | Function                            | Examples of Protocols               | Security Considerations                 |
| -------------------------- | ----------------------------------- | ----------------------------------- | --------------------------------------- |
| **Application (Layer 7)**  | End-user interactions               | HTTP, HTTPS, FTP, SMTP, DNS         | Encryption (TLS/SSL), Authentication    |
| **Presentation (Layer 6)** | Data translation & encryption       | JPEG, GIF, ASCII, SSL/TLS           | Data compression, Encoding security     |
| **Session (Layer 5)**      | Establishing & maintaining sessions | NetBIOS, RPC, PPTP                  | Session hijacking protection            |
| **Transport (Layer 4)**    | Reliable data transmission          | TCP, UDP, SCTP                      | Firewall rules, DoS protection          |
| **Network (Layer 3)**      | Logical addressing & routing        | IP, ICMP, ARP, RIP, OSPF            | IP Spoofing protection, VPN security    |
| **Data Link (Layer 2)**    | Physical addressing & MAC layer     | Ethernet, Wi-Fi (802.11), PPP, VLAN | MAC filtering, ARP poisoning protection |
| **Physical (Layer 1)**     | Electrical & hardware transmission  | Fiber optics, Coaxial, Bluetooth    | Physical security, Network segmentation |

**🔹 TCP/IP Model Layers & Protocols**

| TCP/IP Layer                    | Equivalent OSI Layers | Function                                   | Examples of Protocols     | Security Considerations        |
| ------------------------------- | --------------------- | ------------------------------------------ | ------------------------- | ------------------------------ |
| **Application**                 | Layers 5, 6, 7        | User interaction & application services    | HTTP, SMTP, FTP, DNS, SSH | TLS/SSL, Authentication        |
| **Transport**                   | Layer 4               | End-to-end communication                   | TCP, UDP                  | Firewall rules, DoS protection |
| **Internet**                    | Layer 3               | Logical addressing & routing               | IP, ICMP, ARP             | IP Spoofing protection         |
| **Network Access (Link Layer)** | Layers 1 & 2          | Data transmission over the physical medium | Ethernet, Wi-Fi, PPP      | MAC filtering, VLAN security   |

***

### **3️⃣ Key Differences Between OSI & TCP/IP**

| Feature                 | OSI Model                                | TCP/IP Model                                             |
| ----------------------- | ---------------------------------------- | -------------------------------------------------------- |
| **Usage**               | Conceptual, mainly for teaching          | Practically implemented in networks                      |
| **Security Handling**   | Security concepts are separate per layer | Security is built into protocols like HTTPS, SSH         |
| **Complexity**          | More structured, 7 layers                | Simplified, only 4 layers                                |
| **Protocol Dependence** | Independent protocols at each layer      | TCP & IP are core components                             |
| **Data Flow Control**   | Uses session and presentation layers     | Managed directly in the transport and application layers |

***

### **4️⃣ Real-World Use Cases**

| Scenario                    | OSI Model Application                           | TCP/IP Model Application          |
| --------------------------- | ----------------------------------------------- | --------------------------------- |
| **Web Browsing**            | HTTPS at Layer 7, TCP at Layer 4, IP at Layer 3 | HTTP(S) over TCP/IP               |
| **File Transfer**           | FTP at Layer 7, TCP at Layer 4                  | FTP over TCP/IP                   |
| **Network Troubleshooting** | ICMP at Layer 3, ARP at Layer 2                 | Ping, Traceroute (ICMP)           |
| **VoIP Calls**              | RTP at Layer 7, UDP at Layer 4                  | SIP/RTP over UDP                  |
| **Wireless Communication**  | Wi-Fi at Layer 2, Physical signals at Layer 1   | Wi-Fi in the Network Access layer |

***

### **5️⃣ Security Considerations in Both Models**

| Threat                              | Affected Layer(s)      | Protection Measures                         |
| ----------------------------------- | ---------------------- | ------------------------------------------- |
| **Man-in-the-Middle Attack (MitM)** | Application, Transport | TLS/SSL encryption, VPNs                    |
| **DDoS Attacks**                    | Transport, Network     | Firewalls, Rate limiting                    |
| **Packet Sniffing**                 | Network, Data Link     | Encrypted traffic (HTTPS, VPNs)             |
| **IP Spoofing**                     | Network                | Secure IP filtering, Anti-spoofing rules    |
| **MAC Address Spoofing**            | Data Link              | MAC filtering, Dynamic ARP inspection       |
| **Physical Access Attacks**         | Physical               | Biometric authentication, Restricted access |

***

### **6️⃣ Conclusion**

* The **OSI Model** is great for **understanding networking**, but it's rarely implemented as-is.
* The **TCP/IP Model** is **practically used** in the real world, and **all internet communications** rely on it.
* **Security is better integrated into TCP/IP**, whereas OSI separates concerns at different layers.

***



## <mark style="color:green;">DNS - Domain Name Server</mark>



<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption><p>DNS</p></figcaption></figure>

## <mark style="color:green;">The DNS Resolution Process: A Clear Guide</mark>

When you type a website like `www.example.com` into your browser, the Domain Name System (DNS) translates that human-friendly name into an IP address (like `192.0.2.1`) that your device can use to connect to the server. Here’s how it works, step by step, with all the key details made simple and engaging.

#### **1. You Start the Process**

* **What Happens:** You enter `www.example.com` in your browser.
* **Why It Matters:** The internet runs on IP addresses, not domain names, so DNS is the translator that makes this possible.

***

#### **2. Checking Local Sources First**

Before asking the internet for help, your device looks for the answer locally in this order:

1. **Browser Cache**
   * Checks if the browser recently resolved this domain.
   * _Example:_ You visited `www.example.com` five minutes ago, and it’s still stored.
2. **Operating System Cache**
   * Looks at the device’s DNS storage (e.g., Windows or macOS cache).
   * _Think:_ A shared list for all apps on your computer.
3. **Router Cache**
   * Your Wi-Fi router might have the answer from a previous request on your network.
4. **Hosts File**
   * A local file (like a mini phonebook) with manual mappings (e.g., `127.0.0.1 localhost`).
   * _Fun Fact:_ Hackers sometimes edit this to redirect websites!

* **Outcome:**
  * **Found It?** If any of these have a valid, non-expired IP address, your browser uses it, and you’re done!
  * **Not Found?** Time to ask the DNS resolver.

***

#### **3. The DNS Resolver Steps In**

* **What’s a Resolver?**\
  A server that does the heavy lifting to find the IP. It could be:
  * Your ISP’s server
  * A public one like Google (`8.8.8.8`) or Cloudflare (`1.1.1.1`)
  * A custom one set by you or your company.
* **What It Does:**
  1. **Checks Its Cache:** Has it answered this recently? If yes, it sends the IP back fast.
  2. **No Luck?** It starts a journey to find the answer from scratch.

***

#### **4. The DNS Query Adventure**

If the resolver needs to dig deeper, it follows this chain:

1. **Root Servers**
   * **Who They Are:** 13 global server groups (labeled A to M).
   * **What They Do:** Say, “I don’t have the IP, but ask the `.com` server.”
   * _Cool Note:_ There are hundreds of physical copies worldwide for speed and reliability.
2. **TLD Servers**
   * **Who They Are:** Servers for top-level domains like `.com`, `.org`, or `.edu` (e.g., Verisign runs `.com`).
   * **What They Do:** Point to the domain’s specific nameserver, like “Ask example.com’s server.”
3. **Authoritative Nameserver**
   * **Who They Are:** The server that holds `example.com`’s official records.
   * **What They Do:** Finally give the IP (e.g., `192.0.2.1`) or other data like:
     * **A Record:** IPv4 address
     * **AAAA Record:** IPv6 address
     * **CNAME:** An alias (e.g., `www` points to `server1.example.com`), which restarts the process.

***

#### **5. Caching for Next Time**

* **What Happens:**
  * The resolver saves the IP with a “time to live” (TTL), like 24 hours.
  * Your browser, OS, and even router might cache it too.
* **Why It’s Great:** Next time you visit, it’s lightning-fast—no external queries needed!

***

#### **6. Back to You**

* **What Happens:** The resolver sends the IP to your device.
* **Result:** Your browser connects to `192.0.2.1`, and the website loads. Done!

***

#### **7. Bonus Features and Fun Twists**

DNS isn’t just a one-trick pony—here are some cool extras:

* **Reverse Lookup (PTR):** Turns an IP back into a name (e.g., `192.0.2.1` → `www.example.com`).
* **Split-Horizon DNS:** Gives different IPs based on where you’re asking from (e.g., office vs. home).
* **Dynamic DNS:** Updates IPs for devices that change addresses (e.g., your home server).
* **DNSSEC:** Adds security to stop fake answers.
* **Load Balancing:** Sends you to different servers to spread traffic (e.g., round-robin IPs).
* **NXDOMAIN:** If the site doesn’t exist, you get a “not found” message.
* **Encrypted DNS (DoH/DoT):** Keeps your queries private with HTTPS or TLS.

***



## DNS Mind Map ->

Below is an extensive, clear, and detailed mind map of the DNS resolution process covering all major flows and special cases—with a thorough, step‐by‐step explanation afterward.

```plaintext
[DNS Resolution Process]
         │
         ├─► [User Input]
         │       • Enter domain (e.g., www.example.com)
         │       • May include subdomains (e.g., blog.example.com)
         │
         ├─► [Local Lookup & Overrides]
         │       • **Typical Order of Checks:**
         │         - Browser Cache (e.g., Chrome’s DNS cache)
         │         - OS Cache (e.g., Windows DNS Client, /etc/resolv.conf)
         │         - Hosts File (e.g., /etc/hosts, overrides DNS queries)
         │         - Router Cache (if router acts as a DNS proxy)
         │       • **Notes:**
         │         - Order may vary by system configuration
         │         - Cached entries have TTL (Time to Live) expiration
         │       └─► If found → Return IP (End)
         │
         └─► [No Local Record Found]
                 │
                 ├─► [Send Query to DNS Resolver]
                 │         • Usually a Recursive Resolver (e.g., ISP, Google 8.8.8.8, Cloudflare 1.1.1.1)
                 │         • Alternatively, a local resolver performing iterative queries (e.g., stub resolver on client)
                 │         • **Enhancements:**
                 │           - May use Encrypted DNS:
                 │             * DNS over HTTPS (DoH): Queries via HTTPS (port 443)
                 │             * DNS over TLS (DoT): Queries via TLS (port 853)
                 │           - Supports DNS forwarders (e.g., in enterprise networks)
                 │
                 ├─► [Resolution Mode Decision]
                 │         ├─► Recursive Mode
                 │         │       • Resolver performs full lookup on behalf of client
                 │         │       • Common for public resolvers (e.g., ISP-provided)
                 │         │
                 │         └─► Iterative Mode (or Hybrid)
                 │                 • Client or local resolver follows referrals step-by-step
                 │                 • Used by stub resolvers or custom DNS setups
                 │
                 └─► [Query Chain]
                           │
                           ├─► Query Root Servers
                           │         • 13 logical root server groups (operated globally)
                           │         • Returns referral to TLD server (e.g., .com, .org)
                           │         • Uses anycast routing for load balancing
                           │
                           ├─► Query TLD Server (e.g., for .com)
                           │         • Manages top-level domains (e.g., .com, .net, .edu)
                           │         • Returns referral to Authoritative Nameserver
                           │         • Operated by registries (e.g., Verisign for .com)
                           │
                           ├─► Query Authoritative Nameserver
                           │         • Holds DNS records for the specific domain
                           │         • Returns DNS record(s):
                           │           - A record (IPv4 address, e.g., 192.0.2.1)
                           │           - AAAA record (IPv6 address, e.g., 2001:db8::1)
                           │           - CNAME record (alias, e.g., www → example.com)
                           │           - Other records:
                           │             * MX (Mail Exchange, for email servers)
                           │             * TXT (Text, e.g., SPF, DKIM for verification)
                           │             * NS (Nameserver, delegates to other NS)
                           │             * SOA (Start of Authority, zone info)
                           │         • **Security:**
                           │           - Responses may be validated with DNSSEC (digital signatures)
                           │
                           └─► [If CNAME Record]
                                     • Restart resolution for the canonical name
                                     • May involve multiple CNAME redirects (e.g., alias1 → alias2 → IP)
                                     • Loop prevention: Resolvers limit redirect chains (e.g., 10 hops)
                           │
                           └─► [Cache Results]
                                     • **Caching Levels:**
                                     │         - Resolver caches response with TTL (e.g., 3600s)
                                     │         - Client OS caches (e.g., for other apps)
                                     │         - Browser caches (e.g., for future page loads)
                                     │         - Intermediate servers (e.g., ISP recursive resolvers)
                                     • **Notes:**
                                     │         - TTL dictates freshness; expired entries trigger new queries
                                     │         - Negative caching (e.g., NXDOMAIN) also occurs
                           │
                           └─► [Return Final IP to Client]
                                     • Client receives IP address(es)
                                     • **Special Cases:**
                                     │         - Multiple IPs returned (e.g., for load balancing, round-robin)
                                     │         - IPv6 preferred if supported (dual-stack systems)
                                     │         - For CDNs: IP selected based on client’s geolocation
                           │
                           └─► [Establish Connection]
                                     • Browser connects via HTTP/HTTPS to the IP
                                     • **Notes:**
                                     │         - For email: Uses MX records instead
                                     │         - For other protocols: May use SRV records
                           │
                           └─► [Additional Considerations]
                                     • **Reverse DNS Lookup (PTR):**
                                     │         - Maps IP to domain (e.g., 192.0.2.1 → example.com)
                                     │         - Used for verification (e.g., anti-spam checks)
                                     • **Split-Horizon DNS:**
                                     │         - Different responses based on query source (e.g., internal LAN vs. public)
                                     • **Dynamic DNS (DDNS) Updates:**
                                     │         - Auto-updates records for devices with changing IPs (e.g., home routers)
                                     • **IPv4 (A) vs. IPv6 (AAAA) Records:**
                                     │         - Resolvers request both; client selects based on support/preference
                                     • **DNSSEC & Security:**
                                     │         - Validates responses to prevent cache poisoning, spoofing
                                     • **Common DNS Errors:**
                                     │         - NXDOMAIN: Domain doesn’t exist
                                     │         - SERVFAIL: Server failed to process query
                                     │         - Timeout: No response within time limit
                                     • **Encrypted DNS:**
                                     │         - DoH/DoT enhance privacy, prevent interception
                                     • **DNS in CDNs:**
                                     │         - Directs users to optimal servers (e.g., based on latency, load)
                                     • **DNS Load Balancing:**
                                     │         - Returns multiple IPs; client or resolver chooses
```

***

