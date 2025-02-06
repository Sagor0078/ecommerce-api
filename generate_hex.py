import secrets

# Generate a 16-bit hex value (4 hex characters)
hex_value = secrets.token_hex(16)  # 2 bytes = 16 bits = 4 hex characters
print(hex_value)
