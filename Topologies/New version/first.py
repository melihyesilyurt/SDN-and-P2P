from mininet.topo import Topo

class first(Topo):
    def __init__(self):
        Topo.__init__(self)
        firstHost = self.addHost( 'h1' )
        secondHost = self.addHost( 'h2' )
        thirdHost = self.addHost( 'h3' )
        fourthHost = self.addHost( 'h4' )
        fifthHost = self.addHost( 'h5' )

        switch = self.addSwitch ( 's1' )

        self.addLink( firstHost, switch )
        self.addLink( secondHost, switch )
        self.addLink( thirdHost, switch )
        self.addLink( fourthHost, switch )
        self.addLink( fifthHost, switch )
        
topos={'first':(lambda:first())}