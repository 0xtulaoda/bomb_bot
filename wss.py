from websocket import create_connection
import json
import pprint

# Initialize the headers needed for the websocket connection

headers = json.dumps({
'Accept - Encoding': 'gzip, deflate, br',
'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'no-cache',
'Connection': 'Upgrade',
'Host': 'server.bombcrypto.io:8443',
'Origin': 'https://app.bombcrypto.io',
'Pragma': 'no-cache',
'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
'Sec-WebSocket-Key': 'jR2Aek3Wfvsr6MDZK4tqRg==',
'Sec-WebSocket-Version': '13',
'Upgrade': 'websocket',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
})
# Then create a connection to the tunnel
ws = create_connection(
    'wss://server.bombcrypto.io:8443/websocket',headers=headers)

# Then send a message through the tunnel
ws.send('{"H":"publicmaphub","M":"getData","A":[],"I":1}')

# Here you will view the message return from the tunnel
while True:
    pprint.pprint(json.loads(ws.recv()))