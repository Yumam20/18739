import socket

# The string to be sent
message = "The key is jltZxFQgDkqFYSorxmtflgKEk"

# UDP server address and port (example)
server_ip = "128.2.100.168"  # Use the desired IP address or 'localhost'
server_port = 12345       # Use the desired port

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Loop through each character in the message and send it 3 times
for char in message:
    for _ in range(3):  # Send each character 3 times
        # Send the character (encoded as bytes)
        sock.sendto(char.encode(), (server_ip, server_port))

# Close the socket
sock.close()

print(f"Sent message: '{message}' three times per character.")
