import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import re
from dotenv import load_dotenv
import os
load_dotenv()

security_code = os.getenv('SECURITY_CODE')
client = MongoClient("mongodb+srv://krishnakalyan:"+security_code)
url="https://www.javatpoint.com/operating-system-interview-questions"

db = client.get_database('Interview_Questions')

os = db.os

# r=requests.get(url)
r = """
<td>
<img src="https://static.javatpoint.com/interview/images/networking-interview-questions.png" alt="Networking Interview Questions" class="imageright">
<h1 class="h1">Networking Interview Questions</h1>
<p>A list of top frequently asked <strong>networking interview questions</strong> and answers are given below</p>
<h3 class="h3">1) What is the network?</h3>
<ul class="points">
<li>A network is a set of devices that are connected with a physical media link. In a network, two or more nodes are connected by a physical link or two or more networks are connected by one or more nodes.</li>
<li>A network is a collection of devices connected to each other to allow the sharing of data.</li>
<li>Example of a network is an internet. An internet connects the millions of people across the world.</li>
</ul>
<hr>
<h3 class="h3">2) What do you mean by network topology?</h3>
<p>Network topology specifies the layout of a computer network. It shows how devices and cables are connected to each other. The types of topologies are:</p>
<p><strong>Bus:</strong></p>
<img src="https://static.javatpoint.com/interview/images/networking-interview-questions2.png" alt="Networking Interview Questions">
<ul class="points">
<li>Bus topology is a network topology in which all the nodes are connected to a single cable known as a central cable or bus.</li>
<li>It acts as a shared communication medium, i.e., if any device wants to send the data to other devices, then it will send the data over the bus which in turn sends the data to all the attached devices.</li>
<li>Bus topology is useful for a small number of devices. As if the bus is damaged then the whole network fails.</li>
</ul>
<p><strong>Star:</strong></p>
<img src="https://static.javatpoint.com/interview/images/networking-interview-questions3.png" alt="Networking Interview Questions">
<ul class="points">
<li>Star topology is a network topology in which all the nodes are connected to a single device known as a central device.</li>
<li>Star topology requires more cable compared to other topologies. Therefore, it is more robust as a failure in one cable will only disconnect a specific computer connected to this cable.</li>
<li>If the central device is damaged, then the whole network fails.</li>
<li>Star topology is very easy to install, manage and troubleshoot.</li>
<li>Star topology is commonly used in office and home networks.</li>
</ul>
<p><strong>Ring</strong></p>
<img src="https://static.javatpoint.com/interview/images/networking-interview-questions4.png" alt="Networking Interview Questions">
<ul class="points">
<li>Ring topology is a network topology in which nodes are exactly connected to two or more nodes and thus, forming a single continuous path for the transmission.</li>
<li>It does not need any central server to control the connectivity among the nodes.</li>
<li>If the single node is damaged, then the whole network fails.</li>
<li>Ring topology is very rarely used as it is expensive, difficult to install and manage.</li>
<li>Examples of Ring topology are SONET network, SDH network, etc.</li>
</ul>
<p><strong>Mesh</strong></p>
<img src="https://static.javatpoint.com/interview/images/networking-interview-questions5.png" alt="Networking Interview Questions">
<ul class="points">
<li>Mesh topology is a network topology in which all the nodes are individually connected to other nodes.</li>
<li>It does not need any central switch or hub to control the connectivity among the nodes.</li>
<li>Mesh topology is categorized into two parts:
<ul class="points">
<li><strong>Fully connected mesh topology</strong>: In this topology, all the nodes are connected to each other.</li>
<li><strong>Partially connected mesh topology</strong>: In this topology, all the nodes are not connected to each other.</li>
</ul>
</li><li>It is a robust as a failure in one cable will only disconnect the specified computer connected to this cable.</li>
<li>Mesh topology is rarely used as installation and configuration are difficult when connectivity gets more.</li>
<li>Cabling cost is high as it requires bulk wiring.</li>

</ul>
<p><strong>Tree</strong></p>
<img src="https://static.javatpoint.com/interview/images/networking-interview-questions6.png" alt="Networking Interview Questions">
<ul class="points">
<li>Tree topology is a combination of star and bus topology. It is also known as the expanded star topology.</li>
<li>In tree topology, all the star networks are connected to a single bus.</li>
<li>Ethernet protocol is used in this topology.</li>
<li>In this, the whole network is divided into segments known as star networks which can be easily maintained. If one segment is damaged, but there is no effect on other segments.</li>
<li>Tree topology depends on the "main bus," and if it breaks, then the whole network gets damaged.</li>
</ul>
<p><strong>Hybrid</strong></p>
<ul class="points">
<li>A hybrid topology is a combination of different topologies to form a resulting topology.</li>
<li>If star topology is connected with another star topology, then it remains star topology. If star topology is connected with different topology, then it becomes a Hybrid topology.</li>
<li>It provides flexibility as it can be implemented in a different network environment.</li>
<li>The weakness of a topology is ignored, and only strength will be taken into consideration.</li>
</ul>
<hr>
<h3 class="h3">3) What are the advantages of Distributed Processing?</h3>
<p>A list of advantages of distributed processing:</p>
<ul class="points">
<li>Secure</li>
<li>Support Encapsulation</li>
<li>Distributed database</li>
<li>Faster Problem solving</li>
<li>Security through redundancy</li>
<li>Collaborative Processing</li>
</ul>
<hr>
<h3 class="h3">4) What is the criteria to check the network reliability?</h3>
<p><strong>Network reliability:</strong> Network reliability means the ability of the network to carry out the desired operation through a network such as communication through a network.</p>
<p>Network reliability plays a significant role in the network functionality. The network monitoring systems and devices are the essential requirements for making the network reliable.The network monitoring system identifies the problems that are occurred in the network while the network devices ensure that data should reach the appropriate destination.</p>
<p>The reliability of a network can be measured by the following factors:</p>
<ul class="points">
<li><strong>Downtime</strong>: The downtime is defined as the required time to recover.</li>
<li><strong>Failure Frequency</strong>: It is the frequency when it fails to work the way it is intended.</li>
<li><strong>Catastrophe</strong>: It indicates that the network has been attacked by some unexpected event such as fire, earthquake.</li>
</ul>
<hr>
<h3 class="h3">5) Which are the different factors that affect the security of a network?</h3>
<p>There are mainly two security affecting factors:</p>
<ul class="points">
<li>Unauthorized Access</li>
<li>Viruses</li>
</ul>
<hr>
<h3 class="h3">6) Which are the different factors that affect the reliability of a network?</h3>
<p>The following factors affect the reliability of a network:</p>
<ul class="points">
<li>Frequency of failure</li>
<li>Recovery time of a network after a failure</li>
</ul>
<hr>
<h3 class="h3">7) Which are the different factors that affect the performance of a network?</h3>
<p>The following factors affect the performance of a network:</p>
<ul class="points">
<li>Large number of users</li>
<li>Transmission medium types</li>
<li>Hardware</li>
<li>Software</li>
</ul>
<hr>
<h3 class="h3">8) What makes a network effective and efficient?</h3>
<p>There are mainly two criteria which make a network effective and efficient:</p>
<ul class="points">
<li><strong>Performance:</strong> : performance can be measured in many ways like transmit time and response time.</li>
<li><strong>Reliability:</strong> reliability is measured by frequency of failure.</li>
<li><strong>Robustness:</strong> robustness specifies the quality or condition of being strong and in good condition.</li>
<li><strong>Security:</strong> It specifies how to protect data from unauthorized access and viruses.</li>
</ul>
<hr>
<h3 class="h3">9) What is bandwidth?</h3>
<p>Every signal has a limit of upper range frequency and lower range frequency. The range of limit of network between its upper and lower frequency is called bandwidth.</p>
<hr>
<h3 class="h3">10) What is a node and link?</h3>
<p>A network is a connection setup of two or more computers directly connected by some physical mediums like optical fiber or coaxial cable. This physical medium of connection is known as a link, and the computers that it is connected are known as nodes.</p>
<hr>
<h3 class="h3">11) What is a gateway? Is there any difference between a gateway and router?</h3>
<p>A node that is connected to two or more networks is commonly known as a gateway. It is also known as a router. It is used to forward messages from one network to another. <strong>Both the gateway and router regulate the traffic in the network</strong>.</p>
<p><strong>Differences between gateway and router:</strong></p>
<p>A router sends the data between two similar networks while gateway sends the data between two dissimilar networks.</p>
<hr>
<script async="" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>

<ins class="adsbygoogle cm_jtp_wtc_responsive" style="display:inline-block" data-ad-client="ca-pub-4699858549023382" data-ad-slot="6746133113"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
<h3 class="h3">12) What is DNS?</h3>
<p>DNS is an acronym stands for Domain Name System.</p>
<ul class="points">
<li>DNS was introduced by Paul Mockapetris and Jon Postel in 1983.</li>
<li>It is a naming system for all the resources over the internet which includes physical nodes and applications. It is used to locate to resource easily over a network.</li>
<li>DNS is an internet which maps the domain names to their associated IP addresses.</li>
<li>Without DNS, users must know the IP address of the web page that you wanted to access.</li>
</ul>
<p><strong>Working of DNS:</strong></p>
<p>If you want to visit the website of "javaTpoint", then the user will type "<a href="https://www.javatpoint.com" target="_blank">https://www.javatpoint.com</a>" into the address bar of the web browser. Once the domain name is entered, then the domain name system will translate the domain name into the IP address which can be easily interpreted by the computer. Using the IP address, the computer can locate the web page requested by the user.</p>
<hr>
<h3 class="h3">13) What is DNS forwarder?</h3>
<ul class="points">
<li>A forwarder is used with DNS server when it receives DNS queries that cannot be resolved quickly. So it forwards those requests to external DNS servers for resolution.</li>
<li>A DNS server which is configured as a forwarder will behave differently than the DNS server which is not configured as a forwarder.</li>
<li><strong>Following are the ways that the DNS server behaves when it is configured as a forwarder</strong>:
<ul class="points">
<li>When the DNS server receives the query, then it resolves the query by using a cache.</li>
<li>If the DNS server is not able to resolve the query, then it forwards the query to another DNS server.</li>
<li>If the forwarder is not available, then it will try to resolve the query by using root hint.</li>
</ul>
</li>
</ul>
<hr>
<h3 class="h3">14) What is NIC?</h3>
<ul class="points">
<li>NIC stands for Network Interface Card. It is a peripheral card attached to the PC to connect to a network. Every NIC has its own MAC address that identifies the PC on the network.</li>
<li>It provides a wireless connection to a local area network.</li>
<li>NICs were mainly used in desktop computers.</li>
</ul>
<hr>
<h3 class="h3">15) What is the meaning of 10Base-T?</h3>
<p>It is used to specify data transfer rate. In 10Base-T, 10 specify the data transfer rate, i.e., 10Mbps. The word Base specifies the baseband as opposed to broadband. T specifies the type of the cable which is a twisted pair.</p>
<hr>
<h3 class="h3">16) What is NOS in computer networking?</h3>
<ul class="points">
<li>NOS stands for Network Operating System. It is specialized software which is used to provide network connectivity to a computer to make communication possible with other computers and connected devices.</li>
<li>NOS is the software which allows the device to communicate, share files with other devices.</li>
<li>The first network operating system was Novel NetWare released in 1983. Some other examples of NOS are Windows 2000, Windows XP, Linux, etc.</li>
</ul>
<hr>
<h3 class="h3">17) What are the different types of networks?</h3>
<p>Networks can be divided on the basis of area of distribution. For example:</p>
<ul class="points">
<li><strong>PAN (Personal Area Network)</strong>: Its range limit is up to 10 meters. It is created for personal use. Generally, personal devices are connected to this network. For example computers, telephones, fax, printers, etc.</li>
<li><strong>LAN (Local Area Network)</strong>: It is used for a small geographical location like office, hospital, school, etc.</li>
<li><strong>HAN (House Area Network)</strong>: It is actually a LAN that is used within a house and used to connect homely devices like personal computers, phones, printers, etc.</li>
<li><strong>CAN (Campus Area Network)</strong>: It is a connection of devices within a campus area which links to other departments of the organization within the same campus.</li>
<li><strong>MAN (Metropolitan Area Network)</strong>: It is used to connect the devices which span to large cities like metropolitan cities over a wide geographical area.</li>
<li><strong>WAN (Wide Area Network)</strong>: It is used over a wide geographical location that may range to connect cities and countries.</li>
<li><strong>GAN (Global Area Network)</strong>: It uses satellites to connect devices over global are.</li>
</ul>
<hr>
<h3 class="h3">18) What is POP3?</h3>
<p>POP3 stands for Post Office Protocol version3. POP is responsible for accessing the mail service on a client machine. POP3 works on two models such as Delete mode and Keep mode.</p>
<hr>
<h3 class="h3">19) What do you understand by MAC address?</h3>
<p>MAC stands for Media Access Control. It is the address of the device at the Media Access Control Layer of Network Architecture. It is a unique address means no two devices can have same MAC addresses.</p>
<hr>
<h3 class="h3">20) What is IP address?</h3>
<p>IP address is a unique 32 bit software address of a computer in a network system.</p>
<hr>
<h3 class="h3">21) What is private IP address?</h3>
<p>There are three ranges of IP addresses that have been reserved for IP addresses. They are not valid for use on the internet. If you want to access internet on these private IPs, you must have to use proxy server or NAT server.</p>

<hr>
<h3 class="h3">22) What is public IP address?</h3>
<p>A public IP address is an address taken by the Internet Service Provider which facilitates you to communication on the internet.</p>
<hr>
<h3 class="h3">23) What is APIPA?</h3>
<p>APIPA is an acronym stands for Automatic Private IP Addressing. This feature is generally found in Microsoft operating system.</p>
<hr>
<h3 class="h3">24) What is the full form of ADS?</h3>
<ul class="points">
<li>ADS stands for Active Directory Structure.</li>
<li>ADS is a microsoft technology used to manage the computers and other devices.</li>
<li>ADS allows the network administrators to manage the domains, users and objects within the network.</li>
<li>ADS consists of three main tiers:
<ul class="points">
<li><strong>Domain</strong>: Users that use the same database will be grouped into a single domain.</li>
<li><strong>Tree</strong>: Multiple domains can be grouped into a single tree.</li>
<li><strong>Forest</strong>: Multiple trees can be grouped into a single forest.</li>
</ul>
</li>
</ul>
<hr>
<h3 class="h3">25) What is RAID?</h3>
<p>RAID is a method to provide Fault Tolerance by using multiple Hard Disc Drives.</p>
<hr>
<h3 class="h3">26) What is anonymous FTP?</h3>
<p>Anonymous FTP is used to grant users access to files in public servers. Users which are allowed access to data in these servers do not need to identify themselves, but instead log in as an anonymous guest.</p>
<hr>
<h3 class="h3">27) What is protocol?</h3>
<p>A protocol is a set of rules which is used to govern all the aspects of information communication.</p>
<hr>
<h3 class="h3">28) What are the main elements of a protocol?</h3>
<p>The main elements of a protocol are:</p>
<ul class="points">
<li><strong>Syntax</strong>: It specifies the structure or format of the data. It also specifies the order in which they are presented.</li>
<li><strong>Semantics</strong>: It specifies the meaning of each section of bits.</li>
<li><strong>Timing</strong>: Timing specifies two characteristics: When data should be sent and how fast it can be sent.</li>
</ul>
<hr>
<h3 class="h3">29 What is the Domain Name System?</h3>
<p>There are two types of client/server programs. First is directly used by the users and the second supports application programs.</p>
<p>The Domain Name System is the second type supporting program that is used by other programs such as to find the IP address of an e-mail recipient.</p>
<hr>
<h3 class="h3">30) What is link?</h3>
<p>A link is connectivity between two devices which includes the cables and protocols used in order to make communication between devices.</p>
<hr>
<h3 class="h3">31) How many layers are in OSI reference model?</h3>
<p><strong>OSI reference model</strong>: OSI reference model is an ISO standard which defines a networking framework for implementing the protocols in seven layers. These seven layers can be grouped into three categories:</p>
<ul class="points">
<li><strong>Network layer</strong>: Layer 1, Layer 2 and layer 3 are the network layers.</li>
<li><strong>Transport layer</strong>: Layer 4 is a transport layer.</li>
<li><strong>Application layer</strong>. Layer 5, Layer 6 and Layer 7 are the application layers.</li>
</ul>
<p>There are 7 layers in the OSI reference model.</p>
<p><strong>1. Physical Layer</strong></p>
<ul class="points">
<li>It is the lowest layer of the OSI reference model.</li>
<li>It is used for the transmission of an unstructured raw bit stream over a physical medium.</li>
<li>Physical layer transmits the data either in the form of electrical/optical or mechanical form.</li>
<li>The physical layer is mainly used for the physical connection between the devices, and such physical connection can be made by using twisted-pair cable, fibre-optic or wireless transmission media.</li>
</ul>
<p><strong>2. DataLink Layer</strong></p>
<ul class="points">
<li>It is used for transferring the data from one node to another node.</li>
<li>It receives the data from the network layer and converts the data into data frames and then attach the physical address to these frames which are sent to the physical layer.</li>
<li>It enables the error-free transfer of data from one node to another node.<br>
<strong>Functions of Data-link layer:</strong></li>
</ul>
<img src="https://static.javatpoint.com/interview/images/osi-reference-model.png" alt="Networking Interview Questions">
<ul class="points">
<li><strong>Frame synchronization</strong>: Data-link layer converts the data into frames, and it ensures that the destination must recognize the starting and ending of each frame.</li>
<li><strong>Flow control</strong>: Data-link layer controls the data flow within the network.</li>
<li><strong>Error control</strong>: It detects and corrects the error occurred during the transmission from source to destination.</li>
<li><strong>Addressing</strong>: Data-link layer attach the physical address with the data frames so that the individual machines can be easily identified.</li>
<li><strong>Link management</strong>: Data-link layer manages the initiation, maintenance and, termination of the link between the source and destination for the effective exchange of data.</li>
</ul>
<p><strong>3. Network Layer</strong></p>
<ul class="points">
<li>Network layer converts the logical address into the physical address.</li>
<li>It provides the routing concept means it determines the best route for the packet to travel from source to the destination.<br>
<strong>Functions of network layer</strong>:</li>
</ul>
<img src="https://static.javatpoint.com/interview/images/osi-reference-model2.png" alt="Networking Interview Questions">
<ul class="points">
<li><strong>Routing</strong>: The network layer determines the best route from source to destination. This function is known as routing.</li>
<li><strong>Logical addressing</strong>: The network layer defines the addressing scheme to identify each device uniquely.</li>
<li><strong>Packetizing</strong>: The network layer receives the data from the upper layer and converts the data into packets. This process is known as packetizing.</li>
<li><strong>Internetworking</strong>: The network layer provides the logical connection between the different types of networks for forming a bigger network.</li>
<li><strong>Fragmentation</strong>: It is a process of dividing the packets into the fragments.</li>
</ul>
<p><strong>4. Transport Layer</strong></p>
<ul class="points">
<li>It delivers the message through the network and provides error checking so that no error occurs during the transfer of data.</li>
<li><strong>It provides two kinds of services</strong>:
<ul class="points">
<li><strong>Connection-oriented transmission</strong>: In this transmission, the receiver sends the acknowledgement to the sender after the packet has been received.</li>
<li><strong>Connectionless transmission</strong>: In this transmission, the receiver does not send the acknowledgement to the sender.</li>
</ul>
</li>
</ul>
<p><strong>5. Session Layer</strong></p>
<ul class="points">
<li>The main responsibility of the session layer is beginning, maintaining and ending the communication between the devices.</li>
<li>Session layer also reports the error coming from the upper layers.</li>
<li>Session layer establishes and maintains the session between the two users.</li>
</ul>
<p><strong>6. Presentation Layer</strong></p>
<ul class="points">
<li>The presentation layer is also known as a Translation layer as it translates the data from one format to another format.</li>
<li>At the sender side, this layer translates the data format used by the application layer to the common format and at the receiver side, this layer translates the common format into a format used by the application layer.<br>
<strong>Functions of presentation layer:</strong>
<ul class="points">
<li>Character code translation</li>
<li>Data conversion</li>
<li>Data compression</li>
<li>Data encryption</li>
</ul>
</li>
</ul>
<p><strong>7. Application Layer</strong></p>
<ul class="points">
<li>Application layer enables the user to access the network.</li>
<li>It is the topmost layer of the OSI reference model.</li>
<li>Application layer protocols are file transfer protocol, simple mail transfer protocol, domain name system, etc.</li>
<li>The most widely used application protocol is HTTP(Hypertext transfer protocol ). A user sends the request for the web page using HTTP.</li>
</ul>
<hr>
<h3 class="h3">32) What is the usage of OSI physical layer?</h3>
<p>The OSI physical layer is used to convert data bits into electrical signals and vice versa. On this layer, network devices and cable types are considered and setup.</p>
<hr>
<h3 class="h3">33) Explain the functionality of OSI session layer?</h3>
<p>OSI session layer provides the protocols and means for two devices on the network to communicate with each other by holding a session. This layer is responsible for setting up the session, managing information exchange during the session, and tear-down process upon termination of the session.</p>
<hr>
<h3 class="h3">34) What is the maximum length allowed for a UTP cable?</h3>
<p>The maximum length of UTP cable is 90 to 100 meters.</p>
<hr>
<h3 class="h3">35) What is RIP?</h3>
<ul class="points">
<li>RIP stands for Routing Information Protocol. It is accessed by the routers to send data from one network to another.</li>
<li>RIP is a dynamic protocol which is used to find the best route from source to the destination over a network by using the hop count algorithm.</li>
<li>Routers use this protocol to exchange the network topology information.</li>
<li>This protocol can be used by small or medium-sized networks.</li>
</ul>
<hr>
<h3 class="h3">36) What do you understand by TCP/IP?</h3>
<p>TCP/IP is short for Transmission Control Protocol /Internet protocol. It is a set of protocol layers that is designed for exchanging data on different types of networks.</p>
<hr>
<h3 class="h3">37) What is netstat?</h3>
<p>The "netstat" is a command line utility program. It gives useful information about the current TCP/IP setting of a connection.</p>
<hr>
<h3 class="h3">38) What do you understand by ping command?</h3>
<p>The "ping" is a utility program that allows you to check the connectivity between the network devices. You can ping devices using its IP address or name.</p>
<hr>
<h3 class="h3">39) What is Sneakernet?</h3>
<p>Sneakernet is the earliest form of networking where the data is physically transported using removable media.</p>
<hr>
<h3 class="h3">40) Explain the peer-peer process.</h3>
<p>The processes on each machine that communicate at a given layer are called peer-peer process.</p>
<hr>
<h3 class="h3">41) What is a congested switch?</h3>
<p>A switch receives packets faster than the shared link. It can accommodate and stores in its memory, for an extended period of time, then the switch will eventually run out of buffer space, and some packets will have to be dropped. This state is called a congested state.</p>
<hr>
<h3 class="h3">42) What is multiplexing in networking?</h3>
<p>In Networking, multiplexing is the set of techniques that is used to allow the simultaneous transmission of multiple signals across a single data link.</p>
<hr>
<h3 class="h3">43) What are the advantages of address sharing?</h3>
<p>Address sharing provides security benefit instead of routing. That's because host PCs on the Internet can only see the public IP address of the external interface on the computer that provides address translation and not the private IP addresses on the internal network.</p>
<hr>
<h3 class="h3">44) What is RSA Algorithm?</h3>
<p>RSA is short for Rivest-Shamir-Adleman algorithm. It is mostly used for public key encryption.</p>
<hr>
<h3 class="h3">45) How many layers are in TCP/IP?</h3>
<p>There are basic 4 layers in TCP/IP:</p>
<ol class="points">
<li>Application Layer</li>
<li>Transport Layer</li>
<li>Internet Layer</li>
<li>Network Layer</li>
</ol>
<hr>
<div id="interviewcategory">
<table class="alt">
<tbody><tr><td><a href="corejava-interview-questions#corebasicsinterview">Java Basics Interview Questions</a></td>
<td><a href="corejava-interview-questions#oopsinterview">Java OOPs Interview Questions</a></td></tr>
<tr><td><a href="java-multithreading-interview-questions">Java Multithreading Interview Questions</a></td>
<td><a href="corejava-interview-questions-3">Java String &amp; Exception Interview Questions</a></td></tr>
<tr><td><a href="java-collections-interview-questions">Java Collection Interview Questions</a></td>
<td><a href="jdbc-interview-questions">JDBC Interview Questions</a></td></tr>
<tr><td><a href="servletinterview">Servlet Interview Questions</a></td>
<td><a href="jspinterview">JSP Interview Questions</a></td></tr>
<tr><td><a href="spring-interview-questions"><span>Spring Interview Questions</span></a></td><td><a href="hibernate-interview-questions"><span>Hibernate Interview Questions</span></a></td></tr>
<tr><td><a href="pl-sql-interview-questions"><span>PL/SQL Interview Questions</span></a></td><td><a href="sql-interview-questions"><span>SQL Interview Questions</span></a></td></tr>
<tr><td><a href="oracle-interview-questions"><span>Oracle Interview Questions</span></a></td><td><a href="android-interview-questions"><span>Android Interview Questions</span></a></td></tr>
<tr><td><a href="sql-server-interview-questions"><span>SQL Server Interview Questions</span></a></td><td><a href="mysql-interview-questions"><span>MySQL Interview Questions</span></a></td></tr>
</tbody></table>
</div>
<br><br>
</td>   


"""



soup=BeautifulSoup(r,"html.parser")

# qsn=soup.find("td")
# print(soup.prettify)
h3_tags = soup.find_all('h3')


for h3 in h3_tags:
    # get the text of the <h3> tag
    h3_text = h3.get_text(strip=True)
    h3_text = re.sub(r'^\d+\)\s*', '', h3_text)
    
    # get the tags below the <h3> tag
    tags_below_h3 = []
    next_tag = h3.next_sibling
    while next_tag is not None and next_tag.name != 'h3':
        tags_below_h3.append(next_tag)
        next_tag = next_tag.next_sibling
        
    # extract the text of the tags below the <h3> tag
    tags_below_h3_text = ' '.join(tag.get_text(strip=True) for tag in tags_below_h3)
    
    # print the result as key-value pair
    d = {h3_text: tags_below_h3_text}

    print(d)

    os.insert_one(d)
    


# print(qsn)

# lq = qsn.find_all("label")
# la=qsn.find_all("div",class_="toggle-content")

# qalist=[]

# for i in range(50):
#     d = {lq[i].text,la[i].text}
#     qalist.append(d)











