Today I ran my topology using my own P2P messaging app. I made H1 a server. I made H6 and H10 clients. H6 and H10 were messaging each other without any problem. Then I launched a DDoS attack from H3 to H6. I used the following command while performing the attack.“sudo hping3 --faster --rand-source 10.0.0.6” To run this command, I typed it into H3's terminal using xterm. When the attack started, the messaging between H10 and H6 became very slow and some messages did not arrive at all. I used wireshark to examine  port 1 of the H6 using Packages were coming from very different addresses. To prevent the attack, I redirected the flow from H3 to H1 using the controller. In this way, H6 and H10 were able to continue messaging between themselves. H1 server although I directed the DDoS attack there, the network was completely disconnected from the server, but there was no problem in messaging because the structure of the messaging application was P2P. Commands I use when routing a DDoS attack below.


• curl -X POST -d '{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-1", "cookie":"0", "priority":"32768", "in_port":"3","active":"true", "actions":"output=2"}' http://localhost:8080/wm/staticentrypusher/json
• curl -X POST -d '{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-2", "cookie":"0", "priority":"32768", "in_port":"2","active":"true", "actions":"output=3"}' http://localhost:8080/wm/staticentrypusher/json
• curl -X POST -d '{"switch":"00:00:00:00:00:00:00:03", "name":"flow-mod-3", "cookie":"0", "priority":"32768", "in_port":"1","active":"true", "actions":"output=2"}' http://localhost:8080/wm/staticentrypusher/json
• curl -X POST -d '{"switch":"00:00:00:00:00:00:00:03", "name":"flow-mod-4", "cookie":"0", "priority":"32768", "in_port":"2","active":"true", "actions":"output=1"}' http://localhost:8080/wm/staticentrypusher/json


I sent 1000 packets before launching the attack and they all arrived. Then I sent 1000 more packages, without waiting for it to arrive, I sent another 1000 packages. Then 2. My sent 1000 packets arrived  The floodlight turned itself off before 3. 1000 packets arrived. A total of 27,000 packages have moved and I have sent only 3000 of them.

You can find the images and information for this test in attachment.

For bandwith => Bandwith.png
For Graph(udp) => graph1.png
For Graph(udp+all) => graph2.png
For packets and packet data => packets.png
For All addresses => addresses.png

I used the command “sudo hping3 –faster –rand-source 10.0.0.6” to start DDoS.
