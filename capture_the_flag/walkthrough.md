## Task 1

### #1 c4n y0u c4p7u23 7h3 f149?

    can you capture the flag

### #2 01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001

    lets try some binary out!

`python3 1_2.py`

### #3 MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM======

    base32 is super common in CTF's

echo "MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM======" | base32 -d


### #4 RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg==

    Each Base64 digit represents exactly 6 bits of data.

`base64 -d 1_4.enc`

### #5 68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 3f

    hexadecimal or base16?   
 
 `python3 1_5.py`

### #6 Ebgngr zr 13 cynprf!

    Rotate me 13 places!

### ROT13

`echo "Ebgngr zr 13 cynprf!" | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'`

### BSD Games
https://launchpad.net/ubuntu/bionic/amd64/bsdgames/2.17-26build1

### #7 *@F DA:? >6 C:89E C@F?5 323J C:89E C@F?5 Wcf E:>6DX

    You spin me right round baby right round (47 times)

### ROT47

`echo "*@F DA:? >6 C:89E C@F?5 323J C:89E C@F?5 Wcf E:>6DX" | tr '\!-~' 'P-~\!-O'`


### #8 	 - . .-.. . -.-. --- -- -- ..- -. .. -.-. .- - .. --- -. . -. -.-. --- -.. .. -. --.
    
    telecommunication? encoding? 

http://www.unit-conversion.info/texttools/morse-code/


### #9 85 110 112 97 99 107 32 116 104 105 115 32 66 67 68  

    Unpack this BCD

`python3 1_9.py`


### #10 
