# CCNA Class 4

Transportation Layer -&#x20;

it breaks up data into smaller parts as complere data can't be send over the network as a single unit.

so it has to be converted / divided into many smaller units (called data units) before transmission at sending side, which are then re-assembled at receiving side.

This whole process is called segmentation, and these smaller units are called segments at transport layer

it enables end to end connectivity using port numbers

ensure reliable data delivery via error detection and re-transmission using TCP&#x20;

protocols used  -&#x20;

TCP is used for reliable communication ( by TCP 3-way handshaking process )

eg -  SMTP, FTP

UDP is used for unreliable communications

eg - phone calls and video calls



port numbers: range -  0 to 65535

0 - 1023 are well known ports

1024 - 64511 are used for general client service sessions

64512 - 65535 are private or dedicated port numbers&#x20;

socket - ip address + port numbers





Network Layer -&#x20;

it provides connectivity and path selection

routing ( packet switching )

defines logical addressing (ipv4  and ipv6)

devices and protocols at this layer ( router , ipv4, ipv6 , icmp)



the IPCONFIG command in CMD gives IP related details&#x20;



Data link Layer -&#x20;

it completes the final formatting of the data before actually sending it over the physical links



defines physical addressing - MAC addressing&#x20;

controls error detection&#x20;

cyclic redundancy check (CRC)

deviceds and protocols at L2:&#x20;

switches , bridges , wireless access points, ethernet ,PPP



Physical Layer -

it defines physcial media properties&#x20;

electrical / optical functions&#x20;

physcial data rates

physical connectors

cable distances

optical wavelength&#x20;

wireless frequencies



Devices and protocols&#x20;

hubs, repeaters, CAT cables, Fiber Optics , Etc







why use layered architecture ?



devices only need to be aware of their own layer - web servers don;t care if the request are coming from wired cables ot wireless frequencies&#x20;

switches don;t care if they are sending either IPv4 or IPv6 as they have nothing to do with it&#x20;



allows inter-operabuluty between devices and vendors&#x20;

google chrome can freely talk to apache server as they both agree on HTML standards&#x20;

HUAWEI ethernet switch can talk to apache server as they both agree on HTML standards

CISCO router can connect to juniper router as they agree on IP routing standards



