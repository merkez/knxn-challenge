import requests
import subprocess
import os 

cwd=os.getcwd()

url_to_be_requested = "https://download.kinexon.com/vpn_config.json"
parent_domain = "vpn.knx"
zonefile_prefix = """$ORIGIN .
@   3600 IN SOA sns.dns.icann.org. noc.dns.icann.org. (
                2017042745 ; serial
                7200       ; refresh (2 hours)
                3600       ; retry (1 hour)
                1209600    ; expire (2 weeks)
                3600       ; minimum (1 hour)
                )
"""

# this is for other domain names to query from Google DNS server 
corefile_prefix = """.:53 {
    forward . 8.8.8.8 
    log
    errors
}
"""

resp = requests.get(url=url_to_be_requested)
respj = resp.json()

zf = open ("dns/zonefile", "w")
cf = open("dns/Corefile", "w")
zf.write(zonefile_prefix)
cf.write(corefile_prefix)
for i in respj:
    subdomain, ip = i['name'], i['subnet'].replace('0/24','1',1) 
    zf.write('{}.{} IN A {}\n'.format(subdomain, parent_domain,ip))
    cf.write("""{}.{}:53 {{
            file zonefile 
         }}\n""".format(subdomain,parent_domain))
zf.close()        
cf.close()

run_coredns_through_docker = subprocess.run(["docker","run","-d","-v",cwd+"/dns/zonefile:/zonefile","-v", cwd+"/dns/Corefile:/Corefile","coredns/coredns", "--conf","/Corefile"])

