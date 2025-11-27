---
description: >-
  these notes are based on content given by Guruji on File system and their
  security
---

# Poking the Filesystem - slide 1

<figure><img src=".gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

## Slide 1: Filesystem Trust Kyun Badi Problem Hai

<mark style="color:yellow;">**Kya problem hai?**</mark>\
\
User-space software (jaise browsers, apps, ya editors) aur security tools (jaise EDRs) filesystem se aane wale data ko bina kisi check ke sach maan lete hain. Yeh ek bada issue hai kyunki hackers iska fayda utha kar fake ya malicious data dikha sakte hain, jisse system compromise ho sakta hai.

* <mark style="color:yellow;">**Example**</mark><mark style="color:yellow;">:</mark> Ek file mein virus hota hai, lekin filesystem usse "safe" file jaisa dikha deta hai, jisse software usse khol deta hai.



<mark style="color:yellow;">**Kyun problem hai?**</mark>

\
Filesystem files ka data aur metadata (jaise naam, size, permissions) store karta hai. Agar hackers isse manipulate kar dein, toh software aur security tools ko galat info milti hai.

* <mark style="color:yellow;">**Example**</mark><mark style="color:yellow;">:</mark> Ek virus wali file ka metadata badal ke "safe" .txt file jaisa dikha diya jaye, toh software bina verify kiye uspe trust kar lega.
* <mark style="color:yellow;">**Detail**</mark><mark style="color:yellow;">:</mark> Filesystem ek storage layer hai, aur agar isme koi weakness ho, toh hackers data ya metadata change kar sakte hain, jisse software ko dhokha milta hai.



<mark style="color:yellow;">**Security tools ka issue kya hai?**</mark>

\
EDRs (Endpoint Detection and Response) jaise tools bhi filesystem ke data pe depend karte hain. Agar hacker file ya metadata badal de, toh EDRs usse safe samajh lete hain.

* **Example**: Ek malicious file ko hacker "photo.jpg" jaisa dikha de, toh EDR usse deeply scan nahi karega kyunki woh metadata pe bharosa karta hai.
* **Detail**: EDRs metadata ya file signatures check karte hain, lekin agar yeh fake ho, toh woh malware detect nahi kar pate.



<mark style="color:yellow;">**Kyun risky hai?**</mark>

\
Hackers filesystem ke weaknesses ka fayda uthate hain:

* **Rootkits**: Yeh tools filesystem ke data ko hide ya change kar sakte hain.
* **Kernel Attacks**: Hackers kernel-level access leke filesystem ke core functions ko manipulate karte hain.
* **Impact**: Fake data se system hack ho sakta hai, sensitive data churi ho sakti hai, ya malware pura system infect kar sakta hai.



<mark style="color:yellow;">**Kya karna chahiye?**</mark>



* Filesystem ke data pe blindly trust nahi karna chahiye.
* **Solutions**:
  * **Cryptographic Verification**: Files ka hash (jaise SHA-256 ya MD5) check karo taaki data original hai ya nahi, pata chale.
  * **Kernel-Level Monitoring**: Filesystem ke low-level operations track karo taaki galat changes pakde ja sakein.
  * **File Integrity Monitoring**: Regular scans karo taaki files aur metadata mein suspicious changes dikhe toh alert mile.
  * **Sandboxing**: Shady files ko isolated environment mein kholo taaki system safe rahe.

<mark style="color:yellow;">**Key Points**</mark><mark style="color:yellow;">:</mark>

* User-space software aur EDRs filesystem ke data ko bina check kiye sach samajhte hain.
* Hackers metadata ya data manipulate karke software ko fool kar sakte hain.
* Rootkits aur kernel attacks se fake data dikha kar system hack hota hai.
* Solutions: Cryptographic hash, kernel monitoring, file integrity checks, aur sandboxing zaroori hain.\
  <br>

<mark style="color:yellow;">**Follow up questions to slide 1 -**</mark><br>
---------------------------------------------------------------------------

#### <mark style="color:yellow;">**1. Filesystem "Safe" ya "Unsafe" Tags Kaise Decide Karta Hai?**</mark>

Filesystem khud se "safe" ya "unsafe" tags nahi lagata. Yeh basically ek storage layer hai jo files aur unka metadata (jaise naam, size, permissions, timestamps) organize karta hai. Yeh metadata batata hai ki file kya hai, lekin "safe" ya "unsafe" ka faisla filesystem ka kaam nahi hai – yeh security tools (jaise AVs, EDRs) ka kaam hai.

* **Kaise hota hai?**\
  Filesystem sirf metadata provide karta hai. For example, ek file ka naam "virus.exe" hai ya "doc.pdf", size kya hai, ya permissions kya hain – yeh info filesystem deta hai. Lekin isse "safe" ya "unsafe" judge karna security software pe depend karta hai, jo metadata ya file content ko analyze karta hai.
* **Example**: Ek file mein virus hai, lekin filesystem usse "safe" file jaisa dikha deta hai kyunki metadata manipulate ho sakta hai (jaise naam ya type change kar diya jaye). Filesystem khud yeh nahi check karta ki file dangerous hai ya nahi – woh bas data serve karta hai.

#### <mark style="color:yellow;">**2. Modern AVs, Defenders, Firewalls, aur Security Mechanisms Isko Kyun Maante Hain?**</mark>

Security tools filesystem ke metadata pe trust kyun karte hain? Simple – speed aur efficiency ke liye.

* <mark style="color:yellow;">**Kyun Trust Karte Hain?**</mark>
  * Filesystem ka data fast access deta hai. Har file ko deeply scan karna time-consuming hai, toh tools metadata (naam, size, timestamps) pe rely karte hain taaki jaldi decision le sakein.
  * Normally, filesystem ka data accurate hota hai, toh yeh ek reliable starting point hai.
  * **Example**: Ek EDR tool file ka metadata dekhta hai – agar naam "safe.pdf" hai aur size normal lagta hai, toh woh usse safe assume kar sakta hai bina pura file scan kiye.
* <mark style="color:yellow;">**Kyun Verify Nahi Karte?**</mark>
  * Deep verification (jaise cryptographic hash check karna) slow hota hai aur system ke performance pe load daalta hai.
  * Har file ko verify karna practical nahi hai, especially jab lakhs files ho. Isliye trade-off karte hain – speed ke liye risk lete hain.
  * Agar filesystem compromise ho jata hai (jaise rootkit attack se), toh yeh trust break ho sakta hai, lekin yeh rare case hai, isliye tools risk accept karte hain.

#### <mark style="color:yellow;">**3. Filesystem Metadata Kahaan Aur Kaise Store Karta Hai?**</mark>

Ab baat karte hain metadata ke storage ki.

* <mark style="color:yellow;">**Kahaan Store Hota Hai?**</mark>\
  Filesystem metadata ko special structures mein rakhta hai. Jaise:
  * **Unix/Linux**: "Inodes" mein metadata store hota hai. Har file ke liye ek inode hota hai jisme naam, size, permissions, timestamps, aur file location ka data hota hai.
  * **Windows (NTFS)**: "Master File Table (MFT)" mein metadata rakha jata hai, jo similar info store karta hai.
  * Yeh structures filesystem ke alag part mein hoti hain, separate from actual file content.
* <mark style="color:yellow;">**Kaise Generate Hota Hai?**</mark>\
  Jab tum ek file create ya modify karte ho, filesystem automatically metadata generate karta hai.
  * **Example**: Tumne "photo.jpg" save kiya – filesystem uska naam, creation time, size, aur permissions set karta hai. Yeh OS aur filesystem ke rules ke hisaab se hota hai.
* <mark style="color:yellow;">**Kaise Modify Kar Sakte Hain?**</mark>
  * **Normal way**: Tum file properties change kar sakte ho (jaise naam ya permissions) OS ke through.
  * **Malicious way**: Hackers rootkits ya kernel-level attacks use karke metadata ko manipulate kar sakte hain. Yeh filesystem ke functions ko hijack karke hota hai – jaise file ka size ya type badal dena.

#### <mark style="color:yellow;">**4. Filesystem Ek Storage Layer Hai, Toh Metadata Ko Kaise Manage Karta Hai?**</mark>

Filesystem sirf storage nahi, balki ek management layer bhi hai. Yeh files aur metadata ko organize aur track karta hai.

* <mark style="color:yellow;">**Kaise Manage Karta Hai?**</mark>
  * Filesystem ek index ya table maintain karta hai (jaise inodes ya MFT) jisme har file ka metadata hota hai.
  * Jab tum file open ya save karte ho, filesystem is index se metadata fetch karta hai taaki file locate aur access ho sake.
  * <mark style="color:yellow;">**Example**</mark><mark style="color:yellow;">:</mark> Jab tum "photo.jpg" kholte ho, filesystem inode ya MFT se uska location aur permissions check karta hai.
* <mark style="color:yellow;">**Metadata Manipulation Kaise Hota Hai?**</mark>
  * <mark style="color:yellow;">**Normal Control**</mark><mark style="color:yellow;">:</mark> OS ke commands (jaise `chmod` ya properties edit) se metadata change hota hai.
  * <mark style="color:yellow;">**Malicious Control**</mark><mark style="color:yellow;">:</mark> Hackers kernel ya filesystem drivers ko target karte hain. Rootkits se woh metadata-serving functions ko hook kar sakte hain, jisse fake info dikhe.
    * <mark style="color:yellow;">**Example**</mark><mark style="color:yellow;">:</mark> Ek virus file ka naam "safe.pdf" aur size chhota dikha sakta hai, taaki security tools usse ignore karein.

#### <mark style="color:yellow;">**Key Takeaways**</mark>

* Filesystem "safe" ya "unsafe" decide nahi karta – woh metadata provide karta hai, jisse security tools judge karte hain.
* Security tools ispe trust karte hain kyunki yeh fast hai, lekin deep verification slow hota hai isliye skip karte hain.
* Metadata inodes ya MFT jaise structures mein store hota hai, jo filesystem generate aur manage karta hai.
* Hackers metadata ko kernel attacks ya rootkits se manipulate kar sakte hain, jo security ke liye risk hai.

### Kyun Karte Hain Hackers Yeh?

Filesystem ko hack karna ek powerful tareeka hai system mein ghusne aur control banane ka. Yeh ek aisa layer hai jisse pura system depend karta hai, toh ispe attack karna hackers ke liye jackpot jaisa hai.



* **Strong Foothold in System**\
  Filesystem system ka core part hai – yeh files aur metadata manage karta hai, jo har software aur OS ke liye zaroori hai.
*

    * **Agar Filesystem Driver Compromise Ho Gaya**\
      Ek baar filesystem driver (jo filesystem ke operations handle karta hai) mein backdoor ya compromise ho jaye, toh hacker ke liye game over hai – system puri tarah unke control mein aa sakta hai.\
      &#xNAN;_&#x45;xample_: Ek backdoored driver fake metadata dikha sakta hai, jaise malicious file ko “safe.pdf” jaisa dikha kar EDR ya antivirus ko bypass kar sakta hai.\
      &#xNAN;_&#x44;etail_: Filesystem driver kernel-level pe kaam karta hai, jisme highest privileges hote hain. Iska compromise matlab pura system vulnerable ho jata hai – data chori, malware spread, ya system crash tak ho sakta hai.



    *   **Detection Mushkil Hai**\
        Filesystem compromise ko detect karna bahut hard hai kyunki:

        * Security tools bhi filesystem ke data pe depend karte hain, aur agar wohi fake ho, toh unhe sachchai pata nahi chalti.
        * Rootkits jaise tools filesystem ke functions ko hide kar sakte hain, jisse malicious activity dikhti hi nahi.\
          &#xNAN;_&#x45;xample_: Ek rootkit ek virus file ko filesystem se chhupa sakta hai, jisse EDR ya antivirus usse detect na kare.


* **Mushkil Hai, Isliye Attractive Hai**\
  Filesystem hacking mushkil kaam hai, lekin iska reward bhi bada hai.
  * **Social Brownie Points**\
    Hacking community mein, mushkil targets (jaise filesystem ya kernel) ko hack karna ek bada achievement mana jata hai.\
    &#xNAN;_&#x45;xample_: Ek hacker jo filesystem driver hack kar leta hai, usse underground forums ya dark web mein respect milta hai, kyunki yeh ek rare aur complex skill hai.\
    &#xNAN;_&#x44;etail_: Yeh na sirf financial gain (jaise ransomware ya data theft) deta hai, balki hacker ke reputation ko bhi boost karta hai.

### Kyun Risky Hai Yeh System Ke Liye?

* **Complete Control**: Filesystem compromise se hacker system ke har part ko manipulate kar sakta hai – files, processes, ya network activity.
* **Stealth**: Rootkits aur backdoors ke through, hacker apni activity hide kar sakta hai, jisse security tools clueless reh jate hain.
* **Long-Term Damage**: Ek compromised filesystem se data leaks, malware spread, ya system corruption ho sakta hai, jo detect hone mein months lag sakte hain.

### Kya Karna Chahiye?

* **Kernel-Level Protection**: Filesystem drivers aur kernel ko secure karne ke liye strong measures lagao, jaise driver signing aur kernel monitoring.
* **Regular Audits**: Filesystem ke low-level operations aur drivers ke behavior ko regularly check karo taaki backdoors ya anomalies pakde ja sakein.
* **Intrusion Detection Systems**: Advanced IDS use karo jo kernel-level changes ya suspicious filesystem activity ko detect kare.
* **Least Privilege Principle**: Filesystem drivers aur processes ko minimum permissions do taaki compromise ka impact kam ho.

### Key Points

* Filesystem compromise hackers ke liye ek strong foothold deta hai kyunki yeh system ka core part hai.
* Compromised filesystem driver se pura system hack ho sakta hai, aur detection bahut mushkil hai.
* Yeh mushkil kaam hai, jo hackers ke liye financially aur socially rewarding hai.
* Solutions: Kernel protection, regular audits, IDS, aur least privilege principle se risk kam kiya ja sakta hai.
