from picozero import pico_led
import socket

import network
wlan = network.WLAN(network.STA_IF)
wlan.disconnect()
wlan.active(False)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pico_led.off()
sock.close()
machine.reset()




