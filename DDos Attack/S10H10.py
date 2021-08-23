from mininet.topo import Topo



class P2PNetwork(Topo):

	def __init__(self):

		Topo.__init__(self)



		firstHost = self.addHost( 'h1' )

		secondHost = self.addHost( 'h2' )

		thirdHost = self.addHost( 'h3' )

		fourthHost = self.addHost( 'h4' )

		fifthHost = self.addHost( 'h5' )

		sixthHost = self.addHost( 'h6' )

		seventhHost = self.addHost( 'h7' )

		eighthHost = self.addHost( 'h8' )

		ninthHost = self.addHost( 'h9' )

		tenthHost = self.addHost( 'h10' )



		switch1 = self.addSwitch( 's1' )

		switch2 = self.addSwitch( 's2' )

		switch3 = self.addSwitch( 's3' )

		switch4 = self.addSwitch( 's4' )

		switch5 = self.addSwitch( 's5' )

		switch6 = self.addSwitch( 's6' )

		switch7 = self.addSwitch( 's7' )

		switch8 = self.addSwitch( 's8' )

		switch9 = self.addSwitch( 's9' )

		switch10 = self.addSwitch( 's10' )



		self.addLink( firstHost, switch1 )

		self.addLink( secondHost, switch2 )

		self.addLink( thirdHost, switch3 )

		self.addLink( fourthHost, switch4 )

		self.addLink( fifthHost, switch5 )

		self.addLink( sixthHost, switch6 )

		self.addLink( seventhHost, switch7 )

		self.addLink( eighthHost, switch8 )

		self.addLink( ninthHost, switch9 )

		self.addLink( tenthHost, switch10 )



		self.addLink( switch1, switch3 )



		self.addLink( switch2, switch10 )



		self.addLink( switch3, switch6 )



		self.addLink( switch4, switch8 )



		self.addLink( switch5, switch7 )

		self.addLink( switch5, switch10 )



		self.addLink( switch6, switch10 )





topos={'P2PNetwork':(lambda:P2PNetwork())}