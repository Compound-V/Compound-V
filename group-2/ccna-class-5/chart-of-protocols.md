---
description: List of Majority of Protocols
---

# Chart of Protocols

***

## <mark style="color:red;">**Comprehensive List of OSI Protocols**</mark>

_(A deep technical reference covering protocols across the OSI model: Application, Presentation, Session, Transport, Network, Data Link, and Physical Layers.)_

***

#### <mark style="color:yellow;">**Application Layer (Layer 7)**</mark>

Handles end-user applications and services such as web browsing, email, file transfers, and directory services.

**Web, Email & File Transfer Protocols**

| **Protocol** | **Full Form**                         | **Port(s)** | **Purpose**                                        | **Vulnerabilities**                                                | **Attack Methods**                                | **Implementation Example**               |
| ------------ | ------------------------------------- | ----------- | -------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------- | ---------------------------------------- |
| HTTP         | HyperText Transfer Protocol           | 80          | Standard web browsing                              | Plaintext transmission; session hijacking; injection attacks       | MITM via packet sniffing; SQL injection; XSS      | Apache/Nginx serving websites            |
| HTTPS        | HTTP Secure                           | 443         | Secure web browsing using TLS/SSL                  | SSL/TLS vulnerabilities (POODLE, Heartbleed); certificate spoofing | SSL stripping; certificate forgery                | Banking portals, secure e-commerce sites |
| FTP          | File Transfer Protocol                | 20, 21      | Transfers files between systems                    | Transmits credentials in plaintext; brute-force susceptible        | Packet sniffing; brute-force credential cracking  | Legacy file servers, web hosting systems |
| SFTP         | Secure File Transfer Protocol         | 22          | Encrypted file transfers over SSH                  | Weak key exchange if misconfigured                                 | Brute-force attacks; exploitation of weak ciphers | Secure backups, file transfers           |
| FTPS         | FTP Secure                            | 990         | FTP with SSL/TLS encryption                        | Misconfigured certificates; downgrade attacks                      | MITM; downgrade exploits                          | Encrypted file transfer in enterprises   |
| TFTP         | Trivial File Transfer Protocol        | 69          | Lightweight file transfers (often used in booting) | No authentication; no encryption                                   | Packet sniffing; spoofing                         | Network booting of diskless workstations |
| SMTP         | Simple Mail Transfer Protocol         | 25          | Sending emails between servers                     | Open relay abuse; email spoofing                                   | Spoofing; spam injection                          | Postfix, Microsoft Exchange              |
| IMAP         | Internet Message Access Protocol      | 143         | Retrieving emails while keeping them on the server | Credential theft; insecure sessions                                | MITM; brute-force password attacks                | Gmail, Outlook (IMAP access)             |
| POP3         | Post Office Protocol v3               | 110         | Downloading emails to a local client               | Plaintext credentials                                              | Sniffing; brute-force attacks                     | Older email clients                      |
| LDAP         | Lightweight Directory Access Protocol | 389         | Directory and authentication services              | LDAP injection; unauthorized data access                           | Injection attacks; spoofing                       | Microsoft Active Directory, OpenLDAP     |
| LDAPS        | Secure LDAP                           | 636         | Encrypted LDAP communication                       | Certificate vulnerabilities                                        | MITM; spoofing attacks                            | Secure enterprise directory services     |

***

#### <mark style="color:yellow;">**Presentation Layer (Layer 6)**</mark>

Manages data representation, encryption, compression, and translation between application and network formats.

**Data Formatting & Encryption Protocols**

| **Protocol** | **Full Form**                         | **Port(s)** | **Purpose**                                    | **Vulnerabilities**                                           | **Attack Methods**                  | **Implementation Example**           |
| ------------ | ------------------------------------- | ----------- | ---------------------------------------------- | ------------------------------------------------------------- | ----------------------------------- | ------------------------------------ |
| SSL          | Secure Sockets Layer                  | 443         | Encrypts data for secure communication         | Vulnerable to POODLE, Heartbleed; outdated cryptography       | Exploitation of known SSL flaws     | Legacy secure connections before TLS |
| TLS          | Transport Layer Security              | 443         | Secures communication with improved encryption | Misconfiguration; certificate issues                          | SSL stripping; certificate spoofing | HTTPS connections                    |
| MIME         | Multipurpose Internet Mail Extensions | -           | Encodes multimedia data for emails             | Complex implementations may lead to injection vulnerabilities | Content spoofing                    | Email attachments handling           |
| JPEG         | Joint Photographic Experts Group      | -           | Image compression                              | Lossy compression can degrade quality                         | Not typically exploited for attacks | Digital image storage                |
| PNG          | Portable Network Graphics             | -           | Lossless image compression                     | Generally secure; vulnerabilities are rare                    | N/A                                 | Web graphics, icons                  |
| MPEG         | Moving Picture Experts Group          | -           | Video and audio compression                    | Compression artifacts may lead to errors                      | N/A                                 | Streaming media formats              |

***

#### <mark style="color:yellow;">**Session Layer (Layer 5)**</mark>

Establishes, manages, and terminates sessions between applications.

**Session Management Protocols**

| **Protocol** | **Full Form**                     | **Port(s)** | **Purpose**                                       | **Vulnerabilities**                                            | **Attack Methods**                        | **Implementation Example**          |
| ------------ | --------------------------------- | ----------- | ------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------- | ----------------------------------- |
| RPC          | Remote Procedure Call             | 135         | Enables execution of code on remote systems       | Vulnerable to injection attacks; potential unauthorized access | Exploitation of poorly secured endpoints  | Distributed computing, Windows DCOM |
| PPTP         | Point-to-Point Tunneling Protocol | 1723        | Creates VPN tunnels for secure remote access      | Known vulnerabilities; outdated encryption methods             | MitM; brute-force attacks                 | Legacy VPN services                 |
| SMB          | Server Message Block              | 445         | Facilitates file and printer sharing              | Vulnerable to wormable attacks (e.g., WannaCry)                | Exploitation of EternalBlue vulnerability | Windows file sharing                |
| NetBIOS      | Network Basic Input/Output System | 137-139     | Legacy protocol for Windows network communication | Lacks encryption; susceptible to spoofing                      | Brute-force attacks; ARP spoofing         | Older Windows networking protocols  |

***

#### <mark style="color:yellow;">**Transport Layer (Layer 4)**</mark>

Provides reliable (or fast) data transfer services between hosts, ensuring proper segmentation and flow control.

**Transport Protocols**

| **Protocol** | **Full Form**                        | **Port(s)** | **Purpose**                                              | **Vulnerabilities**                            | **Attack Methods**                            | **Implementation Example**        |
| ------------ | ------------------------------------ | ----------- | -------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------- | --------------------------------- |
| TCP          | Transmission Control Protocol        | -           | Connection-oriented, reliable data transfer              | Susceptible to SYN flooding, session hijacking | SYN flood; TCP reset attacks                  | Web servers, file transfers       |
| UDP          | User Datagram Protocol               | -           | Connectionless, fast data transfer with less overhead    | No reliability; vulnerable to spoofing         | UDP flooding; amplification attacks           | Streaming, DNS queries            |
| SCTP         | Stream Control Transmission Protocol | -           | Supports multi-streaming and multi-homing                | Limited support; misconfiguration risks        | Exploiting multi-stream features              | Telephony, signaling protocols    |
| DCCP         | Datagram Congestion Control Protocol | -           | Adds congestion control to unreliable datagram transport | Experimental; limited adoption                 | Manipulation of congestion control parameters | Real-time applications, streaming |

***



<mark style="color:yellow;">**Network Layer (Layer 3)**</mark>

Responsible for logical addressing, routing, and delivering packets across networks.

**Internet & Routing Protocols**

| **Protocol** | **Full Form**                              | **Port(s)** | **Purpose**                                            | **Vulnerabilities**                                       | **Attack Methods**                           | **Implementation Example**            |
| ------------ | ------------------------------------------ | ----------- | ------------------------------------------------------ | --------------------------------------------------------- | -------------------------------------------- | ------------------------------------- |
| IP           | Internet Protocol                          | -           | Provides addressing and routing for packets            | IP spoofing; fragmentation attacks                        | Spoofing; fragmentation exploits             | Backbone of IPv4/IPv6 networks        |
| ICMP         | Internet Control Message Protocol          | -           | Provides error reporting and diagnostics               | Exploited in DoS attacks (ping flood)                     | Ping of death; ICMP flood attacks            | Used by ping and traceroute utilities |
| IGMP         | Internet Group Management Protocol         | -           | Manages IP multicast group memberships                 | Susceptible to multicast spoofing; DoS potential          | Group membership manipulation                | IPTV, multicast streaming             |
| IPsec        | Internet Protocol Security                 | -           | Encrypts and authenticates IP packets                  | Misconfiguration; outdated ciphers can be exploited       | MITM; replay attacks                         | Securing VPN tunnels                  |
| BGP          | Border Gateway Protocol                    | 179         | Routes data between autonomous systems on the Internet | Route hijacking; misconfiguration risks                   | BGP hijacking; route leaks                   | Core Internet routing                 |
| OSPF         | Open Shortest Path First                   | -           | Interior gateway routing using link-state information  | LSA spoofing; route manipulation vulnerabilities          | LSA flooding; spoofing                       | Enterprise and ISP routing            |
| EIGRP        | Enhanced Interior Gateway Routing Protocol | -           | Cisco’s efficient routing protocol                     | Proprietary; misconfigurations may expose vulnerabilities | Spoofed routing updates                      | Used in Cisco networks                |
| RIP          | Routing Information Protocol               | 520         | Simple distance-vector routing protocol                | Slow convergence; count-to-infinity problem               | Route poisoning; spoofing                    | Small/legacy networks                 |
| IS-IS        | Intermediate System to Intermediate System | -           | Link-state routing for large networks                  | Complex configurations may lead to vulnerabilities        | Misconfiguration; spoofed link state packets | Carrier-grade and enterprise networks |
| GRE          | Generic Routing Encapsulation              | -           | Encapsulates packets for tunneling                     | Unencrypted by default; can be exploited if not protected | Tunnel hijacking; packet injection           | VPN tunnels, multicast encapsulation  |

***

<mark style="color:yellow;">**Data Link Layer (Layer 2)**</mark>

Responsible for physical addressing and frame delivery on a local network segment.

**Switching & Ethernet Protocols**

| **Protocol** | **Full Form**                | **Port(s)** | **Purpose**                                              | **Vulnerabilities**                                 | **Attack Methods**                  | **Implementation Example**     |
| ------------ | ---------------------------- | ----------- | -------------------------------------------------------- | --------------------------------------------------- | ----------------------------------- | ------------------------------ |
| Ethernet     | IEEE 802.3                   | -           | Wired LAN communication via MAC addresses                | Vulnerable to MAC spoofing; VLAN hopping risks      | ARP spoofing; MAC flooding          | Office LANs, data centers      |
| PPP          | Point-to-Point Protocol      | -           | Encapsulation of network-layer packets over serial links | Weak authentication; prone to replay attacks        | Password cracking; replay attacks   | Dial-up connections, WAN links |
| HDLC         | High-Level Data Link Control | -           | Synchronous serial communication                         | Predictable framing; no encryption                  | Frame injection                     | Serial WAN links               |
| ARP          | Address Resolution Protocol  | -           | Maps IP addresses to MAC addresses                       | ARP spoofing/poisoning; lacks authentication        | MITM via ARP poisoning              | LAN communications             |
| STP          | Spanning Tree Protocol       | -           | Prevents loops in redundant switched networks            | Vulnerable to BPDU spoofing; lack of authentication | BPDU manipulation; topology attacks | Enterprise switch networks     |

***

#### <mark style="color:yellow;">**Physical Layer (Layer 1)**</mark>

Covers the transmission of raw bits over a physical medium.

**Physical Transmission Protocols**

| **Protocol** | **Full Form**                   | **Port(s)** | **Purpose**                                         | **Vulnerabilities**                                          | **Attack Methods**                     | **Implementation Example**              |
| ------------ | ------------------------------- | ----------- | --------------------------------------------------- | ------------------------------------------------------------ | -------------------------------------- | --------------------------------------- |
| Wi-Fi        | IEEE 802.11                     | -           | Wireless LAN communication                          | WEP weaknesses; misconfigured WPA; signal interference       | WEP cracking; deauthentication attacks | Home/office wireless networks           |
| Bluetooth    | Wireless Communication Standard | -           | Short-range wireless data exchange                  | Bluejacking; Bluebugging; weak pairing protocols             | Pairing exploits; sniffing             | Wireless peripherals, headsets          |
| Zigbee       | IEEE 802.15.4                   | -           | Low-power, low-data-rate wireless for IoT devices   | Weak encryption; interference; limited range                 | Eavesdropping; replay attacks          | Smart home sensors, lighting systems    |
| LoRaWAN      | Long Range Wide Area Network    | -           | Long-distance, low-power IoT connectivity           | Limited encryption; susceptibility to physical layer jamming | Signal jamming; interference           | Agricultural sensors, smart cities      |
| NFC          | Near Field Communication        | -           | Contactless data exchange over very short distances | Vulnerable to relay attacks; eavesdropping                   | Relay attacks; unauthorized access     | Mobile payments, access control systems |

***

## <mark style="color:red;">**Security & Authentication Protocols**</mark>

Protocols that secure communication, authenticate users, and protect data integrity.

<mark style="color:yellow;">**Secure Communication & Encryption**</mark>

**Encryption Protocols**

| **Protocol** | **Full Form**                                   | **Port(s)** | **Purpose**                                      | **Vulnerabilities**                                    | **Attack Methods**                 | **Implementation Example** |
| ------------ | ----------------------------------------------- | ----------- | ------------------------------------------------ | ------------------------------------------------------ | ---------------------------------- | -------------------------- |
| IPsec        | Internet Protocol Security                      | -           | Encrypts and authenticates IP packets (for VPNs) | Misconfiguration; outdated or weak ciphers             | MITM; replay attacks               | Securing VPN tunnels       |
| SSL/TLS      | Secure Sockets Layer / Transport Layer Security | 443         | Secures web traffic via encryption               | Vulnerable to Heartbleed, POODLE; certificate spoofing | SSL stripping; certificate forgery | HTTPS websites             |

<mark style="color:yellow;">**Authentication & Authorization**</mark>

**Authentication Protocols**

| **Protocol** | **Full Form**                                         | **Port(s)**              | **Purpose**                                          | **Vulnerabilities**                                           | **Attack Methods**                         | **Implementation Example**             |
| ------------ | ----------------------------------------------------- | ------------------------ | ---------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------ | -------------------------------------- |
| Kerberos     | (Ticket-based Authentication Protocol)                | 88                       | Secure ticket-based authentication                   | Ticket theft; weak encryption if misconfigured                | Pass-the-ticket; brute-force attacks       | Windows Active Directory, Unix systems |
| OAuth        | Open Authorization                                    | -                        | Delegates API authorization without password sharing | Token leakage; CSRF attacks                                   | Token hijacking; phishing                  | Social logins (Google, Facebook)       |
| SAML         | Security Assertion Markup Language                    | -                        | Single sign-on (SSO) for web applications            | XML signature wrapping; replay attacks                        | Token replay; XML signature forgery        | Enterprise SSO systems                 |
| RADIUS       | Remote Authentication Dial-In User Service            | 1812 (auth), 1813 (acct) | Centralized network authentication and accounting    | Default community strings; misconfiguration                   | Brute-force; dictionary attacks            | Network access control in enterprises  |
| TACACS+      | Terminal Access Controller Access-Control System Plus | 49                       | Detailed access control & accounting                 | Insecure implementations; weak encryption                     | Credential harvesting; brute-force attacks | Cisco network device authentication    |
| PGP          | Pretty Good Privacy                                   | -                        | Encrypts emails and files for data integrity         | Key management challenges; outdated algorithms if not updated | Key compromise; social engineering attacks | Secure email communication             |

***

## <mark style="color:red;">**Routing & Switching Protocols**</mark>

Protocols that govern the path of data across networks and manage local traffic switching.

<mark style="color:yellow;">**Routing Protocols**</mark>

**Interior & Exterior Gateway Protocols**

| **Protocol** | **Full Form**                              | **Port(s)** | **Purpose**                                            | **Vulnerabilities**                                                 | **Attack Methods**                           | **Implementation Example**              |
| ------------ | ------------------------------------------ | ----------- | ------------------------------------------------------ | ------------------------------------------------------------------- | -------------------------------------------- | --------------------------------------- |
| BGP          | Border Gateway Protocol                    | 179         | Routes data between autonomous systems on the Internet | Susceptible to route hijacking; misconfigurations                   | BGP hijacking; route leaks                   | Core Internet routing                   |
| OSPF         | Open Shortest Path First                   | -           | Interior gateway routing using link-state information  | LSA spoofing; route manipulation                                    | LSA flooding; spoofing                       | Enterprise and ISP networks             |
| EIGRP        | Enhanced Interior Gateway Routing Protocol | -           | Cisco's efficient proprietary routing protocol         | Proprietary protocol; misconfigurations can lead to vulnerabilities | Spoofed routing updates                      | Cisco-based networks                    |
| RIP          | Routing Information Protocol               | 520         | Simple distance-vector routing protocol                | Slow convergence; count-to-infinity issues                          | Route poisoning; spoofing                    | Small/legacy networks                   |
| IS-IS        | Intermediate System to Intermediate System | -           | Link-state routing for large networks                  | Complex configurations; potential for misconfiguration              | Spoofed link state packets; misconfiguration | Carrier-grade networks                  |
| VRRP         | Virtual Router Redundancy Protocol         | -           | Provides router redundancy and failover                | Lack of encryption; vulnerable to spoofing                          | MITM on failover messages                    | Redundant gateway setups in enterprises |

***

## **VoIP & Telecommunication Protocols**

Protocols that support voice, video, and multimedia communication over IP networks.

<mark style="color:yellow;">**VoIP Protocols**</mark>

**Voice and Multimedia Signaling**

| **Protocol** | **Full Form**                  | **Port(s)** | **Purpose**                                         | **Vulnerabilities**                                  | **Attack Methods**               | **Implementation Example**                     |
| ------------ | ------------------------------ | ----------- | --------------------------------------------------- | ---------------------------------------------------- | -------------------------------- | ---------------------------------------------- |
| SIP          | Session Initiation Protocol    | 5060, 5061  | Establishes, modifies, and terminates VoIP sessions | SIP message tampering; DoS; spoofing vulnerabilities | SIP flooding; call hijacking     | VoIP services (e.g., Skype, Cisco CallManager) |
| MGCP         | Media Gateway Control Protocol | -           | Controls media gateways in VoIP networks            | Insecure gateway control; misconfiguration           | Command injection; spoofing      | Telecom carrier networks                       |
| RTP          | Real-Time Transport Protocol   | -           | Delivers real-time audio/video over IP networks     | Lack of encryption (unless using SRTP)               | Packet injection; replay attacks | Video conferencing, streaming applications     |
| H.323        | ITU-T Standard for VoIP        | 1720        | Signaling for multimedia communications             | Complexity may lead to misconfiguration              | Session hijacking; spoofing      | Legacy VoIP systems                            |

***

## <mark style="color:red;">**Storage & File Transfer Protocols**</mark>

Protocols for accessing, sharing, and storing data over networks.

<mark style="color:yellow;">**Storage Protocols**</mark>

**File Sharing & Storage Networking**

| **Protocol** | **Full Form**                            | **Port(s)** | **Purpose**                                              | **Vulnerabilities**                                    | **Attack Methods**                                    | **Implementation Example**                  |
| ------------ | ---------------------------------------- | ----------- | -------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------- | ------------------------------------------- |
| NFS          | Network File System                      | -           | Enables remote file sharing in Unix/Linux environments   | Weak authentication; misconfigurations                 | Unauthorized access; exploitation of file permissions | Linux/Unix network file shares              |
| SMB          | Server Message Block                     | 445         | Facilitates file and printer sharing on Windows networks | Vulnerable to worm attacks (e.g., WannaCry)            | Exploitation (e.g., EternalBlue vulnerability)        | Windows enterprise file sharing             |
| CIFS         | Common Internet File System              | -           | Variant of SMB for file sharing                          | Similar to SMB vulnerabilities                         | Worm attacks; brute-force attacks                     | Legacy Windows networks                     |
| iSCSI        | Internet Small Computer System Interface | -           | Transports SCSI commands over IP networks (SANs)         | Insecure configurations; lack of encryption            | MITM attacks; session hijacking                       | Storage Area Networks (SAN) in data centers |
| FCoE         | Fibre Channel over Ethernet              | -           | Carries Fibre Channel frames over Ethernet               | Complexity; misconfigurations; interoperability issues | Layer 2 attacks; spoofing                             | Data center storage networks                |

***

## <mark style="color:red;">**Cloud & Virtualization Protocols**</mark>

Protocols that facilitate virtual networking and cloud infrastructure.

<mark style="color:yellow;">**Virtualization & Cloud Networking**</mark>

**Virtual Network Protocols**

| **Protocol** | **Full Form**                    | **Port(s)** | **Purpose**                                            | **Vulnerabilities**                                    | **Attack Methods**                          | **Implementation Example**       |
| ------------ | -------------------------------- | ----------- | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------- | -------------------------------- |
| VXLAN        | Virtual Extensible LAN           | -           | Extends Layer 2 networks over a Layer 3 infrastructure | Complexity in key management; configuration errors     | Tunnel hijacking; misconfiguration exploits | Cloud data center overlays       |
| GRE          | Generic Routing Encapsulation    | -           | Encapsulates packets for tunneling (used in VPNs)      | Unencrypted by default; potential packet injection     | Tunnel hijacking; spoofing attacks          | Site-to-site VPN tunnels         |
| STT          | Stateless Transport Tunneling    | -           | Provides efficient tunneling for virtual networks      | Limited adoption; potential misconfiguration risks     | Exploitation via misconfiguration           | Virtualized network environments |
| NVGRE        | Network Virtualization using GRE | -           | Supports multi-tenant virtualized environments         | Similar vulnerabilities to GRE; complex key management | Tunnel manipulation; spoofing               | Cloud service provider networks  |

***

## <mark style="color:red;">**Blockchain & Cryptocurrency Protocols**</mark>

Protocols that underpin decentralized systems and digital currencies.

<mark style="color:yellow;">**Blockchain Networks**</mark>

**Cryptocurrency & Decentralized Storage Protocols**

| **Protocol**      | **Full Form**                    | **Port(s)** | **Purpose**                                                   | **Vulnerabilities**                           | **Attack Methods**                    | **Implementation Example**         |
| ----------------- | -------------------------------- | ----------- | ------------------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ---------------------------------- |
| Bitcoin P2P       | Bitcoin Peer-to-Peer Protocol    | -           | Facilitates decentralized Bitcoin transactions                | 51% attacks; double-spending risks            | Majority attack; network partitioning | Bitcoin network nodes              |
| Ethereum RLPx     | Ethereum Network Protocol (RLPx) | -           | Manages peer discovery and secure communications for Ethereum | Smart contract vulnerabilities; Sybil attacks | DDoS; Sybil attacks                   | Ethereum blockchain nodes          |
| IPFS              | InterPlanetary File System       | -           | Decentralized file storage and sharing                        | Content poisoning; data persistence issues    | Distributed DoS; node impersonation   | Decentralized applications (dApps) |
| Lightning Network | Bitcoin Micropayment Protocol    | -           | Enables fast, low-fee off-chain Bitcoin transactions          | Routing attacks; channel jamming              | Denial-of-Service on channels         | Bitcoin micropayment networks      |

***
