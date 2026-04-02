"""PE2 Topic 10: Basic Networking (Intro)"""

import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Hostname:", hostname)
print("Local IP address:", ip_address)

# Intro task:
# Try replacing 'example.com' with another domain.
domain = "example.com"
print(f"IP of {domain}:", socket.gethostbyname(domain))
