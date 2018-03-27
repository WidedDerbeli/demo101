import hashlib

def hash(msg):
   return hashlib.md5(msg).digest()
print(hash(b"Hello World"))
print(hash(b"hello every body"))
