import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('MC-Staff', 'SSWst@ff2794!')

# Wait for connection
while not wlan.isconnected():
    time.sleep(1)

print('Connected:', wlan.isconnected())
print('IP Address:', wlan.ifconfig()[0])


