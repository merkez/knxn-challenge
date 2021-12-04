# Kinexon custom DNS challenge 



The challenge description was mentioning about creating a VM for DNS queries, however I preferred to do it through [CoreDNS](https://coredns.io/) Docker image. 

What does this [mini script](./main.py) do ?

- Fetches data from given endpoint 
- Formats data as requested 
- Creates zone and Core files for CoreDNS 
- Launchs a bash command through subprocess library of Python

Since I did not use any VM to complete the task, `host` command cannot work as wanted. Instead, I tested the automated script through `dig` tool. 


## How to run

This is pretty straightforward, it is just `python3 main.py`, however in case your environment is missing `python` or `requests` libraries, it may not work as expected. 

In case you need to install `requests` lib :

```bash 
$ pip3 install requests
```
**OR**

```bash 
$ pip3 install -r requirements.txt
```

### Demo 
----

[![asciicast](https://asciinema.org/a/453619.svg)](https://asciinema.org/a/453619)



Once Python script executed, it will automatically create zone and core files along running coredns image with custom settings. 

The DNS Server can be tested through `dig` command as shown below.




## Testing the script 

- Assuming that [./main.py](./main.py) file is run before using `dig` command

```bash 

$ dig @172.17.0.2 customer-one.vpn.knx

; <<>> DiG 9.16.1-Ubuntu <<>> @172.17.0.2 customer-one.vpn.knx
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6695
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: 9c151ecbd69ad1bf (echoed)
;; QUESTION SECTION:
;customer-one.vpn.knx.		IN	A

;; ANSWER SECTION:
customer-one.vpn.knx.	3600	IN	A	10.0.200.1

;; Query time: 0 msec
;; SERVER: 172.17.0.2#53(172.17.0.2)
;; WHEN: Mon Nov 22 16:47:44 UTC 2021
;; MSG SIZE  rcvd: 97

```


NOTE: This is just a **PROOF OF CONCEPT** solution as the task is requested, so, it is **NOT** a perfect or optimum solution.

Since following example is provided in the challenge desc and there was no further information about the rest of the subnet which is left from each customer, I manipulated the data as expected from challenge description by considering the given assumption below. 

```raw
    {“name”: “customer-one”, “subnet”: “10.0.200.0/24"},
    the DNS server should resolve customer-one.vpn.knx to 10.0.200.1
```

The only difference between what the challenge desc requested and what I provided, is Docker component instead of VM and `dig` instead of `host` command. 



