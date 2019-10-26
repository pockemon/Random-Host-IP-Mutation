### save this file in mininet/examples folder
#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

def simpleTest():
    "Create and test a simple network"
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
    
    
    
''''''''''''' Output ''''''''''''''''''
$ sudo python simpletest.py
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 
*** Adding switches:
s1 
*** Adding links:
(h1, s1) (h2, s1) (h3, s1) (h4, s1) 
*** Configuring hosts
h1 h2 h3 h4 
*** Starting controller
c0 
*** Starting 1 switches
s1 ...
Dumping host connections
h1 h1-eth0:s1-eth1
h2 h2-eth0:s1-eth2
h3 h3-eth0:s1-eth3
h4 h4-eth0:s1-eth4
Testing network connectivity
*** Ping: testing ping reachability
h1 -> h2 h3 h4 
h2 -> h1 h3 h4 
h3 -> h1 h2 h4 
h4 -> h1 h2 h3 
*** Results: 0% dropped (12/12 received)
*** Stopping 1 controllers
c0 
*** Stopping 4 links
....
*** Stopping 1 switches
s1 
*** Stopping 4 hosts
h1 h2 h3 h4 
*** Done
''''''''''''''''''''''''''''''''''''''''
