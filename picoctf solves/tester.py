import random
import string
import binascii

def generate_random_string(length):
    # Combine lowercase, uppercase letters and digits
    characters = string.ascii_letters + string.digits
    # Generate a random string of the specified length
    return ''.join(random.choice(characters) for _ in range(length))

# Generate random strings of lengths 1 to 10
notFound = True
while notFound:
 for length in range(1, 11):
     for i in range(0,100):
         random_string = bytes(generate_random_string(length),'utf-8')
         res = binascii.crc_hqx(random_string,0)
         if(res == 27892):
             notFound = False
             print(f"HIT, {random_string}") 
