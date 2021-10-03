from base64 import b64decode
from itertools import cycle

# Google account name (the part before @)
key = "luka.mesaric1".encode()

# encrypted string
message = "F1IYFE0OAAASVUlZEUsSGQRPGUJfQVUKDF0AEAoGWwhCU1tSTgZCGBAODEsJQl9BVQwFVwMHHxIJ "\
"TV9TRhsHAEMJEQIDQghCX0FVCABZBRAdBEMICwdGUlNDFhkbBw5NBgAXRl5JREMNFwkIWh5CU1tS "\
"ThBQChBMTQ5KAxwOVUlZEUsCAg8PShg="

print(''.join([chr(c1 ^ c2) for c1, c2 in zip(b64decode(message), cycle(key))]))

# Output: {'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}
