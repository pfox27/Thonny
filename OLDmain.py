import network
import socket
import time
from machine import Pin

# Wi-Fi credentials
ssid = 'MC-Staff'
password = 'SSWst@ff2794!'

# Onboard LED pin (use this or an external LED)
led = Pin('LED', Pin.OUT) 

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print(f'Connected on {status[0]}') #

# HTML content for the web page
def get_html(led_state):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pico W Web Server</title>
    </head>
    <body>
        <h1>Pico W LED Control</h1>
        <p>LED state: {led_state}</p>
        <a href="/?led=on">Turn LED On</a>
        <a href="/?led=off">Turn LED Off</a>
    </body>
    </html>
    """
    return html

# Open a socket and listen for requests
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = str(request)
    
    # Check for LED control requests
    if '/?led=on' in request:
        led.value(1)
    elif '/?led=off' in request:
        led.value(0)
        
    # Serve the web page
    response = get_html("on" if led.value() else "off")
    conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    conn.send(response)
    conn.close()



