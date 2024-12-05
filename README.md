![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white)

# Get IP

## **Description**
This Python script retrieves the local IP address of your machine by establishing a network connection to a DNS server *(Google DNS at 8.8.8.8)*. 
<br>The program attempts to connect to this server and returns the local IP address of the computer. If an error occurs (e.g., network or DNS issues), it handles the exception and displays an error message.

## **Features**
- **IP Address Retrieval** : Gets the local IP address of the machine via a network connection.
- **Error Handling** : Displays an error message if there are connection or DNS issues.
- **Dynamic Display** : Prints the IP address in the console, or a failure message if the retrieval fails.

## **Prerequisites**
- **Python 3.11** installed on your machine
- **Soket** library (usually included in Python standard library).

## **Installation Instructions**

Make sure you have [Python](https://www.python.org/downloads/) installed on your system before running the install command.

1. Clone this repository to your machine.

   ```bash
   git clone https://github.com/0x414854/Get_IP.git
   
2. Once the installation is complete, you're ready to run the program!

   ```bash
   python3 get_IP.py

## **Usage Examples**
- Launch the program by running get_IP.py.
- The script will print the local IP address of your machine if the connection is successful.
- If an error occurs, it will print an error message indicating the issue.
- You can also use the `get_ip_address()` function in your own program.
<br><br>Here’s an example :

```python
from ip_address_retriever import get_ip_address

ip_address = get_ip_address()

if ip_address:
    print(f"Your local IP address is : {ip_address}")
else:
    print("Failed to retrieve the IP address.")
```



  
## Tree Directory

Get_IP/
<br>├── get_IP.py
<br>└── README.md

## **Author**

[**0x414854**](https://github.com/0x414854)
