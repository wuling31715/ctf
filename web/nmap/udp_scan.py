import nmap

ip = '192.168.2.0/24'
nm = nmap.PortScanner()
nm.scan(ip, arguments = '-PU')
for host in nm.all_hosts():
    print('---------------')
    print('host: %s' % host)
    print('hostname: %s' % nm[host].hostname())
    print('state: %s' % nm[host].state())

