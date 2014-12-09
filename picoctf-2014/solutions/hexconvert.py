def string_to_bytes(s):
  return [ord(x) for x in s]

def bytes_to_string(b):
  return ''.join(chr(x) for x in b)

def string_to_hex(s):
  return s.encode('hex')

def hex_to_string(s):
  return s.decode('hex')

def bytes_to_hex(b):
  return hex_to_string(bytes_to_string(b))

def hex_to_bytes(s):
  return string_to_bytes(hex_to_string(s))
