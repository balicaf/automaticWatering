# automaticWatering
The goal is to use a wifi/arduino nodemcu to control wirelessly 3 pumps thanks to a relay

3 pumps (5V) are serialized, in order to lift up more water . relay, usb power supply and nodeMCU are put in a 3D printed box (waterproof/ip55)

The Python file is a bot to "smart" control the local hosted website (LAN). It pushes the on button, wait a certain amount of time, then presses the off button.
for mac and firefox, download, right click run, then:
sudo cp geckodriver /usr/local/bin
