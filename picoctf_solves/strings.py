import base64

def decode_base64_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        base64_lines = file.readlines()
    
    with open(output_filename, 'w') as output_file:
        for base64_line in base64_lines:
            # Strip any newline or extra spaces
            base64_line = base64_line.strip()
            try:
                # Decode the base64 string and write the result as a decoded string
                decoded_bytes = base64.b64decode(base64_line)
                decoded_string = decoded_bytes.decode('utf-8')
                output_file.write(decoded_string + '\n')
            except Exception as e:
                # If an error occurs, write an error message to the output file
                output_file.write(f"Error decoding: {e}\n")

    print(f"Decoded strings have been written to {output_filename}")

# Example usage:
input_filename = 'encoded_input.txt'  # Replace with your input file name (base64 encoded)
output_filename = 'decoded_output2.txt'  # Replace with your desired output file name
decode_base64_file('strings.txt', output_filename)
