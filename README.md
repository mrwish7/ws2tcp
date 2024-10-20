# ws2tcp
A Python websocket to TCP server to enable forwarding RDS data from FM-DX-Webserver to RDS Spy

## Pre-requisites 
- Python3
- Python `websocket-client` library
  
  ```
  pip install websocket-client
  ```

## Instructions
- In the terminal, navigate to the folder containing the script and run -
  
  ```
  python3 ws2tcp.py
  ```
- Optional command-line arguments -
  - `-W`, `--websocket`

    Set RDS websocket address for the FM-DX webserver that you want to receive RDS data from (**default:** `ws://127.0.0.1:8080/rdsspy`)
  - `-I`, `--server-ip`

    Set IP address/interface for the forwarding TCP server (**default:** 0.0.0.0)
  - `-P`, `--server-port`

    Set port number for the forwarding TCP server (**default:** 7373)

  For example -

  ```
  python3 ws2tcp.py -W ws://remoteserver.example:12340/rds -I 127.0.0.1 -P 5678
  ```

 - Once the server is started, open RDS Spy to start receiving RDS data. RDS Spy must be configured for TCP input, on the interface and port that you have specified to the Python script.
 - Once finished, in Windows you will probably need to close the terminal to stop the service, as it ignores keyboard interrupts.
