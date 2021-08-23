from mininet.topo import Topo
from mininet.net import Mininet

net = Mininet()
firstHost = net.addHost( 'h1' )
secondHost = net.addHost( 'h2' )
thirdHost = net.addHost( 'h3' )
fourthHost = net.addHost( 'h4' )
fifthHost = net.addHost( 'h5' )

switch = net.addSwitch ( 's1' )

firstHost2 = net.addHost( 'h1_2' )
secondHost2 = net.addHost( 'h2_2' )
thirdHost2 = net.addHost( 'h3_2' )
fourthHost2 = net.addHost( 'h4_2' )
fifthHost2 = net.addHost( 'h5_2' )

switch2 = net.addSwitch( 's1_2' )
c0 =net.addController()

net.addLink( firstHost, switch )
net.addLink( secondHost, switch )
net.addLink( thirdHost, switch )
net.addLink( fourthHost, switch )
net.addLink( fifthHost, switch )

net.addLink( firstHost2, switch2 )
net.addLink( secondHost2, switch2 )
net.addLink( thirdHost2, switch2 )
net.addLink( fourthHost2, switch2 )
net.addLink( fifthHost2, switch2 )

net.addLink( switch, switch2 )

firstHost.setIP('192.168.1.1',24)
secondHost.setIP('192.168.1.2',24)
thirdHost.setIP('192.168.1.3',24)
fourthHost.setIP('192.168.1.4',24)
fifthHost.setIP('192.168.1.5',24)

firstHost2.setIP('192.168.1.6',24)
secondHost2.setIP('192.168.1.7',24)
thirdHost2.setIP('192.168.1.8',24)
fourthHost2.setIP('192.168.1.9',24)
fifthHost2.setIP('192.168.1.10',24)

net.start()
net.pingAll()
net.stop()