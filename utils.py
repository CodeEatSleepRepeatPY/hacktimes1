import hashlib

def hash(plaintxt):
    return hashlib.sha512(str(plaintxt).encode()).hexdigest()
