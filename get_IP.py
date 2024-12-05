import socket

def get_ip_address():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(("8.8.8.8", 80))
            ip_address = s.getsockname()[0]
        except socket.gaierror as e:
            print(f"Error during DNS resolution or network issue: {e}")
            ip_address = None
        except Exception as e:
            print(f"Unexpected error: {e}")
            ip_address = None

    return ip_address

ip_address = get_ip_address()

if ip_address:
    print(f"IP Address: {ip_address}")
else:
    print("Failed to retrieve IP address.")
